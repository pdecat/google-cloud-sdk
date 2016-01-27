"""Generated message classes for cloudbuild version v1.

The Google Cloud Container Builder API lets you build container images in the
cloud.
"""
# NOTE: This file is autogenerated and should not be edited by hand.

from googlecloudsdk.third_party.apitools.base.protorpclite import messages as _messages
from googlecloudsdk.third_party.apitools.base.py import encoding


package = 'cloudbuild'


class Build(_messages.Message):
  """A build resource in the Container Builder API.  At a high level, a Build
  describes where to find source code, how to build it (for example, the
  builder image to run on the source), and what tag to apply to the built
  image when it is pushed to Google Container Registry.

  Enums:
    StatusValueValuesEnum: Status of the build. @OutputOnly

  Fields:
    createTime: Time at which the build was created. @OutputOnly
    finishTime: Time at whihc execution of the build was finished. @OutputOnly
    id: Unique identifier of the build. @OutputOnly
    images: List of images expected to be built and pushed to Google Container
      Registry. If an image is listed here and the image is not produced by
      one of the build steps, the build will fail. Any images present when the
      build steps are complete will be pushed to Container Registry.
    logsBucket: Google Cloud Storage bucket where logs should be written (see
      [Bucket Name Requirements](https://cloud.google.com/storage/docs/bucket-
      naming#requirements)). Logs file names will be of the format
      `${logs_bucket}/log-${build_id}.txt`.
    projectId: ID of the project. @OutputOnly.
    results: Results of the build. @OutputOnly
    source: Describes where to find the source files to build.
    startTime: Time at which execution of the build was started. @OutputOnly
    status: Status of the build. @OutputOnly
    steps: Describes the operations to be performed on the workspace.
    timeout: Amount of time that this build should be allowed to run, to
      second granularity. If this amount of time elapses, work on the build
      will cease and the build status will be TIMEOUT.  Default time is ten
      minutes.
  """

  class StatusValueValuesEnum(_messages.Enum):
    """Status of the build. @OutputOnly

    Values:
      STATUS_UNKNOWN: Status of the build is unknown.
      QUEUED: Build is queued, work has not yet begun.
      WORKING: Build is being executed.
      SUCCESS: Build finished successfully.
      FAILURE: Build failed to complete successfully.
      INTERNAL_ERROR: Build failed due to an internal cause.
      TIMEOUT: Build took longer than was allowed.
      CANCELLED: Build was canceled by a user.
    """
    STATUS_UNKNOWN = 0
    QUEUED = 1
    WORKING = 2
    SUCCESS = 3
    FAILURE = 4
    INTERNAL_ERROR = 5
    TIMEOUT = 6
    CANCELLED = 7

  createTime = _messages.StringField(1)
  finishTime = _messages.StringField(2)
  id = _messages.StringField(3)
  images = _messages.StringField(4, repeated=True)
  logsBucket = _messages.StringField(5)
  projectId = _messages.StringField(6)
  results = _messages.MessageField('Results', 7)
  source = _messages.MessageField('Source', 8)
  startTime = _messages.StringField(9)
  status = _messages.EnumField('StatusValueValuesEnum', 10)
  steps = _messages.MessageField('BuildStep', 11, repeated=True)
  timeout = _messages.StringField(12)


class BuildOperationMetadata(_messages.Message):
  """Metadata for build operations.

  Fields:
    build: The build that the operation is tracking.
  """

  build = _messages.MessageField('Build', 1)


class BuildStep(_messages.Message):
  """BuildStep describes a step to perform in the build pipeline.

  Fields:
    args: Command-line arguments to use when running this step's container.
    dir: Working directory (relative to project source root) to use when
      running this operation's container.
    env: Additional environment variables to set for this step's container.
    name: Name of the container image to use for creating this stage in the
      pipeline, as presented to `docker pull`.
  """

  args = _messages.StringField(1, repeated=True)
  dir = _messages.StringField(2)
  env = _messages.StringField(3, repeated=True)
  name = _messages.StringField(4)


class BuiltImage(_messages.Message):
  """BuiltImage describes an image built by the pipeline.

  Fields:
    digest: Docker Registry 2.0 digest.
    name: Name used to push the container image to Google Container Registry,
      as presented to `docker push`.
  """

  digest = _messages.StringField(1)
  name = _messages.StringField(2)


class CancelBuildRequest(_messages.Message):
  """Request to cancel an ongoing build."""


class CloudbuildOperationsGetRequest(_messages.Message):
  """A CloudbuildOperationsGetRequest object.

  Fields:
    name: The name of the operation resource.
  """

  name = _messages.StringField(1, required=True)


class CloudbuildOperationsListRequest(_messages.Message):
  """A CloudbuildOperationsListRequest object.

  Fields:
    filter: The standard list filter.
    name: The name of the operation collection.
    pageSize: The standard list page size.
    pageToken: The standard list page token.
  """

  filter = _messages.StringField(1)
  name = _messages.StringField(2, required=True)
  pageSize = _messages.IntegerField(3, variant=_messages.Variant.INT32)
  pageToken = _messages.StringField(4)


class CloudbuildProjectsBuildsCancelRequest(_messages.Message):
  """A CloudbuildProjectsBuildsCancelRequest object.

  Fields:
    cancelBuildRequest: A CancelBuildRequest resource to be passed as the
      request body.
    id: ID of the build.
    projectId: ID of the project.
  """

  cancelBuildRequest = _messages.MessageField('CancelBuildRequest', 1)
  id = _messages.StringField(2, required=True)
  projectId = _messages.StringField(3, required=True)


class CloudbuildProjectsBuildsCreateRequest(_messages.Message):
  """A CloudbuildProjectsBuildsCreateRequest object.

  Fields:
    build: A Build resource to be passed as the request body.
    projectId: ID of the project.
  """

  build = _messages.MessageField('Build', 1)
  projectId = _messages.StringField(2, required=True)


class CloudbuildProjectsBuildsGetRequest(_messages.Message):
  """A CloudbuildProjectsBuildsGetRequest object.

  Fields:
    id: ID of the build.
    projectId: ID of the project.
  """

  id = _messages.StringField(1, required=True)
  projectId = _messages.StringField(2, required=True)


class CloudbuildProjectsBuildsListRequest(_messages.Message):
  """A CloudbuildProjectsBuildsListRequest object.

  Fields:
    pageSize: Number of results to return in the list.
    pageToken: Token to provide to skip to a particular spot in the list.
    projectId: ID of the project.
  """

  pageSize = _messages.IntegerField(1, variant=_messages.Variant.INT32)
  pageToken = _messages.StringField(2)
  projectId = _messages.StringField(3, required=True)


class ListBuildsResponse(_messages.Message):
  """Response including listed builds.

  Fields:
    builds: Builds will be sorted by create_time, descending.
    nextPageToken: Token to receive the next page of results.
  """

  builds = _messages.MessageField('Build', 1, repeated=True)
  nextPageToken = _messages.StringField(2)


class ListOperationsResponse(_messages.Message):
  """The response message for Operations.ListOperations.

  Fields:
    nextPageToken: The standard List next-page token.
    operations: A list of operations that matches the specified filter in the
      request.
  """

  nextPageToken = _messages.StringField(1)
  operations = _messages.MessageField('Operation', 2, repeated=True)


class Operation(_messages.Message):
  """This resource represents a long-running operation that is the result of a
  network API call.

  Messages:
    MetadataValue: Service-specific metadata associated with the operation.
      It typically contains progress information and common metadata such as
      create time. Some services might not provide such metadata.  Any method
      that returns a long-running operation should document the metadata type,
      if any.
    ResponseValue: The normal response of the operation in case of success.
      If the original method returns no data on success, such as `Delete`, the
      response is `google.protobuf.Empty`.  If the original method is standard
      `Get`/`Create`/`Update`, the response should be the resource.  For other
      methods, the response should have the type `XxxResponse`, where `Xxx` is
      the original method name.  For example, if the original method name is
      `TakeSnapshot()`, the inferred response type is `TakeSnapshotResponse`.

  Fields:
    done: If the value is `false`, it means the operation is still in
      progress. If true, the operation is completed, and either `error` or
      `response` is available.
    error: The error result of the operation in case of failure.
    metadata: Service-specific metadata associated with the operation.  It
      typically contains progress information and common metadata such as
      create time. Some services might not provide such metadata.  Any method
      that returns a long-running operation should document the metadata type,
      if any.
    name: The server-assigned name, which is only unique within the same
      service that originally returns it. If you use the default HTTP mapping
      above, the `name` should have the format of
      `operations/some/unique/name`.
    response: The normal response of the operation in case of success.  If the
      original method returns no data on success, such as `Delete`, the
      response is `google.protobuf.Empty`.  If the original method is standard
      `Get`/`Create`/`Update`, the response should be the resource.  For other
      methods, the response should have the type `XxxResponse`, where `Xxx` is
      the original method name.  For example, if the original method name is
      `TakeSnapshot()`, the inferred response type is `TakeSnapshotResponse`.
  """

  @encoding.MapUnrecognizedFields('additionalProperties')
  class MetadataValue(_messages.Message):
    """Service-specific metadata associated with the operation.  It typically
    contains progress information and common metadata such as create time.
    Some services might not provide such metadata.  Any method that returns a
    long-running operation should document the metadata type, if any.

    Messages:
      AdditionalProperty: An additional property for a MetadataValue object.

    Fields:
      additionalProperties: Properties of the object. Contains field @ype with
        type URL.
    """

    class AdditionalProperty(_messages.Message):
      """An additional property for a MetadataValue object.

      Fields:
        key: Name of the additional property.
        value: A extra_types.JsonValue attribute.
      """

      key = _messages.StringField(1)
      value = _messages.MessageField('extra_types.JsonValue', 2)

    additionalProperties = _messages.MessageField('AdditionalProperty', 1, repeated=True)

  @encoding.MapUnrecognizedFields('additionalProperties')
  class ResponseValue(_messages.Message):
    """The normal response of the operation in case of success.  If the
    original method returns no data on success, such as `Delete`, the response
    is `google.protobuf.Empty`.  If the original method is standard
    `Get`/`Create`/`Update`, the response should be the resource.  For other
    methods, the response should have the type `XxxResponse`, where `Xxx` is
    the original method name.  For example, if the original method name is
    `TakeSnapshot()`, the inferred response type is `TakeSnapshotResponse`.

    Messages:
      AdditionalProperty: An additional property for a ResponseValue object.

    Fields:
      additionalProperties: Properties of the object. Contains field @ype with
        type URL.
    """

    class AdditionalProperty(_messages.Message):
      """An additional property for a ResponseValue object.

      Fields:
        key: Name of the additional property.
        value: A extra_types.JsonValue attribute.
      """

      key = _messages.StringField(1)
      value = _messages.MessageField('extra_types.JsonValue', 2)

    additionalProperties = _messages.MessageField('AdditionalProperty', 1, repeated=True)

  done = _messages.BooleanField(1)
  error = _messages.MessageField('Status', 2)
  metadata = _messages.MessageField('MetadataValue', 3)
  name = _messages.StringField(4)
  response = _messages.MessageField('ResponseValue', 5)


class Results(_messages.Message):
  """Results describes the artifacts created by the build pipeline.

  Fields:
    images: Images that were built as a part of the build.
    revision: Revision ID of the source that was built.
  """

  images = _messages.MessageField('BuiltImage', 1, repeated=True)
  revision = _messages.StringField(2)


class Source(_messages.Message):
  """Source describes the location of the source in a supported storage
  service.

  Fields:
    storageSource: If provided, get the source from this location in in Google
      Cloud Storage.
  """

  storageSource = _messages.MessageField('StorageSource', 1)


class StandardQueryParameters(_messages.Message):
  """Query parameters accepted by all methods.

  Enums:
    FXgafvValueValuesEnum: V1 error format.
    AltValueValuesEnum: Data format for response.

  Fields:
    f__xgafv: V1 error format.
    access_token: OAuth access token.
    alt: Data format for response.
    bearer_token: OAuth bearer token.
    callback: JSONP
    fields: Selector specifying which fields to include in a partial response.
    key: API key. Your API key identifies your project and provides you with
      API access, quota, and reports. Required unless you provide an OAuth 2.0
      token.
    oauth_token: OAuth 2.0 token for the current user.
    pp: Pretty-print response.
    prettyPrint: Returns response with indentations and line breaks.
    quotaUser: Available to use for quota purposes for server-side
      applications. Can be any arbitrary string assigned to a user, but should
      not exceed 40 characters.
    trace: A tracing token of the form "token:<tokenid>" to include in api
      requests.
    uploadType: Legacy upload protocol for media (e.g. "media", "multipart").
    upload_protocol: Upload protocol for media (e.g. "raw", "multipart").
  """

  class AltValueValuesEnum(_messages.Enum):
    """Data format for response.

    Values:
      json: Responses with Content-Type of application/json
      media: Media download with context-dependent Content-Type
      proto: Responses with Content-Type of application/x-protobuf
    """
    json = 0
    media = 1
    proto = 2

  class FXgafvValueValuesEnum(_messages.Enum):
    """V1 error format.

    Values:
      _1: v1 error format
      _2: v2 error format
    """
    _1 = 0
    _2 = 1

  f__xgafv = _messages.EnumField('FXgafvValueValuesEnum', 1)
  access_token = _messages.StringField(2)
  alt = _messages.EnumField('AltValueValuesEnum', 3, default=u'json')
  bearer_token = _messages.StringField(4)
  callback = _messages.StringField(5)
  fields = _messages.StringField(6)
  key = _messages.StringField(7)
  oauth_token = _messages.StringField(8)
  pp = _messages.BooleanField(9, default=True)
  prettyPrint = _messages.BooleanField(10, default=True)
  quotaUser = _messages.StringField(11)
  trace = _messages.StringField(12)
  uploadType = _messages.StringField(13)
  upload_protocol = _messages.StringField(14)


class Status(_messages.Message):
  """The `Status` type defines a logical error model that is suitable for
  different programming environments, including REST APIs and RPC APIs. It is
  used by [gRPC](https://github.com/grpc). The error model is designed to be:
  - Simple to use and understand for most users - Flexible enough to meet
  unexpected needs  # Overview  The `Status` message contains three pieces of
  data: error code, error message, and error details. The error code should be
  an enum value of google.rpc.Code, but it may accept additional error codes
  if needed.  The error message should be a developer-facing English message
  that helps developers *understand* and *resolve* the error. If a localized
  user-facing error message is needed, put the localized message in the error
  details or localize it in the client. The optional error details may contain
  arbitrary information about the error. There is a predefined set of error
  detail types in the package `google.rpc` which can be used for common error
  conditions.  # Language mapping  The `Status` message is the logical
  representation of the error model, but it is not necessarily the actual wire
  format. When the `Status` message is exposed in different client libraries
  and different wire protocols, it can be mapped differently. For example, it
  will likely be mapped to some exceptions in Java, but more likely mapped to
  some error codes in C.  # Other uses  The error model and the `Status`
  message can be used in a variety of environments, either with or without
  APIs, to provide a consistent developer experience across different
  environments.  Example uses of this error model include:  - Partial errors.
  If a service needs to return partial errors to the client,     it may embed
  the `Status` in the normal response to indicate the partial     errors.  -
  Workflow errors. A typical workflow has multiple steps. Each step may
  have a `Status` message for error reporting purpose.  - Batch operations. If
  a client uses batch request and batch response, the     `Status` message
  should be used directly inside batch response, one for     each error sub-
  response.  - Asynchronous operations. If an API call embeds asynchronous
  operation     results in its response, the status of those operations should
  be     represented directly using the `Status` message.  - Logging. If some
  API errors are stored in logs, the message `Status` could     be used
  directly after any stripping needed for security/privacy reasons.

  Messages:
    DetailsValueListEntry: A DetailsValueListEntry object.

  Fields:
    code: The status code, which should be an enum value of google.rpc.Code.
    details: A list of messages that carry the error details.  There will be a
      common set of message types for APIs to use.
    message: A developer-facing error message, which should be in English. Any
      user-facing error message should be localized and sent in the
      google.rpc.Status.details field, or localized by the client.
  """

  @encoding.MapUnrecognizedFields('additionalProperties')
  class DetailsValueListEntry(_messages.Message):
    """A DetailsValueListEntry object.

    Messages:
      AdditionalProperty: An additional property for a DetailsValueListEntry
        object.

    Fields:
      additionalProperties: Properties of the object. Contains field @ype with
        type URL.
    """

    class AdditionalProperty(_messages.Message):
      """An additional property for a DetailsValueListEntry object.

      Fields:
        key: Name of the additional property.
        value: A extra_types.JsonValue attribute.
      """

      key = _messages.StringField(1)
      value = _messages.MessageField('extra_types.JsonValue', 2)

    additionalProperties = _messages.MessageField('AdditionalProperty', 1, repeated=True)

  code = _messages.IntegerField(1, variant=_messages.Variant.INT32)
  details = _messages.MessageField('DetailsValueListEntry', 2, repeated=True)
  message = _messages.StringField(3)


class StorageSource(_messages.Message):
  """StorageSource describes the location of the source in an archive file in
  Google Cloud Storage.

  Fields:
    bucket: Google Cloud Storage bucket containing source (see [Bucket Name
      Requirements](https://cloud.google.com/storage/docs/bucket-
      naming#requirements)).
    object: Google Cloud Storage object containing source.  This object must
      be a gzipped archive file (.tgz) containing source to build.
  """

  bucket = _messages.StringField(1)
  object = _messages.StringField(2)


encoding.AddCustomJsonFieldMapping(
    StandardQueryParameters, 'f__xgafv', '$.xgafv',
    package=u'cloudbuild')
encoding.AddCustomJsonEnumMapping(
    StandardQueryParameters.FXgafvValueValuesEnum, '_1', '1',
    package=u'cloudbuild')
encoding.AddCustomJsonEnumMapping(
    StandardQueryParameters.FXgafvValueValuesEnum, '_2', '2',
    package=u'cloudbuild')
