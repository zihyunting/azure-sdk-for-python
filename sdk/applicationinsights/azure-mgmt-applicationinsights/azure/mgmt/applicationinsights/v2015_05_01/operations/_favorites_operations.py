# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from io import IOBase
from typing import Any, Callable, Dict, IO, List, Optional, TypeVar, Union, overload

from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    ResourceNotModifiedError,
    map_error,
)
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator import distributed_trace
from azure.core.utils import case_insensitive_dict
from azure.mgmt.core.exceptions import ARMErrorFormat

from .. import models as _models
from ..._serialization import Serializer
from .._vendor import _convert_request

T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False


def build_list_request(
    resource_group_name: str,
    resource_name: str,
    subscription_id: str,
    *,
    favorite_type: Optional[Union[str, _models.FavoriteType]] = None,
    source_type: Optional[Union[str, _models.FavoriteSourceType]] = None,
    can_fetch_content: Optional[bool] = None,
    tags: Optional[List[str]] = None,
    **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2015-05-01"))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop(
        "template_url",
        "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Insights/components/{resourceName}/favorites",
    )  # pylint: disable=line-too-long
    path_format_arguments = {
        "resourceGroupName": _SERIALIZER.url(
            "resource_group_name", resource_group_name, "str", max_length=90, min_length=1
        ),
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, "str", min_length=1),
        "resourceName": _SERIALIZER.url("resource_name", resource_name, "str"),
    }

    _url: str = _url.format(**path_format_arguments)  # type: ignore

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")
    if favorite_type is not None:
        _params["favoriteType"] = _SERIALIZER.query("favorite_type", favorite_type, "str")
    if source_type is not None:
        _params["sourceType"] = _SERIALIZER.query("source_type", source_type, "str")
    if can_fetch_content is not None:
        _params["canFetchContent"] = _SERIALIZER.query("can_fetch_content", can_fetch_content, "bool")
    if tags is not None:
        _params["tags"] = _SERIALIZER.query("tags", tags, "[str]", div=",")

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, params=_params, headers=_headers, **kwargs)


def build_get_request(
    resource_group_name: str, resource_name: str, favorite_id: str, subscription_id: str, **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2015-05-01"))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop(
        "template_url",
        "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Insights/components/{resourceName}/favorites/{favoriteId}",
    )  # pylint: disable=line-too-long
    path_format_arguments = {
        "resourceGroupName": _SERIALIZER.url(
            "resource_group_name", resource_group_name, "str", max_length=90, min_length=1
        ),
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, "str", min_length=1),
        "resourceName": _SERIALIZER.url("resource_name", resource_name, "str"),
        "favoriteId": _SERIALIZER.url("favorite_id", favorite_id, "str"),
    }

    _url: str = _url.format(**path_format_arguments)  # type: ignore

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, params=_params, headers=_headers, **kwargs)


def build_add_request(
    resource_group_name: str, resource_name: str, favorite_id: str, subscription_id: str, **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2015-05-01"))
    content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop(
        "template_url",
        "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Insights/components/{resourceName}/favorites/{favoriteId}",
    )  # pylint: disable=line-too-long
    path_format_arguments = {
        "resourceGroupName": _SERIALIZER.url(
            "resource_group_name", resource_group_name, "str", max_length=90, min_length=1
        ),
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, "str", min_length=1),
        "resourceName": _SERIALIZER.url("resource_name", resource_name, "str"),
        "favoriteId": _SERIALIZER.url("favorite_id", favorite_id, "str"),
    }

    _url: str = _url.format(**path_format_arguments)  # type: ignore

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="PUT", url=_url, params=_params, headers=_headers, **kwargs)


def build_update_request(
    resource_group_name: str, resource_name: str, favorite_id: str, subscription_id: str, **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2015-05-01"))
    content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop(
        "template_url",
        "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Insights/components/{resourceName}/favorites/{favoriteId}",
    )  # pylint: disable=line-too-long
    path_format_arguments = {
        "resourceGroupName": _SERIALIZER.url(
            "resource_group_name", resource_group_name, "str", max_length=90, min_length=1
        ),
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, "str", min_length=1),
        "resourceName": _SERIALIZER.url("resource_name", resource_name, "str"),
        "favoriteId": _SERIALIZER.url("favorite_id", favorite_id, "str"),
    }

    _url: str = _url.format(**path_format_arguments)  # type: ignore

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="PATCH", url=_url, params=_params, headers=_headers, **kwargs)


def build_delete_request(
    resource_group_name: str, resource_name: str, favorite_id: str, subscription_id: str, **kwargs: Any
) -> HttpRequest:
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2015-05-01"))
    # Construct URL
    _url = kwargs.pop(
        "template_url",
        "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Insights/components/{resourceName}/favorites/{favoriteId}",
    )  # pylint: disable=line-too-long
    path_format_arguments = {
        "resourceGroupName": _SERIALIZER.url(
            "resource_group_name", resource_group_name, "str", max_length=90, min_length=1
        ),
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, "str", min_length=1),
        "resourceName": _SERIALIZER.url("resource_name", resource_name, "str"),
        "favoriteId": _SERIALIZER.url("favorite_id", favorite_id, "str"),
    }

    _url: str = _url.format(**path_format_arguments)  # type: ignore

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    return HttpRequest(method="DELETE", url=_url, params=_params, **kwargs)


class FavoritesOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.mgmt.applicationinsights.v2015_05_01.ApplicationInsightsManagementClient`'s
        :attr:`favorites` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs):
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")
        self._api_version = input_args.pop(0) if input_args else kwargs.pop("api_version")

    @distributed_trace
    def list(
        self,
        resource_group_name: str,
        resource_name: str,
        favorite_type: Optional[Union[str, _models.FavoriteType]] = None,
        source_type: Optional[Union[str, _models.FavoriteSourceType]] = None,
        can_fetch_content: Optional[bool] = None,
        tags: Optional[List[str]] = None,
        **kwargs: Any
    ) -> List[_models.ApplicationInsightsComponentFavorite]:
        """Gets a list of favorites defined within an Application Insights component.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param resource_name: The name of the Application Insights component resource. Required.
        :type resource_name: str
        :param favorite_type: The type of favorite. Value can be either shared or user. Known values
         are: "shared" and "user". Default value is None.
        :type favorite_type: str or ~azure.mgmt.applicationinsights.v2015_05_01.models.FavoriteType
        :param source_type: Source type of favorite to return. When left out, the source type defaults
         to 'other' (not present in this enum). Known values are: "retention", "notebook", "sessions",
         "events", "userflows", "funnel", "impact", and "segmentation". Default value is None.
        :type source_type: str or ~azure.mgmt.applicationinsights.v2015_05_01.models.FavoriteSourceType
        :param can_fetch_content: Flag indicating whether or not to return the full content for each
         applicable favorite. If false, only return summary content for favorites. Default value is
         None.
        :type can_fetch_content: bool
        :param tags: Tags that must be present on each favorite returned. Default value is None.
        :type tags: list[str]
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: list of ApplicationInsightsComponentFavorite or the result of cls(response)
        :rtype:
         list[~azure.mgmt.applicationinsights.v2015_05_01.models.ApplicationInsightsComponentFavorite]
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

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._api_version or "2015-05-01"))
        cls: ClsType[List[_models.ApplicationInsightsComponentFavorite]] = kwargs.pop("cls", None)

        request = build_list_request(
            resource_group_name=resource_group_name,
            resource_name=resource_name,
            subscription_id=self._config.subscription_id,
            favorite_type=favorite_type,
            source_type=source_type,
            can_fetch_content=can_fetch_content,
            tags=tags,
            api_version=api_version,
            template_url=self.list.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        _stream = False
        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize("[ApplicationInsightsComponentFavorite]", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    list.metadata = {
        "url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Insights/components/{resourceName}/favorites"
    }

    @distributed_trace
    def get(
        self, resource_group_name: str, resource_name: str, favorite_id: str, **kwargs: Any
    ) -> _models.ApplicationInsightsComponentFavorite:
        """Get a single favorite by its FavoriteId, defined within an Application Insights component.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param resource_name: The name of the Application Insights component resource. Required.
        :type resource_name: str
        :param favorite_id: The Id of a specific favorite defined in the Application Insights
         component. Required.
        :type favorite_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ApplicationInsightsComponentFavorite or the result of cls(response)
        :rtype: ~azure.mgmt.applicationinsights.v2015_05_01.models.ApplicationInsightsComponentFavorite
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

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._api_version or "2015-05-01"))
        cls: ClsType[_models.ApplicationInsightsComponentFavorite] = kwargs.pop("cls", None)

        request = build_get_request(
            resource_group_name=resource_group_name,
            resource_name=resource_name,
            favorite_id=favorite_id,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            template_url=self.get.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        _stream = False
        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize("ApplicationInsightsComponentFavorite", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get.metadata = {
        "url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Insights/components/{resourceName}/favorites/{favoriteId}"
    }

    @overload
    def add(
        self,
        resource_group_name: str,
        resource_name: str,
        favorite_id: str,
        favorite_properties: _models.ApplicationInsightsComponentFavorite,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.ApplicationInsightsComponentFavorite:
        """Adds a new favorites to an Application Insights component.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param resource_name: The name of the Application Insights component resource. Required.
        :type resource_name: str
        :param favorite_id: The Id of a specific favorite defined in the Application Insights
         component. Required.
        :type favorite_id: str
        :param favorite_properties: Properties that need to be specified to create a new favorite and
         add it to an Application Insights component. Required.
        :type favorite_properties:
         ~azure.mgmt.applicationinsights.v2015_05_01.models.ApplicationInsightsComponentFavorite
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ApplicationInsightsComponentFavorite or the result of cls(response)
        :rtype: ~azure.mgmt.applicationinsights.v2015_05_01.models.ApplicationInsightsComponentFavorite
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    def add(
        self,
        resource_group_name: str,
        resource_name: str,
        favorite_id: str,
        favorite_properties: IO,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.ApplicationInsightsComponentFavorite:
        """Adds a new favorites to an Application Insights component.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param resource_name: The name of the Application Insights component resource. Required.
        :type resource_name: str
        :param favorite_id: The Id of a specific favorite defined in the Application Insights
         component. Required.
        :type favorite_id: str
        :param favorite_properties: Properties that need to be specified to create a new favorite and
         add it to an Application Insights component. Required.
        :type favorite_properties: IO
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ApplicationInsightsComponentFavorite or the result of cls(response)
        :rtype: ~azure.mgmt.applicationinsights.v2015_05_01.models.ApplicationInsightsComponentFavorite
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace
    def add(
        self,
        resource_group_name: str,
        resource_name: str,
        favorite_id: str,
        favorite_properties: Union[_models.ApplicationInsightsComponentFavorite, IO],
        **kwargs: Any
    ) -> _models.ApplicationInsightsComponentFavorite:
        """Adds a new favorites to an Application Insights component.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param resource_name: The name of the Application Insights component resource. Required.
        :type resource_name: str
        :param favorite_id: The Id of a specific favorite defined in the Application Insights
         component. Required.
        :type favorite_id: str
        :param favorite_properties: Properties that need to be specified to create a new favorite and
         add it to an Application Insights component. Is either a ApplicationInsightsComponentFavorite
         type or a IO type. Required.
        :type favorite_properties:
         ~azure.mgmt.applicationinsights.v2015_05_01.models.ApplicationInsightsComponentFavorite or IO
        :keyword content_type: Body Parameter content-type. Known values are: 'application/json'.
         Default value is None.
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ApplicationInsightsComponentFavorite or the result of cls(response)
        :rtype: ~azure.mgmt.applicationinsights.v2015_05_01.models.ApplicationInsightsComponentFavorite
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

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._api_version or "2015-05-01"))
        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.ApplicationInsightsComponentFavorite] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(favorite_properties, (IOBase, bytes)):
            _content = favorite_properties
        else:
            _json = self._serialize.body(favorite_properties, "ApplicationInsightsComponentFavorite")

        request = build_add_request(
            resource_group_name=resource_group_name,
            resource_name=resource_name,
            favorite_id=favorite_id,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            content=_content,
            template_url=self.add.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        _stream = False
        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize("ApplicationInsightsComponentFavorite", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    add.metadata = {
        "url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Insights/components/{resourceName}/favorites/{favoriteId}"
    }

    @overload
    def update(
        self,
        resource_group_name: str,
        resource_name: str,
        favorite_id: str,
        favorite_properties: _models.ApplicationInsightsComponentFavorite,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.ApplicationInsightsComponentFavorite:
        """Updates a favorite that has already been added to an Application Insights component.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param resource_name: The name of the Application Insights component resource. Required.
        :type resource_name: str
        :param favorite_id: The Id of a specific favorite defined in the Application Insights
         component. Required.
        :type favorite_id: str
        :param favorite_properties: Properties that need to be specified to update the existing
         favorite. Required.
        :type favorite_properties:
         ~azure.mgmt.applicationinsights.v2015_05_01.models.ApplicationInsightsComponentFavorite
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ApplicationInsightsComponentFavorite or the result of cls(response)
        :rtype: ~azure.mgmt.applicationinsights.v2015_05_01.models.ApplicationInsightsComponentFavorite
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    def update(
        self,
        resource_group_name: str,
        resource_name: str,
        favorite_id: str,
        favorite_properties: IO,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.ApplicationInsightsComponentFavorite:
        """Updates a favorite that has already been added to an Application Insights component.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param resource_name: The name of the Application Insights component resource. Required.
        :type resource_name: str
        :param favorite_id: The Id of a specific favorite defined in the Application Insights
         component. Required.
        :type favorite_id: str
        :param favorite_properties: Properties that need to be specified to update the existing
         favorite. Required.
        :type favorite_properties: IO
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ApplicationInsightsComponentFavorite or the result of cls(response)
        :rtype: ~azure.mgmt.applicationinsights.v2015_05_01.models.ApplicationInsightsComponentFavorite
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace
    def update(
        self,
        resource_group_name: str,
        resource_name: str,
        favorite_id: str,
        favorite_properties: Union[_models.ApplicationInsightsComponentFavorite, IO],
        **kwargs: Any
    ) -> _models.ApplicationInsightsComponentFavorite:
        """Updates a favorite that has already been added to an Application Insights component.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param resource_name: The name of the Application Insights component resource. Required.
        :type resource_name: str
        :param favorite_id: The Id of a specific favorite defined in the Application Insights
         component. Required.
        :type favorite_id: str
        :param favorite_properties: Properties that need to be specified to update the existing
         favorite. Is either a ApplicationInsightsComponentFavorite type or a IO type. Required.
        :type favorite_properties:
         ~azure.mgmt.applicationinsights.v2015_05_01.models.ApplicationInsightsComponentFavorite or IO
        :keyword content_type: Body Parameter content-type. Known values are: 'application/json'.
         Default value is None.
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ApplicationInsightsComponentFavorite or the result of cls(response)
        :rtype: ~azure.mgmt.applicationinsights.v2015_05_01.models.ApplicationInsightsComponentFavorite
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

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._api_version or "2015-05-01"))
        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.ApplicationInsightsComponentFavorite] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(favorite_properties, (IOBase, bytes)):
            _content = favorite_properties
        else:
            _json = self._serialize.body(favorite_properties, "ApplicationInsightsComponentFavorite")

        request = build_update_request(
            resource_group_name=resource_group_name,
            resource_name=resource_name,
            favorite_id=favorite_id,
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
        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize("ApplicationInsightsComponentFavorite", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    update.metadata = {
        "url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Insights/components/{resourceName}/favorites/{favoriteId}"
    }

    @distributed_trace
    def delete(  # pylint: disable=inconsistent-return-statements
        self, resource_group_name: str, resource_name: str, favorite_id: str, **kwargs: Any
    ) -> None:
        """Remove a favorite that is associated to an Application Insights component.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param resource_name: The name of the Application Insights component resource. Required.
        :type resource_name: str
        :param favorite_id: The Id of a specific favorite defined in the Application Insights
         component. Required.
        :type favorite_id: str
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

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._api_version or "2015-05-01"))
        cls: ClsType[None] = kwargs.pop("cls", None)

        request = build_delete_request(
            resource_group_name=resource_group_name,
            resource_name=resource_name,
            favorite_id=favorite_id,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            template_url=self.delete.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        _stream = False
        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    delete.metadata = {
        "url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Insights/components/{resourceName}/favorites/{favoriteId}"
    }
