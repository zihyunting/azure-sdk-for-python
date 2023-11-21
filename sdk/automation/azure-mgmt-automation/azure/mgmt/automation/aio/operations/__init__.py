# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from ._private_endpoint_connections_operations import PrivateEndpointConnectionsOperations
from ._private_link_resources_operations import PrivateLinkResourcesOperations
from ._agent_registration_information_operations import AgentRegistrationInformationOperations
from ._dsc_node_operations import DscNodeOperations
from ._node_reports_operations import NodeReportsOperations
from ._dsc_compilation_job_operations import DscCompilationJobOperations
from ._dsc_compilation_job_stream_operations import DscCompilationJobStreamOperations
from ._node_count_information_operations import NodeCountInformationOperations
from ._watcher_operations import WatcherOperations
from ._software_update_configurations_operations import SoftwareUpdateConfigurationsOperations
from ._webhook_operations import WebhookOperations
from ._deleted_automation_accounts_operations import DeletedAutomationAccountsOperations
from ._automation_account_operations import AutomationAccountOperations
from ._statistics_operations import StatisticsOperations
from ._usages_operations import UsagesOperations
from ._keys_operations import KeysOperations
from ._certificate_operations import CertificateOperations
from ._connection_operations import ConnectionOperations
from ._connection_type_operations import ConnectionTypeOperations
from ._credential_operations import CredentialOperations
from ._dsc_configuration_operations import DscConfigurationOperations
from ._dsc_node_configuration_operations import DscNodeConfigurationOperations
from ._hybrid_runbook_workers_operations import HybridRunbookWorkersOperations
from ._hybrid_runbook_worker_group_operations import HybridRunbookWorkerGroupOperations
from ._job_operations import JobOperations
from ._job_stream_operations import JobStreamOperations
from ._job_schedule_operations import JobScheduleOperations
from ._linked_workspace_operations import LinkedWorkspaceOperations
from ._activity_operations import ActivityOperations
from ._module_operations import ModuleOperations
from ._object_data_types_operations import ObjectDataTypesOperations
from ._fields_operations import FieldsOperations
from ._power_shell72_module_operations import PowerShell72ModuleOperations
from ._operations import Operations
from ._automation_client_operations import AutomationClientOperationsMixin
from ._python2_package_operations import Python2PackageOperations
from ._python3_package_operations import Python3PackageOperations
from ._runbook_draft_operations import RunbookDraftOperations
from ._runbook_operations import RunbookOperations
from ._test_job_streams_operations import TestJobStreamsOperations
from ._test_job_operations import TestJobOperations
from ._schedule_operations import ScheduleOperations
from ._software_update_configuration_machine_runs_operations import SoftwareUpdateConfigurationMachineRunsOperations
from ._software_update_configuration_runs_operations import SoftwareUpdateConfigurationRunsOperations
from ._source_control_operations import SourceControlOperations
from ._source_control_sync_job_operations import SourceControlSyncJobOperations
from ._source_control_sync_job_streams_operations import SourceControlSyncJobStreamsOperations
from ._variable_operations import VariableOperations

from ._patch import __all__ as _patch_all
from ._patch import *  # pylint: disable=unused-wildcard-import
from ._patch import patch_sdk as _patch_sdk

__all__ = [
    "PrivateEndpointConnectionsOperations",
    "PrivateLinkResourcesOperations",
    "AgentRegistrationInformationOperations",
    "DscNodeOperations",
    "NodeReportsOperations",
    "DscCompilationJobOperations",
    "DscCompilationJobStreamOperations",
    "NodeCountInformationOperations",
    "WatcherOperations",
    "SoftwareUpdateConfigurationsOperations",
    "WebhookOperations",
    "DeletedAutomationAccountsOperations",
    "AutomationAccountOperations",
    "StatisticsOperations",
    "UsagesOperations",
    "KeysOperations",
    "CertificateOperations",
    "ConnectionOperations",
    "ConnectionTypeOperations",
    "CredentialOperations",
    "DscConfigurationOperations",
    "DscNodeConfigurationOperations",
    "HybridRunbookWorkersOperations",
    "HybridRunbookWorkerGroupOperations",
    "JobOperations",
    "JobStreamOperations",
    "JobScheduleOperations",
    "LinkedWorkspaceOperations",
    "ActivityOperations",
    "ModuleOperations",
    "ObjectDataTypesOperations",
    "FieldsOperations",
    "PowerShell72ModuleOperations",
    "Operations",
    "AutomationClientOperationsMixin",
    "Python2PackageOperations",
    "Python3PackageOperations",
    "RunbookDraftOperations",
    "RunbookOperations",
    "TestJobStreamsOperations",
    "TestJobOperations",
    "ScheduleOperations",
    "SoftwareUpdateConfigurationMachineRunsOperations",
    "SoftwareUpdateConfigurationRunsOperations",
    "SourceControlOperations",
    "SourceControlSyncJobOperations",
    "SourceControlSyncJobStreamsOperations",
    "VariableOperations",
]
__all__.extend([p for p in _patch_all if p not in __all__])
_patch_sdk()
