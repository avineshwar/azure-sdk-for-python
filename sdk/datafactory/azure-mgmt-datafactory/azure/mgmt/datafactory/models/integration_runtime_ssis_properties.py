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

from msrest.serialization import Model


class IntegrationRuntimeSsisProperties(Model):
    """SSIS properties for managed integration runtime.

    :param additional_properties: Unmatched properties from the message are
     deserialized this collection
    :type additional_properties: dict[str, object]
    :param catalog_info: Catalog information for managed dedicated integration
     runtime.
    :type catalog_info:
     ~azure.mgmt.datafactory.models.IntegrationRuntimeSsisCatalogInfo
    :param license_type: License type for bringing your own license scenario.
     Possible values include: 'BasePrice', 'LicenseIncluded'
    :type license_type: str or
     ~azure.mgmt.datafactory.models.IntegrationRuntimeLicenseType
    :param custom_setup_script_properties: Custom setup script properties for
     a managed dedicated integration runtime.
    :type custom_setup_script_properties:
     ~azure.mgmt.datafactory.models.IntegrationRuntimeCustomSetupScriptProperties
    :param data_proxy_properties: Data proxy properties for a managed
     dedicated integration runtime.
    :type data_proxy_properties:
     ~azure.mgmt.datafactory.models.IntegrationRuntimeDataProxyProperties
    :param edition: The edition for the SSIS Integration Runtime. Possible
     values include: 'Standard', 'Enterprise'
    :type edition: str or
     ~azure.mgmt.datafactory.models.IntegrationRuntimeEdition
    """

    _attribute_map = {
        'additional_properties': {'key': '', 'type': '{object}'},
        'catalog_info': {'key': 'catalogInfo', 'type': 'IntegrationRuntimeSsisCatalogInfo'},
        'license_type': {'key': 'licenseType', 'type': 'str'},
        'custom_setup_script_properties': {'key': 'customSetupScriptProperties', 'type': 'IntegrationRuntimeCustomSetupScriptProperties'},
        'data_proxy_properties': {'key': 'dataProxyProperties', 'type': 'IntegrationRuntimeDataProxyProperties'},
        'edition': {'key': 'edition', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(IntegrationRuntimeSsisProperties, self).__init__(**kwargs)
        self.additional_properties = kwargs.get('additional_properties', None)
        self.catalog_info = kwargs.get('catalog_info', None)
        self.license_type = kwargs.get('license_type', None)
        self.custom_setup_script_properties = kwargs.get('custom_setup_script_properties', None)
        self.data_proxy_properties = kwargs.get('data_proxy_properties', None)
        self.edition = kwargs.get('edition', None)