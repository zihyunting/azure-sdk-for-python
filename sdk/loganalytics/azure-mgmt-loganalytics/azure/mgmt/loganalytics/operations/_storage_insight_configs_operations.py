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


def build_create_or_update_request(
    resource_group_name: str, workspace_name: str, storage_insight_name: str, subscription_id: str, **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2020-08-01"))
    content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop(
        "template_url",
        "/subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.OperationalInsights/workspaces/{workspaceName}/storageInsightConfigs/{storageInsightName}",
    )  # pylint: disable=line-too-long
    path_format_arguments = {
        "resourceGroupName": _SERIALIZER.url(
            "resource_group_name", resource_group_name, "str", max_length=90, min_length=1
        ),
        "workspaceName": _SERIALIZER.url(
            "workspace_name",
            workspace_name,
            "str",
            max_length=63,
            min_length=4,
            pattern=r"^[A-Za-z0-9][A-Za-z0-9-]+[A-Za-z0-9]$",
        ),
        "storageInsightName": _SERIALIZER.url("storage_insight_name", storage_insight_name, "str"),
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, "str", min_length=1),
    }

    _url: str = _url.format(**path_format_arguments)  # type: ignore

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="PUT", url=_url, params=_params, headers=_headers, **kwargs)


def build_get_request(
    resource_group_name: str, workspace_name: str, storage_insight_name: str, subscription_id: str, **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2020-08-01"))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop(
        "template_url",
        "/subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.OperationalInsights/workspaces/{workspaceName}/storageInsightConfigs/{storageInsightName}",
    )  # pylint: disable=line-too-long
    path_format_arguments = {
        "resourceGroupName": _SERIALIZER.url(
            "resource_group_name", resource_group_name, "str", max_length=90, min_length=1
        ),
        "workspaceName": _SERIALIZER.url(
            "workspace_name",
            workspace_name,
            "str",
            max_length=63,
            min_length=4,
            pattern=r"^[A-Za-z0-9][A-Za-z0-9-]+[A-Za-z0-9]$",
        ),
        "storageInsightName": _SERIALIZER.url("storage_insight_name", storage_insight_name, "str"),
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, "str", min_length=1),
    }

    _url: str = _url.format(**path_format_arguments)  # type: ignore

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, params=_params, headers=_headers, **kwargs)


def build_delete_request(
    resource_group_name: str, workspace_name: str, storage_insight_name: str, subscription_id: str, **kwargs: Any
) -> HttpRequest:
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2020-08-01"))
    # Construct URL
    _url = kwargs.pop(
        "template_url",
        "/subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.OperationalInsights/workspaces/{workspaceName}/storageInsightConfigs/{storageInsightName}",
    )  # pylint: disable=line-too-long
    path_format_arguments = {
        "resourceGroupName": _SERIALIZER.url(
            "resource_group_name", resource_group_name, "str", max_length=90, min_length=1
        ),
        "workspaceName": _SERIALIZER.url(
            "workspace_name",
            workspace_name,
            "str",
            max_length=63,
            min_length=4,
            pattern=r"^[A-Za-z0-9][A-Za-z0-9-]+[A-Za-z0-9]$",
        ),
        "storageInsightName": _SERIALIZER.url("storage_insight_name", storage_insight_name, "str"),
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, "str", min_length=1),
    }

    _url: str = _url.format(**path_format_arguments)  # type: ignore

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    return HttpRequest(method="DELETE", url=_url, params=_params, **kwargs)


def build_list_by_workspace_request(
    resource_group_name: str, workspace_name: str, subscription_id: str, **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2020-08-01"))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop(
        "template_url",
        "/subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.OperationalInsights/workspaces/{workspaceName}/storageInsightConfigs",
    )  # pylint: disable=line-too-long
    path_format_arguments = {
        "resourceGroupName": _SERIALIZER.url(
            "resource_group_name", resource_group_name, "str", max_length=90, min_length=1
        ),
        "workspaceName": _SERIALIZER.url(
            "workspace_name",
            workspace_name,
            "str",
            max_length=63,
            min_length=4,
            pattern=r"^[A-Za-z0-9][A-Za-z0-9-]+[A-Za-z0-9]$",
        ),
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, "str", min_length=1),
    }

    _url: str = _url.format(**path_format_arguments)  # type: ignore

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, params=_params, headers=_headers, **kwargs)


class StorageInsightConfigsOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.mgmt.loganalytics.LogAnalyticsManagementClient`'s
        :attr:`storage_insight_configs` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs):
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @overload
    def create_or_update(
        self,
        resource_group_name: str,
        workspace_name: str,
        storage_insight_name: str,
        parameters: _models.StorageInsight,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.StorageInsight:
        """Create or update a storage insight.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param workspace_name: The name of the workspace. Required.
        :type workspace_name: str
        :param storage_insight_name: Name of the storageInsightsConfigs resource. Required.
        :type storage_insight_name: str
        :param parameters: The parameters required to create or update a storage insight. Required.
        :type parameters: ~azure.mgmt.loganalytics.models.StorageInsight
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: StorageInsight or the result of cls(response)
        :rtype: ~azure.mgmt.loganalytics.models.StorageInsight
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    def create_or_update(
        self,
        resource_group_name: str,
        workspace_name: str,
        storage_insight_name: str,
        parameters: IO[bytes],
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.StorageInsight:
        """Create or update a storage insight.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param workspace_name: The name of the workspace. Required.
        :type workspace_name: str
        :param storage_insight_name: Name of the storageInsightsConfigs resource. Required.
        :type storage_insight_name: str
        :param parameters: The parameters required to create or update a storage insight. Required.
        :type parameters: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: StorageInsight or the result of cls(response)
        :rtype: ~azure.mgmt.loganalytics.models.StorageInsight
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace
    def create_or_update(
        self,
        resource_group_name: str,
        workspace_name: str,
        storage_insight_name: str,
        parameters: Union[_models.StorageInsight, IO[bytes]],
        **kwargs: Any
    ) -> _models.StorageInsight:
        """Create or update a storage insight.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param workspace_name: The name of the workspace. Required.
        :type workspace_name: str
        :param storage_insight_name: Name of the storageInsightsConfigs resource. Required.
        :type storage_insight_name: str
        :param parameters: The parameters required to create or update a storage insight. Is either a
         StorageInsight type or a IO[bytes] type. Required.
        :type parameters: ~azure.mgmt.loganalytics.models.StorageInsight or IO[bytes]
        :return: StorageInsight or the result of cls(response)
        :rtype: ~azure.mgmt.loganalytics.models.StorageInsight
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

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2020-08-01"))
        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.StorageInsight] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(parameters, (IOBase, bytes)):
            _content = parameters
        else:
            _json = self._serialize.body(parameters, "StorageInsight")

        _request = build_create_or_update_request(
            resource_group_name=resource_group_name,
            workspace_name=workspace_name,
            storage_insight_name=storage_insight_name,
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
        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200, 201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        if response.status_code == 200:
            deserialized = self._deserialize("StorageInsight", pipeline_response)

        if response.status_code == 201:
            deserialized = self._deserialize("StorageInsight", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @distributed_trace
    def get(
        self, resource_group_name: str, workspace_name: str, storage_insight_name: str, **kwargs: Any
    ) -> _models.StorageInsight:
        """Gets a storage insight instance.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param workspace_name: The name of the workspace. Required.
        :type workspace_name: str
        :param storage_insight_name: Name of the storageInsightsConfigs resource. Required.
        :type storage_insight_name: str
        :return: StorageInsight or the result of cls(response)
        :rtype: ~azure.mgmt.loganalytics.models.StorageInsight
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

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2020-08-01"))
        cls: ClsType[_models.StorageInsight] = kwargs.pop("cls", None)

        _request = build_get_request(
            resource_group_name=resource_group_name,
            workspace_name=workspace_name,
            storage_insight_name=storage_insight_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            headers=_headers,
            params=_params,
        )
        _request = _convert_request(_request)
        _request.url = self._client.format_url(_request.url)

        _stream = False
        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize("StorageInsight", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @distributed_trace
    def delete(  # pylint: disable=inconsistent-return-statements
        self, resource_group_name: str, workspace_name: str, storage_insight_name: str, **kwargs: Any
    ) -> None:
        """Deletes a storageInsightsConfigs resource.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param workspace_name: The name of the workspace. Required.
        :type workspace_name: str
        :param storage_insight_name: Name of the storageInsightsConfigs resource. Required.
        :type storage_insight_name: str
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

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2020-08-01"))
        cls: ClsType[None] = kwargs.pop("cls", None)

        _request = build_delete_request(
            resource_group_name=resource_group_name,
            workspace_name=workspace_name,
            storage_insight_name=storage_insight_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            headers=_headers,
            params=_params,
        )
        _request = _convert_request(_request)
        _request.url = self._client.format_url(_request.url)

        _stream = False
        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200, 204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})  # type: ignore

    @distributed_trace
    def list_by_workspace(
        self, resource_group_name: str, workspace_name: str, **kwargs: Any
    ) -> Iterable["_models.StorageInsight"]:
        """Lists the storage insight instances within a workspace.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param workspace_name: The name of the workspace. Required.
        :type workspace_name: str
        :return: An iterator like instance of either StorageInsight or the result of cls(response)
        :rtype: ~azure.core.paging.ItemPaged[~azure.mgmt.loganalytics.models.StorageInsight]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2020-08-01"))
        cls: ClsType[_models.StorageInsightListResult] = kwargs.pop("cls", None)

        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        def prepare_request(next_link=None):
            if not next_link:

                _request = build_list_by_workspace_request(
                    resource_group_name=resource_group_name,
                    workspace_name=workspace_name,
                    subscription_id=self._config.subscription_id,
                    api_version=api_version,
                    headers=_headers,
                    params=_params,
                )
                _request = _convert_request(_request)
                _request.url = self._client.format_url(_request.url)

            else:
                _request = HttpRequest("GET", next_link)
                _request = _convert_request(_request)
                _request.url = self._client.format_url(_request.url)
                _request.method = "GET"
            return _request

        def extract_data(pipeline_response):
            deserialized = self._deserialize("StorageInsightListResult", pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)  # type: ignore
            return deserialized.odata_next_link or None, iter(list_of_elem)

        def get_next(next_link=None):
            _request = prepare_request(next_link)

            _stream = False
            pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
                _request, stream=_stream, **kwargs
            )
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response, error_format=ARMErrorFormat)

            return pipeline_response

        return ItemPaged(get_next, extract_data)
