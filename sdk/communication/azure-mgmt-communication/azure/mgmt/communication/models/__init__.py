# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from ._models_py3 import CheckNameAvailabilityRequest
from ._models_py3 import CheckNameAvailabilityResponse
from ._models_py3 import CommunicationServiceKeys
from ._models_py3 import CommunicationServiceResource
from ._models_py3 import CommunicationServiceResourceList
from ._models_py3 import CommunicationServiceResourceUpdate
from ._models_py3 import DnsRecord
from ._models_py3 import DomainPropertiesVerificationRecords
from ._models_py3 import DomainPropertiesVerificationStates
from ._models_py3 import DomainResource
from ._models_py3 import DomainResourceList
from ._models_py3 import EmailServiceResource
from ._models_py3 import EmailServiceResourceList
from ._models_py3 import EmailServiceResourceUpdate
from ._models_py3 import ErrorAdditionalInfo
from ._models_py3 import ErrorDetail
from ._models_py3 import ErrorResponse
from ._models_py3 import LinkNotificationHubParameters
from ._models_py3 import LinkedNotificationHub
from ._models_py3 import ManagedServiceIdentity
from ._models_py3 import NameAvailabilityParameters
from ._models_py3 import Operation
from ._models_py3 import OperationDisplay
from ._models_py3 import OperationListResult
from ._models_py3 import ProxyResource
from ._models_py3 import RegenerateKeyParameters
from ._models_py3 import Resource
from ._models_py3 import SenderUsernameResource
from ._models_py3 import SenderUsernameResourceCollection
from ._models_py3 import SuppressionListAddressResource
from ._models_py3 import SuppressionListAddressResourceCollection
from ._models_py3 import SuppressionListResource
from ._models_py3 import SuppressionListResourceCollection
from ._models_py3 import SystemData
from ._models_py3 import TaggedResource
from ._models_py3 import TrackedResource
from ._models_py3 import UpdateDomainRequestParameters
from ._models_py3 import UserAssignedIdentity
from ._models_py3 import VerificationParameter
from ._models_py3 import VerificationStatusRecord

from ._communication_service_management_client_enums import ActionType
from ._communication_service_management_client_enums import CheckNameAvailabilityReason
from ._communication_service_management_client_enums import CommunicationServicesProvisioningState
from ._communication_service_management_client_enums import CreatedByType
from ._communication_service_management_client_enums import DomainManagement
from ._communication_service_management_client_enums import DomainsProvisioningState
from ._communication_service_management_client_enums import EmailServicesProvisioningState
from ._communication_service_management_client_enums import KeyType
from ._communication_service_management_client_enums import ManagedServiceIdentityType
from ._communication_service_management_client_enums import Origin
from ._communication_service_management_client_enums import ProvisioningState
from ._communication_service_management_client_enums import UserEngagementTracking
from ._communication_service_management_client_enums import VerificationStatus
from ._communication_service_management_client_enums import VerificationType
from ._patch import __all__ as _patch_all
from ._patch import *  # pylint: disable=unused-wildcard-import
from ._patch import patch_sdk as _patch_sdk

__all__ = [
    "CheckNameAvailabilityRequest",
    "CheckNameAvailabilityResponse",
    "CommunicationServiceKeys",
    "CommunicationServiceResource",
    "CommunicationServiceResourceList",
    "CommunicationServiceResourceUpdate",
    "DnsRecord",
    "DomainPropertiesVerificationRecords",
    "DomainPropertiesVerificationStates",
    "DomainResource",
    "DomainResourceList",
    "EmailServiceResource",
    "EmailServiceResourceList",
    "EmailServiceResourceUpdate",
    "ErrorAdditionalInfo",
    "ErrorDetail",
    "ErrorResponse",
    "LinkNotificationHubParameters",
    "LinkedNotificationHub",
    "ManagedServiceIdentity",
    "NameAvailabilityParameters",
    "Operation",
    "OperationDisplay",
    "OperationListResult",
    "ProxyResource",
    "RegenerateKeyParameters",
    "Resource",
    "SenderUsernameResource",
    "SenderUsernameResourceCollection",
    "SuppressionListAddressResource",
    "SuppressionListAddressResourceCollection",
    "SuppressionListResource",
    "SuppressionListResourceCollection",
    "SystemData",
    "TaggedResource",
    "TrackedResource",
    "UpdateDomainRequestParameters",
    "UserAssignedIdentity",
    "VerificationParameter",
    "VerificationStatusRecord",
    "ActionType",
    "CheckNameAvailabilityReason",
    "CommunicationServicesProvisioningState",
    "CreatedByType",
    "DomainManagement",
    "DomainsProvisioningState",
    "EmailServicesProvisioningState",
    "KeyType",
    "ManagedServiceIdentityType",
    "Origin",
    "ProvisioningState",
    "UserEngagementTracking",
    "VerificationStatus",
    "VerificationType",
]
__all__.extend([p for p in _patch_all if p not in __all__])
_patch_sdk()
