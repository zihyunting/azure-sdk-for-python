# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from ._models_py3 import CheckQuotaAvailabilityResponse
from ._models_py3 import EncryptionProperties
from ._models_py3 import EncryptionPropertiesIdentity
from ._models_py3 import EndpointDependency
from ._models_py3 import EndpointDetail
from ._models_py3 import ErrorAdditionalInfo
from ._models_py3 import ErrorDetail
from ._models_py3 import ErrorResponse
from ._models_py3 import LoadTestResource
from ._models_py3 import LoadTestResourceListResult
from ._models_py3 import LoadTestResourceUpdate
from ._models_py3 import ManagedServiceIdentity
from ._models_py3 import Operation
from ._models_py3 import OperationDisplay
from ._models_py3 import OperationListResult
from ._models_py3 import OutboundEnvironmentEndpoint
from ._models_py3 import PagedOutboundEnvironmentEndpoint
from ._models_py3 import ProxyResource
from ._models_py3 import QuotaBucketRequest
from ._models_py3 import QuotaBucketRequestPropertiesDimensions
from ._models_py3 import QuotaResource
from ._models_py3 import QuotaResourceListResult
from ._models_py3 import Resource
from ._models_py3 import SystemData
from ._models_py3 import TrackedResource
from ._models_py3 import UserAssignedIdentity

from ._load_test_mgmt_client_enums import ActionType
from ._load_test_mgmt_client_enums import CreatedByType
from ._load_test_mgmt_client_enums import ManagedServiceIdentityType
from ._load_test_mgmt_client_enums import Origin
from ._load_test_mgmt_client_enums import ResourceState
from ._load_test_mgmt_client_enums import Type
from ._patch import __all__ as _patch_all
from ._patch import *  # pylint: disable=unused-wildcard-import
from ._patch import patch_sdk as _patch_sdk

__all__ = [
    "CheckQuotaAvailabilityResponse",
    "EncryptionProperties",
    "EncryptionPropertiesIdentity",
    "EndpointDependency",
    "EndpointDetail",
    "ErrorAdditionalInfo",
    "ErrorDetail",
    "ErrorResponse",
    "LoadTestResource",
    "LoadTestResourceListResult",
    "LoadTestResourceUpdate",
    "ManagedServiceIdentity",
    "Operation",
    "OperationDisplay",
    "OperationListResult",
    "OutboundEnvironmentEndpoint",
    "PagedOutboundEnvironmentEndpoint",
    "ProxyResource",
    "QuotaBucketRequest",
    "QuotaBucketRequestPropertiesDimensions",
    "QuotaResource",
    "QuotaResourceListResult",
    "Resource",
    "SystemData",
    "TrackedResource",
    "UserAssignedIdentity",
    "ActionType",
    "CreatedByType",
    "ManagedServiceIdentityType",
    "Origin",
    "ResourceState",
    "Type",
]
__all__.extend([p for p in _patch_all if p not in __all__])
_patch_sdk()
