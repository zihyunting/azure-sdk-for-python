# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from copy import deepcopy
from typing import Any, Awaitable, TYPE_CHECKING

from azure.core.rest import AsyncHttpResponse, HttpRequest
from azure.mgmt.core import AsyncARMPipelineClient

from .. import models as _models
from .._serialization import Deserializer, Serializer
from ._configuration import DataProtectionClientConfiguration
from .operations import (
    BackupInstancesOperations,
    BackupPoliciesOperations,
    BackupVaultOperationResultsOperations,
    BackupVaultsOperations,
    DataProtectionOperations,
    DataProtectionOperationsOperations,
    ExportJobsOperationResultOperations,
    ExportJobsOperations,
    JobsOperations,
    OperationResultOperations,
    OperationStatusBackupVaultContextOperations,
    OperationStatusOperations,
    OperationStatusResourceGroupContextOperations,
    RecoveryPointsOperations,
    ResourceGuardsOperations,
    RestorableTimeRangesOperations,
)

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from azure.core.credentials_async import AsyncTokenCredential


class DataProtectionClient:  # pylint: disable=client-accepts-api-version-keyword,too-many-instance-attributes
    """Open API 2.0 Specs for Azure Data Protection service.

    :ivar backup_vaults: BackupVaultsOperations operations
    :vartype backup_vaults: azure.mgmt.dataprotection.aio.operations.BackupVaultsOperations
    :ivar operation_result: OperationResultOperations operations
    :vartype operation_result: azure.mgmt.dataprotection.aio.operations.OperationResultOperations
    :ivar operation_status: OperationStatusOperations operations
    :vartype operation_status: azure.mgmt.dataprotection.aio.operations.OperationStatusOperations
    :ivar operation_status_backup_vault_context: OperationStatusBackupVaultContextOperations
     operations
    :vartype operation_status_backup_vault_context:
     azure.mgmt.dataprotection.aio.operations.OperationStatusBackupVaultContextOperations
    :ivar operation_status_resource_group_context: OperationStatusResourceGroupContextOperations
     operations
    :vartype operation_status_resource_group_context:
     azure.mgmt.dataprotection.aio.operations.OperationStatusResourceGroupContextOperations
    :ivar backup_vault_operation_results: BackupVaultOperationResultsOperations operations
    :vartype backup_vault_operation_results:
     azure.mgmt.dataprotection.aio.operations.BackupVaultOperationResultsOperations
    :ivar data_protection: DataProtectionOperations operations
    :vartype data_protection: azure.mgmt.dataprotection.aio.operations.DataProtectionOperations
    :ivar data_protection_operations: DataProtectionOperationsOperations operations
    :vartype data_protection_operations:
     azure.mgmt.dataprotection.aio.operations.DataProtectionOperationsOperations
    :ivar backup_policies: BackupPoliciesOperations operations
    :vartype backup_policies: azure.mgmt.dataprotection.aio.operations.BackupPoliciesOperations
    :ivar backup_instances: BackupInstancesOperations operations
    :vartype backup_instances: azure.mgmt.dataprotection.aio.operations.BackupInstancesOperations
    :ivar recovery_points: RecoveryPointsOperations operations
    :vartype recovery_points: azure.mgmt.dataprotection.aio.operations.RecoveryPointsOperations
    :ivar jobs: JobsOperations operations
    :vartype jobs: azure.mgmt.dataprotection.aio.operations.JobsOperations
    :ivar restorable_time_ranges: RestorableTimeRangesOperations operations
    :vartype restorable_time_ranges:
     azure.mgmt.dataprotection.aio.operations.RestorableTimeRangesOperations
    :ivar export_jobs: ExportJobsOperations operations
    :vartype export_jobs: azure.mgmt.dataprotection.aio.operations.ExportJobsOperations
    :ivar export_jobs_operation_result: ExportJobsOperationResultOperations operations
    :vartype export_jobs_operation_result:
     azure.mgmt.dataprotection.aio.operations.ExportJobsOperationResultOperations
    :ivar resource_guards: ResourceGuardsOperations operations
    :vartype resource_guards: azure.mgmt.dataprotection.aio.operations.ResourceGuardsOperations
    :param credential: Credential needed for the client to connect to Azure. Required.
    :type credential: ~azure.core.credentials_async.AsyncTokenCredential
    :param subscription_id: The subscription Id. Required.
    :type subscription_id: str
    :param base_url: Service URL. Default value is "https://management.azure.com".
    :type base_url: str
    :keyword api_version: Api Version. Default value is "2023-02-01". Note that overriding this
     default value may result in unsupported behavior.
    :paramtype api_version: str
    :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
     Retry-After header is present.
    """

    def __init__(
        self,
        credential: "AsyncTokenCredential",
        subscription_id: str,
        base_url: str = "https://management.azure.com",
        **kwargs: Any
    ) -> None:
        self._config = DataProtectionClientConfiguration(
            credential=credential, subscription_id=subscription_id, **kwargs
        )
        self._client = AsyncARMPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in _models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)
        self._serialize.client_side_validation = False
        self.backup_vaults = BackupVaultsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.operation_result = OperationResultOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.operation_status = OperationStatusOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.operation_status_backup_vault_context = OperationStatusBackupVaultContextOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.operation_status_resource_group_context = OperationStatusResourceGroupContextOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.backup_vault_operation_results = BackupVaultOperationResultsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.data_protection = DataProtectionOperations(self._client, self._config, self._serialize, self._deserialize)
        self.data_protection_operations = DataProtectionOperationsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.backup_policies = BackupPoliciesOperations(self._client, self._config, self._serialize, self._deserialize)
        self.backup_instances = BackupInstancesOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.recovery_points = RecoveryPointsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.jobs = JobsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.restorable_time_ranges = RestorableTimeRangesOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.export_jobs = ExportJobsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.export_jobs_operation_result = ExportJobsOperationResultOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.resource_guards = ResourceGuardsOperations(self._client, self._config, self._serialize, self._deserialize)

    def _send_request(self, request: HttpRequest, **kwargs: Any) -> Awaitable[AsyncHttpResponse]:
        """Runs the network request through the client's chained policies.

        >>> from azure.core.rest import HttpRequest
        >>> request = HttpRequest("GET", "https://www.example.org/")
        <HttpRequest [GET], url: 'https://www.example.org/'>
        >>> response = await client._send_request(request)
        <AsyncHttpResponse: 200 OK>

        For more information on this code flow, see https://aka.ms/azsdk/dpcodegen/python/send_request

        :param request: The network request you want to make. Required.
        :type request: ~azure.core.rest.HttpRequest
        :keyword bool stream: Whether the response payload will be streamed. Defaults to False.
        :return: The response of your network call. Does not do error handling on your response.
        :rtype: ~azure.core.rest.AsyncHttpResponse
        """

        request_copy = deepcopy(request)
        request_copy.url = self._client.format_url(request_copy.url)
        return self._client.send_request(request_copy, **kwargs)

    async def close(self) -> None:
        await self._client.close()

    async def __aenter__(self) -> "DataProtectionClient":
        await self._client.__aenter__()
        return self

    async def __aexit__(self, *exc_details) -> None:
        await self._client.__aexit__(*exc_details)
