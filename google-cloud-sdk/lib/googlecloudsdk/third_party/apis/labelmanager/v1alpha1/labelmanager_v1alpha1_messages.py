"""Generated message classes for labelmanager version v1alpha1.

The Label Manager API allows users to create and manage definitions of labels
across the Cloud Resource Hierarchy. With these user-provided definitions, the
API can provide the applicable label definitions for a resource based on its
hierarchical position.
"""
# NOTE: This file is autogenerated and should not be edited by hand.

from apitools.base.protorpclite import messages as _messages
from apitools.base.py import encoding
from apitools.base.py import extra_types


package = 'labelmanager'


class AuditConfig(_messages.Message):
  r"""Specifies the audit configuration for a service. The configuration
  determines which permission types are logged, and what identities, if any,
  are exempted from logging. An AuditConfig must have one or more
  AuditLogConfigs.  If there are AuditConfigs for both `allServices` and a
  specific service, the union of the two AuditConfigs is used for that
  service: the log_types specified in each AuditConfig are enabled, and the
  exempted_members in each AuditLogConfig are exempted.  Example Policy with
  multiple AuditConfigs:      {       "audit_configs": [         {
  "service": "allServices"           "audit_log_configs": [             {
  "log_type": "DATA_READ",               "exempted_members": [
  "user:jose@example.com"               ]             },             {
  "log_type": "DATA_WRITE",             },             {
  "log_type": "ADMIN_READ",             }           ]         },         {
  "service": "sampleservice.googleapis.com"           "audit_log_configs": [
  {               "log_type": "DATA_READ",             },             {
  "log_type": "DATA_WRITE",               "exempted_members": [
  "user:aliya@example.com"               ]             }           ]         }
  ]     }  For sampleservice, this policy enables DATA_READ, DATA_WRITE and
  ADMIN_READ logging. It also exempts jose@example.com from DATA_READ logging,
  and aliya@example.com from DATA_WRITE logging.

  Fields:
    auditLogConfigs: The configuration for logging of each type of permission.
    service: Specifies a service that will be enabled for audit logging. For
      example, `storage.googleapis.com`, `cloudsql.googleapis.com`.
      `allServices` is a special value that covers all services.
  """

  auditLogConfigs = _messages.MessageField('AuditLogConfig', 1, repeated=True)
  service = _messages.StringField(2)


class AuditLogConfig(_messages.Message):
  r"""Provides the configuration for logging a type of permissions. Example:
  {       "audit_log_configs": [         {           "log_type": "DATA_READ",
  "exempted_members": [             "user:jose@example.com"           ]
  },         {           "log_type": "DATA_WRITE",         }       ]     }
  This enables 'DATA_READ' and 'DATA_WRITE' logging, while exempting
  jose@example.com from DATA_READ logging.

  Enums:
    LogTypeValueValuesEnum: The log type that this config enables.

  Fields:
    exemptedMembers: Specifies the identities that do not cause logging for
      this type of permission. Follows the same format of Binding.members.
    logType: The log type that this config enables.
  """

  class LogTypeValueValuesEnum(_messages.Enum):
    r"""The log type that this config enables.

    Values:
      LOG_TYPE_UNSPECIFIED: Default case. Should never be this.
      ADMIN_READ: Admin reads. Example: CloudIAM getIamPolicy
      DATA_WRITE: Data writes. Example: CloudSQL Users create
      DATA_READ: Data reads. Example: CloudSQL Users list
    """
    LOG_TYPE_UNSPECIFIED = 0
    ADMIN_READ = 1
    DATA_WRITE = 2
    DATA_READ = 3

  exemptedMembers = _messages.StringField(1, repeated=True)
  logType = _messages.EnumField('LogTypeValueValuesEnum', 2)


class Binding(_messages.Message):
  r"""Associates `members` with a `role`.

  Fields:
    condition: The condition that is associated with this binding. NOTE: An
      unsatisfied condition will not allow user access via current binding.
      Different bindings, including their conditions, are examined
      independently.
    members: Specifies the identities requesting access for a Cloud Platform
      resource. `members` can have the following values:  * `allUsers`: A
      special identifier that represents anyone who is    on the internet;
      with or without a Google account.  * `allAuthenticatedUsers`: A special
      identifier that represents anyone    who is authenticated with a Google
      account or a service account.  * `user:{emailid}`: An email address that
      represents a specific Google    account. For example,
      `alice@example.com` .   * `serviceAccount:{emailid}`: An email address
      that represents a service    account. For example, `my-other-
      app@appspot.gserviceaccount.com`.  * `group:{emailid}`: An email address
      that represents a Google group.    For example, `admins@example.com`.
      * `domain:{domain}`: The G Suite domain (primary) that represents all
      the    users of that domain. For example, `google.com` or `example.com`.
    role: Role that is assigned to `members`. For example, `roles/viewer`,
      `roles/editor`, or `roles/owner`.
  """

  condition = _messages.MessageField('Expr', 1)
  members = _messages.StringField(2, repeated=True)
  role = _messages.StringField(3)


class CreateLabelBindingRequest(_messages.Message):
  r"""The request message to create a binding.

  Fields:
    labelBinding: The binding to be created.
  """

  labelBinding = _messages.MessageField('LabelBinding', 1)


class Empty(_messages.Message):
  r"""A generic empty message that you can re-use to avoid defining duplicated
  empty messages in your APIs. A typical example is to use it as the request
  or the response type of an API method. For instance:      service Foo {
  rpc Bar(google.protobuf.Empty) returns (google.protobuf.Empty);     }  The
  JSON representation for `Empty` is empty JSON object `{}`.
  """



class Expr(_messages.Message):
  r"""Represents an expression text. Example:      title: "User account
  presence"     description: "Determines whether the request has a user
  account"     expression: "size(request.user) > 0"

  Fields:
    description: An optional description of the expression. This is a longer
      text which describes the expression, e.g. when hovered over it in a UI.
    expression: Textual representation of an expression in Common Expression
      Language syntax.  The application context of the containing message
      determines which well-known feature set of CEL is supported.
    location: An optional string indicating the location of the expression for
      error reporting, e.g. a file name and a position in the file.
    title: An optional title for the expression, i.e. a short string
      describing its purpose. This can be used e.g. in UIs which allow to
      enter the expression.
  """

  description = _messages.StringField(1)
  expression = _messages.StringField(2)
  location = _messages.StringField(3)
  title = _messages.StringField(4)


class LabelBinding(_messages.Message):
  r"""A Binding represents a connection between a label value and a cloud
  resource. Once a binding is created the label value is applied to all the
  descendents of the cloud resource. The label binding is owned by the label
  value.

  Fields:
    labelValue: The label value of the binding. Must be of the form
      "labelValues/456.
    resource: The full resource name of the node the label is bound to. E.g.
      //library.googleapis.com/shelves/shelf1/books/book2" E.g.
      //cloudresourcemanager.googleapis.com/organizations/123
  """

  labelValue = _messages.StringField(1)
  resource = _messages.StringField(2)


class LabelKey(_messages.Message):
  r"""A label key, used to group a set of label values.

  Enums:
    StateValueValuesEnum: Output only. Label key lifecycle state.

  Fields:
    createTime: Output only.
    deleteTime: Output only.
    description: Optional user-assigned description of the label key. Must not
      exceed 256 characters.  Read-write.
    displayName: Required user-assigned display name for label key. Display
      name should be unique for label keys within the same parent resource.
      The display name must be 1-63 characters, beginning and ending with an
      alphanumeric character ([a-z0-9A-Z]) with dashes (-), underscores (_),
      dots (.), and alphanumerics between.  Read-write.
    etag: Entity tag passed to prevent race conditions. Always set in server
      responses, and optionally set by user for UpdateLabelKey. See
      UpdateLabelKeyRequest for details.
    name: Resource name for label key. Must be in the format labelKeys/123.
      Immutable.
    parent: The resource name of the new label key's parent. Must be of the
      form `folders/{folder_id}` or `organizations/{org_id}`.  Immutable.
    state: Output only. Label key lifecycle state.
  """

  class StateValueValuesEnum(_messages.Enum):
    r"""Output only. Label key lifecycle state.

    Values:
      LIFECYCLE_STATE_UNSPECIFIED: Unspecified state.  This is only
        used/useful for distinguishing unset values.
      ACTIVE: The normal and active state.
      DELETE_REQUESTED: The label key  has been marked for deletion by the
        user (by invoking: DeleteLabelKey) or by the system (Google Cloud
        Platform).  This can generally be reversed by invoking:
        [google.labelmanager.v1alpha1.LabelManager.UndeleteLabelKey]
    """
    LIFECYCLE_STATE_UNSPECIFIED = 0
    ACTIVE = 1
    DELETE_REQUESTED = 2

  createTime = _messages.StringField(1)
  deleteTime = _messages.StringField(2)
  description = _messages.StringField(3)
  displayName = _messages.StringField(4)
  etag = _messages.StringField(5)
  name = _messages.StringField(6)
  parent = _messages.StringField(7)
  state = _messages.EnumField('StateValueValuesEnum', 8)


class LabelValue(_messages.Message):
  r"""A label value is a child of a particular label key. This is used to
  group cloud resources for the purpose of controlling them via policies.

  Enums:
    StateValueValuesEnum: Output only. Label value lifecycle state.

  Fields:
    createTime: Output only. Creation time.
    deleteTime: Output only.
    description: Optional user-assigned description of the label key. Must not
      exceed 256 characters.  Read-write.
    displayName: Required user-assigned display name for label value. Display
      name should be unique for label values within the same parent label key.
      The display name must be 63 characters or less, beginning and ending
      with an alphanumeric character ([a-z0-9A-Z]) with dashes (-),
      underscores (_), dots (.), and alphanumerics between.  Read-write.
    etag: Entity tag passed to prevent race conditions. Always set in server
      responses, and optionally set by user for UpdateLabelValue. See
      UpdateLabelValueRequest for details.
    name: Resource name for label value in the format labelValues/456.
      Immutable.
    parent: The resource name of the new label value's parent label key. Must
      be of the form `labelKeys/{label_key_id}`.  Immutable.
    state: Output only. Label value lifecycle state.
  """

  class StateValueValuesEnum(_messages.Enum):
    r"""Output only. Label value lifecycle state.

    Values:
      LIFECYCLE_STATE_UNSPECIFIED: Unspecified state.  This is only
        used/useful for distinguishing unset values.
      ACTIVE: The normal and active state.
      DELETE_REQUESTED: The label key or value has been marked for deletion by
        the user (by invoking: DeleteLabelValue) or by the system (Google
        Cloud Platform).  This can generally be reversed by invoking:
        [google.labelmanager.v1alpha1.LabelManager.UndeleteLabelValue]
    """
    LIFECYCLE_STATE_UNSPECIFIED = 0
    ACTIVE = 1
    DELETE_REQUESTED = 2

  createTime = _messages.StringField(1)
  deleteTime = _messages.StringField(2)
  description = _messages.StringField(3)
  displayName = _messages.StringField(4)
  etag = _messages.StringField(5)
  name = _messages.StringField(6)
  parent = _messages.StringField(7)
  state = _messages.EnumField('StateValueValuesEnum', 8)


class LabelmanagerLabelKeysDeleteRequest(_messages.Message):
  r"""A LabelmanagerLabelKeysDeleteRequest object.

  Fields:
    name: Resource name for label key to be deleted in the format
      labelKeys/123. The label key cannot be a parent of any label values to
      be deleted successfully.
  """

  name = _messages.StringField(1, required=True)


class LabelmanagerLabelKeysGetIamPolicyRequest(_messages.Message):
  r"""A LabelmanagerLabelKeysGetIamPolicyRequest object.

  Fields:
    options_requestedPolicyVersion: Optional. The policy format version to be
      returned.  Valid values are 0, 1, and 3. Requests specifying an invalid
      value will be rejected.  Requests for policies with any conditional
      bindings must specify version 3. Policies without any conditional
      bindings may specify any valid value or leave the field unset.
    resource: REQUIRED: The resource for which the policy is being requested.
      See the operation documentation for the appropriate value for this
      field.
  """

  options_requestedPolicyVersion = _messages.IntegerField(1, variant=_messages.Variant.INT32)
  resource = _messages.StringField(2, required=True)


class LabelmanagerLabelKeysGetRequest(_messages.Message):
  r"""A LabelmanagerLabelKeysGetRequest object.

  Fields:
    name: Resource name for label key to be fetched in the format
      labelKeys/123.
  """

  name = _messages.StringField(1, required=True)


class LabelmanagerLabelKeysListRequest(_messages.Message):
  r"""A LabelmanagerLabelKeysListRequest object.

  Fields:
    pageSize: The maximum number of label keys to return in the response. This
      field is optional. This is currently not used by the server and will
      return the full page even if a size is specified currently.
    pageToken: A pagination token returned from a previous call to
      `ListLabelKey` that indicates where this listing should continue from.
      This is currently not used by the server. This field is optional.
    parent: The resource name of the new label key's parent. Must be of the
      form `folders/{folder_id}` or `organizations/{org_id}`.
  """

  pageSize = _messages.IntegerField(1, variant=_messages.Variant.INT32)
  pageToken = _messages.StringField(2)
  parent = _messages.StringField(3)


class LabelmanagerLabelKeysPatchRequest(_messages.Message):
  r"""A LabelmanagerLabelKeysPatchRequest object.

  Fields:
    labelKey: A LabelKey resource to be passed as the request body.
    name: Resource name for label key. Must be in the format labelKeys/123.
      Immutable.
    updateMask: Fields to be updated
  """

  labelKey = _messages.MessageField('LabelKey', 1)
  name = _messages.StringField(2, required=True)
  updateMask = _messages.StringField(3)


class LabelmanagerLabelKeysSetIamPolicyRequest(_messages.Message):
  r"""A LabelmanagerLabelKeysSetIamPolicyRequest object.

  Fields:
    resource: REQUIRED: The resource for which the policy is being specified.
      See the operation documentation for the appropriate value for this
      field.
    setIamPolicyRequest: A SetIamPolicyRequest resource to be passed as the
      request body.
  """

  resource = _messages.StringField(1, required=True)
  setIamPolicyRequest = _messages.MessageField('SetIamPolicyRequest', 2)


class LabelmanagerLabelKeysTestIamPermissionsRequest(_messages.Message):
  r"""A LabelmanagerLabelKeysTestIamPermissionsRequest object.

  Fields:
    resource: REQUIRED: The resource for which the policy detail is being
      requested. See the operation documentation for the appropriate value for
      this field.
    testIamPermissionsRequest: A TestIamPermissionsRequest resource to be
      passed as the request body.
  """

  resource = _messages.StringField(1, required=True)
  testIamPermissionsRequest = _messages.MessageField('TestIamPermissionsRequest', 2)


class LabelmanagerLabelKeysUndeleteRequest(_messages.Message):
  r"""A LabelmanagerLabelKeysUndeleteRequest object.

  Fields:
    name: Resource name for label key to be un-deleted in the format
      labelKeys/123.
    undeleteLabelKeyRequest: A UndeleteLabelKeyRequest resource to be passed
      as the request body.
  """

  name = _messages.StringField(1, required=True)
  undeleteLabelKeyRequest = _messages.MessageField('UndeleteLabelKeyRequest', 2)


class LabelmanagerLabelValuesDeleteLabelBindingsRequest(_messages.Message):
  r"""A LabelmanagerLabelValuesDeleteLabelBindingsRequest object.

  Fields:
    labelBinding_labelValue: The label value of the binding. Must be of the
      form "labelValues/456.
    labelBinding_resource: The full resource name of the node the label is
      bound to. E.g. //library.googleapis.com/shelves/shelf1/books/book2" E.g.
      //cloudresourcemanager.googleapis.com/organizations/123
    labelValuesId: A string attribute.
  """

  labelBinding_labelValue = _messages.StringField(1)
  labelBinding_resource = _messages.StringField(2)
  labelValuesId = _messages.StringField(3, required=True)


class LabelmanagerLabelValuesDeleteRequest(_messages.Message):
  r"""A LabelmanagerLabelValuesDeleteRequest object.

  Fields:
    name: Resource name for label value to be deleted in the format
      labelValues/456.
  """

  name = _messages.StringField(1, required=True)


class LabelmanagerLabelValuesGetRequest(_messages.Message):
  r"""A LabelmanagerLabelValuesGetRequest object.

  Fields:
    name: Resource name for label value to be fetched in the format
      labelValues/456.
  """

  name = _messages.StringField(1, required=True)


class LabelmanagerLabelValuesLabelBindingsCreateRequest(_messages.Message):
  r"""A LabelmanagerLabelValuesLabelBindingsCreateRequest object.

  Fields:
    createLabelBindingRequest: A CreateLabelBindingRequest resource to be
      passed as the request body.
    labelValuesId: A string attribute.
  """

  createLabelBindingRequest = _messages.MessageField('CreateLabelBindingRequest', 1)
  labelValuesId = _messages.StringField(2, required=True)


class LabelmanagerLabelValuesLabelBindingsListRequest(_messages.Message):
  r"""A LabelmanagerLabelValuesLabelBindingsListRequest object.

  Fields:
    label: The name of the label value should be of the form "labelvalues/123"
    labelValuesId: A string attribute.
    pageSize: The maximum number of bindingss to return in the response. This
      field is optional. This is currently not used by the server and will
      return the full page even if a size is specified currently.
    pageToken: A pagination token returned from a previous call to
      `ListLabelBindings` that indicates where this listing should continue
      from. This is currently not used by the server. This field is optional.
    resource: The full name of the resource should be of the form "type/id".
      E.g. E.g. //library.googleapis.com/shelves/shelf1/books/book2" E.g.
      //cloudresourcemanager.googleapis.com/organizations/123
  """

  label = _messages.StringField(1)
  labelValuesId = _messages.StringField(2, required=True)
  pageSize = _messages.IntegerField(3, variant=_messages.Variant.INT32)
  pageToken = _messages.StringField(4)
  resource = _messages.StringField(5)


class LabelmanagerLabelValuesListRequest(_messages.Message):
  r"""A LabelmanagerLabelValuesListRequest object.

  Fields:
    pageSize: The maximum number of label values to return in the response.
      This field is optional. This is currently not used by the server and
      will return the full page even if a size is specified currently.
    pageToken: A pagination token returned from a previous call to
      `ListLabelValues` that indicates where this listing should continue
      from. This is currently not used by the server.  This field is optional.
    parent: Resource name for label key, parent of the label values to be
      listed, in the format labelKeys/123.
  """

  pageSize = _messages.IntegerField(1, variant=_messages.Variant.INT32)
  pageToken = _messages.StringField(2)
  parent = _messages.StringField(3)


class LabelmanagerLabelValuesPatchRequest(_messages.Message):
  r"""A LabelmanagerLabelValuesPatchRequest object.

  Fields:
    labelValue: A LabelValue resource to be passed as the request body.
    name: Resource name for label value in the format labelValues/456.
      Immutable.
    updateMask: Fields to be updated.
  """

  labelValue = _messages.MessageField('LabelValue', 1)
  name = _messages.StringField(2, required=True)
  updateMask = _messages.StringField(3)


class LabelmanagerLabelValuesUndeleteRequest(_messages.Message):
  r"""A LabelmanagerLabelValuesUndeleteRequest object.

  Fields:
    name: Resource name for label value to be un-deleted in the format
      labelValues/456.
    undeleteLabelValueRequest: A UndeleteLabelValueRequest resource to be
      passed as the request body.
  """

  name = _messages.StringField(1, required=True)
  undeleteLabelValueRequest = _messages.MessageField('UndeleteLabelValueRequest', 2)


class ListLabelBindingsResponse(_messages.Message):
  r"""The ListLabelBindings response

  Fields:
    bindings: A possibly paginated list of bindings for the specified label
      value or resource.
    nextPageToken: A pagination token returned from a previous call to
      `ListLabelBindings` that indicates from where listing should continue.
      This is currently not used, but the server may at any point start
      supplying a valid token. This field is optional.
  """

  bindings = _messages.MessageField('LabelBinding', 1, repeated=True)
  nextPageToken = _messages.StringField(2)


class ListLabelKeysResponse(_messages.Message):
  r"""The ListLabelKeys response message.

  Fields:
    keys: List of label keys that live under the specified parent in the
      request.
    nextPageToken: A pagination token returned from a previous call to
      `ListLabelKeys` that indicates from where listing should continue. This
      is currently not used, but the server may at any point start supplying a
      valid token. This field is optional.
  """

  keys = _messages.MessageField('LabelKey', 1, repeated=True)
  nextPageToken = _messages.StringField(2)


class ListLabelValuesResponse(_messages.Message):
  r"""The ListLabelValues response.

  Fields:
    nextPageToken: A pagination token returned from a previous call to
      `ListLabelValues` that indicates from where listing should continue.
      This is currently not used, but the server may at any point start
      supplying a valid token. This field is optional.
    values: A possibly paginated list of labels that are direct descendants of
      the specified parent label key.
  """

  nextPageToken = _messages.StringField(1)
  values = _messages.MessageField('LabelValue', 2, repeated=True)


class Operation(_messages.Message):
  r"""This resource represents a long-running operation that is the result of
  a network API call.

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
      progress. If `true`, the operation is completed, and either `error` or
      `response` is available.
    error: The error result of the operation in case of failure or
      cancellation.
    metadata: Service-specific metadata associated with the operation.  It
      typically contains progress information and common metadata such as
      create time. Some services might not provide such metadata.  Any method
      that returns a long-running operation should document the metadata type,
      if any.
    name: The server-assigned name, which is only unique within the same
      service that originally returns it. If you use the default HTTP mapping,
      the `name` should be a resource name ending with
      `operations/{unique_id}`.
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
    r"""Service-specific metadata associated with the operation.  It typically
    contains progress information and common metadata such as create time.
    Some services might not provide such metadata.  Any method that returns a
    long-running operation should document the metadata type, if any.

    Messages:
      AdditionalProperty: An additional property for a MetadataValue object.

    Fields:
      additionalProperties: Properties of the object. Contains field @type
        with type URL.
    """

    class AdditionalProperty(_messages.Message):
      r"""An additional property for a MetadataValue object.

      Fields:
        key: Name of the additional property.
        value: A extra_types.JsonValue attribute.
      """

      key = _messages.StringField(1)
      value = _messages.MessageField('extra_types.JsonValue', 2)

    additionalProperties = _messages.MessageField('AdditionalProperty', 1, repeated=True)

  @encoding.MapUnrecognizedFields('additionalProperties')
  class ResponseValue(_messages.Message):
    r"""The normal response of the operation in case of success.  If the
    original method returns no data on success, such as `Delete`, the response
    is `google.protobuf.Empty`.  If the original method is standard
    `Get`/`Create`/`Update`, the response should be the resource.  For other
    methods, the response should have the type `XxxResponse`, where `Xxx` is
    the original method name.  For example, if the original method name is
    `TakeSnapshot()`, the inferred response type is `TakeSnapshotResponse`.

    Messages:
      AdditionalProperty: An additional property for a ResponseValue object.

    Fields:
      additionalProperties: Properties of the object. Contains field @type
        with type URL.
    """

    class AdditionalProperty(_messages.Message):
      r"""An additional property for a ResponseValue object.

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


class Policy(_messages.Message):
  r"""Defines an Identity and Access Management (IAM) policy. It is used to
  specify access control policies for Cloud Platform resources.   A `Policy`
  is a collection of `bindings`. A `binding` binds one or more `members` to a
  single `role`. Members can be user accounts, service accounts, Google
  groups, and domains (such as G Suite). A `role` is a named list of
  permissions (defined by IAM or configured by users). A `binding` can
  optionally specify a `condition`, which is a logic expression that further
  constrains the role binding based on attributes about the request and/or
  target resource.  **JSON Example**      {       "bindings": [         {
  "role": "role/resourcemanager.organizationAdmin",           "members": [
  "user:mike@example.com",             "group:admins@example.com",
  "domain:google.com",             "serviceAccount:my-project-
  id@appspot.gserviceaccount.com"           ]         },         {
  "role": "roles/resourcemanager.organizationViewer",           "members":
  ["user:eve@example.com"],           "condition": {             "title":
  "expirable access",             "description": "Does not grant access after
  Sep 2020",             "expression": "request.time <
  timestamp('2020-10-01T00:00:00.000Z')",           }         }       ]     }
  **YAML Example**      bindings:     - members:       - user:mike@example.com
  - group:admins@example.com       - domain:google.com       - serviceAccount
  :my-project-id@appspot.gserviceaccount.com       role:
  roles/resourcemanager.organizationAdmin     - members:       -
  user:eve@example.com       role: roles/resourcemanager.organizationViewer
  condition:         title: expirable access         description: Does not
  grant access after Sep 2020         expression: request.time <
  timestamp('2020-10-01T00:00:00.000Z')  For a description of IAM and its
  features, see the [IAM developer's
  guide](https://cloud.google.com/iam/docs).

  Fields:
    auditConfigs: Specifies cloud audit logging configuration for this policy.
    bindings: Associates a list of `members` to a `role`. Optionally may
      specify a `condition` that determines when binding is in effect.
      `bindings` with no members will result in an error.
    etag: `etag` is used for optimistic concurrency control as a way to help
      prevent simultaneous updates of a policy from overwriting each other. It
      is strongly suggested that systems make use of the `etag` in the read-
      modify-write cycle to perform policy updates in order to avoid race
      conditions: An `etag` is returned in the response to `getIamPolicy`, and
      systems are expected to put that etag in the request to `setIamPolicy`
      to ensure that their change will be applied to the same version of the
      policy.  If no `etag` is provided in the call to `setIamPolicy`, then
      the existing policy is overwritten. Due to blind-set semantics of an
      etag-less policy, 'setIamPolicy' will not fail even if either of
      incoming or stored policy does not meet the version requirements.
    version: Specifies the format of the policy.  Valid values are 0, 1, and
      3. Requests specifying an invalid value will be rejected.  Operations
      affecting conditional bindings must specify version 3. This can be
      either setting a conditional policy, modifying a conditional binding, or
      removing a conditional binding from the stored conditional policy.
      Operations on non-conditional policies may specify any valid value or
      leave the field unset.  If no etag is provided in the call to
      `setIamPolicy`, any version compliance checks on the incoming and/or
      stored policy is skipped.
  """

  auditConfigs = _messages.MessageField('AuditConfig', 1, repeated=True)
  bindings = _messages.MessageField('Binding', 2, repeated=True)
  etag = _messages.BytesField(3)
  version = _messages.IntegerField(4, variant=_messages.Variant.INT32)


class SetIamPolicyRequest(_messages.Message):
  r"""Request message for `SetIamPolicy` method.

  Fields:
    policy: REQUIRED: The complete policy to be applied to the `resource`. The
      size of the policy is limited to a few 10s of KB. An empty policy is a
      valid policy but certain Cloud Platform services (such as Projects)
      might reject them.
    updateMask: OPTIONAL: A FieldMask specifying which fields of the policy to
      modify. Only the fields in the mask will be modified. If no mask is
      provided, the following default mask is used: paths: "bindings, etag"
      This field is only used by Cloud IAM.
  """

  policy = _messages.MessageField('Policy', 1)
  updateMask = _messages.StringField(2)


class StandardQueryParameters(_messages.Message):
  r"""Query parameters accepted by all methods.

  Enums:
    FXgafvValueValuesEnum: V1 error format.
    AltValueValuesEnum: Data format for response.

  Fields:
    f__xgafv: V1 error format.
    access_token: OAuth access token.
    alt: Data format for response.
    callback: JSONP
    fields: Selector specifying which fields to include in a partial response.
    key: API key. Your API key identifies your project and provides you with
      API access, quota, and reports. Required unless you provide an OAuth 2.0
      token.
    oauth_token: OAuth 2.0 token for the current user.
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
    r"""Data format for response.

    Values:
      json: Responses with Content-Type of application/json
      media: Media download with context-dependent Content-Type
      proto: Responses with Content-Type of application/x-protobuf
    """
    json = 0
    media = 1
    proto = 2

  class FXgafvValueValuesEnum(_messages.Enum):
    r"""V1 error format.

    Values:
      _1: v1 error format
      _2: v2 error format
    """
    _1 = 0
    _2 = 1

  f__xgafv = _messages.EnumField('FXgafvValueValuesEnum', 1)
  access_token = _messages.StringField(2)
  alt = _messages.EnumField('AltValueValuesEnum', 3, default=u'json')
  callback = _messages.StringField(4)
  fields = _messages.StringField(5)
  key = _messages.StringField(6)
  oauth_token = _messages.StringField(7)
  prettyPrint = _messages.BooleanField(8, default=True)
  quotaUser = _messages.StringField(9)
  trace = _messages.StringField(10)
  uploadType = _messages.StringField(11)
  upload_protocol = _messages.StringField(12)


class Status(_messages.Message):
  r"""The `Status` type defines a logical error model that is suitable for
  different programming environments, including REST APIs and RPC APIs. It is
  used by [gRPC](https://github.com/grpc). Each `Status` message contains
  three pieces of data: error code, error message, and error details.  You can
  find out more about this error model and how to work with it in the [API
  Design Guide](https://cloud.google.com/apis/design/errors).

  Messages:
    DetailsValueListEntry: A DetailsValueListEntry object.

  Fields:
    code: The status code, which should be an enum value of google.rpc.Code.
    details: A list of messages that carry the error details.  There is a
      common set of message types for APIs to use.
    message: A developer-facing error message, which should be in English. Any
      user-facing error message should be localized and sent in the
      google.rpc.Status.details field, or localized by the client.
  """

  @encoding.MapUnrecognizedFields('additionalProperties')
  class DetailsValueListEntry(_messages.Message):
    r"""A DetailsValueListEntry object.

    Messages:
      AdditionalProperty: An additional property for a DetailsValueListEntry
        object.

    Fields:
      additionalProperties: Properties of the object. Contains field @type
        with type URL.
    """

    class AdditionalProperty(_messages.Message):
      r"""An additional property for a DetailsValueListEntry object.

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


class TestIamPermissionsRequest(_messages.Message):
  r"""Request message for `TestIamPermissions` method.

  Fields:
    permissions: The set of permissions to check for the `resource`.
      Permissions with wildcards (such as '*' or 'storage.*') are not allowed.
      For more information see [IAM
      Overview](https://cloud.google.com/iam/docs/overview#permissions).
  """

  permissions = _messages.StringField(1, repeated=True)


class TestIamPermissionsResponse(_messages.Message):
  r"""Response message for `TestIamPermissions` method.

  Fields:
    permissions: A subset of `TestPermissionsRequest.permissions` that the
      caller is allowed.
  """

  permissions = _messages.StringField(1, repeated=True)


class UndeleteLabelKeyRequest(_messages.Message):
  r"""The request message for undeleting a label key."""


class UndeleteLabelValueRequest(_messages.Message):
  r"""The request message for undeleting a label value."""


encoding.AddCustomJsonFieldMapping(
    StandardQueryParameters, 'f__xgafv', '$.xgafv')
encoding.AddCustomJsonEnumMapping(
    StandardQueryParameters.FXgafvValueValuesEnum, '_1', '1')
encoding.AddCustomJsonEnumMapping(
    StandardQueryParameters.FXgafvValueValuesEnum, '_2', '2')
