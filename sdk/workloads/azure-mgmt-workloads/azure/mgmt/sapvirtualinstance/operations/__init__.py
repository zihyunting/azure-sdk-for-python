# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from ._workloads_client_operations import WorkloadsClientOperationsMixin
from ._sap_virtual_instances_operations import SAPVirtualInstancesOperations
from ._sap_central_instances_operations import SAPCentralInstancesOperations
from ._sap_database_instances_operations import SAPDatabaseInstancesOperations
from ._sap_application_server_instances_operations import SAPApplicationServerInstancesOperations
from ._operations import Operations

from ._patch import __all__ as _patch_all
from ._patch import *  # pylint: disable=unused-wildcard-import
from ._patch import patch_sdk as _patch_sdk

__all__ = [
    "WorkloadsClientOperationsMixin",
    "SAPVirtualInstancesOperations",
    "SAPCentralInstancesOperations",
    "SAPDatabaseInstancesOperations",
    "SAPApplicationServerInstancesOperations",
    "Operations",
]
__all__.extend([p for p in _patch_all if p not in __all__])
_patch_sdk()
