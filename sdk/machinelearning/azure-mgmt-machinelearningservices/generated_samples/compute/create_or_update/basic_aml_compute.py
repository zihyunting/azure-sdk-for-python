# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Any, IO, Union

from azure.identity import DefaultAzureCredential

from azure.mgmt.machinelearningservices import MachineLearningServicesMgmtClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-machinelearningservices
# USAGE
    python basic_aml_compute.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = MachineLearningServicesMgmtClient(
        credential=DefaultAzureCredential(),
        subscription_id="34adfa4f-cedf-4dc0-ba29-b6d1a69ab345",
    )

    response = client.compute.begin_create_or_update(
        resource_group_name="testrg123",
        workspace_name="workspaces123",
        compute_name="compute123",
        parameters={
            "location": "eastus",
            "properties": {
                "computeType": "AmlCompute",
                "properties": {
                    "enableNodePublicIp": True,
                    "isolatedNetwork": False,
                    "osType": "Windows",
                    "remoteLoginPortPublicAccess": "NotSpecified",
                    "scaleSettings": {"maxNodeCount": 1, "minNodeCount": 0, "nodeIdleTimeBeforeScaleDown": "PT5M"},
                    "virtualMachineImage": {
                        "id": "/subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/myResourceGroup/providers/Microsoft.Compute/galleries/myImageGallery/images/myImageDefinition/versions/0.0.1"
                    },
                    "vmPriority": "Dedicated",
                    "vmSize": "STANDARD_NC6",
                },
            },
        },
    ).result()
    print(response)


# x-ms-original-file: specification/machinelearningservices/resource-manager/Microsoft.MachineLearningServices/preview/2024-04-01-preview/examples/Compute/createOrUpdate/BasicAmlCompute.json
if __name__ == "__main__":
    main()
