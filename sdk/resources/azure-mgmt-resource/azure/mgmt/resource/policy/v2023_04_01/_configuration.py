# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Any, TYPE_CHECKING

from azure.core.configuration import Configuration
from azure.core.pipeline import policies
from azure.mgmt.core.policies import ARMChallengeAuthenticationPolicy, ARMHttpLoggingPolicy

from ._version import VERSION

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from azure.core.credentials import TokenCredential


class PolicyClientConfiguration(Configuration):  # pylint: disable=too-many-instance-attributes
    """Configuration for PolicyClient.

    Note that all parameters used to create this instance are saved as instance
    attributes.

    :param credential: Credential needed for the client to connect to Azure. Required.
    :type credential: ~azure.core.credentials.TokenCredential
    :param policy_definition_name: The name of the policy definition. Required.
    :type policy_definition_name: str
    :param policy_definition_version: The policy definition version.  The format is x.y.z where x
     is the major version number, y is the minor version number, and z is the patch number.
     Required.
    :type policy_definition_version: str
    :param policy_set_definition_name: The name of the policy set definition. Required.
    :type policy_set_definition_name: str
    :param subscription_id: The ID of the target subscription. The value must be an UUID. Required.
    :type subscription_id: str
    :keyword api_version: Api Version. Default value is "2023-04-01". Note that overriding this
     default value may result in unsupported behavior.
    :paramtype api_version: str
    """

    def __init__(
        self,
        credential: "TokenCredential",
        policy_definition_name: str,
        policy_definition_version: str,
        policy_set_definition_name: str,
        subscription_id: str,
        **kwargs: Any
    ) -> None:
        super(PolicyClientConfiguration, self).__init__(**kwargs)
        api_version: str = kwargs.pop("api_version", "2023-04-01")

        if credential is None:
            raise ValueError("Parameter 'credential' must not be None.")
        if policy_definition_name is None:
            raise ValueError("Parameter 'policy_definition_name' must not be None.")
        if policy_definition_version is None:
            raise ValueError("Parameter 'policy_definition_version' must not be None.")
        if policy_set_definition_name is None:
            raise ValueError("Parameter 'policy_set_definition_name' must not be None.")
        if subscription_id is None:
            raise ValueError("Parameter 'subscription_id' must not be None.")

        self.credential = credential
        self.policy_definition_name = policy_definition_name
        self.policy_definition_version = policy_definition_version
        self.policy_set_definition_name = policy_set_definition_name
        self.subscription_id = subscription_id
        self.api_version = api_version
        self.credential_scopes = kwargs.pop("credential_scopes", ["https://management.azure.com/.default"])
        kwargs.setdefault("sdk_moniker", "mgmt-resource/{}".format(VERSION))
        self._configure(**kwargs)

    def _configure(self, **kwargs: Any) -> None:
        self.user_agent_policy = kwargs.get("user_agent_policy") or policies.UserAgentPolicy(**kwargs)
        self.headers_policy = kwargs.get("headers_policy") or policies.HeadersPolicy(**kwargs)
        self.proxy_policy = kwargs.get("proxy_policy") or policies.ProxyPolicy(**kwargs)
        self.logging_policy = kwargs.get("logging_policy") or policies.NetworkTraceLoggingPolicy(**kwargs)
        self.http_logging_policy = kwargs.get("http_logging_policy") or ARMHttpLoggingPolicy(**kwargs)
        self.retry_policy = kwargs.get("retry_policy") or policies.RetryPolicy(**kwargs)
        self.custom_hook_policy = kwargs.get("custom_hook_policy") or policies.CustomHookPolicy(**kwargs)
        self.redirect_policy = kwargs.get("redirect_policy") or policies.RedirectPolicy(**kwargs)
        self.authentication_policy = kwargs.get("authentication_policy")
        if self.credential and not self.authentication_policy:
            self.authentication_policy = ARMChallengeAuthenticationPolicy(
                self.credential, *self.credential_scopes, **kwargs
            )
