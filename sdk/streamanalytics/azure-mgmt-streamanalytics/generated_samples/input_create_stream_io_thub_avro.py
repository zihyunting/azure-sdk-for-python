# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.identity import DefaultAzureCredential
from azure.mgmt.streamanalytics import StreamAnalyticsManagementClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-streamanalytics
# USAGE
    python input_create_stream_io_thub_avro.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = StreamAnalyticsManagementClient(
        credential=DefaultAzureCredential(),
        subscription_id="56b5e0a9-b645-407d-99b0-c64f86013e3d",
    )

    response = client.inputs.create_or_replace(
        resource_group_name="sjrg3467",
        job_name="sj9742",
        input_name="input7970",
        input={
            "properties": {
                "datasource": {
                    "properties": {
                        "consumerGroupName": "sdkconsumergroup",
                        "endpoint": "messages/events",
                        "iotHubNamespace": "iothub",
                        "sharedAccessPolicyKey": "sharedAccessPolicyKey=",
                        "sharedAccessPolicyName": "owner",
                    },
                    "type": "Microsoft.Devices/IotHubs",
                },
                "serialization": {"type": "Avro"},
                "type": "Stream",
            }
        },
    )
    print(response)


# x-ms-original-file: specification/streamanalytics/resource-manager/Microsoft.StreamAnalytics/stable/2020-03-01/examples/Input_Create_Stream_IoTHub_Avro.json
if __name__ == "__main__":
    main()
