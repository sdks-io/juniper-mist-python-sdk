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


class SitesCallsControllerTests(ControllerTestBase):

    @classmethod
    def setUpClass(cls):
        super(SitesCallsControllerTests, cls).setUpClass()
        cls.controller = cls.client.sites_calls
        cls.response_catcher = cls.controller.http_call_back

    # Count Site Call Events
    def test_count_site_call_events(self):
        # Parameters for the API call
        site_id = '000000ab-00ab-00ab-00ab-0000000000ab'
        distinct = None

        # Perform the API call through the SDK function
        result = self.controller.count_site_call_events(site_id, distinct)

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

    # Search Site Call Events
    def test_search_site_call_events(self):
        # Parameters for the API call
        site_id = '000000ab-00ab-00ab-00ab-0000000000ab'
        mtype = None
        ap = None
        mac = None
        app = None

        # Perform the API call through the SDK function
        result = self.controller.search_site_call_events(site_id, mtype, ap, mac, app)

        # Test response code
        assert self.response_catcher.response.status_code == 200

        # Test headers
        expected_headers = {}
        expected_headers['content-type'] = 'application/json'

        assert ComparisonHelper.match_headers(expected_headers, self.response_catcher.response.headers)

        
        # Test whether the captured response is as we expected
        assert result is not None
        expected_body = APIHelper.json_deserialize('{"end":1674819324,"limit":10,"results":[{"app":"zoom","audio_quali'
            'ty":"good","meeting_id":"87609329850","org_id":"2818e386-8dec-2562'
            '-9ede-5b8a0fbbdc71","reason":"Host ended the meeting.","screen_sha'
            're_quality":"good","site_id":"1916d52a-4a90-11e5-8b45-1258369c38a9'
            '","timestamp":1674199827,"type":"CLIENT_LEFT_CALL","video_quality"'
            ':"good","wcid":"82c70a73-e2e1-42f9-6da0-97db44b7b9ad"},{"app":"zoo'
            'm","meeting_id":"87609329850","org_id":"2818e386-8dec-2562-9ede-5b'
            '8a0fbbdc71","reason":"Network connection error.","site_id":"1916d5'
            '2a-4a90-11e5-8b45-1258369c38a9","timestamp":1674199827,"type":"CLI'
            'ENT_DISCONNECTED_FROM_CALL","wcid":"82c70a73-e2e1-42f9-6da0-97db44'
            'b7b9ad"},{"app":"zoom","meeting_id":"87609329850","org_id":"2818e3'
            '86-8dec-2562-9ede-5b8a0fbbdc71","site_id":"1916d52a-4a90-11e5-8b45'
            '-1258369c38a9","timestamp":1674199827,"type":"CLIENTS_JOINED_CALL"'
            ',"wcid":"82c70a73-e2e1-42f9-6da0-97db44b7b9ad"}],"start":167415300'
            '0,"total":3}')
        received_body = APIHelper.json_deserialize(self.response_catcher.response.text)
        assert ComparisonHelper.match_body(expected_body, received_body)

    # Count by Distinct Attributes of Calls
    def test_count_site_calls(self):
        # Parameters for the API call
        site_id = '000000ab-00ab-00ab-00ab-0000000000ab'
        distrinct = 'mac'
        rating = None
        app = None
        start = None
        end = None

        # Perform the API call through the SDK function
        result = self.controller.count_site_calls(site_id, distrinct, rating, app, start, end)

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

    # Search Calls
    def test_search_site_calls(self):
        # Parameters for the API call
        site_id = '000000ab-00ab-00ab-00ab-0000000000ab'
        mac = None
        app = 'zoom'
        limit = 100
        start = 0
        end = 0
        duration = '1d'

        # Perform the API call through the SDK function
        result = self.controller.search_site_calls(site_id, mac, app, limit, start, end, duration)

        # Test response code
        assert self.response_catcher.response.status_code == 200

        # Test headers
        expected_headers = {}
        expected_headers['content-type'] = 'application/json'

        assert ComparisonHelper.match_headers(expected_headers, self.response_catcher.response.headers)

