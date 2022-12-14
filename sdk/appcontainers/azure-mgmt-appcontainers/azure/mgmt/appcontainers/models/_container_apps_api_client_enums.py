# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum
from azure.core import CaseInsensitiveEnumMeta


class AccessMode(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Access mode for storage."""

    READ_ONLY = "ReadOnly"
    READ_WRITE = "ReadWrite"


class Action(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Allow or Deny rules to determine for incoming IP. Note: Rules can only consist of ALL Allow or
    ALL Deny.
    """

    ALLOW = "Allow"
    DENY = "Deny"


class ActiveRevisionsMode(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """ActiveRevisionsMode controls how active revisions are handled for the Container app:


    .. raw:: html

       <list><item>Multiple: multiple revisions can be active.</item><item>Single: Only one
    revision can be active at a time. Revision weights can not be used in this mode. If no value if
    provided, this is the default.</item></list>.
    """

    MULTIPLE = "Multiple"
    SINGLE = "Single"


class Affinity(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Sticky Session Affinity."""

    STICKY = "sticky"
    NONE = "none"


class Applicability(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """indicates whether the profile is default for the location."""

    LOCATION_DEFAULT = "LocationDefault"
    CUSTOM = "Custom"


class AppProtocol(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Tells Dapr which protocol your application is using. Valid options are http and grpc. Default
    is http.
    """

    HTTP = "http"
    GRPC = "grpc"


class BindingType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Custom Domain binding type."""

    DISABLED = "Disabled"
    SNI_ENABLED = "SniEnabled"


class Category(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Used to map workload profile types to billing meter."""

    PREMIUM_SKU_GENERAL_PURPOSE = "PremiumSkuGeneralPurpose"
    PREMIUM_SKU_MEMORY_OPTIMIZED = "PremiumSkuMemoryOptimized"
    PREMIUM_SKU_COMPUTE_OPTIMIZED = "PremiumSkuComputeOptimized"


class CertificateProvisioningState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Provisioning state of the certificate."""

    SUCCEEDED = "Succeeded"
    FAILED = "Failed"
    CANCELED = "Canceled"
    DELETE_FAILED = "DeleteFailed"
    PENDING = "Pending"


class CheckNameAvailabilityReason(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The reason why the given name is not available."""

    INVALID = "Invalid"
    ALREADY_EXISTS = "AlreadyExists"


class ConnectedEnvironmentProvisioningState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Provisioning state of the Kubernetes Environment."""

    SUCCEEDED = "Succeeded"
    FAILED = "Failed"
    CANCELED = "Canceled"
    WAITING = "Waiting"
    INITIALIZATION_IN_PROGRESS = "InitializationInProgress"
    INFRASTRUCTURE_SETUP_IN_PROGRESS = "InfrastructureSetupInProgress"
    INFRASTRUCTURE_SETUP_COMPLETE = "InfrastructureSetupComplete"
    SCHEDULED_FOR_DELETE = "ScheduledForDelete"


class ContainerAppProvisioningState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Provisioning state of the Container App."""

    IN_PROGRESS = "InProgress"
    SUCCEEDED = "Succeeded"
    FAILED = "Failed"
    CANCELED = "Canceled"
    DELETING = "Deleting"


class CookieExpirationConvention(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The convention used when determining the session cookie's expiration."""

    FIXED_TIME = "FixedTime"
    IDENTITY_PROVIDER_DERIVED = "IdentityProviderDerived"


class CreatedByType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The type of identity that created the resource."""

    USER = "User"
    APPLICATION = "Application"
    MANAGED_IDENTITY = "ManagedIdentity"
    KEY = "Key"


class DnsVerificationTestResult(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """DNS verification test result."""

    PASSED = "Passed"
    FAILED = "Failed"
    SKIPPED = "Skipped"


class EnvironmentProvisioningState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Provisioning state of the Environment."""

    SUCCEEDED = "Succeeded"
    FAILED = "Failed"
    CANCELED = "Canceled"
    WAITING = "Waiting"
    INITIALIZATION_IN_PROGRESS = "InitializationInProgress"
    INFRASTRUCTURE_SETUP_IN_PROGRESS = "InfrastructureSetupInProgress"
    INFRASTRUCTURE_SETUP_COMPLETE = "InfrastructureSetupComplete"
    SCHEDULED_FOR_DELETE = "ScheduledForDelete"
    UPGRADE_REQUESTED = "UpgradeRequested"
    UPGRADE_FAILED = "UpgradeFailed"


class ExtendedLocationTypes(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The type of extendedLocation."""

    CUSTOM_LOCATION = "CustomLocation"


class ForwardProxyConvention(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The convention used to determine the url of the request made."""

    NO_PROXY = "NoProxy"
    STANDARD = "Standard"
    CUSTOM = "Custom"


class IngressClientCertificateMode(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Client certificate mode for mTLS authentication. Ignore indicates server drops client
    certificate on forwarding. Accept indicates server forwards client certificate but does not
    require a client certificate. Require indicates server requires a client certificate.
    """

    IGNORE = "ignore"
    ACCEPT = "accept"
    REQUIRE = "require"


class IngressTransportMethod(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Ingress transport protocol."""

    AUTO = "auto"
    HTTP = "http"
    HTTP2 = "http2"
    TCP = "tcp"


class LogLevel(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Sets the log level for the Dapr sidecar. Allowed values are debug, info, warn, error. Default
    is info.
    """

    INFO = "info"
    DEBUG = "debug"
    WARN = "warn"
    ERROR = "error"


class ManagedCertificateDomainControlValidation(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Selected type of domain control validation for managed certificates."""

    CNAME = "CNAME"
    HTTP = "HTTP"
    TXT = "TXT"


class ManagedEnvironmentOutBoundType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Outbound type for the cluster."""

    LOAD_BALANCER = "LoadBalancer"
    USER_DEFINED_ROUTING = "UserDefinedRouting"


class ManagedServiceIdentityType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Type of managed service identity (where both SystemAssigned and UserAssigned types are
    allowed).
    """

    NONE = "None"
    SYSTEM_ASSIGNED = "SystemAssigned"
    USER_ASSIGNED = "UserAssigned"
    SYSTEM_ASSIGNED_USER_ASSIGNED = "SystemAssigned,UserAssigned"


class RevisionHealthState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Current health State of the revision."""

    HEALTHY = "Healthy"
    UNHEALTHY = "Unhealthy"
    NONE = "None"


class RevisionProvisioningState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Current provisioning State of the revision."""

    PROVISIONING = "Provisioning"
    PROVISIONED = "Provisioned"
    FAILED = "Failed"
    DEPROVISIONING = "Deprovisioning"
    DEPROVISIONED = "Deprovisioned"


class Scheme(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Scheme to use for connecting to the host. Defaults to HTTP."""

    HTTP = "HTTP"
    HTTPS = "HTTPS"


class SkuName(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Name of the Sku."""

    #: Consumption SKU of Managed Environment.
    CONSUMPTION = "Consumption"
    #: Premium SKU of Managed Environment.
    PREMIUM = "Premium"


class SourceControlOperationState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Current provisioning State of the operation."""

    IN_PROGRESS = "InProgress"
    SUCCEEDED = "Succeeded"
    FAILED = "Failed"
    CANCELED = "Canceled"


class StorageType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Storage type for the volume. If not provided, use EmptyDir."""

    AZURE_FILE = "AzureFile"
    EMPTY_DIR = "EmptyDir"


class Type(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The type of probe."""

    LIVENESS = "Liveness"
    READINESS = "Readiness"
    STARTUP = "Startup"


class UnauthenticatedClientActionV2(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The action to take when an unauthenticated client attempts to access the app."""

    REDIRECT_TO_LOGIN_PAGE = "RedirectToLoginPage"
    ALLOW_ANONYMOUS = "AllowAnonymous"
    RETURN401 = "Return401"
    RETURN403 = "Return403"
