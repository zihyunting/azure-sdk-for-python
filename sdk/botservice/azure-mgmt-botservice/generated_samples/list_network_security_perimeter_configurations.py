# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.identity import DefaultAzureCredential
from azure.mgmt.botservice import AzureBotService

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-botservice
# USAGE
    python list_network_security_perimeter_configurations.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = AzureBotService(
        credential=DefaultAzureCredential(),
        subscription_id="subId",
    )

    response = client.network_security_perimeter_configurations.list(
        resource_group_name="rgName",
        resource_name="botId",
    )
    for item in response:
        print(item)


# x-ms-original-file: specification/botservice/resource-manager/Microsoft.BotService/preview/2023-09-15-preview/examples/ListNetworkSecurityPerimeterConfigurations.json
if __name__ == "__main__":
    main()
