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
    python builds_list_auth_token.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = ContainerAppsAPIClient(
        credential=DefaultAzureCredential(),
        container_app_name="CONTAINER_APP_NAME",
        subscription_id="00000000-0000-0000-0000-000000000000",
    )

    response = client.build_auth_token.list(
        resource_group_name="rg",
        builder_name="testBuilder",
        build_name="testBuild",
    )
    print(response)


# x-ms-original-file: specification/app/resource-manager/Microsoft.App/preview/2024-02-02-preview/examples/Builds_ListAuthToken.json
if __name__ == "__main__":
    main()
