# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from io import IOBase
from typing import Any, Callable, Dict, IO, Iterable, Optional, TypeVar, Union, overload
import urllib.parse

from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    ResourceNotModifiedError,
    map_error,
)
from azure.core.paging import ItemPaged
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator import distributed_trace
from azure.core.utils import case_insensitive_dict
from azure.mgmt.core.exceptions import ARMErrorFormat

from .. import models as _models
from ..._serialization import Serializer
from .._vendor import _convert_request

T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False


def build_create_or_update_request(
    management_group_id: str, tenant_action_group_name: str, *, x_ms_client_tenant_id: str, **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2023-03-01-preview"))
    content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop(
        "template_url",
        "/providers/Microsoft.Management/managementGroups/{managementGroupId}/providers/Microsoft.Insights/tenantActionGroups/{tenantActionGroupName}",
    )  # pylint: disable=line-too-long
    path_format_arguments = {
        "managementGroupId": _SERIALIZER.url("management_group_id", management_group_id, "str"),
        "tenantActionGroupName": _SERIALIZER.url("tenant_action_group_name", tenant_action_group_name, "str"),
    }

    _url: str = _url.format(**path_format_arguments)  # type: ignore

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    _headers["x-ms-client-tenant-id"] = _SERIALIZER.header("x_ms_client_tenant_id", x_ms_client_tenant_id, "str")
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="PUT", url=_url, params=_params, headers=_headers, **kwargs)


def build_get_request(
    management_group_id: str, tenant_action_group_name: str, *, x_ms_client_tenant_id: str, **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2023-03-01-preview"))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop(
        "template_url",
        "/providers/Microsoft.Management/managementGroups/{managementGroupId}/providers/Microsoft.Insights/tenantActionGroups/{tenantActionGroupName}",
    )  # pylint: disable=line-too-long
    path_format_arguments = {
        "managementGroupId": _SERIALIZER.url("management_group_id", management_group_id, "str"),
        "tenantActionGroupName": _SERIALIZER.url("tenant_action_group_name", tenant_action_group_name, "str"),
    }

    _url: str = _url.format(**path_format_arguments)  # type: ignore

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    _headers["x-ms-client-tenant-id"] = _SERIALIZER.header("x_ms_client_tenant_id", x_ms_client_tenant_id, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, params=_params, headers=_headers, **kwargs)


def build_delete_request(
    management_group_id: str, tenant_action_group_name: str, *, x_ms_client_tenant_id: str, **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2023-03-01-preview"))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop(
        "template_url",
        "/providers/Microsoft.Management/managementGroups/{managementGroupId}/providers/Microsoft.Insights/tenantActionGroups/{tenantActionGroupName}",
    )  # pylint: disable=line-too-long
    path_format_arguments = {
        "managementGroupId": _SERIALIZER.url("management_group_id", management_group_id, "str"),
        "tenantActionGroupName": _SERIALIZER.url("tenant_action_group_name", tenant_action_group_name, "str"),
    }

    _url: str = _url.format(**path_format_arguments)  # type: ignore

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    _headers["x-ms-client-tenant-id"] = _SERIALIZER.header("x_ms_client_tenant_id", x_ms_client_tenant_id, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="DELETE", url=_url, params=_params, headers=_headers, **kwargs)


def build_update_request(
    management_group_id: str, tenant_action_group_name: str, *, x_ms_client_tenant_id: str, **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2023-03-01-preview"))
    content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop(
        "template_url",
        "/providers/Microsoft.Management/managementGroups/{managementGroupId}/providers/Microsoft.Insights/tenantActionGroups/{tenantActionGroupName}",
    )  # pylint: disable=line-too-long
    path_format_arguments = {
        "managementGroupId": _SERIALIZER.url("management_group_id", management_group_id, "str"),
        "tenantActionGroupName": _SERIALIZER.url("tenant_action_group_name", tenant_action_group_name, "str"),
    }

    _url: str = _url.format(**path_format_arguments)  # type: ignore

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    _headers["x-ms-client-tenant-id"] = _SERIALIZER.header("x_ms_client_tenant_id", x_ms_client_tenant_id, "str")
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="PATCH", url=_url, params=_params, headers=_headers, **kwargs)


def build_list_by_management_group_id_request(
    management_group_id: str, *, x_ms_client_tenant_id: str, **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2023-03-01-preview"))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop(
        "template_url",
        "/providers/Microsoft.Management/managementGroups/{managementGroupId}/providers/Microsoft.Insights/tenantActionGroups",
    )  # pylint: disable=line-too-long
    path_format_arguments = {
        "managementGroupId": _SERIALIZER.url("management_group_id", management_group_id, "str"),
    }

    _url: str = _url.format(**path_format_arguments)  # type: ignore

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    _headers["x-ms-client-tenant-id"] = _SERIALIZER.header("x_ms_client_tenant_id", x_ms_client_tenant_id, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, params=_params, headers=_headers, **kwargs)


class TenantActionGroupsOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.mgmt.monitor.v2023_03_01_preview.MonitorManagementClient`'s
        :attr:`tenant_action_groups` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs):
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")
        self._api_version = input_args.pop(0) if input_args else kwargs.pop("api_version")

    @overload
    def create_or_update(
        self,
        management_group_id: str,
        tenant_action_group_name: str,
        x_ms_client_tenant_id: str,
        action_group: _models.TenantActionGroupResource,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.TenantActionGroupResource:
        """Create a new tenant action group or update an existing one.

        :param management_group_id: The management group id. Required.
        :type management_group_id: str
        :param tenant_action_group_name: The name of the action group. Required.
        :type tenant_action_group_name: str
        :param x_ms_client_tenant_id: The tenant ID of the client making the request. Required.
        :type x_ms_client_tenant_id: str
        :param action_group: The tenant action group to create or use for the update. Required.
        :type action_group: ~azure.mgmt.monitor.v2023_03_01_preview.models.TenantActionGroupResource
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: TenantActionGroupResource or the result of cls(response)
        :rtype: ~azure.mgmt.monitor.v2023_03_01_preview.models.TenantActionGroupResource
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    def create_or_update(
        self,
        management_group_id: str,
        tenant_action_group_name: str,
        x_ms_client_tenant_id: str,
        action_group: IO,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.TenantActionGroupResource:
        """Create a new tenant action group or update an existing one.

        :param management_group_id: The management group id. Required.
        :type management_group_id: str
        :param tenant_action_group_name: The name of the action group. Required.
        :type tenant_action_group_name: str
        :param x_ms_client_tenant_id: The tenant ID of the client making the request. Required.
        :type x_ms_client_tenant_id: str
        :param action_group: The tenant action group to create or use for the update. Required.
        :type action_group: IO
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: TenantActionGroupResource or the result of cls(response)
        :rtype: ~azure.mgmt.monitor.v2023_03_01_preview.models.TenantActionGroupResource
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace
    def create_or_update(
        self,
        management_group_id: str,
        tenant_action_group_name: str,
        x_ms_client_tenant_id: str,
        action_group: Union[_models.TenantActionGroupResource, IO],
        **kwargs: Any
    ) -> _models.TenantActionGroupResource:
        """Create a new tenant action group or update an existing one.

        :param management_group_id: The management group id. Required.
        :type management_group_id: str
        :param tenant_action_group_name: The name of the action group. Required.
        :type tenant_action_group_name: str
        :param x_ms_client_tenant_id: The tenant ID of the client making the request. Required.
        :type x_ms_client_tenant_id: str
        :param action_group: The tenant action group to create or use for the update. Is either a
         TenantActionGroupResource type or a IO type. Required.
        :type action_group: ~azure.mgmt.monitor.v2023_03_01_preview.models.TenantActionGroupResource or
         IO
        :keyword content_type: Body Parameter content-type. Known values are: 'application/json'.
         Default value is None.
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: TenantActionGroupResource or the result of cls(response)
        :rtype: ~azure.mgmt.monitor.v2023_03_01_preview.models.TenantActionGroupResource
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

        api_version: str = kwargs.pop(
            "api_version", _params.pop("api-version", self._api_version or "2023-03-01-preview")
        )
        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.TenantActionGroupResource] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(action_group, (IOBase, bytes)):
            _content = action_group
        else:
            _json = self._serialize.body(action_group, "TenantActionGroupResource")

        request = build_create_or_update_request(
            management_group_id=management_group_id,
            tenant_action_group_name=tenant_action_group_name,
            x_ms_client_tenant_id=x_ms_client_tenant_id,
            api_version=api_version,
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
        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200, 201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if response.status_code == 200:
            deserialized = self._deserialize("TenantActionGroupResource", pipeline_response)

        if response.status_code == 201:
            deserialized = self._deserialize("TenantActionGroupResource", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    create_or_update.metadata = {
        "url": "/providers/Microsoft.Management/managementGroups/{managementGroupId}/providers/Microsoft.Insights/tenantActionGroups/{tenantActionGroupName}"
    }

    @distributed_trace
    def get(
        self, management_group_id: str, tenant_action_group_name: str, x_ms_client_tenant_id: str, **kwargs: Any
    ) -> _models.TenantActionGroupResource:
        """Get a tenant action group.

        :param management_group_id: The management group id. Required.
        :type management_group_id: str
        :param tenant_action_group_name: The name of the action group. Required.
        :type tenant_action_group_name: str
        :param x_ms_client_tenant_id: The tenant ID of the client making the request. Required.
        :type x_ms_client_tenant_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: TenantActionGroupResource or the result of cls(response)
        :rtype: ~azure.mgmt.monitor.v2023_03_01_preview.models.TenantActionGroupResource
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

        api_version: str = kwargs.pop(
            "api_version", _params.pop("api-version", self._api_version or "2023-03-01-preview")
        )
        cls: ClsType[_models.TenantActionGroupResource] = kwargs.pop("cls", None)

        request = build_get_request(
            management_group_id=management_group_id,
            tenant_action_group_name=tenant_action_group_name,
            x_ms_client_tenant_id=x_ms_client_tenant_id,
            api_version=api_version,
            template_url=self.get.metadata["url"],
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

        deserialized = self._deserialize("TenantActionGroupResource", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get.metadata = {
        "url": "/providers/Microsoft.Management/managementGroups/{managementGroupId}/providers/Microsoft.Insights/tenantActionGroups/{tenantActionGroupName}"
    }

    @distributed_trace
    def delete(  # pylint: disable=inconsistent-return-statements
        self, management_group_id: str, tenant_action_group_name: str, x_ms_client_tenant_id: str, **kwargs: Any
    ) -> None:
        """Delete a tenant action group.

        :param management_group_id: The management group id. Required.
        :type management_group_id: str
        :param tenant_action_group_name: The name of the action group. Required.
        :type tenant_action_group_name: str
        :param x_ms_client_tenant_id: The tenant ID of the client making the request. Required.
        :type x_ms_client_tenant_id: str
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

        api_version: str = kwargs.pop(
            "api_version", _params.pop("api-version", self._api_version or "2023-03-01-preview")
        )
        cls: ClsType[None] = kwargs.pop("cls", None)

        request = build_delete_request(
            management_group_id=management_group_id,
            tenant_action_group_name=tenant_action_group_name,
            x_ms_client_tenant_id=x_ms_client_tenant_id,
            api_version=api_version,
            template_url=self.delete.metadata["url"],
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

        if response.status_code not in [200, 204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    delete.metadata = {
        "url": "/providers/Microsoft.Management/managementGroups/{managementGroupId}/providers/Microsoft.Insights/tenantActionGroups/{tenantActionGroupName}"
    }

    @overload
    def update(
        self,
        management_group_id: str,
        tenant_action_group_name: str,
        x_ms_client_tenant_id: str,
        tenant_action_group_patch: _models.ActionGroupPatchBody,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.TenantActionGroupResource:
        """Updates an existing tenant action group's tags. To update other fields use the CreateOrUpdate
        method.

        :param management_group_id: The management group id. Required.
        :type management_group_id: str
        :param tenant_action_group_name: The name of the action group. Required.
        :type tenant_action_group_name: str
        :param x_ms_client_tenant_id: The tenant ID of the client making the request. Required.
        :type x_ms_client_tenant_id: str
        :param tenant_action_group_patch: Parameters supplied to the operation. Required.
        :type tenant_action_group_patch:
         ~azure.mgmt.monitor.v2023_03_01_preview.models.ActionGroupPatchBody
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: TenantActionGroupResource or the result of cls(response)
        :rtype: ~azure.mgmt.monitor.v2023_03_01_preview.models.TenantActionGroupResource
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    def update(
        self,
        management_group_id: str,
        tenant_action_group_name: str,
        x_ms_client_tenant_id: str,
        tenant_action_group_patch: IO,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.TenantActionGroupResource:
        """Updates an existing tenant action group's tags. To update other fields use the CreateOrUpdate
        method.

        :param management_group_id: The management group id. Required.
        :type management_group_id: str
        :param tenant_action_group_name: The name of the action group. Required.
        :type tenant_action_group_name: str
        :param x_ms_client_tenant_id: The tenant ID of the client making the request. Required.
        :type x_ms_client_tenant_id: str
        :param tenant_action_group_patch: Parameters supplied to the operation. Required.
        :type tenant_action_group_patch: IO
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: TenantActionGroupResource or the result of cls(response)
        :rtype: ~azure.mgmt.monitor.v2023_03_01_preview.models.TenantActionGroupResource
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace
    def update(
        self,
        management_group_id: str,
        tenant_action_group_name: str,
        x_ms_client_tenant_id: str,
        tenant_action_group_patch: Union[_models.ActionGroupPatchBody, IO],
        **kwargs: Any
    ) -> _models.TenantActionGroupResource:
        """Updates an existing tenant action group's tags. To update other fields use the CreateOrUpdate
        method.

        :param management_group_id: The management group id. Required.
        :type management_group_id: str
        :param tenant_action_group_name: The name of the action group. Required.
        :type tenant_action_group_name: str
        :param x_ms_client_tenant_id: The tenant ID of the client making the request. Required.
        :type x_ms_client_tenant_id: str
        :param tenant_action_group_patch: Parameters supplied to the operation. Is either a
         ActionGroupPatchBody type or a IO type. Required.
        :type tenant_action_group_patch:
         ~azure.mgmt.monitor.v2023_03_01_preview.models.ActionGroupPatchBody or IO
        :keyword content_type: Body Parameter content-type. Known values are: 'application/json'.
         Default value is None.
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: TenantActionGroupResource or the result of cls(response)
        :rtype: ~azure.mgmt.monitor.v2023_03_01_preview.models.TenantActionGroupResource
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

        api_version: str = kwargs.pop(
            "api_version", _params.pop("api-version", self._api_version or "2023-03-01-preview")
        )
        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.TenantActionGroupResource] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(tenant_action_group_patch, (IOBase, bytes)):
            _content = tenant_action_group_patch
        else:
            _json = self._serialize.body(tenant_action_group_patch, "ActionGroupPatchBody")

        request = build_update_request(
            management_group_id=management_group_id,
            tenant_action_group_name=tenant_action_group_name,
            x_ms_client_tenant_id=x_ms_client_tenant_id,
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

        _stream = False
        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize("TenantActionGroupResource", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    update.metadata = {
        "url": "/providers/Microsoft.Management/managementGroups/{managementGroupId}/providers/Microsoft.Insights/tenantActionGroups/{tenantActionGroupName}"
    }

    @distributed_trace
    def list_by_management_group_id(
        self, management_group_id: str, x_ms_client_tenant_id: str, **kwargs: Any
    ) -> Iterable["_models.TenantActionGroupResource"]:
        """Get a list of all tenant action groups in a management group.

        :param management_group_id: The management group id. Required.
        :type management_group_id: str
        :param x_ms_client_tenant_id: The tenant ID of the client making the request. Required.
        :type x_ms_client_tenant_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either TenantActionGroupResource or the result of
         cls(response)
        :rtype:
         ~azure.core.paging.ItemPaged[~azure.mgmt.monitor.v2023_03_01_preview.models.TenantActionGroupResource]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop(
            "api_version", _params.pop("api-version", self._api_version or "2023-03-01-preview")
        )
        cls: ClsType[_models.TenantActionGroupList] = kwargs.pop("cls", None)

        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        def prepare_request(next_link=None):
            if not next_link:

                request = build_list_by_management_group_id_request(
                    management_group_id=management_group_id,
                    x_ms_client_tenant_id=x_ms_client_tenant_id,
                    api_version=api_version,
                    template_url=self.list_by_management_group_id.metadata["url"],
                    headers=_headers,
                    params=_params,
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)

            else:
                # make call to next link with the client's api-version
                _parsed_next_link = urllib.parse.urlparse(next_link)
                _next_request_params = case_insensitive_dict(
                    {
                        key: [urllib.parse.quote(v) for v in value]
                        for key, value in urllib.parse.parse_qs(_parsed_next_link.query).items()
                    }
                )
                _next_request_params["api-version"] = self._config.api_version
                request = HttpRequest(
                    "GET", urllib.parse.urljoin(next_link, _parsed_next_link.path), params=_next_request_params
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)
                request.method = "GET"
            return request

        def extract_data(pipeline_response):
            deserialized = self._deserialize("TenantActionGroupList", pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)  # type: ignore
            return None, iter(list_of_elem)

        def get_next(next_link=None):
            request = prepare_request(next_link)

            _stream = False
            pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
                request, stream=_stream, **kwargs
            )
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
                raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

            return pipeline_response

        return ItemPaged(get_next, extract_data)

    list_by_management_group_id.metadata = {
        "url": "/providers/Microsoft.Management/managementGroups/{managementGroupId}/providers/Microsoft.Insights/tenantActionGroups"
    }
