# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.identity import DefaultAzureCredential
from azure.mgmt.datamigration import DataMigrationManagementClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-datamigration
# USAGE
    python cutover_online_migration_operation_for_the_database..py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = DataMigrationManagementClient(
        credential=DefaultAzureCredential(),
        subscription_id="00000000-1111-2222-3333-444444444444",
    )

    response = client.database_migrations_sql_mi.begin_cutover(
        resource_group_name="testrg",
        managed_instance_name="managedInstance1",
        target_db_name="db1",
        parameters={"migrationOperationId": "4124fe90-d1b6-4b50-b4d9-46d02381f59a"},
    ).result()
    print(response)


# x-ms-original-file: specification/datamigration/resource-manager/Microsoft.DataMigration/preview/2022-10-31-preview/examples/SqlMiCutoverDatabaseMigration.json
if __name__ == "__main__":
    main()
