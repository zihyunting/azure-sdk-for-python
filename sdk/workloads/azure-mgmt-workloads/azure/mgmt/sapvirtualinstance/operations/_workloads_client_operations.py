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
from .._vendor import WorkloadsClientMixinABC, _convert_request

T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False


def build_sap_sizing_recommendations_request(location: str, subscription_id: str, **kwargs: Any) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2023-10-01-preview"))
    content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop(
        "template_url",
        "/subscriptions/{subscriptionId}/providers/Microsoft.Workloads/locations/{location}/sapVirtualInstanceMetadata/default/getSizingRecommendations",
    )  # pylint: disable=line-too-long
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, "str", min_length=1),
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


def build_sap_supported_sku_request(location: str, subscription_id: str, **kwargs: Any) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2023-10-01-preview"))
    content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop(
        "template_url",
        "/subscriptions/{subscriptionId}/providers/Microsoft.Workloads/locations/{location}/sapVirtualInstanceMetadata/default/getSapSupportedSku",
    )  # pylint: disable=line-too-long
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, "str", min_length=1),
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


def build_sap_disk_configurations_request(location: str, subscription_id: str, **kwargs: Any) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2023-10-01-preview"))
    content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop(
        "template_url",
        "/subscriptions/{subscriptionId}/providers/Microsoft.Workloads/locations/{location}/sapVirtualInstanceMetadata/default/getDiskConfigurations",
    )  # pylint: disable=line-too-long
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, "str", min_length=1),
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


def build_sap_availability_zone_details_request(location: str, subscription_id: str, **kwargs: Any) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2023-10-01-preview"))
    content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop(
        "template_url",
        "/subscriptions/{subscriptionId}/providers/Microsoft.Workloads/locations/{location}/sapVirtualInstanceMetadata/default/getAvailabilityZoneDetails",
    )  # pylint: disable=line-too-long
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, "str", min_length=1),
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


class WorkloadsClientOperationsMixin(WorkloadsClientMixinABC):
    @overload
    def sap_sizing_recommendations(
        self,
        location: str,
        sap_sizing_recommendation: Optional[_models.SAPSizingRecommendationRequest] = None,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.SAPSizingRecommendationResult:
        """Get SAP sizing recommendations by providing input SAPS for application tier and memory required
        for database tier.

        :param location: The name of Azure region. Required.
        :type location: str
        :param sap_sizing_recommendation: SAP Sizing Recommendation Request body. Default value is
         None.
        :type sap_sizing_recommendation:
         ~azure.mgmt.workloads.sapvirtualinstance.models.SAPSizingRecommendationRequest
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: SAPSizingRecommendationResult or the result of cls(response)
        :rtype: ~azure.mgmt.workloads.sapvirtualinstance.models.SAPSizingRecommendationResult
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    def sap_sizing_recommendations(
        self,
        location: str,
        sap_sizing_recommendation: Optional[IO] = None,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.SAPSizingRecommendationResult:
        """Get SAP sizing recommendations by providing input SAPS for application tier and memory required
        for database tier.

        :param location: The name of Azure region. Required.
        :type location: str
        :param sap_sizing_recommendation: SAP Sizing Recommendation Request body. Default value is
         None.
        :type sap_sizing_recommendation: IO
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: SAPSizingRecommendationResult or the result of cls(response)
        :rtype: ~azure.mgmt.workloads.sapvirtualinstance.models.SAPSizingRecommendationResult
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace
    def sap_sizing_recommendations(
        self,
        location: str,
        sap_sizing_recommendation: Optional[Union[_models.SAPSizingRecommendationRequest, IO]] = None,
        **kwargs: Any
    ) -> _models.SAPSizingRecommendationResult:
        """Get SAP sizing recommendations by providing input SAPS for application tier and memory required
        for database tier.

        :param location: The name of Azure region. Required.
        :type location: str
        :param sap_sizing_recommendation: SAP Sizing Recommendation Request body. Is either a
         SAPSizingRecommendationRequest type or a IO type. Default value is None.
        :type sap_sizing_recommendation:
         ~azure.mgmt.workloads.sapvirtualinstance.models.SAPSizingRecommendationRequest or IO
        :keyword content_type: Body Parameter content-type. Known values are: 'application/json'.
         Default value is None.
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: SAPSizingRecommendationResult or the result of cls(response)
        :rtype: ~azure.mgmt.workloads.sapvirtualinstance.models.SAPSizingRecommendationResult
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
        cls: ClsType[_models.SAPSizingRecommendationResult] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(sap_sizing_recommendation, (IOBase, bytes)):
            _content = sap_sizing_recommendation
        else:
            if sap_sizing_recommendation is not None:
                _json = self._serialize.body(sap_sizing_recommendation, "SAPSizingRecommendationRequest")
            else:
                _json = None

        request = build_sap_sizing_recommendations_request(
            location=location,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            content=_content,
            template_url=self.sap_sizing_recommendations.metadata["url"],
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

        deserialized = self._deserialize("SAPSizingRecommendationResult", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    sap_sizing_recommendations.metadata = {
        "url": "/subscriptions/{subscriptionId}/providers/Microsoft.Workloads/locations/{location}/sapVirtualInstanceMetadata/default/getSizingRecommendations"
    }

    @overload
    def sap_supported_sku(
        self,
        location: str,
        sap_supported_sku: Optional[_models.SAPSupportedSkusRequest] = None,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.SAPSupportedResourceSkusResult:
        """Get a list of SAP supported SKUs for ASCS, Application and Database tier.

        :param location: The name of Azure region. Required.
        :type location: str
        :param sap_supported_sku: SAP Supported SKU Request body. Default value is None.
        :type sap_supported_sku:
         ~azure.mgmt.workloads.sapvirtualinstance.models.SAPSupportedSkusRequest
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: SAPSupportedResourceSkusResult or the result of cls(response)
        :rtype: ~azure.mgmt.workloads.sapvirtualinstance.models.SAPSupportedResourceSkusResult
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    def sap_supported_sku(
        self,
        location: str,
        sap_supported_sku: Optional[IO] = None,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.SAPSupportedResourceSkusResult:
        """Get a list of SAP supported SKUs for ASCS, Application and Database tier.

        :param location: The name of Azure region. Required.
        :type location: str
        :param sap_supported_sku: SAP Supported SKU Request body. Default value is None.
        :type sap_supported_sku: IO
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: SAPSupportedResourceSkusResult or the result of cls(response)
        :rtype: ~azure.mgmt.workloads.sapvirtualinstance.models.SAPSupportedResourceSkusResult
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace
    def sap_supported_sku(
        self,
        location: str,
        sap_supported_sku: Optional[Union[_models.SAPSupportedSkusRequest, IO]] = None,
        **kwargs: Any
    ) -> _models.SAPSupportedResourceSkusResult:
        """Get a list of SAP supported SKUs for ASCS, Application and Database tier.

        :param location: The name of Azure region. Required.
        :type location: str
        :param sap_supported_sku: SAP Supported SKU Request body. Is either a SAPSupportedSkusRequest
         type or a IO type. Default value is None.
        :type sap_supported_sku:
         ~azure.mgmt.workloads.sapvirtualinstance.models.SAPSupportedSkusRequest or IO
        :keyword content_type: Body Parameter content-type. Known values are: 'application/json'.
         Default value is None.
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: SAPSupportedResourceSkusResult or the result of cls(response)
        :rtype: ~azure.mgmt.workloads.sapvirtualinstance.models.SAPSupportedResourceSkusResult
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
        cls: ClsType[_models.SAPSupportedResourceSkusResult] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(sap_supported_sku, (IOBase, bytes)):
            _content = sap_supported_sku
        else:
            if sap_supported_sku is not None:
                _json = self._serialize.body(sap_supported_sku, "SAPSupportedSkusRequest")
            else:
                _json = None

        request = build_sap_supported_sku_request(
            location=location,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            content=_content,
            template_url=self.sap_supported_sku.metadata["url"],
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

        deserialized = self._deserialize("SAPSupportedResourceSkusResult", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    sap_supported_sku.metadata = {
        "url": "/subscriptions/{subscriptionId}/providers/Microsoft.Workloads/locations/{location}/sapVirtualInstanceMetadata/default/getSapSupportedSku"
    }

    @overload
    def sap_disk_configurations(
        self,
        location: str,
        sap_disk_configurations: Optional[_models.SAPDiskConfigurationsRequest] = None,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.SAPDiskConfigurationsResult:
        """Get the SAP Disk Configuration Layout prod/non-prod SAP System.

        :param location: The name of Azure region. Required.
        :type location: str
        :param sap_disk_configurations: SAP Disk Configurations Request body. Default value is None.
        :type sap_disk_configurations:
         ~azure.mgmt.workloads.sapvirtualinstance.models.SAPDiskConfigurationsRequest
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: SAPDiskConfigurationsResult or the result of cls(response)
        :rtype: ~azure.mgmt.workloads.sapvirtualinstance.models.SAPDiskConfigurationsResult
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    def sap_disk_configurations(
        self,
        location: str,
        sap_disk_configurations: Optional[IO] = None,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.SAPDiskConfigurationsResult:
        """Get the SAP Disk Configuration Layout prod/non-prod SAP System.

        :param location: The name of Azure region. Required.
        :type location: str
        :param sap_disk_configurations: SAP Disk Configurations Request body. Default value is None.
        :type sap_disk_configurations: IO
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: SAPDiskConfigurationsResult or the result of cls(response)
        :rtype: ~azure.mgmt.workloads.sapvirtualinstance.models.SAPDiskConfigurationsResult
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace
    def sap_disk_configurations(
        self,
        location: str,
        sap_disk_configurations: Optional[Union[_models.SAPDiskConfigurationsRequest, IO]] = None,
        **kwargs: Any
    ) -> _models.SAPDiskConfigurationsResult:
        """Get the SAP Disk Configuration Layout prod/non-prod SAP System.

        :param location: The name of Azure region. Required.
        :type location: str
        :param sap_disk_configurations: SAP Disk Configurations Request body. Is either a
         SAPDiskConfigurationsRequest type or a IO type. Default value is None.
        :type sap_disk_configurations:
         ~azure.mgmt.workloads.sapvirtualinstance.models.SAPDiskConfigurationsRequest or IO
        :keyword content_type: Body Parameter content-type. Known values are: 'application/json'.
         Default value is None.
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: SAPDiskConfigurationsResult or the result of cls(response)
        :rtype: ~azure.mgmt.workloads.sapvirtualinstance.models.SAPDiskConfigurationsResult
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
        cls: ClsType[_models.SAPDiskConfigurationsResult] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(sap_disk_configurations, (IOBase, bytes)):
            _content = sap_disk_configurations
        else:
            if sap_disk_configurations is not None:
                _json = self._serialize.body(sap_disk_configurations, "SAPDiskConfigurationsRequest")
            else:
                _json = None

        request = build_sap_disk_configurations_request(
            location=location,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            content=_content,
            template_url=self.sap_disk_configurations.metadata["url"],
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

        deserialized = self._deserialize("SAPDiskConfigurationsResult", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    sap_disk_configurations.metadata = {
        "url": "/subscriptions/{subscriptionId}/providers/Microsoft.Workloads/locations/{location}/sapVirtualInstanceMetadata/default/getDiskConfigurations"
    }

    @overload
    def sap_availability_zone_details(
        self,
        location: str,
        sap_availability_zone_details: Optional[_models.SAPAvailabilityZoneDetailsRequest] = None,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.SAPAvailabilityZoneDetailsResult:
        """Get the recommended SAP Availability Zone Pair Details for your region.

        :param location: The name of Azure region. Required.
        :type location: str
        :param sap_availability_zone_details: SAP Availability Zone Details Request body. Default value
         is None.
        :type sap_availability_zone_details:
         ~azure.mgmt.workloads.sapvirtualinstance.models.SAPAvailabilityZoneDetailsRequest
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: SAPAvailabilityZoneDetailsResult or the result of cls(response)
        :rtype: ~azure.mgmt.workloads.sapvirtualinstance.models.SAPAvailabilityZoneDetailsResult
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    def sap_availability_zone_details(
        self,
        location: str,
        sap_availability_zone_details: Optional[IO] = None,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.SAPAvailabilityZoneDetailsResult:
        """Get the recommended SAP Availability Zone Pair Details for your region.

        :param location: The name of Azure region. Required.
        :type location: str
        :param sap_availability_zone_details: SAP Availability Zone Details Request body. Default value
         is None.
        :type sap_availability_zone_details: IO
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: SAPAvailabilityZoneDetailsResult or the result of cls(response)
        :rtype: ~azure.mgmt.workloads.sapvirtualinstance.models.SAPAvailabilityZoneDetailsResult
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace
    def sap_availability_zone_details(
        self,
        location: str,
        sap_availability_zone_details: Optional[Union[_models.SAPAvailabilityZoneDetailsRequest, IO]] = None,
        **kwargs: Any
    ) -> _models.SAPAvailabilityZoneDetailsResult:
        """Get the recommended SAP Availability Zone Pair Details for your region.

        :param location: The name of Azure region. Required.
        :type location: str
        :param sap_availability_zone_details: SAP Availability Zone Details Request body. Is either a
         SAPAvailabilityZoneDetailsRequest type or a IO type. Default value is None.
        :type sap_availability_zone_details:
         ~azure.mgmt.workloads.sapvirtualinstance.models.SAPAvailabilityZoneDetailsRequest or IO
        :keyword content_type: Body Parameter content-type. Known values are: 'application/json'.
         Default value is None.
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: SAPAvailabilityZoneDetailsResult or the result of cls(response)
        :rtype: ~azure.mgmt.workloads.sapvirtualinstance.models.SAPAvailabilityZoneDetailsResult
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
        cls: ClsType[_models.SAPAvailabilityZoneDetailsResult] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(sap_availability_zone_details, (IOBase, bytes)):
            _content = sap_availability_zone_details
        else:
            if sap_availability_zone_details is not None:
                _json = self._serialize.body(sap_availability_zone_details, "SAPAvailabilityZoneDetailsRequest")
            else:
                _json = None

        request = build_sap_availability_zone_details_request(
            location=location,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            content=_content,
            template_url=self.sap_availability_zone_details.metadata["url"],
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

        deserialized = self._deserialize("SAPAvailabilityZoneDetailsResult", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    sap_availability_zone_details.metadata = {
        "url": "/subscriptions/{subscriptionId}/providers/Microsoft.Workloads/locations/{location}/sapVirtualInstanceMetadata/default/getAvailabilityZoneDetails"
    }
