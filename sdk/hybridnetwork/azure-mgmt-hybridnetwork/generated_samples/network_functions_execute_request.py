# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.identity import DefaultAzureCredential
from azure.mgmt.hybridnetwork import HybridNetworkManagementClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-hybridnetwork
# USAGE
    python network_functions_execute_request.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = HybridNetworkManagementClient(
        credential=DefaultAzureCredential(),
        subscription_id="subid",
    )

    client.network_functions.begin_execute_request(
        resource_group_name="rg",
        network_function_name="testNetworkfunction",
        parameters={
            "requestMetadata": {
                "apiVersion": "apiVersionQueryString",
                "httpMethod": "Post",
                "relativePath": "/simProfiles/testSimProfile",
                "serializedBody": '{"subscriptionProfile":"ChantestSubscription15","permanentKey":"00112233445566778899AABBCCDDEEFF","opcOperatorCode":"63bfa50ee6523365ff14c1f45f88737d","staticIpAddresses":{"internet":{"ipv4Addr":"198.51.100.1","ipv6Prefix":"2001:db8:abcd:12::0/64"},"another_network":{"ipv6Prefix":"2001:111:cdef:22::0/64"}}}',
            },
            "serviceEndpoint": "serviceEndpoint",
        },
    ).result()


# x-ms-original-file: specification/hybridnetwork/resource-manager/Microsoft.HybridNetwork/stable/2023-10-01/examples/NetworkFunctionsExecuteRequest.json
if __name__ == "__main__":
    main()
