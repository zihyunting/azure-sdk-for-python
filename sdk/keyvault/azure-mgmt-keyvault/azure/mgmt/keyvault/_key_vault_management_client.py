# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from typing import Any, Optional, TYPE_CHECKING

from azure.mgmt.core import ARMPipelineClient
from azure.profiles import KnownProfiles, ProfileDefinition
from azure.profiles.multiapiclient import MultiApiClientMixin

from ._configuration import KeyVaultManagementClientConfiguration
from ._serialization import Deserializer, Serializer

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from azure.core.credentials import TokenCredential

class _SDKClient(object):
    def __init__(self, *args, **kwargs):
        """This is a fake class to support current implemetation of MultiApiClientMixin."
        Will be removed in final version of multiapi azure-core based client
        """
        pass

class KeyVaultManagementClient(MultiApiClientMixin, _SDKClient):
    """The Azure management API provides a RESTful set of web services that interact with Azure Key Vault.

    This ready contains multiple API versions, to help you deal with all of the Azure clouds
    (Azure Stack, Azure Government, Azure China, etc.).
    By default, it uses the latest API version available on public Azure.
    For production, you should stick to a particular api-version and/or profile.
    The profile sets a mapping between an operation group and its API version.
    The api-version parameter sets the default API version if the operation
    group is not described in the profile.

    :param credential: Credential needed for the client to connect to Azure. Required.
    :type credential: ~azure.core.credentials.TokenCredential
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. Required.
    :type subscription_id: str
    :param api_version: API version to use if no profile is provided, or if missing in profile.
    :type api_version: str
    :param base_url: Service URL
    :type base_url: str
    :param profile: A profile definition, from KnownProfiles to dict.
    :type profile: azure.profiles.KnownProfiles
    :keyword int polling_interval: Default waiting time between two polls for LRO operations if no Retry-After header is present.
    """

    DEFAULT_API_VERSION = '2022-07-01'
    _PROFILE_TAG = "azure.mgmt.keyvault.KeyVaultManagementClient"
    LATEST_PROFILE = ProfileDefinition({
        _PROFILE_TAG: {
            None: DEFAULT_API_VERSION,
        }},
        _PROFILE_TAG + " latest"
    )

    def __init__(
        self,
        credential: "TokenCredential",
        subscription_id: str,
        api_version=None, # type: Optional[str]
        base_url: str = "https://management.azure.com",
        profile=KnownProfiles.default, # type: KnownProfiles
        **kwargs  # type: Any
    ):
        self._config = KeyVaultManagementClientConfiguration(credential, subscription_id, **kwargs)
        self._client = ARMPipelineClient(base_url=base_url, config=self._config, **kwargs)
        super(KeyVaultManagementClient, self).__init__(
            api_version=api_version,
            profile=profile
        )

    @classmethod
    def _models_dict(cls, api_version):
        return {k: v for k, v in cls.models(api_version).__dict__.items() if isinstance(v, type)}

    @classmethod
    def models(cls, api_version=DEFAULT_API_VERSION):
        """Module depends on the API version:

           * 2016-10-01: :mod:`v2016_10_01.models<azure.mgmt.keyvault.v2016_10_01.models>`
           * 2018-02-14: :mod:`v2018_02_14.models<azure.mgmt.keyvault.v2018_02_14.models>`
           * 2019-09-01: :mod:`v2019_09_01.models<azure.mgmt.keyvault.v2019_09_01.models>`
           * 2020-04-01-preview: :mod:`v2020_04_01_preview.models<azure.mgmt.keyvault.v2020_04_01_preview.models>`
           * 2021-04-01-preview: :mod:`v2021_04_01_preview.models<azure.mgmt.keyvault.v2021_04_01_preview.models>`
           * 2021-06-01-preview: :mod:`v2021_06_01_preview.models<azure.mgmt.keyvault.v2021_06_01_preview.models>`
           * 2021-10-01: :mod:`v2021_10_01.models<azure.mgmt.keyvault.v2021_10_01.models>`
           * 2022-07-01: :mod:`v2022_07_01.models<azure.mgmt.keyvault.v2022_07_01.models>`
        """
        if api_version == '2016-10-01':
            from .v2016_10_01 import models
            return models
        elif api_version == '2018-02-14':
            from .v2018_02_14 import models
            return models
        elif api_version == '2019-09-01':
            from .v2019_09_01 import models
            return models
        elif api_version == '2020-04-01-preview':
            from .v2020_04_01_preview import models
            return models
        elif api_version == '2021-04-01-preview':
            from .v2021_04_01_preview import models
            return models
        elif api_version == '2021-06-01-preview':
            from .v2021_06_01_preview import models
            return models
        elif api_version == '2021-10-01':
            from .v2021_10_01 import models
            return models
        elif api_version == '2022-07-01':
            from .v2022_07_01 import models
            return models
        raise ValueError("API version {} is not available".format(api_version))

    @property
    def keys(self):
        """Instance depends on the API version:

           * 2019-09-01: :class:`KeysOperations<azure.mgmt.keyvault.v2019_09_01.operations.KeysOperations>`
           * 2020-04-01-preview: :class:`KeysOperations<azure.mgmt.keyvault.v2020_04_01_preview.operations.KeysOperations>`
           * 2021-06-01-preview: :class:`KeysOperations<azure.mgmt.keyvault.v2021_06_01_preview.operations.KeysOperations>`
           * 2021-10-01: :class:`KeysOperations<azure.mgmt.keyvault.v2021_10_01.operations.KeysOperations>`
           * 2022-07-01: :class:`KeysOperations<azure.mgmt.keyvault.v2022_07_01.operations.KeysOperations>`
        """
        api_version = self._get_api_version('keys')
        if api_version == '2019-09-01':
            from .v2019_09_01.operations import KeysOperations as OperationClass
        elif api_version == '2020-04-01-preview':
            from .v2020_04_01_preview.operations import KeysOperations as OperationClass
        elif api_version == '2021-06-01-preview':
            from .v2021_06_01_preview.operations import KeysOperations as OperationClass
        elif api_version == '2021-10-01':
            from .v2021_10_01.operations import KeysOperations as OperationClass
        elif api_version == '2022-07-01':
            from .v2022_07_01.operations import KeysOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'keys'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def managed_hsms(self):
        """Instance depends on the API version:

           * 2020-04-01-preview: :class:`ManagedHsmsOperations<azure.mgmt.keyvault.v2020_04_01_preview.operations.ManagedHsmsOperations>`
           * 2021-04-01-preview: :class:`ManagedHsmsOperations<azure.mgmt.keyvault.v2021_04_01_preview.operations.ManagedHsmsOperations>`
           * 2021-06-01-preview: :class:`ManagedHsmsOperations<azure.mgmt.keyvault.v2021_06_01_preview.operations.ManagedHsmsOperations>`
           * 2021-10-01: :class:`ManagedHsmsOperations<azure.mgmt.keyvault.v2021_10_01.operations.ManagedHsmsOperations>`
           * 2022-07-01: :class:`ManagedHsmsOperations<azure.mgmt.keyvault.v2022_07_01.operations.ManagedHsmsOperations>`
        """
        api_version = self._get_api_version('managed_hsms')
        if api_version == '2020-04-01-preview':
            from .v2020_04_01_preview.operations import ManagedHsmsOperations as OperationClass
        elif api_version == '2021-04-01-preview':
            from .v2021_04_01_preview.operations import ManagedHsmsOperations as OperationClass
        elif api_version == '2021-06-01-preview':
            from .v2021_06_01_preview.operations import ManagedHsmsOperations as OperationClass
        elif api_version == '2021-10-01':
            from .v2021_10_01.operations import ManagedHsmsOperations as OperationClass
        elif api_version == '2022-07-01':
            from .v2022_07_01.operations import ManagedHsmsOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'managed_hsms'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def mhsm_private_endpoint_connections(self):
        """Instance depends on the API version:

           * 2021-04-01-preview: :class:`MHSMPrivateEndpointConnectionsOperations<azure.mgmt.keyvault.v2021_04_01_preview.operations.MHSMPrivateEndpointConnectionsOperations>`
           * 2021-06-01-preview: :class:`MHSMPrivateEndpointConnectionsOperations<azure.mgmt.keyvault.v2021_06_01_preview.operations.MHSMPrivateEndpointConnectionsOperations>`
           * 2021-10-01: :class:`MHSMPrivateEndpointConnectionsOperations<azure.mgmt.keyvault.v2021_10_01.operations.MHSMPrivateEndpointConnectionsOperations>`
           * 2022-07-01: :class:`MHSMPrivateEndpointConnectionsOperations<azure.mgmt.keyvault.v2022_07_01.operations.MHSMPrivateEndpointConnectionsOperations>`
        """
        api_version = self._get_api_version('mhsm_private_endpoint_connections')
        if api_version == '2021-04-01-preview':
            from .v2021_04_01_preview.operations import MHSMPrivateEndpointConnectionsOperations as OperationClass
        elif api_version == '2021-06-01-preview':
            from .v2021_06_01_preview.operations import MHSMPrivateEndpointConnectionsOperations as OperationClass
        elif api_version == '2021-10-01':
            from .v2021_10_01.operations import MHSMPrivateEndpointConnectionsOperations as OperationClass
        elif api_version == '2022-07-01':
            from .v2022_07_01.operations import MHSMPrivateEndpointConnectionsOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'mhsm_private_endpoint_connections'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def mhsm_private_link_resources(self):
        """Instance depends on the API version:

           * 2021-04-01-preview: :class:`MHSMPrivateLinkResourcesOperations<azure.mgmt.keyvault.v2021_04_01_preview.operations.MHSMPrivateLinkResourcesOperations>`
           * 2021-06-01-preview: :class:`MHSMPrivateLinkResourcesOperations<azure.mgmt.keyvault.v2021_06_01_preview.operations.MHSMPrivateLinkResourcesOperations>`
           * 2021-10-01: :class:`MHSMPrivateLinkResourcesOperations<azure.mgmt.keyvault.v2021_10_01.operations.MHSMPrivateLinkResourcesOperations>`
           * 2022-07-01: :class:`MHSMPrivateLinkResourcesOperations<azure.mgmt.keyvault.v2022_07_01.operations.MHSMPrivateLinkResourcesOperations>`
        """
        api_version = self._get_api_version('mhsm_private_link_resources')
        if api_version == '2021-04-01-preview':
            from .v2021_04_01_preview.operations import MHSMPrivateLinkResourcesOperations as OperationClass
        elif api_version == '2021-06-01-preview':
            from .v2021_06_01_preview.operations import MHSMPrivateLinkResourcesOperations as OperationClass
        elif api_version == '2021-10-01':
            from .v2021_10_01.operations import MHSMPrivateLinkResourcesOperations as OperationClass
        elif api_version == '2022-07-01':
            from .v2022_07_01.operations import MHSMPrivateLinkResourcesOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'mhsm_private_link_resources'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def operations(self):
        """Instance depends on the API version:

           * 2016-10-01: :class:`Operations<azure.mgmt.keyvault.v2016_10_01.operations.Operations>`
           * 2018-02-14: :class:`Operations<azure.mgmt.keyvault.v2018_02_14.operations.Operations>`
           * 2019-09-01: :class:`Operations<azure.mgmt.keyvault.v2019_09_01.operations.Operations>`
           * 2020-04-01-preview: :class:`Operations<azure.mgmt.keyvault.v2020_04_01_preview.operations.Operations>`
           * 2021-04-01-preview: :class:`Operations<azure.mgmt.keyvault.v2021_04_01_preview.operations.Operations>`
           * 2021-06-01-preview: :class:`Operations<azure.mgmt.keyvault.v2021_06_01_preview.operations.Operations>`
           * 2021-10-01: :class:`Operations<azure.mgmt.keyvault.v2021_10_01.operations.Operations>`
           * 2022-07-01: :class:`Operations<azure.mgmt.keyvault.v2022_07_01.operations.Operations>`
        """
        api_version = self._get_api_version('operations')
        if api_version == '2016-10-01':
            from .v2016_10_01.operations import Operations as OperationClass
        elif api_version == '2018-02-14':
            from .v2018_02_14.operations import Operations as OperationClass
        elif api_version == '2019-09-01':
            from .v2019_09_01.operations import Operations as OperationClass
        elif api_version == '2020-04-01-preview':
            from .v2020_04_01_preview.operations import Operations as OperationClass
        elif api_version == '2021-04-01-preview':
            from .v2021_04_01_preview.operations import Operations as OperationClass
        elif api_version == '2021-06-01-preview':
            from .v2021_06_01_preview.operations import Operations as OperationClass
        elif api_version == '2021-10-01':
            from .v2021_10_01.operations import Operations as OperationClass
        elif api_version == '2022-07-01':
            from .v2022_07_01.operations import Operations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'operations'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def private_endpoint_connections(self):
        """Instance depends on the API version:

           * 2018-02-14: :class:`PrivateEndpointConnectionsOperations<azure.mgmt.keyvault.v2018_02_14.operations.PrivateEndpointConnectionsOperations>`
           * 2019-09-01: :class:`PrivateEndpointConnectionsOperations<azure.mgmt.keyvault.v2019_09_01.operations.PrivateEndpointConnectionsOperations>`
           * 2020-04-01-preview: :class:`PrivateEndpointConnectionsOperations<azure.mgmt.keyvault.v2020_04_01_preview.operations.PrivateEndpointConnectionsOperations>`
           * 2021-04-01-preview: :class:`PrivateEndpointConnectionsOperations<azure.mgmt.keyvault.v2021_04_01_preview.operations.PrivateEndpointConnectionsOperations>`
           * 2021-06-01-preview: :class:`PrivateEndpointConnectionsOperations<azure.mgmt.keyvault.v2021_06_01_preview.operations.PrivateEndpointConnectionsOperations>`
           * 2021-10-01: :class:`PrivateEndpointConnectionsOperations<azure.mgmt.keyvault.v2021_10_01.operations.PrivateEndpointConnectionsOperations>`
           * 2022-07-01: :class:`PrivateEndpointConnectionsOperations<azure.mgmt.keyvault.v2022_07_01.operations.PrivateEndpointConnectionsOperations>`
        """
        api_version = self._get_api_version('private_endpoint_connections')
        if api_version == '2018-02-14':
            from .v2018_02_14.operations import PrivateEndpointConnectionsOperations as OperationClass
        elif api_version == '2019-09-01':
            from .v2019_09_01.operations import PrivateEndpointConnectionsOperations as OperationClass
        elif api_version == '2020-04-01-preview':
            from .v2020_04_01_preview.operations import PrivateEndpointConnectionsOperations as OperationClass
        elif api_version == '2021-04-01-preview':
            from .v2021_04_01_preview.operations import PrivateEndpointConnectionsOperations as OperationClass
        elif api_version == '2021-06-01-preview':
            from .v2021_06_01_preview.operations import PrivateEndpointConnectionsOperations as OperationClass
        elif api_version == '2021-10-01':
            from .v2021_10_01.operations import PrivateEndpointConnectionsOperations as OperationClass
        elif api_version == '2022-07-01':
            from .v2022_07_01.operations import PrivateEndpointConnectionsOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'private_endpoint_connections'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def private_link_resources(self):
        """Instance depends on the API version:

           * 2018-02-14: :class:`PrivateLinkResourcesOperations<azure.mgmt.keyvault.v2018_02_14.operations.PrivateLinkResourcesOperations>`
           * 2019-09-01: :class:`PrivateLinkResourcesOperations<azure.mgmt.keyvault.v2019_09_01.operations.PrivateLinkResourcesOperations>`
           * 2020-04-01-preview: :class:`PrivateLinkResourcesOperations<azure.mgmt.keyvault.v2020_04_01_preview.operations.PrivateLinkResourcesOperations>`
           * 2021-04-01-preview: :class:`PrivateLinkResourcesOperations<azure.mgmt.keyvault.v2021_04_01_preview.operations.PrivateLinkResourcesOperations>`
           * 2021-06-01-preview: :class:`PrivateLinkResourcesOperations<azure.mgmt.keyvault.v2021_06_01_preview.operations.PrivateLinkResourcesOperations>`
           * 2021-10-01: :class:`PrivateLinkResourcesOperations<azure.mgmt.keyvault.v2021_10_01.operations.PrivateLinkResourcesOperations>`
           * 2022-07-01: :class:`PrivateLinkResourcesOperations<azure.mgmt.keyvault.v2022_07_01.operations.PrivateLinkResourcesOperations>`
        """
        api_version = self._get_api_version('private_link_resources')
        if api_version == '2018-02-14':
            from .v2018_02_14.operations import PrivateLinkResourcesOperations as OperationClass
        elif api_version == '2019-09-01':
            from .v2019_09_01.operations import PrivateLinkResourcesOperations as OperationClass
        elif api_version == '2020-04-01-preview':
            from .v2020_04_01_preview.operations import PrivateLinkResourcesOperations as OperationClass
        elif api_version == '2021-04-01-preview':
            from .v2021_04_01_preview.operations import PrivateLinkResourcesOperations as OperationClass
        elif api_version == '2021-06-01-preview':
            from .v2021_06_01_preview.operations import PrivateLinkResourcesOperations as OperationClass
        elif api_version == '2021-10-01':
            from .v2021_10_01.operations import PrivateLinkResourcesOperations as OperationClass
        elif api_version == '2022-07-01':
            from .v2022_07_01.operations import PrivateLinkResourcesOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'private_link_resources'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def secrets(self):
        """Instance depends on the API version:

           * 2020-04-01-preview: :class:`SecretsOperations<azure.mgmt.keyvault.v2020_04_01_preview.operations.SecretsOperations>`
           * 2021-06-01-preview: :class:`SecretsOperations<azure.mgmt.keyvault.v2021_06_01_preview.operations.SecretsOperations>`
           * 2021-10-01: :class:`SecretsOperations<azure.mgmt.keyvault.v2021_10_01.operations.SecretsOperations>`
           * 2022-07-01: :class:`SecretsOperations<azure.mgmt.keyvault.v2022_07_01.operations.SecretsOperations>`
        """
        api_version = self._get_api_version('secrets')
        if api_version == '2020-04-01-preview':
            from .v2020_04_01_preview.operations import SecretsOperations as OperationClass
        elif api_version == '2021-06-01-preview':
            from .v2021_06_01_preview.operations import SecretsOperations as OperationClass
        elif api_version == '2021-10-01':
            from .v2021_10_01.operations import SecretsOperations as OperationClass
        elif api_version == '2022-07-01':
            from .v2022_07_01.operations import SecretsOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'secrets'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def vaults(self):
        """Instance depends on the API version:

           * 2016-10-01: :class:`VaultsOperations<azure.mgmt.keyvault.v2016_10_01.operations.VaultsOperations>`
           * 2018-02-14: :class:`VaultsOperations<azure.mgmt.keyvault.v2018_02_14.operations.VaultsOperations>`
           * 2019-09-01: :class:`VaultsOperations<azure.mgmt.keyvault.v2019_09_01.operations.VaultsOperations>`
           * 2020-04-01-preview: :class:`VaultsOperations<azure.mgmt.keyvault.v2020_04_01_preview.operations.VaultsOperations>`
           * 2021-04-01-preview: :class:`VaultsOperations<azure.mgmt.keyvault.v2021_04_01_preview.operations.VaultsOperations>`
           * 2021-06-01-preview: :class:`VaultsOperations<azure.mgmt.keyvault.v2021_06_01_preview.operations.VaultsOperations>`
           * 2021-10-01: :class:`VaultsOperations<azure.mgmt.keyvault.v2021_10_01.operations.VaultsOperations>`
           * 2022-07-01: :class:`VaultsOperations<azure.mgmt.keyvault.v2022_07_01.operations.VaultsOperations>`
        """
        api_version = self._get_api_version('vaults')
        if api_version == '2016-10-01':
            from .v2016_10_01.operations import VaultsOperations as OperationClass
        elif api_version == '2018-02-14':
            from .v2018_02_14.operations import VaultsOperations as OperationClass
        elif api_version == '2019-09-01':
            from .v2019_09_01.operations import VaultsOperations as OperationClass
        elif api_version == '2020-04-01-preview':
            from .v2020_04_01_preview.operations import VaultsOperations as OperationClass
        elif api_version == '2021-04-01-preview':
            from .v2021_04_01_preview.operations import VaultsOperations as OperationClass
        elif api_version == '2021-06-01-preview':
            from .v2021_06_01_preview.operations import VaultsOperations as OperationClass
        elif api_version == '2021-10-01':
            from .v2021_10_01.operations import VaultsOperations as OperationClass
        elif api_version == '2022-07-01':
            from .v2022_07_01.operations import VaultsOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'vaults'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    def close(self):
        self._client.close()
    def __enter__(self):
        self._client.__enter__()
        return self
    def __exit__(self, *exc_details):
        self._client.__exit__(*exc_details)
