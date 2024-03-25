# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from copy import deepcopy
from typing import Any, TYPE_CHECKING

from azure.core.pipeline import policies
from azure.core.rest import HttpRequest, HttpResponse
from azure.mgmt.core import ARMPipelineClient
from azure.mgmt.core.policies import ARMAutoResourceProviderRegistrationPolicy

from . import models as _models
from ._configuration import DesktopVirtualizationMgmtClientConfiguration
from ._serialization import Deserializer, Serializer
from .operations import (
    ActiveSessionHostConfigurationsOperations,
    AppAttachPackageInfoOperations,
    AppAttachPackageOperations,
    ApplicationGroupsOperations,
    ApplicationsOperations,
    ControlSessionHostUpdateOperations,
    DesktopsOperations,
    HostPoolsOperations,
    InitiateSessionHostUpdateOperations,
    MSIXPackagesOperations,
    MsixImagesOperations,
    Operations,
    PrivateEndpointConnectionsOperations,
    PrivateLinkResourcesOperations,
    ScalingPlanPersonalSchedulesOperations,
    ScalingPlanPooledSchedulesOperations,
    ScalingPlansOperations,
    SessionHostConfigurationsOperationStatusOperations,
    SessionHostConfigurationsOperations,
    SessionHostManagementsOperationStatusOperations,
    SessionHostManagementsOperations,
    SessionHostOperations,
    SessionHostsOperations,
    StartMenuItemsOperations,
    UserSessionsOperations,
    WorkspacesOperations,
)

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from azure.core.credentials import TokenCredential


class DesktopVirtualizationMgmtClient:  # pylint: disable=client-accepts-api-version-keyword,too-many-instance-attributes
    """DesktopVirtualizationMgmtClient.

    :ivar operations: Operations operations
    :vartype operations: azure.mgmt.desktopvirtualization.operations.Operations
    :ivar workspaces: WorkspacesOperations operations
    :vartype workspaces: azure.mgmt.desktopvirtualization.operations.WorkspacesOperations
    :ivar private_endpoint_connections: PrivateEndpointConnectionsOperations operations
    :vartype private_endpoint_connections:
     azure.mgmt.desktopvirtualization.operations.PrivateEndpointConnectionsOperations
    :ivar private_link_resources: PrivateLinkResourcesOperations operations
    :vartype private_link_resources:
     azure.mgmt.desktopvirtualization.operations.PrivateLinkResourcesOperations
    :ivar scaling_plans: ScalingPlansOperations operations
    :vartype scaling_plans: azure.mgmt.desktopvirtualization.operations.ScalingPlansOperations
    :ivar scaling_plan_pooled_schedules: ScalingPlanPooledSchedulesOperations operations
    :vartype scaling_plan_pooled_schedules:
     azure.mgmt.desktopvirtualization.operations.ScalingPlanPooledSchedulesOperations
    :ivar scaling_plan_personal_schedules: ScalingPlanPersonalSchedulesOperations operations
    :vartype scaling_plan_personal_schedules:
     azure.mgmt.desktopvirtualization.operations.ScalingPlanPersonalSchedulesOperations
    :ivar application_groups: ApplicationGroupsOperations operations
    :vartype application_groups:
     azure.mgmt.desktopvirtualization.operations.ApplicationGroupsOperations
    :ivar start_menu_items: StartMenuItemsOperations operations
    :vartype start_menu_items: azure.mgmt.desktopvirtualization.operations.StartMenuItemsOperations
    :ivar applications: ApplicationsOperations operations
    :vartype applications: azure.mgmt.desktopvirtualization.operations.ApplicationsOperations
    :ivar desktops: DesktopsOperations operations
    :vartype desktops: azure.mgmt.desktopvirtualization.operations.DesktopsOperations
    :ivar host_pools: HostPoolsOperations operations
    :vartype host_pools: azure.mgmt.desktopvirtualization.operations.HostPoolsOperations
    :ivar session_host_managements: SessionHostManagementsOperations operations
    :vartype session_host_managements:
     azure.mgmt.desktopvirtualization.operations.SessionHostManagementsOperations
    :ivar initiate_session_host_update: InitiateSessionHostUpdateOperations operations
    :vartype initiate_session_host_update:
     azure.mgmt.desktopvirtualization.operations.InitiateSessionHostUpdateOperations
    :ivar control_session_host_update: ControlSessionHostUpdateOperations operations
    :vartype control_session_host_update:
     azure.mgmt.desktopvirtualization.operations.ControlSessionHostUpdateOperations
    :ivar session_host_managements_operation_status:
     SessionHostManagementsOperationStatusOperations operations
    :vartype session_host_managements_operation_status:
     azure.mgmt.desktopvirtualization.operations.SessionHostManagementsOperationStatusOperations
    :ivar session_host_configurations: SessionHostConfigurationsOperations operations
    :vartype session_host_configurations:
     azure.mgmt.desktopvirtualization.operations.SessionHostConfigurationsOperations
    :ivar session_host_configurations_operation_status:
     SessionHostConfigurationsOperationStatusOperations operations
    :vartype session_host_configurations_operation_status:
     azure.mgmt.desktopvirtualization.operations.SessionHostConfigurationsOperationStatusOperations
    :ivar active_session_host_configurations: ActiveSessionHostConfigurationsOperations operations
    :vartype active_session_host_configurations:
     azure.mgmt.desktopvirtualization.operations.ActiveSessionHostConfigurationsOperations
    :ivar user_sessions: UserSessionsOperations operations
    :vartype user_sessions: azure.mgmt.desktopvirtualization.operations.UserSessionsOperations
    :ivar session_hosts: SessionHostsOperations operations
    :vartype session_hosts: azure.mgmt.desktopvirtualization.operations.SessionHostsOperations
    :ivar session_host: SessionHostOperations operations
    :vartype session_host: azure.mgmt.desktopvirtualization.operations.SessionHostOperations
    :ivar msix_packages: MSIXPackagesOperations operations
    :vartype msix_packages: azure.mgmt.desktopvirtualization.operations.MSIXPackagesOperations
    :ivar app_attach_package_info: AppAttachPackageInfoOperations operations
    :vartype app_attach_package_info:
     azure.mgmt.desktopvirtualization.operations.AppAttachPackageInfoOperations
    :ivar msix_images: MsixImagesOperations operations
    :vartype msix_images: azure.mgmt.desktopvirtualization.operations.MsixImagesOperations
    :ivar app_attach_package: AppAttachPackageOperations operations
    :vartype app_attach_package:
     azure.mgmt.desktopvirtualization.operations.AppAttachPackageOperations
    :param credential: Credential needed for the client to connect to Azure. Required.
    :type credential: ~azure.core.credentials.TokenCredential
    :param subscription_id: The ID of the target subscription. Required.
    :type subscription_id: str
    :param base_url: Service URL. Default value is "https://management.azure.com".
    :type base_url: str
    :keyword api_version: Api Version. Default value is "2024-03-06-preview". Note that overriding
     this default value may result in unsupported behavior.
    :paramtype api_version: str
    :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
     Retry-After header is present.
    """

    def __init__(
        self,
        credential: "TokenCredential",
        subscription_id: str,
        base_url: str = "https://management.azure.com",
        **kwargs: Any
    ) -> None:
        self._config = DesktopVirtualizationMgmtClientConfiguration(
            credential=credential, subscription_id=subscription_id, **kwargs
        )
        _policies = kwargs.pop("policies", None)
        if _policies is None:
            _policies = [
                policies.RequestIdPolicy(**kwargs),
                self._config.headers_policy,
                self._config.user_agent_policy,
                self._config.proxy_policy,
                policies.ContentDecodePolicy(**kwargs),
                ARMAutoResourceProviderRegistrationPolicy(),
                self._config.redirect_policy,
                self._config.retry_policy,
                self._config.authentication_policy,
                self._config.custom_hook_policy,
                self._config.logging_policy,
                policies.DistributedTracingPolicy(**kwargs),
                policies.SensitiveHeaderCleanupPolicy(**kwargs) if self._config.redirect_policy else None,
                self._config.http_logging_policy,
            ]
        self._client: ARMPipelineClient = ARMPipelineClient(base_url=base_url, policies=_policies, **kwargs)

        client_models = {k: v for k, v in _models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)
        self._serialize.client_side_validation = False
        self.operations = Operations(self._client, self._config, self._serialize, self._deserialize)
        self.workspaces = WorkspacesOperations(self._client, self._config, self._serialize, self._deserialize)
        self.private_endpoint_connections = PrivateEndpointConnectionsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.private_link_resources = PrivateLinkResourcesOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.scaling_plans = ScalingPlansOperations(self._client, self._config, self._serialize, self._deserialize)
        self.scaling_plan_pooled_schedules = ScalingPlanPooledSchedulesOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.scaling_plan_personal_schedules = ScalingPlanPersonalSchedulesOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.application_groups = ApplicationGroupsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.start_menu_items = StartMenuItemsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.applications = ApplicationsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.desktops = DesktopsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.host_pools = HostPoolsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.session_host_managements = SessionHostManagementsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.initiate_session_host_update = InitiateSessionHostUpdateOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.control_session_host_update = ControlSessionHostUpdateOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.session_host_managements_operation_status = SessionHostManagementsOperationStatusOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.session_host_configurations = SessionHostConfigurationsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.session_host_configurations_operation_status = SessionHostConfigurationsOperationStatusOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.active_session_host_configurations = ActiveSessionHostConfigurationsOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.user_sessions = UserSessionsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.session_hosts = SessionHostsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.session_host = SessionHostOperations(self._client, self._config, self._serialize, self._deserialize)
        self.msix_packages = MSIXPackagesOperations(self._client, self._config, self._serialize, self._deserialize)
        self.app_attach_package_info = AppAttachPackageInfoOperations(
            self._client, self._config, self._serialize, self._deserialize
        )
        self.msix_images = MsixImagesOperations(self._client, self._config, self._serialize, self._deserialize)
        self.app_attach_package = AppAttachPackageOperations(
            self._client, self._config, self._serialize, self._deserialize
        )

    def _send_request(self, request: HttpRequest, *, stream: bool = False, **kwargs: Any) -> HttpResponse:
        """Runs the network request through the client's chained policies.

        >>> from azure.core.rest import HttpRequest
        >>> request = HttpRequest("GET", "https://www.example.org/")
        <HttpRequest [GET], url: 'https://www.example.org/'>
        >>> response = client._send_request(request)
        <HttpResponse: 200 OK>

        For more information on this code flow, see https://aka.ms/azsdk/dpcodegen/python/send_request

        :param request: The network request you want to make. Required.
        :type request: ~azure.core.rest.HttpRequest
        :keyword bool stream: Whether the response payload will be streamed. Defaults to False.
        :return: The response of your network call. Does not do error handling on your response.
        :rtype: ~azure.core.rest.HttpResponse
        """

        request_copy = deepcopy(request)
        request_copy.url = self._client.format_url(request_copy.url)
        return self._client.send_request(request_copy, stream=stream, **kwargs)  # type: ignore

    def close(self) -> None:
        self._client.close()

    def __enter__(self) -> "DesktopVirtualizationMgmtClient":
        self._client.__enter__()
        return self

    def __exit__(self, *exc_details: Any) -> None:
        self._client.__exit__(*exc_details)
