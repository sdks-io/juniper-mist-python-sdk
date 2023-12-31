# -*- coding: utf-8 -*-

"""
mistapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

import json
import dateutil.parser

from tests.controllers.controller_test_base import ControllerTestBase
from apimatic_core.utilities.comparison_helper import ComparisonHelper
from mistapi.api_helper import APIHelper
from mistapi.models.api_v_1_sites_devices_check_radius_server_request import ApiV1SitesDevicesCheckRadiusServerRequest
from mistapi.models.api_v_1_sites_devices_synthetic_test_request import ApiV1SitesDevicesSyntheticTestRequest
from mistapi.models.api_v_1_sites_synthetic_test_request import ApiV1SitesSyntheticTestRequest


class SitesSyntheticTestsControllerTests(ControllerTestBase):

    @classmethod
    def setUpClass(cls):
        super(SitesSyntheticTestsControllerTests, cls).setUpClass()
        cls.controller = cls.client.sites_synthetic_tests
        cls.response_catcher = cls.controller.http_call_back

    # Ping test from the AP to confirm ‘reachability’ of the Radius server. Utilize Juniper EX switch(to which an AP is connected to) radius test capabilities to get details on the Radius Server ‘availability’.
    def test_start_site_switch_radius_synthetic_test(self):
        # Parameters for the API call
        site_id = '000000ab-00ab-00ab-00ab-0000000000ab'
        device_id = '000000ab-00ab-00ab-00ab-0000000000ab'
        body = APIHelper.json_deserialize('{"password":"string","profile":"dot1x","user":"string"}', ApiV1SitesDevicesCheckRadiusServerRequest.from_dictionary)

        # Perform the API call through the SDK function
        result = self.controller.start_site_switch_radius_synthetic_test(site_id, device_id, body)

        # Test response code
        assert self.response_catcher.response.status_code == 200

        # Test headers
        expected_headers = {}
        expected_headers['content-type'] = 'application/json'

        assert ComparisonHelper.match_headers(expected_headers, self.response_catcher.response.headers)

        
        # Test whether the captured response is as we expected
        assert result is not None
        expected_body = APIHelper.json_deserialize('{"session":"session_id"}')
        received_body = APIHelper.json_deserialize(self.response_catcher.response.text)
        assert ComparisonHelper.match_body(expected_body, received_body)

    # Device Synthetic Test
    #
    def test_start_site_device_synthetic_test(self):
        # Parameters for the API call
        site_id = '000000ab-00ab-00ab-00ab-0000000000ab'
        device_id = '000000ab-00ab-00ab-00ab-0000000000ab'
        body = None

        # Perform the API call through the SDK function
        self.controller.start_site_device_synthetic_test(site_id, device_id, body)

        # Test response code
        assert self.response_catcher.response.status_code == 200

    # Get Synthetic Testing Status
    def test_get_site_synthetic_test_status(self):
        # Parameters for the API call
        site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

        # Perform the API call through the SDK function
        result = self.controller.get_site_synthetic_test_status(site_id)

        # Test response code
        assert self.response_catcher.response.status_code == 200

        # Test headers
        expected_headers = {}
        expected_headers['content-type'] = 'application/json'

        assert ComparisonHelper.match_headers(expected_headers, self.response_catcher.response.headers)


    # Trigger Synthetic Testing
    def test_trigger_site_synthetic_test(self):
        # Parameters for the API call
        site_id = '000000ab-00ab-00ab-00ab-0000000000ab'
        body = APIHelper.json_deserialize('{"email":"john@abc.com"}', ApiV1SitesSyntheticTestRequest.from_dictionary)

        # Perform the API call through the SDK function
        result = self.controller.trigger_site_synthetic_test(site_id, body)

        # Test response code
        assert self.response_catcher.response.status_code == 200

        # Test headers
        expected_headers = {}
        expected_headers['content-type'] = 'application/json'

        assert ComparisonHelper.match_headers(expected_headers, self.response_catcher.response.headers)

        
        # Test whether the captured response is as we expected
        assert result is not None
        expected_body = APIHelper.json_deserialize('{"email":"john@abc.com","id":"68b329da-9893-e340-99c7-d8ad5cb9c940'
            '"}')
        received_body = APIHelper.json_deserialize(self.response_catcher.response.text)
        assert ComparisonHelper.match_body(expected_body, received_body)

