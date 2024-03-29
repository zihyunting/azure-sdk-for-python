# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Any, IO, Union

from azure.identity import DefaultAzureCredential

from azure.mgmt.managedapplications import ManagedApplicationsMgmtClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-managedapplications
# USAGE
    python update_jit_request.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = ManagedApplicationsMgmtClient(
        credential=DefaultAzureCredential(),
        subscription_id="subid",
    )

    response = client.jit_requests.update(
        resource_group_name="rg",
        jit_request_name="myJitRequest",
        parameters={"tags": {"department": "Finance"}},
    )
    print(response)


# x-ms-original-file: specification/solutions/resource-manager/Microsoft.Solutions/stable/2021-07-01/examples/updateJitRequest.json
if __name__ == "__main__":
    main()
