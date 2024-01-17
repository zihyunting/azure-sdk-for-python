# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from ._models_py3 import AlertSyncSettings
from ._models_py3 import AssessmentLinks
from ._models_py3 import AssessmentStatus
from ._models_py3 import AssessmentStatusResponse
from ._models_py3 import AzureResourceDetails
from ._models_py3 import CloudErrorBody
from ._models_py3 import DataExportSettings
from ._models_py3 import ErrorAdditionalInfo
from ._models_py3 import OnPremiseResourceDetails
from ._models_py3 import OnPremiseSqlResourceDetails
from ._models_py3 import Resource
from ._models_py3 import ResourceDetails
from ._models_py3 import SecurityAssessment
from ._models_py3 import SecurityAssessmentList
from ._models_py3 import SecurityAssessmentMetadata
from ._models_py3 import SecurityAssessmentMetadataPartnerData
from ._models_py3 import SecurityAssessmentMetadataProperties
from ._models_py3 import SecurityAssessmentMetadataPropertiesResponse
from ._models_py3 import SecurityAssessmentMetadataPropertiesResponsePublishDates
from ._models_py3 import SecurityAssessmentMetadataResponse
from ._models_py3 import SecurityAssessmentMetadataResponseList
from ._models_py3 import SecurityAssessmentPartnerData
from ._models_py3 import SecurityAssessmentProperties
from ._models_py3 import SecurityAssessmentPropertiesBase
from ._models_py3 import SecurityAssessmentPropertiesResponse
from ._models_py3 import SecurityAssessmentResponse
from ._models_py3 import Setting
from ._models_py3 import SettingsList

from ._security_center_enums import AssessmentStatusCode
from ._security_center_enums import AssessmentType
from ._security_center_enums import Categories
from ._security_center_enums import Enum12
from ._security_center_enums import ExpandEnum
from ._security_center_enums import ImplementationEffort
from ._security_center_enums import SettingKind
from ._security_center_enums import Severity
from ._security_center_enums import Source
from ._security_center_enums import Tactics
from ._security_center_enums import Techniques
from ._security_center_enums import Threats
from ._security_center_enums import UserImpact
from ._patch import __all__ as _patch_all
from ._patch import *  # pylint: disable=unused-wildcard-import
from ._patch import patch_sdk as _patch_sdk

__all__ = [
    "AlertSyncSettings",
    "AssessmentLinks",
    "AssessmentStatus",
    "AssessmentStatusResponse",
    "AzureResourceDetails",
    "CloudErrorBody",
    "DataExportSettings",
    "ErrorAdditionalInfo",
    "OnPremiseResourceDetails",
    "OnPremiseSqlResourceDetails",
    "Resource",
    "ResourceDetails",
    "SecurityAssessment",
    "SecurityAssessmentList",
    "SecurityAssessmentMetadata",
    "SecurityAssessmentMetadataPartnerData",
    "SecurityAssessmentMetadataProperties",
    "SecurityAssessmentMetadataPropertiesResponse",
    "SecurityAssessmentMetadataPropertiesResponsePublishDates",
    "SecurityAssessmentMetadataResponse",
    "SecurityAssessmentMetadataResponseList",
    "SecurityAssessmentPartnerData",
    "SecurityAssessmentProperties",
    "SecurityAssessmentPropertiesBase",
    "SecurityAssessmentPropertiesResponse",
    "SecurityAssessmentResponse",
    "Setting",
    "SettingsList",
    "AssessmentStatusCode",
    "AssessmentType",
    "Categories",
    "Enum12",
    "ExpandEnum",
    "ImplementationEffort",
    "SettingKind",
    "Severity",
    "Source",
    "Tactics",
    "Techniques",
    "Threats",
    "UserImpact",
]
__all__.extend([p for p in _patch_all if p not in __all__])
_patch_sdk()
