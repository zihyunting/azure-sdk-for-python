# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum
from azure.core import CaseInsensitiveEnumMeta


class AuthenticationProvisioningState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """State of the multi-cloud connector."""

    VALID = "Valid"
    """Valid connector"""
    INVALID = "Invalid"
    """Invalid connector"""
    EXPIRED = "Expired"
    """the connection has expired"""
    INCORRECT_POLICY = "IncorrectPolicy"
    """Incorrect policy of the connector"""


class AuthenticationType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Connect to your cloud account, for AWS use either account credentials or role-based
    authentication. For GCP use account organization credentials.
    """

    AWS_CREDS = "awsCreds"
    """AWS cloud account connector user credentials authentication"""
    AWS_ASSUME_ROLE = "awsAssumeRole"
    """AWS account connector assume role authentication"""
    GCP_CREDENTIALS = "gcpCredentials"
    """GCP account connector service to service authentication"""


class AutoProvision(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Whether or not to automatically install Azure Arc (hybrid compute) agents on machines."""

    ON = "On"
    """Install missing Azure Arc agents on machines automatically"""
    OFF = "Off"
    """Do not install Azure Arc agent on the machines automatically"""


class HybridComputeProvisioningState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """State of the service principal and its secret."""

    VALID = "Valid"
    """Valid service principal details."""
    INVALID = "Invalid"
    """Invalid service principal details."""
    EXPIRED = "Expired"
    """the service principal details are expired"""


class MinimalSeverity(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Defines the minimal alert severity which will be sent as email notifications."""

    HIGH = "High"
    """Get notifications on new alerts with High severity"""
    MEDIUM = "Medium"
    """Get notifications on new alerts with medium or high severity"""
    LOW = "Low"
    """Don't get notifications on new alerts with low, medium or high severity"""


class PermissionProperty(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """A permission detected in the cloud account."""

    AWS_AWS_SECURITY_HUB_READ_ONLY_ACCESS = "AWS::AWSSecurityHubReadOnlyAccess"
    """This permission provides read only access to AWS Security Hub resources."""
    AWS_SECURITY_AUDIT = "AWS::SecurityAudit"
    """This permission grants access to read security configuration metadata."""
    AWS_AMAZON_SSM_AUTOMATION_ROLE = "AWS::AmazonSSMAutomationRole"
    """The permission provides for EC2 Automation service to execute activities defined within
    #: Automation documents."""
    GCP_SECURITY_CENTER_ADMIN_VIEWER = "GCP::Security Center Admin Viewer"
    """This permission provides read only access to GCP Security Command Center."""


class Roles(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """A possible role to configure sending security notification alerts to."""

    ACCOUNT_ADMIN = "AccountAdmin"
    """If enabled, send notification on new alerts to the account admins"""
    SERVICE_ADMIN = "ServiceAdmin"
    """If enabled, send notification on new alerts to the service admins"""
    OWNER = "Owner"
    """If enabled, send notification on new alerts to the subscription owners"""
    CONTRIBUTOR = "Contributor"
    """If enabled, send notification on new alerts to the subscription contributors"""


class State(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Defines if email notifications will be sent about new security alerts."""

    ON = "On"
    """Get notifications on new alerts"""
    OFF = "Off"
    """Don't get notifications on new alerts"""
