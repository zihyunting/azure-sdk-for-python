# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from copy import deepcopy
from typing import Any, TYPE_CHECKING

from azure.core.pipeline import policies
from azure.core.rest import HttpRequest, HttpResponse
from azure.mgmt.core import ARMPipelineClient
from azure.mgmt.core.policies import ARMAutoResourceProviderRegistrationPolicy

from . import models as _models
from ._configuration import PostgreSQLManagementClientConfiguration
from ._serialization import Deserializer, Serializer
from .operations import (
    CheckNameAvailabilityOperations,
    ConfigurationsOperations,
    DatabasesOperations,
    FirewallRulesOperations,
    LocationBasedPerformanceTierOperations,
    LogFilesOperations,
    Operations,
    PrivateEndpointConnectionsOperations,
    PrivateLinkResourcesOperations,
    RecoverableServersOperations,
    ReplicasOperations,
    ServerAdministratorsOperations,
    ServerBasedPerformanceTierOperations,
    ServerKeysOperations,
    ServerParametersOperations,
    ServerSecurityAlertPoliciesOperations,
    ServersOperations,
    VirtualNetworkRulesOperations,
)

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from azure.core.credentials import TokenCredential


class PostgreSQLManagementClient:  # pylint: disable=client-accepts-api-version-keyword,too-many-instance-attributes
    """The Microsoft Azure management API provides create, read, update, and delete functionality for
    Azure PostgreSQL resources including servers, databases, firewall rules, VNET rules, security
    alert policies, log files and configurations with new business model.

    :ivar servers: ServersOperations operations
    :vartype servers: azure.mgmt.rdbms.postgresql.operations.ServersOperations
    :ivar replicas: ReplicasOperations operations
    :vartype replicas: azure.mgmt.rdbms.postgresql.operations.ReplicasOperations
    :ivar firewall_rules: FirewallRulesOperations operations
    :vartype firewall_rules: azure.mgmt.rdbms.postgresql.operations.FirewallRulesOperations
    :ivar virtual_network_rules: VirtualNetworkRulesOperations operations
    :vartype virtual_network_rules:
     azure.mgmt.rdbms.postgresql.operations.VirtualNetworkRulesOperations
    :ivar databases: DatabasesOperations operations
    :vartype databases: azure.mgmt.rdbms.postgresql.operations.DatabasesOperations
    :ivar configurations: ConfigurationsOperations operations
    :vartype configurations: azure.mgmt.rdbms.postgresql.operations.ConfigurationsOperations
    :ivar server_parameters: ServerParametersOperations operations
    :vartype server_parameters: azure.mgmt.rdbms.postgresql.operations.ServerParametersOperations
    :ivar log_files: LogFilesOperations operations
    :vartype log_files: azure.mgmt.rdbms.postgresql.operations.LogFilesOperations
    :ivar server_administrators: ServerAdministratorsOperations operations
    :vartype server_administrators:
     azure.mgmt.rdbms.postgresql.operations.ServerAdministratorsOperations
    :ivar recoverable_servers: RecoverableServersOperations operations
    :vartype recoverable_servers:
     azure.mgmt.rdbms.postgresql.operations.RecoverableServersOperations
    :ivar server_based_performance_tier: ServerBasedPerformanceTierOperations operations
    :vartype server_based_performance_tier:
     azure.mgmt.rdbms.postgresql.operations.ServerBasedPerformanceTierOperations
    :ivar location_based_performance_tier: LocationBasedPerformanceTierOperations operations
    :vartype location_based_performance_tier:
     azure.mgmt.rdbms.postgresql.operations.LocationBasedPerformanceTierOperations
    :ivar check_name_availability: CheckNameAvailabilityOperations operations
    :vartype check_name_availability:
     azure.mgmt.rdbms.postgresql.operations.CheckNameAvailabilityOperations
    :ivar operations: Operations operations
    :vartype operations: azure.mgmt.rdbms.postgresql.operations.Operations
    :ivar server_security_alert_policies: ServerSecurityAlertPoliciesOperations operations
    :vartype server_security_alert_policies:
     azure.mgmt.rdbms.postgresql.operations.ServerSecurityAlertPoliciesOperations
    :ivar private_endpoint_connections: PrivateEndpointConnectionsOperations operations
    :vartype private_endpoint_connections:
     azure.mgmt.rdbms.postgresql.operations.PrivateEndpointConnectionsOperations
    :ivar private_link_resources: PrivateLinkResourcesOperations operations
    :vartype private_link_resources:
     azure.mgmt.rdbms.postgresql.operations.PrivateLinkResourcesOperations
    :ivar server_keys: ServerKeysOperations operations
    :vartype server_keys: azure.mgmt.rdbms.postgresql.operations.ServerKeysOperations
    :param credential: Credential needed for the client to connect to Azure. Required.
    :type credential: ~azure.core.credentials.TokenCredential
    :param subscription_id: The ID of the target subscription. Required.
    :type subscription_id: str
    :param base_url: Service URL. Default value is "https://management.azure.com".
    :type base_url: str
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
        self._config = PostgreSQLManagementClientConfiguration(
            credential=credential, subscription_id=subscription_id, **kwargs
        )
        _policies = kwargs.pop("policies", None)
        if _policies is None:
            _policies = [
                policies.RequestIdPolicy(**kwargs),
                self._config.headers_policy,
                self._config.user_agent_policy,
                self._config.proxy_policy,
                policies.ContentDecodePolicy(**kwargs),
                ARMAutoResourceProviderRegistrationPolicy(),
                self._config.redirect_policy,
                self._config.retry_policy,
                self._config.authentication_policy,
                self._config.custom_hook_policy,
                self._config.logging_policy,
                policies.DistributedTracingPolicy(**kwargs),
                policies.SensitiveHeaderCleanupPolicy(**kwargs) if self._config.redirect_policy else None,
                self._config.http_logging_policy,
            ]
        self._client: ARMPipelineClient = ARMPipelineClient(base_url=base_url, policies=_policies, **kwargs)

        client_models = {k: v for k, v in _models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)
        self._serialize.client_side_validation = False
        self.servers = ServersOperations(self._client, self._config, self._serialize, self._deserialize)
        self.replicas = ReplicasOperations(self._client, self._config, self._serialize, self._deserialize)
        self.firewall_rules = FirewallRulesOperations(self._client, self._config, self._serialize, self._deserialize)
        self.virtual_network_rules = VirtualNetworkRulesOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.databases = DatabasesOperations(self._client, self._config, self._serialize, self._deserialize)
        self.configurations = ConfigurationsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.server_parameters = ServerParametersOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.log_files = LogFilesOperations(self._client, self._config, self._serialize, self._deserialize)
        self.server_administrators = ServerAdministratorsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.recoverable_servers = RecoverableServersOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.server_based_performance_tier = ServerBasedPerformanceTierOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.location_based_performance_tier = LocationBasedPerformanceTierOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.check_name_availability = CheckNameAvailabilityOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.operations = Operations(self._client, self._config, self._serialize, self._deserialize)
        self.server_security_alert_policies = ServerSecurityAlertPoliciesOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.private_endpoint_connections = PrivateEndpointConnectionsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.private_link_resources = PrivateLinkResourcesOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.server_keys = ServerKeysOperations(self._client, self._config, self._serialize, self._deserialize)

    def _send_request(self, request: HttpRequest, *, stream: bool = False, **kwargs: Any) -> HttpResponse:
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
        return self._client.send_request(request_copy, stream=stream, **kwargs)  # type: ignore

    def close(self) -> None:
        self._client.close()

    def __enter__(self) -> "PostgreSQLManagementClient":
        self._client.__enter__()
        return self

    def __exit__(self, *exc_details: Any) -> None:
        self._client.__exit__(*exc_details)
