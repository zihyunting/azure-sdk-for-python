# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Any, IO, Union

from azure.identity import DefaultAzureCredential

from azure.mgmt.servicenetworking import ServiceNetworkingMgmtClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-servicenetworking
# USAGE
    python traffic_controller_patch.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = ServiceNetworkingMgmtClient(
        credential=DefaultAzureCredential(),
        subscription_id="subid",
    )

    response = client.traffic_controller_interface.update(
        resource_group_name="rg1",
        traffic_controller_name="tc1",
        properties={"tags": {"key1": "value1"}},
    )
    print(response)


# x-ms-original-file: specification/servicenetworking/resource-manager/Microsoft.ServiceNetworking/stable/2023-11-01/examples/TrafficControllerPatch.json
if __name__ == "__main__":
    main()
