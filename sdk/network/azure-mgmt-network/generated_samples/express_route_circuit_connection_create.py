# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.identity import DefaultAzureCredential
from azure.mgmt.network import NetworkManagementClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-network
# USAGE
    python express_route_circuit_connection_create.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = NetworkManagementClient(
        credential=DefaultAzureCredential(),
        subscription_id="subid1",
    )

    response = client.express_route_circuit_connections.begin_create_or_update(
        resource_group_name="rg1",
        circuit_name="ExpressRouteARMCircuitA",
        peering_name="AzurePrivatePeering",
        connection_name="circuitConnectionUSAUS",
        express_route_circuit_connection_parameters={
            "properties": {
                "addressPrefix": "10.0.0.0/29",
                "authorizationKey": "946a1918-b7a2-4917-b43c-8c4cdaee006a",
                "expressRouteCircuitPeering": {
                    "id": "/subscriptions/subid1/resourceGroups/dedharcktinit/providers/Microsoft.Network/expressRouteCircuits/dedharcktlocal/peerings/AzurePrivatePeering"
                },
                "ipv6CircuitConnectionConfig": {"addressPrefix": "aa:bb::/125"},
                "peerExpressRouteCircuitPeering": {
                    "id": "/subscriptions/subid2/resourceGroups/dedharcktpeer/providers/Microsoft.Network/expressRouteCircuits/dedharcktremote/peerings/AzurePrivatePeering"
                },
            }
        },
    ).result()
    print(response)


# x-ms-original-file: specification/network/resource-manager/Microsoft.Network/stable/2023-11-01/examples/ExpressRouteCircuitConnectionCreate.json
if __name__ == "__main__":
    main()
