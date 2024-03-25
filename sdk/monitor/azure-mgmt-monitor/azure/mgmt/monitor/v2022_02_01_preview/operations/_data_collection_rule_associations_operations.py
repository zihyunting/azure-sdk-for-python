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
from ..._serialization import Serializer
from .._vendor import _convert_request

T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False


def build_list_by_resource_request(resource_uri: str, **kwargs: Any) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2021-09-01-preview"))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop("template_url", "/{resourceUri}/providers/Microsoft.Insights/dataCollectionRuleAssociations")
    path_format_arguments = {
        "resourceUri": _SERIALIZER.url("resource_uri", resource_uri, "str", skip_quote=True, min_length=1),
    }

    _url: str = _url.format(**path_format_arguments)  # type: ignore

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, params=_params, headers=_headers, **kwargs)


def build_list_by_rule_request(
    resource_group_name: str, data_collection_rule_name: str, subscription_id: str, **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2021-09-01-preview"))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop(
        "template_url",
        "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Insights/dataCollectionRules/{dataCollectionRuleName}/associations",
    )  # pylint: disable=line-too-long
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, "str", min_length=1),
        "resourceGroupName": _SERIALIZER.url(
            "resource_group_name", resource_group_name, "str", max_length=90, min_length=1
        ),
        "dataCollectionRuleName": _SERIALIZER.url("data_collection_rule_name", data_collection_rule_name, "str"),
    }

    _url: str = _url.format(**path_format_arguments)  # type: ignore

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, params=_params, headers=_headers, **kwargs)


def build_list_by_data_collection_endpoint_request(  # pylint: disable=name-too-long
    resource_group_name: str, data_collection_endpoint_name: str, subscription_id: str, **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2021-09-01-preview"))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop(
        "template_url",
        "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Insights/dataCollectionEndpoints/{dataCollectionEndpointName}/associations",
    )  # pylint: disable=line-too-long
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, "str", min_length=1),
        "resourceGroupName": _SERIALIZER.url(
            "resource_group_name", resource_group_name, "str", max_length=90, min_length=1
        ),
        "dataCollectionEndpointName": _SERIALIZER.url(
            "data_collection_endpoint_name", data_collection_endpoint_name, "str"
        ),
    }

    _url: str = _url.format(**path_format_arguments)  # type: ignore

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, params=_params, headers=_headers, **kwargs)


def build_get_request(resource_uri: str, association_name: str, **kwargs: Any) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2021-09-01-preview"))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop(
        "template_url", "/{resourceUri}/providers/Microsoft.Insights/dataCollectionRuleAssociations/{associationName}"
    )  # pylint: disable=line-too-long
    path_format_arguments = {
        "resourceUri": _SERIALIZER.url("resource_uri", resource_uri, "str", skip_quote=True, min_length=1),
        "associationName": _SERIALIZER.url("association_name", association_name, "str"),
    }

    _url: str = _url.format(**path_format_arguments)  # type: ignore

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, params=_params, headers=_headers, **kwargs)


def build_create_request(resource_uri: str, association_name: str, **kwargs: Any) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2021-09-01-preview"))
    content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop(
        "template_url", "/{resourceUri}/providers/Microsoft.Insights/dataCollectionRuleAssociations/{associationName}"
    )  # pylint: disable=line-too-long
    path_format_arguments = {
        "resourceUri": _SERIALIZER.url("resource_uri", resource_uri, "str", skip_quote=True, min_length=1),
        "associationName": _SERIALIZER.url("association_name", association_name, "str"),
    }

    _url: str = _url.format(**path_format_arguments)  # type: ignore

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="PUT", url=_url, params=_params, headers=_headers, **kwargs)


def build_delete_request(resource_uri: str, association_name: str, **kwargs: Any) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2021-09-01-preview"))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop(
        "template_url", "/{resourceUri}/providers/Microsoft.Insights/dataCollectionRuleAssociations/{associationName}"
    )  # pylint: disable=line-too-long
    path_format_arguments = {
        "resourceUri": _SERIALIZER.url("resource_uri", resource_uri, "str", skip_quote=True, min_length=1),
        "associationName": _SERIALIZER.url("association_name", association_name, "str"),
    }

    _url: str = _url.format(**path_format_arguments)  # type: ignore

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="DELETE", url=_url, params=_params, headers=_headers, **kwargs)


class DataCollectionRuleAssociationsOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.mgmt.monitor.v2022_02_01_preview.MonitorManagementClient`'s
        :attr:`data_collection_rule_associations` attribute.
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
    def list_by_resource(
        self, resource_uri: str, **kwargs: Any
    ) -> Iterable["_models.DataCollectionRuleAssociationProxyOnlyResource"]:
        """Lists associations for the specified resource.

        Lists associations for the specified resource.

        :param resource_uri: The identifier of the resource. Required.
        :type resource_uri: str
        :return: An iterator like instance of either DataCollectionRuleAssociationProxyOnlyResource or
         the result of cls(response)
        :rtype:
         ~azure.core.paging.ItemPaged[~azure.mgmt.monitor.v2022_02_01_preview.models.DataCollectionRuleAssociationProxyOnlyResource]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop(
            "api_version", _params.pop("api-version", self._api_version or "2021-09-01-preview")
        )
        cls: ClsType[_models.DataCollectionRuleAssociationProxyOnlyResourceListResult] = kwargs.pop("cls", None)

        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        def prepare_request(next_link=None):
            if not next_link:

                _request = build_list_by_resource_request(
                    resource_uri=resource_uri,
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

        def extract_data(pipeline_response):
            deserialized = self._deserialize(
                "DataCollectionRuleAssociationProxyOnlyResourceListResult", pipeline_response
            )
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
                error = self._deserialize.failsafe_deserialize(_models.ErrorResponseCommonV2, pipeline_response)
                raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

            return pipeline_response

        return ItemPaged(get_next, extract_data)

    @distributed_trace
    def list_by_rule(
        self, resource_group_name: str, data_collection_rule_name: str, **kwargs: Any
    ) -> Iterable["_models.DataCollectionRuleAssociationProxyOnlyResource"]:
        """Lists associations for the specified data collection rule.

        Lists associations for the specified data collection rule.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param data_collection_rule_name: The name of the data collection rule. The name is case
         insensitive. Required.
        :type data_collection_rule_name: str
        :return: An iterator like instance of either DataCollectionRuleAssociationProxyOnlyResource or
         the result of cls(response)
        :rtype:
         ~azure.core.paging.ItemPaged[~azure.mgmt.monitor.v2022_02_01_preview.models.DataCollectionRuleAssociationProxyOnlyResource]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop(
            "api_version", _params.pop("api-version", self._api_version or "2021-09-01-preview")
        )
        cls: ClsType[_models.DataCollectionRuleAssociationProxyOnlyResourceListResult] = kwargs.pop("cls", None)

        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        def prepare_request(next_link=None):
            if not next_link:

                _request = build_list_by_rule_request(
                    resource_group_name=resource_group_name,
                    data_collection_rule_name=data_collection_rule_name,
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

        def extract_data(pipeline_response):
            deserialized = self._deserialize(
                "DataCollectionRuleAssociationProxyOnlyResourceListResult", pipeline_response
            )
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
                error = self._deserialize.failsafe_deserialize(_models.ErrorResponseCommonV2, pipeline_response)
                raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

            return pipeline_response

        return ItemPaged(get_next, extract_data)

    @distributed_trace
    def list_by_data_collection_endpoint(
        self, resource_group_name: str, data_collection_endpoint_name: str, **kwargs: Any
    ) -> Iterable["_models.DataCollectionRuleAssociationProxyOnlyResource"]:
        """Lists associations for the specified data collection endpoint.

        Lists associations for the specified data collection endpoint.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param data_collection_endpoint_name: The name of the data collection endpoint. The name is
         case insensitive. Required.
        :type data_collection_endpoint_name: str
        :return: An iterator like instance of either DataCollectionRuleAssociationProxyOnlyResource or
         the result of cls(response)
        :rtype:
         ~azure.core.paging.ItemPaged[~azure.mgmt.monitor.v2022_02_01_preview.models.DataCollectionRuleAssociationProxyOnlyResource]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop(
            "api_version", _params.pop("api-version", self._api_version or "2021-09-01-preview")
        )
        cls: ClsType[_models.DataCollectionRuleAssociationProxyOnlyResourceListResult] = kwargs.pop("cls", None)

        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        def prepare_request(next_link=None):
            if not next_link:

                _request = build_list_by_data_collection_endpoint_request(
                    resource_group_name=resource_group_name,
                    data_collection_endpoint_name=data_collection_endpoint_name,
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

        def extract_data(pipeline_response):
            deserialized = self._deserialize(
                "DataCollectionRuleAssociationProxyOnlyResourceListResult", pipeline_response
            )
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
                error = self._deserialize.failsafe_deserialize(_models.ErrorResponseCommonV2, pipeline_response)
                raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

            return pipeline_response

        return ItemPaged(get_next, extract_data)

    @distributed_trace
    def get(
        self, resource_uri: str, association_name: str, **kwargs: Any
    ) -> _models.DataCollectionRuleAssociationProxyOnlyResource:
        """Returns the specified association.

        Returns the specified association.

        :param resource_uri: The identifier of the resource. Required.
        :type resource_uri: str
        :param association_name: The name of the association. The name is case insensitive. Required.
        :type association_name: str
        :return: DataCollectionRuleAssociationProxyOnlyResource or the result of cls(response)
        :rtype:
         ~azure.mgmt.monitor.v2022_02_01_preview.models.DataCollectionRuleAssociationProxyOnlyResource
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
        cls: ClsType[_models.DataCollectionRuleAssociationProxyOnlyResource] = kwargs.pop("cls", None)

        _request = build_get_request(
            resource_uri=resource_uri,
            association_name=association_name,
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
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponseCommonV2, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize("DataCollectionRuleAssociationProxyOnlyResource", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @overload
    def create(
        self,
        resource_uri: str,
        association_name: str,
        body: Optional[_models.DataCollectionRuleAssociationProxyOnlyResource] = None,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.DataCollectionRuleAssociationProxyOnlyResource:
        """Creates or updates an association.

        Creates or updates an association.

        :param resource_uri: The identifier of the resource. Required.
        :type resource_uri: str
        :param association_name: The name of the association. The name is case insensitive. Required.
        :type association_name: str
        :param body: The payload. Default value is None.
        :type body:
         ~azure.mgmt.monitor.v2022_02_01_preview.models.DataCollectionRuleAssociationProxyOnlyResource
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: DataCollectionRuleAssociationProxyOnlyResource or the result of cls(response)
        :rtype:
         ~azure.mgmt.monitor.v2022_02_01_preview.models.DataCollectionRuleAssociationProxyOnlyResource
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    def create(
        self,
        resource_uri: str,
        association_name: str,
        body: Optional[IO[bytes]] = None,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.DataCollectionRuleAssociationProxyOnlyResource:
        """Creates or updates an association.

        Creates or updates an association.

        :param resource_uri: The identifier of the resource. Required.
        :type resource_uri: str
        :param association_name: The name of the association. The name is case insensitive. Required.
        :type association_name: str
        :param body: The payload. Default value is None.
        :type body: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: DataCollectionRuleAssociationProxyOnlyResource or the result of cls(response)
        :rtype:
         ~azure.mgmt.monitor.v2022_02_01_preview.models.DataCollectionRuleAssociationProxyOnlyResource
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace
    def create(
        self,
        resource_uri: str,
        association_name: str,
        body: Optional[Union[_models.DataCollectionRuleAssociationProxyOnlyResource, IO[bytes]]] = None,
        **kwargs: Any
    ) -> _models.DataCollectionRuleAssociationProxyOnlyResource:
        """Creates or updates an association.

        Creates or updates an association.

        :param resource_uri: The identifier of the resource. Required.
        :type resource_uri: str
        :param association_name: The name of the association. The name is case insensitive. Required.
        :type association_name: str
        :param body: The payload. Is either a DataCollectionRuleAssociationProxyOnlyResource type or a
         IO[bytes] type. Default value is None.
        :type body:
         ~azure.mgmt.monitor.v2022_02_01_preview.models.DataCollectionRuleAssociationProxyOnlyResource
         or IO[bytes]
        :return: DataCollectionRuleAssociationProxyOnlyResource or the result of cls(response)
        :rtype:
         ~azure.mgmt.monitor.v2022_02_01_preview.models.DataCollectionRuleAssociationProxyOnlyResource
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
        cls: ClsType[_models.DataCollectionRuleAssociationProxyOnlyResource] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(body, (IOBase, bytes)):
            _content = body
        else:
            if body is not None:
                _json = self._serialize.body(body, "DataCollectionRuleAssociationProxyOnlyResource")
            else:
                _json = None

        _request = build_create_request(
            resource_uri=resource_uri,
            association_name=association_name,
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
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponseCommonV2, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if response.status_code == 200:
            deserialized = self._deserialize("DataCollectionRuleAssociationProxyOnlyResource", pipeline_response)

        if response.status_code == 201:
            deserialized = self._deserialize("DataCollectionRuleAssociationProxyOnlyResource", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @distributed_trace
    def delete(  # pylint: disable=inconsistent-return-statements
        self, resource_uri: str, association_name: str, **kwargs: Any
    ) -> None:
        """Deletes an association.

        Deletes an association.

        :param resource_uri: The identifier of the resource. Required.
        :type resource_uri: str
        :param association_name: The name of the association. The name is case insensitive. Required.
        :type association_name: str
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
            resource_uri=resource_uri,
            association_name=association_name,
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
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponseCommonV2, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})  # type: ignore
