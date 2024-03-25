# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Any, IO, Union

from azure.identity import DefaultAzureCredential

from azure.mgmt.monitor import MonitorManagementClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-monitor
# USAGE
    python patch_action_group.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = MonitorManagementClient(
        credential=DefaultAzureCredential(),
        subscription_id="187f412d-1758-44d9-b052-169e2564721d",
    )

    response = client.action_groups.update(
        resource_group_name="Default-NotificationRules",
        action_group_name="SampleActionGroup",
        action_group_patch={"properties": {"enabled": False}, "tags": {"key1": "value1", "key2": "value2"}},
    )
    print(response)


# x-ms-original-file: specification/monitor/resource-manager/Microsoft.Insights/stable/2023-01-01/examples/patchActionGroup.json
if __name__ == "__main__":
    main()
