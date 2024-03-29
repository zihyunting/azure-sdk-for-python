# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Any, IO, Union

from azure.identity import DefaultAzureCredential

from azure.mgmt.managednetworkfabric import ManagedNetworkFabricMgmtClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-managednetworkfabric
# USAGE
    python network_taps_update_maximum_set_gen.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = ManagedNetworkFabricMgmtClient(
        credential=DefaultAzureCredential(),
        subscription_id="1234ABCD-0A1B-1234-5678-123456ABCDEF",
    )

    response = client.network_taps.begin_update(
        resource_group_name="example-rg",
        network_tap_name="example-networkTap",
        body={
            "properties": {
                "annotation": "annotation1",
                "destinations": [
                    {
                        "destinationId": "/subscriptions/1234ABCD-0A1B-1234-5678-123456ABCDEF/resourcegroups/example-rg/providers/Microsoft.ManagedNetworkFabric/l3IsloationDomains/example-l3Domain/internalNetworks/example-internalNetwork",
                        "destinationTapRuleId": "/subscriptions/xxxx-xxxx-xxxx-xxxx/resourcegroups/example-rg/providers/Microsoft.ManagedNetworkFabric/networkTapRules/example-destinationTapRule",
                        "destinationType": "IsolationDomain",
                        "isolationDomainProperties": {
                            "encapsulation": "None",
                            "neighborGroupIds": [
                                "/subscriptions/1234ABCD-0A1B-1234-5678-123456ABCDEF/resourcegroups/example-rg/providers/Microsoft.ManagedNetworkFabric/neighborGroups/example-neighborGroup"
                            ],
                        },
                        "name": "example-destinaionName",
                    }
                ],
                "pollingType": "Pull",
            },
            "tags": {"key6024": "1234"},
        },
    ).result()
    print(response)


# x-ms-original-file: specification/managednetworkfabric/resource-manager/Microsoft.ManagedNetworkFabric/stable/2023-06-15/examples/NetworkTaps_Update_MaximumSet_Gen.json
if __name__ == "__main__":
    main()
