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


def build_check_name_availability_request(location: str, subscription_id: str, **kwargs: Any) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2024-05-01"))
    content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop(
        "template_url",
        "/subscriptions/{subscriptionId}/providers/Microsoft.HDInsight/locations/{location}/checkNameAvailability",
    )  # pylint: disable=line-too-long
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, "str"),
        "location": _SERIALIZER.url("location", location, "str", min_length=1),
    }

    _url: str = _url.format(**path_format_arguments)  # type: ignore

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="POST", url=_url, params=_params, headers=_headers, **kwargs)


class LocationsOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.mgmt.hdinsightcontainers.HDInsightContainersMgmtClient`'s
        :attr:`locations` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs):
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @overload
    def check_name_availability(
        self,
        location: str,
        name_availability_parameters: _models.NameAvailabilityParameters,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.NameAvailabilityResult:
        """Check the availability of the resource name.

        :param location: The name of the Azure region. Required.
        :type location: str
        :param name_availability_parameters: The name and type of the resource. Required.
        :type name_availability_parameters:
         ~azure.mgmt.hdinsightcontainers.models.NameAvailabilityParameters
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: NameAvailabilityResult or the result of cls(response)
        :rtype: ~azure.mgmt.hdinsightcontainers.models.NameAvailabilityResult
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    def check_name_availability(
        self,
        location: str,
        name_availability_parameters: IO[bytes],
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.NameAvailabilityResult:
        """Check the availability of the resource name.

        :param location: The name of the Azure region. Required.
        :type location: str
        :param name_availability_parameters: The name and type of the resource. Required.
        :type name_availability_parameters: IO[bytes]
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: NameAvailabilityResult or the result of cls(response)
        :rtype: ~azure.mgmt.hdinsightcontainers.models.NameAvailabilityResult
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace
    def check_name_availability(
        self,
        location: str,
        name_availability_parameters: Union[_models.NameAvailabilityParameters, IO[bytes]],
        **kwargs: Any
    ) -> _models.NameAvailabilityResult:
        """Check the availability of the resource name.

        :param location: The name of the Azure region. Required.
        :type location: str
        :param name_availability_parameters: The name and type of the resource. Is either a
         NameAvailabilityParameters type or a IO[bytes] type. Required.
        :type name_availability_parameters:
         ~azure.mgmt.hdinsightcontainers.models.NameAvailabilityParameters or IO[bytes]
        :return: NameAvailabilityResult or the result of cls(response)
        :rtype: ~azure.mgmt.hdinsightcontainers.models.NameAvailabilityResult
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
        cls: ClsType[_models.NameAvailabilityResult] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(name_availability_parameters, (IOBase, bytes)):
            _content = name_availability_parameters
        else:
            _json = self._serialize.body(name_availability_parameters, "NameAvailabilityParameters")

        _request = build_check_name_availability_request(
            location=location,
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

        deserialized = self._deserialize("NameAvailabilityResult", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore
