# pylint: disable=too-many-lines,too-many-statements
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
from .._vendor import _convert_request

T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False


def build_post_request(subscription_id: str, **kwargs: Any) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2024-03-01-preview"))
    content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop("template_url", "/subscriptions/{subscriptionId}/providers/Microsoft.Help/discoverSolutions")
    path_format_arguments = {
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


class DiscoverySolutionNLPSubscriptionScopeOperations:  # pylint: disable=name-too-long
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.mgmt.selfhelp.SelfHelpMgmtClient`'s
        :attr:`discovery_solution_nlp_subscription_scope` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs):
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @overload
    def post(
        self,
        discover_solution_request: Optional[_models.DiscoveryNlpRequest] = None,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.DiscoveryNlpResponse:
        """Search for relevant Azure diagnostics and solutions using a natural language issue summary and
        subscription.

        :param discover_solution_request: Request body for discovering solutions using NLP. Default
         value is None.
        :type discover_solution_request: ~azure.mgmt.selfhelp.models.DiscoveryNlpRequest
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: DiscoveryNlpResponse or the result of cls(response)
        :rtype: ~azure.mgmt.selfhelp.models.DiscoveryNlpResponse
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    def post(
        self,
        discover_solution_request: Optional[IO[bytes]] = None,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.DiscoveryNlpResponse:
        """Search for relevant Azure diagnostics and solutions using a natural language issue summary and
        subscription.

        :param discover_solution_request: Request body for discovering solutions using NLP. Default
         value is None.
        :type discover_solution_request: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: DiscoveryNlpResponse or the result of cls(response)
        :rtype: ~azure.mgmt.selfhelp.models.DiscoveryNlpResponse
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace
    def post(
        self, discover_solution_request: Optional[Union[_models.DiscoveryNlpRequest, IO[bytes]]] = None, **kwargs: Any
    ) -> _models.DiscoveryNlpResponse:
        """Search for relevant Azure diagnostics and solutions using a natural language issue summary and
        subscription.

        :param discover_solution_request: Request body for discovering solutions using NLP. Is either a
         DiscoveryNlpRequest type or a IO[bytes] type. Default value is None.
        :type discover_solution_request: ~azure.mgmt.selfhelp.models.DiscoveryNlpRequest or IO[bytes]
        :return: DiscoveryNlpResponse or the result of cls(response)
        :rtype: ~azure.mgmt.selfhelp.models.DiscoveryNlpResponse
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

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))
        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.DiscoveryNlpResponse] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(discover_solution_request, (IOBase, bytes)):
            _content = discover_solution_request
        else:
            if discover_solution_request is not None:
                _json = self._serialize.body(discover_solution_request, "DiscoveryNlpRequest")
            else:
                _json = None

        _request = build_post_request(
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

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize("DiscoveryNlpResponse", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore
