# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Any, IO, Union

from azure.identity import DefaultAzureCredential

from azure.mgmt.appcontainers import ContainerAppsAPIClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-appcontainers
# USAGE
    python managed_environments_create_or_update.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = ContainerAppsAPIClient(
        credential=DefaultAzureCredential(),
        container_app_name="CONTAINER_APP_NAME",
        subscription_id="34adfa4f-cedf-4dc0-ba29-b6d1a69ab345",
    )

    response = client.managed_environments.begin_create_or_update(
        resource_group_name="examplerg",
        environment_name="testcontainerenv",
        environment_envelope={
            "identity": {
                "type": "SystemAssigned, UserAssigned",
                "userAssignedIdentities": {
                    "/subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/contoso-resources/providers/Microsoft.ManagedIdentity/userAssignedIdentities/contoso-identity": {}
                },
            },
            "location": "East US",
            "properties": {
                "appInsightsConfiguration": {
                    "connectionString": "InstrumentationKey=00000000-0000-0000-0000-000000000000;IngestionEndpoint=https://eastus-8.in.applicationinsights.azure.com/;LiveEndpoint=https://eastus.livediagnostics.monitor.azure.com/"
                },
                "appLogsConfiguration": {
                    "logAnalyticsConfiguration": {
                        "customerId": "string",
                        "dynamicJsonColumns": True,
                        "sharedKey": "string",
                    }
                },
                "customDomainConfiguration": {
                    "certificatePassword": "1234",
                    "certificateValue": "Y2VydA==",
                    "dnsSuffix": "www.my-name.com",
                },
                "daprAIConnectionString": "InstrumentationKey=00000000-0000-0000-0000-000000000000;IngestionEndpoint=https://northcentralus-0.in.applicationinsights.azure.com/",
                "openTelemetryConfiguration": {
                    "destinationsConfiguration": {
                        "dataDogConfiguration": {"key": "000000000000000000000000", "site": "string"},
                        "otlpConfigurations": [
                            {
                                "endpoint": "dashboard.k8s.region.azurecontainerapps.io:80",
                                "headers": [{"key": "api-key", "value": "xxxxxxxxxxx"}],
                                "insecure": True,
                                "name": "dashboard",
                            }
                        ],
                    },
                    "logsConfiguration": {"destinations": ["appInsights"]},
                    "metricsConfiguration": {"destinations": ["dataDog"]},
                    "tracesConfiguration": {"destinations": ["appInsights"]},
                },
                "peerAuthentication": {"mtls": {"enabled": True}},
                "peerTrafficConfiguration": {"encryption": {"enabled": True}},
                "vnetConfiguration": {
                    "infrastructureSubnetId": "/subscriptions/34adfa4f-cedf-4dc0-ba29-b6d1a69ab345/resourceGroups/RGName/providers/Microsoft.Network/virtualNetworks/VNetName/subnets/subnetName1"
                },
                "workloadProfiles": [
                    {
                        "maximumCount": 12,
                        "minimumCount": 3,
                        "name": "My-GP-01",
                        "workloadProfileType": "GeneralPurpose",
                    },
                    {
                        "maximumCount": 6,
                        "minimumCount": 3,
                        "name": "My-MO-01",
                        "workloadProfileType": "MemoryOptimized",
                    },
                    {
                        "maximumCount": 6,
                        "minimumCount": 3,
                        "name": "My-CO-01",
                        "workloadProfileType": "ComputeOptimized",
                    },
                    {"name": "My-consumption-01", "workloadProfileType": "Consumption"},
                ],
                "zoneRedundant": True,
            },
        },
    ).result()
    print(response)


# x-ms-original-file: specification/app/resource-manager/Microsoft.App/preview/2024-02-02-preview/examples/ManagedEnvironments_CreateOrUpdate.json
if __name__ == "__main__":
    main()
