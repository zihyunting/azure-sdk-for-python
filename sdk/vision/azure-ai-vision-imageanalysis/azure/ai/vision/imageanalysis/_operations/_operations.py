# pylint: disable=too-many-lines,too-many-statements
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from io import IOBase
import json
import sys
from typing import Any, Callable, Dict, IO, List, Optional, TypeVar, Union, overload

from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    ResourceNotModifiedError,
    map_error,
)
from azure.core.pipeline import PipelineResponse
from azure.core.rest import HttpRequest, HttpResponse
from azure.core.tracing.decorator import distributed_trace
from azure.core.utils import case_insensitive_dict

from .. import models as _models
from .._model_base import SdkJSONEncoder, _deserialize
from .._serialization import Serializer
from .._vendor import ImageAnalysisClientMixinABC

if sys.version_info >= (3, 9):
    from collections.abc import MutableMapping
else:
    from typing import MutableMapping  # type: ignore  # pylint: disable=ungrouped-imports
JSON = MutableMapping[str, Any]  # pylint: disable=unsubscriptable-object
T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False


def build_image_analysis_analyze_from_image_data_request(  # pylint: disable=name-too-long
    *,
    visual_features: List[Union[str, _models.VisualFeatures]],
    language: Optional[str] = None,
    gender_neutral_caption: Optional[bool] = None,
    smart_crops_aspect_ratios: Optional[List[float]] = None,
    model_version: Optional[str] = None,
    **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    content_type: str = kwargs.pop("content_type")
    api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2023-10-01"))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = "/imageanalysis:analyze"

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")
    _params["features"] = _SERIALIZER.query("visual_features", visual_features, "[str]", div=",")
    if language is not None:
        _params["language"] = _SERIALIZER.query("language", language, "str")
    if gender_neutral_caption is not None:
        _params["gender-neutral-caption"] = _SERIALIZER.query("gender_neutral_caption", gender_neutral_caption, "bool")
    if smart_crops_aspect_ratios is not None:
        _params["smartcrops-aspect-ratios"] = _SERIALIZER.query(
            "smart_crops_aspect_ratios", smart_crops_aspect_ratios, "[float]", div=","
        )
    if model_version is not None:
        _params["model-version"] = _SERIALIZER.query("model_version", model_version, "str")

    # Construct headers
    _headers["content-type"] = _SERIALIZER.header("content_type", content_type, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="POST", url=_url, params=_params, headers=_headers, **kwargs)


def build_image_analysis_analyze_from_url_request(  # pylint: disable=name-too-long
    *,
    visual_features: List[Union[str, _models.VisualFeatures]],
    language: Optional[str] = None,
    gender_neutral_caption: Optional[bool] = None,
    smart_crops_aspect_ratios: Optional[List[float]] = None,
    model_version: Optional[str] = None,
    **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("content-type", None))
    api_version: str = kwargs.pop("api_version", _params.pop("api-version", "2023-10-01"))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = "/imageanalysis:analyze"

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")
    _params["features"] = _SERIALIZER.query("visual_features", visual_features, "[str]", div=",")
    if language is not None:
        _params["language"] = _SERIALIZER.query("language", language, "str")
    if gender_neutral_caption is not None:
        _params["gender-neutral-caption"] = _SERIALIZER.query("gender_neutral_caption", gender_neutral_caption, "bool")
    if smart_crops_aspect_ratios is not None:
        _params["smartcrops-aspect-ratios"] = _SERIALIZER.query(
            "smart_crops_aspect_ratios", smart_crops_aspect_ratios, "[float]", div=","
        )
    if model_version is not None:
        _params["model-version"] = _SERIALIZER.query("model_version", model_version, "str")

    # Construct headers
    if content_type is not None:
        _headers["content-type"] = _SERIALIZER.header("content_type", content_type, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="POST", url=_url, params=_params, headers=_headers, **kwargs)


class ImageAnalysisClientOperationsMixin(ImageAnalysisClientMixinABC):
    @distributed_trace
    def _analyze_from_image_data(
        self,
        image_data: bytes,
        *,
        visual_features: List[Union[str, _models.VisualFeatures]],
        language: Optional[str] = None,
        gender_neutral_caption: Optional[bool] = None,
        smart_crops_aspect_ratios: Optional[List[float]] = None,
        model_version: Optional[str] = None,
        **kwargs: Any
    ) -> _models.ImageAnalysisResult:
        # pylint: disable=line-too-long
        """Performs a single Image Analysis operation.

        :param image_data: The image to be analyzed. Required.
        :type image_data: bytes
        :keyword visual_features: A list of visual features to analyze.
         Seven visual features are supported: Caption, DenseCaptions, Read (OCR), Tags, Objects,
         SmartCrops, and People.
         At least one visual feature must be specified. Required.
        :paramtype visual_features: list[str or ~azure.ai.vision.imageanalysis.models.VisualFeatures]
        :keyword language: The desired language for result generation (a two-letter language code).
         If this option is not specified, the default value 'en' is used (English).
         See https://aka.ms/cv-languages for a list of supported languages. Default value is None.
        :paramtype language: str
        :keyword gender_neutral_caption: Boolean flag for enabling gender-neutral captioning for
         Caption and Dense Captions features.
         By default captions may contain gender terms (for example: 'man', 'woman', or 'boy', 'girl').
         If you set this to "true", those will be replaced with gender-neutral terms (for example:
         'person' or 'child'). Default value is None.
        :paramtype gender_neutral_caption: bool
        :keyword smart_crops_aspect_ratios: A list of aspect ratios to use for smart cropping.
         Aspect ratios are calculated by dividing the target crop width in pixels by the height in
         pixels.
         Supported values are between 0.75 and 1.8 (inclusive).
         If this parameter is not specified, the service will return one crop region with an aspect
         ratio it sees fit between 0.5 and 2.0 (inclusive). Default value is None.
        :paramtype smart_crops_aspect_ratios: list[float]
        :keyword model_version: The version of cloud AI-model used for analysis.
         The format is the following: 'latest' (default value) or 'YYYY-MM-DD' or 'YYYY-MM-DD-preview',
         where 'YYYY', 'MM', 'DD' are the year, month and day associated with the model.
         This is not commonly set, as the default always gives the latest AI model with recent
         improvements.
         If however you would like to make sure analysis results do not change over time, set this
         value to a specific model version. Default value is None.
        :paramtype model_version: str
        :return: ImageAnalysisResult. The ImageAnalysisResult is compatible with MutableMapping
        :rtype: ~azure.ai.vision.imageanalysis.models.ImageAnalysisResult
        :raises ~azure.core.exceptions.HttpResponseError:

        Example:
            .. code-block:: python

                # response body for status code(s): 200
                response == {
                    "metadata": {
                        "height": 0,  # The height of the image in pixels. Required.
                        "width": 0  # The width of the image in pixels. Required.
                    },
                    "modelVersion": "str",  # The cloud AI model used for the analysis. Required.
                    "captionResult": {
                        "confidence": 0.0,  # A score, in the range of 0 to 1 (inclusive),
                          representing the confidence that this description is accurate. Higher values
                          indicating higher confidence. Required.
                        "text": "str"  # The text of the caption. Required.
                    },
                    "denseCaptionsResult": {
                        "values": [
                            {
                                "boundingBox": {
                                    "h": 0,  # Height of the area, in pixels.
                                      Required.
                                    "w": 0,  # Width of the area, in pixels.
                                      Required.
                                    "x": 0,  # X-coordinate of the top left point
                                      of the area, in pixels. Required.
                                    "y": 0  # Y-coordinate of the top left point
                                      of the area, in pixels. Required.
                                },
                                "confidence": 0.0,  # A score, in the range of 0 to 1
                                  (inclusive), representing the confidence that this description is
                                  accurate. Higher values indicating higher confidence. Required.
                                "text": "str"  # The text of the caption. Required.
                            }
                        ]
                    },
                    "objectsResult": {
                        "values": [
                            {
                                "boundingBox": {
                                    "h": 0,  # Height of the area, in pixels.
                                      Required.
                                    "w": 0,  # Width of the area, in pixels.
                                      Required.
                                    "x": 0,  # X-coordinate of the top left point
                                      of the area, in pixels. Required.
                                    "y": 0  # Y-coordinate of the top left point
                                      of the area, in pixels. Required.
                                },
                                "tags": [
                                    {
                                        "confidence": 0.0,  # A score, in the
                                          range of 0 to 1 (inclusive), representing the confidence that
                                          this entity was observed. Higher values indicating higher
                                          confidence. Required.
                                        "name": "str"  # Name of the entity.
                                          Required.
                                    }
                                ]
                            }
                        ]
                    },
                    "peopleResult": {
                        "values": [
                            {
                                "boundingBox": {
                                    "h": 0,  # Height of the area, in pixels.
                                      Required.
                                    "w": 0,  # Width of the area, in pixels.
                                      Required.
                                    "x": 0,  # X-coordinate of the top left point
                                      of the area, in pixels. Required.
                                    "y": 0  # Y-coordinate of the top left point
                                      of the area, in pixels. Required.
                                },
                                "confidence": 0.0  # A score, in the range of 0 to 1
                                  (inclusive), representing the confidence that this detection was
                                  accurate. Higher values indicating higher confidence. Required.
                            }
                        ]
                    },
                    "readResult": {
                        "blocks": [
                            {
                                "lines": [
                                    {
                                        "boundingPolygon": [
                                            {
                                                "x": 0,  # The
                                                  horizontal x-coordinate of this point, in pixels.
                                                  Zero values corresponds to the left-most pixels in
                                                  the image. Required.
                                                "y": 0  # The
                                                  vertical y-coordinate of this point, in pixels. Zero
                                                  values corresponds to the top-most pixels in the
                                                  image. Required.
                                            }
                                        ],
                                        "text": "str",  # Text content of the
                                          detected text line. Required.
                                        "words": [
                                            {
                                                "boundingPolygon": [
                                                    {
                                                        "x":
                                                          0,  # The horizontal x-coordinate of this
                                                          point, in pixels. Zero values corresponds to
                                                          the left-most pixels in the image. Required.
                                                        "y":
                                                          0  # The vertical y-coordinate of this point,
                                                          in pixels. Zero values corresponds to the
                                                          top-most pixels in the image. Required.
                                                    }
                                                ],
                                                "confidence": 0.0,  #
                                                  The level of confidence that the word was detected.
                                                  Confidence scores span the range of 0.0 to 1.0
                                                  (inclusive), with higher values indicating a higher
                                                  confidence of detection. Required.
                                                "text": "str"  # Text
                                                  content of the word. Required.
                                            }
                                        ]
                                    }
                                ]
                            }
                        ]
                    },
                    "smartCropsResult": {
                        "values": [
                            {
                                "aspectRatio": 0.0,  # The aspect ratio of the crop
                                  region. Aspect ratio is calculated by dividing the width of the
                                  region in pixels by its height in pixels. The aspect ratio will be in
                                  the range 0.75 to 1.8 (inclusive) if provided by the developer during
                                  the analyze call. Otherwise, it will be in the range 0.5 to 2.0
                                  (inclusive). Required.
                                "boundingBox": {
                                    "h": 0,  # Height of the area, in pixels.
                                      Required.
                                    "w": 0,  # Width of the area, in pixels.
                                      Required.
                                    "x": 0,  # X-coordinate of the top left point
                                      of the area, in pixels. Required.
                                    "y": 0  # Y-coordinate of the top left point
                                      of the area, in pixels. Required.
                                }
                            }
                        ]
                    },
                    "tagsResult": {
                        "values": [
                            {
                                "confidence": 0.0,  # A score, in the range of 0 to 1
                                  (inclusive), representing the confidence that this entity was
                                  observed. Higher values indicating higher confidence. Required.
                                "name": "str"  # Name of the entity. Required.
                            }
                        ]
                    }
                }
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = kwargs.pop("params", {}) or {}

        content_type: str = kwargs.pop("content_type", _headers.pop("content-type", "application/octet-stream"))
        cls: ClsType[_models.ImageAnalysisResult] = kwargs.pop("cls", None)

        _content = image_data

        _request = build_image_analysis_analyze_from_image_data_request(
            visual_features=visual_features,
            language=language,
            gender_neutral_caption=gender_neutral_caption,
            smart_crops_aspect_ratios=smart_crops_aspect_ratios,
            model_version=model_version,
            content_type=content_type,
            api_version=self._config.api_version,
            content=_content,
            headers=_headers,
            params=_params,
        )
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        _request.url = self._client.format_url(_request.url, **path_format_arguments)

        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            if _stream:
                response.read()  # Load the body in memory and close the socket
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if _stream:
            deserialized = response.iter_bytes()
        else:
            deserialized = _deserialize(_models.ImageAnalysisResult, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    @overload
    def _analyze_from_url(  # pylint: disable=protected-access
        self,
        image_url: _models._models.ImageUrl,
        *,
        visual_features: List[Union[str, _models.VisualFeatures]],
        content_type: str = "application/json",
        language: Optional[str] = None,
        gender_neutral_caption: Optional[bool] = None,
        smart_crops_aspect_ratios: Optional[List[float]] = None,
        model_version: Optional[str] = None,
        **kwargs: Any
    ) -> _models.ImageAnalysisResult:
        ...

    @overload
    def _analyze_from_url(
        self,
        image_url: JSON,
        *,
        visual_features: List[Union[str, _models.VisualFeatures]],
        content_type: str = "application/json",
        language: Optional[str] = None,
        gender_neutral_caption: Optional[bool] = None,
        smart_crops_aspect_ratios: Optional[List[float]] = None,
        model_version: Optional[str] = None,
        **kwargs: Any
    ) -> _models.ImageAnalysisResult:
        ...

    @overload
    def _analyze_from_url(
        self,
        image_url: IO[bytes],
        *,
        visual_features: List[Union[str, _models.VisualFeatures]],
        content_type: str = "application/json",
        language: Optional[str] = None,
        gender_neutral_caption: Optional[bool] = None,
        smart_crops_aspect_ratios: Optional[List[float]] = None,
        model_version: Optional[str] = None,
        **kwargs: Any
    ) -> _models.ImageAnalysisResult:
        ...

    @distributed_trace
    def _analyze_from_url(
        self,
        image_url: Union[_models._models.ImageUrl, JSON, IO[bytes]],
        *,
        visual_features: List[Union[str, _models.VisualFeatures]],
        language: Optional[str] = None,
        gender_neutral_caption: Optional[bool] = None,
        smart_crops_aspect_ratios: Optional[List[float]] = None,
        model_version: Optional[str] = None,
        **kwargs: Any
    ) -> _models.ImageAnalysisResult:
        # pylint: disable=line-too-long
        """Performs a single Image Analysis operation.

        :param image_url: The image to be analyzed. Is one of the following types: ImageUrl, JSON,
         IO[bytes] Required.
        :type image_url: ~azure.ai.vision.imageanalysis.models.ImageUrl or JSON or IO[bytes]
        :keyword visual_features: A list of visual features to analyze.
         Seven visual features are supported: Caption, DenseCaptions, Read (OCR), Tags, Objects,
         SmartCrops, and People.
         At least one visual feature must be specified. Required.
        :paramtype visual_features: list[str or ~azure.ai.vision.imageanalysis.models.VisualFeatures]
        :keyword language: The desired language for result generation (a two-letter language code).
         If this option is not specified, the default value 'en' is used (English).
         See https://aka.ms/cv-languages for a list of supported languages. Default value is None.
        :paramtype language: str
        :keyword gender_neutral_caption: Boolean flag for enabling gender-neutral captioning for
         Caption and Dense Captions features.
         By default captions may contain gender terms (for example: 'man', 'woman', or 'boy', 'girl').
         If you set this to "true", those will be replaced with gender-neutral terms (for example:
         'person' or 'child'). Default value is None.
        :paramtype gender_neutral_caption: bool
        :keyword smart_crops_aspect_ratios: A list of aspect ratios to use for smart cropping.
         Aspect ratios are calculated by dividing the target crop width in pixels by the height in
         pixels.
         Supported values are between 0.75 and 1.8 (inclusive).
         If this parameter is not specified, the service will return one crop region with an aspect
         ratio it sees fit between 0.5 and 2.0 (inclusive). Default value is None.
        :paramtype smart_crops_aspect_ratios: list[float]
        :keyword model_version: The version of cloud AI-model used for analysis.
         The format is the following: 'latest' (default value) or 'YYYY-MM-DD' or 'YYYY-MM-DD-preview',
         where 'YYYY', 'MM', 'DD' are the year, month and day associated with the model.
         This is not commonly set, as the default always gives the latest AI model with recent
         improvements.
         If however you would like to make sure analysis results do not change over time, set this
         value to a specific model version. Default value is None.
        :paramtype model_version: str
        :return: ImageAnalysisResult. The ImageAnalysisResult is compatible with MutableMapping
        :rtype: ~azure.ai.vision.imageanalysis.models.ImageAnalysisResult
        :raises ~azure.core.exceptions.HttpResponseError:

        Example:
            .. code-block:: python

                # JSON input template you can fill out and use as your body input.
                image_url = {
                    "url": "str"  # Publicly reachable URL of an image to analyze. Required.
                }

                # response body for status code(s): 200
                response == {
                    "metadata": {
                        "height": 0,  # The height of the image in pixels. Required.
                        "width": 0  # The width of the image in pixels. Required.
                    },
                    "modelVersion": "str",  # The cloud AI model used for the analysis. Required.
                    "captionResult": {
                        "confidence": 0.0,  # A score, in the range of 0 to 1 (inclusive),
                          representing the confidence that this description is accurate. Higher values
                          indicating higher confidence. Required.
                        "text": "str"  # The text of the caption. Required.
                    },
                    "denseCaptionsResult": {
                        "values": [
                            {
                                "boundingBox": {
                                    "h": 0,  # Height of the area, in pixels.
                                      Required.
                                    "w": 0,  # Width of the area, in pixels.
                                      Required.
                                    "x": 0,  # X-coordinate of the top left point
                                      of the area, in pixels. Required.
                                    "y": 0  # Y-coordinate of the top left point
                                      of the area, in pixels. Required.
                                },
                                "confidence": 0.0,  # A score, in the range of 0 to 1
                                  (inclusive), representing the confidence that this description is
                                  accurate. Higher values indicating higher confidence. Required.
                                "text": "str"  # The text of the caption. Required.
                            }
                        ]
                    },
                    "objectsResult": {
                        "values": [
                            {
                                "boundingBox": {
                                    "h": 0,  # Height of the area, in pixels.
                                      Required.
                                    "w": 0,  # Width of the area, in pixels.
                                      Required.
                                    "x": 0,  # X-coordinate of the top left point
                                      of the area, in pixels. Required.
                                    "y": 0  # Y-coordinate of the top left point
                                      of the area, in pixels. Required.
                                },
                                "tags": [
                                    {
                                        "confidence": 0.0,  # A score, in the
                                          range of 0 to 1 (inclusive), representing the confidence that
                                          this entity was observed. Higher values indicating higher
                                          confidence. Required.
                                        "name": "str"  # Name of the entity.
                                          Required.
                                    }
                                ]
                            }
                        ]
                    },
                    "peopleResult": {
                        "values": [
                            {
                                "boundingBox": {
                                    "h": 0,  # Height of the area, in pixels.
                                      Required.
                                    "w": 0,  # Width of the area, in pixels.
                                      Required.
                                    "x": 0,  # X-coordinate of the top left point
                                      of the area, in pixels. Required.
                                    "y": 0  # Y-coordinate of the top left point
                                      of the area, in pixels. Required.
                                },
                                "confidence": 0.0  # A score, in the range of 0 to 1
                                  (inclusive), representing the confidence that this detection was
                                  accurate. Higher values indicating higher confidence. Required.
                            }
                        ]
                    },
                    "readResult": {
                        "blocks": [
                            {
                                "lines": [
                                    {
                                        "boundingPolygon": [
                                            {
                                                "x": 0,  # The
                                                  horizontal x-coordinate of this point, in pixels.
                                                  Zero values corresponds to the left-most pixels in
                                                  the image. Required.
                                                "y": 0  # The
                                                  vertical y-coordinate of this point, in pixels. Zero
                                                  values corresponds to the top-most pixels in the
                                                  image. Required.
                                            }
                                        ],
                                        "text": "str",  # Text content of the
                                          detected text line. Required.
                                        "words": [
                                            {
                                                "boundingPolygon": [
                                                    {
                                                        "x":
                                                          0,  # The horizontal x-coordinate of this
                                                          point, in pixels. Zero values corresponds to
                                                          the left-most pixels in the image. Required.
                                                        "y":
                                                          0  # The vertical y-coordinate of this point,
                                                          in pixels. Zero values corresponds to the
                                                          top-most pixels in the image. Required.
                                                    }
                                                ],
                                                "confidence": 0.0,  #
                                                  The level of confidence that the word was detected.
                                                  Confidence scores span the range of 0.0 to 1.0
                                                  (inclusive), with higher values indicating a higher
                                                  confidence of detection. Required.
                                                "text": "str"  # Text
                                                  content of the word. Required.
                                            }
                                        ]
                                    }
                                ]
                            }
                        ]
                    },
                    "smartCropsResult": {
                        "values": [
                            {
                                "aspectRatio": 0.0,  # The aspect ratio of the crop
                                  region. Aspect ratio is calculated by dividing the width of the
                                  region in pixels by its height in pixels. The aspect ratio will be in
                                  the range 0.75 to 1.8 (inclusive) if provided by the developer during
                                  the analyze call. Otherwise, it will be in the range 0.5 to 2.0
                                  (inclusive). Required.
                                "boundingBox": {
                                    "h": 0,  # Height of the area, in pixels.
                                      Required.
                                    "w": 0,  # Width of the area, in pixels.
                                      Required.
                                    "x": 0,  # X-coordinate of the top left point
                                      of the area, in pixels. Required.
                                    "y": 0  # Y-coordinate of the top left point
                                      of the area, in pixels. Required.
                                }
                            }
                        ]
                    },
                    "tagsResult": {
                        "values": [
                            {
                                "confidence": 0.0,  # A score, in the range of 0 to 1
                                  (inclusive), representing the confidence that this entity was
                                  observed. Higher values indicating higher confidence. Required.
                                "name": "str"  # Name of the entity. Required.
                            }
                        ]
                    }
                }
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = kwargs.pop("params", {}) or {}

        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("content-type", None))
        cls: ClsType[_models.ImageAnalysisResult] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _content = None
        if isinstance(image_url, (IOBase, bytes)):
            _content = image_url
        else:
            _content = json.dumps(image_url, cls=SdkJSONEncoder, exclude_readonly=True)  # type: ignore

        _request = build_image_analysis_analyze_from_url_request(
            visual_features=visual_features,
            language=language,
            gender_neutral_caption=gender_neutral_caption,
            smart_crops_aspect_ratios=smart_crops_aspect_ratios,
            model_version=model_version,
            content_type=content_type,
            api_version=self._config.api_version,
            content=_content,
            headers=_headers,
            params=_params,
        )
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        _request.url = self._client.format_url(_request.url, **path_format_arguments)

        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            if _stream:
                response.read()  # Load the body in memory and close the socket
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if _stream:
            deserialized = response.iter_bytes()
        else:
            deserialized = _deserialize(_models.ImageAnalysisResult, response.json())

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore
