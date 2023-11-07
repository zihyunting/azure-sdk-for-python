# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.identity import DefaultAzureCredential
from azure.mgmt.sql import SqlManagementClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-sql
# USAGE
    python managed_database_sensitivity_labels_current_update.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = SqlManagementClient(
        credential=DefaultAzureCredential(),
        subscription_id="00000000-1111-2222-3333-444444444444",
    )

    client.managed_database_sensitivity_labels.update(
        resource_group_name="myRG",
        managed_instance_name="myManagedInstanceName",
        database_name="myDatabase",
        parameters={
            "operations": [
                {
                    "properties": {
                        "column": "column1",
                        "op": "set",
                        "schema": "dbo",
                        "sensitivityLabel": {
                            "properties": {
                                "informationType": "Financial",
                                "informationTypeId": "1D3652D6-422C-4115-82F1-65DAEBC665C8",
                                "labelId": "3A477B16-9423-432B-AA97-6069B481CEC3",
                                "labelName": "Highly Confidential",
                            }
                        },
                        "table": "table1",
                    }
                },
                {
                    "properties": {
                        "column": "column2",
                        "op": "set",
                        "schema": "dbo",
                        "sensitivityLabel": {
                            "properties": {
                                "informationType": "PhoneNumber",
                                "informationTypeId": "d22fa6e9-5ee4-3bde-4c2b-a409604c4646",
                                "labelId": "bf91e08c-f4f0-478a-b016-25164b2a65ff",
                                "labelName": "PII",
                            }
                        },
                        "table": "table2",
                    }
                },
                {"properties": {"column": "Column3", "op": "remove", "schema": "dbo", "table": "Table1"}},
            ]
        },
    )


# x-ms-original-file: specification/sql/resource-manager/Microsoft.Sql/preview/2023-05-01-preview/examples/ManagedDatabaseSensitivityLabelsCurrentUpdate.json
if __name__ == "__main__":
    main()
