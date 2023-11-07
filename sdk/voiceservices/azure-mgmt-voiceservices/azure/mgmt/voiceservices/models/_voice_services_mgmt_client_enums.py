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


class ApiBridgeActivationState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """API Bridge activation state."""

    ENABLED = "enabled"
    """API Bridge is enabled"""
    DISABLED = "disabled"
    """API Bridge is disabled"""


class AutoGeneratedDomainNameLabelScope(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Available auto-generated domain name scopes."""

    TENANT_REUSE = "TenantReuse"
    """Generated domain name label depends on resource name and tenant ID."""
    SUBSCRIPTION_REUSE = "SubscriptionReuse"
    """Generated domain name label depends on resource name, tenant ID and subscription ID."""
    RESOURCE_GROUP_REUSE = "ResourceGroupReuse"
    """Generated domain name label depends on resource name, tenant ID, subscription ID and resource
    #: group name."""
    NO_REUSE = "NoReuse"
    """Generated domain name label is always unique."""


class CheckNameAvailabilityReason(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Possible reasons for a name not being available."""

    INVALID = "Invalid"
    ALREADY_EXISTS = "AlreadyExists"


class CommunicationsPlatform(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Available platform types."""

    OPERATOR_CONNECT = "OperatorConnect"
    """Operator Connect"""
    TEAMS_PHONE_MOBILE = "TeamsPhoneMobile"
    """Teams Phone Mobile"""
    TEAMS_DIRECT_ROUTING = "TeamsDirectRouting"
    """Teams Direct Routing"""


class Connectivity(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """How this deployment connects back to the operator network."""

    PUBLIC_ADDRESS = "PublicAddress"
    """This deployment connects to the operator network using a Public IP address, e.g. when using
    #: MAPS"""


class CreatedByType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The type of identity that created the resource."""

    USER = "User"
    APPLICATION = "Application"
    MANAGED_IDENTITY = "ManagedIdentity"
    KEY = "Key"


class E911Type(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The method for terminating emergency calls to the PSTN."""

    STANDARD = "Standard"
    """Emergency calls are not handled different from other calls"""
    DIRECT_TO_ESRP = "DirectToEsrp"
    """Emergency calls are routed directly to the ESRP"""


class ManagedServiceIdentityType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Type of managed service identity (where both SystemAssigned and UserAssigned types are
    allowed).
    """

    NONE = "None"
    SYSTEM_ASSIGNED = "SystemAssigned"
    USER_ASSIGNED = "UserAssigned"
    SYSTEM_ASSIGNED_USER_ASSIGNED = "SystemAssigned, UserAssigned"


class Origin(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The intended executor of the operation; as in Resource Based Access Control (RBAC) and audit
    logs UX. Default value is "user,system".
    """

    USER = "user"
    SYSTEM = "system"
    USER_SYSTEM = "user,system"


class ProvisioningState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Provisioning state of the resource."""

    SUCCEEDED = "Succeeded"
    """Resource has been created."""
    FAILED = "Failed"
    """Resource creation failed."""
    CANCELED = "Canceled"
    """Resource creation was canceled."""


class SkuTier(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """This field is required to be implemented by the Resource Provider if the service has more than
    one tier, but is not required on a PUT.
    """

    FREE = "Free"
    BASIC = "Basic"
    STANDARD = "Standard"
    PREMIUM = "Premium"


class Status(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The status of the current CommunicationsGateway resource."""

    CHANGE_PENDING = "ChangePending"
    """The resource has been created or updated, but the CommunicationsGateway service has not yet
    #: been updated to reflect the changes."""
    COMPLETE = "Complete"
    """The CommunicationsGateway service is up and running with the parameters specified in the
    #: resource."""


class TeamsCodecs(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The voice codecs expected for communication with Teams."""

    PCMA = "PCMA"
    """Pulse code modulation(PCM) U-law narrowband audio codec(G.711u)"""
    PCMU = "PCMU"
    """Pulse code modulation(PCM) U-law narrowband audio codec(G.711u)"""
    G722 = "G722"
    """G.722 wideband audio codec"""
    G722_2 = "G722_2"
    """G.722.2 wideband audio codec"""
    SILK8 = "SILK_8"
    """SILK/8000 narrowband audio codec"""
    SILK16 = "SILK_16"
    """SILK/16000 wideband audio codec"""


class TestLinePurpose(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The purpose of the TestLine resource."""

    MANUAL = "Manual"
    """The test line is used for manual testing"""
    AUTOMATED = "Automated"
    """The test line is used for automated testing"""
