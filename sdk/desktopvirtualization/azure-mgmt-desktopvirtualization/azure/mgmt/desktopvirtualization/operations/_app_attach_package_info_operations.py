# pylint: disable=too-many-lines,too-many-statements
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from io import IOBase
from typing import Any, Callable, Dict, IO, Iterable, Optional, TypeVar, Union, overload
import urllib.parse

from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    ResourceNotModifiedError,
    map_error,
)
from azure.core.paging import ItemPaged
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator import distributed_trace
from azure.core.utils import case_insensitive_dict
from azure.mgmt.core.exceptions import ARMErrorFormat

from .. import models as _models
from .._serialization import Serializer
from .._vendor import _convert_request

T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False


def build_import_method_request(
    resource_group_name: str, host_pool_name: str, subscription_id: str, **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2024-03-06-preview"))
    content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop(
        "template_url",
        "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DesktopVirtualization/hostPools/{hostPoolName}/importAppAttachPackageInfo",
    )  # pylint: disable=line-too-long
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, "str", min_length=1),
        "resourceGroupName": _SERIALIZER.url(
            "resource_group_name", resource_group_name, "str", max_length=90, min_length=1
        ),
        "hostPoolName": _SERIALIZER.url("host_pool_name", host_pool_name, "str", max_length=64, min_length=3),
    }

    _url: str = _url.format(**path_format_arguments)  # type: ignore

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="POST", url=_url, params=_params, headers=_headers, **kwargs)


class AppAttachPackageInfoOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.mgmt.desktopvirtualization.DesktopVirtualizationMgmtClient`'s
        :attr:`app_attach_package_info` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs):
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @overload
    def import_method(
        self,
        resource_group_name: str,
        host_pool_name: str,
        import_package_info_request: _models.ImportPackageInfoRequest,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> Iterable["_models.AppAttachPackage"]:
        """Gets information from a package given the path to the package.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param host_pool_name: The name of the host pool within the specified resource group. Required.
        :type host_pool_name: str
        :param import_package_info_request: Object containing URI to package image and other optional
         properties. Required.
        :type import_package_info_request:
         ~azure.mgmt.desktopvirtualization.models.ImportPackageInfoRequest
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An iterator like instance of either AppAttachPackage or the result of cls(response)
        :rtype: ~azure.core.paging.ItemPaged[~azure.mgmt.desktopvirtualization.models.AppAttachPackage]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    def import_method(
        self,
        resource_group_name: str,
        host_pool_name: str,
        import_package_info_request: IO[bytes],
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> Iterable["_models.AppAttachPackage"]:
        """Gets information from a package given the path to the package.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param host_pool_name: The name of the host pool within the specified resource group. Required.
        :type host_pool_name: str
        :param import_package_info_request: Object containing URI to package image and other optional
         properties. Required.
        :type import_package_info_request: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An iterator like instance of either AppAttachPackage or the result of cls(response)
        :rtype: ~azure.core.paging.ItemPaged[~azure.mgmt.desktopvirtualization.models.AppAttachPackage]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace
    def import_method(
        self,
        resource_group_name: str,
        host_pool_name: str,
        import_package_info_request: Union[_models.ImportPackageInfoRequest, IO[bytes]],
        **kwargs: Any
    ) -> Iterable["_models.AppAttachPackage"]:
        """Gets information from a package given the path to the package.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param host_pool_name: The name of the host pool within the specified resource group. Required.
        :type host_pool_name: str
        :param import_package_info_request: Object containing URI to package image and other optional
         properties. Is either a ImportPackageInfoRequest type or a IO[bytes] type. Required.
        :type import_package_info_request:
         ~azure.mgmt.desktopvirtualization.models.ImportPackageInfoRequest or IO[bytes]
        :return: An iterator like instance of either AppAttachPackage or the result of cls(response)
        :rtype: ~azure.core.paging.ItemPaged[~azure.mgmt.desktopvirtualization.models.AppAttachPackage]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))
        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.AppAttachPackageList] = kwargs.pop("cls", None)

        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})
        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(import_package_info_request, (IOBase, bytes)):
            _content = import_package_info_request
        else:
            _json = self._serialize.body(import_package_info_request, "ImportPackageInfoRequest")

        def prepare_request(next_link=None):
            if not next_link:

                _request = build_import_method_request(
                    resource_group_name=resource_group_name,
                    host_pool_name=host_pool_name,
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

        def extract_data(pipeline_response):
            deserialized = self._deserialize("AppAttachPackageList", pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)  # type: ignore
            return deserialized.next_link or None, iter(list_of_elem)

        def get_next(next_link=None):
            _request = prepare_request(next_link)

            _stream = False
            pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
                _request, stream=_stream, **kwargs
            )
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
                raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

            return pipeline_response

        return ItemPaged(get_next, extract_data)
