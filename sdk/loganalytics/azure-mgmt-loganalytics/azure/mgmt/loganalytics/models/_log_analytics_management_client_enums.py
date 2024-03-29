# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum
from azure.core import CaseInsensitiveEnumMeta


class BillingType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Configures whether billing will be only on the cluster or each workspace will be billed by its
    proportional use. This does not change the overall billing, only how it will be distributed.
    Default value is 'Cluster'.
    """

    CLUSTER = "Cluster"
    WORKSPACES = "Workspaces"


class Capacity(int, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The capacity reservation level in Gigabytes for this cluster."""

    ONE_HUNDRED = 100
    TWO_HUNDRED = 200
    THREE_HUNDRED = 300
    FOUR_HUNDRED = 400
    FIVE_HUNDRED = 500
    TEN_HUNDRED = 1000
    TWO_THOUSAND = 2000
    FIVE_THOUSAND = 5000
    TEN_THOUSAND = 10000
    TWENTY_FIVE_THOUSAND = 25000
    FIFTY_THOUSAND = 50000


class CapacityReservationLevel(int, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The capacity reservation level in GB for this workspace, when CapacityReservation sku is
    selected.
    """

    ONE_HUNDRED = 100
    TWO_HUNDRED = 200
    THREE_HUNDRED = 300
    FOUR_HUNDRED = 400
    FIVE_HUNDRED = 500
    TEN_HUNDRED = 1000
    TWO_THOUSAND = 2000
    FIVE_THOUSAND = 5000
    TEN_THOUSAND = 10000
    TWENTY_FIVE_THOUSAND = 25000
    FIFTY_THOUSAND = 50000


class ClusterEntityStatus(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The provisioning state of the cluster."""

    CREATING = "Creating"
    SUCCEEDED = "Succeeded"
    FAILED = "Failed"
    CANCELED = "Canceled"
    DELETING = "Deleting"
    PROVISIONING_ACCOUNT = "ProvisioningAccount"
    UPDATING = "Updating"


class ClusterSkuNameEnum(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The SKU (tier) of a cluster."""

    CAPACITY_RESERVATION = "CapacityReservation"


class ColumnDataTypeHintEnum(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Column data type logical hint."""

    URI = "uri"
    """A string that matches the pattern of a URI, for example,
    scheme://username:password@host:1234/this/is/a/path?k1=v1&k2=v2#fragment"""
    GUID = "guid"
    """A standard 128-bit GUID following the standard shape, xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"""
    ARM_PATH = "armPath"
    """An Azure Resource Model (ARM) path:
    /subscriptions/{...}/resourceGroups/{...}/providers/Microsoft.{...}/{...}/{...}/{...}..."""
    IP = "ip"
    """A standard V4/V6 ip address following the standard shape, x.x.x.x/y:y:y:y:y:y:y:y"""


class ColumnTypeEnum(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Column data type."""

    STRING = "string"
    INT_ENUM = "int"
    LONG = "long"
    REAL = "real"
    BOOLEAN = "boolean"
    DATE_TIME = "dateTime"
    GUID = "guid"
    DYNAMIC = "dynamic"


class CreatedByType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The type of identity that created the resource."""

    USER = "User"
    APPLICATION = "Application"
    MANAGED_IDENTITY = "ManagedIdentity"
    KEY = "Key"


class DataIngestionStatus(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The status of data ingestion for this workspace."""

    RESPECT_QUOTA = "RespectQuota"
    """Ingestion enabled following daily cap quota reset, or subscription enablement."""
    FORCE_ON = "ForceOn"
    """Ingestion started following service setting change."""
    FORCE_OFF = "ForceOff"
    """Ingestion stopped following service setting change."""
    OVER_QUOTA = "OverQuota"
    """Reached daily cap quota, ingestion stopped."""
    SUBSCRIPTION_SUSPENDED = "SubscriptionSuspended"
    """Ingestion stopped following suspended subscription."""
    APPROACHING_QUOTA = "ApproachingQuota"
    """80% of daily cap quota reached."""


class DataSourceKind(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The kind of the DataSource."""

    WINDOWS_EVENT = "WindowsEvent"
    WINDOWS_PERFORMANCE_COUNTER = "WindowsPerformanceCounter"
    IIS_LOGS = "IISLogs"
    LINUX_SYSLOG = "LinuxSyslog"
    LINUX_SYSLOG_COLLECTION = "LinuxSyslogCollection"
    LINUX_PERFORMANCE_OBJECT = "LinuxPerformanceObject"
    LINUX_PERFORMANCE_COLLECTION = "LinuxPerformanceCollection"
    CUSTOM_LOG = "CustomLog"
    CUSTOM_LOG_COLLECTION = "CustomLogCollection"
    AZURE_AUDIT_LOG = "AzureAuditLog"
    AZURE_ACTIVITY_LOG = "AzureActivityLog"
    GENERIC_DATA_SOURCE = "GenericDataSource"
    CHANGE_TRACKING_CUSTOM_PATH = "ChangeTrackingCustomPath"
    CHANGE_TRACKING_PATH = "ChangeTrackingPath"
    CHANGE_TRACKING_SERVICES = "ChangeTrackingServices"
    CHANGE_TRACKING_DATA_TYPE_CONFIGURATION = "ChangeTrackingDataTypeConfiguration"
    CHANGE_TRACKING_DEFAULT_REGISTRY = "ChangeTrackingDefaultRegistry"
    CHANGE_TRACKING_REGISTRY = "ChangeTrackingRegistry"
    CHANGE_TRACKING_LINUX_PATH = "ChangeTrackingLinuxPath"
    LINUX_CHANGE_TRACKING_PATH = "LinuxChangeTrackingPath"
    CHANGE_TRACKING_CONTENT_LOCATION = "ChangeTrackingContentLocation"
    WINDOWS_TELEMETRY = "WindowsTelemetry"
    OFFICE365 = "Office365"
    SECURITY_WINDOWS_BASELINE_CONFIGURATION = "SecurityWindowsBaselineConfiguration"
    SECURITY_CENTER_SECURITY_WINDOWS_BASELINE_CONFIGURATION = "SecurityCenterSecurityWindowsBaselineConfiguration"
    SECURITY_EVENT_COLLECTION_CONFIGURATION = "SecurityEventCollectionConfiguration"
    SECURITY_INSIGHTS_SECURITY_EVENT_COLLECTION_CONFIGURATION = "SecurityInsightsSecurityEventCollectionConfiguration"
    IMPORT_COMPUTER_GROUP = "ImportComputerGroup"
    NETWORK_MONITORING = "NetworkMonitoring"
    ITSM = "Itsm"
    DNS_ANALYTICS = "DnsAnalytics"
    APPLICATION_INSIGHTS = "ApplicationInsights"
    SQL_DATA_CLASSIFICATION = "SqlDataClassification"


class DataSourceType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Linked storage accounts type."""

    CUSTOM_LOGS = "CustomLogs"
    AZURE_WATSON = "AzureWatson"
    QUERY = "Query"
    INGESTION = "Ingestion"
    ALERTS = "Alerts"


class IdentityType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The type of identity that creates/modifies resources."""

    USER = "user"
    APPLICATION = "application"
    MANAGED_IDENTITY = "managedIdentity"
    KEY = "key"
    SYSTEM_ASSIGNED = "SystemAssigned"
    USER_ASSIGNED = "UserAssigned"
    NONE = "None"


class LinkedServiceEntityStatus(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The provisioning state of the linked service."""

    SUCCEEDED = "Succeeded"
    DELETING = "Deleting"
    PROVISIONING_ACCOUNT = "ProvisioningAccount"
    UPDATING = "Updating"


class ManagedServiceIdentityType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Type of managed service identity (where both SystemAssigned and UserAssigned types are
    allowed).
    """

    NONE = "None"
    SYSTEM_ASSIGNED = "SystemAssigned"
    USER_ASSIGNED = "UserAssigned"
    SYSTEM_ASSIGNED_USER_ASSIGNED = "SystemAssigned,UserAssigned"


class ProvisioningStateEnum(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Table's current provisioning state. If set to 'updating', indicates a resource lock due to
    ongoing operation, forbidding any update to the table until the ongoing operation is concluded.
    """

    UPDATING = "Updating"
    """Table schema is still being built and updated, table is currently locked for any changes till
    the procedure is done."""
    IN_PROGRESS = "InProgress"
    """Table schema is stable and without changes, table data is being updated."""
    SUCCEEDED = "Succeeded"
    """Table state is stable and without changes, table is unlocked and open for new updates."""
    DELETING = "Deleting"
    """Table state is deleting."""


class PublicNetworkAccessType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The network access type for operating on the Log Analytics Workspace. By default it is Enabled."""

    ENABLED = "Enabled"
    """Enables connectivity to Log Analytics through public DNS."""
    DISABLED = "Disabled"
    """Disables public connectivity to Log Analytics through public DNS."""


class PurgeState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Status of the operation represented by the requested Id."""

    PENDING = "pending"
    COMPLETED = "completed"


class SearchSortEnum(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The sort order of the search."""

    ASC = "asc"
    DESC = "desc"


class SkuNameEnum(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The name of the Service Tier."""

    FREE = "Free"
    STANDARD = "Standard"
    PREMIUM = "Premium"
    PER_NODE = "PerNode"
    PER_GB2018 = "PerGB2018"
    STANDALONE = "Standalone"
    CAPACITY_RESERVATION = "CapacityReservation"


class SourceEnum(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Table's creator."""

    MICROSOFT = "microsoft"
    """Tables provisioned by the system, as collected via Diagnostic Settings, the Agents, or any
    other standard data collection means."""
    CUSTOMER = "customer"
    """Tables created by the owner of the Workspace, and only found in this Workspace."""


class StorageInsightState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The state of the storage insight connection to the workspace."""

    OK = "OK"
    ERROR = "ERROR"


class TablePlanEnum(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Instruct the system how to handle and charge the logs ingested to this table."""

    BASIC = "Basic"
    """Logs  that are adjusted to support high volume low value verbose logs."""
    ANALYTICS = "Analytics"
    """Logs  that allow monitoring and analytics."""


class TableSubTypeEnum(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The subtype describes what APIs can be used to interact with the table, and what features are
    available against it.
    """

    ANY = "Any"
    """The default subtype with which built-in tables are created."""
    CLASSIC = "Classic"
    """Indicates a table created through the Data Collector API or with the custom logs feature of the
    MMA agent, or any table against which Custom Fields were created."""
    DATA_COLLECTION_RULE_BASED = "DataCollectionRuleBased"
    """A table eligible to have data sent into it via any of the means supported by Data Collection
    Rules: the Data Collection Endpoint API, ingestion-time transformations, or any other mechanism
    provided by Data Collection Rules"""


class TableTypeEnum(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Table's creator."""

    MICROSOFT = "Microsoft"
    """Standard data collected by Azure Monitor."""
    CUSTOM_LOG = "CustomLog"
    """Custom log table."""
    RESTORED_LOGS = "RestoredLogs"
    """Restored data."""
    SEARCH_RESULTS = "SearchResults"
    """Data collected by a search job."""


class Type(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The type of the destination resource."""

    STORAGE_ACCOUNT = "StorageAccount"
    EVENT_HUB = "EventHub"


class WorkspaceEntityStatus(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The provisioning state of the workspace."""

    CREATING = "Creating"
    SUCCEEDED = "Succeeded"
    FAILED = "Failed"
    CANCELED = "Canceled"
    DELETING = "Deleting"
    PROVISIONING_ACCOUNT = "ProvisioningAccount"
    UPDATING = "Updating"


class WorkspaceSkuNameEnum(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The name of the SKU."""

    FREE = "Free"
    STANDARD = "Standard"
    PREMIUM = "Premium"
    PER_NODE = "PerNode"
    PER_GB2018 = "PerGB2018"
    STANDALONE = "Standalone"
    CAPACITY_RESERVATION = "CapacityReservation"
    LA_CLUSTER = "LACluster"
