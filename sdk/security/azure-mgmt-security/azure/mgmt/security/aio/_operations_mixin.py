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
from .._serialization import Serializer, Deserializer
from io import IOBase
from typing import Any, IO, Optional, Union

from .. import models as _models


class SecurityCenterOperationsMixin(object):

    async def get_sensitivity_settings(
        self,
        **kwargs: Any
    ) -> _models.GetSensitivitySettingsResponse:
        """Gets data sensitivity settings for sensitive data discovery.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: GetSensitivitySettingsResponse or the result of cls(response)
        :rtype: ~azure.mgmt.security.v2023_02_15_preview.models.GetSensitivitySettingsResponse
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        api_version = self._get_api_version('get_sensitivity_settings')
        if api_version == '2023-02-15-preview':
            from ..v2023_02_15_preview.aio.operations import SecurityCenterOperationsMixin as OperationClass
        else:
            raise ValueError("API version {} does not have operation 'get_sensitivity_settings'".format(api_version))
        mixin_instance = OperationClass()
        mixin_instance._client = self._client
        mixin_instance._config = self._config
        mixin_instance._config.api_version = api_version
        mixin_instance._serialize = Serializer(self._models_dict(api_version))
        mixin_instance._serialize.client_side_validation = False
        mixin_instance._deserialize = Deserializer(self._models_dict(api_version))
        return await mixin_instance.get_sensitivity_settings(**kwargs)

    async def update_sensitivity_settings(
        self,
        sensitivity_settings: Union[_models.UpdateSensitivitySettingsRequest, IO],
        **kwargs: Any
    ) -> _models.GetSensitivitySettingsResponse:
        """Updates data sensitivity settings for sensitive data discovery.

        :param sensitivity_settings: The data sensitivity settings to update. Is either a
         UpdateSensitivitySettingsRequest type or a IO type. Required.
        :type sensitivity_settings:
         ~azure.mgmt.security.v2023_02_15_preview.models.UpdateSensitivitySettingsRequest or IO
        :keyword content_type: Body Parameter content-type. Known values are: 'application/json'.
         Default value is None.
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: GetSensitivitySettingsResponse or the result of cls(response)
        :rtype: ~azure.mgmt.security.v2023_02_15_preview.models.GetSensitivitySettingsResponse
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        api_version = self._get_api_version('update_sensitivity_settings')
        if api_version == '2023-02-15-preview':
            from ..v2023_02_15_preview.aio.operations import SecurityCenterOperationsMixin as OperationClass
        else:
            raise ValueError("API version {} does not have operation 'update_sensitivity_settings'".format(api_version))
        mixin_instance = OperationClass()
        mixin_instance._client = self._client
        mixin_instance._config = self._config
        mixin_instance._config.api_version = api_version
        mixin_instance._serialize = Serializer(self._models_dict(api_version))
        mixin_instance._serialize.client_side_validation = False
        mixin_instance._deserialize = Deserializer(self._models_dict(api_version))
        return await mixin_instance.update_sensitivity_settings(sensitivity_settings, **kwargs)
