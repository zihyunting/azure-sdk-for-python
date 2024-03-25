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
from ...operations._consumer_groups_operations import (
    build_create_or_update_request,
    build_delete_request,
    build_get_request,
    build_list_by_event_hub_request,
)

T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class ConsumerGroupsOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.mgmt.eventhub.v2022_01_01_preview.aio.EventHubManagementClient`'s
        :attr:`consumer_groups` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs) -> None:
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")
        self._api_version = input_args.pop(0) if input_args else kwargs.pop("api_version")

    @overload
    async def create_or_update(
        self,
        resource_group_name: str,
        namespace_name: str,
        event_hub_name: str,
        consumer_group_name: str,
        parameters: _models.ConsumerGroup,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.ConsumerGroup:
        """Creates or updates an Event Hubs consumer group as a nested resource within a Namespace.

        :param resource_group_name: Name of the resource group within the azure subscription. Required.
        :type resource_group_name: str
        :param namespace_name: The Namespace name. Required.
        :type namespace_name: str
        :param event_hub_name: The Event Hub name. Required.
        :type event_hub_name: str
        :param consumer_group_name: The consumer group name. Required.
        :type consumer_group_name: str
        :param parameters: Parameters supplied to create or update a consumer group resource. Required.
        :type parameters: ~azure.mgmt.eventhub.v2022_01_01_preview.models.ConsumerGroup
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: ConsumerGroup or the result of cls(response)
        :rtype: ~azure.mgmt.eventhub.v2022_01_01_preview.models.ConsumerGroup
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def create_or_update(
        self,
        resource_group_name: str,
        namespace_name: str,
        event_hub_name: str,
        consumer_group_name: str,
        parameters: IO[bytes],
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.ConsumerGroup:
        """Creates or updates an Event Hubs consumer group as a nested resource within a Namespace.

        :param resource_group_name: Name of the resource group within the azure subscription. Required.
        :type resource_group_name: str
        :param namespace_name: The Namespace name. Required.
        :type namespace_name: str
        :param event_hub_name: The Event Hub name. Required.
        :type event_hub_name: str
        :param consumer_group_name: The consumer group name. Required.
        :type consumer_group_name: str
        :param parameters: Parameters supplied to create or update a consumer group resource. Required.
        :type parameters: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: ConsumerGroup or the result of cls(response)
        :rtype: ~azure.mgmt.eventhub.v2022_01_01_preview.models.ConsumerGroup
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def create_or_update(
        self,
        resource_group_name: str,
        namespace_name: str,
        event_hub_name: str,
        consumer_group_name: str,
        parameters: Union[_models.ConsumerGroup, IO[bytes]],
        **kwargs: Any
    ) -> _models.ConsumerGroup:
        """Creates or updates an Event Hubs consumer group as a nested resource within a Namespace.

        :param resource_group_name: Name of the resource group within the azure subscription. Required.
        :type resource_group_name: str
        :param namespace_name: The Namespace name. Required.
        :type namespace_name: str
        :param event_hub_name: The Event Hub name. Required.
        :type event_hub_name: str
        :param consumer_group_name: The consumer group name. Required.
        :type consumer_group_name: str
        :param parameters: Parameters supplied to create or update a consumer group resource. Is either
         a ConsumerGroup type or a IO[bytes] type. Required.
        :type parameters: ~azure.mgmt.eventhub.v2022_01_01_preview.models.ConsumerGroup or IO[bytes]
        :return: ConsumerGroup or the result of cls(response)
        :rtype: ~azure.mgmt.eventhub.v2022_01_01_preview.models.ConsumerGroup
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
            "api_version", _params.pop("api-version", self._api_version or "2022-01-01-preview")
        )
        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.ConsumerGroup] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(parameters, (IOBase, bytes)):
            _content = parameters
        else:
            _json = self._serialize.body(parameters, "ConsumerGroup")

        _request = build_create_or_update_request(
            resource_group_name=resource_group_name,
            namespace_name=namespace_name,
            event_hub_name=event_hub_name,
            consumer_group_name=consumer_group_name,
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

        deserialized = self._deserialize("ConsumerGroup", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @distributed_trace_async
    async def delete(  # pylint: disable=inconsistent-return-statements
        self,
        resource_group_name: str,
        namespace_name: str,
        event_hub_name: str,
        consumer_group_name: str,
        **kwargs: Any
    ) -> None:
        """Deletes a consumer group from the specified Event Hub and resource group.

        :param resource_group_name: Name of the resource group within the azure subscription. Required.
        :type resource_group_name: str
        :param namespace_name: The Namespace name. Required.
        :type namespace_name: str
        :param event_hub_name: The Event Hub name. Required.
        :type event_hub_name: str
        :param consumer_group_name: The consumer group name. Required.
        :type consumer_group_name: str
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
            "api_version", _params.pop("api-version", self._api_version or "2022-01-01-preview")
        )
        cls: ClsType[None] = kwargs.pop("cls", None)

        _request = build_delete_request(
            resource_group_name=resource_group_name,
            namespace_name=namespace_name,
            event_hub_name=event_hub_name,
            consumer_group_name=consumer_group_name,
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

    @distributed_trace_async
    async def get(
        self,
        resource_group_name: str,
        namespace_name: str,
        event_hub_name: str,
        consumer_group_name: str,
        **kwargs: Any
    ) -> _models.ConsumerGroup:
        """Gets a description for the specified consumer group.

        :param resource_group_name: Name of the resource group within the azure subscription. Required.
        :type resource_group_name: str
        :param namespace_name: The Namespace name. Required.
        :type namespace_name: str
        :param event_hub_name: The Event Hub name. Required.
        :type event_hub_name: str
        :param consumer_group_name: The consumer group name. Required.
        :type consumer_group_name: str
        :return: ConsumerGroup or the result of cls(response)
        :rtype: ~azure.mgmt.eventhub.v2022_01_01_preview.models.ConsumerGroup
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
            "api_version", _params.pop("api-version", self._api_version or "2022-01-01-preview")
        )
        cls: ClsType[_models.ConsumerGroup] = kwargs.pop("cls", None)

        _request = build_get_request(
            resource_group_name=resource_group_name,
            namespace_name=namespace_name,
            event_hub_name=event_hub_name,
            consumer_group_name=consumer_group_name,
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

        deserialized = self._deserialize("ConsumerGroup", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @distributed_trace
    def list_by_event_hub(
        self,
        resource_group_name: str,
        namespace_name: str,
        event_hub_name: str,
        skip: Optional[int] = None,
        top: Optional[int] = None,
        **kwargs: Any
    ) -> AsyncIterable["_models.ConsumerGroup"]:
        """Gets all the consumer groups in a Namespace. An empty feed is returned if no consumer group
        exists in the Namespace.

        :param resource_group_name: Name of the resource group within the azure subscription. Required.
        :type resource_group_name: str
        :param namespace_name: The Namespace name. Required.
        :type namespace_name: str
        :param event_hub_name: The Event Hub name. Required.
        :type event_hub_name: str
        :param skip: Skip is only used if a previous operation returned a partial result. If a previous
         response contains a nextLink element, the value of the nextLink element will include a skip
         parameter that specifies a starting point to use for subsequent calls. Default value is None.
        :type skip: int
        :param top: May be used to limit the number of results to the most recent N usageDetails.
         Default value is None.
        :type top: int
        :return: An iterator like instance of either ConsumerGroup or the result of cls(response)
        :rtype:
         ~azure.core.async_paging.AsyncItemPaged[~azure.mgmt.eventhub.v2022_01_01_preview.models.ConsumerGroup]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop(
            "api_version", _params.pop("api-version", self._api_version or "2022-01-01-preview")
        )
        cls: ClsType[_models.ConsumerGroupListResult] = kwargs.pop("cls", None)

        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        def prepare_request(next_link=None):
            if not next_link:

                _request = build_list_by_event_hub_request(
                    resource_group_name=resource_group_name,
                    namespace_name=namespace_name,
                    event_hub_name=event_hub_name,
                    subscription_id=self._config.subscription_id,
                    skip=skip,
                    top=top,
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
            deserialized = self._deserialize("ConsumerGroupListResult", pipeline_response)
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
