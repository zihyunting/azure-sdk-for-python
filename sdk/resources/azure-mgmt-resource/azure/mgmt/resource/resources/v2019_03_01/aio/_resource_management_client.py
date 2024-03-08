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
from ..._serialization import Deserializer, Serializer
from ._configuration import ResourceManagementClientConfiguration
from .operations import (
    DeploymentOperationsOperations,
    DeploymentsOperations,
    Operations,
    ProvidersOperations,
    ResourceGroupsOperations,
    ResourcesOperations,
    TagsOperations,
)

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from azure.core.credentials_async import AsyncTokenCredential


class ResourceManagementClient:  # pylint: disable=client-accepts-api-version-keyword,too-many-instance-attributes
    """Provides operations for working with resources and resource groups.

    :ivar operations: Operations operations
    :vartype operations: azure.mgmt.resource.resources.v2019_03_01.aio.operations.Operations
    :ivar deployments: DeploymentsOperations operations
    :vartype deployments:
     azure.mgmt.resource.resources.v2019_03_01.aio.operations.DeploymentsOperations
    :ivar providers: ProvidersOperations operations
    :vartype providers:
     azure.mgmt.resource.resources.v2019_03_01.aio.operations.ProvidersOperations
    :ivar resources: ResourcesOperations operations
    :vartype resources:
     azure.mgmt.resource.resources.v2019_03_01.aio.operations.ResourcesOperations
    :ivar resource_groups: ResourceGroupsOperations operations
    :vartype resource_groups:
     azure.mgmt.resource.resources.v2019_03_01.aio.operations.ResourceGroupsOperations
    :ivar tags: TagsOperations operations
    :vartype tags: azure.mgmt.resource.resources.v2019_03_01.aio.operations.TagsOperations
    :ivar deployment_operations: DeploymentOperationsOperations operations
    :vartype deployment_operations:
     azure.mgmt.resource.resources.v2019_03_01.aio.operations.DeploymentOperationsOperations
    :param credential: Credential needed for the client to connect to Azure. Required.
    :type credential: ~azure.core.credentials_async.AsyncTokenCredential
    :param subscription_id: The ID of the target subscription. Required.
    :type subscription_id: str
    :param base_url: Service URL. Default value is "https://management.azure.com".
    :type base_url: str
    :keyword api_version: Api Version. Default value is "2019-03-01". Note that overriding this
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
        self._config = ResourceManagementClientConfiguration(
            credential=credential, subscription_id=subscription_id, **kwargs
        )
        self._client: AsyncARMPipelineClient = AsyncARMPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in _models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)
        self._serialize.client_side_validation = False
        self.operations = Operations(self._client, self._config, self._serialize, self._deserialize, "2019-03-01")
        self.deployments = DeploymentsOperations(
            self._client, self._config, self._serialize, self._deserialize, "2019-03-01"
        )
        self.providers = ProvidersOperations(
            self._client, self._config, self._serialize, self._deserialize, "2019-03-01"
        )
        self.resources = ResourcesOperations(
            self._client, self._config, self._serialize, self._deserialize, "2019-03-01"
        )
        self.resource_groups = ResourceGroupsOperations(
            self._client, self._config, self._serialize, self._deserialize, "2019-03-01"
        )
        self.tags = TagsOperations(self._client, self._config, self._serialize, self._deserialize, "2019-03-01")
        self.deployment_operations = DeploymentOperationsOperations(
            self._client, self._config, self._serialize, self._deserialize, "2019-03-01"
        )

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

    async def __aenter__(self) -> "ResourceManagementClient":
        await self._client.__aenter__()
        return self

    async def __aexit__(self, *exc_details: Any) -> None:
        await self._client.__aexit__(*exc_details)
