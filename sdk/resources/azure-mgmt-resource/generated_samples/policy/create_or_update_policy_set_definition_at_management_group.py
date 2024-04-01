# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Any, IO, Union

from azure.identity import DefaultAzureCredential

from azure.mgmt.resource import PolicyClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-resource
# USAGE
    python create_or_update_policy_set_definition_at_management_group.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = PolicyClient(
        credential=DefaultAzureCredential(),
        policy_definition_name="POLICY_DEFINITION_NAME",
        policy_definition_version="POLICY_DEFINITION_VERSION",
        policy_set_definition_name="CostManagement",
        subscription_id="SUBSCRIPTION_ID",
    )

    response = client.policy_set_definitions.create_or_update_at_management_group(
        management_group_id="MyManagementGroup",
        policy_set_definition_name="CostManagement",
        parameters={
            "properties": {
                "description": "Policies to enforce low cost storage SKUs",
                "displayName": "Cost Management",
                "metadata": {"category": "Cost Management"},
                "policyDefinitions": [
                    {
                        "parameters": {"listOfAllowedSKUs": {"value": ["Standard_GRS", "Standard_LRS"]}},
                        "policyDefinitionId": "/providers/Microsoft.Management/managementgroups/MyManagementGroup/providers/Microsoft.Authorization/policyDefinitions/7433c107-6db4-4ad1-b57a-a76dce0154a1",
                        "policyDefinitionReferenceId": "Limit_Skus",
                    },
                    {
                        "parameters": {"prefix": {"value": "DeptA"}, "suffix": {"value": "-LC"}},
                        "policyDefinitionId": "/providers/Microsoft.Management/managementgroups/MyManagementGroup/providers/Microsoft.Authorization/policyDefinitions/ResourceNaming",
                        "policyDefinitionReferenceId": "Resource_Naming",
                    },
                ],
            }
        },
    )
    print(response)


# x-ms-original-file: specification/resources/resource-manager/Microsoft.Authorization/stable/2023-04-01/examples/createOrUpdatePolicySetDefinitionAtManagementGroup.json
if __name__ == "__main__":
    main()
