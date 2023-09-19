# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.identity import DefaultAzureCredential
from azure.mgmt.storage import StorageManagementClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-storage
# USAGE
    python table_services_put.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = StorageManagementClient(
        credential=DefaultAzureCredential(),
        subscription_id="{subscription-id}",
    )

    response = client.table_services.set_service_properties(
        resource_group_name="res4410",
        account_name="sto8607",
        parameters={
            "properties": {
                "cors": {
                    "corsRules": [
                        {
                            "allowedHeaders": ["x-ms-meta-abc", "x-ms-meta-data*", "x-ms-meta-target*"],
                            "allowedMethods": ["GET", "HEAD", "POST", "OPTIONS", "MERGE", "PUT"],
                            "allowedOrigins": ["http://www.contoso.com", "http://www.fabrikam.com"],
                            "exposedHeaders": ["x-ms-meta-*"],
                            "maxAgeInSeconds": 100,
                        },
                        {
                            "allowedHeaders": ["*"],
                            "allowedMethods": ["GET"],
                            "allowedOrigins": ["*"],
                            "exposedHeaders": ["*"],
                            "maxAgeInSeconds": 2,
                        },
                        {
                            "allowedHeaders": ["x-ms-meta-12345675754564*"],
                            "allowedMethods": ["GET", "PUT"],
                            "allowedOrigins": ["http://www.abc23.com", "https://www.fabrikam.com/*"],
                            "exposedHeaders": ["x-ms-meta-abc", "x-ms-meta-data*", "x-ms-meta-target*"],
                            "maxAgeInSeconds": 2000,
                        },
                    ]
                }
            }
        },
    )
    print(response)


# x-ms-original-file: specification/storage/resource-manager/Microsoft.Storage/stable/2023-04-01/examples/TableServicesPut.json
if __name__ == "__main__":
    main()
