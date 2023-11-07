# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.identity import DefaultAzureCredential
from azure.mgmt.azurelargeinstance import AzureLargeInstance

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-azurelargeinstance
# USAGE
    python azure_large_storage_instance_list_by_subscription.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = AzureLargeInstance(
        credential=DefaultAzureCredential(),
        subscription_id="f0f4887f-d13c-4943-a8ba-d7da28d2a3fd",
    )

    response = client.azure_large_storage_instance.list_by_subscription()
    for item in response:
        print(item)


# x-ms-original-file: specification/azurelargeinstance/resource-manager/Microsoft.AzureLargeInstance/preview/2023-07-20-preview/examples/AzureLargeStorageInstance_ListBySubscription.json
if __name__ == "__main__":
    main()
