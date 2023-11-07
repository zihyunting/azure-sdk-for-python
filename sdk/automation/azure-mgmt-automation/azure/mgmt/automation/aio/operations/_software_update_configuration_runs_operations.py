# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Callable, Dict, Optional, TypeVar

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
from azure.core.tracing.decorator_async import distributed_trace_async
from azure.core.utils import case_insensitive_dict
from azure.mgmt.core.exceptions import ARMErrorFormat

from ... import models as _models
from ..._vendor import _convert_request
from ...operations._software_update_configuration_runs_operations import build_get_by_id_request, build_list_request
from .._vendor import AutomationClientMixinABC

T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class SoftwareUpdateConfigurationRunsOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.mgmt.automation.aio.AutomationClient`'s
        :attr:`software_update_configuration_runs` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs) -> None:
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @distributed_trace_async
    async def get_by_id(
        self,
        resource_group_name: str,
        automation_account_name: str,
        software_update_configuration_run_id: str,
        client_request_id: Optional[str] = None,
        **kwargs: Any
    ) -> _models.SoftwareUpdateConfigurationRun:
        """Get a single software update configuration Run by Id.

        .. seealso::
           - http://aka.ms/azureautomationsdk/softwareupdateconfigurationrunoperations

        :param resource_group_name: Name of an Azure Resource group. Required.
        :type resource_group_name: str
        :param automation_account_name: The name of the automation account. Required.
        :type automation_account_name: str
        :param software_update_configuration_run_id: The Id of the software update configuration run.
         Required.
        :type software_update_configuration_run_id: str
        :param client_request_id: Identifies this specific client request. Default value is None.
        :type client_request_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: SoftwareUpdateConfigurationRun or the result of cls(response)
        :rtype: ~azure.mgmt.automation.models.SoftwareUpdateConfigurationRun
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

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2023-11-01"))
        cls: ClsType[_models.SoftwareUpdateConfigurationRun] = kwargs.pop("cls", None)

        request = build_get_by_id_request(
            resource_group_name=resource_group_name,
            automation_account_name=automation_account_name,
            software_update_configuration_run_id=software_update_configuration_run_id,
            subscription_id=self._config.subscription_id,
            client_request_id=client_request_id,
            api_version=api_version,
            template_url=self.get_by_id.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize("SoftwareUpdateConfigurationRun", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_by_id.metadata = {
        "url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Automation/automationAccounts/{automationAccountName}/softwareUpdateConfigurationRuns/{softwareUpdateConfigurationRunId}"
    }

    @distributed_trace_async
    async def list(
        self,
        resource_group_name: str,
        automation_account_name: str,
        client_request_id: Optional[str] = None,
        filter: Optional[str] = None,
        skip: Optional[str] = None,
        top: Optional[str] = None,
        **kwargs: Any
    ) -> _models.SoftwareUpdateConfigurationRunListResult:
        """Return list of software update configuration runs.

        .. seealso::
           - http://aka.ms/azureautomationsdk/softwareupdateconfigurationoperations

        :param resource_group_name: Name of an Azure Resource group. Required.
        :type resource_group_name: str
        :param automation_account_name: The name of the automation account. Required.
        :type automation_account_name: str
        :param client_request_id: Identifies this specific client request. Default value is None.
        :type client_request_id: str
        :param filter: The filter to apply on the operation. You can use the following filters:
         'properties/osType', 'properties/status', 'properties/startTime', and
         'properties/softwareUpdateConfiguration/name'. Default value is None.
        :type filter: str
        :param skip: Number of entries you skip before returning results. Default value is None.
        :type skip: str
        :param top: Maximum number of entries returned in the results collection. Default value is
         None.
        :type top: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: SoftwareUpdateConfigurationRunListResult or the result of cls(response)
        :rtype: ~azure.mgmt.automation.models.SoftwareUpdateConfigurationRunListResult
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

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2023-11-01"))
        cls: ClsType[_models.SoftwareUpdateConfigurationRunListResult] = kwargs.pop("cls", None)

        request = build_list_request(
            resource_group_name=resource_group_name,
            automation_account_name=automation_account_name,
            subscription_id=self._config.subscription_id,
            client_request_id=client_request_id,
            filter=filter,
            skip=skip,
            top=top,
            api_version=api_version,
            template_url=self.list.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize("SoftwareUpdateConfigurationRunListResult", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    list.metadata = {
        "url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Automation/automationAccounts/{automationAccountName}/softwareUpdateConfigurationRuns"
    }
