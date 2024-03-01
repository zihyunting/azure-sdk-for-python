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
    python create_hunt.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = SecurityInsights(
        credential=DefaultAzureCredential(),
        subscription_id="bd794837-4d29-4647-9105-6339bfdb4e6a",
    )

    response = client.hunts.create_or_update(
        resource_group_name="myRg",
        workspace_name="myWorkspace",
        hunt_id="163e7b2a-a2ec-4041-aaba-d878a38f265f",
        hunt={
            "properties": {
                "attackTactics": ["Reconnaissance"],
                "attackTechniques": ["T1595"],
                "description": "Log4J Hunt Description",
                "displayName": "Log4J new hunt",
                "hypothesisStatus": "Unknown",
                "labels": ["Label1", "Label2"],
                "owner": {"objectId": "873b5263-5d34-4149-b356-ad341b01e123"},
                "status": "New",
            }
        },
    )
    print(response)


# x-ms-original-file: specification/securityinsights/resource-manager/Microsoft.SecurityInsights/preview/2024-03-01-preview/examples/hunts/CreateHunt.json
if __name__ == "__main__":
    main()
