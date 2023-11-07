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
    python sync_member_update.py

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

    response = client.sync_members.begin_create_or_update(
        resource_group_name="syncgroupcrud-65440",
        server_name="syncgroupcrud-8475",
        database_name="syncgroupcrud-4328",
        sync_group_name="syncgroupcrud-3187",
        sync_member_name="syncmembercrud-4879",
        parameters={
            "properties": {
                "databaseName": "syncgroupcrud-7421",
                "databaseType": "AzureSqlDatabase",
                "serverName": "syncgroupcrud-3379.database.windows.net",
                "syncDirection": "Bidirectional",
                "syncMemberAzureDatabaseResourceId": "/subscriptions/00000000-1111-2222-3333-444444444444/resourceGroups/syncgroupcrud-65440/providers/Microsoft.Sql/servers/syncgroupcrud-8475/databases/syncgroupcrud-4328",
                "usePrivateLinkConnection": True,
                "userName": "myUser",
            }
        },
    ).result()
    print(response)


# x-ms-original-file: specification/sql/resource-manager/Microsoft.Sql/preview/2023-05-01-preview/examples/SyncMemberUpdate.json
if __name__ == "__main__":
    main()
