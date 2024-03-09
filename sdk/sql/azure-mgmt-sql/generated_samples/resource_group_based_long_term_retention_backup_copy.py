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
    python resource_group_based_long_term_retention_backup_copy.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = SqlManagementClient(
        credential=DefaultAzureCredential(),
        subscription_id="00000000-1111-2222-3333-444444444444",
    )

    response = client.long_term_retention_backups.begin_copy_by_resource_group(
        resource_group_name="testResourceGroup",
        location_name="japaneast",
        long_term_retention_server_name="testserver",
        long_term_retention_database_name="testDatabase",
        backup_name="55555555-6666-7777-8888-999999999999;131637960820000000",
        parameters={
            "properties": {
                "targetBackupStorageRedundancy": "Geo",
                "targetDatabaseName": "testDatabase2",
                "targetServerResourceId": "/subscriptions/00000000-1111-2222-3333-444444444444/providers/Microsoft.Sql/resourceGroups/resourceGroup/servers/testserver2",
            }
        },
    ).result()
    print(response)


# x-ms-original-file: specification/sql/resource-manager/Microsoft.Sql/preview/2024-02-01-preview/examples/ResourceGroupBasedLongTermRetentionBackupCopy.json
if __name__ == "__main__":
    main()
