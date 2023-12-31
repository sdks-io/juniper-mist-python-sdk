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


class SitesSubscriptionsControllerTests(ControllerTestBase):

    @classmethod
    def setUpClass(cls):
        super(SitesSubscriptionsControllerTests, cls).setUpClass()
        cls.controller = cls.client.sites_subscriptions
        cls.response_catcher = cls.controller.http_call_back

    # Unsubscribe to Site Alarms
    def test_unsubscribe_site_alarms(self):
        # Parameters for the API call
        site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

        # Perform the API call through the SDK function
        result = self.controller.unsubscribe_site_alarms(site_id)

        # Test response code
        assert self.response_catcher.response.status_code == 200

        # Test headers
        expected_headers = {}
        expected_headers['content-type'] = 'application/json'

        assert ComparisonHelper.match_headers(expected_headers, self.response_catcher.response.headers)


    # Subscribe to Site Alarms
    def test_subscribe_site_alarms(self):
        # Parameters for the API call
        site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

        # Perform the API call through the SDK function
        result = self.controller.subscribe_site_alarms(site_id)

        # Test response code
        assert self.response_catcher.response.status_code == 200

        # Test headers
        expected_headers = {}
        expected_headers['content-type'] = 'application/json'

        assert ComparisonHelper.match_headers(expected_headers, self.response_catcher.response.headers)


