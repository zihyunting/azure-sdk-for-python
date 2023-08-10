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
    python auth_configs_create_or_update.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = ContainerAppsAPIClient(
        credential=DefaultAzureCredential(),
        subscription_id="651f8027-33e8-4ec4-97b4-f6e9f3dc8744",
    )

    response = client.container_apps_auth_configs.create_or_update(
        resource_group_name="workerapps-rg-xj",
        container_app_name="testcanadacentral",
        auth_config_name="current",
        auth_config_envelope={
            "properties": {
                "encryptionSettings": {
                    "containerAppAuthEncryptionSecretName": "testEncryptionSecretName",
                    "containerAppAuthSigningSecretName": "testSigningSecretName",
                },
                "globalValidation": {"unauthenticatedClientAction": "AllowAnonymous"},
                "identityProviders": {
                    "facebook": {"registration": {"appId": "123", "appSecretSettingName": "facebook-secret"}}
                },
                "platform": {"enabled": True},
            }
        },
    )
    print(response)


# x-ms-original-file: specification/app/resource-manager/Microsoft.App/preview/2023-05-02-preview/examples/AuthConfigs_CreateOrUpdate.json
if __name__ == "__main__":
    main()
