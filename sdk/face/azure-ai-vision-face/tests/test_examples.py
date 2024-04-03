# coding: utf-8

# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------

from devtools_testutils import AzureRecordedTestCase, recorded_by_proxy

from preparers import FacePreparer


class TestExamples(AzureRecordedTestCase):
    @staticmethod
    def func(x):
        return x + 1

    def test_answer(self):
        assert self.func(3) == 4

    @FacePreparer()
    @recorded_by_proxy
    def test_example_with_preparer(self, **kwargs):
        service_endpoint = kwargs.pop("azure_face_api_endpoint")
        service_name = kwargs.pop("azure_face_api_name")
        service_account_key = kwargs.pop("azure_face_api_account_key")

        assert service_endpoint != ""
        assert service_name != ""
        assert service_account_key != ""
