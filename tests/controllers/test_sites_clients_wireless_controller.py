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


class SitesClientsWirelessControllerTests(ControllerTestBase):

    @classmethod
    def setUpClass(cls):
        super(SitesClientsWirelessControllerTests, cls).setUpClass()
        cls.controller = cls.client.sites_clients_wireless
        cls.response_catcher = cls.controller.http_call_back

    # Count by Distinct Attributes of Clients
    def test_count_site_wireless_clients(self):
        # Parameters for the API call
        site_id = '000000ab-00ab-00ab-00ab-0000000000ab'
        distinct = 'device'
        ssid = None
        ap = None
        ip_address = '192.168.1.1'
        vlan = None
        hostname = None
        os = None
        model = None
        device = None
        page = 1
        limit = 100
        start = 0
        end = 0
        duration = '1d'

        # Perform the API call through the SDK function
        result = self.controller.count_site_wireless_clients(site_id, distinct, ssid, ap, ip_address, vlan, hostname, os, model, device, page, limit, start, end, duration)

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

    # To unauthorize multiple clients
    def test_disconnect_site_multiple_clients(self):
        # Parameters for the API call
        site_id = '000000ab-00ab-00ab-00ab-0000000000ab'
        body = APIHelper.json_deserialize('["683b679ac024"]')

        # Perform the API call through the SDK function
        result = self.controller.disconnect_site_multiple_clients(site_id, body)

        # Test response code
        assert self.response_catcher.response.status_code == 200

        # Test headers
        expected_headers = {}
        expected_headers['content-type'] = 'application/json'

        assert ComparisonHelper.match_headers(expected_headers, self.response_catcher.response.headers)


    # Count by Distinct Attributes of Client-Events
    def test_count_site_wireless_clients_events(self):
        # Parameters for the API call
        site_id = '000000ab-00ab-00ab-00ab-0000000000ab'
        distinct = 'type'
        mtype = None
        reason_code = None
        ssid = None
        ap = None
        proto = None
        band = None
        wlan_id = None
        page = 1
        limit = 100
        start = 0
        end = 0
        duration = '1d'

        # Perform the API call through the SDK function
        result = self.controller.count_site_wireless_clients_events(site_id, distinct, mtype, reason_code, ssid, ap, proto, band, wlan_id, page, limit, start, end, duration)

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

    # Get Site Clients Events
    def test_search_site_wireless_clients_events(self):
        # Parameters for the API call
        site_id = '000000ab-00ab-00ab-00ab-0000000000ab'
        mtype = None
        reason_code = None
        ssid = None
        ap = None
        proto = None
        band = None
        wlan_id = None
        limit = 100
        start = 0
        end = 0
        duration = '1d'

        # Perform the API call through the SDK function
        result = self.controller.search_site_wireless_clients_events(site_id, mtype, reason_code, ssid, ap, proto, band, wlan_id, limit, start, end, duration)

        # Test response code
        assert self.response_catcher.response.status_code == 200

        # Test headers
        expected_headers = {}
        expected_headers['content-type'] = 'application/json'

        assert ComparisonHelper.match_headers(expected_headers, self.response_catcher.response.headers)

        
        # Test whether the captured response is as we expected
        assert result is not None
        expected_body = APIHelper.json_deserialize('{"end":0,"limit":0,"results":[{"ap":"string","band":"24","bssid":"'
            'string","channel":0,"proto":"a","ssid":"string","text":"string","t'
            'imestamp":0,"type":"string","type_code":0,"wlan_id":"b069b358-4c97'
            '-5319-1f8c-7c5ca64d6ab1"}],"start":0,"total":0}')
        received_body = APIHelper.json_deserialize(self.response_catcher.response.text)
        assert ComparisonHelper.match_body(expected_body, received_body)

    # Search Wireless Clients
    #
    #**NOTE**: fuzzy logic can be used with ‘*’, supported filters: mac, hostname, device, os, model. E.g. /clients/search?device=Mac*&hostname=jerry
    def test_search_site_wireless_clients(self):
        # Parameters for the API call
        site_id = '000000ab-00ab-00ab-00ab-0000000000ab'
        mac = None
        ip_address = '192.168.1.1'
        hostname = None
        device = None
        os = None
        model = None
        ap = None
        ssid = None
        text = None
        limit = 100
        start = 0
        end = 0
        duration = '1d'

        # Perform the API call through the SDK function
        result = self.controller.search_site_wireless_clients(site_id, mac, ip_address, hostname, device, os, model, ap, ssid, text, limit, start, end, duration)

        # Test response code
        assert self.response_catcher.response.status_code == 200

        # Test headers
        expected_headers = {}
        expected_headers['content-type'] = 'application/json'

        assert ComparisonHelper.match_headers(expected_headers, self.response_catcher.response.headers)

        
        # Test whether the captured response is as we expected
        assert result is not None
        expected_body = APIHelper.json_deserialize('{"end":0,"limit":0,"results":[{"ap":"string","band":"24","bssid":"'
            'string","channel":0,"proto":"a","ssid":"string","text":"string","t'
            'imestamp":0,"type":"string","type_code":0,"wlan_id":"b069b358-4c97'
            '-5319-1f8c-7c5ca64d6ab1"}],"start":0,"total":0}')
        received_body = APIHelper.json_deserialize(self.response_catcher.response.text)
        assert ComparisonHelper.match_body(expected_body, received_body)

    # Count by Distinct Attributes of Client Sessions
    def test_count_site_wireless_client_sessions(self):
        # Parameters for the API call
        site_id = '000000ab-00ab-00ab-00ab-0000000000ab'
        distinct = 'mac'
        ap = None
        band = None
        client_family = None
        client_manufacture = None
        client_model = None
        client_os = None
        ssid = None
        wlan_id = None
        page = 1
        limit = 100
        start = 0
        end = 0
        duration = '1d'

        # Perform the API call through the SDK function
        result = self.controller.count_site_wireless_client_sessions(site_id, distinct, ap, band, client_family, client_manufacture, client_model, client_os, ssid, wlan_id, page, limit, start, end, duration)

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

    # Search Client Sessions
    def test_search_site_wireless_client_sessions(self):
        # Parameters for the API call
        site_id = '000000ab-00ab-00ab-00ab-0000000000ab'
        ap = None
        band = None
        client_family = None
        client_manufacture = None
        client_model = None
        client_username = None
        client_os = None
        ssid = None
        wlan_id = None
        psk_id = '000000ab-00ab-00ab-00ab-0000000000ab'
        psk_name = None
        limit = 100
        start = 0
        end = 0
        duration = '1d'

        # Perform the API call through the SDK function
        result = self.controller.search_site_wireless_client_sessions(site_id, ap, band, client_family, client_manufacture, client_model, client_username, client_os, ssid, wlan_id, psk_id, psk_name, limit, start, end, duration)

        # Test response code
        assert self.response_catcher.response.status_code == 200

        # Test headers
        expected_headers = {}
        expected_headers['content-type'] = 'application/json'

        assert ComparisonHelper.match_headers(expected_headers, self.response_catcher.response.headers)

        
        # Test whether the captured response is as we expected
        assert result is not None
        expected_body = APIHelper.json_deserialize('{"end":1513177200,"limit":10,"results":[{"ap":"5c5b350e0262","band'
            '":"5","client_manufacture":"Apple","connect":1565208388,"disconnec'
            't":1565208448,"duration":60.09423865,"mac":"b019c66c8348","org_id"'
            ':"3139f2c2-fac6-11e5-8156-0242ac110006","site_id":"70e0f468-fc13-1'
            '1e5-85ad-0242ac110008","ssid":"Dummy WLAN 2","tags":["disassociate'
            '"],"timestamp":1565208448.662,"wlan_id":"99bb4c74-f954-4f36-b844-6'
            'b030faffabc"}],"start":1511967600,"total":100}')
        received_body = APIHelper.json_deserialize(self.response_catcher.response.text)
        assert ComparisonHelper.match_body(expected_body, received_body)

    # This unauthorize clients (if they are guest) and disconnect them. From the guest’s perspective, they will see the splash page again and go through the flow (e.g. Terms of Use) again.
    def test_unauthorize_site_multiple_clients(self):
        # Parameters for the API call
        site_id = '000000ab-00ab-00ab-00ab-0000000000ab'
        body = APIHelper.json_deserialize('["683b679ac024"]')

        # Perform the API call through the SDK function
        result = self.controller.unauthorize_site_multiple_clients(site_id, body)

        # Test response code
        assert self.response_catcher.response.status_code == 200

        # Test headers
        expected_headers = {}
        expected_headers['content-type'] = 'application/json'

        assert ComparisonHelper.match_headers(expected_headers, self.response_catcher.response.headers)


    # This disconnect a client (and it’s likely to connect back)
    def test_disconnect_site_wireless_client(self):
        # Parameters for the API call
        site_id = '000000ab-00ab-00ab-00ab-0000000000ab'
        client_mac = '0000000000ab'

        # Perform the API call through the SDK function
        result = self.controller.disconnect_site_wireless_client(site_id, client_mac)

        # Test response code
        assert self.response_catcher.response.status_code == 200

        # Test headers
        expected_headers = {}
        expected_headers['content-type'] = 'application/json'

        assert ComparisonHelper.match_headers(expected_headers, self.response_catcher.response.headers)


    # Get the list of events for a specific client
    def test_get_site_events_for_client(self):
        # Parameters for the API call
        site_id = '000000ab-00ab-00ab-00ab-0000000000ab'
        client_mac = '0000000000ab'
        mtype = None
        proto = None
        band = None
        channel = None
        wlan_id = None
        ssid = None
        start = 0
        end = 0
        page = 1
        limit = 100
        duration = '1d'

        # Perform the API call through the SDK function
        result = self.controller.get_site_events_for_client(site_id, client_mac, mtype, proto, band, channel, wlan_id, ssid, start, end, page, limit, duration)

        # Test response code
        assert self.response_catcher.response.status_code == 200

        # Test headers
        expected_headers = {}
        expected_headers['content-type'] = 'application/json'

        assert ComparisonHelper.match_headers(expected_headers, self.response_catcher.response.headers)

        
        # Test whether the captured response is as we expected
        assert result is not None
        expected_body = APIHelper.json_deserialize('{"end":1513176951,"limit":10,"results":[{"ap":"5c5b350eb31b","band'
            '":"5","bssid":"5c5b350918f1","channel":149,"proto":"ac","ssid":"Gu'
            'est","text":"Status code 0 \"Successful\" ","timestamp":1513358874'
            '.667,"type":"CLIENT_DNS_OK","type_code":15,"wlan_id":"be22bba7-8e2'
            '2-e1cf-5185-b880816fe2cf"}],"start":1512572151,"total":1}')
        received_body = APIHelper.json_deserialize(self.response_catcher.response.text)
        assert ComparisonHelper.match_body(expected_body, received_body)

    # This unauthorize a client (if it’s a guest) and disconnect it. From the guest’s perspective, s/he will see the splash page again and go through the flow (e.g. Terms of Use) again.
    def test_unauthorize_site_wireless_client(self):
        # Parameters for the API call
        site_id = '000000ab-00ab-00ab-00ab-0000000000ab'
        client_mac = '0000000000ab'

        # Perform the API call through the SDK function
        result = self.controller.unauthorize_site_wireless_client(site_id, client_mac)

        # Test response code
        assert self.response_catcher.response.status_code == 200

        # Test headers
        expected_headers = {}
        expected_headers['content-type'] = 'application/json'

        assert ComparisonHelper.match_headers(expected_headers, self.response_catcher.response.headers)


