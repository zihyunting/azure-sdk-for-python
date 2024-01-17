# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.identity import DefaultAzureCredential
from azure.mgmt.apicenter import ApiCenterMgmtClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-apicenter
# USAGE
    python deployments_head.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = ApiCenterMgmtClient(
        credential=DefaultAzureCredential(),
        api_name="echo-api",
        version_name="VERSION_NAME",
        definition_name="DEFINITION_NAME",
        deployment_name="production",
        environment_name="ENVIRONMENT_NAME",
        metadata_schema_name="METADATA_SCHEMA_NAME",
        workspace_name="default",
        subscription_id="00000000-0000-0000-0000-000000000000",
    )

    response = client.deployments.head(
        resource_group_name="contoso-resources",
        service_name="contoso",
    )
    print(response)


# x-ms-original-file: specification/apicenter/resource-manager/Microsoft.ApiCenter/preview/2024-03-15-preview/examples/Deployments_Head.json
if __name__ == "__main__":
    main()
