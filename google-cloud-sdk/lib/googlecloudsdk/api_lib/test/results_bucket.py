# Copyright 2015 Google Inc. All Rights Reserved.

"""Utility methods to aid in interacting with a GCS results bucket."""

import os

from googlecloudsdk.api_lib.test import util
from googlecloudsdk.calliope import exceptions
from googlecloudsdk.core import log
from googlecloudsdk.core import resources
from googlecloudsdk.third_party.apis.storage import v1 as storage_v1
from googlecloudsdk.third_party.apitools.base import py as apitools_base


GCS_PREFIX = 'gs://'
ERROR_NOTFOUND = 404
FORBIDDEN = 403


class ResultsBucketOps(object):
  """A utility class to encapsulate operations on the results bucket."""

  def __init__(self, project, bucket_name, unique_obj_name,
               tr_client, tr_messages, storage_client):
    """Construct a ResultsBucketOps object to be used with a single matrix run.

    Args:
      project: string containing the Google Developers Console project id.
      bucket_name: string with the user-supplied name of a GCS bucket, or None.
      unique_obj_name: the name of a unique GCS object to hold the raw test
        results within the supplied bucket_name.
      tr_client: ToolResults API client library generated by Apitools.
      tr_messages: ToolResults API messages library generated by Apitools.
      storage_client: Cloud Storage API client library generated by Apitools.

    Attributes:
      gcs_results_root: string containing the root path for the test results in
        'gs://{bucket}/{timestamp-suffix}' format.
    """
    self._project = project
    self._storage_client = storage_client
    self._gcs_object_name = unique_obj_name

    # If the user supplied a results bucket, make sure it exists. Otherwise,
    # call the SettingsService to get the project's existing default bucket.
    if bucket_name:
      self.EnsureBucketExists(bucket_name)
    else:
      bucket_name = self._GetDefaultBucket(tr_client, tr_messages)

    bucket_ref = resources.Parse(bucket_name, collection='storage.buckets')
    self._results_bucket = bucket_ref.bucket

    self._gcs_results_url = (
        'https://console.developers.google.com/storage/browser/{b}/{t}/'
        .format(b=bucket_name, t=self._gcs_object_name))
    self.gcs_results_root = ('gs://{b}/{t}/'
                             .format(b=bucket_name, t=self._gcs_object_name))
    log.info('Raw results root path is: [{0}]'.format(self.gcs_results_root))

  def _GetDefaultBucket(self, tr_client, tr_messages):
    """Fetch the project's default GCS bucket name for storing tool results."""
    request = tr_messages.ToolresultsProjectsInitializeSettingsRequest(
        projectId=self._project)
    try:
      response = tr_client.projects.InitializeSettings(request)
      return response.defaultBucket.decode('utf8')
    except apitools_base.HttpError as error:
      code, err_msg = util.GetErrorCodeAndMessage(error)
      if code == FORBIDDEN:
        msg = ('Permission denied while fetching the default results bucket. '
               'Is billing enabled for project: [{0}]?'
               .format(self._project))
      else:
        msg = ('Http error while trying to fetch the default results bucket:\n'
               'ResponseError {0}: {1}'
               .format(code, err_msg))
      raise exceptions.HttpException(msg)

  def EnsureBucketExists(self, bucket_name):
    """Create a GCS bucket if it doesn't already exist.

    Args:
      bucket_name: the name of the GCS bucket to create if it doesn't exist.

    Raises:
      BadFileException if the bucket name is malformed, the user does not
        have access rights to the bucket, or the bucket can't be created.
    """
    get_req = storage_v1.StorageBucketsGetRequest(bucket=bucket_name)
    try:
      self._storage_client.buckets.Get(get_req)
      return  # The bucket exists and the user can access it.
    except apitools_base.HttpError as err:
      code, err_msg = util.GetErrorCodeAndMessage(err)
      if code != ERROR_NOTFOUND:
        raise exceptions.BadFileException(
            'Could not access bucket [{b}]. Response error {c}: {e}. '
            'Please supply a valid bucket name or use the default bucket '
            'provided by Google Cloud Test Lab.'
            .format(b=bucket_name, c=code, e=err_msg))

    # The bucket does not exist in any project, so create it in user's project.
    log.status.Print('Creating results bucket [{g}{b}] in project [{p}].'
                     .format(g=GCS_PREFIX, b=bucket_name, p=self._project))

    bucket_req = storage_v1.StorageBucketsInsertRequest
    acl = bucket_req.PredefinedAclValueValuesEnum.projectPrivate
    objacl = bucket_req.PredefinedDefaultObjectAclValueValuesEnum.projectPrivate

    insert_req = storage_v1.StorageBucketsInsertRequest(
        bucket=storage_v1.Bucket(name=bucket_name),
        predefinedAcl=acl,
        predefinedDefaultObjectAcl=objacl,
        project=self._project)
    try:
      self._storage_client.buckets.Insert(insert_req)
      return
    except apitools_base.HttpError as err:

      code, err_msg = util.GetErrorCodeAndMessage(err)
      if code == FORBIDDEN:
        msg = ('Permission denied while creating bucket [{b}]. '
               'Is billing enabled for project: [{p}]?'
               .format(b=bucket_name, p=self._project))
      else:
        msg = ('Failed to create bucket [{b}] {e}'
               .format(b=bucket_name, e=util.GetError(err)))
      raise exceptions.BadFileException(msg)

  def UploadFileToGcs(self, path):
    """Upload a file to the GCS results bucket using the storage API.

    Args:
      path: str, the absolute or relative path of the file to upload. File
        may be in located in GCS or the local filesystem.

    Raises:
      BadFileException if the file upload is not successful.
    """
    log.status.Print('Uploading [{f}] to the Cloud Test Lab...'.format(f=path))
    try:
      if path.startswith(GCS_PREFIX):
        # Perform a GCS object to GCS object copy
        file_bucket, file_obj = _SplitBucketAndObject(path)
        copy_req = storage_v1.StorageObjectsCopyRequest(
            sourceBucket=file_bucket,
            sourceObject=file_obj,
            destinationBucket=self._results_bucket,
            destinationObject='{obj}/{name}'.format(
                obj=self._gcs_object_name, name=os.path.basename(file_obj)))
        self._storage_client.objects.Copy(copy_req)
      else:
        # Perform a GCS insert of a file which is not in GCS
        try:
          file_size = os.path.getsize(path)
          file_stream = open(path, 'r')
        except os.error:
          raise exceptions.BadFileException('[{0}] not found or not accessible'
                                            .format(path))
        src_obj = storage_v1.Object(size=file_size)
        upload = apitools_base.Upload.FromStream(
            file_stream,
            mime_type='application/vnd.android.package-archive',
            total_size=file_size)
        insert_req = storage_v1.StorageObjectsInsertRequest(
            bucket=self._results_bucket,
            name='{obj}/{name}'.format(obj=self._gcs_object_name,
                                       name=os.path.basename(path)),
            object=src_obj)
        self._storage_client.objects.Insert(insert_req, upload=upload)
    except apitools_base.HttpError as err:
      raise exceptions.BadFileException(
          'Could not copy [{f}] to [{gcs}] {e}.'
          .format(f=path, gcs=self.gcs_results_root, e=util.GetError(err)))

  def LogGcsResultsUrl(self):
    log.status.Print('Raw results will be stored in your GCS bucket at [{0}]\n'
                     .format(self._gcs_results_url))


def _SplitBucketAndObject(gcs_path):
  """Split a GCS path into bucket & object tokens, or raise BadFileException."""
  tokens = gcs_path[len(GCS_PREFIX):].strip('/').split('/', 1)
  if len(tokens) != 2:
    raise exceptions.BadFileException(
        '[{0}] is not a valid Google Cloud Storage path'.format(gcs_path))
  return tokens
