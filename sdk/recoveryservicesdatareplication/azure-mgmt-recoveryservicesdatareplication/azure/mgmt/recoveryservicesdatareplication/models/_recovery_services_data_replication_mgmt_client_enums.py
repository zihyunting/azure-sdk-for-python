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


class HealthStatus(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Gets or sets the fabric health."""

    NORMAL = "Normal"
    WARNING = "Warning"
    CRITICAL = "Critical"


class Origin(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The intended executor of the operation; as in Resource Based Access Control (RBAC) and audit
    logs UX. Default value is "user,system".
    """

    USER = "user"
    SYSTEM = "system"
    USER_SYSTEM = "user,system"


class ProtectedItemActiveLocation(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Gets or sets the location of the protected item."""

    PRIMARY = "Primary"
    RECOVERY = "Recovery"


class ProtectionState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Gets or sets the protection state."""

    UNPROTECTED_STATES_BEGIN = "UnprotectedStatesBegin"
    ENABLING_PROTECTION = "EnablingProtection"
    ENABLING_FAILED = "EnablingFailed"
    DISABLING_PROTECTION = "DisablingProtection"
    MARKED_FOR_DELETION = "MarkedForDeletion"
    DISABLING_FAILED = "DisablingFailed"
    UNPROTECTED_STATES_END = "UnprotectedStatesEnd"
    INITIAL_REPLICATION_STATES_BEGIN = "InitialReplicationStatesBegin"
    INITIAL_REPLICATION_IN_PROGRESS = "InitialReplicationInProgress"
    INITIAL_REPLICATION_COMPLETED_ON_PRIMARY = "InitialReplicationCompletedOnPrimary"
    INITIAL_REPLICATION_COMPLETED_ON_RECOVERY = "InitialReplicationCompletedOnRecovery"
    INITIAL_REPLICATION_FAILED = "InitialReplicationFailed"
    INITIAL_REPLICATION_STATES_END = "InitialReplicationStatesEnd"
    PROTECTED_STATES_BEGIN = "ProtectedStatesBegin"
    PROTECTED = "Protected"
    PROTECTED_STATES_END = "ProtectedStatesEnd"
    PLANNED_FAILOVER_TRANSITION_STATES_BEGIN = "PlannedFailoverTransitionStatesBegin"
    PLANNED_FAILOVER_INITIATED = "PlannedFailoverInitiated"
    PLANNED_FAILOVER_COMPLETING = "PlannedFailoverCompleting"
    PLANNED_FAILOVER_COMPLETED = "PlannedFailoverCompleted"
    PLANNED_FAILOVER_FAILED = "PlannedFailoverFailed"
    PLANNED_FAILOVER_COMPLETION_FAILED = "PlannedFailoverCompletionFailed"
    PLANNED_FAILOVER_TRANSITION_STATES_END = "PlannedFailoverTransitionStatesEnd"
    UNPLANNED_FAILOVER_TRANSITION_STATES_BEGIN = "UnplannedFailoverTransitionStatesBegin"
    UNPLANNED_FAILOVER_INITIATED = "UnplannedFailoverInitiated"
    UNPLANNED_FAILOVER_COMPLETING = "UnplannedFailoverCompleting"
    UNPLANNED_FAILOVER_COMPLETED = "UnplannedFailoverCompleted"
    UNPLANNED_FAILOVER_FAILED = "UnplannedFailoverFailed"
    UNPLANNED_FAILOVER_COMPLETION_FAILED = "UnplannedFailoverCompletionFailed"
    UNPLANNED_FAILOVER_TRANSITION_STATES_END = "UnplannedFailoverTransitionStatesEnd"
    COMMIT_FAILOVER_STATES_BEGIN = "CommitFailoverStatesBegin"
    COMMIT_FAILOVER_IN_PROGRESS_ON_PRIMARY = "CommitFailoverInProgressOnPrimary"
    COMMIT_FAILOVER_IN_PROGRESS_ON_RECOVERY = "CommitFailoverInProgressOnRecovery"
    COMMIT_FAILOVER_COMPLETED = "CommitFailoverCompleted"
    COMMIT_FAILOVER_FAILED_ON_PRIMARY = "CommitFailoverFailedOnPrimary"
    COMMIT_FAILOVER_FAILED_ON_RECOVERY = "CommitFailoverFailedOnRecovery"
    COMMIT_FAILOVER_STATES_END = "CommitFailoverStatesEnd"
    CANCEL_FAILOVER_STATES_BEGIN = "CancelFailoverStatesBegin"
    CANCEL_FAILOVER_IN_PROGRESS_ON_PRIMARY = "CancelFailoverInProgressOnPrimary"
    CANCEL_FAILOVER_IN_PROGRESS_ON_RECOVERY = "CancelFailoverInProgressOnRecovery"
    CANCEL_FAILOVER_FAILED_ON_PRIMARY = "CancelFailoverFailedOnPrimary"
    CANCEL_FAILOVER_FAILED_ON_RECOVERY = "CancelFailoverFailedOnRecovery"
    CANCEL_FAILOVER_STATES_END = "CancelFailoverStatesEnd"
    CHANGE_RECOVERY_POINT_STATES_BEGIN = "ChangeRecoveryPointStatesBegin"
    CHANGE_RECOVERY_POINT_INITIATED = "ChangeRecoveryPointInitiated"
    CHANGE_RECOVERY_POINT_COMPLETED = "ChangeRecoveryPointCompleted"
    CHANGE_RECOVERY_POINT_FAILED = "ChangeRecoveryPointFailed"
    CHANGE_RECOVERY_POINT_STATES_END = "ChangeRecoveryPointStatesEnd"
    REPROTECT_STATES_BEGIN = "ReprotectStatesBegin"
    REPROTECT_INITIATED = "ReprotectInitiated"
    REPROTECT_FAILED = "ReprotectFailed"
    REPROTECT_STATES_END = "ReprotectStatesEnd"


class ProvisioningState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Gets or sets the provisioning state of the Dra."""

    CANCELED = "Canceled"
    CREATING = "Creating"
    DELETING = "Deleting"
    DELETED = "Deleted"
    FAILED = "Failed"
    SUCCEEDED = "Succeeded"
    UPDATING = "Updating"


class RecoveryPointType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Gets or sets the recovery point type."""

    APPLICATION_CONSISTENT = "ApplicationConsistent"
    CRASH_CONSISTENT = "CrashConsistent"


class ReplicationVaultType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Gets or sets the type of vault."""

    DISASTER_RECOVERY = "DisasterRecovery"
    MIGRATE = "Migrate"


class ResynchronizationState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Gets or sets the resynchronization state."""

    NONE = "None"
    RESYNCHRONIZATION_INITIATED = "ResynchronizationInitiated"
    RESYNCHRONIZATION_COMPLETED = "ResynchronizationCompleted"
    RESYNCHRONIZATION_FAILED = "ResynchronizationFailed"


class TaskState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Gets or sets the task state."""

    PENDING = "Pending"
    STARTED = "Started"
    SUCCEEDED = "Succeeded"
    FAILED = "Failed"
    CANCELLED = "Cancelled"
    SKIPPED = "Skipped"


class TestFailoverState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Gets or sets the test failover state."""

    NONE = "None"
    TEST_FAILOVER_INITIATED = "TestFailoverInitiated"
    TEST_FAILOVER_COMPLETING = "TestFailoverCompleting"
    TEST_FAILOVER_COMPLETED = "TestFailoverCompleted"
    TEST_FAILOVER_FAILED = "TestFailoverFailed"
    TEST_FAILOVER_COMPLETION_FAILED = "TestFailoverCompletionFailed"
    TEST_FAILOVER_CLEANUP_INITIATED = "TestFailoverCleanupInitiated"
    TEST_FAILOVER_CLEANUP_COMPLETING = "TestFailoverCleanupCompleting"
    MARKED_FOR_DELETION = "MarkedForDeletion"


class VMNicSelection(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Gets or sets the selection type of the NIC."""

    NOT_SELECTED = "NotSelected"
    SELECTED_BY_USER = "SelectedByUser"
    SELECTED_BY_DEFAULT = "SelectedByDefault"
    SELECTED_BY_USER_OVERRIDE = "SelectedByUserOverride"


class VMwareToAzureMigrateResyncState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Gets or sets the resync state."""

    NONE = "None"
    PREPARED_FOR_RESYNCHRONIZATION = "PreparedForResynchronization"
    STARTED_RESYNCHRONIZATION = "StartedResynchronization"


class WorkflowObjectType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Gets or sets the object type."""

    AVS_DISK_POOL = "AvsDiskPool"
    DRA = "Dra"
    FABRIC = "Fabric"
    POLICY = "Policy"
    PROTECTED_ITEM = "ProtectedItem"
    RECOVERY_PLAN = "RecoveryPlan"
    REPLICATION_EXTENSION = "ReplicationExtension"
    VAULT = "Vault"


class WorkflowState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Gets or sets the workflow state."""

    PENDING = "Pending"
    STARTED = "Started"
    CANCELLING = "Cancelling"
    SUCCEEDED = "Succeeded"
    FAILED = "Failed"
    CANCELLED = "Cancelled"
    COMPLETED_WITH_INFORMATION = "CompletedWithInformation"
    COMPLETED_WITH_WARNINGS = "CompletedWithWarnings"
    COMPLETED_WITH_ERRORS = "CompletedWithErrors"
