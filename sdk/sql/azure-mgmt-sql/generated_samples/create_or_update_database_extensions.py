# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.identity import DefaultAzureCredential
from azure.mgmt.sql import SqlManagementClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-sql
# USAGE
    python create_or_update_database_extensions.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = SqlManagementClient(
        credential=DefaultAzureCredential(),
        subscription_id="a1c0814d-3c18-4e1e-a247-c128c12b1677",
    )

    response = client.database_extensions.begin_create_or_update(
        resource_group_name="rg_20cbe0f0-c2d9-4522-9177-5469aad53029",
        server_name="srv_1ffd1cf8-9951-47fb-807d-a9c384763849",
        database_name="878e303f-1ea0-4f17-aa3d-a22ac5e9da08",
        extension_name="polybaseimport",
        parameters={
            "properties": {
                "operationMode": "PolybaseImport",
                "storageKey": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
                "storageKeyType": "StorageAccessKey",
                "storageUri": "https://teststorage.blob.core.windows.net/testcontainer/Manifest.xml",
            }
        },
    ).result()
    print(response)


# x-ms-original-file: specification/sql/resource-manager/Microsoft.Sql/preview/2023-05-01-preview/examples/CreateOrUpdateDatabaseExtensions.json
if __name__ == "__main__":
    main()
