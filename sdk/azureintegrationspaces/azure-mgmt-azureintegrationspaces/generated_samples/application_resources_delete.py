# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.identity import DefaultAzureCredential
from azure.mgmt.azureintegrationspaces import MicrosoftIntegrationSpaces

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-azureintegrationspaces
# USAGE
    python application_resources_delete.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = MicrosoftIntegrationSpaces(
        credential=DefaultAzureCredential(),
        subscription_id="00000000-0000-0000-0000-000000000000",
    )

    client.application_resources.delete(
        resource_group_name="testrg",
        space_name="Space1",
        application_name="Application1",
        resource_name="Resource1",
    )


# x-ms-original-file: specification/azureintegrationspaces/resource-manager/Microsoft.IntegrationSpaces/preview/2023-11-14-preview/examples/ApplicationResources_Delete.json
if __name__ == "__main__":
    main()
