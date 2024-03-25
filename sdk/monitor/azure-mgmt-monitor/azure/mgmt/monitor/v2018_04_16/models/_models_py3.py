# coding=utf-8
# pylint: disable=too-many-lines
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Any, Dict, List, Optional, TYPE_CHECKING, Union

from ... import _serialization

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from .. import models as _models


class Action(_serialization.Model):
    """Action descriptor.

    You probably want to use the sub-classes and not this class directly. Known sub-classes are:
    AlertingAction, LogToMetricAction

    All required parameters must be populated in order to send to server.

    :ivar odata_type: Specifies the action. Supported values - AlertingAction, LogToMetricAction.
     Required.
    :vartype odata_type: str
    """

    _validation = {
        "odata_type": {"required": True},
    }

    _attribute_map = {
        "odata_type": {"key": "odata\\.type", "type": "str"},
    }

    _subtype_map = {
        "odata_type": {
            "Microsoft.WindowsAzure.Management.Monitoring.Alerts.Models.Microsoft.AppInsights.Nexus.DataContracts.Resources.ScheduledQueryRules.AlertingAction": "AlertingAction",
            "Microsoft.WindowsAzure.Management.Monitoring.Alerts.Models.Microsoft.AppInsights.Nexus.DataContracts.Resources.ScheduledQueryRules.LogToMetricAction": "LogToMetricAction",
        }
    }

    def __init__(self, **kwargs: Any) -> None:
        """ """
        super().__init__(**kwargs)
        self.odata_type: Optional[str] = None


class AlertingAction(Action):
    """Specify action need to be taken when rule type is Alert.

    All required parameters must be populated in order to send to server.

    :ivar odata_type: Specifies the action. Supported values - AlertingAction, LogToMetricAction.
     Required.
    :vartype odata_type: str
    :ivar severity: Severity of the alert. Required. Known values are: "0", "1", "2", "3", and "4".
    :vartype severity: str or ~azure.mgmt.monitor.v2018_04_16.models.AlertSeverity
    :ivar azns_action: Azure action group reference.
    :vartype azns_action: ~azure.mgmt.monitor.v2018_04_16.models.AzNsActionGroup
    :ivar throttling_in_min: time (in minutes) for which Alerts should be throttled or suppressed.
    :vartype throttling_in_min: int
    :ivar trigger: The trigger condition that results in the alert rule being. Required.
    :vartype trigger: ~azure.mgmt.monitor.v2018_04_16.models.TriggerCondition
    """

    _validation = {
        "odata_type": {"required": True},
        "severity": {"required": True},
        "trigger": {"required": True},
    }

    _attribute_map = {
        "odata_type": {"key": "odata\\.type", "type": "str"},
        "severity": {"key": "severity", "type": "str"},
        "azns_action": {"key": "aznsAction", "type": "AzNsActionGroup"},
        "throttling_in_min": {"key": "throttlingInMin", "type": "int"},
        "trigger": {"key": "trigger", "type": "TriggerCondition"},
    }

    def __init__(
        self,
        *,
        severity: Union[str, "_models.AlertSeverity"],
        trigger: "_models.TriggerCondition",
        azns_action: Optional["_models.AzNsActionGroup"] = None,
        throttling_in_min: Optional[int] = None,
        **kwargs: Any
    ) -> None:
        """
        :keyword severity: Severity of the alert. Required. Known values are: "0", "1", "2", "3", and
         "4".
        :paramtype severity: str or ~azure.mgmt.monitor.v2018_04_16.models.AlertSeverity
        :keyword azns_action: Azure action group reference.
        :paramtype azns_action: ~azure.mgmt.monitor.v2018_04_16.models.AzNsActionGroup
        :keyword throttling_in_min: time (in minutes) for which Alerts should be throttled or
         suppressed.
        :paramtype throttling_in_min: int
        :keyword trigger: The trigger condition that results in the alert rule being. Required.
        :paramtype trigger: ~azure.mgmt.monitor.v2018_04_16.models.TriggerCondition
        """
        super().__init__(**kwargs)
        self.odata_type: str = "Microsoft.WindowsAzure.Management.Monitoring.Alerts.Models.Microsoft.AppInsights.Nexus.DataContracts.Resources.ScheduledQueryRules.AlertingAction"
        self.severity = severity
        self.azns_action = azns_action
        self.throttling_in_min = throttling_in_min
        self.trigger = trigger


class AzNsActionGroup(_serialization.Model):
    """Azure action group.

    :ivar action_group: Azure Action Group reference.
    :vartype action_group: list[str]
    :ivar email_subject: Custom subject override for all email ids in Azure action group.
    :vartype email_subject: str
    :ivar custom_webhook_payload: Custom payload to be sent for all webhook URI in Azure action
     group.
    :vartype custom_webhook_payload: str
    """

    _attribute_map = {
        "action_group": {"key": "actionGroup", "type": "[str]"},
        "email_subject": {"key": "emailSubject", "type": "str"},
        "custom_webhook_payload": {"key": "customWebhookPayload", "type": "str"},
    }

    def __init__(
        self,
        *,
        action_group: Optional[List[str]] = None,
        email_subject: Optional[str] = None,
        custom_webhook_payload: Optional[str] = None,
        **kwargs: Any
    ) -> None:
        """
        :keyword action_group: Azure Action Group reference.
        :paramtype action_group: list[str]
        :keyword email_subject: Custom subject override for all email ids in Azure action group.
        :paramtype email_subject: str
        :keyword custom_webhook_payload: Custom payload to be sent for all webhook URI in Azure action
         group.
        :paramtype custom_webhook_payload: str
        """
        super().__init__(**kwargs)
        self.action_group = action_group
        self.email_subject = email_subject
        self.custom_webhook_payload = custom_webhook_payload


class Criteria(_serialization.Model):
    """Specifies the criteria for converting log to metric.

    All required parameters must be populated in order to send to server.

    :ivar metric_name: Name of the metric. Required.
    :vartype metric_name: str
    :ivar dimensions: List of Dimensions for creating metric.
    :vartype dimensions: list[~azure.mgmt.monitor.v2018_04_16.models.Dimension]
    """

    _validation = {
        "metric_name": {"required": True},
    }

    _attribute_map = {
        "metric_name": {"key": "metricName", "type": "str"},
        "dimensions": {"key": "dimensions", "type": "[Dimension]"},
    }

    def __init__(
        self, *, metric_name: str, dimensions: Optional[List["_models.Dimension"]] = None, **kwargs: Any
    ) -> None:
        """
        :keyword metric_name: Name of the metric. Required.
        :paramtype metric_name: str
        :keyword dimensions: List of Dimensions for creating metric.
        :paramtype dimensions: list[~azure.mgmt.monitor.v2018_04_16.models.Dimension]
        """
        super().__init__(**kwargs)
        self.metric_name = metric_name
        self.dimensions = dimensions


class Dimension(_serialization.Model):
    """Specifies the criteria for converting log to metric.

    All required parameters must be populated in order to send to server.

    :ivar name: Name of the dimension. Required.
    :vartype name: str
    :ivar operator: Operator for dimension values. Required. "Include"
    :vartype operator: str or ~azure.mgmt.monitor.v2018_04_16.models.Operator
    :ivar values: List of dimension values. Required.
    :vartype values: list[str]
    """

    _validation = {
        "name": {"required": True},
        "operator": {"required": True},
        "values": {"required": True},
    }

    _attribute_map = {
        "name": {"key": "name", "type": "str"},
        "operator": {"key": "operator", "type": "str"},
        "values": {"key": "values", "type": "[str]"},
    }

    def __init__(
        self, *, name: str, operator: Union[str, "_models.Operator"], values: List[str], **kwargs: Any
    ) -> None:
        """
        :keyword name: Name of the dimension. Required.
        :paramtype name: str
        :keyword operator: Operator for dimension values. Required. "Include"
        :paramtype operator: str or ~azure.mgmt.monitor.v2018_04_16.models.Operator
        :keyword values: List of dimension values. Required.
        :paramtype values: list[str]
        """
        super().__init__(**kwargs)
        self.name = name
        self.operator = operator
        self.values = values


class ErrorContract(_serialization.Model):
    """Describes the format of Error response.

    :ivar error: The error details.
    :vartype error: ~azure.mgmt.monitor.v2018_04_16.models.ErrorResponse
    """

    _attribute_map = {
        "error": {"key": "error", "type": "ErrorResponse"},
    }

    def __init__(self, *, error: Optional["_models.ErrorResponse"] = None, **kwargs: Any) -> None:
        """
        :keyword error: The error details.
        :paramtype error: ~azure.mgmt.monitor.v2018_04_16.models.ErrorResponse
        """
        super().__init__(**kwargs)
        self.error = error


class ErrorResponse(_serialization.Model):
    """Describes the format of Error response.

    :ivar code: Error code.
    :vartype code: str
    :ivar message: Error message indicating why the operation failed.
    :vartype message: str
    """

    _attribute_map = {
        "code": {"key": "code", "type": "str"},
        "message": {"key": "message", "type": "str"},
    }

    def __init__(self, *, code: Optional[str] = None, message: Optional[str] = None, **kwargs: Any) -> None:
        """
        :keyword code: Error code.
        :paramtype code: str
        :keyword message: Error message indicating why the operation failed.
        :paramtype message: str
        """
        super().__init__(**kwargs)
        self.code = code
        self.message = message


class LogMetricTrigger(_serialization.Model):
    """A log metrics trigger descriptor.

    :ivar threshold_operator: Evaluation operation for Metric -'GreaterThan' or 'LessThan' or
     'Equal'. Known values are: "GreaterThanOrEqual", "LessThanOrEqual", "GreaterThan", "LessThan",
     and "Equal".
    :vartype threshold_operator: str or ~azure.mgmt.monitor.v2018_04_16.models.ConditionalOperator
    :ivar threshold: The threshold of the metric trigger.
    :vartype threshold: float
    :ivar metric_trigger_type: Metric Trigger Type - 'Consecutive' or 'Total'. Known values are:
     "Consecutive" and "Total".
    :vartype metric_trigger_type: str or ~azure.mgmt.monitor.v2018_04_16.models.MetricTriggerType
    :ivar metric_column: Evaluation of metric on a particular column.
    :vartype metric_column: str
    """

    _attribute_map = {
        "threshold_operator": {"key": "thresholdOperator", "type": "str"},
        "threshold": {"key": "threshold", "type": "float"},
        "metric_trigger_type": {"key": "metricTriggerType", "type": "str"},
        "metric_column": {"key": "metricColumn", "type": "str"},
    }

    def __init__(
        self,
        *,
        threshold_operator: Union[str, "_models.ConditionalOperator"] = "GreaterThanOrEqual",
        threshold: Optional[float] = None,
        metric_trigger_type: Union[str, "_models.MetricTriggerType"] = "Consecutive",
        metric_column: Optional[str] = None,
        **kwargs: Any
    ) -> None:
        """
        :keyword threshold_operator: Evaluation operation for Metric -'GreaterThan' or 'LessThan' or
         'Equal'. Known values are: "GreaterThanOrEqual", "LessThanOrEqual", "GreaterThan", "LessThan",
         and "Equal".
        :paramtype threshold_operator: str or
         ~azure.mgmt.monitor.v2018_04_16.models.ConditionalOperator
        :keyword threshold: The threshold of the metric trigger.
        :paramtype threshold: float
        :keyword metric_trigger_type: Metric Trigger Type - 'Consecutive' or 'Total'. Known values are:
         "Consecutive" and "Total".
        :paramtype metric_trigger_type: str or ~azure.mgmt.monitor.v2018_04_16.models.MetricTriggerType
        :keyword metric_column: Evaluation of metric on a particular column.
        :paramtype metric_column: str
        """
        super().__init__(**kwargs)
        self.threshold_operator = threshold_operator
        self.threshold = threshold
        self.metric_trigger_type = metric_trigger_type
        self.metric_column = metric_column


class Resource(_serialization.Model):
    """An azure resource object.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to server.

    :ivar id: Azure resource Id.
    :vartype id: str
    :ivar name: Azure resource name.
    :vartype name: str
    :ivar type: Azure resource type.
    :vartype type: str
    :ivar location: Resource location. Required.
    :vartype location: str
    :ivar tags: Resource tags.
    :vartype tags: dict[str, str]
    :ivar kind: Metadata used by portal/tooling/etc to render different UX experiences for
     resources of the same type; e.g. ApiApps are a kind of Microsoft.Web/sites type.  If supported,
     the resource provider must validate and persist this value.
    :vartype kind: str
    :ivar etag: The etag field is *not* required. If it is provided in the response body, it must
     also be provided as a header per the normal etag convention.  Entity tags are used for
     comparing two or more entities from the same requested resource. HTTP/1.1 uses entity tags in
     the etag (section 14.19), If-Match (section 14.24), If-None-Match (section 14.26), and If-Range
     (section 14.27) header fields.
    :vartype etag: str
    """

    _validation = {
        "id": {"readonly": True},
        "name": {"readonly": True},
        "type": {"readonly": True},
        "location": {"required": True},
        "kind": {"readonly": True},
        "etag": {"readonly": True},
    }

    _attribute_map = {
        "id": {"key": "id", "type": "str"},
        "name": {"key": "name", "type": "str"},
        "type": {"key": "type", "type": "str"},
        "location": {"key": "location", "type": "str"},
        "tags": {"key": "tags", "type": "{str}"},
        "kind": {"key": "kind", "type": "str"},
        "etag": {"key": "etag", "type": "str"},
    }

    def __init__(self, *, location: str, tags: Optional[Dict[str, str]] = None, **kwargs: Any) -> None:
        """
        :keyword location: Resource location. Required.
        :paramtype location: str
        :keyword tags: Resource tags.
        :paramtype tags: dict[str, str]
        """
        super().__init__(**kwargs)
        self.id = None
        self.name = None
        self.type = None
        self.location = location
        self.tags = tags
        self.kind = None
        self.etag = None


class LogSearchRuleResource(Resource):  # pylint: disable=too-many-instance-attributes
    """The Log Search Rule resource.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to server.

    :ivar id: Azure resource Id.
    :vartype id: str
    :ivar name: Azure resource name.
    :vartype name: str
    :ivar type: Azure resource type.
    :vartype type: str
    :ivar location: Resource location. Required.
    :vartype location: str
    :ivar tags: Resource tags.
    :vartype tags: dict[str, str]
    :ivar kind: Metadata used by portal/tooling/etc to render different UX experiences for
     resources of the same type; e.g. ApiApps are a kind of Microsoft.Web/sites type.  If supported,
     the resource provider must validate and persist this value.
    :vartype kind: str
    :ivar etag: The etag field is *not* required. If it is provided in the response body, it must
     also be provided as a header per the normal etag convention.  Entity tags are used for
     comparing two or more entities from the same requested resource. HTTP/1.1 uses entity tags in
     the etag (section 14.19), If-Match (section 14.24), If-None-Match (section 14.26), and If-Range
     (section 14.27) header fields.
    :vartype etag: str
    :ivar created_with_api_version: The api-version used when creating this alert rule.
    :vartype created_with_api_version: str
    :ivar is_legacy_log_analytics_rule: True if alert rule is legacy Log Analytic rule.
    :vartype is_legacy_log_analytics_rule: bool
    :ivar description: The description of the Log Search rule.
    :vartype description: str
    :ivar display_name: The display name of the alert rule.
    :vartype display_name: str
    :ivar auto_mitigate: The flag that indicates whether the alert should be automatically resolved
     or not. The default is false.
    :vartype auto_mitigate: bool
    :ivar enabled: The flag which indicates whether the Log Search rule is enabled. Value should be
     true or false. Known values are: "true" and "false".
    :vartype enabled: str or ~azure.mgmt.monitor.v2018_04_16.models.Enabled
    :ivar last_updated_time: Last time the rule was updated in IS08601 format.
    :vartype last_updated_time: ~datetime.datetime
    :ivar provisioning_state: Provisioning state of the scheduled query rule. Known values are:
     "Succeeded", "Deploying", "Canceled", and "Failed".
    :vartype provisioning_state: str or ~azure.mgmt.monitor.v2018_04_16.models.ProvisioningState
    :ivar source: Data Source against which rule will Query Data. Required.
    :vartype source: ~azure.mgmt.monitor.v2018_04_16.models.Source
    :ivar schedule: Schedule (Frequency, Time Window) for rule. Required for action type -
     AlertingAction.
    :vartype schedule: ~azure.mgmt.monitor.v2018_04_16.models.Schedule
    :ivar action: Action needs to be taken on rule execution. Required.
    :vartype action: ~azure.mgmt.monitor.v2018_04_16.models.Action
    """

    _validation = {
        "id": {"readonly": True},
        "name": {"readonly": True},
        "type": {"readonly": True},
        "location": {"required": True},
        "kind": {"readonly": True},
        "etag": {"readonly": True},
        "created_with_api_version": {"readonly": True},
        "is_legacy_log_analytics_rule": {"readonly": True},
        "last_updated_time": {"readonly": True},
        "provisioning_state": {"readonly": True},
        "source": {"required": True},
        "action": {"required": True},
    }

    _attribute_map = {
        "id": {"key": "id", "type": "str"},
        "name": {"key": "name", "type": "str"},
        "type": {"key": "type", "type": "str"},
        "location": {"key": "location", "type": "str"},
        "tags": {"key": "tags", "type": "{str}"},
        "kind": {"key": "kind", "type": "str"},
        "etag": {"key": "etag", "type": "str"},
        "created_with_api_version": {"key": "properties.createdWithApiVersion", "type": "str"},
        "is_legacy_log_analytics_rule": {"key": "properties.isLegacyLogAnalyticsRule", "type": "bool"},
        "description": {"key": "properties.description", "type": "str"},
        "display_name": {"key": "properties.displayName", "type": "str"},
        "auto_mitigate": {"key": "properties.autoMitigate", "type": "bool"},
        "enabled": {"key": "properties.enabled", "type": "str"},
        "last_updated_time": {"key": "properties.lastUpdatedTime", "type": "iso-8601"},
        "provisioning_state": {"key": "properties.provisioningState", "type": "str"},
        "source": {"key": "properties.source", "type": "Source"},
        "schedule": {"key": "properties.schedule", "type": "Schedule"},
        "action": {"key": "properties.action", "type": "Action"},
    }

    def __init__(
        self,
        *,
        location: str,
        source: "_models.Source",
        action: "_models.Action",
        tags: Optional[Dict[str, str]] = None,
        description: Optional[str] = None,
        display_name: Optional[str] = None,
        auto_mitigate: bool = False,
        enabled: Optional[Union[str, "_models.Enabled"]] = None,
        schedule: Optional["_models.Schedule"] = None,
        **kwargs: Any
    ) -> None:
        """
        :keyword location: Resource location. Required.
        :paramtype location: str
        :keyword tags: Resource tags.
        :paramtype tags: dict[str, str]
        :keyword description: The description of the Log Search rule.
        :paramtype description: str
        :keyword display_name: The display name of the alert rule.
        :paramtype display_name: str
        :keyword auto_mitigate: The flag that indicates whether the alert should be automatically
         resolved or not. The default is false.
        :paramtype auto_mitigate: bool
        :keyword enabled: The flag which indicates whether the Log Search rule is enabled. Value should
         be true or false. Known values are: "true" and "false".
        :paramtype enabled: str or ~azure.mgmt.monitor.v2018_04_16.models.Enabled
        :keyword source: Data Source against which rule will Query Data. Required.
        :paramtype source: ~azure.mgmt.monitor.v2018_04_16.models.Source
        :keyword schedule: Schedule (Frequency, Time Window) for rule. Required for action type -
         AlertingAction.
        :paramtype schedule: ~azure.mgmt.monitor.v2018_04_16.models.Schedule
        :keyword action: Action needs to be taken on rule execution. Required.
        :paramtype action: ~azure.mgmt.monitor.v2018_04_16.models.Action
        """
        super().__init__(location=location, tags=tags, **kwargs)
        self.created_with_api_version = None
        self.is_legacy_log_analytics_rule = None
        self.description = description
        self.display_name = display_name
        self.auto_mitigate = auto_mitigate
        self.enabled = enabled
        self.last_updated_time = None
        self.provisioning_state = None
        self.source = source
        self.schedule = schedule
        self.action = action


class LogSearchRuleResourceCollection(_serialization.Model):
    """Represents a collection of Log Search rule resources.

    :ivar value: The values for the Log Search Rule resources.
    :vartype value: list[~azure.mgmt.monitor.v2018_04_16.models.LogSearchRuleResource]
    """

    _attribute_map = {
        "value": {"key": "value", "type": "[LogSearchRuleResource]"},
    }

    def __init__(self, *, value: Optional[List["_models.LogSearchRuleResource"]] = None, **kwargs: Any) -> None:
        """
        :keyword value: The values for the Log Search Rule resources.
        :paramtype value: list[~azure.mgmt.monitor.v2018_04_16.models.LogSearchRuleResource]
        """
        super().__init__(**kwargs)
        self.value = value


class LogSearchRuleResourcePatch(_serialization.Model):
    """The log search rule resource for patch operations.

    :ivar tags: Resource tags.
    :vartype tags: dict[str, str]
    :ivar enabled: The flag which indicates whether the Log Search rule is enabled. Value should be
     true or false. Known values are: "true" and "false".
    :vartype enabled: str or ~azure.mgmt.monitor.v2018_04_16.models.Enabled
    """

    _attribute_map = {
        "tags": {"key": "tags", "type": "{str}"},
        "enabled": {"key": "properties.enabled", "type": "str"},
    }

    def __init__(
        self,
        *,
        tags: Optional[Dict[str, str]] = None,
        enabled: Optional[Union[str, "_models.Enabled"]] = None,
        **kwargs: Any
    ) -> None:
        """
        :keyword tags: Resource tags.
        :paramtype tags: dict[str, str]
        :keyword enabled: The flag which indicates whether the Log Search rule is enabled. Value should
         be true or false. Known values are: "true" and "false".
        :paramtype enabled: str or ~azure.mgmt.monitor.v2018_04_16.models.Enabled
        """
        super().__init__(**kwargs)
        self.tags = tags
        self.enabled = enabled


class LogToMetricAction(Action):
    """Specify action need to be taken when rule type is converting log to metric.

    All required parameters must be populated in order to send to server.

    :ivar odata_type: Specifies the action. Supported values - AlertingAction, LogToMetricAction.
     Required.
    :vartype odata_type: str
    :ivar criteria: Criteria of Metric. Required.
    :vartype criteria: list[~azure.mgmt.monitor.v2018_04_16.models.Criteria]
    """

    _validation = {
        "odata_type": {"required": True},
        "criteria": {"required": True},
    }

    _attribute_map = {
        "odata_type": {"key": "odata\\.type", "type": "str"},
        "criteria": {"key": "criteria", "type": "[Criteria]"},
    }

    def __init__(self, *, criteria: List["_models.Criteria"], **kwargs: Any) -> None:
        """
        :keyword criteria: Criteria of Metric. Required.
        :paramtype criteria: list[~azure.mgmt.monitor.v2018_04_16.models.Criteria]
        """
        super().__init__(**kwargs)
        self.odata_type: str = "Microsoft.WindowsAzure.Management.Monitoring.Alerts.Models.Microsoft.AppInsights.Nexus.DataContracts.Resources.ScheduledQueryRules.LogToMetricAction"
        self.criteria = criteria


class Schedule(_serialization.Model):
    """Defines how often to run the search and the time interval.

    All required parameters must be populated in order to send to server.

    :ivar frequency_in_minutes: frequency (in minutes) at which rule condition should be evaluated.
     Required.
    :vartype frequency_in_minutes: int
    :ivar time_window_in_minutes: Time window for which data needs to be fetched for query (should
     be greater than or equal to frequencyInMinutes). Required.
    :vartype time_window_in_minutes: int
    """

    _validation = {
        "frequency_in_minutes": {"required": True},
        "time_window_in_minutes": {"required": True},
    }

    _attribute_map = {
        "frequency_in_minutes": {"key": "frequencyInMinutes", "type": "int"},
        "time_window_in_minutes": {"key": "timeWindowInMinutes", "type": "int"},
    }

    def __init__(self, *, frequency_in_minutes: int, time_window_in_minutes: int, **kwargs: Any) -> None:
        """
        :keyword frequency_in_minutes: frequency (in minutes) at which rule condition should be
         evaluated. Required.
        :paramtype frequency_in_minutes: int
        :keyword time_window_in_minutes: Time window for which data needs to be fetched for query
         (should be greater than or equal to frequencyInMinutes). Required.
        :paramtype time_window_in_minutes: int
        """
        super().__init__(**kwargs)
        self.frequency_in_minutes = frequency_in_minutes
        self.time_window_in_minutes = time_window_in_minutes


class Source(_serialization.Model):
    """Specifies the log search query.

    All required parameters must be populated in order to send to server.

    :ivar query: Log search query. Required for action type - AlertingAction.
    :vartype query: str
    :ivar authorized_resources: List of  Resource referred into query.
    :vartype authorized_resources: list[str]
    :ivar data_source_id: The resource uri over which log search query is to be run. Required.
    :vartype data_source_id: str
    :ivar query_type: Set value to 'ResultCount' . "ResultCount"
    :vartype query_type: str or ~azure.mgmt.monitor.v2018_04_16.models.QueryType
    """

    _validation = {
        "data_source_id": {"required": True},
    }

    _attribute_map = {
        "query": {"key": "query", "type": "str"},
        "authorized_resources": {"key": "authorizedResources", "type": "[str]"},
        "data_source_id": {"key": "dataSourceId", "type": "str"},
        "query_type": {"key": "queryType", "type": "str"},
    }

    def __init__(
        self,
        *,
        data_source_id: str,
        query: Optional[str] = None,
        authorized_resources: Optional[List[str]] = None,
        query_type: Optional[Union[str, "_models.QueryType"]] = None,
        **kwargs: Any
    ) -> None:
        """
        :keyword query: Log search query. Required for action type - AlertingAction.
        :paramtype query: str
        :keyword authorized_resources: List of  Resource referred into query.
        :paramtype authorized_resources: list[str]
        :keyword data_source_id: The resource uri over which log search query is to be run. Required.
        :paramtype data_source_id: str
        :keyword query_type: Set value to 'ResultCount' . "ResultCount"
        :paramtype query_type: str or ~azure.mgmt.monitor.v2018_04_16.models.QueryType
        """
        super().__init__(**kwargs)
        self.query = query
        self.authorized_resources = authorized_resources
        self.data_source_id = data_source_id
        self.query_type = query_type


class TriggerCondition(_serialization.Model):
    """The condition that results in the Log Search rule.

    All required parameters must be populated in order to send to server.

    :ivar threshold_operator: Evaluation operation for rule - 'GreaterThan' or 'LessThan. Known
     values are: "GreaterThanOrEqual", "LessThanOrEqual", "GreaterThan", "LessThan", and "Equal".
    :vartype threshold_operator: str or ~azure.mgmt.monitor.v2018_04_16.models.ConditionalOperator
    :ivar threshold: Result or count threshold based on which rule should be triggered. Required.
    :vartype threshold: float
    :ivar metric_trigger: Trigger condition for metric query rule.
    :vartype metric_trigger: ~azure.mgmt.monitor.v2018_04_16.models.LogMetricTrigger
    """

    _validation = {
        "threshold_operator": {"required": True},
        "threshold": {"required": True},
    }

    _attribute_map = {
        "threshold_operator": {"key": "thresholdOperator", "type": "str"},
        "threshold": {"key": "threshold", "type": "float"},
        "metric_trigger": {"key": "metricTrigger", "type": "LogMetricTrigger"},
    }

    def __init__(
        self,
        *,
        threshold_operator: Union[str, "_models.ConditionalOperator"] = "GreaterThanOrEqual",
        threshold: float,
        metric_trigger: Optional["_models.LogMetricTrigger"] = None,
        **kwargs: Any
    ) -> None:
        """
        :keyword threshold_operator: Evaluation operation for rule - 'GreaterThan' or 'LessThan. Known
         values are: "GreaterThanOrEqual", "LessThanOrEqual", "GreaterThan", "LessThan", and "Equal".
        :paramtype threshold_operator: str or
         ~azure.mgmt.monitor.v2018_04_16.models.ConditionalOperator
        :keyword threshold: Result or count threshold based on which rule should be triggered.
         Required.
        :paramtype threshold: float
        :keyword metric_trigger: Trigger condition for metric query rule.
        :paramtype metric_trigger: ~azure.mgmt.monitor.v2018_04_16.models.LogMetricTrigger
        """
        super().__init__(**kwargs)
        self.threshold_operator = threshold_operator
        self.threshold = threshold
        self.metric_trigger = metric_trigger
