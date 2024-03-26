# pylint: disable=too-many-lines,too-many-statements
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from io import IOBase
from typing import Any, Callable, Dict, IO, Optional, TypeVar, Union, cast, overload

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
from azure.core.tracing.decorator_async import distributed_trace_async
from azure.core.utils import case_insensitive_dict
from azure.mgmt.core.exceptions import ARMErrorFormat
from azure.mgmt.core.polling.async_arm_polling import AsyncARMPolling

from ... import models as _models
from ..._vendor import _convert_request
from ...operations._sql_virtual_machine_troubleshoot_operations import build_troubleshoot_request

T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class SqlVirtualMachineTroubleshootOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.mgmt.sqlvirtualmachine.aio.SqlVirtualMachineManagementClient`'s
        :attr:`sql_virtual_machine_troubleshoot` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs) -> None:
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    async def _troubleshoot_initial(
        self,
        resource_group_name: str,
        sql_virtual_machine_name: str,
        parameters: Union[_models.SqlVmTroubleshooting, IO[bytes]],
        **kwargs: Any
    ) -> Optional[_models.SqlVmTroubleshooting]:
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
        cls: ClsType[Optional[_models.SqlVmTroubleshooting]] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(parameters, (IOBase, bytes)):
            _content = parameters
        else:
            _json = self._serialize.body(parameters, "SqlVmTroubleshooting")

        _request = build_troubleshoot_request(
            resource_group_name=resource_group_name,
            sql_virtual_machine_name=sql_virtual_machine_name,
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

        if response.status_code not in [200, 202]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = None
        response_headers = {}
        if response.status_code == 200:
            deserialized = self._deserialize("SqlVmTroubleshooting", pipeline_response)

        if response.status_code == 202:
            response_headers["Location"] = self._deserialize("str", response.headers.get("Location"))

        if cls:
            return cls(pipeline_response, deserialized, response_headers)  # type: ignore

        return deserialized  # type: ignore

    @overload
    async def begin_troubleshoot(
        self,
        resource_group_name: str,
        sql_virtual_machine_name: str,
        parameters: _models.SqlVmTroubleshooting,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> AsyncLROPoller[_models.SqlVmTroubleshooting]:
        """Starts SQL virtual machine troubleshooting.

        :param resource_group_name: Name of the resource group that contains the resource. You can
         obtain this value from the Azure Resource Manager API or the portal. Required.
        :type resource_group_name: str
        :param sql_virtual_machine_name: Name of the SQL virtual machine. Required.
        :type sql_virtual_machine_name: str
        :param parameters: The SQL virtual machine troubleshooting entity. Required.
        :type parameters: ~azure.mgmt.sqlvirtualmachine.models.SqlVmTroubleshooting
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of AsyncLROPoller that returns either SqlVmTroubleshooting or the result
         of cls(response)
        :rtype:
         ~azure.core.polling.AsyncLROPoller[~azure.mgmt.sqlvirtualmachine.models.SqlVmTroubleshooting]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def begin_troubleshoot(
        self,
        resource_group_name: str,
        sql_virtual_machine_name: str,
        parameters: IO[bytes],
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> AsyncLROPoller[_models.SqlVmTroubleshooting]:
        """Starts SQL virtual machine troubleshooting.

        :param resource_group_name: Name of the resource group that contains the resource. You can
         obtain this value from the Azure Resource Manager API or the portal. Required.
        :type resource_group_name: str
        :param sql_virtual_machine_name: Name of the SQL virtual machine. Required.
        :type sql_virtual_machine_name: str
        :param parameters: The SQL virtual machine troubleshooting entity. Required.
        :type parameters: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An instance of AsyncLROPoller that returns either SqlVmTroubleshooting or the result
         of cls(response)
        :rtype:
         ~azure.core.polling.AsyncLROPoller[~azure.mgmt.sqlvirtualmachine.models.SqlVmTroubleshooting]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def begin_troubleshoot(
        self,
        resource_group_name: str,
        sql_virtual_machine_name: str,
        parameters: Union[_models.SqlVmTroubleshooting, IO[bytes]],
        **kwargs: Any
    ) -> AsyncLROPoller[_models.SqlVmTroubleshooting]:
        """Starts SQL virtual machine troubleshooting.

        :param resource_group_name: Name of the resource group that contains the resource. You can
         obtain this value from the Azure Resource Manager API or the portal. Required.
        :type resource_group_name: str
        :param sql_virtual_machine_name: Name of the SQL virtual machine. Required.
        :type sql_virtual_machine_name: str
        :param parameters: The SQL virtual machine troubleshooting entity. Is either a
         SqlVmTroubleshooting type or a IO[bytes] type. Required.
        :type parameters: ~azure.mgmt.sqlvirtualmachine.models.SqlVmTroubleshooting or IO[bytes]
        :return: An instance of AsyncLROPoller that returns either SqlVmTroubleshooting or the result
         of cls(response)
        :rtype:
         ~azure.core.polling.AsyncLROPoller[~azure.mgmt.sqlvirtualmachine.models.SqlVmTroubleshooting]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))
        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.SqlVmTroubleshooting] = kwargs.pop("cls", None)
        polling: Union[bool, AsyncPollingMethod] = kwargs.pop("polling", True)
        lro_delay = kwargs.pop("polling_interval", self._config.polling_interval)
        cont_token: Optional[str] = kwargs.pop("continuation_token", None)
        if cont_token is None:
            raw_result = await self._troubleshoot_initial(
                resource_group_name=resource_group_name,
                sql_virtual_machine_name=sql_virtual_machine_name,
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
            deserialized = self._deserialize("SqlVmTroubleshooting", pipeline_response)
            if cls:
                return cls(pipeline_response, deserialized, {})  # type: ignore
            return deserialized

        if polling is True:
            polling_method: AsyncPollingMethod = cast(
                AsyncPollingMethod, AsyncARMPolling(lro_delay, lro_options={"final-state-via": "location"}, **kwargs)
            )
        elif polling is False:
            polling_method = cast(AsyncPollingMethod, AsyncNoPolling())
        else:
            polling_method = polling
        if cont_token:
            return AsyncLROPoller[_models.SqlVmTroubleshooting].from_continuation_token(
                polling_method=polling_method,
                continuation_token=cont_token,
                client=self._client,
                deserialization_callback=get_long_running_output,
            )
        return AsyncLROPoller[_models.SqlVmTroubleshooting](
            self._client, raw_result, get_long_running_output, polling_method  # type: ignore
        )
