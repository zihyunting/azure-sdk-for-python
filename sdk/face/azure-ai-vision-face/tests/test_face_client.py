# coding: utf-8

# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------

from pathlib import Path

from devtools_testutils import AzureRecordedTestCase, recorded_by_proxy

from azure.ai.vision.face.models import FaceDetectionModel, FaceRecognitionModel
from preparers import FacePreparer
from _shared.constants import IMAGE_FILE_PATH
from _shared.client_helpers import get_face_client


class TestFaceClient(AzureRecordedTestCase):
    @FacePreparer()
    @recorded_by_proxy
    def test_face_client_api_key_authentication(self, **kwargs):
        face_client = get_face_client(**kwargs)

        sample_file_path = Path(__file__).resolve().parent / IMAGE_FILE_PATH
        with open(sample_file_path, "rb") as fd:
            file_content = fd.read()

        result = face_client.detect(
            image_content=file_content, return_face_id=False, return_face_landmarks=True,
            return_face_attributes="headPose,qualityForRecognition",
            detection_model=FaceDetectionModel.DETECTION_03, recognition_model=FaceRecognitionModel.RECOGNITION_04)

        assert result is not None
        assert len(result) == 1
        assert result[0].face_rectangle is not None
        assert result[0].face_landmarks is not None
        assert result[0].face_attributes.head_pose is not None
        assert result[0].face_attributes.quality_for_recognition is not None
