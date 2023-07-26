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
from mistapi.models.session_1 import Session1
from mistapi.models.api_v_1_sites_synthetic_test_response import ApiV1SitesSyntheticTestResponse
from mistapi.models.api_v_1_sites_synthetic_test_response_1 import ApiV1SitesSyntheticTestResponse1
from mistapi.exceptions.api_exception import APIException
from mistapi.exceptions.api_v_1_sites_devices_check_radius_server_401_error_exception import ApiV1SitesDevicesCheckRadiusServer401ErrorException
from mistapi.exceptions.api_v_1_sites_devices_check_radius_server_403_error_exception import ApiV1SitesDevicesCheckRadiusServer403ErrorException
from mistapi.exceptions.api_v_1_sites_devices_check_radius_server_404_error_exception import ApiV1SitesDevicesCheckRadiusServer404ErrorException
from mistapi.exceptions.api_v_1_sites_devices_synthetic_test_401_error_exception import ApiV1SitesDevicesSyntheticTest401ErrorException
from mistapi.exceptions.api_v_1_sites_devices_synthetic_test_403_error_exception import ApiV1SitesDevicesSyntheticTest403ErrorException
from mistapi.exceptions.api_v_1_sites_devices_synthetic_test_404_error_exception import ApiV1SitesDevicesSyntheticTest404ErrorException
from mistapi.exceptions.api_v_1_sites_synthetic_test_401_error_exception import ApiV1SitesSyntheticTest401ErrorException
from mistapi.exceptions.api_v_1_sites_synthetic_test_403_error_exception import ApiV1SitesSyntheticTest403ErrorException
from mistapi.exceptions.api_v_1_sites_synthetic_test_404_error_exception import ApiV1SitesSyntheticTest404ErrorException


class SitesSyntheticTestsController(BaseController):

    """A Controller to access Endpoints in the mistapi API."""
    def __init__(self, config):
        super(SitesSyntheticTestsController, self).__init__(config)

    def start_site_switch_radius_synthetic_test(self,
                                                site_id,
                                                device_id,
                                                body=None):
        """Does a POST request to /api/v1/sites/{site_id}/devices/{device_id}/check_radius_server.

        Ping test from the AP to confirm ‘reachability’ of the Radius server.
        Utilize Juniper EX switch(to which an AP is connected to) radius test
        capabilities to get details on the Radius Server ‘availability’.

        Args:
            site_id (uuid|string): TODO: type description here.
            device_id (uuid|string): TODO: type description here.
            body (ApiV1SitesDevicesCheckRadiusServerRequest, optional): TODO:
                type description here.

        Returns:
            Session1: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/api/v1/sites/{site_id}/devices/{device_id}/check_radius_server')
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
            .deserialize_into(Session1.from_dictionary)
            .local_error('400', 'The API endpoint exists but its syntax/payload is incorrect, detail may be given', APIException)
            .local_error('401', 'Unauthorized', ApiV1SitesDevicesCheckRadiusServer401ErrorException)
            .local_error('403', 'Permission Denied', ApiV1SitesDevicesCheckRadiusServer403ErrorException)
            .local_error('404', 'Not found. The API endpoint doesn\'t exist or resource doesn\'t exist', ApiV1SitesDevicesCheckRadiusServer404ErrorException)
        ).execute()

    def start_site_device_synthetic_test(self,
                                         site_id,
                                         device_id,
                                         body=None):
        """Does a POST request to /api/v1/sites/{site_id}/devices/{device_id}/synthetic_test.

        Device Synthetic Test

        Args:
            site_id (uuid|string): TODO: type description here.
            device_id (uuid|string): TODO: type description here.
            body (ApiV1SitesDevicesSyntheticTestRequest, optional): TODO: type
                description here.

        Returns:
            void: Response from the API. scheduled

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/api/v1/sites/{site_id}/devices/{device_id}/synthetic_test')
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
                          .key('Content-Type')
                          .value('application/json'))
            .body_param(Parameter()
                        .value(body))
            .body_serializer(APIHelper.json_serialize)
            .auth(Single('global'))
        ).execute()

    def get_site_synthetic_test_status(self,
                                       site_id):
        """Does a GET request to /api/v1/sites/{site_id}/synthetic_test.

        Get Synthetic Testing Status

        Args:
            site_id (uuid|string): TODO: type description here.

        Returns:
            ApiV1SitesSyntheticTestResponse: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/api/v1/sites/{site_id}/synthetic_test')
            .http_method(HttpMethodEnum.GET)
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
            .deserialize_into(ApiV1SitesSyntheticTestResponse.from_dictionary)
            .local_error('400', 'The API endpoint exists but its syntax/payload is incorrect, detail may be given', APIException)
            .local_error('401', 'Unauthorized', ApiV1SitesSyntheticTest401ErrorException)
            .local_error('403', 'Permission Denied', ApiV1SitesSyntheticTest403ErrorException)
            .local_error('404', 'Not found. The API endpoint doesn\'t exist or resource doesn\'t exist', ApiV1SitesSyntheticTest404ErrorException)
        ).execute()

    def trigger_site_synthetic_test(self,
                                    site_id,
                                    body=None):
        """Does a POST request to /api/v1/sites/{site_id}/synthetic_test.

        Trigger Synthetic Testing

        Args:
            site_id (uuid|string): TODO: type description here.
            body (ApiV1SitesSyntheticTestRequest, optional): TODO: type
                description here.

        Returns:
            ApiV1SitesSyntheticTestResponse1: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/api/v1/sites/{site_id}/synthetic_test')
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
            .deserialize_into(ApiV1SitesSyntheticTestResponse1.from_dictionary)
            .local_error('400', 'The API endpoint exists but its syntax/payload is incorrect, detail may be given', APIException)
            .local_error('401', 'Unauthorized', ApiV1SitesSyntheticTest401ErrorException)
            .local_error('403', 'Permission Denied', ApiV1SitesSyntheticTest403ErrorException)
            .local_error('404', 'Not found. The API endpoint doesn\'t exist or resource doesn\'t exist', ApiV1SitesSyntheticTest404ErrorException)
        ).execute()
