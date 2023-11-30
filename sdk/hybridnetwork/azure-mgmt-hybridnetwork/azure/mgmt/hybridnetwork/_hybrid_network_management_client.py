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

from . import models as _models
from ._configuration import HybridNetworkManagementClientConfiguration
from ._serialization import Deserializer, Serializer
from .operations import (
    ArtifactManifestsOperations,
    ArtifactStoresOperations,
    ComponentsOperations,
    ConfigurationGroupSchemasOperations,
    ConfigurationGroupValuesOperations,
    NetworkFunctionDefinitionGroupsOperations,
    NetworkFunctionDefinitionVersionsOperations,
    NetworkFunctionsOperations,
    NetworkServiceDesignGroupsOperations,
    NetworkServiceDesignVersionsOperations,
    Operations,
    ProxyArtifactOperations,
    PublishersOperations,
    SiteNetworkServicesOperations,
    SitesOperations,
)

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from azure.core.credentials import TokenCredential


class HybridNetworkManagementClient:  # pylint: disable=client-accepts-api-version-keyword,too-many-instance-attributes
    """The definitions in this swagger specification will be used to manage the Hybrid Network
    resources.

    :ivar configuration_group_schemas: ConfigurationGroupSchemasOperations operations
    :vartype configuration_group_schemas:
     azure.mgmt.hybridnetwork.operations.ConfigurationGroupSchemasOperations
    :ivar configuration_group_values: ConfigurationGroupValuesOperations operations
    :vartype configuration_group_values:
     azure.mgmt.hybridnetwork.operations.ConfigurationGroupValuesOperations
    :ivar network_functions: NetworkFunctionsOperations operations
    :vartype network_functions: azure.mgmt.hybridnetwork.operations.NetworkFunctionsOperations
    :ivar components: ComponentsOperations operations
    :vartype components: azure.mgmt.hybridnetwork.operations.ComponentsOperations
    :ivar network_function_definition_groups: NetworkFunctionDefinitionGroupsOperations operations
    :vartype network_function_definition_groups:
     azure.mgmt.hybridnetwork.operations.NetworkFunctionDefinitionGroupsOperations
    :ivar network_function_definition_versions: NetworkFunctionDefinitionVersionsOperations
     operations
    :vartype network_function_definition_versions:
     azure.mgmt.hybridnetwork.operations.NetworkFunctionDefinitionVersionsOperations
    :ivar network_service_design_groups: NetworkServiceDesignGroupsOperations operations
    :vartype network_service_design_groups:
     azure.mgmt.hybridnetwork.operations.NetworkServiceDesignGroupsOperations
    :ivar network_service_design_versions: NetworkServiceDesignVersionsOperations operations
    :vartype network_service_design_versions:
     azure.mgmt.hybridnetwork.operations.NetworkServiceDesignVersionsOperations
    :ivar operations: Operations operations
    :vartype operations: azure.mgmt.hybridnetwork.operations.Operations
    :ivar publishers: PublishersOperations operations
    :vartype publishers: azure.mgmt.hybridnetwork.operations.PublishersOperations
    :ivar artifact_stores: ArtifactStoresOperations operations
    :vartype artifact_stores: azure.mgmt.hybridnetwork.operations.ArtifactStoresOperations
    :ivar artifact_manifests: ArtifactManifestsOperations operations
    :vartype artifact_manifests: azure.mgmt.hybridnetwork.operations.ArtifactManifestsOperations
    :ivar proxy_artifact: ProxyArtifactOperations operations
    :vartype proxy_artifact: azure.mgmt.hybridnetwork.operations.ProxyArtifactOperations
    :ivar sites: SitesOperations operations
    :vartype sites: azure.mgmt.hybridnetwork.operations.SitesOperations
    :ivar site_network_services: SiteNetworkServicesOperations operations
    :vartype site_network_services:
     azure.mgmt.hybridnetwork.operations.SiteNetworkServicesOperations
    :param credential: Credential needed for the client to connect to Azure. Required.
    :type credential: ~azure.core.credentials.TokenCredential
    :param subscription_id: The ID of the target subscription. Required.
    :type subscription_id: str
    :param base_url: Service URL. Default value is "https://management.azure.com".
    :type base_url: str
    :keyword api_version: Api Version. Default value is "2023-10-01". Note that overriding this
     default value may result in unsupported behavior.
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
        self._config = HybridNetworkManagementClientConfiguration(
            credential=credential, subscription_id=subscription_id, **kwargs
        )
        self._client: ARMPipelineClient = ARMPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in _models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)
        self._serialize.client_side_validation = False
        self.configuration_group_schemas = ConfigurationGroupSchemasOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.configuration_group_values = ConfigurationGroupValuesOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.network_functions = NetworkFunctionsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.components = ComponentsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.network_function_definition_groups = NetworkFunctionDefinitionGroupsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.network_function_definition_versions = NetworkFunctionDefinitionVersionsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.network_service_design_groups = NetworkServiceDesignGroupsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.network_service_design_versions = NetworkServiceDesignVersionsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.operations = Operations(self._client, self._config, self._serialize, self._deserialize)
        self.publishers = PublishersOperations(self._client, self._config, self._serialize, self._deserialize)
        self.artifact_stores = ArtifactStoresOperations(self._client, self._config, self._serialize, self._deserialize)
        self.artifact_manifests = ArtifactManifestsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.proxy_artifact = ProxyArtifactOperations(self._client, self._config, self._serialize, self._deserialize)
        self.sites = SitesOperations(self._client, self._config, self._serialize, self._deserialize)
        self.site_network_services = SiteNetworkServicesOperations(
            self._client, self._config, self._serialize, self._deserialize
        )

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

    def close(self) -> None:
        self._client.close()

    def __enter__(self) -> "HybridNetworkManagementClient":
        self._client.__enter__()
        return self

    def __exit__(self, *exc_details: Any) -> None:
        self._client.__exit__(*exc_details)
