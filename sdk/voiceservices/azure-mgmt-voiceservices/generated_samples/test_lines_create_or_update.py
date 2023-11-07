# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.identity import DefaultAzureCredential
from azure.mgmt.voiceservices import VoiceServicesMgmtClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-voiceservices
# USAGE
    python test_lines_create_or_update.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = VoiceServicesMgmtClient(
        credential=DefaultAzureCredential(),
        subscription_id="00000000-0000-0000-0000-000000000000",
    )

    response = client.test_lines.begin_create_or_update(
        resource_group_name="testrg",
        communications_gateway_name="myname",
        test_line_name="myline",
        resource={"location": "useast", "properties": {"phoneNumber": "+1-555-1234", "purpose": "Automated"}},
    ).result()
    print(response)


# x-ms-original-file: specification/voiceservices/resource-manager/Microsoft.VoiceServices/stable/2023-09-01/examples/TestLines_CreateOrUpdate.json
if __name__ == "__main__":
    main()
