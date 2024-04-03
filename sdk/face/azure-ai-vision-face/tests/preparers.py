# coding: utf-8

# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------

import functools

from devtools_testutils import EnvironmentVariableLoader

FacePreparer = functools.partial(
    EnvironmentVariableLoader,
    "face",
    azure_face_api_endpoint="fake-endpoint",
    azure_face_api_name="fake-account-name",
    azure_face_api_account_key="fake-account-key"
)
