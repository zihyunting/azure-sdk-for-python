# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum
from azure.core import CaseInsensitiveEnumMeta


class AdditionalOsPatch(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Additional VM Patching solution enabled on the Virtual Machine."""

    WU = "WU"
    WUMU = "WUMU"
    WSUS = "WSUS"


class AdditionalVmPatch(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Additional Patch to be enable or enabled on the SQL Virtual Machine."""

    NOT_SET = "NotSet"
    MICROSOFT_UPDATE = "MicrosoftUpdate"


class AssessmentDayOfWeek(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Day of the week to run assessment."""

    MONDAY = "Monday"
    TUESDAY = "Tuesday"
    WEDNESDAY = "Wednesday"
    THURSDAY = "Thursday"
    FRIDAY = "Friday"
    SATURDAY = "Saturday"
    SUNDAY = "Sunday"


class AutoBackupDaysOfWeek(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """AutoBackupDaysOfWeek."""

    MONDAY = "Monday"
    TUESDAY = "Tuesday"
    WEDNESDAY = "Wednesday"
    THURSDAY = "Thursday"
    FRIDAY = "Friday"
    SATURDAY = "Saturday"
    SUNDAY = "Sunday"


class BackupScheduleType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Backup schedule type."""

    MANUAL = "Manual"
    AUTOMATED = "Automated"


class ClusterConfiguration(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Cluster type."""

    DOMAINFUL = "Domainful"


class ClusterManagerType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Type of cluster manager: Windows Server Failover Cluster (WSFC), implied by the scale type of
    the group and the OS type.
    """

    WSFC = "WSFC"


class ClusterSubnetType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Cluster subnet type."""

    SINGLE_SUBNET = "SingleSubnet"
    MULTI_SUBNET = "MultiSubnet"


class Commit(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Replica commit mode in availability group."""

    SYNCHRONOUS_COMMIT = "Synchronous_Commit"
    ASYNCHRONOUS_COMMIT = "Asynchronous_Commit"


class ConnectivityType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """SQL Server connectivity option."""

    LOCAL = "LOCAL"
    PRIVATE = "PRIVATE"
    PUBLIC = "PUBLIC"


class CreatedByType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The type of identity that created the resource."""

    USER = "User"
    APPLICATION = "Application"
    MANAGED_IDENTITY = "ManagedIdentity"
    KEY = "Key"


class DayOfWeek(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Day of week to apply the patch on."""

    EVERYDAY = "Everyday"
    MONDAY = "Monday"
    TUESDAY = "Tuesday"
    WEDNESDAY = "Wednesday"
    THURSDAY = "Thursday"
    FRIDAY = "Friday"
    SATURDAY = "Saturday"
    SUNDAY = "Sunday"


class DiskConfigurationType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Disk configuration to apply to SQL Server."""

    NEW = "NEW"
    EXTEND = "EXTEND"
    ADD = "ADD"


class Failover(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Replica failover mode in availability group."""

    AUTOMATIC = "Automatic"
    MANUAL = "Manual"


class FullBackupFrequencyType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Frequency of full backups. In both cases, full backups begin during the next scheduled time
    window.
    """

    DAILY = "Daily"
    WEEKLY = "Weekly"


class IdentityType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The identity type. Set this to 'SystemAssigned' in order to automatically create and assign an
    Azure Active Directory principal for the resource.
    """

    NONE = "None"
    SYSTEM_ASSIGNED = "SystemAssigned"
    USER_ASSIGNED = "UserAssigned"
    SYSTEM_ASSIGNED_USER_ASSIGNED = "SystemAssigned,UserAssigned"


class LeastPrivilegeMode(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """SQL IaaS Agent least privilege mode."""

    ENABLED = "Enabled"
    NOT_SET = "NotSet"


class OperationOrigin(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The intended executor of the operation."""

    USER = "user"
    SYSTEM = "system"


class OsType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Operating System of the current SQL Virtual Machine."""

    WINDOWS = "Windows"
    LINUX = "Linux"


class ReadableSecondary(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Replica readable secondary mode in availability group."""

    NO = "No"
    ALL = "All"
    READ_ONLY = "Read_Only"


class Role(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Replica Role in availability group."""

    PRIMARY = "Primary"
    SECONDARY = "Secondary"


class ScaleType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Scale type."""

    HA = "HA"


class SqlImageSku(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """SQL Server edition type."""

    DEVELOPER = "Developer"
    EXPRESS = "Express"
    STANDARD = "Standard"
    ENTERPRISE = "Enterprise"
    WEB = "Web"


class SqlManagementMode(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """SQL Server Management type. NOTE: This parameter is not used anymore. API will automatically
    detect the Sql Management, refrain from using it.
    """

    FULL = "Full"
    LIGHT_WEIGHT = "LightWeight"
    NO_AGENT = "NoAgent"


class SqlServerLicenseType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """SQL Server license type."""

    PAYG = "PAYG"
    AHUB = "AHUB"
    DR = "DR"


class SqlVmGroupImageSku(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """SQL image sku."""

    DEVELOPER = "Developer"
    ENTERPRISE = "Enterprise"


class SqlWorkloadType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """SQL Server workload type."""

    GENERAL = "GENERAL"
    OLTP = "OLTP"
    DW = "DW"


class StorageWorkloadType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Storage workload type."""

    GENERAL = "GENERAL"
    OLTP = "OLTP"
    DW = "DW"


class TroubleshootingScenario(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """SQL VM troubleshooting scenario."""

    UNHEALTHY_REPLICA = "UnhealthyReplica"


class VmIdentityType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Identity type of the virtual machine. Specify None to opt-out of Managed Identities."""

    NONE = "None"
    SYSTEM_ASSIGNED = "SystemAssigned"
    USER_ASSIGNED = "UserAssigned"
