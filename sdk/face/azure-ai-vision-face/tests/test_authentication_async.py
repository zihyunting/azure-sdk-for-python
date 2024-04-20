# coding: utf-8

# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------

from pathlib import Path

from devtools_testutils import AzureRecordedTestCase
from devtools_testutils.aio import recorded_by_proxy_async

from azure.ai.vision.face.models import FaceDetectionModel, FaceRecognitionModel, FaceAttributeType

from preparers import AsyncFaceClientPreparer, FacePreparer
from _shared.constants import IMAGE_DETECTION_1


class TestAuthenticationAsync(AzureRecordedTestCase):
    @FacePreparer()
    @AsyncFaceClientPreparer()
    @recorded_by_proxy_async
    async def test_face_client_api_key_authentication(self, client, **kwargs):
        sample_file_path = Path(__file__).resolve().parent / IMAGE_DETECTION_1
        with open(sample_file_path, "rb") as fd:
            file_content = fd.read()

        result = await client.detect(
            image_content=file_content,
            detection_model=FaceDetectionModel.DETECTION_03,
            recognition_model=FaceRecognitionModel.RECOGNITION_04,
            return_face_landmarks=True,
            return_face_attributes=[
                FaceAttributeType.HEAD_POSE, FaceAttributeType.MASK, FaceAttributeType.QUALITY_FOR_RECOGNITION])

        assert result is not None

        await client.close()
