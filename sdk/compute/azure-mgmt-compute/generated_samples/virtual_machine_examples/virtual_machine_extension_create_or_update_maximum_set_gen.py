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
    python virtual_machine_extension_create_or_update_maximum_set_gen.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = ComputeManagementClient(
        credential=DefaultAzureCredential(),
        subscription_id="{subscription-id}",
    )

    response = client.virtual_machine_extensions.begin_create_or_update(
        resource_group_name="rgcompute",
        vm_name="aaaaaaaaaaaaaaaaaaaaaaaa",
        vm_extension_name="aaaaaaaaaaaaa",
        extension_parameters={
            "location": "westus",
            "properties": {
                "autoUpgradeMinorVersion": True,
                "enableAutomaticUpgrade": True,
                "forceUpdateTag": "a",
                "instanceView": {
                    "name": "aaaaaaaaaaaaaaaaa",
                    "statuses": [
                        {
                            "code": "aaaaaaaaaaaaaaaaaaaaaaa",
                            "displayStatus": "aaaaaa",
                            "level": "Info",
                            "message": "a",
                            "time": "2021-11-30T12:58:26.522Z",
                        }
                    ],
                    "substatuses": [
                        {
                            "code": "aaaaaaaaaaaaaaaaaaaaaaa",
                            "displayStatus": "aaaaaa",
                            "level": "Info",
                            "message": "a",
                            "time": "2021-11-30T12:58:26.522Z",
                        }
                    ],
                    "type": "aaaaaaaaa",
                    "typeHandlerVersion": "aaaaaaaaaaaaaaaaaaaaaaaaaa",
                },
                "protectedSettings": {},
                "publisher": "extPublisher",
                "settings": {},
                "suppressFailures": True,
                "type": "extType",
                "typeHandlerVersion": "1.2",
            },
            "tags": {"key9183": "aa"},
        },
    ).result()
    print(response)


# x-ms-original-file: specification/compute/resource-manager/Microsoft.Compute/ComputeRP/stable/2023-07-01/examples/virtualMachineExamples/VirtualMachineExtension_CreateOrUpdate_MaximumSet_Gen.json
if __name__ == "__main__":
    main()
