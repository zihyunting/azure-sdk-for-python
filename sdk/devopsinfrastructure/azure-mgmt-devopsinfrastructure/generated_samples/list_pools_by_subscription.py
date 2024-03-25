# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.identity import DefaultAzureCredential

from azure.mgmt.devopsinfrastructure import ManagedDevOpsInfrastructure

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-devopsinfrastructure
# USAGE
    python list_pools_by_subscription.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = ManagedDevOpsInfrastructure(
        credential=DefaultAzureCredential(),
        subscription_id="a2e95d27-c161-4b61-bda4-11512c14c2c2",
    )

    response = client.pools.list_by_subscription()
    for item in response:
        print(item)


# x-ms-original-file: specification/devopsinfrastructure/resource-manager/Microsoft.DevOpsInfrastructure/preview/2023-12-13-preview/examples/ListPoolsBySubscription.json
if __name__ == "__main__":
    main()
