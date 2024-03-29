# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from ._models_py3 import AccessControlList
from ._models_py3 import AccessControlListAction
from ._models_py3 import AccessControlListMatchCondition
from ._models_py3 import AccessControlListMatchConfiguration
from ._models_py3 import AccessControlListPatch
from ._models_py3 import AccessControlListPatchProperties
from ._models_py3 import AccessControlListPatchableProperties
from ._models_py3 import AccessControlListPortCondition
from ._models_py3 import AccessControlListProperties
from ._models_py3 import AccessControlListsListResult
from ._models_py3 import ActionIpCommunityProperties
from ._models_py3 import ActionIpExtendedCommunityProperties
from ._models_py3 import AggregateRoute
from ._models_py3 import AggregateRouteConfiguration
from ._models_py3 import AnnotationResource
from ._models_py3 import BfdConfiguration
from ._models_py3 import BgpConfiguration
from ._models_py3 import CommonDynamicMatchConfiguration
from ._models_py3 import CommonMatchConditions
from ._models_py3 import CommonPostActionResponseForDeviceUpdate
from ._models_py3 import CommonPostActionResponseForStateUpdate
from ._models_py3 import ConnectedSubnet
from ._models_py3 import ConnectedSubnetRoutePolicy
from ._models_py3 import ControllerServices
from ._models_py3 import DestinationProperties
from ._models_py3 import DeviceInterfaceProperties
from ._models_py3 import EnableDisableOnResources
from ._models_py3 import ErrorAdditionalInfo
from ._models_py3 import ErrorDetail
from ._models_py3 import ErrorResponse
from ._models_py3 import ExportRoutePolicy
from ._models_py3 import ExportRoutePolicyInformation
from ._models_py3 import ExpressRouteConnectionInformation
from ._models_py3 import ExtendedLocation
from ._models_py3 import ExtensionEnumProperty
from ._models_py3 import ExternalNetwork
from ._models_py3 import ExternalNetworkPatch
from ._models_py3 import ExternalNetworkPatchProperties
from ._models_py3 import ExternalNetworkPatchPropertiesOptionAProperties
from ._models_py3 import ExternalNetworkPatchableProperties
from ._models_py3 import ExternalNetworkProperties
from ._models_py3 import ExternalNetworkPropertiesOptionAProperties
from ._models_py3 import ExternalNetworksList
from ._models_py3 import ImportRoutePolicy
from ._models_py3 import ImportRoutePolicyInformation
from ._models_py3 import InternalNetwork
from ._models_py3 import InternalNetworkPatch
from ._models_py3 import InternalNetworkPatchProperties
from ._models_py3 import InternalNetworkPatchableProperties
from ._models_py3 import InternalNetworkProperties
from ._models_py3 import InternalNetworkPropertiesBgpConfiguration
from ._models_py3 import InternalNetworkPropertiesStaticRouteConfiguration
from ._models_py3 import InternalNetworksList
from ._models_py3 import InternetGateway
from ._models_py3 import InternetGatewayPatch
from ._models_py3 import InternetGatewayPatchableProperties
from ._models_py3 import InternetGatewayProperties
from ._models_py3 import InternetGatewayRule
from ._models_py3 import InternetGatewayRulePatch
from ._models_py3 import InternetGatewayRuleProperties
from ._models_py3 import InternetGatewayRulesListResult
from ._models_py3 import InternetGatewaysListResult
from ._models_py3 import IpCommunitiesListResult
from ._models_py3 import IpCommunity
from ._models_py3 import IpCommunityAddOperationProperties
from ._models_py3 import IpCommunityDeleteOperationProperties
from ._models_py3 import IpCommunityIdList
from ._models_py3 import IpCommunityPatch
from ._models_py3 import IpCommunityPatchableProperties
from ._models_py3 import IpCommunityProperties
from ._models_py3 import IpCommunityRule
from ._models_py3 import IpCommunitySetOperationProperties
from ._models_py3 import IpExtendedCommunity
from ._models_py3 import IpExtendedCommunityAddOperationProperties
from ._models_py3 import IpExtendedCommunityDeleteOperationProperties
from ._models_py3 import IpExtendedCommunityIdList
from ._models_py3 import IpExtendedCommunityListResult
from ._models_py3 import IpExtendedCommunityPatch
from ._models_py3 import IpExtendedCommunityPatchProperties
from ._models_py3 import IpExtendedCommunityPatchableProperties
from ._models_py3 import IpExtendedCommunityProperties
from ._models_py3 import IpExtendedCommunityRule
from ._models_py3 import IpExtendedCommunitySetOperationProperties
from ._models_py3 import IpGroupProperties
from ._models_py3 import IpMatchCondition
from ._models_py3 import IpPrefix
from ._models_py3 import IpPrefixPatch
from ._models_py3 import IpPrefixPatchProperties
from ._models_py3 import IpPrefixPatchableProperties
from ._models_py3 import IpPrefixProperties
from ._models_py3 import IpPrefixRule
from ._models_py3 import IpPrefixesListResult
from ._models_py3 import IsolationDomainProperties
from ._models_py3 import L2IsolationDomain
from ._models_py3 import L2IsolationDomainPatch
from ._models_py3 import L2IsolationDomainPatchProperties
from ._models_py3 import L2IsolationDomainProperties
from ._models_py3 import L2IsolationDomainsListResult
from ._models_py3 import L3ExportRoutePolicy
from ._models_py3 import L3IsolationDomain
from ._models_py3 import L3IsolationDomainPatch
from ._models_py3 import L3IsolationDomainPatchProperties
from ._models_py3 import L3IsolationDomainPatchableProperties
from ._models_py3 import L3IsolationDomainProperties
from ._models_py3 import L3IsolationDomainsListResult
from ._models_py3 import L3OptionAProperties
from ._models_py3 import L3OptionBProperties
from ._models_py3 import Layer2Configuration
from ._models_py3 import Layer3IpPrefixProperties
from ._models_py3 import ManagedResourceGroupConfiguration
from ._models_py3 import ManagementNetworkConfigurationPatchableProperties
from ._models_py3 import ManagementNetworkConfigurationProperties
from ._models_py3 import NeighborAddress
from ._models_py3 import NeighborGroup
from ._models_py3 import NeighborGroupDestination
from ._models_py3 import NeighborGroupPatch
from ._models_py3 import NeighborGroupPatchProperties
from ._models_py3 import NeighborGroupPatchableProperties
from ._models_py3 import NeighborGroupProperties
from ._models_py3 import NeighborGroupsListResult
from ._models_py3 import NetworkDevice
from ._models_py3 import NetworkDevicePatchParameters
from ._models_py3 import NetworkDevicePatchParametersProperties
from ._models_py3 import NetworkDevicePatchableProperties
from ._models_py3 import NetworkDeviceProperties
from ._models_py3 import NetworkDeviceSku
from ._models_py3 import NetworkDeviceSkusListResult
from ._models_py3 import NetworkDevicesListResult
from ._models_py3 import NetworkFabric
from ._models_py3 import NetworkFabricController
from ._models_py3 import NetworkFabricControllerPatch
from ._models_py3 import NetworkFabricControllerPatchableProperties
from ._models_py3 import NetworkFabricControllerProperties
from ._models_py3 import NetworkFabricControllersListResult
from ._models_py3 import NetworkFabricPatch
from ._models_py3 import NetworkFabricPatchProperties
from ._models_py3 import NetworkFabricPatchableProperties
from ._models_py3 import NetworkFabricPatchablePropertiesTerminalServerConfiguration
from ._models_py3 import NetworkFabricProperties
from ._models_py3 import NetworkFabricSku
from ._models_py3 import NetworkFabricSkusListResult
from ._models_py3 import NetworkFabricsListResult
from ._models_py3 import NetworkInterface
from ._models_py3 import NetworkInterfacePatch
from ._models_py3 import NetworkInterfacePatchProperties
from ._models_py3 import NetworkInterfaceProperties
from ._models_py3 import NetworkInterfacesList
from ._models_py3 import NetworkPacketBroker
from ._models_py3 import NetworkPacketBrokerPatch
from ._models_py3 import NetworkPacketBrokersListResult
from ._models_py3 import NetworkRack
from ._models_py3 import NetworkRackProperties
from ._models_py3 import NetworkRacksListResult
from ._models_py3 import NetworkTap
from ._models_py3 import NetworkTapPatch
from ._models_py3 import NetworkTapPatchableParameters
from ._models_py3 import NetworkTapPatchableParametersDestinationsItem
from ._models_py3 import NetworkTapProperties
from ._models_py3 import NetworkTapPropertiesDestinationsItem
from ._models_py3 import NetworkTapRule
from ._models_py3 import NetworkTapRuleAction
from ._models_py3 import NetworkTapRuleMatchCondition
from ._models_py3 import NetworkTapRuleMatchConfiguration
from ._models_py3 import NetworkTapRulePatch
from ._models_py3 import NetworkTapRulePatchProperties
from ._models_py3 import NetworkTapRulePatchableProperties
from ._models_py3 import NetworkTapRuleProperties
from ._models_py3 import NetworkTapRulesListResult
from ._models_py3 import NetworkTapsListResult
from ._models_py3 import NetworkToNetworkInterconnect
from ._models_py3 import NetworkToNetworkInterconnectPatch
from ._models_py3 import NetworkToNetworkInterconnectPropertiesOptionBLayer3Configuration
from ._models_py3 import NetworkToNetworkInterconnectsList
from ._models_py3 import NpbStaticRouteConfiguration
from ._models_py3 import Operation
from ._models_py3 import OperationDisplay
from ._models_py3 import OperationListResult
from ._models_py3 import OptionAProperties
from ._models_py3 import OptionBLayer3Configuration
from ._models_py3 import OptionBProperties
from ._models_py3 import PortCondition
from ._models_py3 import PortGroupProperties
from ._models_py3 import ProxyResource
from ._models_py3 import RebootProperties
from ._models_py3 import Resource
from ._models_py3 import RoutePoliciesListResult
from ._models_py3 import RoutePolicy
from ._models_py3 import RoutePolicyPatch
from ._models_py3 import RoutePolicyPatchableProperties
from ._models_py3 import RoutePolicyProperties
from ._models_py3 import RoutePolicyStatementProperties
from ._models_py3 import RouteTargetInformation
from ._models_py3 import RuleProperties
from ._models_py3 import StatementActionProperties
from ._models_py3 import StatementConditionProperties
from ._models_py3 import StaticRouteConfiguration
from ._models_py3 import StaticRouteProperties
from ._models_py3 import SupportedConnectorProperties
from ._models_py3 import SupportedVersionProperties
from ._models_py3 import SystemData
from ._models_py3 import TagsUpdate
from ._models_py3 import TerminalServerConfiguration
from ._models_py3 import TerminalServerPatchableProperties
from ._models_py3 import TrackedResource
from ._models_py3 import UpdateAdministrativeState
from ._models_py3 import UpdateDeviceAdministrativeState
from ._models_py3 import UpdateVersion
from ._models_py3 import UpgradeNetworkFabricProperties
from ._models_py3 import ValidateConfigurationProperties
from ._models_py3 import ValidateConfigurationResponse
from ._models_py3 import VlanGroupProperties
from ._models_py3 import VlanMatchCondition
from ._models_py3 import VpnConfigurationPatchableProperties
from ._models_py3 import VpnConfigurationPatchablePropertiesOptionAProperties
from ._models_py3 import VpnConfigurationProperties
from ._models_py3 import VpnConfigurationPropertiesOptionAProperties

from ._managed_network_fabric_mgmt_client_enums import AclActionType
from ._managed_network_fabric_mgmt_client_enums import Action
from ._managed_network_fabric_mgmt_client_enums import ActionType
from ._managed_network_fabric_mgmt_client_enums import AddressFamilyType
from ._managed_network_fabric_mgmt_client_enums import AdministrativeState
from ._managed_network_fabric_mgmt_client_enums import AllowASOverride
from ._managed_network_fabric_mgmt_client_enums import BfdAdministrativeState
from ._managed_network_fabric_mgmt_client_enums import BooleanEnumProperty
from ._managed_network_fabric_mgmt_client_enums import CommunityActionTypes
from ._managed_network_fabric_mgmt_client_enums import Condition
from ._managed_network_fabric_mgmt_client_enums import ConfigurationState
from ._managed_network_fabric_mgmt_client_enums import ConfigurationType
from ._managed_network_fabric_mgmt_client_enums import CreatedByType
from ._managed_network_fabric_mgmt_client_enums import DestinationType
from ._managed_network_fabric_mgmt_client_enums import DeviceAdministrativeState
from ._managed_network_fabric_mgmt_client_enums import EnableDisableState
from ._managed_network_fabric_mgmt_client_enums import Encapsulation
from ._managed_network_fabric_mgmt_client_enums import EncapsulationType
from ._managed_network_fabric_mgmt_client_enums import Extension
from ._managed_network_fabric_mgmt_client_enums import FabricSkuType
from ._managed_network_fabric_mgmt_client_enums import GatewayType
from ._managed_network_fabric_mgmt_client_enums import IPAddressType
from ._managed_network_fabric_mgmt_client_enums import InterfaceType
from ._managed_network_fabric_mgmt_client_enums import IsManagementType
from ._managed_network_fabric_mgmt_client_enums import IsMonitoringEnabled
from ._managed_network_fabric_mgmt_client_enums import IsWorkloadManagementNetworkEnabled
from ._managed_network_fabric_mgmt_client_enums import Layer4Protocol
from ._managed_network_fabric_mgmt_client_enums import NetworkDeviceRole
from ._managed_network_fabric_mgmt_client_enums import NetworkDeviceRoleName
from ._managed_network_fabric_mgmt_client_enums import NetworkFabricUpgradeAction
from ._managed_network_fabric_mgmt_client_enums import NetworkRackType
from ._managed_network_fabric_mgmt_client_enums import NfcSku
from ._managed_network_fabric_mgmt_client_enums import NniType
from ._managed_network_fabric_mgmt_client_enums import Origin
from ._managed_network_fabric_mgmt_client_enums import PeeringOption
from ._managed_network_fabric_mgmt_client_enums import PollingIntervalInSeconds
from ._managed_network_fabric_mgmt_client_enums import PollingType
from ._managed_network_fabric_mgmt_client_enums import PortType
from ._managed_network_fabric_mgmt_client_enums import PrefixType
from ._managed_network_fabric_mgmt_client_enums import ProvisioningState
from ._managed_network_fabric_mgmt_client_enums import RebootType
from ._managed_network_fabric_mgmt_client_enums import RedistributeConnectedSubnets
from ._managed_network_fabric_mgmt_client_enums import RedistributeStaticRoutes
from ._managed_network_fabric_mgmt_client_enums import RoutePolicyActionType
from ._managed_network_fabric_mgmt_client_enums import RoutePolicyConditionType
from ._managed_network_fabric_mgmt_client_enums import SourceDestinationType
from ._managed_network_fabric_mgmt_client_enums import TapRuleActionType
from ._managed_network_fabric_mgmt_client_enums import ValidateAction
from ._managed_network_fabric_mgmt_client_enums import WellKnownCommunities
from ._patch import __all__ as _patch_all
from ._patch import *  # pylint: disable=unused-wildcard-import
from ._patch import patch_sdk as _patch_sdk

__all__ = [
    "AccessControlList",
    "AccessControlListAction",
    "AccessControlListMatchCondition",
    "AccessControlListMatchConfiguration",
    "AccessControlListPatch",
    "AccessControlListPatchProperties",
    "AccessControlListPatchableProperties",
    "AccessControlListPortCondition",
    "AccessControlListProperties",
    "AccessControlListsListResult",
    "ActionIpCommunityProperties",
    "ActionIpExtendedCommunityProperties",
    "AggregateRoute",
    "AggregateRouteConfiguration",
    "AnnotationResource",
    "BfdConfiguration",
    "BgpConfiguration",
    "CommonDynamicMatchConfiguration",
    "CommonMatchConditions",
    "CommonPostActionResponseForDeviceUpdate",
    "CommonPostActionResponseForStateUpdate",
    "ConnectedSubnet",
    "ConnectedSubnetRoutePolicy",
    "ControllerServices",
    "DestinationProperties",
    "DeviceInterfaceProperties",
    "EnableDisableOnResources",
    "ErrorAdditionalInfo",
    "ErrorDetail",
    "ErrorResponse",
    "ExportRoutePolicy",
    "ExportRoutePolicyInformation",
    "ExpressRouteConnectionInformation",
    "ExtendedLocation",
    "ExtensionEnumProperty",
    "ExternalNetwork",
    "ExternalNetworkPatch",
    "ExternalNetworkPatchProperties",
    "ExternalNetworkPatchPropertiesOptionAProperties",
    "ExternalNetworkPatchableProperties",
    "ExternalNetworkProperties",
    "ExternalNetworkPropertiesOptionAProperties",
    "ExternalNetworksList",
    "ImportRoutePolicy",
    "ImportRoutePolicyInformation",
    "InternalNetwork",
    "InternalNetworkPatch",
    "InternalNetworkPatchProperties",
    "InternalNetworkPatchableProperties",
    "InternalNetworkProperties",
    "InternalNetworkPropertiesBgpConfiguration",
    "InternalNetworkPropertiesStaticRouteConfiguration",
    "InternalNetworksList",
    "InternetGateway",
    "InternetGatewayPatch",
    "InternetGatewayPatchableProperties",
    "InternetGatewayProperties",
    "InternetGatewayRule",
    "InternetGatewayRulePatch",
    "InternetGatewayRuleProperties",
    "InternetGatewayRulesListResult",
    "InternetGatewaysListResult",
    "IpCommunitiesListResult",
    "IpCommunity",
    "IpCommunityAddOperationProperties",
    "IpCommunityDeleteOperationProperties",
    "IpCommunityIdList",
    "IpCommunityPatch",
    "IpCommunityPatchableProperties",
    "IpCommunityProperties",
    "IpCommunityRule",
    "IpCommunitySetOperationProperties",
    "IpExtendedCommunity",
    "IpExtendedCommunityAddOperationProperties",
    "IpExtendedCommunityDeleteOperationProperties",
    "IpExtendedCommunityIdList",
    "IpExtendedCommunityListResult",
    "IpExtendedCommunityPatch",
    "IpExtendedCommunityPatchProperties",
    "IpExtendedCommunityPatchableProperties",
    "IpExtendedCommunityProperties",
    "IpExtendedCommunityRule",
    "IpExtendedCommunitySetOperationProperties",
    "IpGroupProperties",
    "IpMatchCondition",
    "IpPrefix",
    "IpPrefixPatch",
    "IpPrefixPatchProperties",
    "IpPrefixPatchableProperties",
    "IpPrefixProperties",
    "IpPrefixRule",
    "IpPrefixesListResult",
    "IsolationDomainProperties",
    "L2IsolationDomain",
    "L2IsolationDomainPatch",
    "L2IsolationDomainPatchProperties",
    "L2IsolationDomainProperties",
    "L2IsolationDomainsListResult",
    "L3ExportRoutePolicy",
    "L3IsolationDomain",
    "L3IsolationDomainPatch",
    "L3IsolationDomainPatchProperties",
    "L3IsolationDomainPatchableProperties",
    "L3IsolationDomainProperties",
    "L3IsolationDomainsListResult",
    "L3OptionAProperties",
    "L3OptionBProperties",
    "Layer2Configuration",
    "Layer3IpPrefixProperties",
    "ManagedResourceGroupConfiguration",
    "ManagementNetworkConfigurationPatchableProperties",
    "ManagementNetworkConfigurationProperties",
    "NeighborAddress",
    "NeighborGroup",
    "NeighborGroupDestination",
    "NeighborGroupPatch",
    "NeighborGroupPatchProperties",
    "NeighborGroupPatchableProperties",
    "NeighborGroupProperties",
    "NeighborGroupsListResult",
    "NetworkDevice",
    "NetworkDevicePatchParameters",
    "NetworkDevicePatchParametersProperties",
    "NetworkDevicePatchableProperties",
    "NetworkDeviceProperties",
    "NetworkDeviceSku",
    "NetworkDeviceSkusListResult",
    "NetworkDevicesListResult",
    "NetworkFabric",
    "NetworkFabricController",
    "NetworkFabricControllerPatch",
    "NetworkFabricControllerPatchableProperties",
    "NetworkFabricControllerProperties",
    "NetworkFabricControllersListResult",
    "NetworkFabricPatch",
    "NetworkFabricPatchProperties",
    "NetworkFabricPatchableProperties",
    "NetworkFabricPatchablePropertiesTerminalServerConfiguration",
    "NetworkFabricProperties",
    "NetworkFabricSku",
    "NetworkFabricSkusListResult",
    "NetworkFabricsListResult",
    "NetworkInterface",
    "NetworkInterfacePatch",
    "NetworkInterfacePatchProperties",
    "NetworkInterfaceProperties",
    "NetworkInterfacesList",
    "NetworkPacketBroker",
    "NetworkPacketBrokerPatch",
    "NetworkPacketBrokersListResult",
    "NetworkRack",
    "NetworkRackProperties",
    "NetworkRacksListResult",
    "NetworkTap",
    "NetworkTapPatch",
    "NetworkTapPatchableParameters",
    "NetworkTapPatchableParametersDestinationsItem",
    "NetworkTapProperties",
    "NetworkTapPropertiesDestinationsItem",
    "NetworkTapRule",
    "NetworkTapRuleAction",
    "NetworkTapRuleMatchCondition",
    "NetworkTapRuleMatchConfiguration",
    "NetworkTapRulePatch",
    "NetworkTapRulePatchProperties",
    "NetworkTapRulePatchableProperties",
    "NetworkTapRuleProperties",
    "NetworkTapRulesListResult",
    "NetworkTapsListResult",
    "NetworkToNetworkInterconnect",
    "NetworkToNetworkInterconnectPatch",
    "NetworkToNetworkInterconnectPropertiesOptionBLayer3Configuration",
    "NetworkToNetworkInterconnectsList",
    "NpbStaticRouteConfiguration",
    "Operation",
    "OperationDisplay",
    "OperationListResult",
    "OptionAProperties",
    "OptionBLayer3Configuration",
    "OptionBProperties",
    "PortCondition",
    "PortGroupProperties",
    "ProxyResource",
    "RebootProperties",
    "Resource",
    "RoutePoliciesListResult",
    "RoutePolicy",
    "RoutePolicyPatch",
    "RoutePolicyPatchableProperties",
    "RoutePolicyProperties",
    "RoutePolicyStatementProperties",
    "RouteTargetInformation",
    "RuleProperties",
    "StatementActionProperties",
    "StatementConditionProperties",
    "StaticRouteConfiguration",
    "StaticRouteProperties",
    "SupportedConnectorProperties",
    "SupportedVersionProperties",
    "SystemData",
    "TagsUpdate",
    "TerminalServerConfiguration",
    "TerminalServerPatchableProperties",
    "TrackedResource",
    "UpdateAdministrativeState",
    "UpdateDeviceAdministrativeState",
    "UpdateVersion",
    "UpgradeNetworkFabricProperties",
    "ValidateConfigurationProperties",
    "ValidateConfigurationResponse",
    "VlanGroupProperties",
    "VlanMatchCondition",
    "VpnConfigurationPatchableProperties",
    "VpnConfigurationPatchablePropertiesOptionAProperties",
    "VpnConfigurationProperties",
    "VpnConfigurationPropertiesOptionAProperties",
    "AclActionType",
    "Action",
    "ActionType",
    "AddressFamilyType",
    "AdministrativeState",
    "AllowASOverride",
    "BfdAdministrativeState",
    "BooleanEnumProperty",
    "CommunityActionTypes",
    "Condition",
    "ConfigurationState",
    "ConfigurationType",
    "CreatedByType",
    "DestinationType",
    "DeviceAdministrativeState",
    "EnableDisableState",
    "Encapsulation",
    "EncapsulationType",
    "Extension",
    "FabricSkuType",
    "GatewayType",
    "IPAddressType",
    "InterfaceType",
    "IsManagementType",
    "IsMonitoringEnabled",
    "IsWorkloadManagementNetworkEnabled",
    "Layer4Protocol",
    "NetworkDeviceRole",
    "NetworkDeviceRoleName",
    "NetworkFabricUpgradeAction",
    "NetworkRackType",
    "NfcSku",
    "NniType",
    "Origin",
    "PeeringOption",
    "PollingIntervalInSeconds",
    "PollingType",
    "PortType",
    "PrefixType",
    "ProvisioningState",
    "RebootType",
    "RedistributeConnectedSubnets",
    "RedistributeStaticRoutes",
    "RoutePolicyActionType",
    "RoutePolicyConditionType",
    "SourceDestinationType",
    "TapRuleActionType",
    "ValidateAction",
    "WellKnownCommunities",
]
__all__.extend([p for p in _patch_all if p not in __all__])
_patch_sdk()
