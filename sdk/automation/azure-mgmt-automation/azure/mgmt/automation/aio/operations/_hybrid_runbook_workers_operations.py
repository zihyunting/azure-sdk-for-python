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
from ...operations._hybrid_runbook_workers_operations import (
    build_create_request,
    build_delete_request,
    build_get_request,
    build_list_by_hybrid_runbook_worker_group_request,
    build_move_request,
)
from .._vendor import AutomationClientMixinABC

T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class HybridRunbookWorkersOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.mgmt.automation.aio.AutomationClient`'s
        :attr:`hybrid_runbook_workers` attribute.
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
        self,
        resource_group_name: str,
        automation_account_name: str,
        hybrid_runbook_worker_group_name: str,
        hybrid_runbook_worker_id: str,
        **kwargs: Any
    ) -> None:
        """Delete a hybrid runbook worker.

        .. seealso::
           - http://aka.ms/azureautomationsdk/hybridrunbookworkeroperations

        :param resource_group_name: Name of an Azure Resource group. Required.
        :type resource_group_name: str
        :param automation_account_name: The name of the automation account. Required.
        :type automation_account_name: str
        :param hybrid_runbook_worker_group_name: The hybrid runbook worker group name. Required.
        :type hybrid_runbook_worker_group_name: str
        :param hybrid_runbook_worker_id: The hybrid runbook worker id. Required.
        :type hybrid_runbook_worker_id: str
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
            hybrid_runbook_worker_group_name=hybrid_runbook_worker_group_name,
            hybrid_runbook_worker_id=hybrid_runbook_worker_id,
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

        if response.status_code not in [200, 204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    delete.metadata = {
        "url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Automation/automationAccounts/{automationAccountName}/hybridRunbookWorkerGroups/{hybridRunbookWorkerGroupName}/hybridRunbookWorkers/{hybridRunbookWorkerId}"
    }

    @distributed_trace_async
    async def get(
        self,
        resource_group_name: str,
        automation_account_name: str,
        hybrid_runbook_worker_group_name: str,
        hybrid_runbook_worker_id: str,
        **kwargs: Any
    ) -> _models.HybridRunbookWorker:
        """Retrieve a hybrid runbook worker.

        .. seealso::
           - http://aka.ms/azureautomationsdk/hybridrunbookworkeroperations

        :param resource_group_name: Name of an Azure Resource group. Required.
        :type resource_group_name: str
        :param automation_account_name: The name of the automation account. Required.
        :type automation_account_name: str
        :param hybrid_runbook_worker_group_name: The hybrid runbook worker group name. Required.
        :type hybrid_runbook_worker_group_name: str
        :param hybrid_runbook_worker_id: The hybrid runbook worker id. Required.
        :type hybrid_runbook_worker_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: HybridRunbookWorker or the result of cls(response)
        :rtype: ~azure.mgmt.automation.models.HybridRunbookWorker
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
        cls: ClsType[_models.HybridRunbookWorker] = kwargs.pop("cls", None)

        request = build_get_request(
            resource_group_name=resource_group_name,
            automation_account_name=automation_account_name,
            hybrid_runbook_worker_group_name=hybrid_runbook_worker_group_name,
            hybrid_runbook_worker_id=hybrid_runbook_worker_id,
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

        deserialized = self._deserialize("HybridRunbookWorker", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get.metadata = {
        "url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Automation/automationAccounts/{automationAccountName}/hybridRunbookWorkerGroups/{hybridRunbookWorkerGroupName}/hybridRunbookWorkers/{hybridRunbookWorkerId}"
    }

    @overload
    async def create(
        self,
        resource_group_name: str,
        automation_account_name: str,
        hybrid_runbook_worker_group_name: str,
        hybrid_runbook_worker_id: str,
        hybrid_runbook_worker_creation_parameters: _models.HybridRunbookWorkerCreateParameters,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.HybridRunbookWorker:
        """Create a hybrid runbook worker.

        .. seealso::
           - http://aka.ms/azureautomationsdk/hybridrunbookworkeroperations

        :param resource_group_name: Name of an Azure Resource group. Required.
        :type resource_group_name: str
        :param automation_account_name: The name of the automation account. Required.
        :type automation_account_name: str
        :param hybrid_runbook_worker_group_name: The hybrid runbook worker group name. Required.
        :type hybrid_runbook_worker_group_name: str
        :param hybrid_runbook_worker_id: The hybrid runbook worker id. Required.
        :type hybrid_runbook_worker_id: str
        :param hybrid_runbook_worker_creation_parameters: The create or update parameters for hybrid
         runbook worker. Required.
        :type hybrid_runbook_worker_creation_parameters:
         ~azure.mgmt.automation.models.HybridRunbookWorkerCreateParameters
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: HybridRunbookWorker or the result of cls(response)
        :rtype: ~azure.mgmt.automation.models.HybridRunbookWorker
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def create(
        self,
        resource_group_name: str,
        automation_account_name: str,
        hybrid_runbook_worker_group_name: str,
        hybrid_runbook_worker_id: str,
        hybrid_runbook_worker_creation_parameters: IO,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.HybridRunbookWorker:
        """Create a hybrid runbook worker.

        .. seealso::
           - http://aka.ms/azureautomationsdk/hybridrunbookworkeroperations

        :param resource_group_name: Name of an Azure Resource group. Required.
        :type resource_group_name: str
        :param automation_account_name: The name of the automation account. Required.
        :type automation_account_name: str
        :param hybrid_runbook_worker_group_name: The hybrid runbook worker group name. Required.
        :type hybrid_runbook_worker_group_name: str
        :param hybrid_runbook_worker_id: The hybrid runbook worker id. Required.
        :type hybrid_runbook_worker_id: str
        :param hybrid_runbook_worker_creation_parameters: The create or update parameters for hybrid
         runbook worker. Required.
        :type hybrid_runbook_worker_creation_parameters: IO
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: HybridRunbookWorker or the result of cls(response)
        :rtype: ~azure.mgmt.automation.models.HybridRunbookWorker
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def create(
        self,
        resource_group_name: str,
        automation_account_name: str,
        hybrid_runbook_worker_group_name: str,
        hybrid_runbook_worker_id: str,
        hybrid_runbook_worker_creation_parameters: Union[_models.HybridRunbookWorkerCreateParameters, IO],
        **kwargs: Any
    ) -> _models.HybridRunbookWorker:
        """Create a hybrid runbook worker.

        .. seealso::
           - http://aka.ms/azureautomationsdk/hybridrunbookworkeroperations

        :param resource_group_name: Name of an Azure Resource group. Required.
        :type resource_group_name: str
        :param automation_account_name: The name of the automation account. Required.
        :type automation_account_name: str
        :param hybrid_runbook_worker_group_name: The hybrid runbook worker group name. Required.
        :type hybrid_runbook_worker_group_name: str
        :param hybrid_runbook_worker_id: The hybrid runbook worker id. Required.
        :type hybrid_runbook_worker_id: str
        :param hybrid_runbook_worker_creation_parameters: The create or update parameters for hybrid
         runbook worker. Is either a HybridRunbookWorkerCreateParameters type or a IO type. Required.
        :type hybrid_runbook_worker_creation_parameters:
         ~azure.mgmt.automation.models.HybridRunbookWorkerCreateParameters or IO
        :keyword content_type: Body Parameter content-type. Known values are: 'application/json'.
         Default value is None.
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: HybridRunbookWorker or the result of cls(response)
        :rtype: ~azure.mgmt.automation.models.HybridRunbookWorker
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
        cls: ClsType[_models.HybridRunbookWorker] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(hybrid_runbook_worker_creation_parameters, (IOBase, bytes)):
            _content = hybrid_runbook_worker_creation_parameters
        else:
            _json = self._serialize.body(
                hybrid_runbook_worker_creation_parameters, "HybridRunbookWorkerCreateParameters"
            )

        request = build_create_request(
            resource_group_name=resource_group_name,
            automation_account_name=automation_account_name,
            hybrid_runbook_worker_group_name=hybrid_runbook_worker_group_name,
            hybrid_runbook_worker_id=hybrid_runbook_worker_id,
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

        if response.status_code not in [200, 201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if response.status_code == 200:
            deserialized = self._deserialize("HybridRunbookWorker", pipeline_response)

        if response.status_code == 201:
            deserialized = self._deserialize("HybridRunbookWorker", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    create.metadata = {
        "url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Automation/automationAccounts/{automationAccountName}/hybridRunbookWorkerGroups/{hybridRunbookWorkerGroupName}/hybridRunbookWorkers/{hybridRunbookWorkerId}"
    }

    @overload
    async def move(  # pylint: disable=inconsistent-return-statements
        self,
        resource_group_name: str,
        automation_account_name: str,
        hybrid_runbook_worker_group_name: str,
        hybrid_runbook_worker_id: str,
        hybrid_runbook_worker_move_parameters: _models.HybridRunbookWorkerMoveParameters,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> None:
        """Move a hybrid worker to a different group.

        .. seealso::
           - http://aka.ms/azureautomationsdk/hybridrunbookworkeroperations

        :param resource_group_name: Name of an Azure Resource group. Required.
        :type resource_group_name: str
        :param automation_account_name: The name of the automation account. Required.
        :type automation_account_name: str
        :param hybrid_runbook_worker_group_name: The hybrid runbook worker group name. Required.
        :type hybrid_runbook_worker_group_name: str
        :param hybrid_runbook_worker_id: The hybrid runbook worker id. Required.
        :type hybrid_runbook_worker_id: str
        :param hybrid_runbook_worker_move_parameters: The hybrid runbook worker move parameters.
         Required.
        :type hybrid_runbook_worker_move_parameters:
         ~azure.mgmt.automation.models.HybridRunbookWorkerMoveParameters
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def move(  # pylint: disable=inconsistent-return-statements
        self,
        resource_group_name: str,
        automation_account_name: str,
        hybrid_runbook_worker_group_name: str,
        hybrid_runbook_worker_id: str,
        hybrid_runbook_worker_move_parameters: IO,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> None:
        """Move a hybrid worker to a different group.

        .. seealso::
           - http://aka.ms/azureautomationsdk/hybridrunbookworkeroperations

        :param resource_group_name: Name of an Azure Resource group. Required.
        :type resource_group_name: str
        :param automation_account_name: The name of the automation account. Required.
        :type automation_account_name: str
        :param hybrid_runbook_worker_group_name: The hybrid runbook worker group name. Required.
        :type hybrid_runbook_worker_group_name: str
        :param hybrid_runbook_worker_id: The hybrid runbook worker id. Required.
        :type hybrid_runbook_worker_id: str
        :param hybrid_runbook_worker_move_parameters: The hybrid runbook worker move parameters.
         Required.
        :type hybrid_runbook_worker_move_parameters: IO
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def move(  # pylint: disable=inconsistent-return-statements
        self,
        resource_group_name: str,
        automation_account_name: str,
        hybrid_runbook_worker_group_name: str,
        hybrid_runbook_worker_id: str,
        hybrid_runbook_worker_move_parameters: Union[_models.HybridRunbookWorkerMoveParameters, IO],
        **kwargs: Any
    ) -> None:
        """Move a hybrid worker to a different group.

        .. seealso::
           - http://aka.ms/azureautomationsdk/hybridrunbookworkeroperations

        :param resource_group_name: Name of an Azure Resource group. Required.
        :type resource_group_name: str
        :param automation_account_name: The name of the automation account. Required.
        :type automation_account_name: str
        :param hybrid_runbook_worker_group_name: The hybrid runbook worker group name. Required.
        :type hybrid_runbook_worker_group_name: str
        :param hybrid_runbook_worker_id: The hybrid runbook worker id. Required.
        :type hybrid_runbook_worker_id: str
        :param hybrid_runbook_worker_move_parameters: The hybrid runbook worker move parameters. Is
         either a HybridRunbookWorkerMoveParameters type or a IO type. Required.
        :type hybrid_runbook_worker_move_parameters:
         ~azure.mgmt.automation.models.HybridRunbookWorkerMoveParameters or IO
        :keyword content_type: Body Parameter content-type. Known values are: 'application/json'.
         Default value is None.
        :paramtype content_type: str
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

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2023-11-01"))
        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[None] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(hybrid_runbook_worker_move_parameters, (IOBase, bytes)):
            _content = hybrid_runbook_worker_move_parameters
        else:
            _json = self._serialize.body(hybrid_runbook_worker_move_parameters, "HybridRunbookWorkerMoveParameters")

        request = build_move_request(
            resource_group_name=resource_group_name,
            automation_account_name=automation_account_name,
            hybrid_runbook_worker_group_name=hybrid_runbook_worker_group_name,
            hybrid_runbook_worker_id=hybrid_runbook_worker_id,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            content=_content,
            template_url=self.move.metadata["url"],
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

    move.metadata = {
        "url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Automation/automationAccounts/{automationAccountName}/hybridRunbookWorkerGroups/{hybridRunbookWorkerGroupName}/hybridRunbookWorkers/{hybridRunbookWorkerId}/move"
    }

    @distributed_trace
    def list_by_hybrid_runbook_worker_group(
        self,
        resource_group_name: str,
        automation_account_name: str,
        hybrid_runbook_worker_group_name: str,
        filter: Optional[str] = None,
        **kwargs: Any
    ) -> AsyncIterable["_models.HybridRunbookWorker"]:
        """Retrieve a list of hybrid runbook workers.

        .. seealso::
           - http://aka.ms/azureautomationsdk/hybridrunbookworkeroperations

        :param resource_group_name: Name of an Azure Resource group. Required.
        :type resource_group_name: str
        :param automation_account_name: The name of the automation account. Required.
        :type automation_account_name: str
        :param hybrid_runbook_worker_group_name: The hybrid runbook worker group name. Required.
        :type hybrid_runbook_worker_group_name: str
        :param filter: The filter to apply on the operation. Default value is None.
        :type filter: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either HybridRunbookWorker or the result of cls(response)
        :rtype:
         ~azure.core.async_paging.AsyncItemPaged[~azure.mgmt.automation.models.HybridRunbookWorker]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2023-11-01"))
        cls: ClsType[_models.HybridRunbookWorkersListResult] = kwargs.pop("cls", None)

        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        def prepare_request(next_link=None):
            if not next_link:

                request = build_list_by_hybrid_runbook_worker_group_request(
                    resource_group_name=resource_group_name,
                    automation_account_name=automation_account_name,
                    hybrid_runbook_worker_group_name=hybrid_runbook_worker_group_name,
                    subscription_id=self._config.subscription_id,
                    filter=filter,
                    api_version=api_version,
                    template_url=self.list_by_hybrid_runbook_worker_group.metadata["url"],
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
            deserialized = self._deserialize("HybridRunbookWorkersListResult", pipeline_response)
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

    list_by_hybrid_runbook_worker_group.metadata = {
        "url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Automation/automationAccounts/{automationAccountName}/hybridRunbookWorkerGroups/{hybridRunbookWorkerGroupName}/hybridRunbookWorkers"
    }
