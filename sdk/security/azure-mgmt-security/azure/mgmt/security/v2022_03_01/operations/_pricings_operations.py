# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import sys
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
from ..._serialization import Serializer
from .._vendor import _convert_request, _format_url_section

if sys.version_info >= (3, 8):
    from typing import Literal  # pylint: disable=no-name-in-module, ungrouped-imports
else:
    from typing_extensions import Literal  # type: ignore  # pylint: disable=ungrouped-imports
T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False


def build_list_request(subscription_id: str, **kwargs: Any) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version: Literal["2022-03-01"] = kwargs.pop("api_version", _params.pop("api-version", "2022-03-01"))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop("template_url", "/subscriptions/{subscriptionId}/providers/Microsoft.Security/pricings")
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url(
            "subscription_id", subscription_id, "str", pattern=r"^[0-9A-Fa-f]{8}-([0-9A-Fa-f]{4}-){3}[0-9A-Fa-f]{12}$"
        ),
    }

    _url: str = _format_url_section(_url, **path_format_arguments)  # type: ignore

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, params=_params, headers=_headers, **kwargs)


def build_get_request(pricing_name: str, subscription_id: str, **kwargs: Any) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version: Literal["2022-03-01"] = kwargs.pop("api_version", _params.pop("api-version", "2022-03-01"))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop(
        "template_url", "/subscriptions/{subscriptionId}/providers/Microsoft.Security/pricings/{pricingName}"
    )
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url(
            "subscription_id", subscription_id, "str", pattern=r"^[0-9A-Fa-f]{8}-([0-9A-Fa-f]{4}-){3}[0-9A-Fa-f]{12}$"
        ),
        "pricingName": _SERIALIZER.url("pricing_name", pricing_name, "str"),
    }

    _url: str = _format_url_section(_url, **path_format_arguments)  # type: ignore

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, params=_params, headers=_headers, **kwargs)


def build_update_request(pricing_name: str, subscription_id: str, **kwargs: Any) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version: Literal["2022-03-01"] = kwargs.pop("api_version", _params.pop("api-version", "2022-03-01"))
    content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop(
        "template_url", "/subscriptions/{subscriptionId}/providers/Microsoft.Security/pricings/{pricingName}"
    )
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url(
            "subscription_id", subscription_id, "str", pattern=r"^[0-9A-Fa-f]{8}-([0-9A-Fa-f]{4}-){3}[0-9A-Fa-f]{12}$"
        ),
        "pricingName": _SERIALIZER.url("pricing_name", pricing_name, "str"),
    }

    _url: str = _format_url_section(_url, **path_format_arguments)  # type: ignore

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="PUT", url=_url, params=_params, headers=_headers, **kwargs)


class PricingsOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.mgmt.security.v2022_03_01.SecurityCenter`'s
        :attr:`pricings` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs):
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @distributed_trace
    def list(self, **kwargs: Any) -> _models.PricingList:
        """Lists Microsoft Defender for Cloud pricing configurations in the subscription.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: PricingList or the result of cls(response)
        :rtype: ~azure.mgmt.security.v2022_03_01.models.PricingList
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

        api_version: Literal["2022-03-01"] = kwargs.pop("api_version", _params.pop("api-version", "2022-03-01"))
        cls: ClsType[_models.PricingList] = kwargs.pop("cls", None)

        request = build_list_request(
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            template_url=self.list.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize("PricingList", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    list.metadata = {"url": "/subscriptions/{subscriptionId}/providers/Microsoft.Security/pricings"}

    @distributed_trace
    def get(self, pricing_name: str, **kwargs: Any) -> _models.Pricing:
        """Gets a provided Microsoft Defender for Cloud pricing configuration in the subscription.

        :param pricing_name: name of the pricing configuration. Required.
        :type pricing_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: Pricing or the result of cls(response)
        :rtype: ~azure.mgmt.security.v2022_03_01.models.Pricing
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

        api_version: Literal["2022-03-01"] = kwargs.pop("api_version", _params.pop("api-version", "2022-03-01"))
        cls: ClsType[_models.Pricing] = kwargs.pop("cls", None)

        request = build_get_request(
            pricing_name=pricing_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            template_url=self.get.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize("Pricing", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get.metadata = {"url": "/subscriptions/{subscriptionId}/providers/Microsoft.Security/pricings/{pricingName}"}

    @overload
    def update(
        self, pricing_name: str, pricing: _models.Pricing, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.Pricing:
        """Updates a provided Microsoft Defender for Cloud pricing configuration in the subscription.

        :param pricing_name: name of the pricing configuration. Required.
        :type pricing_name: str
        :param pricing: Pricing object. Required.
        :type pricing: ~azure.mgmt.security.v2022_03_01.models.Pricing
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: Pricing or the result of cls(response)
        :rtype: ~azure.mgmt.security.v2022_03_01.models.Pricing
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    def update(
        self, pricing_name: str, pricing: IO, *, content_type: str = "application/json", **kwargs: Any
    ) -> _models.Pricing:
        """Updates a provided Microsoft Defender for Cloud pricing configuration in the subscription.

        :param pricing_name: name of the pricing configuration. Required.
        :type pricing_name: str
        :param pricing: Pricing object. Required.
        :type pricing: IO
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: Pricing or the result of cls(response)
        :rtype: ~azure.mgmt.security.v2022_03_01.models.Pricing
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace
    def update(self, pricing_name: str, pricing: Union[_models.Pricing, IO], **kwargs: Any) -> _models.Pricing:
        """Updates a provided Microsoft Defender for Cloud pricing configuration in the subscription.

        :param pricing_name: name of the pricing configuration. Required.
        :type pricing_name: str
        :param pricing: Pricing object. Is either a model type or a IO type. Required.
        :type pricing: ~azure.mgmt.security.v2022_03_01.models.Pricing or IO
        :keyword content_type: Body Parameter content-type. Known values are: 'application/json'.
         Default value is None.
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: Pricing or the result of cls(response)
        :rtype: ~azure.mgmt.security.v2022_03_01.models.Pricing
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

        api_version: Literal["2022-03-01"] = kwargs.pop("api_version", _params.pop("api-version", "2022-03-01"))
        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.Pricing] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(pricing, (IO, bytes)):
            _content = pricing
        else:
            _json = self._serialize.body(pricing, "Pricing")

        request = build_update_request(
            pricing_name=pricing_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            content=_content,
            template_url=self.update.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize("Pricing", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    update.metadata = {"url": "/subscriptions/{subscriptionId}/providers/Microsoft.Security/pricings/{pricingName}"}
