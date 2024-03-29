# pylint: disable=too-many-lines,too-many-statements
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
from .._serialization import Serializer
from .._vendor import _convert_request

T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False


def build_list_request(
    azure_region: str,
    subscription_id: str,
    *,
    filter: Optional[str] = None,
    skip_token: Optional[str] = None,
    **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2021-11-15"))
    content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop(
        "template_url",
        "/subscriptions/{subscriptionId}/providers/Microsoft.RecoveryServices/locations/{azureRegion}/backupCrrJobs",
    )  # pylint: disable=line-too-long
    path_format_arguments = {
        "azureRegion": _SERIALIZER.url("azure_region", azure_region, "str"),
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, "str"),
    }

    _url: str = _url.format(**path_format_arguments)  # type: ignore

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")
    if filter is not None:
        _params["$filter"] = _SERIALIZER.query("filter", filter, "str")
    if skip_token is not None:
        _params["$skipToken"] = _SERIALIZER.query("skip_token", skip_token, "str")

    # Construct headers
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="POST", url=_url, params=_params, headers=_headers, **kwargs)


class BackupCrrJobsOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.mgmt.recoveryservicesbackup.passivestamp.RecoveryServicesBackupPassiveClient`'s
        :attr:`backup_crr_jobs` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs):
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @overload
    def list(
        self,
        azure_region: str,
        parameters: _models.CrrJobRequest,
        filter: Optional[str] = None,
        skip_token: Optional[str] = None,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> Iterable["_models.JobResource"]:
        """Gets the list of CRR jobs from the target region.

        Gets the list of CRR jobs from the target region.

        :param azure_region: Azure region to hit Api. Required.
        :type azure_region: str
        :param parameters: Backup CRR Job request. Required.
        :type parameters: ~azure.mgmt.recoveryservicesbackup.passivestamp.models.CrrJobRequest
        :param filter: OData filter options. Default value is None.
        :type filter: str
        :param skip_token: skipToken Filter. Default value is None.
        :type skip_token: str
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An iterator like instance of either JobResource or the result of cls(response)
        :rtype:
         ~azure.core.paging.ItemPaged[~azure.mgmt.recoveryservicesbackup.passivestamp.models.JobResource]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    def list(
        self,
        azure_region: str,
        parameters: IO[bytes],
        filter: Optional[str] = None,
        skip_token: Optional[str] = None,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> Iterable["_models.JobResource"]:
        """Gets the list of CRR jobs from the target region.

        Gets the list of CRR jobs from the target region.

        :param azure_region: Azure region to hit Api. Required.
        :type azure_region: str
        :param parameters: Backup CRR Job request. Required.
        :type parameters: IO[bytes]
        :param filter: OData filter options. Default value is None.
        :type filter: str
        :param skip_token: skipToken Filter. Default value is None.
        :type skip_token: str
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :return: An iterator like instance of either JobResource or the result of cls(response)
        :rtype:
         ~azure.core.paging.ItemPaged[~azure.mgmt.recoveryservicesbackup.passivestamp.models.JobResource]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace
    def list(
        self,
        azure_region: str,
        parameters: Union[_models.CrrJobRequest, IO[bytes]],
        filter: Optional[str] = None,
        skip_token: Optional[str] = None,
        **kwargs: Any
    ) -> Iterable["_models.JobResource"]:
        """Gets the list of CRR jobs from the target region.

        Gets the list of CRR jobs from the target region.

        :param azure_region: Azure region to hit Api. Required.
        :type azure_region: str
        :param parameters: Backup CRR Job request. Is either a CrrJobRequest type or a IO[bytes] type.
         Required.
        :type parameters: ~azure.mgmt.recoveryservicesbackup.passivestamp.models.CrrJobRequest or
         IO[bytes]
        :param filter: OData filter options. Default value is None.
        :type filter: str
        :param skip_token: skipToken Filter. Default value is None.
        :type skip_token: str
        :return: An iterator like instance of either JobResource or the result of cls(response)
        :rtype:
         ~azure.core.paging.ItemPaged[~azure.mgmt.recoveryservicesbackup.passivestamp.models.JobResource]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))
        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.JobResourceList] = kwargs.pop("cls", None)

        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})
        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(parameters, (IOBase, bytes)):
            _content = parameters
        else:
            _json = self._serialize.body(parameters, "CrrJobRequest")

        def prepare_request(next_link=None):
            if not next_link:

                _request = build_list_request(
                    azure_region=azure_region,
                    subscription_id=self._config.subscription_id,
                    filter=filter,
                    skip_token=skip_token,
                    api_version=api_version,
                    content_type=content_type,
                    json=_json,
                    content=_content,
                    headers=_headers,
                    params=_params,
                )
                _request = _convert_request(_request)
                _request.url = self._client.format_url(_request.url)

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
                _request = HttpRequest(
                    "GET", urllib.parse.urljoin(next_link, _parsed_next_link.path), params=_next_request_params
                )
                _request = _convert_request(_request)
                _request.url = self._client.format_url(_request.url)
                _request.method = "GET"
            return _request

        def extract_data(pipeline_response):
            deserialized = self._deserialize("JobResourceList", pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)  # type: ignore
            return deserialized.next_link or None, iter(list_of_elem)

        def get_next(next_link=None):
            _request = prepare_request(next_link)

            _stream = False
            pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
                _request, stream=_stream, **kwargs
            )
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                error = self._deserialize.failsafe_deserialize(_models.NewErrorResponse, pipeline_response)
                raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

            return pipeline_response

        return ItemPaged(get_next, extract_data)
