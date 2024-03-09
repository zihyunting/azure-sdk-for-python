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
    python managed_instance_administrator_create.py

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

    response = client.managed_instance_administrators.begin_create_or_update(
        resource_group_name="Default-SQL-SouthEastAsia",
        managed_instance_name="managedInstance",
        administrator_name="ActiveDirectory",
        parameters={
            "properties": {
                "administratorType": "ActiveDirectory",
                "login": "bob@contoso.com",
                "sid": "44444444-3333-2222-1111-000000000000",
                "tenantId": "55555555-4444-3333-2222-111111111111",
            }
        },
    ).result()
    print(response)


# x-ms-original-file: specification/sql/resource-manager/Microsoft.Sql/preview/2024-02-01-preview/examples/ManagedInstanceAdministratorCreate.json
if __name__ == "__main__":
    main()
