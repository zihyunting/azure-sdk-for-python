# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Any, IO, Union

from azure.identity import DefaultAzureCredential

from azure.mgmt.desktopvirtualization import DesktopVirtualizationMgmtClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-desktopvirtualization
# USAGE
    python session_host_managements_create.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = DesktopVirtualizationMgmtClient(
        credential=DefaultAzureCredential(),
        subscription_id="daefabc0-95b4-48b3-b645-8a753a63c4fa",
    )

    response = client.session_host_managements.create_or_update(
        resource_group_name="resourceGroup1",
        host_pool_name="hostPool1",
        session_host_management={
            "properties": {
                "scheduledDateTimeZone": "Alaskan Standard Time",
                "update": {
                    "deleteOriginalVm": True,
                    "logOffDelayMinutes": 10,
                    "logOffMessage": "logging off for hostpool update",
                    "maxVmsRemoved": 4,
                },
            }
        },
    )
    print(response)


# x-ms-original-file: specification/desktopvirtualization/resource-manager/Microsoft.DesktopVirtualization/preview/2024-03-06-preview/examples/SessionHostManagements_Create.json
if __name__ == "__main__":
    main()
