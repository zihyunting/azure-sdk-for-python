# pylint: disable=too-many-lines,too-many-statements
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from io import IOBase
from typing import Any, AsyncIterable, Callable, Dict, IO, Optional, TypeVar, Union, cast, overload
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
from azure.core.polling import AsyncLROPoller, AsyncNoPolling, AsyncPollingMethod
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator import distributed_trace
from azure.core.tracing.decorator_async import distributed_trace_async
from azure.core.utils import case_insensitive_dict
from azure.mgmt.core.exceptions import ARMErrorFormat
from azure.mgmt.core.polling.async_arm_polling import AsyncARMPolling

from ... import models as _models
from ..._vendor import _convert_request
from ...operations._agent_pools_operations import (
    build_create_or_update_request,
    build_delete_request,
    build_get_available_agent_pool_versions_request,
    build_get_request,
    build_get_upgrade_profile_request,
    build_list_request,
    build_upgrade_node_image_version_request,
)

T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class AgentPoolsOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.mgmt.containerservice.v2021_05_01.aio.ContainerServiceClient`'s
        :attr:`agent_pools` attribute.
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
    def list(self, resource_group_name: str, resource_name: str, **kwargs: Any) -> AsyncIterable["_models.AgentPool"]:
        """Gets a list of agent pools in the specified managed cluster.

        Gets a list of agent pools in the specified managed cluster.

        :param resource_group_name: The name of the resource group. Required.
        :type resource_group_name: str
        :param resource_name: The name of the managed cluster resource. Required.
        :type resource_name: str
        :return: An iterator like instance of either AgentPool or the result of cls(response)
        :rtype:
         ~azure.core.async_paging.AsyncItemPaged[~azure.mgmt.containerservice.v2021_05_01.models.AgentPool]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._api_version or "2021-05-01"))
        cls: ClsType[_models.AgentPoolListResult] = kwargs.pop("cls", None)

        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        def prepare_request(next_link=None):
            if not next_link:

                _request = build_list_request(
                    resource_group_name=resource_group_name,
                    resource_name=resource_name,
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
            deserialized = self._deserialize("AgentPoolListResult", pipeline_response)
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
                raise HttpResponseError(response=response, error_format=ARMErrorFormat)

            return pipeline_response

        return AsyncItemPaged(get_next, extract_data)

    @distributed_trace_async
    async def get(
        self, resource_group_name: str, resource_name: str, agent_pool_name: str, **kwargs: Any
    ) -> _models.AgentPool:
        """Gets the specified managed cluster agent pool.

        Gets the specified managed cluster agent pool.

        :param resource_group_name: The name of the resource group. Required.
        :type resource_group_name: str
        :param resource_name: The name of the managed cluster resource. Required.
        :type resource_name: str
        :param agent_pool_name: The name of the agent pool. Required.
        :type agent_pool_name: str
        :return: AgentPool or the result of cls(response)
        :rtype: ~azure.mgmt.containerservice.v2021_05_01.models.AgentPool
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

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._api_version or "2021-05-01"))
        cls: ClsType[_models.AgentPool] = kwargs.pop("cls", None)

        _request = build_get_request(
            resource_group_name=resource_group_name,
            resource_name=resource_name,
            agent_pool_name=agent_pool_name,
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
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize("AgentPool", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    async def _create_or_update_initial(
        self,
        resource_group_name: str,
        resource_name: str,
        agent_pool_name: str,
        parameters: Union[_models.AgentPool, IO[bytes]],
        **kwargs: Any
    ) -> _models.AgentPool:
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._api_version or "2021-05-01"))
        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.AgentPool] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(parameters, (IOBase, bytes)):
            _content = parameters
        else:
            _json = self._serialize.body(parameters, "AgentPool")

        _request = build_create_or_update_request(
            resource_group_name=resource_group_name,
            resource_name=resource_name,
            agent_pool_name=agent_pool_name,
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
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        if response.status_code == 200:
            deserialized = self._deserialize("AgentPool", pipeline_response)

        if response.status_code == 201:
            deserialized = self._deserialize("AgentPool", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @overload
    async def begin_create_or_update(
        self,
        resource_group_name: str,
        resource_name: str,
        agent_pool_name: str,
        parameters: _models.AgentPool,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> AsyncLROPoller[_models.AgentPool]:
        """Creates or updates an agent pool in the specified managed cluster.

        Creates or updates an agent pool in the specified managed cluster.

        :param resource_group_name: The name of the resource group. Required.
        :type resource_group_name: str
        :param resource_name: The name of the managed cluster resource. Required.
        :type resource_name: str
        :param agent_pool_name: The name of the agent pool. Required.
        :type agent_pool_name: str
        :param parameters: The agent pool to create or update. Required.
        :type parameters: ~azure.mgmt.containerservice.v2021_05_01.models.AgentPool
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of AsyncLROPoller that returns either AgentPool or the result of
         cls(response)
        :rtype:
         ~azure.core.polling.AsyncLROPoller[~azure.mgmt.containerservice.v2021_05_01.models.AgentPool]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def begin_create_or_update(
        self,
        resource_group_name: str,
        resource_name: str,
        agent_pool_name: str,
        parameters: IO[bytes],
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> AsyncLROPoller[_models.AgentPool]:
        """Creates or updates an agent pool in the specified managed cluster.

        Creates or updates an agent pool in the specified managed cluster.

        :param resource_group_name: The name of the resource group. Required.
        :type resource_group_name: str
        :param resource_name: The name of the managed cluster resource. Required.
        :type resource_name: str
        :param agent_pool_name: The name of the agent pool. Required.
        :type agent_pool_name: str
        :param parameters: The agent pool to create or update. Required.
        :type parameters: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of AsyncLROPoller that returns either AgentPool or the result of
         cls(response)
        :rtype:
         ~azure.core.polling.AsyncLROPoller[~azure.mgmt.containerservice.v2021_05_01.models.AgentPool]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def begin_create_or_update(
        self,
        resource_group_name: str,
        resource_name: str,
        agent_pool_name: str,
        parameters: Union[_models.AgentPool, IO[bytes]],
        **kwargs: Any
    ) -> AsyncLROPoller[_models.AgentPool]:
        """Creates or updates an agent pool in the specified managed cluster.

        Creates or updates an agent pool in the specified managed cluster.

        :param resource_group_name: The name of the resource group. Required.
        :type resource_group_name: str
        :param resource_name: The name of the managed cluster resource. Required.
        :type resource_name: str
        :param agent_pool_name: The name of the agent pool. Required.
        :type agent_pool_name: str
        :param parameters: The agent pool to create or update. Is either a AgentPool type or a
         IO[bytes] type. Required.
        :type parameters: ~azure.mgmt.containerservice.v2021_05_01.models.AgentPool or IO[bytes]
        :return: An instance of AsyncLROPoller that returns either AgentPool or the result of
         cls(response)
        :rtype:
         ~azure.core.polling.AsyncLROPoller[~azure.mgmt.containerservice.v2021_05_01.models.AgentPool]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._api_version or "2021-05-01"))
        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.AgentPool] = kwargs.pop("cls", None)
        polling: Union[bool, AsyncPollingMethod] = kwargs.pop("polling", True)
        lro_delay = kwargs.pop("polling_interval", self._config.polling_interval)
        cont_token: Optional[str] = kwargs.pop("continuation_token", None)
        if cont_token is None:
            raw_result = await self._create_or_update_initial(
                resource_group_name=resource_group_name,
                resource_name=resource_name,
                agent_pool_name=agent_pool_name,
                parameters=parameters,
                api_version=api_version,
                content_type=content_type,
                cls=lambda x, y, z: x,
                headers=_headers,
                params=_params,
                **kwargs
            )
        kwargs.pop("error_map", None)

        def get_long_running_output(pipeline_response):
            deserialized = self._deserialize("AgentPool", pipeline_response)
            if cls:
                return cls(pipeline_response, deserialized, {})  # type: ignore
            return deserialized

        if polling is True:
            polling_method: AsyncPollingMethod = cast(AsyncPollingMethod, AsyncARMPolling(lro_delay, **kwargs))
        elif polling is False:
            polling_method = cast(AsyncPollingMethod, AsyncNoPolling())
        else:
            polling_method = polling
        if cont_token:
            return AsyncLROPoller[_models.AgentPool].from_continuation_token(
                polling_method=polling_method,
                continuation_token=cont_token,
                client=self._client,
                deserialization_callback=get_long_running_output,
            )
        return AsyncLROPoller[_models.AgentPool](
            self._client, raw_result, get_long_running_output, polling_method  # type: ignore
        )

    async def _delete_initial(  # pylint: disable=inconsistent-return-statements
        self, resource_group_name: str, resource_name: str, agent_pool_name: str, **kwargs: Any
    ) -> None:
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._api_version or "2021-05-01"))
        cls: ClsType[None] = kwargs.pop("cls", None)

        _request = build_delete_request(
            resource_group_name=resource_group_name,
            resource_name=resource_name,
            agent_pool_name=agent_pool_name,
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

        if response.status_code not in [202, 204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})  # type: ignore

    @distributed_trace_async
    async def begin_delete(
        self, resource_group_name: str, resource_name: str, agent_pool_name: str, **kwargs: Any
    ) -> AsyncLROPoller[None]:
        """Deletes an agent pool in the specified managed cluster.

        Deletes an agent pool in the specified managed cluster.

        :param resource_group_name: The name of the resource group. Required.
        :type resource_group_name: str
        :param resource_name: The name of the managed cluster resource. Required.
        :type resource_name: str
        :param agent_pool_name: The name of the agent pool. Required.
        :type agent_pool_name: str
        :return: An instance of AsyncLROPoller that returns either None or the result of cls(response)
        :rtype: ~azure.core.polling.AsyncLROPoller[None]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._api_version or "2021-05-01"))
        cls: ClsType[None] = kwargs.pop("cls", None)
        polling: Union[bool, AsyncPollingMethod] = kwargs.pop("polling", True)
        lro_delay = kwargs.pop("polling_interval", self._config.polling_interval)
        cont_token: Optional[str] = kwargs.pop("continuation_token", None)
        if cont_token is None:
            raw_result = await self._delete_initial(  # type: ignore
                resource_group_name=resource_group_name,
                resource_name=resource_name,
                agent_pool_name=agent_pool_name,
                api_version=api_version,
                cls=lambda x, y, z: x,
                headers=_headers,
                params=_params,
                **kwargs
            )
        kwargs.pop("error_map", None)

        def get_long_running_output(pipeline_response):  # pylint: disable=inconsistent-return-statements
            if cls:
                return cls(pipeline_response, None, {})  # type: ignore

        if polling is True:
            polling_method: AsyncPollingMethod = cast(AsyncPollingMethod, AsyncARMPolling(lro_delay, **kwargs))
        elif polling is False:
            polling_method = cast(AsyncPollingMethod, AsyncNoPolling())
        else:
            polling_method = polling
        if cont_token:
            return AsyncLROPoller[None].from_continuation_token(
                polling_method=polling_method,
                continuation_token=cont_token,
                client=self._client,
                deserialization_callback=get_long_running_output,
            )
        return AsyncLROPoller[None](self._client, raw_result, get_long_running_output, polling_method)  # type: ignore

    @distributed_trace_async
    async def get_upgrade_profile(
        self, resource_group_name: str, resource_name: str, agent_pool_name: str, **kwargs: Any
    ) -> _models.AgentPoolUpgradeProfile:
        """Gets the upgrade profile for an agent pool.

        Gets the upgrade profile for an agent pool.

        :param resource_group_name: The name of the resource group. Required.
        :type resource_group_name: str
        :param resource_name: The name of the managed cluster resource. Required.
        :type resource_name: str
        :param agent_pool_name: The name of the agent pool. Required.
        :type agent_pool_name: str
        :return: AgentPoolUpgradeProfile or the result of cls(response)
        :rtype: ~azure.mgmt.containerservice.v2021_05_01.models.AgentPoolUpgradeProfile
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

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._api_version or "2021-05-01"))
        cls: ClsType[_models.AgentPoolUpgradeProfile] = kwargs.pop("cls", None)

        _request = build_get_upgrade_profile_request(
            resource_group_name=resource_group_name,
            resource_name=resource_name,
            agent_pool_name=agent_pool_name,
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
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize("AgentPoolUpgradeProfile", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @distributed_trace_async
    async def get_available_agent_pool_versions(
        self, resource_group_name: str, resource_name: str, **kwargs: Any
    ) -> _models.AgentPoolAvailableVersions:
        """Gets a list of supported Kubernetes versions for the specified agent pool.

        See `supported Kubernetes versions
        <https://docs.microsoft.com/azure/aks/supported-kubernetes-versions>`_ for more details about
        the version lifecycle.

        :param resource_group_name: The name of the resource group. Required.
        :type resource_group_name: str
        :param resource_name: The name of the managed cluster resource. Required.
        :type resource_name: str
        :return: AgentPoolAvailableVersions or the result of cls(response)
        :rtype: ~azure.mgmt.containerservice.v2021_05_01.models.AgentPoolAvailableVersions
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

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._api_version or "2021-05-01"))
        cls: ClsType[_models.AgentPoolAvailableVersions] = kwargs.pop("cls", None)

        _request = build_get_available_agent_pool_versions_request(
            resource_group_name=resource_group_name,
            resource_name=resource_name,
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
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize("AgentPoolAvailableVersions", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    async def _upgrade_node_image_version_initial(
        self, resource_group_name: str, resource_name: str, agent_pool_name: str, **kwargs: Any
    ) -> Optional[_models.AgentPool]:
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._api_version or "2021-05-01"))
        cls: ClsType[Optional[_models.AgentPool]] = kwargs.pop("cls", None)

        _request = build_upgrade_node_image_version_request(
            resource_group_name=resource_group_name,
            resource_name=resource_name,
            agent_pool_name=agent_pool_name,
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

        if response.status_code not in [200, 202]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = None
        if response.status_code == 202:
            deserialized = self._deserialize("AgentPool", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @distributed_trace_async
    async def begin_upgrade_node_image_version(
        self, resource_group_name: str, resource_name: str, agent_pool_name: str, **kwargs: Any
    ) -> AsyncLROPoller[_models.AgentPool]:
        """Upgrades the node image version of an agent pool to the latest.

        Upgrading the node image version of an agent pool applies the newest OS and runtime updates to
        the nodes. AKS provides one new image per week with the latest updates. For more details on
        node image versions, see: https://docs.microsoft.com/azure/aks/node-image-upgrade.

        :param resource_group_name: The name of the resource group. Required.
        :type resource_group_name: str
        :param resource_name: The name of the managed cluster resource. Required.
        :type resource_name: str
        :param agent_pool_name: The name of the agent pool. Required.
        :type agent_pool_name: str
        :return: An instance of AsyncLROPoller that returns either AgentPool or the result of
         cls(response)
        :rtype:
         ~azure.core.polling.AsyncLROPoller[~azure.mgmt.containerservice.v2021_05_01.models.AgentPool]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._api_version or "2021-05-01"))
        cls: ClsType[None] = kwargs.pop("cls", None)
        polling: Union[bool, AsyncPollingMethod] = kwargs.pop("polling", True)
        lro_delay = kwargs.pop("polling_interval", self._config.polling_interval)
        cont_token: Optional[str] = kwargs.pop("continuation_token", None)
        if cont_token is None:
            raw_result = await self._upgrade_node_image_version_initial(
                resource_group_name=resource_group_name,
                resource_name=resource_name,
                agent_pool_name=agent_pool_name,
                api_version=api_version,
                cls=lambda x, y, z: x,
                headers=_headers,
                params=_params,
                **kwargs
            )
        kwargs.pop("error_map", None)

        def get_long_running_output(pipeline_response):
            deserialized = self._deserialize("AgentPool", pipeline_response)
            if cls:
                return cls(pipeline_response, deserialized, {})  # type: ignore
            return deserialized

        if polling is True:
            polling_method: AsyncPollingMethod = cast(AsyncPollingMethod, AsyncARMPolling(lro_delay, **kwargs))
        elif polling is False:
            polling_method = cast(AsyncPollingMethod, AsyncNoPolling())
        else:
            polling_method = polling
        if cont_token:
            return AsyncLROPoller[_models.AgentPool].from_continuation_token(
                polling_method=polling_method,
                continuation_token=cont_token,
                client=self._client,
                deserialization_callback=get_long_running_output,
            )
        return AsyncLROPoller[_models.AgentPool](
            self._client, raw_result, get_long_running_output, polling_method  # type: ignore
        )
