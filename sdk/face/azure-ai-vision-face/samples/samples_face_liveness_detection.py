# coding: utf-8

# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
"""
FILE: sample_face_liveness_detection.py

DESCRIPTION:
    This sample demonstrates how to determine if a face in an input video stream is real (live) or fake (spoof).
    There is a step during the execution of the program that requires the user to switch to mobile SDK for performing
    the liveness detection.

USAGE:
    python sample_face_liveness_detection.py

    Set the environment variables with your own values before running this sample:
    1) FACE_ENDPOINT - the endpoint to your Face resource.
    2) FACE_KEY - your Face API key.
"""
import os
import uuid

from dotenv import find_dotenv, load_dotenv

from _shared.constants import (
    CONFIGURATION_NAME_FACE_API_ACCOUNT_KEY,
    CONFIGURATION_NAME_FACE_API_ENDPOINT,
    DEFAULT_FACE_API_ACCOUNT_KEY,
    DEFAULT_FACE_API_ENDPOINT,
)
from _shared.helpers import beautify_json, get_logger


class DetectLiveness():
    def __init__(self):
        load_dotenv(find_dotenv())
        self.endpoint = os.getenv(CONFIGURATION_NAME_FACE_API_ENDPOINT, DEFAULT_FACE_API_ENDPOINT)
        self.key = os.getenv(CONFIGURATION_NAME_FACE_API_ACCOUNT_KEY, DEFAULT_FACE_API_ACCOUNT_KEY)
        self.logger = get_logger("sample_face_liveness_detection")

    def livenessSession(self):
        from azure.core.credentials import AzureKeyCredential
        from azure.ai.vision.face import FaceSessionClient
        from azure.ai.vision.face.models import LivenessSessionCreationContent, LivenessOperationMode

        with FaceSessionClient(endpoint=self.endpoint, credential=AzureKeyCredential(self.key)) as face_session_client:
            # Create a session.
            self.logger.info("Create a new liveness session.")
            created_session = face_session_client.create_liveness_session(
                LivenessSessionCreationContent(
                    liveness_operation_mode=LivenessOperationMode.PASSIVE,
                    device_correlation_id=str(uuid.uuid4()),
                    send_results_to_client=False))
            self.logger.info(f"Result: {beautify_json(created_session.as_dict())}")

            # Get the liveness detection result.
            self.logger.info("Get the liveness detection result.")
            liveness_result = face_session_client.get_liveness_session_result(created_session.session_id)
            self.logger.info(f"Result: {beautify_json(liveness_result.as_dict())}")

            self.logger.info(
                "Please refer to https://learn.microsoft.com/en-us/azure/ai-services/computer-vision/tutorials/liveness"
                " to download client SDK to run session starts and detcet liveness call.")
            input("Press any key to continue when you complete these steps to run sample to get session results.")

            # Get the liveness detection result again.
            self.logger.info("Get the liveness detection result again.")
            liveness_result = face_session_client.get_liveness_session_result(created_session.session_id)
            self.logger.info(f"Result: {beautify_json(liveness_result.as_dict())}")

            # Get audit entries
            self.logger.info("Get the audit entries of this session.")
            audit_entries = face_session_client.get_liveness_session_audit_entries(created_session.session_id)
            for idx, entry in enumerate(audit_entries):
                self.logger.info(f"----- Audit entries: #{idx+1}-----")
                self.logger.info(f"Entry: {beautify_json(entry.as_dict())}")

            # Delete the session
            self.logger.info("Delete the session.")
            face_session_client.delete_liveness_session(created_session.session_id)


if __name__ == "__main__":
    sample = DetectLiveness()
    sample.livenessSession()
