# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.identity import DefaultAzureCredential
from azure.mgmt.maps import AzureMapsManagementClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-maps
# USAGE
    python delete_account.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = AzureMapsManagementClient(
        credential=DefaultAzureCredential(),
        subscription_id="21a9967a-e8a9-4656-a70b-96ff1c4d05a0",
    )

    client.accounts.delete(
        resource_group_name="myResourceGroup",
        account_name="myMapsAccount",
    )


# x-ms-original-file: specification/maps/resource-manager/Microsoft.Maps/preview/2023-08-01-preview/examples/DeleteAccount.json
if __name__ == "__main__":
    main()
