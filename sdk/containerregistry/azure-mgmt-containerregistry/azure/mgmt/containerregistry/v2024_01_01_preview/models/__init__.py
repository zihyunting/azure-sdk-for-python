# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from ._models_py3 import ActivationProperties
from ._models_py3 import ActiveDirectoryObject
from ._models_py3 import Actor
from ._models_py3 import Archive
from ._models_py3 import ArchiveListResult
from ._models_py3 import ArchivePackageSourceProperties
from ._models_py3 import ArchiveProperties
from ._models_py3 import ArchiveUpdateParameters
from ._models_py3 import ArchiveVersion
from ._models_py3 import ArchiveVersionListResult
from ._models_py3 import ArtifactSyncEstimateResult
from ._models_py3 import ArtifactSyncScopeFilterProperties
from ._models_py3 import AuthCredential
from ._models_py3 import AzureADAuthenticationAsArmPolicy
from ._models_py3 import CacheRule
from ._models_py3 import CacheRuleArtifactSyncEstimateResult
from ._models_py3 import CacheRuleUpdateParameters
from ._models_py3 import CacheRulesListResult
from ._models_py3 import CallbackConfig
from ._models_py3 import ConnectedRegistry
from ._models_py3 import ConnectedRegistryListResult
from ._models_py3 import ConnectedRegistryUpdateParameters
from ._models_py3 import CredentialHealth
from ._models_py3 import CredentialSet
from ._models_py3 import CredentialSetListResult
from ._models_py3 import CredentialSetUpdateParameters
from ._models_py3 import DebianArchivePackageSourceProperties
from ._models_py3 import DebianArchiveProperties
from ._models_py3 import EncryptionProperty
from ._models_py3 import ErrorAdditionalInfo
from ._models_py3 import ErrorDetail
from ._models_py3 import ErrorResponse
from ._models_py3 import Event
from ._models_py3 import EventContent
from ._models_py3 import EventInfo
from ._models_py3 import EventListResult
from ._models_py3 import EventRequestMessage
from ._models_py3 import EventResponseMessage
from ._models_py3 import ExportPipeline
from ._models_py3 import ExportPipelineListResult
from ._models_py3 import ExportPipelineTargetProperties
from ._models_py3 import ExportPolicy
from ._models_py3 import GenerateCredentialsParameters
from ._models_py3 import GenerateCredentialsResult
from ._models_py3 import IPRule
from ._models_py3 import IdentityProperties
from ._models_py3 import ImportImageParameters
from ._models_py3 import ImportPipeline
from ._models_py3 import ImportPipelineListResult
from ._models_py3 import ImportPipelineSourceProperties
from ._models_py3 import ImportSource
from ._models_py3 import ImportSourceCredentials
from ._models_py3 import KeyVaultProperties
from ._models_py3 import LoggingProperties
from ._models_py3 import LoginServerProperties
from ._models_py3 import NetworkRuleSet
from ._models_py3 import OperationDefinition
from ._models_py3 import OperationDisplayDefinition
from ._models_py3 import OperationListResult
from ._models_py3 import OperationLogSpecificationDefinition
from ._models_py3 import OperationMetricSpecificationDefinition
from ._models_py3 import OperationServiceSpecificationDefinition
from ._models_py3 import ParentProperties
from ._models_py3 import PipelineRun
from ._models_py3 import PipelineRunListResult
from ._models_py3 import PipelineRunRequest
from ._models_py3 import PipelineRunResponse
from ._models_py3 import PipelineRunSourceProperties
from ._models_py3 import PipelineRunTargetProperties
from ._models_py3 import PipelineSourceTriggerDescriptor
from ._models_py3 import PipelineSourceTriggerProperties
from ._models_py3 import PipelineTriggerDescriptor
from ._models_py3 import PipelineTriggerProperties
from ._models_py3 import Policies
from ._models_py3 import PrivateEndpoint
from ._models_py3 import PrivateEndpointConnection
from ._models_py3 import PrivateEndpointConnectionListResult
from ._models_py3 import PrivateLinkResource
from ._models_py3 import PrivateLinkResourceListResult
from ._models_py3 import PrivateLinkServiceConnectionState
from ._models_py3 import ProgressProperties
from ._models_py3 import ProxyResource
from ._models_py3 import QuarantinePolicy
from ._models_py3 import RegenerateCredentialParameters
from ._models_py3 import Registry
from ._models_py3 import RegistryListCredentialsResult
from ._models_py3 import RegistryListResult
from ._models_py3 import RegistryNameCheckRequest
from ._models_py3 import RegistryNameStatus
from ._models_py3 import RegistryPassword
from ._models_py3 import RegistryUpdateParameters
from ._models_py3 import RegistryUsage
from ._models_py3 import RegistryUsageListResult
from ._models_py3 import Replication
from ._models_py3 import ReplicationListResult
from ._models_py3 import ReplicationUpdateParameters
from ._models_py3 import Request
from ._models_py3 import Resource
from ._models_py3 import RetentionPolicy
from ._models_py3 import ScopeMap
from ._models_py3 import ScopeMapListResult
from ._models_py3 import ScopeMapUpdateParameters
from ._models_py3 import Sku
from ._models_py3 import SoftDeletePolicy
from ._models_py3 import Source
from ._models_py3 import Status
from ._models_py3 import StatusDetailProperties
from ._models_py3 import StorageAccountProperties
from ._models_py3 import SyncProperties
from ._models_py3 import SyncUpdateProperties
from ._models_py3 import SystemData
from ._models_py3 import Target
from ._models_py3 import TlsCertificateProperties
from ._models_py3 import TlsProperties
from ._models_py3 import Token
from ._models_py3 import TokenCertificate
from ._models_py3 import TokenCredentialsProperties
from ._models_py3 import TokenListResult
from ._models_py3 import TokenPassword
from ._models_py3 import TokenUpdateParameters
from ._models_py3 import TrustPolicy
from ._models_py3 import UserIdentityProperties
from ._models_py3 import Webhook
from ._models_py3 import WebhookCreateParameters
from ._models_py3 import WebhookListResult
from ._models_py3 import WebhookUpdateParameters

from ._container_registry_management_client_enums import Action
from ._container_registry_management_client_enums import ActionsRequired
from ._container_registry_management_client_enums import ActivationStatus
from ._container_registry_management_client_enums import ArtifactSyncScopeFilterType
from ._container_registry_management_client_enums import ArtifactSyncStatus
from ._container_registry_management_client_enums import AuditLogStatus
from ._container_registry_management_client_enums import AzureADAuthenticationAsArmPolicyStatus
from ._container_registry_management_client_enums import CertificateType
from ._container_registry_management_client_enums import ConnectedRegistryMode
from ._container_registry_management_client_enums import ConnectionState
from ._container_registry_management_client_enums import ConnectionStatus
from ._container_registry_management_client_enums import CreatedByType
from ._container_registry_management_client_enums import CredentialHealthStatus
from ._container_registry_management_client_enums import CredentialName
from ._container_registry_management_client_enums import DefaultAction
from ._container_registry_management_client_enums import EncryptionStatus
from ._container_registry_management_client_enums import ExportPolicyStatus
from ._container_registry_management_client_enums import ImportMode
from ._container_registry_management_client_enums import LastModifiedByType
from ._container_registry_management_client_enums import LogLevel
from ._container_registry_management_client_enums import MetadataSearch
from ._container_registry_management_client_enums import NetworkRuleBypassOptions
from ._container_registry_management_client_enums import PackageSourceType
from ._container_registry_management_client_enums import PasswordName
from ._container_registry_management_client_enums import PipelineOptions
from ._container_registry_management_client_enums import PipelineRunSourceType
from ._container_registry_management_client_enums import PipelineRunTargetType
from ._container_registry_management_client_enums import PipelineSourceType
from ._container_registry_management_client_enums import PolicyStatus
from ._container_registry_management_client_enums import ProvisioningState
from ._container_registry_management_client_enums import PublicNetworkAccess
from ._container_registry_management_client_enums import RegistryUsageUnit
from ._container_registry_management_client_enums import ResourceIdentityType
from ._container_registry_management_client_enums import SkuName
from ._container_registry_management_client_enums import SkuTier
from ._container_registry_management_client_enums import TlsStatus
from ._container_registry_management_client_enums import TokenCertificateName
from ._container_registry_management_client_enums import TokenPasswordName
from ._container_registry_management_client_enums import TokenStatus
from ._container_registry_management_client_enums import TriggerStatus
from ._container_registry_management_client_enums import TrustPolicyType
from ._container_registry_management_client_enums import WebhookAction
from ._container_registry_management_client_enums import WebhookStatus
from ._container_registry_management_client_enums import ZoneRedundancy
from ._patch import __all__ as _patch_all
from ._patch import *  # pylint: disable=unused-wildcard-import
from ._patch import patch_sdk as _patch_sdk

__all__ = [
    "ActivationProperties",
    "ActiveDirectoryObject",
    "Actor",
    "Archive",
    "ArchiveListResult",
    "ArchivePackageSourceProperties",
    "ArchiveProperties",
    "ArchiveUpdateParameters",
    "ArchiveVersion",
    "ArchiveVersionListResult",
    "ArtifactSyncEstimateResult",
    "ArtifactSyncScopeFilterProperties",
    "AuthCredential",
    "AzureADAuthenticationAsArmPolicy",
    "CacheRule",
    "CacheRuleArtifactSyncEstimateResult",
    "CacheRuleUpdateParameters",
    "CacheRulesListResult",
    "CallbackConfig",
    "ConnectedRegistry",
    "ConnectedRegistryListResult",
    "ConnectedRegistryUpdateParameters",
    "CredentialHealth",
    "CredentialSet",
    "CredentialSetListResult",
    "CredentialSetUpdateParameters",
    "DebianArchivePackageSourceProperties",
    "DebianArchiveProperties",
    "EncryptionProperty",
    "ErrorAdditionalInfo",
    "ErrorDetail",
    "ErrorResponse",
    "Event",
    "EventContent",
    "EventInfo",
    "EventListResult",
    "EventRequestMessage",
    "EventResponseMessage",
    "ExportPipeline",
    "ExportPipelineListResult",
    "ExportPipelineTargetProperties",
    "ExportPolicy",
    "GenerateCredentialsParameters",
    "GenerateCredentialsResult",
    "IPRule",
    "IdentityProperties",
    "ImportImageParameters",
    "ImportPipeline",
    "ImportPipelineListResult",
    "ImportPipelineSourceProperties",
    "ImportSource",
    "ImportSourceCredentials",
    "KeyVaultProperties",
    "LoggingProperties",
    "LoginServerProperties",
    "NetworkRuleSet",
    "OperationDefinition",
    "OperationDisplayDefinition",
    "OperationListResult",
    "OperationLogSpecificationDefinition",
    "OperationMetricSpecificationDefinition",
    "OperationServiceSpecificationDefinition",
    "ParentProperties",
    "PipelineRun",
    "PipelineRunListResult",
    "PipelineRunRequest",
    "PipelineRunResponse",
    "PipelineRunSourceProperties",
    "PipelineRunTargetProperties",
    "PipelineSourceTriggerDescriptor",
    "PipelineSourceTriggerProperties",
    "PipelineTriggerDescriptor",
    "PipelineTriggerProperties",
    "Policies",
    "PrivateEndpoint",
    "PrivateEndpointConnection",
    "PrivateEndpointConnectionListResult",
    "PrivateLinkResource",
    "PrivateLinkResourceListResult",
    "PrivateLinkServiceConnectionState",
    "ProgressProperties",
    "ProxyResource",
    "QuarantinePolicy",
    "RegenerateCredentialParameters",
    "Registry",
    "RegistryListCredentialsResult",
    "RegistryListResult",
    "RegistryNameCheckRequest",
    "RegistryNameStatus",
    "RegistryPassword",
    "RegistryUpdateParameters",
    "RegistryUsage",
    "RegistryUsageListResult",
    "Replication",
    "ReplicationListResult",
    "ReplicationUpdateParameters",
    "Request",
    "Resource",
    "RetentionPolicy",
    "ScopeMap",
    "ScopeMapListResult",
    "ScopeMapUpdateParameters",
    "Sku",
    "SoftDeletePolicy",
    "Source",
    "Status",
    "StatusDetailProperties",
    "StorageAccountProperties",
    "SyncProperties",
    "SyncUpdateProperties",
    "SystemData",
    "Target",
    "TlsCertificateProperties",
    "TlsProperties",
    "Token",
    "TokenCertificate",
    "TokenCredentialsProperties",
    "TokenListResult",
    "TokenPassword",
    "TokenUpdateParameters",
    "TrustPolicy",
    "UserIdentityProperties",
    "Webhook",
    "WebhookCreateParameters",
    "WebhookListResult",
    "WebhookUpdateParameters",
    "Action",
    "ActionsRequired",
    "ActivationStatus",
    "ArtifactSyncScopeFilterType",
    "ArtifactSyncStatus",
    "AuditLogStatus",
    "AzureADAuthenticationAsArmPolicyStatus",
    "CertificateType",
    "ConnectedRegistryMode",
    "ConnectionState",
    "ConnectionStatus",
    "CreatedByType",
    "CredentialHealthStatus",
    "CredentialName",
    "DefaultAction",
    "EncryptionStatus",
    "ExportPolicyStatus",
    "ImportMode",
    "LastModifiedByType",
    "LogLevel",
    "MetadataSearch",
    "NetworkRuleBypassOptions",
    "PackageSourceType",
    "PasswordName",
    "PipelineOptions",
    "PipelineRunSourceType",
    "PipelineRunTargetType",
    "PipelineSourceType",
    "PolicyStatus",
    "ProvisioningState",
    "PublicNetworkAccess",
    "RegistryUsageUnit",
    "ResourceIdentityType",
    "SkuName",
    "SkuTier",
    "TlsStatus",
    "TokenCertificateName",
    "TokenPasswordName",
    "TokenStatus",
    "TriggerStatus",
    "TrustPolicyType",
    "WebhookAction",
    "WebhookStatus",
    "ZoneRedundancy",
]
__all__.extend([p for p in _patch_all if p not in __all__])
_patch_sdk()
