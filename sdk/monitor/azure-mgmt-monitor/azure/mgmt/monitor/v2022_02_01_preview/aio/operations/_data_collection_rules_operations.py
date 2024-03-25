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
from ...operations._data_collection_rules_operations import (
    build_create_request,
    build_delete_request,
    build_get_request,
    build_list_by_resource_group_request,
    build_list_by_subscription_request,
    build_update_request,
)

T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class DataCollectionRulesOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.mgmt.monitor.v2022_02_01_preview.aio.MonitorManagementClient`'s
        :attr:`data_collection_rules` attribute.
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
    ) -> AsyncIterable["_models.DataCollectionRuleResource"]:
        """Lists all data collection rules in the specified resource group.

        Lists all data collection rules in the specified resource group.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :return: An iterator like instance of either DataCollectionRuleResource or the result of
         cls(response)
        :rtype:
         ~azure.core.async_paging.AsyncItemPaged[~azure.mgmt.monitor.v2022_02_01_preview.models.DataCollectionRuleResource]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop(
            "api_version", _params.pop("api-version", self._api_version or "2021-09-01-preview")
        )
        cls: ClsType[_models.DataCollectionRuleResourceListResult] = kwargs.pop("cls", None)

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
            deserialized = self._deserialize("DataCollectionRuleResourceListResult", pipeline_response)
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
                error = self._deserialize.failsafe_deserialize(_models.ErrorResponseCommonV2, pipeline_response)
                raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

            return pipeline_response

        return AsyncItemPaged(get_next, extract_data)

    @distributed_trace
    def list_by_subscription(self, **kwargs: Any) -> AsyncIterable["_models.DataCollectionRuleResource"]:
        """Lists all data collection rules in the specified subscription.

        Lists all data collection rules in the specified subscription.

        :return: An iterator like instance of either DataCollectionRuleResource or the result of
         cls(response)
        :rtype:
         ~azure.core.async_paging.AsyncItemPaged[~azure.mgmt.monitor.v2022_02_01_preview.models.DataCollectionRuleResource]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop(
            "api_version", _params.pop("api-version", self._api_version or "2021-09-01-preview")
        )
        cls: ClsType[_models.DataCollectionRuleResourceListResult] = kwargs.pop("cls", None)

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
            deserialized = self._deserialize("DataCollectionRuleResourceListResult", pipeline_response)
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
                error = self._deserialize.failsafe_deserialize(_models.ErrorResponseCommonV2, pipeline_response)
                raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

            return pipeline_response

        return AsyncItemPaged(get_next, extract_data)

    @distributed_trace_async
    async def get(
        self, resource_group_name: str, data_collection_rule_name: str, **kwargs: Any
    ) -> _models.DataCollectionRuleResource:
        """Returns the specified data collection rule.

        Returns the specified data collection rule.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param data_collection_rule_name: The name of the data collection rule. The name is case
         insensitive. Required.
        :type data_collection_rule_name: str
        :return: DataCollectionRuleResource or the result of cls(response)
        :rtype: ~azure.mgmt.monitor.v2022_02_01_preview.models.DataCollectionRuleResource
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
            "api_version", _params.pop("api-version", self._api_version or "2021-09-01-preview")
        )
        cls: ClsType[_models.DataCollectionRuleResource] = kwargs.pop("cls", None)

        _request = build_get_request(
            resource_group_name=resource_group_name,
            data_collection_rule_name=data_collection_rule_name,
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
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponseCommonV2, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize("DataCollectionRuleResource", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @overload
    async def create(
        self,
        resource_group_name: str,
        data_collection_rule_name: str,
        body: Optional[_models.DataCollectionRuleResource] = None,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.DataCollectionRuleResource:
        """Creates or updates a data collection rule.

        Creates or updates a data collection rule.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param data_collection_rule_name: The name of the data collection rule. The name is case
         insensitive. Required.
        :type data_collection_rule_name: str
        :param body: The payload. Default value is None.
        :type body: ~azure.mgmt.monitor.v2022_02_01_preview.models.DataCollectionRuleResource
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: DataCollectionRuleResource or the result of cls(response)
        :rtype: ~azure.mgmt.monitor.v2022_02_01_preview.models.DataCollectionRuleResource
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def create(
        self,
        resource_group_name: str,
        data_collection_rule_name: str,
        body: Optional[IO[bytes]] = None,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.DataCollectionRuleResource:
        """Creates or updates a data collection rule.

        Creates or updates a data collection rule.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param data_collection_rule_name: The name of the data collection rule. The name is case
         insensitive. Required.
        :type data_collection_rule_name: str
        :param body: The payload. Default value is None.
        :type body: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: DataCollectionRuleResource or the result of cls(response)
        :rtype: ~azure.mgmt.monitor.v2022_02_01_preview.models.DataCollectionRuleResource
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def create(
        self,
        resource_group_name: str,
        data_collection_rule_name: str,
        body: Optional[Union[_models.DataCollectionRuleResource, IO[bytes]]] = None,
        **kwargs: Any
    ) -> _models.DataCollectionRuleResource:
        """Creates or updates a data collection rule.

        Creates or updates a data collection rule.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param data_collection_rule_name: The name of the data collection rule. The name is case
         insensitive. Required.
        :type data_collection_rule_name: str
        :param body: The payload. Is either a DataCollectionRuleResource type or a IO[bytes] type.
         Default value is None.
        :type body: ~azure.mgmt.monitor.v2022_02_01_preview.models.DataCollectionRuleResource or
         IO[bytes]
        :return: DataCollectionRuleResource or the result of cls(response)
        :rtype: ~azure.mgmt.monitor.v2022_02_01_preview.models.DataCollectionRuleResource
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
            "api_version", _params.pop("api-version", self._api_version or "2021-09-01-preview")
        )
        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.DataCollectionRuleResource] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(body, (IOBase, bytes)):
            _content = body
        else:
            if body is not None:
                _json = self._serialize.body(body, "DataCollectionRuleResource")
            else:
                _json = None

        _request = build_create_request(
            resource_group_name=resource_group_name,
            data_collection_rule_name=data_collection_rule_name,
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
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponseCommonV2, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if response.status_code == 200:
            deserialized = self._deserialize("DataCollectionRuleResource", pipeline_response)

        if response.status_code == 201:
            deserialized = self._deserialize("DataCollectionRuleResource", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @overload
    async def update(
        self,
        resource_group_name: str,
        data_collection_rule_name: str,
        body: Optional[_models.ResourceForUpdate] = None,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.DataCollectionRuleResource:
        """Updates part of a data collection rule.

        Updates part of a data collection rule.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param data_collection_rule_name: The name of the data collection rule. The name is case
         insensitive. Required.
        :type data_collection_rule_name: str
        :param body: The payload. Default value is None.
        :type body: ~azure.mgmt.monitor.v2022_02_01_preview.models.ResourceForUpdate
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: DataCollectionRuleResource or the result of cls(response)
        :rtype: ~azure.mgmt.monitor.v2022_02_01_preview.models.DataCollectionRuleResource
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def update(
        self,
        resource_group_name: str,
        data_collection_rule_name: str,
        body: Optional[IO[bytes]] = None,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.DataCollectionRuleResource:
        """Updates part of a data collection rule.

        Updates part of a data collection rule.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param data_collection_rule_name: The name of the data collection rule. The name is case
         insensitive. Required.
        :type data_collection_rule_name: str
        :param body: The payload. Default value is None.
        :type body: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: DataCollectionRuleResource or the result of cls(response)
        :rtype: ~azure.mgmt.monitor.v2022_02_01_preview.models.DataCollectionRuleResource
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def update(
        self,
        resource_group_name: str,
        data_collection_rule_name: str,
        body: Optional[Union[_models.ResourceForUpdate, IO[bytes]]] = None,
        **kwargs: Any
    ) -> _models.DataCollectionRuleResource:
        """Updates part of a data collection rule.

        Updates part of a data collection rule.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param data_collection_rule_name: The name of the data collection rule. The name is case
         insensitive. Required.
        :type data_collection_rule_name: str
        :param body: The payload. Is either a ResourceForUpdate type or a IO[bytes] type. Default value
         is None.
        :type body: ~azure.mgmt.monitor.v2022_02_01_preview.models.ResourceForUpdate or IO[bytes]
        :return: DataCollectionRuleResource or the result of cls(response)
        :rtype: ~azure.mgmt.monitor.v2022_02_01_preview.models.DataCollectionRuleResource
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
            "api_version", _params.pop("api-version", self._api_version or "2021-09-01-preview")
        )
        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.DataCollectionRuleResource] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(body, (IOBase, bytes)):
            _content = body
        else:
            if body is not None:
                _json = self._serialize.body(body, "ResourceForUpdate")
            else:
                _json = None

        _request = build_update_request(
            resource_group_name=resource_group_name,
            data_collection_rule_name=data_collection_rule_name,
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
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponseCommonV2, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize("DataCollectionRuleResource", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @distributed_trace_async
    async def delete(  # pylint: disable=inconsistent-return-statements
        self, resource_group_name: str, data_collection_rule_name: str, **kwargs: Any
    ) -> None:
        """Deletes a data collection rule.

        Deletes a data collection rule.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param data_collection_rule_name: The name of the data collection rule. The name is case
         insensitive. Required.
        :type data_collection_rule_name: str
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
            "api_version", _params.pop("api-version", self._api_version or "2021-09-01-preview")
        )
        cls: ClsType[None] = kwargs.pop("cls", None)

        _request = build_delete_request(
            resource_group_name=resource_group_name,
            data_collection_rule_name=data_collection_rule_name,
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
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponseCommonV2, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})  # type: ignore
