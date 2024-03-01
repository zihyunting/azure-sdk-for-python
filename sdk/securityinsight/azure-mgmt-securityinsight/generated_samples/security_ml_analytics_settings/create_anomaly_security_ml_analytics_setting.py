# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.identity import DefaultAzureCredential
from azure.mgmt.securityinsight import SecurityInsights

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-securityinsight
# USAGE
    python create_anomaly_security_ml_analytics_setting.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = SecurityInsights(
        credential=DefaultAzureCredential(),
        subscription_id="d0cfe6b2-9ac0-4464-9919-dccaee2e48c0",
    )

    response = client.security_ml_analytics_settings.create_or_update(
        resource_group_name="myRg",
        workspace_name="myWorkspace",
        settings_resource_name="f209187f-1d17-4431-94af-c141bf5f23db",
        security_ml_analytics_setting={
            "etag": '"260090e2-0000-0d00-0000-5d6fb8670000"',
            "kind": "Anomaly",
            "properties": {
                "anomalySettingsVersion": 0,
                "anomalyVersion": "1.0.5",
                "customizableObservations": {
                    "multiSelectObservations": None,
                    "prioritizeExcludeObservations": None,
                    "singleSelectObservations": [
                        {
                            "description": "Select device vendor of network connection logs from CommonSecurityLog",
                            "name": "Device vendor",
                            "rerun": "RerunAlways",
                            "sequenceNumber": 1,
                            "supportedValues": ["Palo Alto Networks", "Fortinet", "Check Point"],
                            "supportedValuesKql": None,
                            "value": ["Palo Alto Networks"],
                            "valuesKql": None,
                        }
                    ],
                    "singleValueObservations": None,
                    "thresholdObservations": [
                        {
                            "description": "Suppress anomalies when daily data transfered (in MB) per hour is less than the chosen value",
                            "maximum": "100",
                            "minimum": "1",
                            "name": "Daily data transfer threshold in MB",
                            "rerun": "RerunAlways",
                            "sequenceNumber": 1,
                            "value": "25",
                        },
                        {
                            "description": "Triggers anomalies when number of standard deviations is greater than the chosen value",
                            "maximum": "10",
                            "minimum": "2",
                            "name": "Number of standard deviations",
                            "rerun": "RerunAlways",
                            "sequenceNumber": 2,
                            "value": "3",
                        },
                    ],
                },
                "description": "When account logs from a source region that has rarely been logged in from during the last 14 days, an anomaly is triggered.",
                "displayName": "Login from unusual region",
                "enabled": True,
                "frequency": "PT1H",
                "isDefaultSettings": True,
                "requiredDataConnectors": [{"connectorId": "AWS", "dataTypes": ["AWSCloudTrail"]}],
                "settingsDefinitionId": "f209187f-1d17-4431-94af-c141bf5f23db",
                "settingsStatus": "Production",
                "tactics": ["Exfiltration", "CommandAndControl"],
                "techniques": ["T1037", "T1021"],
            },
        },
    )
    print(response)


# x-ms-original-file: specification/securityinsights/resource-manager/Microsoft.SecurityInsights/preview/2024-03-01-preview/examples/securityMLAnalyticsSettings/CreateAnomalySecurityMLAnalyticsSetting.json
if __name__ == "__main__":
    main()
