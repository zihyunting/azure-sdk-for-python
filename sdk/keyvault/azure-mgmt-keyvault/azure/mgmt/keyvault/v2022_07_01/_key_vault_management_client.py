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
from .._serialization import Deserializer, Serializer
from ._configuration import KeyVaultManagementClientConfiguration
from .operations import (
    KeysOperations,
    MHSMPrivateEndpointConnectionsOperations,
    MHSMPrivateLinkResourcesOperations,
    ManagedHsmsOperations,
    Operations,
    PrivateEndpointConnectionsOperations,
    PrivateLinkResourcesOperations,
    SecretsOperations,
    VaultsOperations,
)

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from azure.core.credentials import TokenCredential


class KeyVaultManagementClient:  # pylint: disable=client-accepts-api-version-keyword,too-many-instance-attributes
    """The Azure management API provides a RESTful set of web services that interact with Azure Key
    Vault.

    :ivar keys: KeysOperations operations
    :vartype keys: azure.mgmt.keyvault.v2022_07_01.operations.KeysOperations
    :ivar vaults: VaultsOperations operations
    :vartype vaults: azure.mgmt.keyvault.v2022_07_01.operations.VaultsOperations
    :ivar private_endpoint_connections: PrivateEndpointConnectionsOperations operations
    :vartype private_endpoint_connections:
     azure.mgmt.keyvault.v2022_07_01.operations.PrivateEndpointConnectionsOperations
    :ivar private_link_resources: PrivateLinkResourcesOperations operations
    :vartype private_link_resources:
     azure.mgmt.keyvault.v2022_07_01.operations.PrivateLinkResourcesOperations
    :ivar managed_hsms: ManagedHsmsOperations operations
    :vartype managed_hsms: azure.mgmt.keyvault.v2022_07_01.operations.ManagedHsmsOperations
    :ivar mhsm_private_endpoint_connections: MHSMPrivateEndpointConnectionsOperations operations
    :vartype mhsm_private_endpoint_connections:
     azure.mgmt.keyvault.v2022_07_01.operations.MHSMPrivateEndpointConnectionsOperations
    :ivar mhsm_private_link_resources: MHSMPrivateLinkResourcesOperations operations
    :vartype mhsm_private_link_resources:
     azure.mgmt.keyvault.v2022_07_01.operations.MHSMPrivateLinkResourcesOperations
    :ivar operations: Operations operations
    :vartype operations: azure.mgmt.keyvault.v2022_07_01.operations.Operations
    :ivar secrets: SecretsOperations operations
    :vartype secrets: azure.mgmt.keyvault.v2022_07_01.operations.SecretsOperations
    :param credential: Credential needed for the client to connect to Azure. Required.
    :type credential: ~azure.core.credentials.TokenCredential
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure
     subscription. The subscription ID forms part of the URI for every service call. Required.
    :type subscription_id: str
    :param base_url: Service URL. Default value is "https://management.azure.com".
    :type base_url: str
    :keyword api_version: Api Version. Default value is "2022-07-01". Note that overriding this
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
        self._config = KeyVaultManagementClientConfiguration(
            credential=credential, subscription_id=subscription_id, **kwargs
        )
        self._client = ARMPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)
        self._serialize.client_side_validation = False
        self.keys = KeysOperations(self._client, self._config, self._serialize, self._deserialize)
        self.vaults = VaultsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.private_endpoint_connections = PrivateEndpointConnectionsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.private_link_resources = PrivateLinkResourcesOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.managed_hsms = ManagedHsmsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.mhsm_private_endpoint_connections = MHSMPrivateEndpointConnectionsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.mhsm_private_link_resources = MHSMPrivateLinkResourcesOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.operations = Operations(self._client, self._config, self._serialize, self._deserialize)
        self.secrets = SecretsOperations(self._client, self._config, self._serialize, self._deserialize)

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
        # type: () -> KeyVaultManagementClient
        self._client.__enter__()
        return self

    def __exit__(self, *exc_details):
        # type: (Any) -> None
        self._client.__exit__(*exc_details)
