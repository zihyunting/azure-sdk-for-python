# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from ._models_py3 import AzureLargeInstance
from ._models_py3 import AzureLargeInstanceListResult
from ._models_py3 import AzureLargeStorageInstance
from ._models_py3 import AzureLargeStorageInstanceListResult
from ._models_py3 import Disk
from ._models_py3 import ErrorAdditionalInfo
from ._models_py3 import ErrorDetail
from ._models_py3 import ErrorResponse
from ._models_py3 import ForceState
from ._models_py3 import HardwareProfile
from ._models_py3 import IpAddress
from ._models_py3 import NetworkProfile
from ._models_py3 import OSProfile
from ._models_py3 import Operation
from ._models_py3 import OperationDisplay
from ._models_py3 import OperationListResult
from ._models_py3 import OperationStatusResult
from ._models_py3 import Resource
from ._models_py3 import StorageBillingProperties
from ._models_py3 import StorageProfile
from ._models_py3 import StorageProperties
from ._models_py3 import SystemData
from ._models_py3 import Tags
from ._models_py3 import TrackedResource

from ._azure_large_instance_enums import ActionType
from ._azure_large_instance_enums import AzureLargeInstanceForcePowerState
from ._azure_large_instance_enums import AzureLargeInstanceHardwareTypeNamesEnum
from ._azure_large_instance_enums import AzureLargeInstancePowerStateEnum
from ._azure_large_instance_enums import AzureLargeInstanceProvisioningStatesEnum
from ._azure_large_instance_enums import AzureLargeInstanceSizeNamesEnum
from ._azure_large_instance_enums import CreatedByType
from ._azure_large_instance_enums import Origin
from ._azure_large_instance_enums import ProvisioningState
from ._patch import __all__ as _patch_all
from ._patch import *  # pylint: disable=unused-wildcard-import
from ._patch import patch_sdk as _patch_sdk

__all__ = [
    "AzureLargeInstance",
    "AzureLargeInstanceListResult",
    "AzureLargeStorageInstance",
    "AzureLargeStorageInstanceListResult",
    "Disk",
    "ErrorAdditionalInfo",
    "ErrorDetail",
    "ErrorResponse",
    "ForceState",
    "HardwareProfile",
    "IpAddress",
    "NetworkProfile",
    "OSProfile",
    "Operation",
    "OperationDisplay",
    "OperationListResult",
    "OperationStatusResult",
    "Resource",
    "StorageBillingProperties",
    "StorageProfile",
    "StorageProperties",
    "SystemData",
    "Tags",
    "TrackedResource",
    "ActionType",
    "AzureLargeInstanceForcePowerState",
    "AzureLargeInstanceHardwareTypeNamesEnum",
    "AzureLargeInstancePowerStateEnum",
    "AzureLargeInstanceProvisioningStatesEnum",
    "AzureLargeInstanceSizeNamesEnum",
    "CreatedByType",
    "Origin",
    "ProvisioningState",
]
__all__.extend([p for p in _patch_all if p not in __all__])
_patch_sdk()
