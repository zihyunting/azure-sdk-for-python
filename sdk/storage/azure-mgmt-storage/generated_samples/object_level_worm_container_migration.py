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
    python object_level_worm_container_migration.py

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

    client.blob_containers.begin_object_level_worm(
        resource_group_name="res1782",
        account_name="sto7069",
        container_name="container6397",
    ).result()


# x-ms-original-file: specification/storage/resource-manager/Microsoft.Storage/stable/2023-04-01/examples/ObjectLevelWormContainerMigration.json
if __name__ == "__main__":
    main()
