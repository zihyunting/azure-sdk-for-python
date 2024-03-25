# pylint: disable=too-many-lines,too-many-statements
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from io import IOBase
from typing import Any, Callable, Dict, IO, Iterable, Optional, TypeVar, Union, cast, overload

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
from azure.core.polling import LROPoller, NoPolling, PollingMethod
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator import distributed_trace
from azure.core.utils import case_insensitive_dict
from azure.mgmt.core.exceptions import ARMErrorFormat
from azure.mgmt.core.polling.arm_polling import ARMPolling

from .. import models as _models
from .._serialization import Serializer
from .._vendor import _convert_request

T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False


def build_get_request(
    resource_group_name: str,
    workspace_name: str,
    azure_ad_only_authentication_name: Union[str, _models.AzureADOnlyAuthenticationName],
    subscription_id: str,
    **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2021-06-01"))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop(
        "template_url",
        "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Synapse/workspaces/{workspaceName}/azureADOnlyAuthentications/{azureADOnlyAuthenticationName}",
    )  # pylint: disable=line-too-long
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, "str", min_length=1),
        "resourceGroupName": _SERIALIZER.url(
            "resource_group_name", resource_group_name, "str", max_length=90, min_length=1
        ),
        "workspaceName": _SERIALIZER.url("workspace_name", workspace_name, "str"),
        "azureADOnlyAuthenticationName": _SERIALIZER.url(
            "azure_ad_only_authentication_name", azure_ad_only_authentication_name, "str"
        ),
    }

    _url: str = _url.format(**path_format_arguments)  # type: ignore

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, params=_params, headers=_headers, **kwargs)


def build_create_request(
    resource_group_name: str,
    workspace_name: str,
    azure_ad_only_authentication_name: Union[str, _models.AzureADOnlyAuthenticationName],
    subscription_id: str,
    **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2021-06-01"))
    content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop(
        "template_url",
        "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Synapse/workspaces/{workspaceName}/azureADOnlyAuthentications/{azureADOnlyAuthenticationName}",
    )  # pylint: disable=line-too-long
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, "str", min_length=1),
        "resourceGroupName": _SERIALIZER.url(
            "resource_group_name", resource_group_name, "str", max_length=90, min_length=1
        ),
        "workspaceName": _SERIALIZER.url("workspace_name", workspace_name, "str"),
        "azureADOnlyAuthenticationName": _SERIALIZER.url(
            "azure_ad_only_authentication_name", azure_ad_only_authentication_name, "str"
        ),
    }

    _url: str = _url.format(**path_format_arguments)  # type: ignore

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="PUT", url=_url, params=_params, headers=_headers, **kwargs)


def build_list_request(
    resource_group_name: str, workspace_name: str, subscription_id: str, **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2021-06-01"))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop(
        "template_url",
        "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Synapse/workspaces/{workspaceName}/azureADOnlyAuthentications",
    )  # pylint: disable=line-too-long
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, "str", min_length=1),
        "resourceGroupName": _SERIALIZER.url(
            "resource_group_name", resource_group_name, "str", max_length=90, min_length=1
        ),
        "workspaceName": _SERIALIZER.url("workspace_name", workspace_name, "str"),
    }

    _url: str = _url.format(**path_format_arguments)  # type: ignore

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, params=_params, headers=_headers, **kwargs)


class AzureADOnlyAuthenticationsOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.mgmt.synapse.SynapseManagementClient`'s
        :attr:`azure_ad_only_authentications` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs):
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @distributed_trace
    def get(
        self,
        resource_group_name: str,
        workspace_name: str,
        azure_ad_only_authentication_name: Union[str, _models.AzureADOnlyAuthenticationName],
        **kwargs: Any
    ) -> _models.AzureADOnlyAuthentication:
        """Get Azure Active Directory only authentication property.

        Gets a Azure Active Directory only authentication property.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param workspace_name: The name of the workspace. Required.
        :type workspace_name: str
        :param azure_ad_only_authentication_name: name of the property. "default" Required.
        :type azure_ad_only_authentication_name: str or
         ~azure.mgmt.synapse.models.AzureADOnlyAuthenticationName
        :return: AzureADOnlyAuthentication or the result of cls(response)
        :rtype: ~azure.mgmt.synapse.models.AzureADOnlyAuthentication
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

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2021-06-01"))
        cls: ClsType[_models.AzureADOnlyAuthentication] = kwargs.pop("cls", None)

        _request = build_get_request(
            resource_group_name=resource_group_name,
            workspace_name=workspace_name,
            azure_ad_only_authentication_name=azure_ad_only_authentication_name,
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
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize("AzureADOnlyAuthentication", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    def _create_initial(
        self,
        resource_group_name: str,
        workspace_name: str,
        azure_ad_only_authentication_name: Union[str, _models.AzureADOnlyAuthenticationName],
        azure_ad_only_authentication_info: Union[_models.AzureADOnlyAuthentication, IO[bytes]],
        **kwargs: Any
    ) -> Optional[_models.AzureADOnlyAuthentication]:
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2021-06-01"))
        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[Optional[_models.AzureADOnlyAuthentication]] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(azure_ad_only_authentication_info, (IOBase, bytes)):
            _content = azure_ad_only_authentication_info
        else:
            _json = self._serialize.body(azure_ad_only_authentication_info, "AzureADOnlyAuthentication")

        _request = build_create_request(
            resource_group_name=resource_group_name,
            workspace_name=workspace_name,
            azure_ad_only_authentication_name=azure_ad_only_authentication_name,
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

        if response.status_code not in [200, 201, 202]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize("AzureADOnlyAuthentication", pipeline_response)

        if response.status_code == 201:
            deserialized = self._deserialize("AzureADOnlyAuthentication", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @overload
    def begin_create(
        self,
        resource_group_name: str,
        workspace_name: str,
        azure_ad_only_authentication_name: Union[str, _models.AzureADOnlyAuthenticationName],
        azure_ad_only_authentication_info: _models.AzureADOnlyAuthentication,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> LROPoller[_models.AzureADOnlyAuthentication]:
        """Create or Update Azure Active Directory only authentication property.

        Create or Update a Azure Active Directory only authentication property for the workspaces.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param workspace_name: The name of the workspace. Required.
        :type workspace_name: str
        :param azure_ad_only_authentication_name: name of the property. "default" Required.
        :type azure_ad_only_authentication_name: str or
         ~azure.mgmt.synapse.models.AzureADOnlyAuthenticationName
        :param azure_ad_only_authentication_info: Azure Active Directory Property. Required.
        :type azure_ad_only_authentication_info: ~azure.mgmt.synapse.models.AzureADOnlyAuthentication
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of LROPoller that returns either AzureADOnlyAuthentication or the result
         of cls(response)
        :rtype: ~azure.core.polling.LROPoller[~azure.mgmt.synapse.models.AzureADOnlyAuthentication]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    def begin_create(
        self,
        resource_group_name: str,
        workspace_name: str,
        azure_ad_only_authentication_name: Union[str, _models.AzureADOnlyAuthenticationName],
        azure_ad_only_authentication_info: IO[bytes],
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> LROPoller[_models.AzureADOnlyAuthentication]:
        """Create or Update Azure Active Directory only authentication property.

        Create or Update a Azure Active Directory only authentication property for the workspaces.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param workspace_name: The name of the workspace. Required.
        :type workspace_name: str
        :param azure_ad_only_authentication_name: name of the property. "default" Required.
        :type azure_ad_only_authentication_name: str or
         ~azure.mgmt.synapse.models.AzureADOnlyAuthenticationName
        :param azure_ad_only_authentication_info: Azure Active Directory Property. Required.
        :type azure_ad_only_authentication_info: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of LROPoller that returns either AzureADOnlyAuthentication or the result
         of cls(response)
        :rtype: ~azure.core.polling.LROPoller[~azure.mgmt.synapse.models.AzureADOnlyAuthentication]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace
    def begin_create(
        self,
        resource_group_name: str,
        workspace_name: str,
        azure_ad_only_authentication_name: Union[str, _models.AzureADOnlyAuthenticationName],
        azure_ad_only_authentication_info: Union[_models.AzureADOnlyAuthentication, IO[bytes]],
        **kwargs: Any
    ) -> LROPoller[_models.AzureADOnlyAuthentication]:
        """Create or Update Azure Active Directory only authentication property.

        Create or Update a Azure Active Directory only authentication property for the workspaces.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param workspace_name: The name of the workspace. Required.
        :type workspace_name: str
        :param azure_ad_only_authentication_name: name of the property. "default" Required.
        :type azure_ad_only_authentication_name: str or
         ~azure.mgmt.synapse.models.AzureADOnlyAuthenticationName
        :param azure_ad_only_authentication_info: Azure Active Directory Property. Is either a
         AzureADOnlyAuthentication type or a IO[bytes] type. Required.
        :type azure_ad_only_authentication_info: ~azure.mgmt.synapse.models.AzureADOnlyAuthentication
         or IO[bytes]
        :return: An instance of LROPoller that returns either AzureADOnlyAuthentication or the result
         of cls(response)
        :rtype: ~azure.core.polling.LROPoller[~azure.mgmt.synapse.models.AzureADOnlyAuthentication]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2021-06-01"))
        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.AzureADOnlyAuthentication] = kwargs.pop("cls", None)
        polling: Union[bool, PollingMethod] = kwargs.pop("polling", True)
        lro_delay = kwargs.pop("polling_interval", self._config.polling_interval)
        cont_token: Optional[str] = kwargs.pop("continuation_token", None)
        if cont_token is None:
            raw_result = self._create_initial(
                resource_group_name=resource_group_name,
                workspace_name=workspace_name,
                azure_ad_only_authentication_name=azure_ad_only_authentication_name,
                azure_ad_only_authentication_info=azure_ad_only_authentication_info,
                api_version=api_version,
                content_type=content_type,
                cls=lambda x, y, z: x,
                headers=_headers,
                params=_params,
                **kwargs
            )
        kwargs.pop("error_map", None)

        def get_long_running_output(pipeline_response):
            deserialized = self._deserialize("AzureADOnlyAuthentication", pipeline_response)
            if cls:
                return cls(pipeline_response, deserialized, {})  # type: ignore
            return deserialized

        if polling is True:
            polling_method: PollingMethod = cast(
                PollingMethod, ARMPolling(lro_delay, lro_options={"final-state-via": "location"}, **kwargs)
            )
        elif polling is False:
            polling_method = cast(PollingMethod, NoPolling())
        else:
            polling_method = polling
        if cont_token:
            return LROPoller[_models.AzureADOnlyAuthentication].from_continuation_token(
                polling_method=polling_method,
                continuation_token=cont_token,
                client=self._client,
                deserialization_callback=get_long_running_output,
            )
        return LROPoller[_models.AzureADOnlyAuthentication](
            self._client, raw_result, get_long_running_output, polling_method  # type: ignore
        )

    @distributed_trace
    def list(
        self, resource_group_name: str, workspace_name: str, **kwargs: Any
    ) -> Iterable["_models.AzureADOnlyAuthentication"]:
        """Gets a list of Azure Active Directory only authentication property.

        Gets a list of Azure Active Directory only authentication property for a workspace.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param workspace_name: The name of the workspace. Required.
        :type workspace_name: str
        :return: An iterator like instance of either AzureADOnlyAuthentication or the result of
         cls(response)
        :rtype: ~azure.core.paging.ItemPaged[~azure.mgmt.synapse.models.AzureADOnlyAuthentication]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2021-06-01"))
        cls: ClsType[_models.AzureADOnlyAuthenticationListResult] = kwargs.pop("cls", None)

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
            deserialized = self._deserialize("AzureADOnlyAuthenticationListResult", pipeline_response)
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
