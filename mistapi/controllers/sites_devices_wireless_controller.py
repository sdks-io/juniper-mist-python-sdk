# -*- coding: utf-8 -*-

"""
mistapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

from mistapi.api_helper import APIHelper
from mistapi.configuration import Server
from mistapi.controllers.base_controller import BaseController
from apimatic_core.request_builder import RequestBuilder
from apimatic_core.response_handler import ResponseHandler
from apimatic_core.types.parameter import Parameter
from mistapi.http.http_method_enum import HttpMethodEnum
from apimatic_core.authentication.multiple.single_auth import Single
from apimatic_core.authentication.multiple.and_auth_group import And
from apimatic_core.authentication.multiple.or_auth_group import Or
from mistapi.models.device_radio_channels import DeviceRadioChannels
from mistapi.exceptions.api_exception import APIException
from mistapi.exceptions.api_v_1_sites_devices_ap_channels_401_error_exception import ApiV1SitesDevicesApChannels401ErrorException
from mistapi.exceptions.api_v_1_sites_devices_ap_channels_403_error_exception import ApiV1SitesDevicesApChannels403ErrorException
from mistapi.exceptions.api_v_1_sites_devices_ap_channels_404_error_exception import ApiV1SitesDevicesApChannels404ErrorException
from mistapi.exceptions.api_v_1_sites_devices_reprovision_401_error_exception import ApiV1SitesDevicesReprovision401ErrorException
from mistapi.exceptions.api_v_1_sites_devices_reprovision_403_error_exception import ApiV1SitesDevicesReprovision403ErrorException
from mistapi.exceptions.api_v_1_sites_devices_reprovision_404_error_exception import ApiV1SitesDevicesReprovision404ErrorException
from mistapi.exceptions.api_v_1_sites_devices_reset_radio_config_401_error_exception import ApiV1SitesDevicesResetRadioConfig401ErrorException
from mistapi.exceptions.api_v_1_sites_devices_reset_radio_config_403_error_exception import ApiV1SitesDevicesResetRadioConfig403ErrorException
from mistapi.exceptions.api_v_1_sites_devices_reset_radio_config_404_error_exception import ApiV1SitesDevicesResetRadioConfig404ErrorException
from mistapi.exceptions.api_v_1_sites_devices_zerioze_401_error_exception import ApiV1SitesDevicesZerioze401ErrorException
from mistapi.exceptions.api_v_1_sites_devices_zerioze_403_error_exception import ApiV1SitesDevicesZerioze403ErrorException
from mistapi.exceptions.api_v_1_sites_devices_zerioze_404_error_exception import ApiV1SitesDevicesZerioze404ErrorException
from mistapi.exceptions.api_v_1_sites_devices_iot_401_error_exception import ApiV1SitesDevicesIot401ErrorException
from mistapi.exceptions.api_v_1_sites_devices_iot_403_error_exception import ApiV1SitesDevicesIot403ErrorException
from mistapi.exceptions.api_v_1_sites_devices_iot_404_error_exception import ApiV1SitesDevicesIot404ErrorException
from mistapi.exceptions.api_v_1_sites_devices_locate_401_error_exception import ApiV1SitesDevicesLocate401ErrorException
from mistapi.exceptions.api_v_1_sites_devices_locate_403_error_exception import ApiV1SitesDevicesLocate403ErrorException
from mistapi.exceptions.api_v_1_sites_devices_locate_404_error_exception import ApiV1SitesDevicesLocate404ErrorException
from mistapi.exceptions.api_v_1_sites_devices_unlocate_401_error_exception import ApiV1SitesDevicesUnlocate401ErrorException
from mistapi.exceptions.api_v_1_sites_devices_unlocate_403_error_exception import ApiV1SitesDevicesUnlocate403ErrorException
from mistapi.exceptions.api_v_1_sites_devices_unlocate_404_error_exception import ApiV1SitesDevicesUnlocate404ErrorException


class SitesDevicesWirelessController(BaseController):

    """A Controller to access Endpoints in the mistapi API."""
    def __init__(self, config):
        super(SitesDevicesWirelessController, self).__init__(config)

    def get_site_device_radio_channels(self,
                                       site_id,
                                       country_code=None):
        """Does a GET request to /api/v1/sites/{site_id}/devices/ap_channels.

        Get a list of allowed channels (per channel width)

        Args:
            site_id (uuid|string): TODO: type description here.
            country_code (string, optional): country code for the site (for AP
                config generation), in
                [two-character](http://en.wikipedia.org/wiki/ISO_3166-1_alpha-2
                )

        Returns:
            DeviceRadioChannels: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/api/v1/sites/{site_id}/devices/ap_channels')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('site_id')
                            .value(site_id)
                            .should_encode(True))
            .query_param(Parameter()
                         .key('country_code')
                         .value(country_code))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('global'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(DeviceRadioChannels.from_dictionary)
            .local_error('400', 'The API endpoint exists but its syntax/payload is incorrect, detail may be given', APIException)
            .local_error('401', 'Unauthorized', ApiV1SitesDevicesApChannels401ErrorException)
            .local_error('403', 'Permission Denied', ApiV1SitesDevicesApChannels403ErrorException)
            .local_error('404', 'Not found. The API endpoint doesn\'t exist or resource doesn\'t exist', ApiV1SitesDevicesApChannels404ErrorException)
        ).execute()

    def reprovision_site_all_aps(self,
                                 site_id):
        """Does a POST request to /api/v1/sites/{site_id}/devices/reprovision.

        To force all APs to reprovision itself again. 

        Args:
            site_id (uuid|string): TODO: type description here.

        Returns:
            object: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/api/v1/sites/{site_id}/devices/reprovision')
            .http_method(HttpMethodEnum.POST)
            .template_param(Parameter()
                            .key('site_id')
                            .value(site_id)
                            .should_encode(True))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('global'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .local_error('400', 'The API endpoint exists but its syntax/payload is incorrect, detail may be given', APIException)
            .local_error('401', 'Unauthorized', ApiV1SitesDevicesReprovision401ErrorException)
            .local_error('403', 'Permission Denied', ApiV1SitesDevicesReprovision403ErrorException)
            .local_error('404', 'Not found. The API endpoint doesn\'t exist or resource doesn\'t exist', ApiV1SitesDevicesReprovision404ErrorException)
        ).execute()

    def reset_site_all_aps_to_use_rrm(self,
                                      site_id,
                                      body=None):
        """Does a POST request to /api/v1/sites/{site_id}/devices/reset_radio_config.

        Reset all APs in the Site to use RRM

        Args:
            site_id (uuid|string): TODO: type description here.
            body (ApiV1SitesDevicesResetRadioConfigRequest, optional): Request
                Body

        Returns:
            object: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/api/v1/sites/{site_id}/devices/reset_radio_config')
            .http_method(HttpMethodEnum.POST)
            .template_param(Parameter()
                            .key('site_id')
                            .value(site_id)
                            .should_encode(True))
            .header_param(Parameter()
                          .key('Content-Type')
                          .value('application/json'))
            .body_param(Parameter()
                        .value(body))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .body_serializer(APIHelper.json_serialize)
            .auth(Single('global'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .local_error('400', 'The API endpoint exists but its syntax/payload is incorrect, detail may be given', APIException)
            .local_error('401', 'Unauthorized', ApiV1SitesDevicesResetRadioConfig401ErrorException)
            .local_error('403', 'Permission Denied', ApiV1SitesDevicesResetRadioConfig403ErrorException)
            .local_error('404', 'Not found. The API endpoint doesn\'t exist or resource doesn\'t exist', ApiV1SitesDevicesResetRadioConfig404ErrorException)
        ).execute()

    def zeroize_site_fips_all_aps(self,
                                  site_id,
                                  body=None):
        """Does a POST request to /api/v1/sites/{site_id}/devices/zerioze.

        Zeroize all FIPS APs in the Site

        Args:
            site_id (uuid|string): TODO: type description here.
            body (ApiV1SitesDevicesZeriozeRequest, optional): Request Body

        Returns:
            object: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/api/v1/sites/{site_id}/devices/zerioze')
            .http_method(HttpMethodEnum.POST)
            .template_param(Parameter()
                            .key('site_id')
                            .value(site_id)
                            .should_encode(True))
            .header_param(Parameter()
                          .key('Content-Type')
                          .value('application/json'))
            .body_param(Parameter()
                        .value(body))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .body_serializer(APIHelper.json_serialize)
            .auth(Single('global'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .local_error('400', 'The API endpoint exists but its syntax/payload is incorrect, detail may be given', APIException)
            .local_error('401', 'Unauthorized', ApiV1SitesDevicesZerioze401ErrorException)
            .local_error('403', 'Permission Denied', ApiV1SitesDevicesZerioze403ErrorException)
            .local_error('404', 'Not found. The API endpoint doesn\'t exist or resource doesn\'t exist', ApiV1SitesDevicesZerioze404ErrorException)
        ).execute()

    def get_site_device_iot_port(self,
                                 site_id,
                                 device_id):
        """Does a GET request to /api/v1/sites/{site_id}/devices/{device_id}/iot.

        Returns the current state of each enabled IoT pin configured as an
        output.

        Args:
            site_id (uuid|string): TODO: type description here.
            device_id (uuid|string): TODO: type description here.

        Returns:
            dict: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/api/v1/sites/{site_id}/devices/{device_id}/iot')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('site_id')
                            .value(site_id)
                            .should_encode(True))
            .template_param(Parameter()
                            .key('device_id')
                            .value(device_id)
                            .should_encode(True))
            .auth(Single('global'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .local_error('400', 'The API endpoint exists but its syntax/payload is incorrect, detail may be given', APIException)
            .local_error('401', 'Unauthorized', ApiV1SitesDevicesIot401ErrorException)
            .local_error('403', 'Permission Denied', ApiV1SitesDevicesIot403ErrorException)
            .local_error('404', 'Not found. The API endpoint doesn\'t exist or resource doesn\'t exist', ApiV1SitesDevicesIot404ErrorException)
        ).execute()

    def set_site_device_iot_port(self,
                                 site_id,
                                 device_id,
                                 body=None):
        """Does a PUT request to /api/v1/sites/{site_id}/devices/{device_id}/iot.

        **Note**: For each IoT pin referenced:
         * The pin must be enabled using the Device `iot_config` API
         * The pin must support the output direction

        Args:
            site_id (uuid|string): TODO: type description here.
            device_id (uuid|string): TODO: type description here.
            body (dict, optional): Request Body

        Returns:
            dict: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/api/v1/sites/{site_id}/devices/{device_id}/iot')
            .http_method(HttpMethodEnum.PUT)
            .template_param(Parameter()
                            .key('site_id')
                            .value(site_id)
                            .should_encode(True))
            .template_param(Parameter()
                            .key('device_id')
                            .value(device_id)
                            .should_encode(True))
            .header_param(Parameter()
                          .key('Content-Type')
                          .value('application/json'))
            .body_param(Parameter()
                        .value(body))
            .body_serializer(str)
            .auth(Single('global'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .local_error('400', 'The API endpoint exists but its syntax/payload is incorrect, detail may be given', APIException)
            .local_error('401', 'Unauthorized', ApiV1SitesDevicesIot401ErrorException)
            .local_error('403', 'Permission Denied', ApiV1SitesDevicesIot403ErrorException)
            .local_error('404', 'Not found. The API endpoint doesn\'t exist or resource doesn\'t exist', ApiV1SitesDevicesIot404ErrorException)
        ).execute()

    def start_site_locate_device(self,
                                 site_id,
                                 device_id):
        """Does a POST request to /api/v1/sites/{site_id}/devices/{device_id}/locate.

        Locate a Device by blinking it’s LED, it’s a persisted state that has
        to be stopped by calling Stop Locating API

        Args:
            site_id (uuid|string): TODO: type description here.
            device_id (uuid|string): TODO: type description here.

        Returns:
            object: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/api/v1/sites/{site_id}/devices/{device_id}/locate')
            .http_method(HttpMethodEnum.POST)
            .template_param(Parameter()
                            .key('site_id')
                            .value(site_id)
                            .should_encode(True))
            .template_param(Parameter()
                            .key('device_id')
                            .value(device_id)
                            .should_encode(True))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('global'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .local_error('400', 'The API endpoint exists but its syntax/payload is incorrect, detail may be given', APIException)
            .local_error('401', 'Unauthorized', ApiV1SitesDevicesLocate401ErrorException)
            .local_error('403', 'Permission Denied', ApiV1SitesDevicesLocate403ErrorException)
            .local_error('404', 'Not found. The API endpoint doesn\'t exist or resource doesn\'t exist', ApiV1SitesDevicesLocate404ErrorException)
        ).execute()

    def stop_site_locate_device(self,
                                site_id,
                                device_id):
        """Does a POST request to /api/v1/sites/{site_id}/devices/{device_id}/unlocate.

        Stop Locate a Device

        Args:
            site_id (uuid|string): TODO: type description here.
            device_id (uuid|string): TODO: type description here.

        Returns:
            object: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/api/v1/sites/{site_id}/devices/{device_id}/unlocate')
            .http_method(HttpMethodEnum.POST)
            .template_param(Parameter()
                            .key('site_id')
                            .value(site_id)
                            .should_encode(True))
            .template_param(Parameter()
                            .key('device_id')
                            .value(device_id)
                            .should_encode(True))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('global'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .local_error('400', 'The API endpoint exists but its syntax/payload is incorrect, detail may be given', APIException)
            .local_error('401', 'Unauthorized', ApiV1SitesDevicesUnlocate401ErrorException)
            .local_error('403', 'Permission Denied', ApiV1SitesDevicesUnlocate403ErrorException)
            .local_error('404', 'Not found. The API endpoint doesn\'t exist or resource doesn\'t exist', ApiV1SitesDevicesUnlocate404ErrorException)
        ).execute()
