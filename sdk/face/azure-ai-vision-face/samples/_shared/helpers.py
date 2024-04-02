# coding: utf-8

# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------

"""
FILE: config.py

DESCRIPTION:
    This module loads configuration required to run the sample codes.
"""

import os

from .constants import (
    CONFIGURATION_NAME_FACE_API_ENDPOINT,
    CONFIGURATION_NAME_FACE_API_ACCOUNT_KEY,
    DEFAULT_FACE_API_ENDPOINT,
    DEFAULT_FACE_API_ACCOUNT_KEY
)


def get_face_api_endpoint():
    return os.getenv(CONFIGURATION_NAME_FACE_API_ENDPOINT, DEFAULT_FACE_API_ENDPOINT)


def get_face_api_account_key():
    return os.getenv(CONFIGURATION_NAME_FACE_API_ACCOUNT_KEY, DEFAULT_FACE_API_ACCOUNT_KEY)
