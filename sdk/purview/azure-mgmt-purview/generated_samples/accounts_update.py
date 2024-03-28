# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Any, IO, Union

from azure.identity import DefaultAzureCredential

from azure.mgmt.purview import PurviewManagementClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-purview
# USAGE
    python accounts_update.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = PurviewManagementClient(
        credential=DefaultAzureCredential(),
        subscription_id="34adfa4f-cedf-4dc0-ba29-b6d1a69ab345",
    )

    response = client.accounts.begin_update(
        resource_group_name="SampleResourceGroup",
        account_name="account1",
        account_update_parameters={
            "properties": {
                "cloudConnectors": {},
                "ingestionStorage": {"publicNetworkAccess": "Disabled"},
                "managedResourcesPublicNetworkAccess": "Disabled",
                "publicNetworkAccess": "Disabled",
            },
            "tags": {"newTag": "New tag value."},
        },
    ).result()
    print(response)


# x-ms-original-file: specification/purview/resource-manager/Microsoft.Purview/preview/2024-04-01-preview/examples/Accounts_Update.json
if __name__ == "__main__":
    main()
