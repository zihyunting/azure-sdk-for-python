# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.identity import DefaultAzureCredential
from azure.mgmt.securityinsight import SecurityInsights

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-securityinsight
# USAGE
    python create_microsoft_threat_protection_data_connetor.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = SecurityInsights(
        credential=DefaultAzureCredential(),
        subscription_id="d0cfe6b2-9ac0-4464-9919-dccaee2e48c0",
    )

    response = client.data_connectors.create_or_update(
        resource_group_name="myRg",
        workspace_name="myWorkspace",
        data_connector_id="73e01a99-5cd7-4139-a149-9f2736ff2ab5",
        data_connector={
            "etag": '"0300bf09-0000-0000-0000-5c37296e0000"',
            "kind": "MicrosoftThreatProtection",
            "properties": {
                "dataTypes": {"alerts": {"state": "Enabled"}, "incidents": {"state": "Disabled"}},
                "filteredProviders": {"alerts": ["microsoftDefenderForCloudApps"]},
                "tenantId": "178265c4-3136-4ff6-8ed1-b5b62b4cb5f5",
            },
        },
    )
    print(response)


# x-ms-original-file: specification/securityinsights/resource-manager/Microsoft.SecurityInsights/preview/2024-03-01-preview/examples/dataConnectors/CreateMicrosoftThreatProtectionDataConnetor.json
if __name__ == "__main__":
    main()
