# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Any, IO, Union

from azure.identity import DefaultAzureCredential

from azure.mgmt.containerservice import ContainerServiceClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-containerservice
# USAGE
    python maintenance_configurations_create_update_maintenance_window.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = ContainerServiceClient(
        credential=DefaultAzureCredential(),
        subscription_id="00000000-0000-0000-0000-000000000000",
    )

    response = client.maintenance_configurations.create_or_update(
        resource_group_name="rg1",
        resource_name="clustername1",
        config_name="aksManagedAutoUpgradeSchedule",
        parameters={
            "properties": {
                "maintenanceWindow": {
                    "durationHours": 10,
                    "notAllowedDates": [
                        {"end": "2023-02-25", "start": "2023-02-18"},
                        {"end": "2024-01-05", "start": "2023-12-23"},
                    ],
                    "schedule": {"relativeMonthly": {"dayOfWeek": "Monday", "intervalMonths": 3, "weekIndex": "First"}},
                    "startDate": "2023-01-01",
                    "startTime": "08:30",
                    "utcOffset": "+05:30",
                }
            }
        },
    )
    print(response)


# x-ms-original-file: specification/containerservice/resource-manager/Microsoft.ContainerService/aks/preview/2024-03-02-preview/examples/MaintenanceConfigurationsCreate_Update_MaintenanceWindow.json
if __name__ == "__main__":
    main()
