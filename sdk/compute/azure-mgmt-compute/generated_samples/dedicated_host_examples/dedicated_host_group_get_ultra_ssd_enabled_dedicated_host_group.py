# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.identity import DefaultAzureCredential
from azure.mgmt.compute import ComputeManagementClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-compute
# USAGE
    python dedicated_host_group_get_ultra_ssd_enabled_dedicated_host_group.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = ComputeManagementClient(
        credential=DefaultAzureCredential(),
        subscription_id="{subscriptionId}",
    )

    response = client.dedicated_host_groups.get(
        resource_group_name="myResourceGroup",
        host_group_name="myDedicatedHostGroup",
    )
    print(response)


# x-ms-original-file: specification/compute/resource-manager/Microsoft.Compute/ComputeRP/stable/2023-07-01/examples/dedicatedHostExamples/DedicatedHostGroup_Get_UltraSSDEnabledDedicatedHostGroup.json
if __name__ == "__main__":
    main()
