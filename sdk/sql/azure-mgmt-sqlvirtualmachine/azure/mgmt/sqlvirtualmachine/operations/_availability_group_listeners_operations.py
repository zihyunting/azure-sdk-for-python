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
    sql_virtual_machine_group_name: str,
    availability_group_listener_name: str,
    subscription_id: str,
    *,
    expand: Optional[str] = None,
    **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2023-10-01"))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop(
        "template_url",
        "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.SqlVirtualMachine/sqlVirtualMachineGroups/{sqlVirtualMachineGroupName}/availabilityGroupListeners/{availabilityGroupListenerName}",
    )  # pylint: disable=line-too-long
    path_format_arguments = {
        "resourceGroupName": _SERIALIZER.url("resource_group_name", resource_group_name, "str"),
        "sqlVirtualMachineGroupName": _SERIALIZER.url(
            "sql_virtual_machine_group_name", sql_virtual_machine_group_name, "str"
        ),
        "availabilityGroupListenerName": _SERIALIZER.url(
            "availability_group_listener_name", availability_group_listener_name, "str"
        ),
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, "str"),
    }

    _url: str = _url.format(**path_format_arguments)  # type: ignore

    # Construct parameters
    if expand is not None:
        _params["$expand"] = _SERIALIZER.query("expand", expand, "str")
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, params=_params, headers=_headers, **kwargs)


def build_create_or_update_request(
    resource_group_name: str,
    sql_virtual_machine_group_name: str,
    availability_group_listener_name: str,
    subscription_id: str,
    **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2023-10-01"))
    content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop(
        "template_url",
        "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.SqlVirtualMachine/sqlVirtualMachineGroups/{sqlVirtualMachineGroupName}/availabilityGroupListeners/{availabilityGroupListenerName}",
    )  # pylint: disable=line-too-long
    path_format_arguments = {
        "resourceGroupName": _SERIALIZER.url("resource_group_name", resource_group_name, "str"),
        "sqlVirtualMachineGroupName": _SERIALIZER.url(
            "sql_virtual_machine_group_name", sql_virtual_machine_group_name, "str"
        ),
        "availabilityGroupListenerName": _SERIALIZER.url(
            "availability_group_listener_name", availability_group_listener_name, "str"
        ),
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, "str"),
    }

    _url: str = _url.format(**path_format_arguments)  # type: ignore

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="PUT", url=_url, params=_params, headers=_headers, **kwargs)


def build_delete_request(
    resource_group_name: str,
    sql_virtual_machine_group_name: str,
    availability_group_listener_name: str,
    subscription_id: str,
    **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2023-10-01"))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop(
        "template_url",
        "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.SqlVirtualMachine/sqlVirtualMachineGroups/{sqlVirtualMachineGroupName}/availabilityGroupListeners/{availabilityGroupListenerName}",
    )  # pylint: disable=line-too-long
    path_format_arguments = {
        "resourceGroupName": _SERIALIZER.url("resource_group_name", resource_group_name, "str"),
        "sqlVirtualMachineGroupName": _SERIALIZER.url(
            "sql_virtual_machine_group_name", sql_virtual_machine_group_name, "str"
        ),
        "availabilityGroupListenerName": _SERIALIZER.url(
            "availability_group_listener_name", availability_group_listener_name, "str"
        ),
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, "str"),
    }

    _url: str = _url.format(**path_format_arguments)  # type: ignore

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="DELETE", url=_url, params=_params, headers=_headers, **kwargs)


def build_list_by_group_request(
    resource_group_name: str, sql_virtual_machine_group_name: str, subscription_id: str, **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2023-10-01"))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop(
        "template_url",
        "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.SqlVirtualMachine/sqlVirtualMachineGroups/{sqlVirtualMachineGroupName}/availabilityGroupListeners",
    )  # pylint: disable=line-too-long
    path_format_arguments = {
        "resourceGroupName": _SERIALIZER.url("resource_group_name", resource_group_name, "str"),
        "sqlVirtualMachineGroupName": _SERIALIZER.url(
            "sql_virtual_machine_group_name", sql_virtual_machine_group_name, "str"
        ),
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, "str"),
    }

    _url: str = _url.format(**path_format_arguments)  # type: ignore

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, params=_params, headers=_headers, **kwargs)


class AvailabilityGroupListenersOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.mgmt.sqlvirtualmachine.SqlVirtualMachineManagementClient`'s
        :attr:`availability_group_listeners` attribute.
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
        sql_virtual_machine_group_name: str,
        availability_group_listener_name: str,
        expand: Optional[str] = None,
        **kwargs: Any
    ) -> _models.AvailabilityGroupListener:
        """Gets an availability group listener.

        :param resource_group_name: Name of the resource group that contains the resource. You can
         obtain this value from the Azure Resource Manager API or the portal. Required.
        :type resource_group_name: str
        :param sql_virtual_machine_group_name: Name of the SQL virtual machine group. Required.
        :type sql_virtual_machine_group_name: str
        :param availability_group_listener_name: Name of the availability group listener. Required.
        :type availability_group_listener_name: str
        :param expand: The child resources to include in the response. Default value is None.
        :type expand: str
        :return: AvailabilityGroupListener or the result of cls(response)
        :rtype: ~azure.mgmt.sqlvirtualmachine.models.AvailabilityGroupListener
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
        cls: ClsType[_models.AvailabilityGroupListener] = kwargs.pop("cls", None)

        _request = build_get_request(
            resource_group_name=resource_group_name,
            sql_virtual_machine_group_name=sql_virtual_machine_group_name,
            availability_group_listener_name=availability_group_listener_name,
            subscription_id=self._config.subscription_id,
            expand=expand,
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

        deserialized = self._deserialize("AvailabilityGroupListener", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    def _create_or_update_initial(
        self,
        resource_group_name: str,
        sql_virtual_machine_group_name: str,
        availability_group_listener_name: str,
        parameters: Union[_models.AvailabilityGroupListener, IO[bytes]],
        **kwargs: Any
    ) -> _models.AvailabilityGroupListener:
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
        cls: ClsType[_models.AvailabilityGroupListener] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(parameters, (IOBase, bytes)):
            _content = parameters
        else:
            _json = self._serialize.body(parameters, "AvailabilityGroupListener")

        _request = build_create_or_update_request(
            resource_group_name=resource_group_name,
            sql_virtual_machine_group_name=sql_virtual_machine_group_name,
            availability_group_listener_name=availability_group_listener_name,
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
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if response.status_code == 200:
            deserialized = self._deserialize("AvailabilityGroupListener", pipeline_response)

        if response.status_code == 201:
            deserialized = self._deserialize("AvailabilityGroupListener", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @overload
    def begin_create_or_update(
        self,
        resource_group_name: str,
        sql_virtual_machine_group_name: str,
        availability_group_listener_name: str,
        parameters: _models.AvailabilityGroupListener,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> LROPoller[_models.AvailabilityGroupListener]:
        """Creates or updates an availability group listener.

        :param resource_group_name: Name of the resource group that contains the resource. You can
         obtain this value from the Azure Resource Manager API or the portal. Required.
        :type resource_group_name: str
        :param sql_virtual_machine_group_name: Name of the SQL virtual machine group. Required.
        :type sql_virtual_machine_group_name: str
        :param availability_group_listener_name: Name of the availability group listener. Required.
        :type availability_group_listener_name: str
        :param parameters: The availability group listener. Required.
        :type parameters: ~azure.mgmt.sqlvirtualmachine.models.AvailabilityGroupListener
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of LROPoller that returns either AvailabilityGroupListener or the result
         of cls(response)
        :rtype:
         ~azure.core.polling.LROPoller[~azure.mgmt.sqlvirtualmachine.models.AvailabilityGroupListener]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    def begin_create_or_update(
        self,
        resource_group_name: str,
        sql_virtual_machine_group_name: str,
        availability_group_listener_name: str,
        parameters: IO[bytes],
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> LROPoller[_models.AvailabilityGroupListener]:
        """Creates or updates an availability group listener.

        :param resource_group_name: Name of the resource group that contains the resource. You can
         obtain this value from the Azure Resource Manager API or the portal. Required.
        :type resource_group_name: str
        :param sql_virtual_machine_group_name: Name of the SQL virtual machine group. Required.
        :type sql_virtual_machine_group_name: str
        :param availability_group_listener_name: Name of the availability group listener. Required.
        :type availability_group_listener_name: str
        :param parameters: The availability group listener. Required.
        :type parameters: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of LROPoller that returns either AvailabilityGroupListener or the result
         of cls(response)
        :rtype:
         ~azure.core.polling.LROPoller[~azure.mgmt.sqlvirtualmachine.models.AvailabilityGroupListener]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace
    def begin_create_or_update(
        self,
        resource_group_name: str,
        sql_virtual_machine_group_name: str,
        availability_group_listener_name: str,
        parameters: Union[_models.AvailabilityGroupListener, IO[bytes]],
        **kwargs: Any
    ) -> LROPoller[_models.AvailabilityGroupListener]:
        """Creates or updates an availability group listener.

        :param resource_group_name: Name of the resource group that contains the resource. You can
         obtain this value from the Azure Resource Manager API or the portal. Required.
        :type resource_group_name: str
        :param sql_virtual_machine_group_name: Name of the SQL virtual machine group. Required.
        :type sql_virtual_machine_group_name: str
        :param availability_group_listener_name: Name of the availability group listener. Required.
        :type availability_group_listener_name: str
        :param parameters: The availability group listener. Is either a AvailabilityGroupListener type
         or a IO[bytes] type. Required.
        :type parameters: ~azure.mgmt.sqlvirtualmachine.models.AvailabilityGroupListener or IO[bytes]
        :return: An instance of LROPoller that returns either AvailabilityGroupListener or the result
         of cls(response)
        :rtype:
         ~azure.core.polling.LROPoller[~azure.mgmt.sqlvirtualmachine.models.AvailabilityGroupListener]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))
        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.AvailabilityGroupListener] = kwargs.pop("cls", None)
        polling: Union[bool, PollingMethod] = kwargs.pop("polling", True)
        lro_delay = kwargs.pop("polling_interval", self._config.polling_interval)
        cont_token: Optional[str] = kwargs.pop("continuation_token", None)
        if cont_token is None:
            raw_result = self._create_or_update_initial(
                resource_group_name=resource_group_name,
                sql_virtual_machine_group_name=sql_virtual_machine_group_name,
                availability_group_listener_name=availability_group_listener_name,
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
            deserialized = self._deserialize("AvailabilityGroupListener", pipeline_response)
            if cls:
                return cls(pipeline_response, deserialized, {})  # type: ignore
            return deserialized

        if polling is True:
            polling_method: PollingMethod = cast(
                PollingMethod, ARMPolling(lro_delay, lro_options={"final-state-via": "azure-async-operation"}, **kwargs)
            )
        elif polling is False:
            polling_method = cast(PollingMethod, NoPolling())
        else:
            polling_method = polling
        if cont_token:
            return LROPoller[_models.AvailabilityGroupListener].from_continuation_token(
                polling_method=polling_method,
                continuation_token=cont_token,
                client=self._client,
                deserialization_callback=get_long_running_output,
            )
        return LROPoller[_models.AvailabilityGroupListener](
            self._client, raw_result, get_long_running_output, polling_method  # type: ignore
        )

    def _delete_initial(  # pylint: disable=inconsistent-return-statements
        self,
        resource_group_name: str,
        sql_virtual_machine_group_name: str,
        availability_group_listener_name: str,
        **kwargs: Any
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

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))
        cls: ClsType[None] = kwargs.pop("cls", None)

        _request = build_delete_request(
            resource_group_name=resource_group_name,
            sql_virtual_machine_group_name=sql_virtual_machine_group_name,
            availability_group_listener_name=availability_group_listener_name,
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

        if response.status_code not in [200, 202, 204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        response_headers = {}
        if response.status_code == 202:
            response_headers["Location"] = self._deserialize("str", response.headers.get("Location"))

        if cls:
            return cls(pipeline_response, None, response_headers)  # type: ignore

    @distributed_trace
    def begin_delete(
        self,
        resource_group_name: str,
        sql_virtual_machine_group_name: str,
        availability_group_listener_name: str,
        **kwargs: Any
    ) -> LROPoller[None]:
        """Deletes an availability group listener.

        :param resource_group_name: Name of the resource group that contains the resource. You can
         obtain this value from the Azure Resource Manager API or the portal. Required.
        :type resource_group_name: str
        :param sql_virtual_machine_group_name: Name of the SQL virtual machine group. Required.
        :type sql_virtual_machine_group_name: str
        :param availability_group_listener_name: Name of the availability group listener. Required.
        :type availability_group_listener_name: str
        :return: An instance of LROPoller that returns either None or the result of cls(response)
        :rtype: ~azure.core.polling.LROPoller[None]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))
        cls: ClsType[None] = kwargs.pop("cls", None)
        polling: Union[bool, PollingMethod] = kwargs.pop("polling", True)
        lro_delay = kwargs.pop("polling_interval", self._config.polling_interval)
        cont_token: Optional[str] = kwargs.pop("continuation_token", None)
        if cont_token is None:
            raw_result = self._delete_initial(  # type: ignore
                resource_group_name=resource_group_name,
                sql_virtual_machine_group_name=sql_virtual_machine_group_name,
                availability_group_listener_name=availability_group_listener_name,
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
            polling_method: PollingMethod = cast(
                PollingMethod, ARMPolling(lro_delay, lro_options={"final-state-via": "location"}, **kwargs)
            )
        elif polling is False:
            polling_method = cast(PollingMethod, NoPolling())
        else:
            polling_method = polling
        if cont_token:
            return LROPoller[None].from_continuation_token(
                polling_method=polling_method,
                continuation_token=cont_token,
                client=self._client,
                deserialization_callback=get_long_running_output,
            )
        return LROPoller[None](self._client, raw_result, get_long_running_output, polling_method)  # type: ignore

    @distributed_trace
    def list_by_group(
        self, resource_group_name: str, sql_virtual_machine_group_name: str, **kwargs: Any
    ) -> Iterable["_models.AvailabilityGroupListener"]:
        """Lists all availability group listeners in a SQL virtual machine group.

        :param resource_group_name: Name of the resource group that contains the resource. You can
         obtain this value from the Azure Resource Manager API or the portal. Required.
        :type resource_group_name: str
        :param sql_virtual_machine_group_name: Name of the SQL virtual machine group. Required.
        :type sql_virtual_machine_group_name: str
        :return: An iterator like instance of either AvailabilityGroupListener or the result of
         cls(response)
        :rtype:
         ~azure.core.paging.ItemPaged[~azure.mgmt.sqlvirtualmachine.models.AvailabilityGroupListener]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))
        cls: ClsType[_models.AvailabilityGroupListenerListResult] = kwargs.pop("cls", None)

        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        def prepare_request(next_link=None):
            if not next_link:

                _request = build_list_by_group_request(
                    resource_group_name=resource_group_name,
                    sql_virtual_machine_group_name=sql_virtual_machine_group_name,
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
                _next_request_params["api-version"] = self._config.api_version
                _request = HttpRequest(
                    "GET", urllib.parse.urljoin(next_link, _parsed_next_link.path), params=_next_request_params
                )
                _request = _convert_request(_request)
                _request.url = self._client.format_url(_request.url)
                _request.method = "GET"
            return _request

        def extract_data(pipeline_response):
            deserialized = self._deserialize("AvailabilityGroupListenerListResult", pipeline_response)
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
