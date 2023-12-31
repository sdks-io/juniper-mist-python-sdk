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


class SitesApplicationsControllerTests(ControllerTestBase):

    @classmethod
    def setUpClass(cls):
        super(SitesApplicationsControllerTests, cls).setUpClass()
        cls.controller = cls.client.sites_applications
        cls.response_catcher = cls.controller.http_call_back

    # Get List of Site Applications
    def test_list_site_apps(self):
        # Parameters for the API call
        site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

        # Perform the API call through the SDK function
        result = self.controller.list_site_apps(site_id)

        # Test response code
        assert self.response_catcher.response.status_code == 200

        # Test headers
        expected_headers = {}
        expected_headers['content-type'] = 'application/json'

        assert ComparisonHelper.match_headers(expected_headers, self.response_catcher.response.headers)

        
        # Test whether the captured response is as we expected
        assert result is not None
        expected_body = APIHelper.json_deserialize('[{"group":"string","key":"string","name":"string"}]')
        received_body = APIHelper.json_deserialize(self.response_catcher.response.text)
        assert ComparisonHelper.match_body(expected_body, received_body)

    # Count by Distinct Attributes of Applications
    def test_count_site_apps(self):
        # Parameters for the API call
        site_id = '000000ab-00ab-00ab-00ab-0000000000ab'
        distinct = None
        device_mac = None
        app = None
        wired = None

        # Perform the API call through the SDK function
        result = self.controller.count_site_apps(site_id, distinct, device_mac, app, wired)

        # Test response code
        assert self.response_catcher.response.status_code == 200

        # Test headers
        expected_headers = {}
        expected_headers['content-type'] = 'application/json'

        assert ComparisonHelper.match_headers(expected_headers, self.response_catcher.response.headers)

        
        # Test whether the captured response is as we expected
        assert result is not None
        expected_body = APIHelper.json_deserialize('{"distinct":"string","end":0,"limit":0,"percentage":0,"results":[{'
            '"count":0,"property":"string"}],"start":0,"total":0}')
        received_body = APIHelper.json_deserialize(self.response_catcher.response.text)
        assert ComparisonHelper.match_body(expected_body, received_body)

