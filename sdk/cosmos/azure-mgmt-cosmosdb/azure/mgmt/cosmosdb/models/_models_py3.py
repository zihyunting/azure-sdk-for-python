# coding=utf-8
# pylint: disable=too-many-lines
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

import datetime
from typing import Any, List, Optional, TYPE_CHECKING, Union

from .. import _serialization

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from .. import models as _models


class ErrorResponse(_serialization.Model):
    """Error Response.

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


class NetworkSecurityPerimeter(_serialization.Model):
    """NetworkSecurityPerimeter related information.

    :ivar id: The ARM identifier of the resource.
    :vartype id: str
    :ivar perimeter_guid: Guid of the resource.
    :vartype perimeter_guid: str
    :ivar location: Location of the resource.
    :vartype location: str
    """

    _attribute_map = {
        "id": {"key": "id", "type": "str"},
        "perimeter_guid": {"key": "perimeterGuid", "type": "str"},
        "location": {"key": "location", "type": "str"},
    }

    def __init__(
        self,
        *,
        id: Optional[str] = None,  # pylint: disable=redefined-builtin
        perimeter_guid: Optional[str] = None,
        location: Optional[str] = None,
        **kwargs: Any
    ) -> None:
        """
        :keyword id: The ARM identifier of the resource.
        :paramtype id: str
        :keyword perimeter_guid: Guid of the resource.
        :paramtype perimeter_guid: str
        :keyword location: Location of the resource.
        :paramtype location: str
        """
        super().__init__(**kwargs)
        self.id = id
        self.perimeter_guid = perimeter_guid
        self.location = location


class Resource(_serialization.Model):
    """Common fields that are returned in the response for all Azure Resource Manager resources.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: Fully qualified resource ID for the resource. Ex -
     /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}.  # pylint: disable=line-too-long
    :vartype id: str
    :ivar name: The name of the resource.
    :vartype name: str
    :ivar type: The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or
     "Microsoft.Storage/storageAccounts".
    :vartype type: str
    :ivar system_data: Azure Resource Manager metadata containing createdBy and modifiedBy
     information.
    :vartype system_data: ~azure.mgmt.cosmosdb.models.SystemData
    """

    _validation = {
        "id": {"readonly": True},
        "name": {"readonly": True},
        "type": {"readonly": True},
        "system_data": {"readonly": True},
    }

    _attribute_map = {
        "id": {"key": "id", "type": "str"},
        "name": {"key": "name", "type": "str"},
        "type": {"key": "type", "type": "str"},
        "system_data": {"key": "systemData", "type": "SystemData"},
    }

    def __init__(self, **kwargs: Any) -> None:
        """ """
        super().__init__(**kwargs)
        self.id = None
        self.name = None
        self.type = None
        self.system_data = None


class ProxyResource(Resource):
    """The resource model definition for a Azure Resource Manager proxy resource. It will not have
    tags and a location.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: Fully qualified resource ID for the resource. Ex -
     /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}.  # pylint: disable=line-too-long
    :vartype id: str
    :ivar name: The name of the resource.
    :vartype name: str
    :ivar type: The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or
     "Microsoft.Storage/storageAccounts".
    :vartype type: str
    :ivar system_data: Azure Resource Manager metadata containing createdBy and modifiedBy
     information.
    :vartype system_data: ~azure.mgmt.cosmosdb.models.SystemData
    """


class NetworkSecurityPerimeterConfiguration(ProxyResource):
    """The Network Security Perimeter configuration resource.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: Fully qualified resource ID for the resource. Ex -
     /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}.  # pylint: disable=line-too-long
    :vartype id: str
    :ivar name: The name of the resource.
    :vartype name: str
    :ivar type: The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or
     "Microsoft.Storage/storageAccounts".
    :vartype type: str
    :ivar system_data: Azure Resource Manager metadata containing createdBy and modifiedBy
     information.
    :vartype system_data: ~azure.mgmt.cosmosdb.models.SystemData
    :ivar provisioning_state: Provisioning state of Network Security Perimeter configuration
     propagation. Known values are: "Accepted", "Succeeded", "Failed", and "Deleting".
    :vartype provisioning_state: str or
     ~azure.mgmt.cosmosdb.models.NetworkSecurityPerimeterConfigurationProvisioningState
    :ivar provisioning_issues: List of Provisioning Issues if any.
    :vartype provisioning_issues: list[~azure.mgmt.cosmosdb.models.ProvisioningIssue]
    :ivar network_security_perimeter: NetworkSecurityPerimeter related information.
    :vartype network_security_perimeter: ~azure.mgmt.cosmosdb.models.NetworkSecurityPerimeter
    :ivar resource_association: Information about resource association.
    :vartype resource_association:
     ~azure.mgmt.cosmosdb.models.NetworkSecurityPerimeterConfigurationPropertiesResourceAssociation
    :ivar profile: Network Security Perimeter profile.
    :vartype profile:
     ~azure.mgmt.cosmosdb.models.NetworkSecurityPerimeterConfigurationPropertiesProfile
    """

    _validation = {
        "id": {"readonly": True},
        "name": {"readonly": True},
        "type": {"readonly": True},
        "system_data": {"readonly": True},
        "provisioning_state": {"readonly": True},
        "provisioning_issues": {"readonly": True},
        "network_security_perimeter": {"readonly": True},
        "resource_association": {"readonly": True},
        "profile": {"readonly": True},
    }

    _attribute_map = {
        "id": {"key": "id", "type": "str"},
        "name": {"key": "name", "type": "str"},
        "type": {"key": "type", "type": "str"},
        "system_data": {"key": "systemData", "type": "SystemData"},
        "provisioning_state": {"key": "properties.provisioningState", "type": "str"},
        "provisioning_issues": {"key": "properties.provisioningIssues", "type": "[ProvisioningIssue]"},
        "network_security_perimeter": {
            "key": "properties.networkSecurityPerimeter",
            "type": "NetworkSecurityPerimeter",
        },
        "resource_association": {
            "key": "properties.resourceAssociation",
            "type": "NetworkSecurityPerimeterConfigurationPropertiesResourceAssociation",
        },
        "profile": {"key": "properties.profile", "type": "NetworkSecurityPerimeterConfigurationPropertiesProfile"},
    }

    def __init__(self, **kwargs: Any) -> None:
        """ """
        super().__init__(**kwargs)
        self.provisioning_state = None
        self.provisioning_issues = None
        self.network_security_perimeter = None
        self.resource_association = None
        self.profile = None


class NetworkSecurityPerimeterConfigurationList(_serialization.Model):  # pylint: disable=name-too-long
    """Result of the List Network Security Perimeter configuration operation.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar value: A collection of Network Security Perimeter configurations.
    :vartype value: list[~azure.mgmt.cosmosdb.models.NetworkSecurityPerimeterConfiguration]
    """

    _validation = {
        "value": {"readonly": True},
    }

    _attribute_map = {
        "value": {"key": "value", "type": "[NetworkSecurityPerimeterConfiguration]"},
    }

    def __init__(self, **kwargs: Any) -> None:
        """ """
        super().__init__(**kwargs)
        self.value = None


class NetworkSecurityPerimeterConfigurationPropertiesProfile(_serialization.Model):  # pylint: disable=name-too-long
    """Network Security Perimeter profile.

    :ivar name: Name of the resource.
    :vartype name: str
    :ivar access_rules_version: Current access rules version.
    :vartype access_rules_version: float
    :ivar access_rules: List of Access Rules.
    :vartype access_rules: list[~azure.mgmt.cosmosdb.models.NspAccessRule]
    :ivar diagnostic_settings_version: Diagnostic settings version.
    :vartype diagnostic_settings_version: float
    :ivar enabled_log_categories: Enabled logging categories.
    :vartype enabled_log_categories: list[str]
    """

    _attribute_map = {
        "name": {"key": "name", "type": "str"},
        "access_rules_version": {"key": "accessRulesVersion", "type": "float"},
        "access_rules": {"key": "accessRules", "type": "[NspAccessRule]"},
        "diagnostic_settings_version": {"key": "diagnosticSettingsVersion", "type": "float"},
        "enabled_log_categories": {"key": "enabledLogCategories", "type": "[str]"},
    }

    def __init__(
        self,
        *,
        name: Optional[str] = None,
        access_rules_version: Optional[float] = None,
        access_rules: Optional[List["_models.NspAccessRule"]] = None,
        diagnostic_settings_version: Optional[float] = None,
        enabled_log_categories: Optional[List[str]] = None,
        **kwargs: Any
    ) -> None:
        """
        :keyword name: Name of the resource.
        :paramtype name: str
        :keyword access_rules_version: Current access rules version.
        :paramtype access_rules_version: float
        :keyword access_rules: List of Access Rules.
        :paramtype access_rules: list[~azure.mgmt.cosmosdb.models.NspAccessRule]
        :keyword diagnostic_settings_version: Diagnostic settings version.
        :paramtype diagnostic_settings_version: float
        :keyword enabled_log_categories: Enabled logging categories.
        :paramtype enabled_log_categories: list[str]
        """
        super().__init__(**kwargs)
        self.name = name
        self.access_rules_version = access_rules_version
        self.access_rules = access_rules
        self.diagnostic_settings_version = diagnostic_settings_version
        self.enabled_log_categories = enabled_log_categories


class NetworkSecurityPerimeterConfigurationPropertiesResourceAssociation(
    _serialization.Model
):  # pylint: disable=name-too-long
    """Information about resource association.

    :ivar name: Name of the resource association.
    :vartype name: str
    :ivar access_mode: Access Mode of the resource association. Known values are: "Enforced",
     "Learning", and "Audit".
    :vartype access_mode: str or ~azure.mgmt.cosmosdb.models.ResourceAssociationAccessMode
    """

    _attribute_map = {
        "name": {"key": "name", "type": "str"},
        "access_mode": {"key": "accessMode", "type": "str"},
    }

    def __init__(
        self,
        *,
        name: Optional[str] = None,
        access_mode: Optional[Union[str, "_models.ResourceAssociationAccessMode"]] = None,
        **kwargs: Any
    ) -> None:
        """
        :keyword name: Name of the resource association.
        :paramtype name: str
        :keyword access_mode: Access Mode of the resource association. Known values are: "Enforced",
         "Learning", and "Audit".
        :paramtype access_mode: str or ~azure.mgmt.cosmosdb.models.ResourceAssociationAccessMode
        """
        super().__init__(**kwargs)
        self.name = name
        self.access_mode = access_mode


class NspAccessRule(_serialization.Model):
    """Information of Access Rule in Network Security Perimeter profile.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar name: Name of the resource.
    :vartype name: str
    :ivar properties: Properties of Access Rule.
    :vartype properties: ~azure.mgmt.cosmosdb.models.NspAccessRuleProperties
    """

    _validation = {
        "properties": {"readonly": True},
    }

    _attribute_map = {
        "name": {"key": "name", "type": "str"},
        "properties": {"key": "properties", "type": "NspAccessRuleProperties"},
    }

    def __init__(self, *, name: Optional[str] = None, **kwargs: Any) -> None:
        """
        :keyword name: Name of the resource.
        :paramtype name: str
        """
        super().__init__(**kwargs)
        self.name = name
        self.properties = None


class NspAccessRuleProperties(_serialization.Model):
    """Properties of Access Rule.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar direction: Direction of Access Rule. Known values are: "Inbound" and "Outbound".
    :vartype direction: str or ~azure.mgmt.cosmosdb.models.NspAccessRuleDirection
    :ivar address_prefixes: Address prefixes in the CIDR format for inbound rules.
    :vartype address_prefixes: list[str]
    :ivar subscriptions: Subscriptions for inbound rules.
    :vartype subscriptions:
     list[~azure.mgmt.cosmosdb.models.NspAccessRulePropertiesSubscriptionsItem]
    :ivar network_security_perimeters: NetworkSecurityPerimeters for inbound rules.
    :vartype network_security_perimeters:
     list[~azure.mgmt.cosmosdb.models.NetworkSecurityPerimeter]
    :ivar fully_qualified_domain_names: FQDN for outbound rules.
    :vartype fully_qualified_domain_names: list[str]
    """

    _validation = {
        "network_security_perimeters": {"readonly": True},
        "fully_qualified_domain_names": {"readonly": True},
    }

    _attribute_map = {
        "direction": {"key": "direction", "type": "str"},
        "address_prefixes": {"key": "addressPrefixes", "type": "[str]"},
        "subscriptions": {"key": "subscriptions", "type": "[NspAccessRulePropertiesSubscriptionsItem]"},
        "network_security_perimeters": {"key": "networkSecurityPerimeters", "type": "[NetworkSecurityPerimeter]"},
        "fully_qualified_domain_names": {"key": "fullyQualifiedDomainNames", "type": "[str]"},
    }

    def __init__(
        self,
        *,
        direction: Optional[Union[str, "_models.NspAccessRuleDirection"]] = None,
        address_prefixes: Optional[List[str]] = None,
        subscriptions: Optional[List["_models.NspAccessRulePropertiesSubscriptionsItem"]] = None,
        **kwargs: Any
    ) -> None:
        """
        :keyword direction: Direction of Access Rule. Known values are: "Inbound" and "Outbound".
        :paramtype direction: str or ~azure.mgmt.cosmosdb.models.NspAccessRuleDirection
        :keyword address_prefixes: Address prefixes in the CIDR format for inbound rules.
        :paramtype address_prefixes: list[str]
        :keyword subscriptions: Subscriptions for inbound rules.
        :paramtype subscriptions:
         list[~azure.mgmt.cosmosdb.models.NspAccessRulePropertiesSubscriptionsItem]
        """
        super().__init__(**kwargs)
        self.direction = direction
        self.address_prefixes = address_prefixes
        self.subscriptions = subscriptions
        self.network_security_perimeters = None
        self.fully_qualified_domain_names = None


class NspAccessRulePropertiesSubscriptionsItem(_serialization.Model):
    """Subscription for inbound rule.

    :ivar id: The ARM identifier of subscription.
    :vartype id: str
    """

    _attribute_map = {
        "id": {"key": "id", "type": "str"},
    }

    def __init__(self, *, id: Optional[str] = None, **kwargs: Any) -> None:  # pylint: disable=redefined-builtin
        """
        :keyword id: The ARM identifier of subscription.
        :paramtype id: str
        """
        super().__init__(**kwargs)
        self.id = id


class ProvisioningIssue(_serialization.Model):
    """Describes provisioning issue for given NetworkSecurityPerimeterConfiguration.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar name: Name of the issue.
    :vartype name: str
    :ivar properties: Properties of provisioning issue.
    :vartype properties: ~azure.mgmt.cosmosdb.models.ProvisioningIssueProperties
    """

    _validation = {
        "properties": {"readonly": True},
    }

    _attribute_map = {
        "name": {"key": "name", "type": "str"},
        "properties": {"key": "properties", "type": "ProvisioningIssueProperties"},
    }

    def __init__(self, *, name: Optional[str] = None, **kwargs: Any) -> None:
        """
        :keyword name: Name of the issue.
        :paramtype name: str
        """
        super().__init__(**kwargs)
        self.name = name
        self.properties = None


class ProvisioningIssueProperties(_serialization.Model):
    """Properties of provisioning issue.

    :ivar issue_type: Type of issue. Known values are: "Unknown" and
     "ConfigurationPropagationFailure".
    :vartype issue_type: str or ~azure.mgmt.cosmosdb.models.IssueType
    :ivar severity: Severity of the issue. Known values are: "Warning" and "Error".
    :vartype severity: str or ~azure.mgmt.cosmosdb.models.Severity
    :ivar description: Description of the issue.
    :vartype description: str
    """

    _attribute_map = {
        "issue_type": {"key": "issueType", "type": "str"},
        "severity": {"key": "severity", "type": "str"},
        "description": {"key": "description", "type": "str"},
    }

    def __init__(
        self,
        *,
        issue_type: Optional[Union[str, "_models.IssueType"]] = None,
        severity: Optional[Union[str, "_models.Severity"]] = None,
        description: Optional[str] = None,
        **kwargs: Any
    ) -> None:
        """
        :keyword issue_type: Type of issue. Known values are: "Unknown" and
         "ConfigurationPropagationFailure".
        :paramtype issue_type: str or ~azure.mgmt.cosmosdb.models.IssueType
        :keyword severity: Severity of the issue. Known values are: "Warning" and "Error".
        :paramtype severity: str or ~azure.mgmt.cosmosdb.models.Severity
        :keyword description: Description of the issue.
        :paramtype description: str
        """
        super().__init__(**kwargs)
        self.issue_type = issue_type
        self.severity = severity
        self.description = description


class SystemData(_serialization.Model):
    """Metadata pertaining to creation and last modification of the resource.

    :ivar created_by: The identity that created the resource.
    :vartype created_by: str
    :ivar created_by_type: The type of identity that created the resource. Known values are:
     "User", "Application", "ManagedIdentity", and "Key".
    :vartype created_by_type: str or ~azure.mgmt.cosmosdb.models.CreatedByType
    :ivar created_at: The timestamp of resource creation (UTC).
    :vartype created_at: ~datetime.datetime
    :ivar last_modified_by: The identity that last modified the resource.
    :vartype last_modified_by: str
    :ivar last_modified_by_type: The type of identity that last modified the resource. Known values
     are: "User", "Application", "ManagedIdentity", and "Key".
    :vartype last_modified_by_type: str or ~azure.mgmt.cosmosdb.models.CreatedByType
    :ivar last_modified_at: The timestamp of resource last modification (UTC).
    :vartype last_modified_at: ~datetime.datetime
    """

    _attribute_map = {
        "created_by": {"key": "createdBy", "type": "str"},
        "created_by_type": {"key": "createdByType", "type": "str"},
        "created_at": {"key": "createdAt", "type": "iso-8601"},
        "last_modified_by": {"key": "lastModifiedBy", "type": "str"},
        "last_modified_by_type": {"key": "lastModifiedByType", "type": "str"},
        "last_modified_at": {"key": "lastModifiedAt", "type": "iso-8601"},
    }

    def __init__(
        self,
        *,
        created_by: Optional[str] = None,
        created_by_type: Optional[Union[str, "_models.CreatedByType"]] = None,
        created_at: Optional[datetime.datetime] = None,
        last_modified_by: Optional[str] = None,
        last_modified_by_type: Optional[Union[str, "_models.CreatedByType"]] = None,
        last_modified_at: Optional[datetime.datetime] = None,
        **kwargs: Any
    ) -> None:
        """
        :keyword created_by: The identity that created the resource.
        :paramtype created_by: str
        :keyword created_by_type: The type of identity that created the resource. Known values are:
         "User", "Application", "ManagedIdentity", and "Key".
        :paramtype created_by_type: str or ~azure.mgmt.cosmosdb.models.CreatedByType
        :keyword created_at: The timestamp of resource creation (UTC).
        :paramtype created_at: ~datetime.datetime
        :keyword last_modified_by: The identity that last modified the resource.
        :paramtype last_modified_by: str
        :keyword last_modified_by_type: The type of identity that last modified the resource. Known
         values are: "User", "Application", "ManagedIdentity", and "Key".
        :paramtype last_modified_by_type: str or ~azure.mgmt.cosmosdb.models.CreatedByType
        :keyword last_modified_at: The timestamp of resource last modification (UTC).
        :paramtype last_modified_at: ~datetime.datetime
        """
        super().__init__(**kwargs)
        self.created_by = created_by
        self.created_by_type = created_by_type
        self.created_at = created_at
        self.last_modified_by = last_modified_by
        self.last_modified_by_type = last_modified_by_type
        self.last_modified_at = last_modified_at
