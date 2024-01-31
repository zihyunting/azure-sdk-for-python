# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from io import IOBase
from typing import Any, Callable, Dict, IO, Optional, TypeVar, Union, overload

from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    ResourceNotModifiedError,
    map_error,
)
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator_async import distributed_trace_async
from azure.core.utils import case_insensitive_dict
from azure.mgmt.core.exceptions import ARMErrorFormat

from ... import models as _models
from ..._vendor import _convert_request
from ...operations._kusto_pool_child_resource_operations import build_check_name_availability_request

T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class KustoPoolChildResourceOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.mgmt.synapse.aio.SynapseManagementClient`'s
        :attr:`kusto_pool_child_resource` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs) -> None:
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @overload
    async def check_name_availability(
        self,
        workspace_name: str,
        kusto_pool_name: str,
        resource_group_name: str,
        resource_name: _models.DatabaseCheckNameRequest,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.CheckNameResult:
        """Checks that the Kusto Pool child resource name is valid and is not already in use.

        :param workspace_name: The name of the workspace. Required.
        :type workspace_name: str
        :param kusto_pool_name: The name of the Kusto pool. Required.
        :type kusto_pool_name: str
        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param resource_name: The name of the Kusto Pool child resource. Required.
        :type resource_name: ~azure.mgmt.synapse.models.DatabaseCheckNameRequest
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: CheckNameResult or the result of cls(response)
        :rtype: ~azure.mgmt.synapse.models.CheckNameResult
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def check_name_availability(
        self,
        workspace_name: str,
        kusto_pool_name: str,
        resource_group_name: str,
        resource_name: IO,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.CheckNameResult:
        """Checks that the Kusto Pool child resource name is valid and is not already in use.

        :param workspace_name: The name of the workspace. Required.
        :type workspace_name: str
        :param kusto_pool_name: The name of the Kusto pool. Required.
        :type kusto_pool_name: str
        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param resource_name: The name of the Kusto Pool child resource. Required.
        :type resource_name: IO
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: CheckNameResult or the result of cls(response)
        :rtype: ~azure.mgmt.synapse.models.CheckNameResult
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def check_name_availability(
        self,
        workspace_name: str,
        kusto_pool_name: str,
        resource_group_name: str,
        resource_name: Union[_models.DatabaseCheckNameRequest, IO],
        **kwargs: Any
    ) -> _models.CheckNameResult:
        """Checks that the Kusto Pool child resource name is valid and is not already in use.

        :param workspace_name: The name of the workspace. Required.
        :type workspace_name: str
        :param kusto_pool_name: The name of the Kusto pool. Required.
        :type kusto_pool_name: str
        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param resource_name: The name of the Kusto Pool child resource. Is either a
         DatabaseCheckNameRequest type or a IO type. Required.
        :type resource_name: ~azure.mgmt.synapse.models.DatabaseCheckNameRequest or IO
        :keyword content_type: Body Parameter content-type. Known values are: 'application/json'.
         Default value is None.
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: CheckNameResult or the result of cls(response)
        :rtype: ~azure.mgmt.synapse.models.CheckNameResult
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2021-06-01-preview"))
        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.CheckNameResult] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(resource_name, (IOBase, bytes)):
            _content = resource_name
        else:
            _json = self._serialize.body(resource_name, "DatabaseCheckNameRequest")

        request = build_check_name_availability_request(
            workspace_name=workspace_name,
            kusto_pool_name=kusto_pool_name,
            resource_group_name=resource_group_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            content=_content,
            template_url=self.check_name_availability.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize("CheckNameResult", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    check_name_availability.metadata = {
        "url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Synapse/workspaces/{workspaceName}/kustoPools/{kustoPoolName}/checkNameAvailability"
    }
