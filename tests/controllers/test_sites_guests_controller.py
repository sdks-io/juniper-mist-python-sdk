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
from mistapi.models.guest import Guest


class SitesGuestsControllerTests(ControllerTestBase):

    @classmethod
    def setUpClass(cls):
        super(SitesGuestsControllerTests, cls).setUpClass()
        cls.controller = cls.client.sites_guests
        cls.response_catcher = cls.controller.http_call_back

    # Get List of Site Guest Authorizations
    def test_list_site_all_guest_authorizations(self):
        # Parameters for the API call
        site_id = '000000ab-00ab-00ab-00ab-0000000000ab'
        wlan_id = None

        # Perform the API call through the SDK function
        result = self.controller.list_site_all_guest_authorizations(site_id, wlan_id)

        # Test response code
        assert self.response_catcher.response.status_code == 200

        # Test headers
        expected_headers = {}
        expected_headers['content-type'] = 'application/json'

        assert ComparisonHelper.match_headers(expected_headers, self.response_catcher.response.headers)

        
        # Test whether the captured response is as we expected
        assert result is not None
        expected_body = APIHelper.json_deserialize('[{"authorized":true,"authorized_expiring_time":0,"authorized_time"'
            ':0,"company":"string","email":"user@example.com","field1":"string"'
            ',"field2":"string","field3":"string","field4":"string","mac":"stri'
            'ng","minutes":0,"name":"string"}]')
        received_body = APIHelper.json_deserialize(self.response_catcher.response.text)
        assert ComparisonHelper.match_body(expected_body, received_body)

    # Count Authorized Guest
    def test_count_site_guest_authorizations(self):
        # Parameters for the API call
        site_id = '000000ab-00ab-00ab-00ab-0000000000ab'
        distinct = 'auth_method'
        page = 1
        limit = 100
        start = 0
        end = 0
        duration = '1d'

        # Perform the API call through the SDK function
        result = self.controller.count_site_guest_authorizations(site_id, distinct, page, limit, start, end, duration)

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

    # Search Authorized Guest
    def test_search_site_guest_authorization(self):
        # Parameters for the API call
        site_id = '000000ab-00ab-00ab-00ab-0000000000ab'
        wlan_id = '00000000-0000-0000-0000-000000000000'
        auth_method = None
        ssid = None
        limit = 100
        start = 0
        end = 0
        duration = '1d'

        # Perform the API call through the SDK function
        result = self.controller.search_site_guest_authorization(site_id, wlan_id, auth_method, ssid, limit, start, end, duration)

        # Test response code
        assert self.response_catcher.response.status_code == 200

        # Test headers
        expected_headers = {}
        expected_headers['content-type'] = 'application/json'

        assert ComparisonHelper.match_headers(expected_headers, self.response_catcher.response.headers)

        
        # Test whether the captured response is as we expected
        assert result is not None
        expected_body = APIHelper.json_deserialize('{"end":1531862583,"limit":2,"next":"/api/v1/sites/8aaba0aa-09cc-44'
            'bd-9709-33b98040550c/guests/search?wlan_id=88ffe630-95b8-11e8-b294'
            '-346895ed1b7d&end=1531855849.000&limit=2&start=1531776183.0","resu'
            'lts":[{"ap":"5c5b350e0001","auth_method":"passphrase","authorized_'
            'expiring_time":1531810258.1862731,"authorized_time":1531782218,"co'
            'mpany":"mistsystems","email":"user@mistsys.com","name":"john","ssi'
            'd":"openNet","timestamp":1531782218},{"ap":"5c5b350e0001","auth_me'
            'thod":"facebook","authorized_expiring_time":1531810821.145,"author'
            'ized_time":1531782632,"company":"xyz inc.","email":"cool_user@yaho'
            'o.com","name":"John White","ssid":"openNet","timestamp":1531782632'
            '}],"start":1531776183,"total":14}')
        received_body = APIHelper.json_deserialize(self.response_catcher.response.text)
        assert ComparisonHelper.match_body(expected_body, received_body)

    # Delete Guest Authorization
    def test_delete_site_guest_authorization(self):
        # Parameters for the API call
        site_id = '000000ab-00ab-00ab-00ab-0000000000ab'
        guest_mac = '0000000000ab'

        # Perform the API call through the SDK function
        result = self.controller.delete_site_guest_authorization(site_id, guest_mac)

        # Test response code
        assert self.response_catcher.response.status_code == 200

        # Test headers
        expected_headers = {}
        expected_headers['content-type'] = 'application/json'

        assert ComparisonHelper.match_headers(expected_headers, self.response_catcher.response.headers)


    # Get Guest Authorization
    def test_get_site_guest_authorization(self):
        # Parameters for the API call
        site_id = '000000ab-00ab-00ab-00ab-0000000000ab'
        guest_mac = '0000000000ab'

        # Perform the API call through the SDK function
        result = self.controller.get_site_guest_authorization(site_id, guest_mac)

        # Test response code
        assert self.response_catcher.response.status_code == 200

        # Test headers
        expected_headers = {}
        expected_headers['content-type'] = 'application/json'

        assert ComparisonHelper.match_headers(expected_headers, self.response_catcher.response.headers)

        
        # Test whether the captured response is as we expected
        assert result is not None
        expected_body = APIHelper.json_deserialize('{"authorized":true,"authorized_expiring_time":0,"authorized_time":'
            '0,"company":"string","email":"user@example.com","field1":"string",'
            '"field2":"string","field3":"string","field4":"string","mac":"strin'
            'g","minutes":0,"name":"string"}')
        received_body = APIHelper.json_deserialize(self.response_catcher.response.text)
        assert ComparisonHelper.match_body(expected_body, received_body)

    # Update Guest Authorization  
    def test_update_site_guest_authorization(self):
        # Parameters for the API call
        site_id = '000000ab-00ab-00ab-00ab-0000000000ab'
        guest_mac = '0000000000ab'
        body = None

        # Perform the API call through the SDK function
        result = self.controller.update_site_guest_authorization(site_id, guest_mac, body)

        # Test response code
        assert self.response_catcher.response.status_code == 200

        # Test headers
        expected_headers = {}
        expected_headers['content-type'] = 'application/json'

        assert ComparisonHelper.match_headers(expected_headers, self.response_catcher.response.headers)

        
        # Test whether the captured response is as we expected
        assert result is not None
        expected_body = APIHelper.json_deserialize('{"authorized":true,"authorized_expiring_time":0,"authorized_time":'
            '0,"company":"string","email":"user@example.com","field1":"string",'
            '"field2":"string","field3":"string","field4":"string","mac":"strin'
            'g","minutes":0,"name":"string"}')
        received_body = APIHelper.json_deserialize(self.response_catcher.response.text)
        assert ComparisonHelper.match_body(expected_body, received_body)

