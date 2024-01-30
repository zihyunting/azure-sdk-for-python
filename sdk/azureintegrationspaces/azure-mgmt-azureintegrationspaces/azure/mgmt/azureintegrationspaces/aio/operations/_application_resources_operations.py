# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from io import IOBase
from typing import Any, AsyncIterable, Callable, Dict, IO, List, Optional, TypeVar, Union, overload
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
from ...operations._application_resources_operations import (
    build_create_or_update_request,
    build_delete_request,
    build_get_request,
    build_list_by_application_request,
    build_patch_request,
)

T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class ApplicationResourcesOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.mgmt.azureintegrationspaces.aio.IntegrationSpacesMgmtClient`'s
        :attr:`application_resources` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs) -> None:
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @distributed_trace
    def list_by_application(
        self,
        resource_group_name: str,
        space_name: str,
        application_name: str,
        top: Optional[int] = None,
        skip: int = 0,
        maxpagesize: Optional[int] = None,
        filter: Optional[str] = None,
        select: Optional[List[str]] = None,
        expand: Optional[List[str]] = None,
        orderby: Optional[List[str]] = None,
        **kwargs: Any
    ) -> AsyncIterable["_models.ApplicationResource"]:
        """List ApplicationResource resources by Application.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param space_name: The name of the space. Required.
        :type space_name: str
        :param application_name: The name of the Application. Required.
        :type application_name: str
        :param top: The number of result items to return. Default value is None.
        :type top: int
        :param skip: The number of result items to skip. Default value is 0.
        :type skip: int
        :param maxpagesize: The maximum number of result items per page. Default value is None.
        :type maxpagesize: int
        :param filter: Filter the result list using the given expression. Default value is None.
        :type filter: str
        :param select: Select the specified fields to be included in the response. Default value is
         None.
        :type select: list[str]
        :param expand: Expand the indicated resources into the response. Default value is None.
        :type expand: list[str]
        :param orderby: Expressions that specify the order of returned results. Default value is None.
        :type orderby: list[str]
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either ApplicationResource or the result of cls(response)
        :rtype:
         ~azure.core.async_paging.AsyncItemPaged[~azure.mgmt.azureintegrationspaces.models.ApplicationResource]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))
        cls: ClsType[_models.ApplicationResourceListResult] = kwargs.pop("cls", None)

        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        def prepare_request(next_link=None):
            if not next_link:

                request = build_list_by_application_request(
                    resource_group_name=resource_group_name,
                    space_name=space_name,
                    application_name=application_name,
                    subscription_id=self._config.subscription_id,
                    top=top,
                    skip=skip,
                    maxpagesize=maxpagesize,
                    filter=filter,
                    select=select,
                    expand=expand,
                    orderby=orderby,
                    api_version=api_version,
                    template_url=self.list_by_application.metadata["url"],
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
            deserialized = self._deserialize("ApplicationResourceListResult", pipeline_response)
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
                error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
                raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

            return pipeline_response

        return AsyncItemPaged(get_next, extract_data)

    list_by_application.metadata = {
        "url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.IntegrationSpaces/spaces/{spaceName}/applications/{applicationName}/resources"
    }

    @distributed_trace_async
    async def get(
        self, resource_group_name: str, space_name: str, application_name: str, resource_name: str, **kwargs: Any
    ) -> _models.ApplicationResource:
        """Get a ApplicationResource.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param space_name: The name of the space. Required.
        :type space_name: str
        :param application_name: The name of the Application. Required.
        :type application_name: str
        :param resource_name: The name of the resource. Required.
        :type resource_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ApplicationResource or the result of cls(response)
        :rtype: ~azure.mgmt.azureintegrationspaces.models.ApplicationResource
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
        cls: ClsType[_models.ApplicationResource] = kwargs.pop("cls", None)

        request = build_get_request(
            resource_group_name=resource_group_name,
            space_name=space_name,
            application_name=application_name,
            resource_name=resource_name,
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
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize("ApplicationResource", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get.metadata = {
        "url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.IntegrationSpaces/spaces/{spaceName}/applications/{applicationName}/resources/{resourceName}"
    }

    @overload
    async def create_or_update(
        self,
        resource_group_name: str,
        space_name: str,
        application_name: str,
        resource_name: str,
        resource: _models.ApplicationResource,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.ApplicationResource:
        """Create a ApplicationResource.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param space_name: The name of the space. Required.
        :type space_name: str
        :param application_name: The name of the Application. Required.
        :type application_name: str
        :param resource_name: The name of the resource. Required.
        :type resource_name: str
        :param resource: Resource create parameters. Required.
        :type resource: ~azure.mgmt.azureintegrationspaces.models.ApplicationResource
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ApplicationResource or the result of cls(response)
        :rtype: ~azure.mgmt.azureintegrationspaces.models.ApplicationResource
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def create_or_update(
        self,
        resource_group_name: str,
        space_name: str,
        application_name: str,
        resource_name: str,
        resource: IO,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.ApplicationResource:
        """Create a ApplicationResource.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param space_name: The name of the space. Required.
        :type space_name: str
        :param application_name: The name of the Application. Required.
        :type application_name: str
        :param resource_name: The name of the resource. Required.
        :type resource_name: str
        :param resource: Resource create parameters. Required.
        :type resource: IO
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ApplicationResource or the result of cls(response)
        :rtype: ~azure.mgmt.azureintegrationspaces.models.ApplicationResource
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def create_or_update(
        self,
        resource_group_name: str,
        space_name: str,
        application_name: str,
        resource_name: str,
        resource: Union[_models.ApplicationResource, IO],
        **kwargs: Any
    ) -> _models.ApplicationResource:
        """Create a ApplicationResource.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param space_name: The name of the space. Required.
        :type space_name: str
        :param application_name: The name of the Application. Required.
        :type application_name: str
        :param resource_name: The name of the resource. Required.
        :type resource_name: str
        :param resource: Resource create parameters. Is either a ApplicationResource type or a IO type.
         Required.
        :type resource: ~azure.mgmt.azureintegrationspaces.models.ApplicationResource or IO
        :keyword content_type: Body Parameter content-type. Known values are: 'application/json'.
         Default value is None.
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ApplicationResource or the result of cls(response)
        :rtype: ~azure.mgmt.azureintegrationspaces.models.ApplicationResource
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
        cls: ClsType[_models.ApplicationResource] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(resource, (IOBase, bytes)):
            _content = resource
        else:
            _json = self._serialize.body(resource, "ApplicationResource")

        request = build_create_or_update_request(
            resource_group_name=resource_group_name,
            space_name=space_name,
            application_name=application_name,
            resource_name=resource_name,
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
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if response.status_code == 200:
            deserialized = self._deserialize("ApplicationResource", pipeline_response)

        if response.status_code == 201:
            deserialized = self._deserialize("ApplicationResource", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    create_or_update.metadata = {
        "url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.IntegrationSpaces/spaces/{spaceName}/applications/{applicationName}/resources/{resourceName}"
    }

    @overload
    async def patch(
        self,
        resource_group_name: str,
        space_name: str,
        application_name: str,
        resource_name: str,
        properties: _models.ApplicationResourceUpdate,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.ApplicationResource:
        """Update a ApplicationResource.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param space_name: The name of the space. Required.
        :type space_name: str
        :param application_name: The name of the Application. Required.
        :type application_name: str
        :param resource_name: The name of the resource. Required.
        :type resource_name: str
        :param properties: The resource properties to be updated. Required.
        :type properties: ~azure.mgmt.azureintegrationspaces.models.ApplicationResourceUpdate
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ApplicationResource or the result of cls(response)
        :rtype: ~azure.mgmt.azureintegrationspaces.models.ApplicationResource
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def patch(
        self,
        resource_group_name: str,
        space_name: str,
        application_name: str,
        resource_name: str,
        properties: IO,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.ApplicationResource:
        """Update a ApplicationResource.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param space_name: The name of the space. Required.
        :type space_name: str
        :param application_name: The name of the Application. Required.
        :type application_name: str
        :param resource_name: The name of the resource. Required.
        :type resource_name: str
        :param properties: The resource properties to be updated. Required.
        :type properties: IO
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ApplicationResource or the result of cls(response)
        :rtype: ~azure.mgmt.azureintegrationspaces.models.ApplicationResource
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def patch(
        self,
        resource_group_name: str,
        space_name: str,
        application_name: str,
        resource_name: str,
        properties: Union[_models.ApplicationResourceUpdate, IO],
        **kwargs: Any
    ) -> _models.ApplicationResource:
        """Update a ApplicationResource.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param space_name: The name of the space. Required.
        :type space_name: str
        :param application_name: The name of the Application. Required.
        :type application_name: str
        :param resource_name: The name of the resource. Required.
        :type resource_name: str
        :param properties: The resource properties to be updated. Is either a ApplicationResourceUpdate
         type or a IO type. Required.
        :type properties: ~azure.mgmt.azureintegrationspaces.models.ApplicationResourceUpdate or IO
        :keyword content_type: Body Parameter content-type. Known values are: 'application/json'.
         Default value is None.
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ApplicationResource or the result of cls(response)
        :rtype: ~azure.mgmt.azureintegrationspaces.models.ApplicationResource
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
        cls: ClsType[_models.ApplicationResource] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(properties, (IOBase, bytes)):
            _content = properties
        else:
            _json = self._serialize.body(properties, "ApplicationResourceUpdate")

        request = build_patch_request(
            resource_group_name=resource_group_name,
            space_name=space_name,
            application_name=application_name,
            resource_name=resource_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            content=_content,
            template_url=self.patch.metadata["url"],
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

        deserialized = self._deserialize("ApplicationResource", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    patch.metadata = {
        "url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.IntegrationSpaces/spaces/{spaceName}/applications/{applicationName}/resources/{resourceName}"
    }

    @distributed_trace_async
    async def delete(  # pylint: disable=inconsistent-return-statements
        self, resource_group_name: str, space_name: str, application_name: str, resource_name: str, **kwargs: Any
    ) -> None:
        """Delete a ApplicationResource.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param space_name: The name of the space. Required.
        :type space_name: str
        :param application_name: The name of the Application. Required.
        :type application_name: str
        :param resource_name: The name of the resource. Required.
        :type resource_name: str
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
            space_name=space_name,
            application_name=application_name,
            resource_name=resource_name,
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
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    delete.metadata = {
        "url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.IntegrationSpaces/spaces/{spaceName}/applications/{applicationName}/resources/{resourceName}"
    }
