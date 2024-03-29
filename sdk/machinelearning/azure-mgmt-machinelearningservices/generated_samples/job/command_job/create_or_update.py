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
    python create_or_update.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = MachineLearningServicesMgmtClient(
        credential=DefaultAzureCredential(),
        subscription_id="00000000-1111-2222-3333-444444444444",
    )

    response = client.jobs.create_or_update(
        resource_group_name="test-rg",
        workspace_name="my-aml-workspace",
        id="string",
        body={
            "properties": {
                "autologgerSettings": {"mlflowAutologger": "Disabled"},
                "codeId": "string",
                "command": "string",
                "componentId": "string",
                "computeId": "string",
                "description": "string",
                "displayName": "string",
                "distribution": {"distributionType": "TensorFlow", "parameterServerCount": 1, "workerCount": 1},
                "environmentId": "string",
                "environmentVariables": {"string": "string"},
                "experimentName": "string",
                "identity": {"identityType": "AMLToken"},
                "inputs": {"string": {"description": "string", "jobInputType": "literal", "value": "string"}},
                "isArchived": False,
                "jobType": "Command",
                "limits": {"jobLimitsType": "Command", "timeout": "PT5M"},
                "notificationSetting": {"emailOn": ["JobCancelled"], "emails": ["string"]},
                "outputs": {
                    "string": {
                        "assetName": "string",
                        "assetVersion": "string",
                        "description": "string",
                        "jobOutputType": "uri_file",
                        "mode": "Upload",
                        "uri": "string",
                    }
                },
                "properties": {"string": "string"},
                "queueSettings": {"jobTier": "Basic", "priority": 1},
                "resources": {
                    "dockerArgs": "string",
                    "instanceCount": 1,
                    "instanceType": "string",
                    "locations": ["string"],
                    "properties": {"string": {"c9ac10d0-915b-4de5-afe8-a4c78a37a558": None}},
                    "shmSize": "2g",
                },
                "services": {
                    "string": {
                        "endpoint": "string",
                        "jobServiceType": "string",
                        "nodes": {"nodesValueType": "All"},
                        "port": 1,
                        "properties": {"string": "string"},
                    }
                },
                "tags": {"string": "string"},
            }
        },
    )
    print(response)


# x-ms-original-file: specification/machinelearningservices/resource-manager/Microsoft.MachineLearningServices/preview/2024-04-01-preview/examples/Job/CommandJob/createOrUpdate.json
if __name__ == "__main__":
    main()
