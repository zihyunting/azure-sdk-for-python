# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum
from azure.core import CaseInsensitiveEnumMeta


class ActionType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Enum. Indicates the action type. "Internal" refers to actions that are for internal only APIs."""

    INTERNAL = "Internal"


class CheckNameAvailabilityReason(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The reason why the given name is not available."""

    INVALID = "Invalid"
    ALREADY_EXISTS = "AlreadyExists"


class CostThresholdStatus(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Indicates whether this threshold will be displayed on cost charts."""

    ENABLED = "Enabled"
    DISABLED = "Disabled"


class CostType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The type of the cost."""

    UNAVAILABLE = "Unavailable"
    REPORTED = "Reported"
    PROJECTED = "Projected"


class CreatedByType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The type of identity that created the resource."""

    USER = "User"
    APPLICATION = "Application"
    MANAGED_IDENTITY = "ManagedIdentity"
    KEY = "Key"


class CustomImageOsType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The OS type of the custom image (i.e. Windows, Linux)."""

    WINDOWS = "Windows"
    LINUX = "Linux"
    NONE = "None"


class EnableState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Enables all images in the gallery to be available in the lab for VM creation. This will
    override the EnableState on shared images.
    """

    DISABLED = "Disabled"
    ENABLED = "Enabled"


class EnableStatus(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Indicates if the artifact source is enabled (values: Enabled, Disabled)."""

    ENABLED = "Enabled"
    DISABLED = "Disabled"


class EncryptionStatus(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Indicates whether or not the encryption is enabled for container registry."""

    ENABLED = "enabled"
    DISABLED = "disabled"


class EncryptionType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Gets or sets the type of key used to encrypt the data of the disk. Possible values include:
    'EncryptionAtRestWithPlatformKey', 'EncryptionAtRestWithCustomerKey'.
    """

    ENCRYPTION_AT_REST_WITH_PLATFORM_KEY = "EncryptionAtRestWithPlatformKey"
    ENCRYPTION_AT_REST_WITH_CUSTOMER_KEY = "EncryptionAtRestWithCustomerKey"


class EnvironmentPermission(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The access rights to be granted to the user when provisioning an environment."""

    READER = "Reader"
    CONTRIBUTOR = "Contributor"


class FileUploadOptions(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Options for uploading the files for the artifact. UploadFilesAndGenerateSasTokens is the
    default value.
    """

    UPLOAD_FILES_AND_GENERATE_SAS_TOKENS = "UploadFilesAndGenerateSasTokens"
    NONE = "None"


class HostCachingOptions(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Caching option for a data disk (i.e. None, ReadOnly, ReadWrite)."""

    NONE = "None"
    READ_ONLY = "ReadOnly"
    READ_WRITE = "ReadWrite"


class HttpStatusCode(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The status code for the operation."""

    CONTINUE = "Continue"
    SWITCHING_PROTOCOLS = "SwitchingProtocols"
    PROCESSING = "Processing"
    EARLY_HINTS = "EarlyHints"
    OK = "OK"
    CREATED = "Created"
    ACCEPTED = "Accepted"
    NON_AUTHORITATIVE_INFORMATION = "NonAuthoritativeInformation"
    NO_CONTENT = "NoContent"
    RESET_CONTENT = "ResetContent"
    PARTIAL_CONTENT = "PartialContent"
    MULTI_STATUS = "MultiStatus"
    ALREADY_REPORTED = "AlreadyReported"
    IM_USED = "IMUsed"
    MULTIPLE_CHOICES = "MultipleChoices"
    AMBIGUOUS = "Ambiguous"
    MOVED_PERMANENTLY = "MovedPermanently"
    MOVED = "Moved"
    FOUND = "Found"
    REDIRECT = "Redirect"
    SEE_OTHER = "SeeOther"
    REDIRECT_METHOD = "RedirectMethod"
    NOT_MODIFIED = "NotModified"
    USE_PROXY = "UseProxy"
    UNUSED = "Unused"
    TEMPORARY_REDIRECT = "TemporaryRedirect"
    REDIRECT_KEEP_VERB = "RedirectKeepVerb"
    PERMANENT_REDIRECT = "PermanentRedirect"
    BAD_REQUEST = "BadRequest"
    UNAUTHORIZED = "Unauthorized"
    PAYMENT_REQUIRED = "PaymentRequired"
    FORBIDDEN = "Forbidden"
    NOT_FOUND = "NotFound"
    METHOD_NOT_ALLOWED = "MethodNotAllowed"
    NOT_ACCEPTABLE = "NotAcceptable"
    PROXY_AUTHENTICATION_REQUIRED = "ProxyAuthenticationRequired"
    REQUEST_TIMEOUT = "RequestTimeout"
    CONFLICT = "Conflict"
    GONE = "Gone"
    LENGTH_REQUIRED = "LengthRequired"
    PRECONDITION_FAILED = "PreconditionFailed"
    REQUEST_ENTITY_TOO_LARGE = "RequestEntityTooLarge"
    REQUEST_URI_TOO_LONG = "RequestUriTooLong"
    UNSUPPORTED_MEDIA_TYPE = "UnsupportedMediaType"
    REQUESTED_RANGE_NOT_SATISFIABLE = "RequestedRangeNotSatisfiable"
    EXPECTATION_FAILED = "ExpectationFailed"
    MISDIRECTED_REQUEST = "MisdirectedRequest"
    UNPROCESSABLE_ENTITY = "UnprocessableEntity"
    LOCKED = "Locked"
    FAILED_DEPENDENCY = "FailedDependency"
    UPGRADE_REQUIRED = "UpgradeRequired"
    PRECONDITION_REQUIRED = "PreconditionRequired"
    TOO_MANY_REQUESTS = "TooManyRequests"
    REQUEST_HEADER_FIELDS_TOO_LARGE = "RequestHeaderFieldsTooLarge"
    UNAVAILABLE_FOR_LEGAL_REASONS = "UnavailableForLegalReasons"
    INTERNAL_SERVER_ERROR = "InternalServerError"
    NOT_IMPLEMENTED = "NotImplemented"
    BAD_GATEWAY = "BadGateway"
    SERVICE_UNAVAILABLE = "ServiceUnavailable"
    GATEWAY_TIMEOUT = "GatewayTimeout"
    HTTP_VERSION_NOT_SUPPORTED = "HttpVersionNotSupported"
    VARIANT_ALSO_NEGOTIATES = "VariantAlsoNegotiates"
    INSUFFICIENT_STORAGE = "InsufficientStorage"
    LOOP_DETECTED = "LoopDetected"
    NOT_EXTENDED = "NotExtended"
    NETWORK_AUTHENTICATION_REQUIRED = "NetworkAuthenticationRequired"
    CONTINUE_ENUM = "Continue"


class ImageType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The type of image in the gallery (generalized or specialized)."""

    GENERALIZED = "Generalized"
    SPECIALIZED = "Specialized"


class LinuxOsState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The state of the Linux OS (i.e. NonDeprovisioned, DeprovisionRequested, DeprovisionApplied)."""

    NON_DEPROVISIONED = "NonDeprovisioned"
    DEPROVISION_REQUESTED = "DeprovisionRequested"
    DEPROVISION_APPLIED = "DeprovisionApplied"


class ManagedIdentityType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Type of identity (SystemAssigned, UserAssigned, None)."""

    NONE = "None"
    SYSTEM_ASSIGNED = "SystemAssigned"
    USER_ASSIGNED = "UserAssigned"
    SYSTEM_ASSIGNED_USER_ASSIGNED = "SystemAssigned,UserAssigned"


class NotificationChannelEventType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The event type for which this notification is enabled (i.e. AutoShutdown, Cost)."""

    AUTO_SHUTDOWN = "AutoShutdown"
    COST = "Cost"


class Origin(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The intended executor of the operation; as in Resource Based Access Control (RBAC) and audit
    logs UX. Default value is "user,system".
    """

    USER = "user"
    SYSTEM = "system"
    USER_SYSTEM = "user,system"


class OsType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The operating system of the image."""

    WINDOWS = "Windows"
    LINUX = "Linux"


class PolicyEvaluatorType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The evaluator type of the policy (i.e. AllowedValuesPolicy, MaxValuePolicy)."""

    ALLOWED_VALUES_POLICY = "AllowedValuesPolicy"
    MAX_VALUE_POLICY = "MaxValuePolicy"


class PolicyFactName(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The fact name of the policy (e.g. LabVmCount, LabVmSize, MaxVmsAllowedPerLab, etc."""

    USER_OWNED_LAB_VM_COUNT = "UserOwnedLabVmCount"
    USER_OWNED_LAB_PREMIUM_VM_COUNT = "UserOwnedLabPremiumVmCount"
    LAB_VM_COUNT = "LabVmCount"
    LAB_PREMIUM_VM_COUNT = "LabPremiumVmCount"
    LAB_VM_SIZE = "LabVmSize"
    GALLERY_IMAGE = "GalleryImage"
    USER_OWNED_LAB_VM_COUNT_IN_SUBNET = "UserOwnedLabVmCountInSubnet"
    LAB_TARGET_COST = "LabTargetCost"
    ENVIRONMENT_TEMPLATE = "EnvironmentTemplate"
    SCHEDULE_EDIT_PERMISSION = "ScheduleEditPermission"


class PolicyStatus(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The status of the policy."""

    ENABLED = "Enabled"
    DISABLED = "Disabled"


class PremiumDataDisk(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The setting to enable usage of premium data disks.
    When its value is 'Enabled', creation of standard or premium data disks is allowed.
    When its value is 'Disabled', only creation of standard data disks is allowed.
    """

    DISABLED = "Disabled"
    ENABLED = "Enabled"


class ReportingCycleType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Reporting cycle type."""

    CALENDAR_MONTH = "CalendarMonth"
    CUSTOM = "Custom"


class SkuTier(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """This field is required to be implemented by the Resource Provider if the service has more than
    one tier, but is not required on a PUT.
    """

    FREE = "Free"
    BASIC = "Basic"
    STANDARD = "Standard"
    PREMIUM = "Premium"


class SourceControlType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The artifact source's type."""

    VSO_GIT = "VsoGit"
    GIT_HUB = "GitHub"
    STORAGE_ACCOUNT = "StorageAccount"


class StorageType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The storage type for the disk (i.e. Standard, Premium)."""

    STANDARD = "Standard"
    PREMIUM = "Premium"
    STANDARD_SSD = "StandardSSD"


class StorageTypes(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Storage type to use for virtual machine (i.e. Standard, Premium, StandardSSD)."""

    STANDARD = "Standard"
    PREMIUM = "Premium"
    STANDARD_SSD = "StandardSSD"


class TargetCostStatus(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Target cost status."""

    ENABLED = "Enabled"
    DISABLED = "Disabled"


class TransportProtocol(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The transport protocol for the endpoint."""

    TCP = "Tcp"
    UDP = "Udp"


class UsagePermissionType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The permission policy of the subnet for allowing public IP addresses (i.e. Allow, Deny))."""

    DEFAULT = "Default"
    DENY = "Deny"
    ALLOW = "Allow"


class VirtualMachineCreationSource(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Tells source of creation of lab virtual machine. Output property only."""

    FROM_CUSTOM_IMAGE = "FromCustomImage"
    FROM_GALLERY_IMAGE = "FromGalleryImage"
    FROM_SHARED_GALLERY_IMAGE = "FromSharedGalleryImage"


class WindowsOsState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The state of the Windows OS (i.e. NonSysprepped, SysprepRequested, SysprepApplied)."""

    NON_SYSPREPPED = "NonSysprepped"
    SYSPREP_REQUESTED = "SysprepRequested"
    SYSPREP_APPLIED = "SysprepApplied"
