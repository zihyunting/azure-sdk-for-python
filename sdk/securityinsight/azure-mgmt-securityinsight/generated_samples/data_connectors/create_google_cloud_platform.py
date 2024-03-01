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
    python create_google_cloud_platform.py

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
        data_connector_id="GCP_fce27b90-d6f5-4d30-991a-af509a2b50a1",
        data_connector={
            "kind": "GCP",
            "properties": {
                "auth": {
                    "projectNumber": "123456789012",
                    "serviceAccountEmail": "sentinel-service-account@project-id.iam.gserviceaccount.com",
                    "type": "GCP",
                    "workloadIdentityProviderId": "sentinel-identity-provider",
                },
                "connectorDefinitionName": "GcpConnector",
                "dcrConfig": {
                    "dataCollectionEndpoint": "https://microsoft-sentinel-datacollectionendpoint-123m.westeurope-1.ingest.monitor.azure.com",
                    "dataCollectionRuleImmutableId": "dcr-de21b053bd5a44beb99a256c9db85023",
                    "streamName": "SENTINEL_GCP_AUDIT_LOGS",
                },
                "request": {"projectId": "project-id", "subscriptionNames": ["sentinel-subscription"]},
            },
        },
    )
    print(response)


# x-ms-original-file: specification/securityinsights/resource-manager/Microsoft.SecurityInsights/preview/2024-03-01-preview/examples/dataConnectors/CreateGoogleCloudPlatform.json
if __name__ == "__main__":
    main()
