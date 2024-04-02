# coding: utf-8

# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------

"""
FILE: sample_face_detection_async.py

DESCRIPTION:
    This sample demonstrates how to detect faces and analyze faces from an image or binary data.

USAGE:
    python sample_face_detection_async.py

    Set the environment variables with your own values before running this sample:
    1) FACE_ENDPOINT - the endpoint to your Face resource.
    2) FACE_KEY - your Face API key.
"""

import asyncio

from dotenv import find_dotenv, load_dotenv

from samples._shared.constants import (
    DEFAULT_IMAGE_FILE_PATH,
    DEFAULT_IMAGE_URL,
)
from samples._shared.helpers import get_face_api_endpoint, get_face_api_account_key


class DetectFaces():
    def __init__(self):
        load_dotenv(find_dotenv())
        self.endpoint = get_face_api_endpoint()
        self.key = get_face_api_account_key()

    async def detect_from_url(self):
        # [START detect_from_url]
        from azure.core.credentials import AzureKeyCredential
        from azure.ai.vision.face.aio import FaceClient
        from azure.ai.vision.face.models import FaceDetectionModel, FaceRecognitionModel

        async with FaceClient(endpoint=self.endpoint, credential=AzureKeyCredential(self.key)) as face_client:
            sample_url = DEFAULT_IMAGE_URL
            result = await face_client.detect_from_url(
                url=sample_url, return_face_id=False, return_face_landmarks=True,
                return_face_attributes="headPose,qualityForRecognition",
                detection_model=FaceDetectionModel.DETECTION_03, recognition_model=FaceRecognitionModel.RECOGNITION_04)

            print(f"Detect faces from the url: {sample_url}")
            for idx, face in enumerate(result):
                print(f"----- Detection result: #{idx+1} -----")
                print(f"Face rectangle: {face.face_rectangle}")
                print(f"Face landmarks: {face.face_landmarks}")
                print(f"Face attributes: {face.face_attributes}")
        # [END detect_from_url]

    async def detect(self):
        # [START detect]
        from azure.core.credentials import AzureKeyCredential
        from azure.ai.vision.face.aio import FaceClient
        from azure.ai.vision.face.models import FaceDetectionModel, FaceRecognitionModel

        async with FaceClient(endpoint=self.endpoint, credential=AzureKeyCredential(self.key)) as face_client:
            from pathlib import Path

            sample_file_path = Path(__file__).resolve().parent / ("../" + DEFAULT_IMAGE_FILE_PATH)
            with open(sample_file_path, "rb") as fd:
                file_content = fd.read()

            result = await face_client.detect(
                image_content=file_content, return_face_id=False, return_face_landmarks=True,
                return_face_attributes="headPose,qualityForRecognition",
                detection_model=FaceDetectionModel.DETECTION_03, recognition_model=FaceRecognitionModel.RECOGNITION_04)

            print(f"Detect faces from the file: {sample_file_path}")
            for idx, face in enumerate(result):
                print(f"----- Detection result: #{idx+1} -----")
                print(f"Face rectangle: {face.face_rectangle}")
                print(f"Face landmarks: {face.face_landmarks}")
                print(f"Face attributes: {face.face_attributes}")
        # [END detect]


async def main():
    sample = DetectFaces()
    await sample.detect()
    await sample.detect_from_url()


if __name__ == "__main__":
    asyncio.run(main())
