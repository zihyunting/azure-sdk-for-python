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
from ...operations._msix_packages_operations import (
    build_create_or_update_request,
    build_delete_request,
    build_get_request,
    build_list_request,
    build_update_request,
)

T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class MSIXPackagesOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.mgmt.desktopvirtualization.aio.DesktopVirtualizationMgmtClient`'s
        :attr:`msix_packages` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs) -> None:
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @distributed_trace_async
    async def get(
        self, resource_group_name: str, host_pool_name: str, msix_package_full_name: str, **kwargs: Any
    ) -> _models.MSIXPackage:
        """Get a msixpackage.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param host_pool_name: The name of the host pool within the specified resource group. Required.
        :type host_pool_name: str
        :param msix_package_full_name: The version specific package full name of the MSIX package
         within specified hostpool. Required.
        :type msix_package_full_name: str
        :return: MSIXPackage or the result of cls(response)
        :rtype: ~azure.mgmt.desktopvirtualization.models.MSIXPackage
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
        cls: ClsType[_models.MSIXPackage] = kwargs.pop("cls", None)

        _request = build_get_request(
            resource_group_name=resource_group_name,
            host_pool_name=host_pool_name,
            msix_package_full_name=msix_package_full_name,
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

        deserialized = self._deserialize("MSIXPackage", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @overload
    async def create_or_update(
        self,
        resource_group_name: str,
        host_pool_name: str,
        msix_package_full_name: str,
        msix_package: _models.MSIXPackage,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.MSIXPackage:
        """Create or update a MSIX package.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param host_pool_name: The name of the host pool within the specified resource group. Required.
        :type host_pool_name: str
        :param msix_package_full_name: The version specific package full name of the MSIX package
         within specified hostpool. Required.
        :type msix_package_full_name: str
        :param msix_package: Object containing  MSIX Package definitions. Required.
        :type msix_package: ~azure.mgmt.desktopvirtualization.models.MSIXPackage
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: MSIXPackage or the result of cls(response)
        :rtype: ~azure.mgmt.desktopvirtualization.models.MSIXPackage
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def create_or_update(
        self,
        resource_group_name: str,
        host_pool_name: str,
        msix_package_full_name: str,
        msix_package: IO[bytes],
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.MSIXPackage:
        """Create or update a MSIX package.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param host_pool_name: The name of the host pool within the specified resource group. Required.
        :type host_pool_name: str
        :param msix_package_full_name: The version specific package full name of the MSIX package
         within specified hostpool. Required.
        :type msix_package_full_name: str
        :param msix_package: Object containing  MSIX Package definitions. Required.
        :type msix_package: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: MSIXPackage or the result of cls(response)
        :rtype: ~azure.mgmt.desktopvirtualization.models.MSIXPackage
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def create_or_update(
        self,
        resource_group_name: str,
        host_pool_name: str,
        msix_package_full_name: str,
        msix_package: Union[_models.MSIXPackage, IO[bytes]],
        **kwargs: Any
    ) -> _models.MSIXPackage:
        """Create or update a MSIX package.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param host_pool_name: The name of the host pool within the specified resource group. Required.
        :type host_pool_name: str
        :param msix_package_full_name: The version specific package full name of the MSIX package
         within specified hostpool. Required.
        :type msix_package_full_name: str
        :param msix_package: Object containing  MSIX Package definitions. Is either a MSIXPackage type
         or a IO[bytes] type. Required.
        :type msix_package: ~azure.mgmt.desktopvirtualization.models.MSIXPackage or IO[bytes]
        :return: MSIXPackage or the result of cls(response)
        :rtype: ~azure.mgmt.desktopvirtualization.models.MSIXPackage
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
        cls: ClsType[_models.MSIXPackage] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(msix_package, (IOBase, bytes)):
            _content = msix_package
        else:
            _json = self._serialize.body(msix_package, "MSIXPackage")

        _request = build_create_or_update_request(
            resource_group_name=resource_group_name,
            host_pool_name=host_pool_name,
            msix_package_full_name=msix_package_full_name,
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
            deserialized = self._deserialize("MSIXPackage", pipeline_response)

        if response.status_code == 201:
            deserialized = self._deserialize("MSIXPackage", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @distributed_trace_async
    async def delete(  # pylint: disable=inconsistent-return-statements
        self, resource_group_name: str, host_pool_name: str, msix_package_full_name: str, **kwargs: Any
    ) -> None:
        """Remove an MSIX Package.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param host_pool_name: The name of the host pool within the specified resource group. Required.
        :type host_pool_name: str
        :param msix_package_full_name: The version specific package full name of the MSIX package
         within specified hostpool. Required.
        :type msix_package_full_name: str
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

        _request = build_delete_request(
            resource_group_name=resource_group_name,
            host_pool_name=host_pool_name,
            msix_package_full_name=msix_package_full_name,
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
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})  # type: ignore

    @overload
    async def update(
        self,
        resource_group_name: str,
        host_pool_name: str,
        msix_package_full_name: str,
        msix_package: Optional[_models.MSIXPackagePatch] = None,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.MSIXPackage:
        """Update an  MSIX Package.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param host_pool_name: The name of the host pool within the specified resource group. Required.
        :type host_pool_name: str
        :param msix_package_full_name: The version specific package full name of the MSIX package
         within specified hostpool. Required.
        :type msix_package_full_name: str
        :param msix_package: Object containing MSIX Package definitions. Default value is None.
        :type msix_package: ~azure.mgmt.desktopvirtualization.models.MSIXPackagePatch
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: MSIXPackage or the result of cls(response)
        :rtype: ~azure.mgmt.desktopvirtualization.models.MSIXPackage
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def update(
        self,
        resource_group_name: str,
        host_pool_name: str,
        msix_package_full_name: str,
        msix_package: Optional[IO[bytes]] = None,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.MSIXPackage:
        """Update an  MSIX Package.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param host_pool_name: The name of the host pool within the specified resource group. Required.
        :type host_pool_name: str
        :param msix_package_full_name: The version specific package full name of the MSIX package
         within specified hostpool. Required.
        :type msix_package_full_name: str
        :param msix_package: Object containing MSIX Package definitions. Default value is None.
        :type msix_package: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: MSIXPackage or the result of cls(response)
        :rtype: ~azure.mgmt.desktopvirtualization.models.MSIXPackage
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def update(
        self,
        resource_group_name: str,
        host_pool_name: str,
        msix_package_full_name: str,
        msix_package: Optional[Union[_models.MSIXPackagePatch, IO[bytes]]] = None,
        **kwargs: Any
    ) -> _models.MSIXPackage:
        """Update an  MSIX Package.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param host_pool_name: The name of the host pool within the specified resource group. Required.
        :type host_pool_name: str
        :param msix_package_full_name: The version specific package full name of the MSIX package
         within specified hostpool. Required.
        :type msix_package_full_name: str
        :param msix_package: Object containing MSIX Package definitions. Is either a MSIXPackagePatch
         type or a IO[bytes] type. Default value is None.
        :type msix_package: ~azure.mgmt.desktopvirtualization.models.MSIXPackagePatch or IO[bytes]
        :return: MSIXPackage or the result of cls(response)
        :rtype: ~azure.mgmt.desktopvirtualization.models.MSIXPackage
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
        cls: ClsType[_models.MSIXPackage] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(msix_package, (IOBase, bytes)):
            _content = msix_package
        else:
            if msix_package is not None:
                _json = self._serialize.body(msix_package, "MSIXPackagePatch")
            else:
                _json = None

        _request = build_update_request(
            resource_group_name=resource_group_name,
            host_pool_name=host_pool_name,
            msix_package_full_name=msix_package_full_name,
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
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize("MSIXPackage", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @distributed_trace
    def list(
        self,
        resource_group_name: str,
        host_pool_name: str,
        page_size: Optional[int] = None,
        is_descending: Optional[bool] = None,
        initial_skip: Optional[int] = None,
        **kwargs: Any
    ) -> AsyncIterable["_models.MSIXPackage"]:
        """List MSIX packages in hostpool.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param host_pool_name: The name of the host pool within the specified resource group. Required.
        :type host_pool_name: str
        :param page_size: Number of items per page. Default value is None.
        :type page_size: int
        :param is_descending: Indicates whether the collection is descending. Default value is None.
        :type is_descending: bool
        :param initial_skip: Initial number of items to skip. Default value is None.
        :type initial_skip: int
        :return: An iterator like instance of either MSIXPackage or the result of cls(response)
        :rtype:
         ~azure.core.async_paging.AsyncItemPaged[~azure.mgmt.desktopvirtualization.models.MSIXPackage]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))
        cls: ClsType[_models.MSIXPackageList] = kwargs.pop("cls", None)

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
                    host_pool_name=host_pool_name,
                    subscription_id=self._config.subscription_id,
                    page_size=page_size,
                    is_descending=is_descending,
                    initial_skip=initial_skip,
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
                _next_request_params["api-version"] = self._config.api_version
                _request = HttpRequest(
                    "GET", urllib.parse.urljoin(next_link, _parsed_next_link.path), params=_next_request_params
                )
                _request = _convert_request(_request)
                _request.url = self._client.format_url(_request.url)
                _request.method = "GET"
            return _request

        async def extract_data(pipeline_response):
            deserialized = self._deserialize("MSIXPackageList", pipeline_response)
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
