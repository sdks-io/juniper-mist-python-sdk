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


class SitesEventsControllerTests(ControllerTestBase):

    @classmethod
    def setUpClass(cls):
        super(SitesEventsControllerTests, cls).setUpClass()
        cls.controller = cls.client.sites_events
        cls.response_catcher = cls.controller.http_call_back

    # Get Roaming Events data
    def test_get_site_roaming_events(self):
        # Parameters for the API call
        site_id = '000000ab-00ab-00ab-00ab-0000000000ab'
        mtype = None
        page = 1
        limit = 100
        start = 0
        end = 0
        duration = '1d'

        # Perform the API call through the SDK function
        result = self.controller.get_site_roaming_events(site_id, mtype, page, limit, start, end, duration)

        # Test response code
        assert self.response_catcher.response.status_code == 200

        # Test headers
        expected_headers = {}
        expected_headers['content-type'] = 'application/json'

        assert ComparisonHelper.match_headers(expected_headers, self.response_catcher.response.headers)

        
        # Test whether the captured response is as we expected
        assert result is not None
        expected_body = APIHelper.json_deserialize('{"end":1501023379,"limit":2,"next":"/api/v1/sites/dca0a44b-324c-11'
            'e6-a776-0243ad110007/events/fast_roam?type=success&start=142893960'
            '0&end=1428949600&limit=200&token=AAAAEgAIAAVVJh4hF8AAAARzc2lkAH%2F'
            '%2F%2F%2F0%3D","results":[{"ap_mac":"5c5b350e040b","client_mac":"d'
            'c2b2a3fb13d","fromap":"5c5b350e0569","latency":0.1874195,"ssid":"m'
            'arvis_test","subtype":"CLIENT_AUTHENTICATED_11R","timestamp":15010'
            '00002283782}],"start":1500940800}')
        received_body = APIHelper.json_deserialize(self.response_catcher.response.text)
        assert ComparisonHelper.match_body(expected_body, received_body)

    # Get Interference Events
    def test_get_site_interference_events(self):
        # Parameters for the API call
        site_id = '000000ab-00ab-00ab-00ab-0000000000ab'
        page = 1
        limit = 100
        start = 0
        end = 0
        duration = '1d'

        # Perform the API call through the SDK function
        result = self.controller.get_site_interference_events(site_id, page, limit, start, end, duration)

        # Test response code
        assert self.response_catcher.response.status_code == 200

        # Test headers
        expected_headers = {}
        expected_headers['content-type'] = 'application/json'

        assert ComparisonHelper.match_headers(expected_headers, self.response_catcher.response.headers)

        
        # Test whether the captured response is as we expected
        assert result is not None
        expected_body = APIHelper.json_deserialize('{"end":1428954000,"limit":100,"page":1,"results":[{"ap_id":"000000'
            '00-0000-0000-1000-5c5b359e4fe0","band":5,"channel_util":0.03,"chan'
            'nels":[1,2,5],"rssi":-64,"source":"Microwave Oven","timestamp":142'
            '8939600}],"start":1428939600,"total":135}')
        received_body = APIHelper.json_deserialize(self.response_catcher.response.text)
        assert ComparisonHelper.match_body(expected_body, received_body)

    # Count System Events
    def test_count_site_system_events(self):
        # Parameters for the API call
        site_id = '000000ab-00ab-00ab-00ab-0000000000ab'
        distinct = 'type'
        page = 1
        limit = 100
        start = 0
        end = 0
        duration = '1d'

        # Perform the API call through the SDK function
        result = self.controller.count_site_system_events(site_id, distinct, page, limit, start, end, duration)

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

    # Search System Events
    def test_search_site_system_events(self):
        # Parameters for the API call
        site_id = '000000ab-00ab-00ab-00ab-0000000000ab'
        mtype = None
        limit = 100
        start = 0
        end = 0
        duration = '1d'

        # Perform the API call through the SDK function
        result = self.controller.search_site_system_events(site_id, mtype, limit, start, end, duration)

        # Test response code
        assert self.response_catcher.response.status_code == 200

        # Test headers
        expected_headers = {}
        expected_headers['content-type'] = 'application/json'

        assert ComparisonHelper.match_headers(expected_headers, self.response_catcher.response.headers)

        
        # Test whether the captured response is as we expected
        assert result is not None
        expected_body = APIHelper.json_deserialize('{"end":0,"limit":0,"next":"string","results":[{"ap":"5c5b351e13b5"'
            ',"apfw":"5c5b351e13b5","model":"BT11-WW","org_id":"4ac1dcf4-9d8b-7'
            '211-65c4-057819f0862a","site_id":"4ac1dcf4-9d8b-7211-65c4-057819f0'
            '862b","text":"Succeeding DNS query from 172.29.101.134 to 172.29.1'
            '01.7 for \"portal.mistsys.com\" on vlan 1, id 60224","timestamp":1'
            '547235620.89,"type":"CLIENT_DNS_OK"}],"start":0,"total":0}')
        received_body = APIHelper.json_deserialize(self.response_catcher.response.text)
        assert ComparisonHelper.match_body(expected_body, received_body)

