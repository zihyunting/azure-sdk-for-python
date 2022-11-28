# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.identity import DefaultAzureCredential
from azure.mgmt.recoveryservicessiterecovery import SiteRecoveryManagementClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-recoveryservicessiterecovery
# USAGE
    python replication_protection_containers_switch_protection.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = SiteRecoveryManagementClient(
        credential=DefaultAzureCredential(),
        subscription_id="42195872-7e70-4f8a-837f-84b28ecbb78b",
        resource_group_name="priyanprg",
        resource_name="priyanponeboxvault",
    )

    response = client.replication_protection_containers.begin_switch_protection(
        fabric_name="CentralUSCanSite",
        protection_container_name="CentralUSCancloud",
        switch_input={
            "properties": {
                "providerSpecificDetails": {"instanceType": "A2A"},
                "replicationProtectedItemName": "a2aSwapOsVm",
            }
        },
    ).result()
    print(response)


# x-ms-original-file: specification/recoveryservicessiterecovery/resource-manager/Microsoft.RecoveryServices/stable/2022-10-01/examples/ReplicationProtectionContainers_SwitchProtection.json
if __name__ == "__main__":
    main()
