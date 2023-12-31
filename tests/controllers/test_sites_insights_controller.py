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


class SitesInsightsControllerTests(ControllerTestBase):

    @classmethod
    def setUpClass(cls):
        super(SitesInsightsControllerTests, cls).setUpClass()
        cls.controller = cls.client.sites_insights
        cls.response_catcher = cls.controller.http_call_back

    # Get List of Site Rogue/Neighbor APs
    def test_list_site_rogue_a_ps(self):
        # Parameters for the API call
        site_id = '000000ab-00ab-00ab-00ab-0000000000ab'
        mtype = None
        limit = 100
        start = 0
        end = 0
        duration = '1d'
        interval = '10m'

        # Perform the API call through the SDK function
        result = self.controller.list_site_rogue_a_ps(site_id, mtype, limit, start, end, duration, interval)

        # Test response code
        assert self.response_catcher.response.status_code == 200

        # Test headers
        expected_headers = {}
        expected_headers['content-type'] = 'application/json'

        assert ComparisonHelper.match_headers(expected_headers, self.response_catcher.response.headers)

        
        # Test whether the captured response is as we expected
        assert result is not None
        expected_body = APIHelper.json_deserialize('{"end":1428954000,"limit":100,"next":"/api/v1/sites/a3eda150-ab3f-'
            '11e4-aa18-13e21dd250cc/rogues?start=1498482000&end=1498485600&limi'
            't=10&interval=1h&type=others","results":[{"ap_mac":"5c5b350e021c",'
            '"avg_rssi":-72,"bssid":"d8-97-ba-76-b5-aa","channel":"11","num_aps'
            '":4,"ssid":"xfinitywifi","times_heard":8}],"start":1428939600}')
        received_body = APIHelper.json_deserialize(self.response_catcher.response.text)
        assert ComparisonHelper.match_body(expected_body, received_body)

    # Get List of Site Rogue Clients
    def test_list_site_rogue_clients(self):
        # Parameters for the API call
        site_id = '000000ab-00ab-00ab-00ab-0000000000ab'
        limit = 100
        start = 0
        end = 0
        duration = '1d'
        interval = '10m'

        # Perform the API call through the SDK function
        result = self.controller.list_site_rogue_clients(site_id, limit, start, end, duration, interval)

        # Test response code
        assert self.response_catcher.response.status_code == 200

        # Test headers
        expected_headers = {}
        expected_headers['content-type'] = 'application/json'

        assert ComparisonHelper.match_headers(expected_headers, self.response_catcher.response.headers)

        
        # Test whether the captured response is as we expected
        assert result is not None
        expected_body = APIHelper.json_deserialize('{"end":1428954000,"limit":100,"next":"/api/v1/sites/a3eda150-ab3f-'
            '11e4-aa18-13e21dd250cc/rogues/clients?start=1498482000&end=1498485'
            '600&limit=10&interval=1h","results":[{"annotation":"whitelist","ap'
            '_mac":"5c-5b-35-0e-02-1c","avg_rssi":-63.9,"band":"5","bssid":"d8-'
            '97-ba-76-b5-aa","client_mac":"34-f8-32-13-57-c2","num_aps":2}],"st'
            'art":1428939600}')
        received_body = APIHelper.json_deserialize(self.response_catcher.response.text)
        assert ComparisonHelper.match_body(expected_body, received_body)

