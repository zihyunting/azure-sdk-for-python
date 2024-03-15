# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from ._operations import DeploymentsOperations
from ._operations import DeploymentOperationsOperations
from ._operations import Operations
from ._operations import ProvidersOperations
from ._operations import ProviderResourceTypesOperations
from ._operations import ResourcesOperations
from ._operations import ResourceGroupsOperations
from ._operations import TagsOperations

from ._patch import __all__ as _patch_all
from ._patch import *  # pylint: disable=unused-wildcard-import
from ._patch import patch_sdk as _patch_sdk

__all__ = [
    "DeploymentsOperations",
    "DeploymentOperationsOperations",
    "Operations",
    "ProvidersOperations",
    "ProviderResourceTypesOperations",
    "ResourcesOperations",
    "ResourceGroupsOperations",
    "TagsOperations",
]
__all__.extend([p for p in _patch_all if p not in __all__])
_patch_sdk()
