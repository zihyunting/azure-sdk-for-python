# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.identity import DefaultAzureCredential

from azure.mgmt.appcontainers import ContainerAppsAPIClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-appcontainers
# USAGE
    python revisions_activate.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = ContainerAppsAPIClient(
        credential=DefaultAzureCredential(),
        container_app_name="testcontainerApp0",
        subscription_id="34adfa4f-cedf-4dc0-ba29-b6d1a69ab345",
    )

    client.container_apps_revisions.activate_revision(
        resource_group_name="rg",
        container_app_name="testcontainerApp0",
        revision_name="testcontainerApp0-pjxhsye",
    )


# x-ms-original-file: specification/app/resource-manager/Microsoft.App/preview/2024-02-02-preview/examples/Revisions_Activate.json
if __name__ == "__main__":
    main()
