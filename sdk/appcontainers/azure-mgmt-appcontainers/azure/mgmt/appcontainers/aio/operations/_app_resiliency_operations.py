# pylint: disable=too-many-lines
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
from ...operations._app_resiliency_operations import (
    build_create_or_update_request,
    build_delete_request,
    build_get_request,
    build_list_request,
    build_update_request,
)
from .._vendor import ContainerAppsAPIClientMixinABC

T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class AppResiliencyOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.mgmt.appcontainers.aio.ContainerAppsAPIClient`'s
        :attr:`app_resiliency` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs) -> None:
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @overload
    async def create_or_update(
        self,
        resource_group_name: str,
        app_name: str,
        name: str,
        resiliency_envelope: _models.AppResiliency,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.AppResiliency:
        """Create or update an application's resiliency policy.

        Create or update container app resiliency policy.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param app_name: Name of the Container App. Required.
        :type app_name: str
        :param name: Name of the resiliency policy. Required.
        :type name: str
        :param resiliency_envelope: The resiliency policy to create or update. Required.
        :type resiliency_envelope: ~azure.mgmt.appcontainers.models.AppResiliency
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: AppResiliency or the result of cls(response)
        :rtype: ~azure.mgmt.appcontainers.models.AppResiliency
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def create_or_update(
        self,
        resource_group_name: str,
        app_name: str,
        name: str,
        resiliency_envelope: IO,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.AppResiliency:
        """Create or update an application's resiliency policy.

        Create or update container app resiliency policy.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param app_name: Name of the Container App. Required.
        :type app_name: str
        :param name: Name of the resiliency policy. Required.
        :type name: str
        :param resiliency_envelope: The resiliency policy to create or update. Required.
        :type resiliency_envelope: IO
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: AppResiliency or the result of cls(response)
        :rtype: ~azure.mgmt.appcontainers.models.AppResiliency
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def create_or_update(
        self,
        resource_group_name: str,
        app_name: str,
        name: str,
        resiliency_envelope: Union[_models.AppResiliency, IO],
        **kwargs: Any
    ) -> _models.AppResiliency:
        """Create or update an application's resiliency policy.

        Create or update container app resiliency policy.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param app_name: Name of the Container App. Required.
        :type app_name: str
        :param name: Name of the resiliency policy. Required.
        :type name: str
        :param resiliency_envelope: The resiliency policy to create or update. Is either a
         AppResiliency type or a IO type. Required.
        :type resiliency_envelope: ~azure.mgmt.appcontainers.models.AppResiliency or IO
        :keyword content_type: Body Parameter content-type. Known values are: 'application/json'.
         Default value is None.
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: AppResiliency or the result of cls(response)
        :rtype: ~azure.mgmt.appcontainers.models.AppResiliency
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

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))
        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.AppResiliency] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(resiliency_envelope, (IOBase, bytes)):
            _content = resiliency_envelope
        else:
            _json = self._serialize.body(resiliency_envelope, "AppResiliency")

        request = build_create_or_update_request(
            resource_group_name=resource_group_name,
            app_name=app_name,
            name=name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            content=_content,
            template_url=self.create_or_update.metadata["url"],
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

        if response.status_code not in [200, 201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.DefaultErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if response.status_code == 200:
            deserialized = self._deserialize("AppResiliency", pipeline_response)

        if response.status_code == 201:
            deserialized = self._deserialize("AppResiliency", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    create_or_update.metadata = {
        "url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.App/containerApps/{appName}/resiliencyPolicies/{name}"
    }

    @overload
    async def update(
        self,
        resource_group_name: str,
        app_name: str,
        name: str,
        resiliency_envelope: _models.AppResiliency,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.AppResiliency:
        """Update an application's resiliency policy.

        Update container app resiliency policy.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param app_name: Name of the Container App. Required.
        :type app_name: str
        :param name: Name of the resiliency policy. Required.
        :type name: str
        :param resiliency_envelope: The resiliency policy to update. Required.
        :type resiliency_envelope: ~azure.mgmt.appcontainers.models.AppResiliency
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: AppResiliency or the result of cls(response)
        :rtype: ~azure.mgmt.appcontainers.models.AppResiliency
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def update(
        self,
        resource_group_name: str,
        app_name: str,
        name: str,
        resiliency_envelope: IO,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.AppResiliency:
        """Update an application's resiliency policy.

        Update container app resiliency policy.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param app_name: Name of the Container App. Required.
        :type app_name: str
        :param name: Name of the resiliency policy. Required.
        :type name: str
        :param resiliency_envelope: The resiliency policy to update. Required.
        :type resiliency_envelope: IO
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: AppResiliency or the result of cls(response)
        :rtype: ~azure.mgmt.appcontainers.models.AppResiliency
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def update(
        self,
        resource_group_name: str,
        app_name: str,
        name: str,
        resiliency_envelope: Union[_models.AppResiliency, IO],
        **kwargs: Any
    ) -> _models.AppResiliency:
        """Update an application's resiliency policy.

        Update container app resiliency policy.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param app_name: Name of the Container App. Required.
        :type app_name: str
        :param name: Name of the resiliency policy. Required.
        :type name: str
        :param resiliency_envelope: The resiliency policy to update. Is either a AppResiliency type or
         a IO type. Required.
        :type resiliency_envelope: ~azure.mgmt.appcontainers.models.AppResiliency or IO
        :keyword content_type: Body Parameter content-type. Known values are: 'application/json'.
         Default value is None.
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: AppResiliency or the result of cls(response)
        :rtype: ~azure.mgmt.appcontainers.models.AppResiliency
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

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))
        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.AppResiliency] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(resiliency_envelope, (IOBase, bytes)):
            _content = resiliency_envelope
        else:
            _json = self._serialize.body(resiliency_envelope, "AppResiliency")

        request = build_update_request(
            resource_group_name=resource_group_name,
            app_name=app_name,
            name=name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            content=_content,
            template_url=self.update.metadata["url"],
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
            error = self._deserialize.failsafe_deserialize(_models.DefaultErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize("AppResiliency", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    update.metadata = {
        "url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.App/containerApps/{appName}/resiliencyPolicies/{name}"
    }

    @distributed_trace_async
    async def delete(  # pylint: disable=inconsistent-return-statements
        self, resource_group_name: str, app_name: str, name: str, **kwargs: Any
    ) -> None:
        """Delete an application's resiliency policy.

        Delete container app resiliency policy.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param app_name: Name of the Container App. Required.
        :type app_name: str
        :param name: Name of the resiliency policy. Required.
        :type name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
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

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))
        cls: ClsType[None] = kwargs.pop("cls", None)

        request = build_delete_request(
            resource_group_name=resource_group_name,
            app_name=app_name,
            name=name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            template_url=self.delete.metadata["url"],
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

        if response.status_code not in [200, 204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.DefaultErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    delete.metadata = {
        "url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.App/containerApps/{appName}/resiliencyPolicies/{name}"
    }

    @distributed_trace_async
    async def get(self, resource_group_name: str, app_name: str, name: str, **kwargs: Any) -> _models.AppResiliency:
        """Get an application's resiliency policy.

        Get container app resiliency policy.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param app_name: Name of the Container App. Required.
        :type app_name: str
        :param name: Name of the resiliency policy. Required.
        :type name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: AppResiliency or the result of cls(response)
        :rtype: ~azure.mgmt.appcontainers.models.AppResiliency
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

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))
        cls: ClsType[_models.AppResiliency] = kwargs.pop("cls", None)

        request = build_get_request(
            resource_group_name=resource_group_name,
            app_name=app_name,
            name=name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            template_url=self.get.metadata["url"],
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
            error = self._deserialize.failsafe_deserialize(_models.DefaultErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize("AppResiliency", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get.metadata = {
        "url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.App/containerApps/{appName}/resiliencyPolicies/{name}"
    }

    @distributed_trace
    def list(self, resource_group_name: str, app_name: str, **kwargs: Any) -> AsyncIterable["_models.AppResiliency"]:
        """List an application's resiliency policies.

        List container app resiliency policies.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param app_name: Name of the Container App. Required.
        :type app_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either AppResiliency or the result of cls(response)
        :rtype: ~azure.core.async_paging.AsyncItemPaged[~azure.mgmt.appcontainers.models.AppResiliency]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))
        cls: ClsType[_models.AppResiliencyCollection] = kwargs.pop("cls", None)

        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        def prepare_request(next_link=None):
            if not next_link:

                request = build_list_request(
                    resource_group_name=resource_group_name,
                    app_name=app_name,
                    subscription_id=self._config.subscription_id,
                    api_version=api_version,
                    template_url=self.list.metadata["url"],
                    headers=_headers,
                    params=_params,
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)

            else:
                # make call to next link with the client's api-version
                _parsed_next_link = urllib.parse.urlparse(next_link)
                _next_request_params = case_insensitive_dict(
                    {
                        key: [urllib.parse.quote(v) for v in value]
                        for key, value in urllib.parse.parse_qs(_parsed_next_link.query).items()
                    }
                )
                _next_request_params["api-version"] = self._config.api_version
                request = HttpRequest(
                    "GET", urllib.parse.urljoin(next_link, _parsed_next_link.path), params=_next_request_params
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)
                request.method = "GET"
            return request

        async def extract_data(pipeline_response):
            deserialized = self._deserialize("AppResiliencyCollection", pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)  # type: ignore
            return deserialized.next_link or None, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            request = prepare_request(next_link)

            _stream = False
            pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
                request, stream=_stream, **kwargs
            )
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                error = self._deserialize.failsafe_deserialize(_models.DefaultErrorResponse, pipeline_response)
                raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

            return pipeline_response

        return AsyncItemPaged(get_next, extract_data)

    list.metadata = {
        "url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.App/containerApps/{appName}/resiliencyPolicies"
    }
