# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum
from azure.core import CaseInsensitiveEnumMeta


class AuthenticationMode(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Authentication Mode. Valid modes are ``ConnectionString``\ , ``Msi`` and 'UserToken'."""

    MSI = "Msi"
    USER_TOKEN = "UserToken"
    CONNECTION_STRING = "ConnectionString"


class ClusterProvisioningState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The status of the cluster provisioning. The three terminal states are: Succeeded, Failed and
    Canceled.
    """

    SUCCEEDED = "Succeeded"
    """The cluster provisioning succeeded."""
    FAILED = "Failed"
    """The cluster provisioning failed."""
    CANCELED = "Canceled"
    """The cluster provisioning was canceled."""
    IN_PROGRESS = "InProgress"
    """The cluster provisioning was inprogress."""


class ClusterSkuName(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Specifies the SKU name of the cluster. Required on PUT (CreateOrUpdate) requests."""

    DEFAULT = "Default"
    """The default SKU."""


class CompatibilityLevel(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Controls certain runtime behaviors of the streaming job."""

    ONE0 = "1.0"
    ONE2 = "1.2"


class CompressionType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Indicates the type of compression that the input uses. Required on PUT (CreateOrReplace)
    requests.
    """

    NONE = "None"
    G_ZIP = "GZip"
    DEFLATE = "Deflate"


class ContentStoragePolicy(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Valid values are JobStorageAccount and SystemAccount. If set to JobStorageAccount, this
    requires the user to also specify jobStorageAccount property. .
    """

    SYSTEM_ACCOUNT = "SystemAccount"
    JOB_STORAGE_ACCOUNT = "JobStorageAccount"


class Encoding(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Specifies the encoding of the incoming data in the case of input and the encoding of outgoing
    data in the case of output.
    """

    UTF8 = "UTF8"


class EventSerializationType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Indicates the type of serialization that the input or output uses. Required on PUT
    (CreateOrReplace) requests.
    """

    CSV = "Csv"
    AVRO = "Avro"
    JSON = "Json"
    PARQUET = "Parquet"


class EventsOutOfOrderPolicy(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Indicates the policy to apply to events that arrive out of order in the input event stream."""

    ADJUST = "Adjust"
    DROP = "Drop"


class JobState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The current execution state of the streaming job."""

    CREATED = "Created"
    """The job is currently in the Created state."""
    STARTING = "Starting"
    """The job is currently in the Starting state."""
    RUNNING = "Running"
    """The job is currently in the Running state."""
    STOPPING = "Stopping"
    """The job is currently in the Stopping state."""
    STOPPED = "Stopped"
    """The job is currently in the Stopped state."""
    DELETING = "Deleting"
    """The job is currently in the Deleting state."""
    FAILED = "Failed"
    """The job is currently in the Failed state."""
    DEGRADED = "Degraded"
    """The job is currently in the Degraded state."""
    RESTARTING = "Restarting"
    """The job is currently in the Restarting state."""
    SCALING = "Scaling"
    """The job is currently in the Scaling state."""


class JobType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Describes the type of the job. Valid modes are ``Cloud`` and 'Edge'."""

    CLOUD = "Cloud"
    EDGE = "Edge"


class JsonOutputSerializationFormat(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Specifies the format of the JSON the output will be written in. The currently supported values
    are 'lineSeparated' indicating the output will be formatted by having each JSON object
    separated by a new line and 'array' indicating the output will be formatted as an array of JSON
    objects.
    """

    LINE_SEPARATED = "LineSeparated"
    ARRAY = "Array"


class OutputErrorPolicy(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Indicates the policy to apply to events that arrive at the output and cannot be written to the
    external storage due to being malformed (missing column values, column values of wrong type or
    size).
    """

    STOP = "Stop"
    DROP = "Drop"


class OutputStartMode(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Value may be JobStartTime, CustomTime, or LastOutputEventTime to indicate whether the starting
    point of the output event stream should start whenever the job is started, start at a custom
    user time stamp specified via the outputStartTime property, or start from the last event output
    time.
    """

    JOB_START_TIME = "JobStartTime"
    CUSTOM_TIME = "CustomTime"
    LAST_OUTPUT_EVENT_TIME = "LastOutputEventTime"


class RefreshType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Indicates the type of data refresh option."""

    STATIC = "Static"
    REFRESH_PERIODICALLY_WITH_FULL = "RefreshPeriodicallyWithFull"
    REFRESH_PERIODICALLY_WITH_DELTA = "RefreshPeriodicallyWithDelta"


class SkuName(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The name of the SKU. Required on PUT (CreateOrReplace) requests."""

    STANDARD = "Standard"
