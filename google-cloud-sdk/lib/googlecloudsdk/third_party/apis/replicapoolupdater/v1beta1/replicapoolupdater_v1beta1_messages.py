"""Generated message classes for replicapoolupdater version v1beta1.

Updates groups of Compute Engine instances.
"""
# NOTE: This file is autogenerated and should not be edited by hand.

from apitools.base.protorpclite import messages as _messages


package = 'replicapoolupdater'


class InstanceUpdate(_messages.Message):
  """Update of a single instance.

  Messages:
    ErrorValue: Errors that occurred during the instance update.

  Fields:
    error: Errors that occurred during the instance update.
    instance: Fully-qualified URL of the instance being updated.
    status: Status of the instance update. Possible values are:   - "PENDING":
      The instance update is pending execution.  - "ROLLING_FORWARD": The
      instance update is going forward.  - "ROLLING_BACK": The instance update
      is being rolled back.  - "PAUSED": The instance update is temporarily
      paused (inactive).  - "ROLLED_OUT": The instance update is finished, the
      instance is running the new template.  - "ROLLED_BACK": The instance
      update is finished, the instance has been reverted to the previous
      template.  - "CANCELLED": The instance update is paused and no longer
      can be resumed, undefined in which template the instance is running.
  """

  class ErrorValue(_messages.Message):
    """Errors that occurred during the instance update.

    Messages:
      ErrorsValueListEntry: A ErrorsValueListEntry object.

    Fields:
      errors: [Output Only] The array of errors encountered while processing
        this operation.
    """

    class ErrorsValueListEntry(_messages.Message):
      """A ErrorsValueListEntry object.

      Fields:
        code: [Output Only] The error type identifier for this error.
        location: [Output Only] Indicates the field in the request that caused
          the error. This property is optional.
        message: [Output Only] An optional, human-readable error message.
      """

      code = _messages.StringField(1)
      location = _messages.StringField(2)
      message = _messages.StringField(3)

    errors = _messages.MessageField('ErrorsValueListEntry', 1, repeated=True)

  error = _messages.MessageField('ErrorValue', 1)
  instance = _messages.StringField(2)
  status = _messages.StringField(3)


class InstanceUpdateList(_messages.Message):
  """Response returned by ListInstanceUpdates method.

  Fields:
    items: Collection of requested instance updates.
    kind: [Output Only] Type of the resource.
    nextPageToken: A token used to continue a truncated list request.
    selfLink: [Output Only] The fully qualified URL for the resource.
  """

  items = _messages.MessageField('InstanceUpdate', 1, repeated=True)
  kind = _messages.StringField(2, default=u'replicapoolupdater#instanceUpdateList')
  nextPageToken = _messages.StringField(3)
  selfLink = _messages.StringField(4)


class Operation(_messages.Message):
  """An operation resource, used to manage asynchronous API requests.

  Messages:
    ErrorValue: [Output Only] If errors occurred during processing of this
      operation, this field will be populated.
    WarningsValueListEntry: A WarningsValueListEntry object.

  Fields:
    clientOperationId: A string attribute.
    creationTimestamp: [Output Only] Creation timestamp in RFC3339 text
      format.
    endTime: A string attribute.
    error: [Output Only] If errors occurred during processing of this
      operation, this field will be populated.
    httpErrorMessage: A string attribute.
    httpErrorStatusCode: A integer attribute.
    id: [Output Only] Unique identifier for the resource; defined by the
      server.
    insertTime: [Output Only] The time that this operation was requested. This
      is in RFC 3339 format.
    kind: [Output Only] Type of the resource. Always
      replicapoolupdater#operation for Operation resources.
    name: [Output Only] Name of the resource.
    operationType: A string attribute.
    progress: A integer attribute.
    region: [Output Only] URL of the region where the operation resides.
    selfLink: [Output Only] The fully qualified URL for the resource.
    startTime: [Output Only] The time that this operation was started by the
      server. This is in RFC 3339 format.
    status: [Output Only] Status of the operation. Can be one of the
      following: "PENDING", "RUNNING", or "DONE".
    statusMessage: [Output Only] An optional textual description of the
      current status of the operation.
    targetId: [Output Only] Unique target id which identifies a particular
      incarnation of the target.
    targetLink: [Output Only] URL of the resource the operation is mutating.
    user: A string attribute.
    warnings: A WarningsValueListEntry attribute.
    zone: [Output Only] URL of the zone where the operation resides.
  """

  class ErrorValue(_messages.Message):
    """[Output Only] If errors occurred during processing of this operation,
    this field will be populated.

    Messages:
      ErrorsValueListEntry: A ErrorsValueListEntry object.

    Fields:
      errors: [Output Only] The array of errors encountered while processing
        this operation.
    """

    class ErrorsValueListEntry(_messages.Message):
      """A ErrorsValueListEntry object.

      Fields:
        code: [Output Only] The error type identifier for this error.
        location: [Output Only] Indicates the field in the request that caused
          the error. This property is optional.
        message: [Output Only] An optional, human-readable error message.
      """

      code = _messages.StringField(1)
      location = _messages.StringField(2)
      message = _messages.StringField(3)

    errors = _messages.MessageField('ErrorsValueListEntry', 1, repeated=True)

  class WarningsValueListEntry(_messages.Message):
    """A WarningsValueListEntry object.

    Messages:
      DataValueListEntry: A DataValueListEntry object.

    Fields:
      code: [Output only] The warning type identifier for this warning.
      data: [Output only] Metadata for this warning in key:value format.
      message: [Output only] Optional human-readable details for this warning.
    """

    class DataValueListEntry(_messages.Message):
      """A DataValueListEntry object.

      Fields:
        key: [Output Only] Metadata key for this warning.
        value: [Output Only] Metadata value for this warning.
      """

      key = _messages.StringField(1)
      value = _messages.StringField(2)

    code = _messages.StringField(1)
    data = _messages.MessageField('DataValueListEntry', 2, repeated=True)
    message = _messages.StringField(3)

  clientOperationId = _messages.StringField(1)
  creationTimestamp = _messages.StringField(2)
  endTime = _messages.StringField(3)
  error = _messages.MessageField('ErrorValue', 4)
  httpErrorMessage = _messages.StringField(5)
  httpErrorStatusCode = _messages.IntegerField(6, variant=_messages.Variant.INT32)
  id = _messages.IntegerField(7, variant=_messages.Variant.UINT64)
  insertTime = _messages.StringField(8)
  kind = _messages.StringField(9, default=u'replicapoolupdater#operation')
  name = _messages.StringField(10)
  operationType = _messages.StringField(11)
  progress = _messages.IntegerField(12, variant=_messages.Variant.INT32)
  region = _messages.StringField(13)
  selfLink = _messages.StringField(14)
  startTime = _messages.StringField(15)
  status = _messages.StringField(16)
  statusMessage = _messages.StringField(17)
  targetId = _messages.IntegerField(18, variant=_messages.Variant.UINT64)
  targetLink = _messages.StringField(19)
  user = _messages.StringField(20)
  warnings = _messages.MessageField('WarningsValueListEntry', 21, repeated=True)
  zone = _messages.StringField(22)


class OperationList(_messages.Message):
  """Contains a list of Operation resources.

  Fields:
    id: [Output Only] Unique identifier for the resource; defined by the
      server.
    items: [Output Only] The Operation resources.
    kind: [Output Only] Type of resource. Always
      replicapoolupdater#operationList for OperationList resources.
    nextPageToken: [Output Only] A token used to continue a truncate.
    selfLink: [Output Only] The fully qualified URL for the resource.
  """

  id = _messages.StringField(1)
  items = _messages.MessageField('Operation', 2, repeated=True)
  kind = _messages.StringField(3, default=u'replicapoolupdater#operationList')
  nextPageToken = _messages.StringField(4)
  selfLink = _messages.StringField(5)


class ReplicapoolupdaterRollingUpdatesCancelRequest(_messages.Message):
  """A ReplicapoolupdaterRollingUpdatesCancelRequest object.

  Fields:
    project: The Google Developers Console project name.
    rollingUpdate: The name of the update.
    zone: The name of the zone in which the update's target resides.
  """

  project = _messages.StringField(1, required=True)
  rollingUpdate = _messages.StringField(2, required=True)
  zone = _messages.StringField(3, required=True)


class ReplicapoolupdaterRollingUpdatesGetRequest(_messages.Message):
  """A ReplicapoolupdaterRollingUpdatesGetRequest object.

  Fields:
    project: The Google Developers Console project name.
    rollingUpdate: The name of the update.
    zone: The name of the zone in which the update's target resides.
  """

  project = _messages.StringField(1, required=True)
  rollingUpdate = _messages.StringField(2, required=True)
  zone = _messages.StringField(3, required=True)


class ReplicapoolupdaterRollingUpdatesInsertRequest(_messages.Message):
  """A ReplicapoolupdaterRollingUpdatesInsertRequest object.

  Fields:
    project: The Google Developers Console project name.
    rollingUpdate: A RollingUpdate resource to be passed as the request body.
    zone: The name of the zone in which the update's target resides.
  """

  project = _messages.StringField(1, required=True)
  rollingUpdate = _messages.MessageField('RollingUpdate', 2)
  zone = _messages.StringField(3, required=True)


class ReplicapoolupdaterRollingUpdatesListInstanceUpdatesRequest(_messages.Message):
  """A ReplicapoolupdaterRollingUpdatesListInstanceUpdatesRequest object.

  Fields:
    filter: Optional. Filter expression for filtering listed resources.
    maxResults: Optional. Maximum count of results to be returned. Maximum
      value is 500 and default value is 500.
    pageToken: Optional. Tag returned by a previous list request truncated by
      maxResults. Used to continue a previous list request.
    project: The Google Developers Console project name.
    rollingUpdate: The name of the update.
    zone: The name of the zone in which the update's target resides.
  """

  filter = _messages.StringField(1)
  maxResults = _messages.IntegerField(2, variant=_messages.Variant.UINT32, default=500)
  pageToken = _messages.StringField(3)
  project = _messages.StringField(4, required=True)
  rollingUpdate = _messages.StringField(5, required=True)
  zone = _messages.StringField(6, required=True)


class ReplicapoolupdaterRollingUpdatesListRequest(_messages.Message):
  """A ReplicapoolupdaterRollingUpdatesListRequest object.

  Fields:
    filter: Optional. Filter expression for filtering listed resources.
    maxResults: Optional. Maximum count of results to be returned. Maximum
      value is 500 and default value is 500.
    pageToken: Optional. Tag returned by a previous list request truncated by
      maxResults. Used to continue a previous list request.
    project: The Google Developers Console project name.
    zone: The name of the zone in which the update's target resides.
  """

  filter = _messages.StringField(1)
  maxResults = _messages.IntegerField(2, variant=_messages.Variant.UINT32, default=500)
  pageToken = _messages.StringField(3)
  project = _messages.StringField(4, required=True)
  zone = _messages.StringField(5, required=True)


class ReplicapoolupdaterRollingUpdatesPauseRequest(_messages.Message):
  """A ReplicapoolupdaterRollingUpdatesPauseRequest object.

  Fields:
    project: The Google Developers Console project name.
    rollingUpdate: The name of the update.
    zone: The name of the zone in which the update's target resides.
  """

  project = _messages.StringField(1, required=True)
  rollingUpdate = _messages.StringField(2, required=True)
  zone = _messages.StringField(3, required=True)


class ReplicapoolupdaterRollingUpdatesResumeRequest(_messages.Message):
  """A ReplicapoolupdaterRollingUpdatesResumeRequest object.

  Fields:
    project: The Google Developers Console project name.
    rollingUpdate: The name of the update.
    zone: The name of the zone in which the update's target resides.
  """

  project = _messages.StringField(1, required=True)
  rollingUpdate = _messages.StringField(2, required=True)
  zone = _messages.StringField(3, required=True)


class ReplicapoolupdaterRollingUpdatesRollbackRequest(_messages.Message):
  """A ReplicapoolupdaterRollingUpdatesRollbackRequest object.

  Fields:
    project: The Google Developers Console project name.
    rollingUpdate: The name of the update.
    zone: The name of the zone in which the update's target resides.
  """

  project = _messages.StringField(1, required=True)
  rollingUpdate = _messages.StringField(2, required=True)
  zone = _messages.StringField(3, required=True)


class ReplicapoolupdaterZoneOperationsGetRequest(_messages.Message):
  """A ReplicapoolupdaterZoneOperationsGetRequest object.

  Fields:
    operation: Name of the operation resource to return.
    project: Name of the project scoping this request.
    zone: Name of the zone scoping this request.
  """

  operation = _messages.StringField(1, required=True)
  project = _messages.StringField(2, required=True)
  zone = _messages.StringField(3, required=True)


class ReplicapoolupdaterZoneOperationsListRequest(_messages.Message):
  """A ReplicapoolupdaterZoneOperationsListRequest object.

  Fields:
    filter: Optional. Filter expression for filtering listed resources.
    maxResults: Optional. Maximum count of results to be returned. Maximum
      value is 500 and default value is 500.
    pageToken: Optional. Tag returned by a previous list request truncated by
      maxResults. Used to continue a previous list request.
    project: Name of the project scoping this request.
    zone: Name of the zone scoping this request.
  """

  filter = _messages.StringField(1)
  maxResults = _messages.IntegerField(2, variant=_messages.Variant.UINT32, default=500)
  pageToken = _messages.StringField(3)
  project = _messages.StringField(4, required=True)
  zone = _messages.StringField(5, required=True)


class RollingUpdate(_messages.Message):
  """The following represents a resource describing a single update (rollout)
  of a group of instances to the given template.

  Messages:
    ErrorValue: [Output Only] Errors that occurred during the rolling update.
    PolicyValue: Parameters of the update process.

  Fields:
    actionType: Specifies the action to take for each instance within the
      instance group. This can be RECREATE which will recreate each instance
      and is only available for managed instance groups. It can also be REBOOT
      which performs a soft reboot for each instance and is only available for
      regular (non-managed) instance groups.
    creationTimestamp: [Output Only] Creation timestamp in RFC3339 text
      format.
    description: An optional textual description of the resource; provided by
      the client when the resource is created.
    error: [Output Only] Errors that occurred during the rolling update.
    id: [Output Only] Unique identifier for the resource; defined by the
      server.
    instanceGroup: Fully-qualified URL of an instance group being updated.
      Exactly one of instanceGroupManager and instanceGroup must be set.
    instanceGroupManager: Fully-qualified URL of an instance group manager
      being updated. Exactly one of instanceGroupManager and instanceGroup
      must be set.
    instanceTemplate: Fully-qualified URL of an instance template to apply.
    kind: [Output Only] Type of the resource.
    oldInstanceTemplate: Fully-qualified URL of the instance template
      encountered while starting the update.
    policy: Parameters of the update process.
    progress: [Output Only] An optional progress indicator that ranges from 0
      to 100. There is no requirement that this be linear or support any
      granularity of operations. This should not be used to guess at when the
      update will be complete. This number should be monotonically increasing
      as the update progresses.
    selfLink: [Output Only] The fully qualified URL for the resource.
    status: [Output Only] Status of the update. Possible values are:   -
      "ROLLING_FORWARD": The update is going forward.  - "ROLLING_BACK": The
      update is being rolled back.  - "PAUSED": The update is temporarily
      paused (inactive).  - "ROLLED_OUT": The update is finished, all
      instances have been updated successfully.  - "ROLLED_BACK": The update
      is finished, all instances have been reverted to the previous template.
      - "CANCELLED": The update is paused and no longer can be resumed,
      undefined how many instances are running in which template.
    statusMessage: [Output Only] An optional textual description of the
      current status of the update.
    user: [Output Only] User who requested the update, for example:
      user@example.com.
  """

  class ErrorValue(_messages.Message):
    """[Output Only] Errors that occurred during the rolling update.

    Messages:
      ErrorsValueListEntry: A ErrorsValueListEntry object.

    Fields:
      errors: [Output Only] The array of errors encountered while processing
        this operation.
    """

    class ErrorsValueListEntry(_messages.Message):
      """A ErrorsValueListEntry object.

      Fields:
        code: [Output Only] The error type identifier for this error.
        location: [Output Only] Indicates the field in the request that caused
          the error. This property is optional.
        message: [Output Only] An optional, human-readable error message.
      """

      code = _messages.StringField(1)
      location = _messages.StringField(2)
      message = _messages.StringField(3)

    errors = _messages.MessageField('ErrorsValueListEntry', 1, repeated=True)

  class PolicyValue(_messages.Message):
    """Parameters of the update process.

    Fields:
      autoPauseAfterInstances: Number of instances to update before the
        updater pauses the rolling update.
      instanceStartupTimeoutSec: The maximum amount of time that the updater
        waits for a HEALTHY state after all of the update steps are complete.
        If the HEALTHY state is not received before the deadline, the instance
        update is considered a failure.
      maxNumConcurrentInstances: The maximum number of instances that can be
        updated simultaneously. An instance update is considered complete only
        after the instance is restarted and initialized.
      maxNumFailedInstances: The maximum number of instance updates that can
        fail before the group update is considered a failure. An instance
        update is considered failed if any of its update actions (e.g. Stop
        call on Instance resource in Rolling Reboot) failed with permanent
        failure, or if the instance is in an UNHEALTHY state after it finishes
        all of the update actions.
      minInstanceUpdateTimeSec: The minimum amount of time that the updater
        spends to update each instance. Update time is the time it takes to
        complete all update actions (e.g. Stop call on Instance resource in
        Rolling Reboot), reboot, and initialize. If the instance update
        finishes early, the updater pauses for the remainder of the time
        before it starts the next instance update.
    """

    autoPauseAfterInstances = _messages.IntegerField(1, variant=_messages.Variant.INT32)
    instanceStartupTimeoutSec = _messages.IntegerField(2, variant=_messages.Variant.INT32)
    maxNumConcurrentInstances = _messages.IntegerField(3, variant=_messages.Variant.INT32)
    maxNumFailedInstances = _messages.IntegerField(4, variant=_messages.Variant.INT32)
    minInstanceUpdateTimeSec = _messages.IntegerField(5, variant=_messages.Variant.INT32)

  actionType = _messages.StringField(1)
  creationTimestamp = _messages.StringField(2)
  description = _messages.StringField(3)
  error = _messages.MessageField('ErrorValue', 4)
  id = _messages.StringField(5)
  instanceGroup = _messages.StringField(6)
  instanceGroupManager = _messages.StringField(7)
  instanceTemplate = _messages.StringField(8)
  kind = _messages.StringField(9, default=u'replicapoolupdater#rollingUpdate')
  oldInstanceTemplate = _messages.StringField(10)
  policy = _messages.MessageField('PolicyValue', 11)
  progress = _messages.IntegerField(12, variant=_messages.Variant.INT32)
  selfLink = _messages.StringField(13)
  status = _messages.StringField(14)
  statusMessage = _messages.StringField(15)
  user = _messages.StringField(16)


class RollingUpdateList(_messages.Message):
  """Response returned by List method.

  Fields:
    items: Collection of requested updates.
    kind: [Output Only] Type of the resource.
    nextPageToken: A token used to continue a truncated list request.
    selfLink: [Output Only] The fully qualified URL for the resource.
  """

  items = _messages.MessageField('RollingUpdate', 1, repeated=True)
  kind = _messages.StringField(2, default=u'replicapoolupdater#rollingUpdateList')
  nextPageToken = _messages.StringField(3)
  selfLink = _messages.StringField(4)


class StandardQueryParameters(_messages.Message):
  """Query parameters accepted by all methods.

  Enums:
    AltValueValuesEnum: Data format for the response.

  Fields:
    alt: Data format for the response.
    fields: Selector specifying which fields to include in a partial response.
    key: API key. Your API key identifies your project and provides you with
      API access, quota, and reports. Required unless you provide an OAuth 2.0
      token.
    oauth_token: OAuth 2.0 token for the current user.
    prettyPrint: Returns response with indentations and line breaks.
    quotaUser: Available to use for quota purposes for server-side
      applications. Can be any arbitrary string assigned to a user, but should
      not exceed 40 characters. Overrides userIp if both are provided.
    trace: A tracing token of the form "token:<tokenid>" to include in api
      requests.
    userIp: IP address of the site where the request originates. Use this if
      you want to enforce per-user limits.
  """

  class AltValueValuesEnum(_messages.Enum):
    """Data format for the response.

    Values:
      json: Responses with Content-Type of application/json
    """
    json = 0

  alt = _messages.EnumField('AltValueValuesEnum', 1, default=u'json')
  fields = _messages.StringField(2)
  key = _messages.StringField(3)
  oauth_token = _messages.StringField(4)
  prettyPrint = _messages.BooleanField(5, default=True)
  quotaUser = _messages.StringField(6)
  trace = _messages.StringField(7)
  userIp = _messages.StringField(8)


