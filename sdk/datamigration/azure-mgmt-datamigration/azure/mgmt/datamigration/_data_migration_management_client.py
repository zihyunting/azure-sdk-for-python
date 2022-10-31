# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from copy import deepcopy
from typing import Any, TYPE_CHECKING

from azure.core.rest import HttpRequest, HttpResponse
from azure.mgmt.core import ARMPipelineClient

from . import models
from ._configuration import DataMigrationManagementClientConfiguration
from ._serialization import Deserializer, Serializer
from .operations import (
    DatabaseMigrationsSqlDbOperations,
    DatabaseMigrationsSqlMiOperations,
    DatabaseMigrationsSqlVmOperations,
    FilesOperations,
    Operations,
    ProjectsOperations,
    ResourceSkusOperations,
    ServiceTasksOperations,
    ServicesOperations,
    SqlMigrationServicesOperations,
    TasksOperations,
    UsagesOperations,
)

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from azure.core.credentials import TokenCredential


class DataMigrationManagementClient:  # pylint: disable=client-accepts-api-version-keyword,too-many-instance-attributes
    """Data Migration Client.

    :ivar database_migrations_sql_db: DatabaseMigrationsSqlDbOperations operations
    :vartype database_migrations_sql_db:
     azure.mgmt.datamigration.operations.DatabaseMigrationsSqlDbOperations
    :ivar database_migrations_sql_mi: DatabaseMigrationsSqlMiOperations operations
    :vartype database_migrations_sql_mi:
     azure.mgmt.datamigration.operations.DatabaseMigrationsSqlMiOperations
    :ivar database_migrations_sql_vm: DatabaseMigrationsSqlVmOperations operations
    :vartype database_migrations_sql_vm:
     azure.mgmt.datamigration.operations.DatabaseMigrationsSqlVmOperations
    :ivar operations: Operations operations
    :vartype operations: azure.mgmt.datamigration.operations.Operations
    :ivar sql_migration_services: SqlMigrationServicesOperations operations
    :vartype sql_migration_services:
     azure.mgmt.datamigration.operations.SqlMigrationServicesOperations
    :ivar resource_skus: ResourceSkusOperations operations
    :vartype resource_skus: azure.mgmt.datamigration.operations.ResourceSkusOperations
    :ivar services: ServicesOperations operations
    :vartype services: azure.mgmt.datamigration.operations.ServicesOperations
    :ivar tasks: TasksOperations operations
    :vartype tasks: azure.mgmt.datamigration.operations.TasksOperations
    :ivar service_tasks: ServiceTasksOperations operations
    :vartype service_tasks: azure.mgmt.datamigration.operations.ServiceTasksOperations
    :ivar projects: ProjectsOperations operations
    :vartype projects: azure.mgmt.datamigration.operations.ProjectsOperations
    :ivar usages: UsagesOperations operations
    :vartype usages: azure.mgmt.datamigration.operations.UsagesOperations
    :ivar files: FilesOperations operations
    :vartype files: azure.mgmt.datamigration.operations.FilesOperations
    :param credential: Credential needed for the client to connect to Azure. Required.
    :type credential: ~azure.core.credentials.TokenCredential
    :param subscription_id: Subscription ID that identifies an Azure subscription. Required.
    :type subscription_id: str
    :param base_url: Service URL. Default value is "https://management.azure.com".
    :type base_url: str
    :keyword api_version: Api Version. Default value is "2022-10-31-preview". Note that overriding
     this default value may result in unsupported behavior.
    :paramtype api_version: str
    :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
     Retry-After header is present.
    """

    def __init__(
        self,
        credential: "TokenCredential",
        subscription_id: str,
        base_url: str = "https://management.azure.com",
        **kwargs: Any
    ) -> None:
        self._config = DataMigrationManagementClientConfiguration(
            credential=credential, subscription_id=subscription_id, **kwargs
        )
        self._client = ARMPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)
        self._serialize.client_side_validation = False
        self.database_migrations_sql_db = DatabaseMigrationsSqlDbOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.database_migrations_sql_mi = DatabaseMigrationsSqlMiOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.database_migrations_sql_vm = DatabaseMigrationsSqlVmOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.operations = Operations(self._client, self._config, self._serialize, self._deserialize)
        self.sql_migration_services = SqlMigrationServicesOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.resource_skus = ResourceSkusOperations(self._client, self._config, self._serialize, self._deserialize)
        self.services = ServicesOperations(self._client, self._config, self._serialize, self._deserialize)
        self.tasks = TasksOperations(self._client, self._config, self._serialize, self._deserialize)
        self.service_tasks = ServiceTasksOperations(self._client, self._config, self._serialize, self._deserialize)
        self.projects = ProjectsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.usages = UsagesOperations(self._client, self._config, self._serialize, self._deserialize)
        self.files = FilesOperations(self._client, self._config, self._serialize, self._deserialize)

    def _send_request(self, request: HttpRequest, **kwargs: Any) -> HttpResponse:
        """Runs the network request through the client's chained policies.

        >>> from azure.core.rest import HttpRequest
        >>> request = HttpRequest("GET", "https://www.example.org/")
        <HttpRequest [GET], url: 'https://www.example.org/'>
        >>> response = client._send_request(request)
        <HttpResponse: 200 OK>

        For more information on this code flow, see https://aka.ms/azsdk/dpcodegen/python/send_request

        :param request: The network request you want to make. Required.
        :type request: ~azure.core.rest.HttpRequest
        :keyword bool stream: Whether the response payload will be streamed. Defaults to False.
        :return: The response of your network call. Does not do error handling on your response.
        :rtype: ~azure.core.rest.HttpResponse
        """

        request_copy = deepcopy(request)
        request_copy.url = self._client.format_url(request_copy.url)
        return self._client.send_request(request_copy, **kwargs)

    def close(self):
        # type: () -> None
        self._client.close()

    def __enter__(self):
        # type: () -> DataMigrationManagementClient
        self._client.__enter__()
        return self

    def __exit__(self, *exc_details):
        # type: (Any) -> None
        self._client.__exit__(*exc_details)
