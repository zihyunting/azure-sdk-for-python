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
    python load_balancer_create_gateway_load_balancer_consumer.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = NetworkManagementClient(
        credential=DefaultAzureCredential(),
        subscription_id="subid",
    )

    response = client.load_balancers.begin_create_or_update(
        resource_group_name="rg1",
        load_balancer_name="lb",
        parameters={
            "location": "eastus",
            "properties": {
                "backendAddressPools": [{"name": "be-lb", "properties": {}}],
                "frontendIPConfigurations": [
                    {
                        "name": "fe-lb",
                        "properties": {
                            "gatewayLoadBalancer": {
                                "id": "/subscriptions/subid/resourceGroups/rg1/providers/Microsoft.Network/loadBalancers/lb/frontendIPConfigurations/fe-lb-provider"
                            },
                            "subnet": {
                                "id": "/subscriptions/subid/resourceGroups/rg1/providers/Microsoft.Network/virtualNetworks/vnetlb/subnets/subnetlb"
                            },
                        },
                    }
                ],
                "inboundNatPools": [],
                "inboundNatRules": [
                    {
                        "name": "in-nat-rule",
                        "properties": {
                            "backendPort": 3389,
                            "enableFloatingIP": True,
                            "frontendIPConfiguration": {
                                "id": "/subscriptions/subid/resourceGroups/rg1/providers/Microsoft.Network/loadBalancers/lb/frontendIPConfigurations/fe-lb"
                            },
                            "frontendPort": 3389,
                            "idleTimeoutInMinutes": 15,
                            "protocol": "Tcp",
                        },
                    }
                ],
                "loadBalancingRules": [
                    {
                        "name": "rulelb",
                        "properties": {
                            "backendAddressPool": {
                                "id": "/subscriptions/subid/resourceGroups/rg1/providers/Microsoft.Network/loadBalancers/lb/backendAddressPools/be-lb"
                            },
                            "backendPort": 80,
                            "enableFloatingIP": True,
                            "frontendIPConfiguration": {
                                "id": "/subscriptions/subid/resourceGroups/rg1/providers/Microsoft.Network/loadBalancers/lb/frontendIPConfigurations/fe-lb"
                            },
                            "frontendPort": 80,
                            "idleTimeoutInMinutes": 15,
                            "loadDistribution": "Default",
                            "probe": {
                                "id": "/subscriptions/subid/resourceGroups/rg1/providers/Microsoft.Network/loadBalancers/lb/probes/probe-lb"
                            },
                            "protocol": "Tcp",
                        },
                    }
                ],
                "outboundRules": [],
                "probes": [
                    {
                        "name": "probe-lb",
                        "properties": {
                            "intervalInSeconds": 15,
                            "numberOfProbes": 2,
                            "port": 80,
                            "probeThreshold": 1,
                            "protocol": "Http",
                            "requestPath": "healthcheck.aspx",
                        },
                    }
                ],
            },
            "sku": {"name": "Standard"},
        },
    ).result()
    print(response)


# x-ms-original-file: specification/network/resource-manager/Microsoft.Network/stable/2023-11-01/examples/LoadBalancerCreateGatewayLoadBalancerConsumer.json
if __name__ == "__main__":
    main()
