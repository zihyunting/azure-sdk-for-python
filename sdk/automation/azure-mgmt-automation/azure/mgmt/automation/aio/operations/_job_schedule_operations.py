# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from io import IOBase
from typing import Any, AsyncIterable, Callable, Dict, IO, Optional, TypeVar, Union, overload

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
from ...operations._job_schedule_operations import (
    build_create_request,
    build_delete_request,
    build_get_request,
    build_list_by_automation_account_request,
)
from .._vendor import AutomationClientMixinABC

T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class JobScheduleOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.mgmt.automation.aio.AutomationClient`'s
        :attr:`job_schedule` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs) -> None:
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @distributed_trace_async
    async def delete(  # pylint: disable=inconsistent-return-statements
        self, resource_group_name: str, automation_account_name: str, job_schedule_id: str, **kwargs: Any
    ) -> None:
        """Delete the job schedule identified by job schedule name.

        .. seealso::
           - http://aka.ms/azureautomationsdk/jobscheduleoperations

        :param resource_group_name: Name of an Azure Resource group. Required.
        :type resource_group_name: str
        :param automation_account_name: The name of the automation account. Required.
        :type automation_account_name: str
        :param job_schedule_id: The job schedule name. Required.
        :type job_schedule_id: str
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

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2023-11-01"))
        cls: ClsType[None] = kwargs.pop("cls", None)

        request = build_delete_request(
            resource_group_name=resource_group_name,
            automation_account_name=automation_account_name,
            job_schedule_id=job_schedule_id,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            template_url=self.delete.metadata["url"],
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

        if cls:
            return cls(pipeline_response, None, {})

    delete.metadata = {
        "url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Automation/automationAccounts/{automationAccountName}/jobSchedules/{jobScheduleId}"
    }

    @distributed_trace_async
    async def get(
        self, resource_group_name: str, automation_account_name: str, job_schedule_id: str, **kwargs: Any
    ) -> _models.JobSchedule:
        """Retrieve the job schedule identified by job schedule name.

        .. seealso::
           - http://aka.ms/azureautomationsdk/jobscheduleoperations

        :param resource_group_name: Name of an Azure Resource group. Required.
        :type resource_group_name: str
        :param automation_account_name: The name of the automation account. Required.
        :type automation_account_name: str
        :param job_schedule_id: The job schedule name. Required.
        :type job_schedule_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: JobSchedule or the result of cls(response)
        :rtype: ~azure.mgmt.automation.models.JobSchedule
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
        cls: ClsType[_models.JobSchedule] = kwargs.pop("cls", None)

        request = build_get_request(
            resource_group_name=resource_group_name,
            automation_account_name=automation_account_name,
            job_schedule_id=job_schedule_id,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            template_url=self.get.metadata["url"],
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

        deserialized = self._deserialize("JobSchedule", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get.metadata = {
        "url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Automation/automationAccounts/{automationAccountName}/jobSchedules/{jobScheduleId}"
    }

    @overload
    async def create(
        self,
        resource_group_name: str,
        automation_account_name: str,
        job_schedule_id: str,
        parameters: _models.JobScheduleCreateParameters,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.JobSchedule:
        """Create a job schedule.

        .. seealso::
           - http://aka.ms/azureautomationsdk/jobscheduleoperations

        :param resource_group_name: Name of an Azure Resource group. Required.
        :type resource_group_name: str
        :param automation_account_name: The name of the automation account. Required.
        :type automation_account_name: str
        :param job_schedule_id: The job schedule name. Required.
        :type job_schedule_id: str
        :param parameters: The parameters supplied to the create job schedule operation. Required.
        :type parameters: ~azure.mgmt.automation.models.JobScheduleCreateParameters
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: JobSchedule or the result of cls(response)
        :rtype: ~azure.mgmt.automation.models.JobSchedule
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def create(
        self,
        resource_group_name: str,
        automation_account_name: str,
        job_schedule_id: str,
        parameters: IO,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.JobSchedule:
        """Create a job schedule.

        .. seealso::
           - http://aka.ms/azureautomationsdk/jobscheduleoperations

        :param resource_group_name: Name of an Azure Resource group. Required.
        :type resource_group_name: str
        :param automation_account_name: The name of the automation account. Required.
        :type automation_account_name: str
        :param job_schedule_id: The job schedule name. Required.
        :type job_schedule_id: str
        :param parameters: The parameters supplied to the create job schedule operation. Required.
        :type parameters: IO
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: JobSchedule or the result of cls(response)
        :rtype: ~azure.mgmt.automation.models.JobSchedule
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def create(
        self,
        resource_group_name: str,
        automation_account_name: str,
        job_schedule_id: str,
        parameters: Union[_models.JobScheduleCreateParameters, IO],
        **kwargs: Any
    ) -> _models.JobSchedule:
        """Create a job schedule.

        .. seealso::
           - http://aka.ms/azureautomationsdk/jobscheduleoperations

        :param resource_group_name: Name of an Azure Resource group. Required.
        :type resource_group_name: str
        :param automation_account_name: The name of the automation account. Required.
        :type automation_account_name: str
        :param job_schedule_id: The job schedule name. Required.
        :type job_schedule_id: str
        :param parameters: The parameters supplied to the create job schedule operation. Is either a
         JobScheduleCreateParameters type or a IO type. Required.
        :type parameters: ~azure.mgmt.automation.models.JobScheduleCreateParameters or IO
        :keyword content_type: Body Parameter content-type. Known values are: 'application/json'.
         Default value is None.
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: JobSchedule or the result of cls(response)
        :rtype: ~azure.mgmt.automation.models.JobSchedule
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

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2023-11-01"))
        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.JobSchedule] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(parameters, (IOBase, bytes)):
            _content = parameters
        else:
            _json = self._serialize.body(parameters, "JobScheduleCreateParameters")

        request = build_create_request(
            resource_group_name=resource_group_name,
            automation_account_name=automation_account_name,
            job_schedule_id=job_schedule_id,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            content=_content,
            template_url=self.create.metadata["url"],
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

        if response.status_code not in [201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize("JobSchedule", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    create.metadata = {
        "url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Automation/automationAccounts/{automationAccountName}/jobSchedules/{jobScheduleId}"
    }

    @distributed_trace
    def list_by_automation_account(
        self, resource_group_name: str, automation_account_name: str, filter: Optional[str] = None, **kwargs: Any
    ) -> AsyncIterable["_models.JobSchedule"]:
        """Retrieve a list of job schedules.

        .. seealso::
           - http://aka.ms/azureautomationsdk/jobscheduleoperations

        :param resource_group_name: Name of an Azure Resource group. Required.
        :type resource_group_name: str
        :param automation_account_name: The name of the automation account. Required.
        :type automation_account_name: str
        :param filter: The filter to apply on the operation. Default value is None.
        :type filter: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either JobSchedule or the result of cls(response)
        :rtype: ~azure.core.async_paging.AsyncItemPaged[~azure.mgmt.automation.models.JobSchedule]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2023-11-01"))
        cls: ClsType[_models.JobScheduleListResult] = kwargs.pop("cls", None)

        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        def prepare_request(next_link=None):
            if not next_link:

                request = build_list_by_automation_account_request(
                    resource_group_name=resource_group_name,
                    automation_account_name=automation_account_name,
                    subscription_id=self._config.subscription_id,
                    filter=filter,
                    api_version=api_version,
                    template_url=self.list_by_automation_account.metadata["url"],
                    headers=_headers,
                    params=_params,
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)

            else:
                request = HttpRequest("GET", next_link)
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)
                request.method = "GET"
            return request

        async def extract_data(pipeline_response):
            deserialized = self._deserialize("JobScheduleListResult", pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)  # type: ignore
            return deserialized.next_link or None, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            request = prepare_request(next_link)

            _stream = False
            pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
                request, stream=_stream, **kwargs
            )
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
                raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

            return pipeline_response

        return AsyncItemPaged(get_next, extract_data)

    list_by_automation_account.metadata = {
        "url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Automation/automationAccounts/{automationAccountName}/jobSchedules"
    }
