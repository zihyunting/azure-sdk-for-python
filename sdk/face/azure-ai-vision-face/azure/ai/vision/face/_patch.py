# ------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------
"""Customize generated code here.

Follow our quickstart for examples: https://aka.ms/azsdk/python/dpcodegen/python/customize
"""
from typing import Any, Callable, Dict, IO, List, Optional, TypeVar, Union, cast
import sys

from azure.core.pipeline import PipelineResponse
from azure.core.polling import LROPoller, NoPolling, PollingMethod
from azure.core.polling.base_polling import LROBasePolling
from azure.core.tracing.decorator import distributed_trace
from azure.core.rest import HttpRequest, HttpResponse

from azure.core.polling.base_polling import _failed, OperationFailed, _raise_if_bad_http_status_and_method

from . import models as _models
from ._client import FaceAdministrationClient as FaceAdministrationClientGenerated
from ._client import FaceClient as FaceClientGenerated
from ._client import FaceSessionClient as FaceSessionClientGenerated
from ._model_base import _deserialize
from ._operations._operations import (
    FaceAdministrationClientOperationsMixin,
    FaceClientOperationsMixin,
    FaceSessionClientOperationsMixin,
)

if sys.version_info >= (3, 9):
    from collections.abc import MutableMapping
else:
    from typing import MutableMapping  # type: ignore  # pylint: disable=ungrouped-imports
JSON = MutableMapping[str, Any]  # pylint: disable=unsubscriptable-object
T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]


class FacePollingMethod(LROBasePolling):
    _operation_status_response = None

    def __init__(self, *args, **kwargs):
        # self._cont_token_response = kwargs.pop("cont_token_response")
        super().__init__(*args, **kwargs)

    def _poll(self) -> None:
        """Poll status of operation so long as operation is incomplete and
        we have an endpoint to query.

        :raises: OperationFailed if operation status 'Failed' or 'Canceled'.
        :raises: BadStatus if response status invalid.
        :raises: BadResponse if response invalid.
        """
        print("Customized polling method is running")
        if not self.finished():
            self.update_status()
        while not self.finished():
            self._delay()
            self.update_status()

        if _failed(self.status()):
            raise OperationFailed("Operation failed or canceled")

        '''
        final_get_url = self._operation.get_final_get_url(self._pipeline_response)
        if final_get_url:
            self._pipeline_response = self.request_status(final_get_url)
            _raise_if_bad_http_status_and_method(self._pipeline_response.http_response)
        '''

    def update_status(self) -> None:
        """Update the current status of the LRO."""
        self._pipeline_response = self.request_status(self._operation.get_polling_url())
        self._operation_status_response = self._pipeline_response.http_response
        _raise_if_bad_http_status_and_method(self._pipeline_response.http_response)
        self._status = self._operation.get_status(self._pipeline_response)

    def get_operation_status_response(self):
        return self._operation_status_response

class FaceAdministrationClient(FaceAdministrationClientGenerated):
    """FaceAdministrationClient.

    :param endpoint: Supported Cognitive Services endpoints (protocol and hostname, for example:
     https://{resource-name}.cognitiveservices.azure.com). Required.
    :type endpoint: str
    :param credential: Credential used to authenticate requests to the service. Is either a
     AzureKeyCredential type or a TokenCredential type. Required.
    :type credential: ~azure.core.credentials.AzureKeyCredential or
     ~azure.core.credentials.TokenCredential
    :keyword api_version: API Version. Default value is "v1.1-preview.1". Note that overriding this
     default value may result in unsupported behavior.
    :paramtype api_version: str or ~azure.ai.vision.face.models.Versions
    :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
     Retry-After header is present.
    """
    # FIXME - Test
    @distributed_trace
    def create_person3(
        self,
        name: str,
        *,
        user_data: Optional[str] = None,
        **kwargs: Any,
    ) -> LROPoller[_models.FaceOperationStatus]:
        lro_delay = kwargs.pop("polling_interval", self._config.polling_interval)

        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
            "apiVersion": self._serialize.url("self._config.api_version", self._config.api_version, "str"),
        }

        polling_method: PollingMethod = cast(
                PollingMethod, FacePollingMethod(lro_delay, path_format_arguments=path_format_arguments, **kwargs))
        return self.create_person2(name, user_data=user_data, polling=polling_method, **kwargs)

    @distributed_trace
    def create_person2(
        self,
        name: str,
        *,
        user_data: Optional[str] = None,
        **kwargs: Any,
    ) -> LROPoller[_models.FaceOperationStatus]:
        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls: ClsType[_models.FaceOperationStatus] = kwargs.pop("cls", None)
        polling: Union[bool, PollingMethod] = kwargs.pop("polling", True)
        lro_delay = kwargs.pop("polling_interval", self._config.polling_interval)
        cont_token: Optional[str] = kwargs.pop("continuation_token", None)
        if cont_token is None:
            raw_result = self._create_person(  # type: ignore
                name=name, user_data=user_data, cls=lambda x, y, z: x, headers=_headers, params=_params, **kwargs)

        print(f"raw_result: {raw_result.http_response}, headers: {raw_result.http_response.headers}")

        kwargs.pop("error_map", None)

        def get_long_running_output(pipeline_response):
            response_headers = {}
            response = pipeline_response.http_response
            response_headers["operation-Location"] = self._deserialize(
                "str", response.headers.get("operation-Location")
            )

            deserialized = _deserialize(_models.FaceOperationStatus, response.json())
            if cls:
                return cls(pipeline_response, deserialized, response_headers)  # type: ignore
            return deserialized

        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
            "apiVersion": self._serialize.url("self._config.api_version", self._config.api_version, "str"),
        }

        if polling is True:
            polling_method: PollingMethod = cast(
                PollingMethod, LROBasePolling(lro_delay, path_format_arguments=path_format_arguments, **kwargs)
            )
        elif polling is False:
            polling_method = cast(PollingMethod, NoPolling())
        else:
            polling_method = polling
        if cont_token:
            return LROPoller[_models.FaceOperationStatus].from_continuation_token(
                polling_method=polling_method,
                continuation_token=cont_token,
                client=self._client,
                deserialization_callback=get_long_running_output,
            )
        print(f"Polling method: {polling_method}")
        return LROPoller[_models.FaceOperationStatus](
            self._client, raw_result, get_long_running_output, polling_method  # type: ignore
        )

    # TODO
    @distributed_trace
    def create_person(
        self,
        name: str,
        *,
        user_data: Optional[str] = None,
        **kwargs: Any,
    ) -> LROPoller[_models.CreatePersonResult]:
        """Creates a new person in a Person Directory. To add face to this person, please call
        PersonDirectory Person - Add Face.

        :param name: User defined name, maximum length is 128. Required.
        :type name: str
        :keyword user_data: Optional user defined data. Length should not exceed 16K. Default value is
         None.
        :paramtype user_data: str
        :return: An instance of LROPoller that returns CreatePersonResult. The CreatePersonResult is compatible
         with MutableMapping
        :rtype:
         ~azure.core.polling.LROPoller[~azure.ai.vision.face.models.CreatePersonResult]
        :raises ~azure.core.exceptions.HttpResponseError:

        Example:
            .. code-block:: python

                # JSON input template you can fill out and use as your body input.
                body = {
                    "name": "str",  # User defined name, maximum length is 128. Required.
                    "userData": "str"  # Optional. Optional user defined data. Length should not
                      exceed 16K.
                }

                # response body for status code(s): 202
                response == {
                    "personId": "str"  # Person ID of the person. Required.
                }
        """
        # TODO
        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls: ClsType[_models.CreatePersonResult] = kwargs.pop("cls", None)
        polling: Union[bool, PollingMethod] = kwargs.pop("polling", True)
        lro_delay = kwargs.pop("polling_interval", self._config.polling_interval)

        # get response from `create_person`
        raw_result = FaceAdministrationClientOperationsMixin._create_person(  # type: ignore
            self, name=name, user_data=user_data, cls=lambda x, y, z: x, headers=_headers, params=_params, **kwargs)
        kwargs.pop("error_map", None)

        def get_long_running_output(pipeline_response):
            return None
            response = pipeline_response.http_response
            deserialized = _deserialize(_models.CreatePersonResult, response.json())

            if cls:
                return cls(pipeline_response, deserialized)  # type: ignore
            return deserialized

        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
            "apiVersion": self._serialize.url("self._config.api_version", self._config.api_version, "str"),
        }

        if polling is True:
            polling_method: PollingMethod = cast(
                PollingMethod, LROBasePolling(lro_delay, path_format_arguments=path_format_arguments, **kwargs)
            )
        elif polling is False:
            polling_method = cast(PollingMethod, NoPolling())
        else:
            polling_method = polling

        return LROPoller[_models.CreatePersonResult](
            self._client, raw_result, get_long_running_output, polling_method  # type: ignore
        )

    # TODO
    @distributed_trace
    def add_person_face_from_url(
        self,
        person_id: str,
        url: str,
        detection_model: Union[str, _models.FaceDetectionModel],
        recognition_model: Union[str, _models.FaceRecognitionModel],
        *,
        target_face: Optional[List[int]] = None,
        user_data: Optional[str] = None,
        **kwargs: Any,
    ) -> _models.AddFaceResult:
        # pylint: disable=line-too-long
        """Add a face to a person (see PersonDirectory Person - Create) for face identification or
        verification.

        To deal with an image containing multiple faces, input face can be specified as an image with a
        targetFace rectangle. It returns a persistedFaceId representing the added face. No image will
        be stored. Only the extracted face feature(s) will be stored on server until PersonDirectory
        Person - Delete Face or PersonDirectory Person - Delete is called.

        Note that persistedFaceId is different from faceId generated by Face - Detect.
        >
        *


        * Higher face image quality means better recognition precision. Please consider high-quality
        faces: frontal, clear, and face size is 200x200 pixels (100 pixels between eyes) or bigger.
        * Each person entry can hold up to 248 faces.
        * JPEG, PNG, GIF (the first frame), and BMP format are supported. The allowed image file size
        is from 1KB to 6MB.
        * "targetFace" rectangle should contain one face. Zero or multiple faces will be regarded as an
        error. If the provided "targetFace" rectangle is not returned from Face - Detect, there's no
        guarantee to detect and add the face successfully.
        * Out of detectable face size (36x36 - 4096x4096 pixels), large head-pose, or large occlusions
        will cause failures.
        * The minimum detectable face size is 36x36 pixels in an image no larger than 1920x1080 pixels.
        Images with dimensions higher than 1920x1080 pixels will need a proportionally larger minimum
        face size.
        * Different 'detectionModel' values can be provided. To use and compare different detection
        models, please refer to
        https://learn.microsoft.com/en-us/azure/ai-services/computer-vision/how-to/specify-detection-model
          *
        * Adding/deleting faces to/from a same person will be processed sequentially. Adding/deleting
        faces to/from different persons are processed in parallel.
        * This is a long running operation. Use Response Header "Operation-Location" to determine when
        the AddFace operation has successfully propagated for future requests to Face - Identify. For
        further information about Operation-Locations see 'Operations - Get Status'.

        :param person_id: Person ID of the person. Required.
        :type person_id: str
        :param url: URL of input image. Required.
        :type url: str
        :param detection_model: The 'detectionModel' associated with the detected faceIds. Supported
         'detectionModel' values include 'detection_01', 'detection_02' and 'detection_03'. The default
         value is 'detection_01'. Known values are: "detection_01", "detection_02", and "detection_03".
         Required.
        :type detection_model: str or ~azure.ai.vision.face.models.FaceDetectionModel
        :param recognition_model: The 'recognitionModel' associated with faces. Known values are:
         "recognition_01", "recognition_02", "recognition_03", and "recognition_04". Required.
        :type recognition_model: str or ~azure.ai.vision.face.models.FaceRecognitionModel
        :keyword target_face: A face rectangle to specify the target face to be added to a person, in
         the format of 'targetFace=left,top,width,height'. Default value is None.
        :paramtype target_face: list[int]
        :keyword user_data: User-provided data attached to the face. The size limit is 1K. Default
         value is None.
        :paramtype user_data: str
        :return: AddFaceResult. The AddFaceResult is compatible with MutableMapping
        :rtype: ~azure.ai.vision.face.models.AddFaceResult
        :raises ~azure.core.exceptions.HttpResponseError:

        Example:
            .. code-block:: python

                # JSON input template you can fill out and use as your body input.
                body = {
                    "url": "str"  # URL of input image. Required.
                }

                # response body for status code(s): 202
                response == {
                    "persistedFaceId": "str"  # Persisted Face ID of the added face, which is
                      persisted and will not expire. Different from faceId which is created in Face -
                      Detect and will expire in 24 hours after the detection call. Required.
                }
        """
        # TODO
        return FaceAdministrationClientOperationsMixin._add_person_face_from_url(
            self,
            person_id,
            recognition_model,
            url=url,
            target_face=target_face,
            detection_model=detection_model,
            user_data=user_data,
            **kwargs)

    # TODO
    @distributed_trace
    def add_person_face(
        self,
        person_id: str,
        image_content: bytes,
        detection_model: Union[str, _models.FaceDetectionModel],
        recognition_model: Union[str, _models.FaceRecognitionModel],
        *,
        target_face: Optional[List[int]] = None,
        user_data: Optional[str] = None,
        **kwargs: Any,
    ) -> LROPoller[_models.PersonDirectoryFace]:
        # pylint: disable=line-too-long
        """Add a face to a person (see PersonDirectory Person - Create) for face identification or
        verification.

        To deal with an image containing multiple faces, input face can be specified as an image with a
        targetFace rectangle. It returns a persistedFaceId representing the added face. No image will
        be stored. Only the extracted face feature(s) will be stored on server until PersonDirectory
        Person - Delete Face or PersonDirectory Person - Delete is called.

        Note that persistedFaceId is different from faceId generated by Face - Detect.
        >
        *


        * Higher face image quality means better recognition precision. Please consider high-quality
        faces: frontal, clear, and face size is 200x200 pixels (100 pixels between eyes) or bigger.
        * Each person entry can hold up to 248 faces.
        * JPEG, PNG, GIF (the first frame), and BMP format are supported. The allowed image file size
        is from 1KB to 6MB.
        * "targetFace" rectangle should contain one face. Zero or multiple faces will be regarded as an
        error. If the provided "targetFace" rectangle is not returned from Face - Detect, there's no
        guarantee to detect and add the face successfully.
        * Out of detectable face size (36x36 - 4096x4096 pixels), large head-pose, or large occlusions
        will cause failures.
        * The minimum detectable face size is 36x36 pixels in an image no larger than 1920x1080 pixels.
        Images with dimensions higher than 1920x1080 pixels will need a proportionally larger minimum
        face size.
        * Different 'detectionModel' values can be provided. To use and compare different detection
        models, please refer to
        https://learn.microsoft.com/en-us/azure/ai-services/computer-vision/how-to/specify-detection-model
          *
        * Adding/deleting faces to/from a same person will be processed sequentially. Adding/deleting
        faces to/from different persons are processed in parallel.
        * This is a long running operation. Use Response Header "Operation-Location" to determine when
        the AddFace operation has successfully propagated for future requests to Face - Identify. For
        further information about Operation-Locations see 'Operations - Get Status'.

        :param person_id: Person ID of the person. Required.
        :type person_id: str
        :param image_content: The image to be analyzed. Required.
        :type image_content: bytes
        :param detection_model: The 'detectionModel' associated with the detected faceIds. Supported
         'detectionModel' values include 'detection_01', 'detection_02' and 'detection_03'. The default
         value is 'detection_01'. Known values are: "detection_01", "detection_02", and "detection_03".
         Required.
        :type detection_model: str or ~azure.ai.vision.face.models.FaceDetectionModel
        :param recognition_model: The 'recognitionModel' associated with faces. Known values are:
         "recognition_01", "recognition_02", "recognition_03", and "recognition_04". Required.
        :type recognition_model: str or ~azure.ai.vision.face.models.FaceRecognitionModel
        :keyword target_face: A face rectangle to specify the target face to be added to a person, in
         the format of 'targetFace=left,top,width,height'. Default value is None.
        :paramtype target_face: list[int]
        :keyword user_data: User-provided data attached to the face. The size limit is 1K. Default
         value is None.
        :paramtype user_data: str
        :return: An instance of LROPoller that returns PersonDirectoryFace. The PersonDirectoryFace is compatible
         with MutableMapping
        :rtype:
         ~azure.core.polling.LROPoller[~azure.ai.vision.face.models.PersonDirectoryFace]
        :raises ~azure.core.exceptions.HttpResponseError:

        Example:
            .. code-block:: python

                # response body for status code(s): 202
                response == {
                    "persistedFaceId": "str"  # Persisted Face ID of the added face, which is
                      persisted and will not expire. Different from faceId which is created in Face -
                      Detect and will expire in 24 hours after the detection call. Required.
                }
        """
        # TODO
        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls: ClsType[_models.PersonDirectoryFace] = kwargs.pop("cls", None)
        polling: Union[bool, PollingMethod] = kwargs.pop("polling", True)
        lro_delay = kwargs.pop("polling_interval", self._config.polling_interval)

        # get response from `add_person_face`
        raw_result = FaceAdministrationClientOperationsMixin._add_person_face(  # type: ignore
            self, person_id, recognition_model, image_content,
            target_face=target_face, detection_model=detection_model, user_data=user_data,
            cls=lambda x, y, z: x, headers=_headers, params=_params, **kwargs)
        kwargs.pop("error_map", None)

        print(f"response: {raw_result.http_response.json()}, response_headers: {raw_result.http_response.headers}")

        def get_long_running_output(pipeline_response):
            response_headers = {}
            response = pipeline_response.http_response
            response_headers["operation-Location"] = self._deserialize(
                "str", response.headers.get("operation-Location")
            )

            deserialized = _deserialize(_models.PersonDirectoryFace, response.json())
            if cls:
                return cls(pipeline_response, deserialized, response_headers)  # type: ignore
            return deserialized

        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
            "apiVersion": self._serialize.url("self._config.api_version", self._config.api_version, "str"),
        }

        if polling is True:
            polling_method: PollingMethod = cast(
                PollingMethod, LROBasePolling(lro_delay, path_format_arguments=path_format_arguments, **kwargs)
            )
        elif polling is False:
            polling_method = cast(PollingMethod, NoPolling())
        else:
            polling_method = polling

        return LROPoller[_models.PersonDirectoryFace](
            self._client, raw_result, get_long_running_output, polling_method  # type: ignore
        )

    # TODO
    @distributed_trace
    def create_dynamic_person_group(  # pylint: disable=inconsistent-return-statements
        self,
        dynamic_person_group_id: str,
        name: str,
        *,
        add_person_ids: Optional[List[str]] = None,
        user_data: Optional[str] = None,
        **kwargs: Any,
    ) -> LROPoller[None]:
        """Creates a new Dynamic Person Group with specified dynamicPersonGroupId, name, and user-provided
        userData.

        A Dynamic Person Group is a container that references PersonDirectory Person - Create. After
        creation, use PersonDirectory DynamicPersonGroup - Update to add or remove persons into the
        Dynamic Person Group.

        DynamicPersonGroup and UserData will be stored on server until PersonDirectory
        DynamicPersonGroup - Delete is called. Use Face - Identify with the dynamicPersonGroupId
        parameter to identify against persons.

        No image will be stored. Only the person's extracted face feature(s) and userData will be
        stored on server until PersonDirectory Person - Delete or PersonDirectory Person - Delete Face
        is called.

        'recognitionModel' does not need to be specified with Dynamic Person Groups. Dynamic Person
        Groups are references to PersonDirectory Person - Create and therefore work with most all
        'recognitionModels'. The faceId's provided during Face - Identify determine the
        'recognitionModel' used.

        :param dynamic_person_group_id: ID of the dynamic person group. Required.
        :type dynamic_person_group_id: str
        :param name: User defined name, maximum length is 128. Required.
        :type name: str
        :keyword add_person_ids: Array of personIds created by PersonDirectory Person - Create to be
         added. Default value is None.
        :paramtype add_person_ids: list[str]
        :keyword user_data: Optional user defined data. Length should not exceed 16K. Default value is
         None.
        :paramtype user_data: str
        :return: None
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:

        Example:
            .. code-block:: python

                # JSON input template you can fill out and use as your body input.
                body = {
                    "name": "str",  # User defined name, maximum length is 128. Required.
                    "addPersonIds": [
                        "str"  # Optional. Array of personIds created by PersonDirectory
                          Person - Create to be added.
                    ],
                    "userData": "str"  # Optional. Optional user defined data. Length should not
                      exceed 16K.
                }
        """
        # TODO
        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls: ClsType[None] = kwargs.pop("cls", None)
        polling: Union[bool, PollingMethod] = kwargs.pop("polling", True)
        lro_delay = kwargs.pop("polling_interval", self._config.polling_interval)

        # get response from `add_person_face`
        raw_result = FaceAdministrationClientOperationsMixin._create_dynamic_person_group(  # type: ignore
            self, dynamic_person_group_id, name=name, add_person_ids=add_person_ids, user_data=user_data,
            cls=lambda x, y, z: x, headers=_headers, params=_params, **kwargs)
        kwargs.pop("error_map", None)

        def get_long_running_output(pipeline_response):
            response_headers = {}
            response = pipeline_response.http_response
            response_headers["operation-Location"] = self._deserialize(
                "str", response.headers.get("operation-Location")
            )

            # deserialized = _deserialize(_models.DynamicPersonGroup, response.json())
            # if cls:
            #     return cls(pipeline_response, deserialized, response_headers)  # type: ignore
            # return deserialized
            return None

        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
            "apiVersion": self._serialize.url("self._config.api_version", self._config.api_version, "str"),
        }

        if raw_result.http_response.status_code == 200 or polling is False:
            polling_method = cast(PollingMethod, NoPolling())
        elif polling is True:
            polling_method: PollingMethod = cast(
                PollingMethod, LROBasePolling(lro_delay, path_format_arguments=path_format_arguments, **kwargs)
            )
        else:
            polling_method = polling

        return LROPoller[None](
            self._client, raw_result, get_long_running_output, polling_method  # type: ignore
        )

    # TODO
    @distributed_trace
    def update_dynamic_person_group(  # pylint: disable=inconsistent-return-statements
        self,
        dynamic_person_group_id: str,
        name: str,
        *,
        add_person_ids: Optional[List[str]] = None,
        remove_person_ids: Optional[List[str]] = None,
        user_data: Optional[str] = None,
        **kwargs: Any,
    ) -> None:
        """Update the name or userData of an existing Dynamic Person Group, and manage its members by
        adding or removing persons.

        The properties keep unchanged if they are not in request body.

        :param dynamic_person_group_id: ID of the dynamic person group. Required.
        :type dynamic_person_group_id: str
        :param name: User defined name, maximum length is 128. Required.
        :type name: str
        :keyword add_person_ids: Array of personIds created by PersonDirectory Person - Create to be
         added. Default value is None.
        :paramtype add_person_ids: list[str]
        :keyword remove_person_ids: Array of personIds created by PersonDirectory Person - Create to be
         removed. Default value is None.
        :paramtype remove_person_ids: list[str]
        :keyword user_data: Optional user defined data. Length should not exceed 16K. Default value is
         None.
        :paramtype user_data: str
        :return: None
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:

        Example:
            .. code-block:: python

                # JSON input template you can fill out and use as your body input.
                body = {
                    "name": "str",  # User defined name, maximum length is 128. Required.
                    "addPersonIds": [
                        "str"  # Optional. Array of personIds created by PersonDirectory
                          Person - Create to be added.
                    ],
                    "removePersonIds": [
                        "str"  # Optional. Array of personIds created by PersonDirectory
                          Person - Create to be removed.
                    ],
                    "userData": "str"  # Optional. Optional user defined data. Length should not
                      exceed 16K.
                }
        """
        # TODO
        return FaceAdministrationClientOperationsMixin._update_dynamic_person_group(
            self,
            dynamic_person_group_id,
            name=name,
            add_person_ids=add_person_ids,
            remove_person_ids=remove_person_ids,
            user_data=user_data,
            **kwargs)


class FaceClient(FaceClientGenerated):
    """FaceClient.

    :param endpoint: Supported Cognitive Services endpoints (protocol and hostname, for example:
     https://{resource-name}.cognitiveservices.azure.com). Required.
    :type endpoint: str
    :param credential: Credential used to authenticate requests to the service. Is either a
     AzureKeyCredential type or a TokenCredential type. Required.
    :type credential: ~azure.core.credentials.AzureKeyCredential or
     ~azure.core.credentials.TokenCredential
    :keyword api_version: API Version. Default value is "v1.1-preview.1". Note that overriding this
     default value may result in unsupported behavior.
    :paramtype api_version: str or ~azure.ai.vision.face.models.Versions
    """

    @distributed_trace
    def detect_from_url(
        self,
        url: str,
        detection_model: Union[str, _models.FaceDetectionModel],
        recognition_model: Union[str, _models.FaceRecognitionModel],
        *,
        return_face_id: Optional[bool] = False,
        return_face_landmarks: Optional[bool] = None,
        return_face_attributes: Optional[List[Union[str, _models.FaceAttributeType]]] = None,
        return_recognition_model: Optional[bool] = None,
        face_id_time_to_live: Optional[int] = None,
        **kwargs: Any,
    ) -> List[_models._models.FaceDetectionResult]:
        # pylint: disable=line-too-long
        """Detect human faces in an image, return face rectangles, and optionally with faceIds, landmarks,
        and attributes.

        ..

           [!IMPORTANT]
           To mitigate potential misuse that can subject people to stereotyping, discrimination, or
        unfair denial of services, we are retiring Face API attributes that predict emotion, gender,
        age, smile, facial hair, hair, and makeup. Read more about this decision
        https://azure.microsoft.com/en-us/blog/responsible-ai-investments-and-safeguards-for-facial-recognition/.


        *


        * No image will be stored. Only the extracted face feature(s) will be stored on server. The
        faceId is an identifier of the face feature and will be used in Face - Identify, Face - Verify,
        and Face - Find Similar. The stored face features will expire and be deleted at the time
        specified by faceIdTimeToLive after the original detection call.
        * Optional parameters include faceId, landmarks, and attributes. Attributes include headPose,
        glasses, occlusion, accessories, blur, exposure, noise, mask, and qualityForRecognition. Some
        of the results returned for specific attributes may not be highly accurate.
        * JPEG, PNG, GIF (the first frame), and BMP format are supported. The allowed image file size
        is from 1KB to 6MB.
        * The minimum detectable face size is 36x36 pixels in an image no larger than 1920x1080 pixels.
        Images with dimensions higher than 1920x1080 pixels will need a proportionally larger minimum
        face size.
        * Up to 100 faces can be returned for an image. Faces are ranked by face rectangle size from
        large to small.
        * For optimal results when querying Face - Identify, Face - Verify, and Face - Find Similar
        ('returnFaceId' is true), please use faces that are: frontal, clear, and with a minimum size of
        200x200 pixels (100 pixels between eyes).
        * Different 'detectionModel' values can be provided. To use and compare different detection
        models, please refer to
        https://learn.microsoft.com/en-us/azure/ai-services/computer-vision/how-to/specify-detection-model

          * 'detection_02': Face attributes and landmarks are disabled if you choose this detection
        model.
          * 'detection_03': Face attributes (mask and headPose only) and landmarks are supported if you
        choose this detection model.

        * Different 'recognitionModel' values are provided. If follow-up operations like Verify,
        Identify, Find Similar are needed, please specify the recognition model with 'recognitionModel'
        parameter. The default value for 'recognitionModel' is 'recognition_01', if latest model
        needed, please explicitly specify the model you need in this parameter. Once specified, the
        detected faceIds will be associated with the specified recognition model. More details, please
        refer to
        https://learn.microsoft.com/en-us/azure/ai-services/computer-vision/how-to/specify-recognition-model.

        :param url: URL of input image. Required.
        :type url: str
        :param detection_model: The 'detectionModel' associated with the detected faceIds. Supported
         'detectionModel' values include 'detection_01', 'detection_02' and 'detection_03'. The default
         value is 'detection_01'. Known values are: "detection_01", "detection_02", and "detection_03".
         Required.
        :type detection_model: str or ~azure.ai.vision.face.models.FaceDetectionModel
        :param recognition_model: The 'recognitionModel' associated with the detected faceIds.
         Supported 'recognitionModel' values include 'recognition_01', 'recognition_02',
         'recognition_03' or 'recognition_04'. The default value is 'recognition_01'. 'recognition_04'
         is recommended since its accuracy is improved on faces wearing masks compared with
         'recognition_03', and its overall accuracy is improved compared with 'recognition_01' and
         'recognition_02'. Known values are: "recognition_01", "recognition_02", "recognition_03", and
         "recognition_04". Required.
        :type recognition_model: str or ~azure.ai.vision.face.models.FaceRecognitionModel
        :keyword return_face_id: Return faceIds of the detected faces or not. The default value is
         true. Default value is False.
        :paramtype return_face_id: bool
        :keyword return_face_landmarks: Return face landmarks of the detected faces or not. The default
         value is false. Default value is None.
        :paramtype return_face_landmarks: bool
        :keyword return_face_attributes: Analyze and return the one or more specified face attributes
         in the comma-separated string like 'returnFaceAttributes=headPose,glasses'. Face attribute
         analysis has additional computational and time cost. Default value is None.
        :paramtype return_face_attributes: list[str or ~azure.ai.vision.face.models.FaceAttributeType]
        :keyword return_recognition_model: Return 'recognitionModel' or not. The default value is
         false. Default value is None.
        :paramtype return_recognition_model: bool
        :keyword face_id_time_to_live: The number of seconds for the face ID being cached. Supported
         range from 60 seconds up to 86400 seconds. The default value is 86400 (24 hours). Default value
         is None.
        :paramtype face_id_time_to_live: int
        :return: list of FaceDetectionResult
        :rtype: list[~azure.ai.vision.face.models.FaceDetectionResult]
        :raises ~azure.core.exceptions.HttpResponseError:

        Example:
            .. code-block:: python

                # JSON input template you can fill out and use as your body input.
                body = {
                    "url": "str"  # URL of input image. Required.
                }

                # response body for status code(s): 200
                response == [
                    {
                        "faceRectangle": {
                            "height": 0,  # The height of the rectangle, in pixels.
                              Required.
                            "left": 0,  # The distance from the left edge if the image to
                              the left edge of the rectangle, in pixels. Required.
                            "top": 0,  # The distance from the top edge if the image to
                              the top edge of the rectangle, in pixels. Required.
                            "width": 0  # The width of the rectangle, in pixels.
                              Required.
                        },
                        "faceAttributes": {
                            "accessories": [
                                {
                                    "confidence": 0.0,  # Confidence level of the
                                      accessory type. Range between [0,1]. Required.
                                    "type": "str"  # Type of the accessory.
                                      Required. Known values are: "headwear", "glasses", and "mask".
                                }
                            ],
                            "age": 0.0,  # Optional. Age in years.
                            "blur": {
                                "blurLevel": "str",  # An enum value indicating level
                                  of blurriness. Required. Known values are: "low", "medium", and
                                  "high".
                                "value": 0.0  # A number indicating level of
                                  blurriness ranging from 0 to 1. Required.
                            },
                            "exposure": {
                                "exposureLevel": "str",  # An enum value indicating
                                  level of exposure. Required. Known values are: "underExposure",
                                  "goodExposure", and "overExposure".
                                "value": 0.0  # A number indicating level of exposure
                                  level ranging from 0 to 1. [0, 0.25) is under exposure. [0.25, 0.75)
                                  is good exposure. [0.75, 1] is over exposure. Required.
                            },
                            "facialHair": {
                                "beard": 0.0,  # A number ranging from 0 to 1
                                  indicating a level of confidence associated with a property.
                                  Required.
                                "moustache": 0.0,  # A number ranging from 0 to 1
                                  indicating a level of confidence associated with a property.
                                  Required.
                                "sideburns": 0.0  # A number ranging from 0 to 1
                                  indicating a level of confidence associated with a property.
                                  Required.
                            },
                            "glasses": "str",  # Optional. Glasses type if any of the
                              face. Known values are: "noGlasses", "readingGlasses", "sunglasses", and
                              "swimmingGoggles".
                            "hair": {
                                "bald": 0.0,  # A number describing confidence level
                                  of whether the person is bald. Required.
                                "hairColor": [
                                    {
                                        "color": "str",  # Name of the hair
                                          color. Required. Known values are: "unknown", "white",
                                          "gray", "blond", "brown", "red", "black", and "other".
                                        "confidence": 0.0  # Confidence level
                                          of the color. Range between [0,1]. Required.
                                    }
                                ],
                                "invisible": bool  # A boolean value describing
                                  whether the hair is visible in the image. Required.
                            },
                            "headPose": {
                                "pitch": 0.0,  # Value of angles. Required.
                                "roll": 0.0,  # Value of angles. Required.
                                "yaw": 0.0  # Value of angles. Required.
                            },
                            "mask": {
                                "noseAndMouthCovered": bool,  # A boolean value
                                  indicating whether nose and mouth are covered. Required.
                                "type": "str"  # Type of the mask. Required. Known
                                  values are: "faceMask", "noMask", "otherMaskOrOcclusion", and
                                  "uncertain".
                            },
                            "noise": {
                                "noiseLevel": "str",  # An enum value indicating
                                  level of noise. Required. Known values are: "low", "medium", and
                                  "high".
                                "value": 0.0  # A number indicating level of noise
                                  level ranging from 0 to 1. [0, 0.25) is under exposure. [0.25, 0.75)
                                  is good exposure. [0.75, 1] is over exposure. [0, 0.3) is low noise
                                  level. [0.3, 0.7) is medium noise level. [0.7, 1] is high noise
                                  level. Required.
                            },
                            "occlusion": {
                                "eyeOccluded": bool,  # A boolean value indicating
                                  whether eyes are occluded. Required.
                                "foreheadOccluded": bool,  # A boolean value
                                  indicating whether forehead is occluded. Required.
                                "mouthOccluded": bool  # A boolean value indicating
                                  whether the mouth is occluded. Required.
                            },
                            "qualityForRecognition": "str",  # Optional. Properties
                              describing the overall image quality regarding whether the image being
                              used in the detection is of sufficient quality to attempt face
                              recognition on. Known values are: "low", "medium", and "high".
                            "smile": 0.0  # Optional. Smile intensity, a number between
                              [0,1].
                        },
                        "faceId": "str",  # Optional. Unique faceId of the detected face,
                          created by detection API and it will expire 24 hours after the detection
                          call. To return this, it requires 'returnFaceId' parameter to be true.
                        "faceLandmarks": {
                            "eyeLeftBottom": {
                                "x": 0.0,  # The horizontal component, in pixels.
                                  Required.
                                "y": 0.0  # The vertical component, in pixels.
                                  Required.
                            },
                            "eyeLeftInner": {
                                "x": 0.0,  # The horizontal component, in pixels.
                                  Required.
                                "y": 0.0  # The vertical component, in pixels.
                                  Required.
                            },
                            "eyeLeftOuter": {
                                "x": 0.0,  # The horizontal component, in pixels.
                                  Required.
                                "y": 0.0  # The vertical component, in pixels.
                                  Required.
                            },
                            "eyeLeftTop": {
                                "x": 0.0,  # The horizontal component, in pixels.
                                  Required.
                                "y": 0.0  # The vertical component, in pixels.
                                  Required.
                            },
                            "eyeRightBottom": {
                                "x": 0.0,  # The horizontal component, in pixels.
                                  Required.
                                "y": 0.0  # The vertical component, in pixels.
                                  Required.
                            },
                            "eyeRightInner": {
                                "x": 0.0,  # The horizontal component, in pixels.
                                  Required.
                                "y": 0.0  # The vertical component, in pixels.
                                  Required.
                            },
                            "eyeRightOuter": {
                                "x": 0.0,  # The horizontal component, in pixels.
                                  Required.
                                "y": 0.0  # The vertical component, in pixels.
                                  Required.
                            },
                            "eyeRightTop": {
                                "x": 0.0,  # The horizontal component, in pixels.
                                  Required.
                                "y": 0.0  # The vertical component, in pixels.
                                  Required.
                            },
                            "eyebrowLeftInner": {
                                "x": 0.0,  # The horizontal component, in pixels.
                                  Required.
                                "y": 0.0  # The vertical component, in pixels.
                                  Required.
                            },
                            "eyebrowLeftOuter": {
                                "x": 0.0,  # The horizontal component, in pixels.
                                  Required.
                                "y": 0.0  # The vertical component, in pixels.
                                  Required.
                            },
                            "eyebrowRightInner": {
                                "x": 0.0,  # The horizontal component, in pixels.
                                  Required.
                                "y": 0.0  # The vertical component, in pixels.
                                  Required.
                            },
                            "eyebrowRightOuter": {
                                "x": 0.0,  # The horizontal component, in pixels.
                                  Required.
                                "y": 0.0  # The vertical component, in pixels.
                                  Required.
                            },
                            "mouthLeft": {
                                "x": 0.0,  # The horizontal component, in pixels.
                                  Required.
                                "y": 0.0  # The vertical component, in pixels.
                                  Required.
                            },
                            "mouthRight": {
                                "x": 0.0,  # The horizontal component, in pixels.
                                  Required.
                                "y": 0.0  # The vertical component, in pixels.
                                  Required.
                            },
                            "noseLeftAlarOutTip": {
                                "x": 0.0,  # The horizontal component, in pixels.
                                  Required.
                                "y": 0.0  # The vertical component, in pixels.
                                  Required.
                            },
                            "noseLeftAlarTop": {
                                "x": 0.0,  # The horizontal component, in pixels.
                                  Required.
                                "y": 0.0  # The vertical component, in pixels.
                                  Required.
                            },
                            "noseRightAlarOutTip": {
                                "x": 0.0,  # The horizontal component, in pixels.
                                  Required.
                                "y": 0.0  # The vertical component, in pixels.
                                  Required.
                            },
                            "noseRightAlarTop": {
                                "x": 0.0,  # The horizontal component, in pixels.
                                  Required.
                                "y": 0.0  # The vertical component, in pixels.
                                  Required.
                            },
                            "noseRootLeft": {
                                "x": 0.0,  # The horizontal component, in pixels.
                                  Required.
                                "y": 0.0  # The vertical component, in pixels.
                                  Required.
                            },
                            "noseRootRight": {
                                "x": 0.0,  # The horizontal component, in pixels.
                                  Required.
                                "y": 0.0  # The vertical component, in pixels.
                                  Required.
                            },
                            "noseTip": {
                                "x": 0.0,  # The horizontal component, in pixels.
                                  Required.
                                "y": 0.0  # The vertical component, in pixels.
                                  Required.
                            },
                            "pupilLeft": {
                                "x": 0.0,  # The horizontal component, in pixels.
                                  Required.
                                "y": 0.0  # The vertical component, in pixels.
                                  Required.
                            },
                            "pupilRight": {
                                "x": 0.0,  # The horizontal component, in pixels.
                                  Required.
                                "y": 0.0  # The vertical component, in pixels.
                                  Required.
                            },
                            "underLipBottom": {
                                "x": 0.0,  # The horizontal component, in pixels.
                                  Required.
                                "y": 0.0  # The vertical component, in pixels.
                                  Required.
                            },
                            "underLipTop": {
                                "x": 0.0,  # The horizontal component, in pixels.
                                  Required.
                                "y": 0.0  # The vertical component, in pixels.
                                  Required.
                            },
                            "upperLipBottom": {
                                "x": 0.0,  # The horizontal component, in pixels.
                                  Required.
                                "y": 0.0  # The vertical component, in pixels.
                                  Required.
                            },
                            "upperLipTop": {
                                "x": 0.0,  # The horizontal component, in pixels.
                                  Required.
                                "y": 0.0  # The vertical component, in pixels.
                                  Required.
                            }
                        },
                        "recognitionModel": "str"  # Optional. The 'recognitionModel'
                          associated with this faceId. This is only returned when
                          'returnRecognitionModel' is explicitly set as true. Known values are:
                          "recognition_01", "recognition_02", "recognition_03", and "recognition_04".
                    }
                ]
        """
        return FaceClientOperationsMixin._detect_from_url(
            self,
            url=url,
            return_face_id=return_face_id,
            return_face_landmarks=return_face_landmarks,
            return_face_attributes=return_face_attributes,
            recognition_model=recognition_model,
            return_recognition_model=return_recognition_model,
            detection_model=detection_model,
            face_id_time_to_live=face_id_time_to_live,
            **kwargs)

    @distributed_trace
    def detect(
        self,
        image_content: bytes,
        detection_model: Union[str, _models.FaceDetectionModel] = None,
        recognition_model: Union[str, _models.FaceRecognitionModel] = None,
        *,
        return_face_id: Optional[bool] = False,
        return_face_landmarks: Optional[bool] = None,
        return_face_attributes: Optional[List[Union[str, _models.FaceAttributeType]]] = None,
        return_recognition_model: Optional[bool] = None,
        face_id_time_to_live: Optional[int] = None,
        **kwargs: Any,
    ) -> List[_models._models.FaceDetectionResult]:
        # pylint: disable=line-too-long
        """Detect human faces in an image, return face rectangles, and optionally with faceIds, landmarks,
        and attributes.

        ..

           [!IMPORTANT]
           To mitigate potential misuse that can subject people to stereotyping, discrimination, or
        unfair denial of services, we are retiring Face API attributes that predict emotion, gender,
        age, smile, facial hair, hair, and makeup. Read more about this decision
        https://azure.microsoft.com/en-us/blog/responsible-ai-investments-and-safeguards-for-facial-recognition/.


        *


        * No image will be stored. Only the extracted face feature(s) will be stored on server. The
        faceId is an identifier of the face feature and will be used in Face - Identify, Face - Verify,
        and Face - Find Similar. The stored face features will expire and be deleted at the time
        specified by faceIdTimeToLive after the original detection call.
        * Optional parameters include faceId, landmarks, and attributes. Attributes include headPose,
        glasses, occlusion, accessories, blur, exposure, noise, mask, and qualityForRecognition. Some
        of the results returned for specific attributes may not be highly accurate.
        * JPEG, PNG, GIF (the first frame), and BMP format are supported. The allowed image file size
        is from 1KB to 6MB.
        * The minimum detectable face size is 36x36 pixels in an image no larger than 1920x1080 pixels.
        Images with dimensions higher than 1920x1080 pixels will need a proportionally larger minimum
        face size.
        * Up to 100 faces can be returned for an image. Faces are ranked by face rectangle size from
        large to small.
        * For optimal results when querying Face - Identify, Face - Verify, and Face - Find Similar
        ('returnFaceId' is true), please use faces that are: frontal, clear, and with a minimum size of
        200x200 pixels (100 pixels between eyes).
        * Different 'detectionModel' values can be provided. To use and compare different detection
        models, please refer to
        https://learn.microsoft.com/en-us/azure/ai-services/computer-vision/how-to/specify-detection-model

          * 'detection_02': Face attributes and landmarks are disabled if you choose this detection
        model.
          * 'detection_03': Face attributes (mask and headPose only) and landmarks are supported if you
        choose this detection model.

        * Different 'recognitionModel' values are provided. If follow-up operations like Verify,
        Identify, Find Similar are needed, please specify the recognition model with 'recognitionModel'
        parameter. The default value for 'recognitionModel' is 'recognition_01', if latest model
        needed, please explicitly specify the model you need in this parameter. Once specified, the
        detected faceIds will be associated with the specified recognition model. More details, please
        refer to
        https://learn.microsoft.com/en-us/azure/ai-services/computer-vision/how-to/specify-recognition-model.

        :param image_content: The input image binary. Required.
        :type image_content: bytes
        :param detection_model: The 'detectionModel' associated with the detected faceIds. Supported
         'detectionModel' values include 'detection_01', 'detection_02' and 'detection_03'. The default
         value is 'detection_01'. Known values are: "detection_01", "detection_02", and "detection_03".
         Required.
        :type detection_model: str or ~azure.ai.vision.face.models.FaceDetectionModel
        :param recognition_model: The 'recognitionModel' associated with the detected faceIds.
         Supported 'recognitionModel' values include 'recognition_01', 'recognition_02',
         'recognition_03' or 'recognition_04'. The default value is 'recognition_01'. 'recognition_04'
         is recommended since its accuracy is improved on faces wearing masks compared with
         'recognition_03', and its overall accuracy is improved compared with 'recognition_01' and
         'recognition_02'. Known values are: "recognition_01", "recognition_02", "recognition_03", and
         "recognition_04". Required.
        :type recognition_model: str or ~azure.ai.vision.face.models.FaceRecognitionModel
        :keyword return_face_id: Return faceIds of the detected faces or not. The default value is
         true. Default value is False.
        :paramtype return_face_id: bool
        :keyword return_face_landmarks: Return face landmarks of the detected faces or not. The default
         value is false. Default value is None.
        :paramtype return_face_landmarks: bool
        :keyword return_face_attributes: Analyze and return the one or more specified face attributes
         in the comma-separated string like 'returnFaceAttributes=headPose,glasses'. Face attribute
         analysis has additional computational and time cost. Default value is None.
        :paramtype return_face_attributes: list[str or ~azure.ai.vision.face.models.FaceAttributeType]
        :keyword return_recognition_model: Return 'recognitionModel' or not. The default value is
         false. Default value is None.
        :paramtype return_recognition_model: bool
        :keyword face_id_time_to_live: The number of seconds for the face ID being cached. Supported
         range from 60 seconds up to 86400 seconds. The default value is 86400 (24 hours). Default value
         is None.
        :paramtype face_id_time_to_live: int
        :return: list of FaceDetectionResult
        :rtype: list[~azure.ai.vision.face.models.FaceDetectionResult]
        :raises ~azure.core.exceptions.HttpResponseError:

        Example:
            .. code-block:: python

                # response body for status code(s): 200
                response == [
                    {
                        "faceRectangle": {
                            "height": 0,  # The height of the rectangle, in pixels.
                              Required.
                            "left": 0,  # The distance from the left edge if the image to
                              the left edge of the rectangle, in pixels. Required.
                            "top": 0,  # The distance from the top edge if the image to
                              the top edge of the rectangle, in pixels. Required.
                            "width": 0  # The width of the rectangle, in pixels.
                              Required.
                        },
                        "faceAttributes": {
                            "accessories": [
                                {
                                    "confidence": 0.0,  # Confidence level of the
                                      accessory type. Range between [0,1]. Required.
                                    "type": "str"  # Type of the accessory.
                                      Required. Known values are: "headwear", "glasses", and "mask".
                                }
                            ],
                            "age": 0.0,  # Optional. Age in years.
                            "blur": {
                                "blurLevel": "str",  # An enum value indicating level
                                  of blurriness. Required. Known values are: "low", "medium", and
                                  "high".
                                "value": 0.0  # A number indicating level of
                                  blurriness ranging from 0 to 1. Required.
                            },
                            "exposure": {
                                "exposureLevel": "str",  # An enum value indicating
                                  level of exposure. Required. Known values are: "underExposure",
                                  "goodExposure", and "overExposure".
                                "value": 0.0  # A number indicating level of exposure
                                  level ranging from 0 to 1. [0, 0.25) is under exposure. [0.25, 0.75)
                                  is good exposure. [0.75, 1] is over exposure. Required.
                            },
                            "facialHair": {
                                "beard": 0.0,  # A number ranging from 0 to 1
                                  indicating a level of confidence associated with a property.
                                  Required.
                                "moustache": 0.0,  # A number ranging from 0 to 1
                                  indicating a level of confidence associated with a property.
                                  Required.
                                "sideburns": 0.0  # A number ranging from 0 to 1
                                  indicating a level of confidence associated with a property.
                                  Required.
                            },
                            "glasses": "str",  # Optional. Glasses type if any of the
                              face. Known values are: "noGlasses", "readingGlasses", "sunglasses", and
                              "swimmingGoggles".
                            "hair": {
                                "bald": 0.0,  # A number describing confidence level
                                  of whether the person is bald. Required.
                                "hairColor": [
                                    {
                                        "color": "str",  # Name of the hair
                                          color. Required. Known values are: "unknown", "white",
                                          "gray", "blond", "brown", "red", "black", and "other".
                                        "confidence": 0.0  # Confidence level
                                          of the color. Range between [0,1]. Required.
                                    }
                                ],
                                "invisible": bool  # A boolean value describing
                                  whether the hair is visible in the image. Required.
                            },
                            "headPose": {
                                "pitch": 0.0,  # Value of angles. Required.
                                "roll": 0.0,  # Value of angles. Required.
                                "yaw": 0.0  # Value of angles. Required.
                            },
                            "mask": {
                                "noseAndMouthCovered": bool,  # A boolean value
                                  indicating whether nose and mouth are covered. Required.
                                "type": "str"  # Type of the mask. Required. Known
                                  values are: "faceMask", "noMask", "otherMaskOrOcclusion", and
                                  "uncertain".
                            },
                            "noise": {
                                "noiseLevel": "str",  # An enum value indicating
                                  level of noise. Required. Known values are: "low", "medium", and
                                  "high".
                                "value": 0.0  # A number indicating level of noise
                                  level ranging from 0 to 1. [0, 0.25) is under exposure. [0.25, 0.75)
                                  is good exposure. [0.75, 1] is over exposure. [0, 0.3) is low noise
                                  level. [0.3, 0.7) is medium noise level. [0.7, 1] is high noise
                                  level. Required.
                            },
                            "occlusion": {
                                "eyeOccluded": bool,  # A boolean value indicating
                                  whether eyes are occluded. Required.
                                "foreheadOccluded": bool,  # A boolean value
                                  indicating whether forehead is occluded. Required.
                                "mouthOccluded": bool  # A boolean value indicating
                                  whether the mouth is occluded. Required.
                            },
                            "qualityForRecognition": "str",  # Optional. Properties
                              describing the overall image quality regarding whether the image being
                              used in the detection is of sufficient quality to attempt face
                              recognition on. Known values are: "low", "medium", and "high".
                            "smile": 0.0  # Optional. Smile intensity, a number between
                              [0,1].
                        },
                        "faceId": "str",  # Optional. Unique faceId of the detected face,
                          created by detection API and it will expire 24 hours after the detection
                          call. To return this, it requires 'returnFaceId' parameter to be true.
                        "faceLandmarks": {
                            "eyeLeftBottom": {
                                "x": 0.0,  # The horizontal component, in pixels.
                                  Required.
                                "y": 0.0  # The vertical component, in pixels.
                                  Required.
                            },
                            "eyeLeftInner": {
                                "x": 0.0,  # The horizontal component, in pixels.
                                  Required.
                                "y": 0.0  # The vertical component, in pixels.
                                  Required.
                            },
                            "eyeLeftOuter": {
                                "x": 0.0,  # The horizontal component, in pixels.
                                  Required.
                                "y": 0.0  # The vertical component, in pixels.
                                  Required.
                            },
                            "eyeLeftTop": {
                                "x": 0.0,  # The horizontal component, in pixels.
                                  Required.
                                "y": 0.0  # The vertical component, in pixels.
                                  Required.
                            },
                            "eyeRightBottom": {
                                "x": 0.0,  # The horizontal component, in pixels.
                                  Required.
                                "y": 0.0  # The vertical component, in pixels.
                                  Required.
                            },
                            "eyeRightInner": {
                                "x": 0.0,  # The horizontal component, in pixels.
                                  Required.
                                "y": 0.0  # The vertical component, in pixels.
                                  Required.
                            },
                            "eyeRightOuter": {
                                "x": 0.0,  # The horizontal component, in pixels.
                                  Required.
                                "y": 0.0  # The vertical component, in pixels.
                                  Required.
                            },
                            "eyeRightTop": {
                                "x": 0.0,  # The horizontal component, in pixels.
                                  Required.
                                "y": 0.0  # The vertical component, in pixels.
                                  Required.
                            },
                            "eyebrowLeftInner": {
                                "x": 0.0,  # The horizontal component, in pixels.
                                  Required.
                                "y": 0.0  # The vertical component, in pixels.
                                  Required.
                            },
                            "eyebrowLeftOuter": {
                                "x": 0.0,  # The horizontal component, in pixels.
                                  Required.
                                "y": 0.0  # The vertical component, in pixels.
                                  Required.
                            },
                            "eyebrowRightInner": {
                                "x": 0.0,  # The horizontal component, in pixels.
                                  Required.
                                "y": 0.0  # The vertical component, in pixels.
                                  Required.
                            },
                            "eyebrowRightOuter": {
                                "x": 0.0,  # The horizontal component, in pixels.
                                  Required.
                                "y": 0.0  # The vertical component, in pixels.
                                  Required.
                            },
                            "mouthLeft": {
                                "x": 0.0,  # The horizontal component, in pixels.
                                  Required.
                                "y": 0.0  # The vertical component, in pixels.
                                  Required.
                            },
                            "mouthRight": {
                                "x": 0.0,  # The horizontal component, in pixels.
                                  Required.
                                "y": 0.0  # The vertical component, in pixels.
                                  Required.
                            },
                            "noseLeftAlarOutTip": {
                                "x": 0.0,  # The horizontal component, in pixels.
                                  Required.
                                "y": 0.0  # The vertical component, in pixels.
                                  Required.
                            },
                            "noseLeftAlarTop": {
                                "x": 0.0,  # The horizontal component, in pixels.
                                  Required.
                                "y": 0.0  # The vertical component, in pixels.
                                  Required.
                            },
                            "noseRightAlarOutTip": {
                                "x": 0.0,  # The horizontal component, in pixels.
                                  Required.
                                "y": 0.0  # The vertical component, in pixels.
                                  Required.
                            },
                            "noseRightAlarTop": {
                                "x": 0.0,  # The horizontal component, in pixels.
                                  Required.
                                "y": 0.0  # The vertical component, in pixels.
                                  Required.
                            },
                            "noseRootLeft": {
                                "x": 0.0,  # The horizontal component, in pixels.
                                  Required.
                                "y": 0.0  # The vertical component, in pixels.
                                  Required.
                            },
                            "noseRootRight": {
                                "x": 0.0,  # The horizontal component, in pixels.
                                  Required.
                                "y": 0.0  # The vertical component, in pixels.
                                  Required.
                            },
                            "noseTip": {
                                "x": 0.0,  # The horizontal component, in pixels.
                                  Required.
                                "y": 0.0  # The vertical component, in pixels.
                                  Required.
                            },
                            "pupilLeft": {
                                "x": 0.0,  # The horizontal component, in pixels.
                                  Required.
                                "y": 0.0  # The vertical component, in pixels.
                                  Required.
                            },
                            "pupilRight": {
                                "x": 0.0,  # The horizontal component, in pixels.
                                  Required.
                                "y": 0.0  # The vertical component, in pixels.
                                  Required.
                            },
                            "underLipBottom": {
                                "x": 0.0,  # The horizontal component, in pixels.
                                  Required.
                                "y": 0.0  # The vertical component, in pixels.
                                  Required.
                            },
                            "underLipTop": {
                                "x": 0.0,  # The horizontal component, in pixels.
                                  Required.
                                "y": 0.0  # The vertical component, in pixels.
                                  Required.
                            },
                            "upperLipBottom": {
                                "x": 0.0,  # The horizontal component, in pixels.
                                  Required.
                                "y": 0.0  # The vertical component, in pixels.
                                  Required.
                            },
                            "upperLipTop": {
                                "x": 0.0,  # The horizontal component, in pixels.
                                  Required.
                                "y": 0.0  # The vertical component, in pixels.
                                  Required.
                            }
                        },
                        "recognitionModel": "str"  # Optional. The 'recognitionModel'
                          associated with this faceId. This is only returned when
                          'returnRecognitionModel' is explicitly set as true. Known values are:
                          "recognition_01", "recognition_02", "recognition_03", and "recognition_04".
                    }
                ]
        """
        return FaceClientOperationsMixin._detect(
            self,
            image_content=image_content,
            return_face_id=return_face_id,
            return_face_landmarks=return_face_landmarks,
            return_face_attributes=return_face_attributes,
            recognition_model=recognition_model,
            return_recognition_model=return_recognition_model,
            detection_model=detection_model,
            face_id_time_to_live=face_id_time_to_live,
            **kwargs)


class FaceSessionClient(FaceSessionClientGenerated):
    """FaceSessionClient.

    :param endpoint: Supported Cognitive Services endpoints (protocol and hostname, for example:
     https://{resource-name}.cognitiveservices.azure.com). Required.
    :type endpoint: str
    :param credential: Credential used to authenticate requests to the service. Is either a
     AzureKeyCredential type or a TokenCredential type. Required.
    :type credential: ~azure.core.credentials.AzureKeyCredential or
     ~azure.core.credentials.TokenCredential
    :keyword api_version: API Version. Default value is "v1.1-preview.1". Note that overriding this
     default value may result in unsupported behavior.
    :paramtype api_version: str or ~azure.ai.vision.face.models.Versions
    """

    # TODO
    @distributed_trace
    def create_liveness_with_verify_session(
        self, body: Union[_models.LivenessSessionCreationContent, JSON, IO[bytes]], **kwargs: Any
    ) -> _models.LivenessSessionCreationResult:
        # pylint: disable=line-too-long
        """Create a new liveness session with verify. Client device submits VerifyImage during the
        /detectLivenessWithVerify/singleModal call.

        A session is best for client device scenarios where developers want to authorize a client
        device to perform only a liveness detection without granting full access to their resource.
        Created sessions have a limited life span and only authorize clients to perform the desired
        action before access is expired.

        Permissions includes...
        >
        *


        * Ability to call /detectLivenessWithVerify/singleModal for up to 3 retries.
        * A token lifetime of 10 minutes.

        ..

           [!NOTE]

           *


           * Client access can be revoked by deleting the session using the Delete Liveness With Verify
        Session operation.
           * To retrieve a result, use the Get Liveness With Verify Session.
           * To audit the individual requests that a client has made to your resource, use the List
        Liveness With Verify Session Audit Entries.


        Alternative Option: Client device submits VerifyImage during the
        /detectLivenessWithVerify/singleModal call.

        ..

           [!NOTE]
           Extra measures should be taken to validate that the client is sending the expected
        VerifyImage.

        :param body: Is one of the following types: LivenessSessionCreationContent, JSON, IO[bytes]
         Required.
        :type body: ~azure.ai.vision.face.models.LivenessSessionCreationContent or JSON or IO[bytes]
        :return: LivenessSessionCreationResult. The LivenessSessionCreationResult is compatible with
         MutableMapping
        :rtype: ~azure.ai.vision.face.models.LivenessSessionCreationResult
        :raises ~azure.core.exceptions.HttpResponseError:

        Example:
            .. code-block:: python

                # JSON input template you can fill out and use as your body input.
                body = {
                    "livenessOperationMode": "str",  # Type of liveness mode the client should
                      follow. Required. "Passive"
                    "authTokenTimeToLiveInSeconds": 0,  # Optional. Seconds the session should
                      last for. Range is 60 to 86400 seconds. Default value is 600.
                    "deviceCorrelationId": "str",  # Optional. Unique Guid per each end-user
                      device. This is to provide rate limiting and anti-hammering. If
                      'deviceCorrelationIdSetInClient' is true in this request, this
                      'deviceCorrelationId' must be null.
                    "deviceCorrelationIdSetInClient": bool,  # Optional. Whether or not to allow
                      client to set their own 'deviceCorrelationId' via the Vision SDK. Default is
                      false, and 'deviceCorrelationId' must be set in this request body.
                    "sendResultsToClient": bool  # Optional. Whether or not to allow a '200 -
                      Success' response body to be sent to the client, which may be undesirable for
                      security reasons. Default is false, clients will receive a '204 - NoContent'
                      empty body response. Regardless of selection, calling Session GetResult will
                      always contain a response body enabling business logic to be implemented.
                }

                # response body for status code(s): 200
                response == {
                    "authToken": "str",  # Bearer token to provide authentication for the Vision
                      SDK running on a client application. This Bearer token has limited permissions to
                      perform only the required action and expires after the TTL time. It is also
                      auditable. Required.
                    "sessionId": "str"  # The unique session ID of the created session. It will
                      expire 48 hours after it was created or may be deleted sooner using the
                      corresponding Session DELETE operation. Required.
                }
        """
        # TODO
        return FaceSessionClientOperationsMixin._create_liveness_with_verify_session(
            self, body, **kwargs)

    # TODO
    @distributed_trace
    def create_liveness_with_verify_session_with_verify_image(  # pylint: disable=protected-access,name-too-long
        self, body: Union[_models._models.LivenessSessionWithVerifyImageCreationContent, JSON], **kwargs: Any
    ) -> _models._models.LivenessSessionWithVerifyCreationResult:
        # pylint: disable=line-too-long
        """Create a new liveness session with verify. Provide the verify image during session creation.

        A session is best for client device scenarios where developers want to authorize a client
        device to perform only a liveness detection without granting full access to their resource.
        Created sessions have a limited life span and only authorize clients to perform the desired
        action before access is expired.

        Permissions includes...
        >
        *


        * Ability to call /detectLivenessWithVerify/singleModal for up to 3 retries.
        * A token lifetime of 10 minutes.

        ..

           [!NOTE]

           *


           * Client access can be revoked by deleting the session using the Delete Liveness With Verify
        Session operation.
           * To retrieve a result, use the Get Liveness With Verify Session.
           * To audit the individual requests that a client has made to your resource, use the List
        Liveness With Verify Session Audit Entries.


        Recommended Option: VerifyImage is provided during session creation.

        :param body: Is either a LivenessSessionWithVerifyImageCreationContent type or a JSON type.
         Required.
        :type body: ~azure.ai.vision.face.models.LivenessSessionWithVerifyImageCreationContent or JSON
        :return: LivenessSessionWithVerifyCreationResult. The LivenessSessionWithVerifyCreationResult
         is compatible with MutableMapping
        :rtype: ~azure.ai.vision.face.models.LivenessSessionWithVerifyCreationResult
        :raises ~azure.core.exceptions.HttpResponseError:

        Example:
            .. code-block:: python

                # JSON input template you can fill out and use as your body input.
                body = {
                    "Parameters": {
                        "livenessOperationMode": "str",  # Type of liveness mode the client
                          should follow. Required. "Passive"
                        "authTokenTimeToLiveInSeconds": 0,  # Optional. Seconds the session
                          should last for. Range is 60 to 86400 seconds. Default value is 600.
                        "deviceCorrelationId": "str",  # Optional. Unique Guid per each
                          end-user device. This is to provide rate limiting and anti-hammering. If
                          'deviceCorrelationIdSetInClient' is true in this request, this
                          'deviceCorrelationId' must be null.
                        "deviceCorrelationIdSetInClient": bool,  # Optional. Whether or not
                          to allow client to set their own 'deviceCorrelationId' via the Vision SDK.
                          Default is false, and 'deviceCorrelationId' must be set in this request body.
                        "sendResultsToClient": bool  # Optional. Whether or not to allow a
                          '200 - Success' response body to be sent to the client, which may be
                          undesirable for security reasons. Default is false, clients will receive a
                          '204 - NoContent' empty body response. Regardless of selection, calling
                          Session GetResult will always contain a response body enabling business logic
                          to be implemented.
                    },
                    "VerifyImage": filetype
                }

                # response body for status code(s): 200
                response == {
                    "authToken": "str",  # Bearer token to provide authentication for the Vision
                      SDK running on a client application. This Bearer token has limited permissions to
                      perform only the required action and expires after the TTL time. It is also
                      auditable. Required.
                    "sessionId": "str",  # The unique session ID of the created session. It will
                      expire 48 hours after it was created or may be deleted sooner using the
                      corresponding Session DELETE operation. Required.
                    "verifyImage": {
                        "faceRectangle": {
                            "height": 0,  # The height of the rectangle, in pixels.
                              Required.
                            "left": 0,  # The distance from the left edge if the image to
                              the left edge of the rectangle, in pixels. Required.
                            "top": 0,  # The distance from the top edge if the image to
                              the top edge of the rectangle, in pixels. Required.
                            "width": 0  # The width of the rectangle, in pixels.
                              Required.
                        },
                        "qualityForRecognition": "str"  # Quality of face image for
                          recognition. Required. Known values are: "low", "medium", and "high".
                    }
                }
        """
        # TODO
        return FaceSessionClientOperationsMixin._create_liveness_with_verify_session_with_verify_image(
            self, body, **kwargs)


__all__: List[str] = [
    "FaceAdministrationClient",
    "FaceClient",
    "FaceSessionClient",
]  # Add all objects you want publicly available to users at this package level


def patch_sdk():
    """Do not remove from this file.

    `patch_sdk` is a last resort escape hatch that allows you to do customizations
    you can't accomplish using the techniques described in
    https://aka.ms/azsdk/python/dpcodegen/python/customize
    """
