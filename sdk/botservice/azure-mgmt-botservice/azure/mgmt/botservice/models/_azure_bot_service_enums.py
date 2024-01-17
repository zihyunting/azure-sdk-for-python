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
    """Access Mode of the resource association."""

    ENFORCED = "Enforced"
    LEARNING = "Learning"
    AUDIT = "Audit"


class ChannelName(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """ChannelName."""

    ALEXA_CHANNEL = "AlexaChannel"
    FACEBOOK_CHANNEL = "FacebookChannel"
    EMAIL_CHANNEL = "EmailChannel"
    KIK_CHANNEL = "KikChannel"
    TELEGRAM_CHANNEL = "TelegramChannel"
    SLACK_CHANNEL = "SlackChannel"
    MS_TEAMS_CHANNEL = "MsTeamsChannel"
    SKYPE_CHANNEL = "SkypeChannel"
    WEB_CHAT_CHANNEL = "WebChatChannel"
    DIRECT_LINE_CHANNEL = "DirectLineChannel"
    SMS_CHANNEL = "SmsChannel"
    LINE_CHANNEL = "LineChannel"
    DIRECT_LINE_SPEECH_CHANNEL = "DirectLineSpeechChannel"
    OUTLOOK_CHANNEL = "OutlookChannel"
    OMNICHANNEL = "Omnichannel"
    TELEPHONY_CHANNEL = "TelephonyChannel"
    ACS_CHAT_CHANNEL = "AcsChatChannel"
    SEARCH_ASSISTANT = "SearchAssistant"
    M365_EXTENSIONS = "M365Extensions"


class EmailChannelAuthMethod(int, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Email channel auth method. 0 Password (Default); 1 Graph."""

    PASSWORD = 0
    """Basic authentication."""
    GRAPH = 1
    """Modern authentication."""


class Key(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Determines which key is to be regenerated."""

    KEY1 = "key1"
    KEY2 = "key2"


class Kind(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Indicates the type of bot service."""

    SDK = "sdk"
    DESIGNER = "designer"
    BOT = "bot"
    FUNCTION = "function"
    AZUREBOT = "azurebot"


class MsaAppType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Microsoft App Type for the bot."""

    USER_ASSIGNED_MSI = "UserAssignedMSI"
    SINGLE_TENANT = "SingleTenant"
    MULTI_TENANT = "MultiTenant"


class NspAccessRuleDirection(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Direction of Access Rule."""

    INBOUND = "Inbound"
    OUTBOUND = "Outbound"


class OperationResultStatus(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The status of the operation being performed."""

    CANCELED = "Canceled"
    SUCCEEDED = "Succeeded"
    FAILED = "Failed"
    REQUESTED = "Requested"
    RUNNING = "Running"


class PrivateEndpointConnectionProvisioningState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The current provisioning state."""

    SUCCEEDED = "Succeeded"
    CREATING = "Creating"
    DELETING = "Deleting"
    FAILED = "Failed"


class PrivateEndpointServiceConnectionStatus(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The private endpoint connection status."""

    PENDING = "Pending"
    APPROVED = "Approved"
    REJECTED = "Rejected"


class ProvisioningState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """ProvisioningState."""

    CREATING = "Creating"
    UPDATING = "Updating"
    ACCEPTED = "Accepted"
    SUCCEEDED = "Succeeded"
    FAILED = "Failed"
    DELETING = "Deleting"


class PublicNetworkAccess(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Whether the bot is in an isolated network."""

    ENABLED = "Enabled"
    DISABLED = "Disabled"
    SECURED_BY_PERIMETER = "SecuredByPerimeter"


class RegenerateKeysChannelName(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """RegenerateKeysChannelName."""

    WEB_CHAT_CHANNEL = "WebChatChannel"
    DIRECT_LINE_CHANNEL = "DirectLineChannel"


class Severity(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Provisioning state of Network Security Perimeter configuration propagation."""

    WARNING = "Warning"
    ERROR = "Error"


class SkuName(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The name of SKU."""

    F0 = "F0"
    S1 = "S1"


class SkuTier(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Gets the sku tier. This is based on the SKU name."""

    FREE = "Free"
    STANDARD = "Standard"
