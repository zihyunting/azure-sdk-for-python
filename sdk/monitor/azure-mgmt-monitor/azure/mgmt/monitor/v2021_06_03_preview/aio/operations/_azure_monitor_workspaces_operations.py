# pylint: disable=too-many-lines,too-many-statements
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from io import IOBase
from typing import Any, AsyncIterable, Callable, Dict, IO, Optional, TypeVar, Union, overload
import urllib.parse

from azure.core.async_paging import AsyncItemPaged, AsyncList
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
from azure.core.tracing.decorator import distributed_trace
from azure.core.tracing.decorator_async import distributed_trace_async
from azure.core.utils import case_insensitive_dict
from azure.mgmt.core.exceptions import ARMErrorFormat

from ... import models as _models
from ..._vendor import _convert_request
from ...operations._azure_monitor_workspaces_operations import (
    build_create_request,
    build_delete_request,
    build_get_request,
    build_list_by_resource_group_request,
    build_list_by_subscription_request,
    build_update_request,
)

T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class AzureMonitorWorkspacesOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.mgmt.monitor.v2021_06_03_preview.aio.MonitorManagementClient`'s
        :attr:`azure_monitor_workspaces` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs) -> None:
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")
        self._api_version = input_args.pop(0) if input_args else kwargs.pop("api_version")

    @distributed_trace
    def list_by_resource_group(
        self, resource_group_name: str, **kwargs: Any
    ) -> AsyncIterable["_models.AzureMonitorWorkspaceResource"]:
        """Lists all Azure Monitor Workspaces in the specified resource group.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :return: An iterator like instance of either AzureMonitorWorkspaceResource or the result of
         cls(response)
        :rtype:
         ~azure.core.async_paging.AsyncItemPaged[~azure.mgmt.monitor.v2021_06_03_preview.models.AzureMonitorWorkspaceResource]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop(
            "api_version", _params.pop("api-version", self._api_version or "2021-06-03-preview")
        )
        cls: ClsType[_models.AzureMonitorWorkspaceResourceListResult] = kwargs.pop("cls", None)

        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        def prepare_request(next_link=None):
            if not next_link:

                _request = build_list_by_resource_group_request(
                    resource_group_name=resource_group_name,
                    subscription_id=self._config.subscription_id,
                    api_version=api_version,
                    headers=_headers,
                    params=_params,
                )
                _request = _convert_request(_request)
                _request.url = self._client.format_url(_request.url)

            else:
                # make call to next link with the client's api-version
                _parsed_next_link = urllib.parse.urlparse(next_link)
                _next_request_params = case_insensitive_dict(
                    {
                        key: [urllib.parse.quote(v) for v in value]
                        for key, value in urllib.parse.parse_qs(_parsed_next_link.query).items()
                    }
                )
                _next_request_params["api-version"] = self._api_version
                _request = HttpRequest(
                    "GET", urllib.parse.urljoin(next_link, _parsed_next_link.path), params=_next_request_params
                )
                _request = _convert_request(_request)
                _request.url = self._client.format_url(_request.url)
                _request.method = "GET"
            return _request

        async def extract_data(pipeline_response):
            deserialized = self._deserialize("AzureMonitorWorkspaceResourceListResult", pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)  # type: ignore
            return deserialized.next_link or None, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            _request = prepare_request(next_link)

            _stream = False
            pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
                _request, stream=_stream, **kwargs
            )
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
                raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

            return pipeline_response

        return AsyncItemPaged(get_next, extract_data)

    @distributed_trace
    def list_by_subscription(self, **kwargs: Any) -> AsyncIterable["_models.AzureMonitorWorkspaceResource"]:
        """Lists all Azure Monitor Workspaces in the specified subscription.

        :return: An iterator like instance of either AzureMonitorWorkspaceResource or the result of
         cls(response)
        :rtype:
         ~azure.core.async_paging.AsyncItemPaged[~azure.mgmt.monitor.v2021_06_03_preview.models.AzureMonitorWorkspaceResource]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop(
            "api_version", _params.pop("api-version", self._api_version or "2021-06-03-preview")
        )
        cls: ClsType[_models.AzureMonitorWorkspaceResourceListResult] = kwargs.pop("cls", None)

        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        def prepare_request(next_link=None):
            if not next_link:

                _request = build_list_by_subscription_request(
                    subscription_id=self._config.subscription_id,
                    api_version=api_version,
                    headers=_headers,
                    params=_params,
                )
                _request = _convert_request(_request)
                _request.url = self._client.format_url(_request.url)

            else:
                # make call to next link with the client's api-version
                _parsed_next_link = urllib.parse.urlparse(next_link)
                _next_request_params = case_insensitive_dict(
                    {
                        key: [urllib.parse.quote(v) for v in value]
                        for key, value in urllib.parse.parse_qs(_parsed_next_link.query).items()
                    }
                )
                _next_request_params["api-version"] = self._api_version
                _request = HttpRequest(
                    "GET", urllib.parse.urljoin(next_link, _parsed_next_link.path), params=_next_request_params
                )
                _request = _convert_request(_request)
                _request.url = self._client.format_url(_request.url)
                _request.method = "GET"
            return _request

        async def extract_data(pipeline_response):
            deserialized = self._deserialize("AzureMonitorWorkspaceResourceListResult", pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)  # type: ignore
            return deserialized.next_link or None, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            _request = prepare_request(next_link)

            _stream = False
            pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
                _request, stream=_stream, **kwargs
            )
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
                raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

            return pipeline_response

        return AsyncItemPaged(get_next, extract_data)

    @distributed_trace_async
    async def get(
        self, resource_group_name: str, azure_monitor_workspace_name: str, **kwargs: Any
    ) -> _models.AzureMonitorWorkspaceResource:
        """Returns the specified Azure Monitor Workspace.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param azure_monitor_workspace_name: The name of the Azure Monitor Workspace. The name is case
         insensitive. Required.
        :type azure_monitor_workspace_name: str
        :return: AzureMonitorWorkspaceResource or the result of cls(response)
        :rtype: ~azure.mgmt.monitor.v2021_06_03_preview.models.AzureMonitorWorkspaceResource
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop(
            "api_version", _params.pop("api-version", self._api_version or "2021-06-03-preview")
        )
        cls: ClsType[_models.AzureMonitorWorkspaceResource] = kwargs.pop("cls", None)

        _request = build_get_request(
            resource_group_name=resource_group_name,
            azure_monitor_workspace_name=azure_monitor_workspace_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            headers=_headers,
            params=_params,
        )
        _request = _convert_request(_request)
        _request.url = self._client.format_url(_request.url)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize("AzureMonitorWorkspaceResource", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @overload
    async def create(
        self,
        resource_group_name: str,
        azure_monitor_workspace_name: str,
        azure_monitor_workspace_properties: _models.AzureMonitorWorkspaceResource,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.AzureMonitorWorkspaceResource:
        """Creates or updates an Azure Monitor Workspace.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param azure_monitor_workspace_name: The name of the Azure Monitor Workspace. The name is case
         insensitive. Required.
        :type azure_monitor_workspace_name: str
        :param azure_monitor_workspace_properties: Properties that need to be specified to create a new
         Azure Monitor Workspace. Required.
        :type azure_monitor_workspace_properties:
         ~azure.mgmt.monitor.v2021_06_03_preview.models.AzureMonitorWorkspaceResource
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: AzureMonitorWorkspaceResource or the result of cls(response)
        :rtype: ~azure.mgmt.monitor.v2021_06_03_preview.models.AzureMonitorWorkspaceResource
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def create(
        self,
        resource_group_name: str,
        azure_monitor_workspace_name: str,
        azure_monitor_workspace_properties: IO[bytes],
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.AzureMonitorWorkspaceResource:
        """Creates or updates an Azure Monitor Workspace.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param azure_monitor_workspace_name: The name of the Azure Monitor Workspace. The name is case
         insensitive. Required.
        :type azure_monitor_workspace_name: str
        :param azure_monitor_workspace_properties: Properties that need to be specified to create a new
         Azure Monitor Workspace. Required.
        :type azure_monitor_workspace_properties: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: AzureMonitorWorkspaceResource or the result of cls(response)
        :rtype: ~azure.mgmt.monitor.v2021_06_03_preview.models.AzureMonitorWorkspaceResource
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def create(
        self,
        resource_group_name: str,
        azure_monitor_workspace_name: str,
        azure_monitor_workspace_properties: Union[_models.AzureMonitorWorkspaceResource, IO[bytes]],
        **kwargs: Any
    ) -> _models.AzureMonitorWorkspaceResource:
        """Creates or updates an Azure Monitor Workspace.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param azure_monitor_workspace_name: The name of the Azure Monitor Workspace. The name is case
         insensitive. Required.
        :type azure_monitor_workspace_name: str
        :param azure_monitor_workspace_properties: Properties that need to be specified to create a new
         Azure Monitor Workspace. Is either a AzureMonitorWorkspaceResource type or a IO[bytes] type.
         Required.
        :type azure_monitor_workspace_properties:
         ~azure.mgmt.monitor.v2021_06_03_preview.models.AzureMonitorWorkspaceResource or IO[bytes]
        :return: AzureMonitorWorkspaceResource or the result of cls(response)
        :rtype: ~azure.mgmt.monitor.v2021_06_03_preview.models.AzureMonitorWorkspaceResource
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

        api_version: str = kwargs.pop(
            "api_version", _params.pop("api-version", self._api_version or "2021-06-03-preview")
        )
        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.AzureMonitorWorkspaceResource] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(azure_monitor_workspace_properties, (IOBase, bytes)):
            _content = azure_monitor_workspace_properties
        else:
            _json = self._serialize.body(azure_monitor_workspace_properties, "AzureMonitorWorkspaceResource")

        _request = build_create_request(
            resource_group_name=resource_group_name,
            azure_monitor_workspace_name=azure_monitor_workspace_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            content=_content,
            headers=_headers,
            params=_params,
        )
        _request = _convert_request(_request)
        _request.url = self._client.format_url(_request.url)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200, 201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if response.status_code == 200:
            deserialized = self._deserialize("AzureMonitorWorkspaceResource", pipeline_response)

        if response.status_code == 201:
            deserialized = self._deserialize("AzureMonitorWorkspaceResource", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @overload
    async def update(
        self,
        resource_group_name: str,
        azure_monitor_workspace_name: str,
        azure_monitor_workspace_properties: Optional[_models.AzureMonitorWorkspaceResourceForUpdate] = None,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.AzureMonitorWorkspaceResource:
        """Updates part of an Azure Monitor Workspace.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param azure_monitor_workspace_name: The name of the Azure Monitor Workspace. The name is case
         insensitive. Required.
        :type azure_monitor_workspace_name: str
        :param azure_monitor_workspace_properties: The payload. Default value is None.
        :type azure_monitor_workspace_properties:
         ~azure.mgmt.monitor.v2021_06_03_preview.models.AzureMonitorWorkspaceResourceForUpdate
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: AzureMonitorWorkspaceResource or the result of cls(response)
        :rtype: ~azure.mgmt.monitor.v2021_06_03_preview.models.AzureMonitorWorkspaceResource
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def update(
        self,
        resource_group_name: str,
        azure_monitor_workspace_name: str,
        azure_monitor_workspace_properties: Optional[IO[bytes]] = None,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.AzureMonitorWorkspaceResource:
        """Updates part of an Azure Monitor Workspace.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param azure_monitor_workspace_name: The name of the Azure Monitor Workspace. The name is case
         insensitive. Required.
        :type azure_monitor_workspace_name: str
        :param azure_monitor_workspace_properties: The payload. Default value is None.
        :type azure_monitor_workspace_properties: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: AzureMonitorWorkspaceResource or the result of cls(response)
        :rtype: ~azure.mgmt.monitor.v2021_06_03_preview.models.AzureMonitorWorkspaceResource
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def update(
        self,
        resource_group_name: str,
        azure_monitor_workspace_name: str,
        azure_monitor_workspace_properties: Optional[
            Union[_models.AzureMonitorWorkspaceResourceForUpdate, IO[bytes]]
        ] = None,
        **kwargs: Any
    ) -> _models.AzureMonitorWorkspaceResource:
        """Updates part of an Azure Monitor Workspace.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param azure_monitor_workspace_name: The name of the Azure Monitor Workspace. The name is case
         insensitive. Required.
        :type azure_monitor_workspace_name: str
        :param azure_monitor_workspace_properties: The payload. Is either a
         AzureMonitorWorkspaceResourceForUpdate type or a IO[bytes] type. Default value is None.
        :type azure_monitor_workspace_properties:
         ~azure.mgmt.monitor.v2021_06_03_preview.models.AzureMonitorWorkspaceResourceForUpdate or
         IO[bytes]
        :return: AzureMonitorWorkspaceResource or the result of cls(response)
        :rtype: ~azure.mgmt.monitor.v2021_06_03_preview.models.AzureMonitorWorkspaceResource
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

        api_version: str = kwargs.pop(
            "api_version", _params.pop("api-version", self._api_version or "2021-06-03-preview")
        )
        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.AzureMonitorWorkspaceResource] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(azure_monitor_workspace_properties, (IOBase, bytes)):
            _content = azure_monitor_workspace_properties
        else:
            if azure_monitor_workspace_properties is not None:
                _json = self._serialize.body(
                    azure_monitor_workspace_properties, "AzureMonitorWorkspaceResourceForUpdate"
                )
            else:
                _json = None

        _request = build_update_request(
            resource_group_name=resource_group_name,
            azure_monitor_workspace_name=azure_monitor_workspace_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            content=_content,
            headers=_headers,
            params=_params,
        )
        _request = _convert_request(_request)
        _request.url = self._client.format_url(_request.url)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize("AzureMonitorWorkspaceResource", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @distributed_trace_async
    async def delete(  # pylint: disable=inconsistent-return-statements
        self, resource_group_name: str, azure_monitor_workspace_name: str, **kwargs: Any
    ) -> None:
        """Deletes an Azure Monitor Workspace.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param azure_monitor_workspace_name: The name of the Azure Monitor Workspace. The name is case
         insensitive. Required.
        :type azure_monitor_workspace_name: str
        :return: None or the result of cls(response)
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop(
            "api_version", _params.pop("api-version", self._api_version or "2021-06-03-preview")
        )
        cls: ClsType[None] = kwargs.pop("cls", None)

        _request = build_delete_request(
            resource_group_name=resource_group_name,
            azure_monitor_workspace_name=azure_monitor_workspace_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            headers=_headers,
            params=_params,
        )
        _request = _convert_request(_request)
        _request.url = self._client.format_url(_request.url)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200, 204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})  # type: ignore
