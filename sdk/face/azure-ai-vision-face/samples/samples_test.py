# coding: utf-8

# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
"""
FILE: sample_authentication.py

DESCRIPTION:
    This sample demonstrates authenticating a client via:
        * api key
        * Azure Active Directory(AAD)

USAGE:
    python sample_authentication.py

    Set the environment variables with your own values before running this sample:
    1) FACE_ENDPOINT - the endpoint to your Face resource.
    The environment variable below is used for api key authentication.
    2) FACE_KEY - your Face API key.
    The following environment variables are required for using azure-identity's DefaultAzureCredential.
    For more information, refer to https://aka.ms/azsdk/python/identity/docs#azure.identity.DefaultAzureCredential
    3) AZURE_TENANT_ID - the tenant ID in Azure Active Directory
    4) AZURE_CLIENT_ID - the application (client) ID registered in the AAD tenant
    5) AZURE_CLIENT_SECRET - the client secret for the registered application
"""
import os
import time

from dotenv import find_dotenv, load_dotenv

from _shared.constants import (
    CONFIGURATION_NAME_FACE_API_ACCOUNT_KEY,
    CONFIGURATION_NAME_FACE_API_ENDPOINT,
    DEFAULT_FACE_API_ACCOUNT_KEY,
    DEFAULT_FACE_API_ENDPOINT,
    DEFAULT_IMAGE_URL,
    IMAGE_DETECTION_1,
)
from _shared.helpers import beautify_json, get_logger


class FaceTest():
    def __init__(self):
        load_dotenv(find_dotenv())
        self.endpoint = os.getenv(CONFIGURATION_NAME_FACE_API_ENDPOINT, DEFAULT_FACE_API_ENDPOINT)
        self.key = os.getenv(CONFIGURATION_NAME_FACE_API_ACCOUNT_KEY, DEFAULT_FACE_API_ACCOUNT_KEY)
        self.logger = get_logger("sample_authentication")

    def test_pd(self):
        from azure.core.credentials import AzureKeyCredential
        from azure.ai.vision.face import FaceAdministrationClient

        with FaceAdministrationClient(endpoint=self.endpoint, credential=AzureKeyCredential(self.key)) as face_client:
            polling = face_client.create_person(name="pdtest1", polling_interval=30)
            polling_result = polling.result()
            print(f"Polling result: {polling_result}, type: {type(polling_result)}")

    def test_pd_add_face(self):
        from azure.core.credentials import AzureKeyCredential
        from azure.ai.vision.face import FaceAdministrationClient
        from azure.ai.vision.face.models import FaceDetectionModel, FaceRecognitionModel

        with FaceAdministrationClient(endpoint=self.endpoint, credential=AzureKeyCredential(self.key)) as face_client:
            from pathlib import Path

            sample_file_path = Path(__file__).resolve().parent / IMAGE_DETECTION_1
            with open(sample_file_path, "rb") as fd:
                file_content = fd.read()

            person_id = "f94307bd-9f13-4410-963b-d828b0caf780"
            polling = face_client.add_person_face(
                person_id, file_content, FaceDetectionModel.DETECTION_03, FaceRecognitionModel.RECOGNITION_04,
                polling_interval=30)
            polling_result = polling.result()
            print(f"Polling result: {polling_result}, type: {type(polling_result)}")

    # FIXME: Get exception because the response is empty
    def test_create_dynamic_person_group(self):
        from azure.core.credentials import AzureKeyCredential
        from azure.ai.vision.face import FaceAdministrationClient

        with FaceAdministrationClient(endpoint=self.endpoint, credential=AzureKeyCredential(self.key)) as face_client:
            dynamic_person_group_id = "dpg0"
            polling = face_client.create_dynamic_person_group(dynamic_person_group_id, name="name0")
            polling_result = polling.result()
            print(f"Polling result: {polling_result}")

    def test_create_dynamic_person_group_with_persons(self):
        from azure.core.credentials import AzureKeyCredential
        from azure.ai.vision.face import FaceAdministrationClient

        with FaceAdministrationClient(endpoint=self.endpoint, credential=AzureKeyCredential(self.key)) as face_client:
            person_id = "f94307bd-9f13-4410-963b-d828b0caf780"
            dynamic_person_group_id = "dpg1"
            polling = face_client.create_dynamic_person_group(
                    dynamic_person_group_id, name="name1", add_person_ids=[person_id])
            polling_result = polling.result()
            print(f"Polling result: {polling_result}")

    def test_training(self):
        from azure.core.credentials import AzureKeyCredential
        from azure.ai.vision.face import FaceAdministrationClient

        with FaceAdministrationClient(endpoint=self.endpoint, credential=AzureKeyCredential(self.key)) as face_client:
            # result = face_client.create_large_face_list(large_face_list_id="lfltest1", name="largeFaceList-test")
            # print(result)

            """
            response = face_client.add_large_face_list_face_from_url(
                large_face_list_id="lfltest1", url=DEFAULT_IMAGE_URL)
            print(f"Add face result: {response}")
            """

            polling = face_client.begin_train_large_face_list(large_face_list_id="lfltest1")
            print("Get poller")
            time.sleep(10)
            print("Get result")
            polling_result = polling.result()
            print(f"Polling result: {polling_result}, type: {type(polling_result)}")

            # Polling shouldn't be False!
            '''
            polling = face_client.begin_train_large_face_list(
                    large_face_list_id="lfltest1", polling=False, cls=lambda x, _, z: z)
            polling_result = polling.result()
            print(f"Polling result: {polling_result}")
            '''


if __name__ == "__main__":
    sample = FaceTest()
    # sample.test_pd()
    # sample.test_pd_add_face()
    sample.test_create_dynamic_person_group()
    # sample.test_create_dynamic_person_group_with_persons()
    # sample.test_training()
