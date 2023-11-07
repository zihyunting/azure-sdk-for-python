# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from io import IOBase
from typing import Any, Callable, Dict, IO, Optional, TypeVar, Union, overload

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
from .._serialization import Serializer
from .._vendor import AutomationClientMixinABC, _convert_request

T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False


def build_convert_graph_runbook_content_request(
    resource_group_name: str, automation_account_name: str, subscription_id: str, **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2023-11-01"))
    content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop(
        "template_url",
        "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Automation/automationAccounts/{automationAccountName}/convertGraphRunbookContent",
    )  # pylint: disable=line-too-long
    path_format_arguments = {
        "resourceGroupName": _SERIALIZER.url(
            "resource_group_name", resource_group_name, "str", max_length=90, min_length=1, pattern=r"^[-\w\._]+$"
        ),
        "automationAccountName": _SERIALIZER.url("automation_account_name", automation_account_name, "str"),
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, "str"),
    }

    _url: str = _url.format(**path_format_arguments)  # type: ignore

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="POST", url=_url, params=_params, headers=_headers, **kwargs)


class AutomationClientOperationsMixin(AutomationClientMixinABC):
    @overload
    def convert_graph_runbook_content(
        self,
        resource_group_name: str,
        automation_account_name: str,
        parameters: _models.GraphicalRunbookContent,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.GraphicalRunbookContent:
        """Post operation to serialize or deserialize GraphRunbookContent.

        :param resource_group_name: Name of an Azure Resource group. Required.
        :type resource_group_name: str
        :param automation_account_name: The name of the automation account. Required.
        :type automation_account_name: str
        :param parameters: Input data describing the graphical runbook. Required.
        :type parameters: ~azure.mgmt.automation.models.GraphicalRunbookContent
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: GraphicalRunbookContent or the result of cls(response)
        :rtype: ~azure.mgmt.automation.models.GraphicalRunbookContent
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    def convert_graph_runbook_content(
        self,
        resource_group_name: str,
        automation_account_name: str,
        parameters: IO,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.GraphicalRunbookContent:
        """Post operation to serialize or deserialize GraphRunbookContent.

        :param resource_group_name: Name of an Azure Resource group. Required.
        :type resource_group_name: str
        :param automation_account_name: The name of the automation account. Required.
        :type automation_account_name: str
        :param parameters: Input data describing the graphical runbook. Required.
        :type parameters: IO
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: GraphicalRunbookContent or the result of cls(response)
        :rtype: ~azure.mgmt.automation.models.GraphicalRunbookContent
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace
    def convert_graph_runbook_content(
        self,
        resource_group_name: str,
        automation_account_name: str,
        parameters: Union[_models.GraphicalRunbookContent, IO],
        **kwargs: Any
    ) -> _models.GraphicalRunbookContent:
        """Post operation to serialize or deserialize GraphRunbookContent.

        :param resource_group_name: Name of an Azure Resource group. Required.
        :type resource_group_name: str
        :param automation_account_name: The name of the automation account. Required.
        :type automation_account_name: str
        :param parameters: Input data describing the graphical runbook. Is either a
         GraphicalRunbookContent type or a IO type. Required.
        :type parameters: ~azure.mgmt.automation.models.GraphicalRunbookContent or IO
        :keyword content_type: Body Parameter content-type. Known values are: 'application/json'.
         Default value is None.
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: GraphicalRunbookContent or the result of cls(response)
        :rtype: ~azure.mgmt.automation.models.GraphicalRunbookContent
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
        cls: ClsType[_models.GraphicalRunbookContent] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(parameters, (IOBase, bytes)):
            _content = parameters
        else:
            _json = self._serialize.body(parameters, "GraphicalRunbookContent")

        request = build_convert_graph_runbook_content_request(
            resource_group_name=resource_group_name,
            automation_account_name=automation_account_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            content=_content,
            template_url=self.convert_graph_runbook_content.metadata["url"],
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
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize("GraphicalRunbookContent", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    convert_graph_runbook_content.metadata = {
        "url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Automation/automationAccounts/{automationAccountName}/convertGraphRunbookContent"
    }
