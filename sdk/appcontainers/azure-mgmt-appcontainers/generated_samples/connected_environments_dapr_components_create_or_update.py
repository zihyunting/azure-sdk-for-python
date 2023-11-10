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
    python connected_environments_dapr_components_create_or_update.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = ContainerAppsAPIClient(
        credential=DefaultAzureCredential(),
        subscription_id="8efdecc5-919e-44eb-b179-915dca89ebf9",
    )

    response = client.connected_environments_dapr_components.create_or_update(
        resource_group_name="examplerg",
        connected_environment_name="myenvironment",
        component_name="reddog",
        dapr_component_envelope={
            "properties": {
                "componentType": "state.azure.cosmosdb",
                "ignoreErrors": False,
                "initTimeout": "50s",
                "metadata": [
                    {"name": "url", "value": "<COSMOS-URL>"},
                    {"name": "database", "value": "itemsDB"},
                    {"name": "collection", "value": "items"},
                    {"name": "masterkey", "secretRef": "masterkey"},
                ],
                "scopes": ["container-app-1", "container-app-2"],
                "secrets": [{"name": "masterkey", "value": "keyvalue"}],
                "serviceComponentBind": [
                    {
                        "metadata": {"name": "daprcomponentBind", "value": "redis-bind"},
                        "name": "statestore",
                        "serviceId": "/subscriptions/9f7371f1-b593-4c3c-84e2-9167806ad358/resourceGroups/ca-syn2-group/providers/Microsoft.App/containerapps/cappredis",
                    }
                ],
                "version": "v1",
            }
        },
    )
    print(response)


# x-ms-original-file: specification/app/resource-manager/Microsoft.App/preview/2023-08-01-preview/examples/ConnectedEnvironmentsDaprComponents_CreateOrUpdate.json
if __name__ == "__main__":
    main()
