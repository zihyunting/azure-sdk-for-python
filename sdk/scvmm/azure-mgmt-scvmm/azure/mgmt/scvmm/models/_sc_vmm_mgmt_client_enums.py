# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum
from azure.core import CaseInsensitiveEnumMeta


class ActionType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Enum. Indicates the action type. "Internal" refers to actions that are for internal only APIs."""

    INTERNAL = "Internal"


class AllocationMethod(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Network address allocation method."""

    DYNAMIC = "Dynamic"
    """Dynamically allocated address."""
    STATIC = "Static"
    """Statically allocated address."""


class CreatedByType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The type of identity that created the resource."""

    USER = "User"
    APPLICATION = "Application"
    MANAGED_IDENTITY = "ManagedIdentity"
    KEY = "Key"


class CreateDiffDisk(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Create diff disk."""

    TRUE = "true"
    """Enable create diff disk."""
    FALSE = "false"
    """Disable create diff disk."""


class DeleteFromHost(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """DeleteFromHost."""

    TRUE = "true"
    """Enable delete from host."""
    FALSE = "false"
    """Disable delete from host."""


class DynamicMemoryEnabled(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Dynamic memory enabled."""

    TRUE = "true"
    """Enable dynamic memory."""
    FALSE = "false"
    """Disable dynamic memory."""


class ForceDelete(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """ForceDelete."""

    TRUE = "true"
    """Enable force delete."""
    FALSE = "false"
    """Disable force delete."""


class InventoryType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The inventory type."""

    CLOUD = "Cloud"
    """Cloud inventory type"""
    VIRTUAL_NETWORK = "VirtualNetwork"
    """VirtualNetwork inventory type"""
    VIRTUAL_MACHINE = "VirtualMachine"
    """VirtualMachine inventory type"""
    VIRTUAL_MACHINE_TEMPLATE = "VirtualMachineTemplate"
    """VirtualMachineTemplate inventory type"""


class IsCustomizable(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Customizable."""

    TRUE = "true"
    """Enable customizable."""
    FALSE = "false"
    """Disable customizable."""


class IsHighlyAvailable(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Highly available."""

    TRUE = "true"
    """Enable highly available."""
    FALSE = "false"
    """Disable highly available."""


class LimitCpuForMigration(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Limit CPU for migration."""

    TRUE = "true"
    """Enable limit CPU for migration."""
    FALSE = "false"
    """Disable limit CPU for migration."""


class Origin(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The intended executor of the operation; as in Resource Based Access Control (RBAC) and audit
    logs UX. Default value is "user,system".
    """

    USER = "user"
    SYSTEM = "system"
    USER_SYSTEM = "user,system"


class OsType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Virtual machine operating system type."""

    WINDOWS = "Windows"
    """Windows operating system."""
    LINUX = "Linux"
    """Linux operating system."""
    OTHER = "Other"
    """Other operating system."""


class ProvisioningAction(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Guest agent provisioning action."""

    INSTALL = "install"
    """Install guest agent."""
    UNINSTALL = "uninstall"
    """Uninstall guest agent."""
    REPAIR = "repair"
    """Repair guest agent."""


class ResourceProvisioningState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The provisioning state of the resource."""

    SUCCEEDED = "Succeeded"
    """Resource has been created."""
    FAILED = "Failed"
    """Resource creation failed."""
    CANCELED = "Canceled"
    """Resource creation was canceled."""
    PROVISIONING = "Provisioning"
    """The resource is provisioning."""
    UPDATING = "Updating"
    """The resource is updating."""
    DELETING = "Deleting"
    """The resource is being deleted."""
    ACCEPTED = "Accepted"
    """The resource has been accepted."""
    CREATED = "Created"
    """The resource was created."""


class SkipShutdown(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Gets or sets a value indicating whether to request non-graceful VM shutdown. True value for
    this flag indicates non-graceful shutdown whereas false indicates otherwise. Defaults to false.
    """

    TRUE = "true"
    """Enable skip shutdown."""
    FALSE = "false"
    """Disable skip shutdown."""
