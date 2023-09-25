# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from io import IOBase
import sys
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
from ...operations._data_masking_rules_operations import (
    build_create_or_update_request,
    build_get_request,
    build_list_by_sql_pool_request,
)

if sys.version_info >= (3, 8):
    from typing import Literal  # pylint: disable=no-name-in-module, ungrouped-imports
else:
    from typing_extensions import Literal  # type: ignore  # pylint: disable=ungrouped-imports
T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class DataMaskingRulesOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.mgmt.synapse.aio.SynapseManagementClient`'s
        :attr:`data_masking_rules` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs) -> None:
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @overload
    async def create_or_update(
        self,
        resource_group_name: str,
        workspace_name: str,
        sql_pool_name: str,
        data_masking_rule_name: str,
        parameters: _models.DataMaskingRule,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.DataMaskingRule:
        """Creates or updates a Sql pool data masking rule.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param workspace_name: The name of the workspace. Required.
        :type workspace_name: str
        :param sql_pool_name: SQL pool name. Required.
        :type sql_pool_name: str
        :param data_masking_rule_name: The name of the data masking rule. Required.
        :type data_masking_rule_name: str
        :param parameters: The required parameters for creating or updating a data masking rule.
         Required.
        :type parameters: ~azure.mgmt.synapse.models.DataMaskingRule
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword data_masking_policy_name: The name of the data masking policy for which the masking
         rule applies. Default value is "Default". Note that overriding this default value may result in
         unsupported behavior.
        :paramtype data_masking_policy_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: DataMaskingRule or the result of cls(response)
        :rtype: ~azure.mgmt.synapse.models.DataMaskingRule
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def create_or_update(
        self,
        resource_group_name: str,
        workspace_name: str,
        sql_pool_name: str,
        data_masking_rule_name: str,
        parameters: IO,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.DataMaskingRule:
        """Creates or updates a Sql pool data masking rule.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param workspace_name: The name of the workspace. Required.
        :type workspace_name: str
        :param sql_pool_name: SQL pool name. Required.
        :type sql_pool_name: str
        :param data_masking_rule_name: The name of the data masking rule. Required.
        :type data_masking_rule_name: str
        :param parameters: The required parameters for creating or updating a data masking rule.
         Required.
        :type parameters: IO
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword data_masking_policy_name: The name of the data masking policy for which the masking
         rule applies. Default value is "Default". Note that overriding this default value may result in
         unsupported behavior.
        :paramtype data_masking_policy_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: DataMaskingRule or the result of cls(response)
        :rtype: ~azure.mgmt.synapse.models.DataMaskingRule
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def create_or_update(
        self,
        resource_group_name: str,
        workspace_name: str,
        sql_pool_name: str,
        data_masking_rule_name: str,
        parameters: Union[_models.DataMaskingRule, IO],
        **kwargs: Any
    ) -> _models.DataMaskingRule:
        """Creates or updates a Sql pool data masking rule.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param workspace_name: The name of the workspace. Required.
        :type workspace_name: str
        :param sql_pool_name: SQL pool name. Required.
        :type sql_pool_name: str
        :param data_masking_rule_name: The name of the data masking rule. Required.
        :type data_masking_rule_name: str
        :param parameters: The required parameters for creating or updating a data masking rule. Is
         either a DataMaskingRule type or a IO type. Required.
        :type parameters: ~azure.mgmt.synapse.models.DataMaskingRule or IO
        :keyword data_masking_policy_name: The name of the data masking policy for which the masking
         rule applies. Default value is "Default". Note that overriding this default value may result in
         unsupported behavior.
        :paramtype data_masking_policy_name: str
        :keyword content_type: Body Parameter content-type. Known values are: 'application/json'.
         Default value is None.
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: DataMaskingRule or the result of cls(response)
        :rtype: ~azure.mgmt.synapse.models.DataMaskingRule
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

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2021-06-01"))
        data_masking_policy_name: Literal["Default"] = kwargs.pop("data_masking_policy_name", "Default")
        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.DataMaskingRule] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(parameters, (IOBase, bytes)):
            _content = parameters
        else:
            _json = self._serialize.body(parameters, "DataMaskingRule")

        request = build_create_or_update_request(
            resource_group_name=resource_group_name,
            workspace_name=workspace_name,
            sql_pool_name=sql_pool_name,
            data_masking_rule_name=data_masking_rule_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            data_masking_policy_name=data_masking_policy_name,
            content_type=content_type,
            json=_json,
            content=_content,
            template_url=self.create_or_update.metadata["url"],
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
            deserialized = self._deserialize("DataMaskingRule", pipeline_response)

        if response.status_code == 201:
            deserialized = self._deserialize("DataMaskingRule", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    create_or_update.metadata = {
        "url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Synapse/workspaces/{workspaceName}/sqlPools/{sqlPoolName}/dataMaskingPolicies/{dataMaskingPolicyName}/rules/{dataMaskingRuleName}"
    }

    @distributed_trace_async
    async def get(
        self,
        resource_group_name: str,
        workspace_name: str,
        sql_pool_name: str,
        data_masking_rule_name: str,
        **kwargs: Any
    ) -> _models.DataMaskingRule:
        """Gets the specific Sql pool data masking rule.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param workspace_name: The name of the workspace. Required.
        :type workspace_name: str
        :param sql_pool_name: SQL pool name. Required.
        :type sql_pool_name: str
        :param data_masking_rule_name: The name of the data masking rule. Required.
        :type data_masking_rule_name: str
        :keyword data_masking_policy_name: The name of the data masking policy for which the masking
         rule applies. Default value is "Default". Note that overriding this default value may result in
         unsupported behavior.
        :paramtype data_masking_policy_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: DataMaskingRule or the result of cls(response)
        :rtype: ~azure.mgmt.synapse.models.DataMaskingRule
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
        data_masking_policy_name: Literal["Default"] = kwargs.pop("data_masking_policy_name", "Default")
        cls: ClsType[_models.DataMaskingRule] = kwargs.pop("cls", None)

        request = build_get_request(
            resource_group_name=resource_group_name,
            workspace_name=workspace_name,
            sql_pool_name=sql_pool_name,
            data_masking_rule_name=data_masking_rule_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            data_masking_policy_name=data_masking_policy_name,
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

        deserialized = self._deserialize("DataMaskingRule", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get.metadata = {
        "url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Synapse/workspaces/{workspaceName}/sqlPools/{sqlPoolName}/dataMaskingPolicies/{dataMaskingPolicyName}/rules/{dataMaskingRuleName}"
    }

    @distributed_trace
    def list_by_sql_pool(
        self, resource_group_name: str, workspace_name: str, sql_pool_name: str, **kwargs: Any
    ) -> AsyncIterable["_models.DataMaskingRule"]:
        """Gets a list of Sql pool data masking rules.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param workspace_name: The name of the workspace. Required.
        :type workspace_name: str
        :param sql_pool_name: SQL pool name. Required.
        :type sql_pool_name: str
        :keyword data_masking_policy_name: The name of the data masking policy for which the masking
         rule applies. Default value is "Default". Note that overriding this default value may result in
         unsupported behavior.
        :paramtype data_masking_policy_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either DataMaskingRule or the result of cls(response)
        :rtype: ~azure.core.async_paging.AsyncItemPaged[~azure.mgmt.synapse.models.DataMaskingRule]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2021-06-01"))
        data_masking_policy_name: Literal["Default"] = kwargs.pop("data_masking_policy_name", "Default")
        cls: ClsType[_models.DataMaskingRuleListResult] = kwargs.pop("cls", None)

        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        def prepare_request(next_link=None):
            if not next_link:

                request = build_list_by_sql_pool_request(
                    resource_group_name=resource_group_name,
                    workspace_name=workspace_name,
                    sql_pool_name=sql_pool_name,
                    subscription_id=self._config.subscription_id,
                    api_version=api_version,
                    data_masking_policy_name=data_masking_policy_name,
                    template_url=self.list_by_sql_pool.metadata["url"],
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
            deserialized = self._deserialize("DataMaskingRuleListResult", pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)  # type: ignore
            return None, AsyncList(list_of_elem)

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

    list_by_sql_pool.metadata = {
        "url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Synapse/workspaces/{workspaceName}/sqlPools/{sqlPoolName}/dataMaskingPolicies/{dataMaskingPolicyName}/rules"
    }
