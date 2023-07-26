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
from mistapi.models.api_v_1_sites_alarms_ack_request import ApiV1SitesAlarmsAckRequest
from mistapi.models.note import Note
from mistapi.models.api_v_1_sites_alarms_unack_request import ApiV1SitesAlarmsUnackRequest


class SitesAlarmsControllerTests(ControllerTestBase):

    @classmethod
    def setUpClass(cls):
        super(SitesAlarmsControllerTests, cls).setUpClass()
        cls.controller = cls.client.sites_alarms
        cls.response_catcher = cls.controller.http_call_back

    # Ack multiple Site Alarms
    def test_multi_ack_site_alarms(self):
        # Parameters for the API call
        site_id = '000000ab-00ab-00ab-00ab-0000000000ab'
        body = APIHelper.json_deserialize('{"alarm_ids":["ccb8c94d-ca56-4075-932f-1f2ab444ff2c","98ff4a3d-ec9'
            'b-4138-a42e-54fc3335179d"],"note":"maintenance window"}', ApiV1SitesAlarmsAckRequest.from_dictionary)

        # Perform the API call through the SDK function
        result = self.controller.multi_ack_site_alarms(site_id, body)

        # Test response code
        assert self.response_catcher.response.status_code == 200

        # Test headers
        expected_headers = {}
        expected_headers['content-type'] = 'application/json'

        assert ComparisonHelper.match_headers(expected_headers, self.response_catcher.response.headers)


    # Ack all Site Alarms
    #
    #**N.B.**: Batch size for multiple alarm ack and unack has to be less or or equal to 1000.
    def test_ack_site_all_alarms(self):
        # Parameters for the API call
        site_id = '000000ab-00ab-00ab-00ab-0000000000ab'
        body = APIHelper.json_deserialize('{"note":"string"}', Note.from_dictionary)

        # Perform the API call through the SDK function
        result = self.controller.ack_site_all_alarms(site_id, body)

        # Test response code
        assert self.response_catcher.response.status_code == 200

        # Test headers
        expected_headers = {}
        expected_headers['content-type'] = 'application/json'

        assert ComparisonHelper.match_headers(expected_headers, self.response_catcher.response.headers)


    # Count Site Alarms
    def test_count_site_alarms(self):
        # Parameters for the API call
        site_id = '000000ab-00ab-00ab-00ab-0000000000ab'
        distinct = 'type'
        ack_admin_name = None
        acked = None
        mtype = None
        severity = None
        group = None
        page = 1
        limit = 100
        start = 0
        end = 0
        duration = '1d'

        # Perform the API call through the SDK function
        result = self.controller.count_site_alarms(site_id, distinct, ack_admin_name, acked, mtype, severity, group, page, limit, start, end, duration)

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

    # Search Site Alarms
    def test_search_site_alarms(self):
        # Parameters for the API call
        site_id = '000000ab-00ab-00ab-00ab-0000000000ab'
        mtype = None
        ack_admin_name = None
        acked = None
        severity = None
        group = None
        limit = 100
        start = 0
        end = 0
        duration = '1d'

        # Perform the API call through the SDK function
        result = self.controller.search_site_alarms(site_id, mtype, ack_admin_name, acked, severity, group, limit, start, end, duration)

        # Test response code
        assert self.response_catcher.response.status_code == 200

        # Test headers
        expected_headers = {}
        expected_headers['content-type'] = 'application/json'

        assert ComparisonHelper.match_headers(expected_headers, self.response_catcher.response.headers)

        
        # Test whether the captured response is as we expected
        assert result is not None
        expected_body = APIHelper.json_deserialize('{"end":0,"limit":0,"next":"string","results":[{"ack_admin_id":"660'
            '3c94c-eaf9-4014-9edf-b9f8eed6b183","ack_admin_name":"string","acke'
            'd":true,"acked_time":0,"aps":["string"],"bssids":["string"],"count'
            '":0,"gateways":["string"],"group":"string","hostnames":["string"],'
            '"id":"483f6eca-6276-4993-bfeb-56cbbbba6f08","last_seen":0,"note":"'
            'string","org_id":"a40f5d1f-d889-42e9-94ea-b9b33585fc6b","severity"'
            ':"string","site_id":"72771e6a-6f5e-4de4-a5b9-1266c4197811","ssids"'
            ':["string"],"switches":["string"],"timestamp":0,"type":"string"}],'
            '"start":0,"total":0}')
        received_body = APIHelper.json_deserialize(self.response_catcher.response.text)
        assert ComparisonHelper.match_body(expected_body, received_body)

    # Unack multiple Site Alarms
    def test_multi_unack_site_alarms(self):
        # Parameters for the API call
        site_id = '000000ab-00ab-00ab-00ab-0000000000ab'
        body = APIHelper.json_deserialize('{"alarm_ids":["ccb8c94d-ca56-4075-932f-1f2ab444ff2c","98ff4a3d-ec9'
            'b-4138-a42e-54fc3335179d"],"note":"maintenance window"}', ApiV1SitesAlarmsUnackRequest.from_dictionary)

        # Perform the API call through the SDK function
        result = self.controller.multi_unack_site_alarms(site_id, body)

        # Test response code
        assert self.response_catcher.response.status_code == 200

        # Test headers
        expected_headers = {}
        expected_headers['content-type'] = 'application/json'

        assert ComparisonHelper.match_headers(expected_headers, self.response_catcher.response.headers)


    # Unack all Site Alarms
    #
    #**N.B.**: Batch size for multiple alarm ack and unack has to be less or or equal to 1000.
    def test_unack_site_all_arlarms(self):
        # Parameters for the API call
        site_id = '000000ab-00ab-00ab-00ab-0000000000ab'
        body = APIHelper.json_deserialize('{"note":"maintenance window"}', Note.from_dictionary)

        # Perform the API call through the SDK function
        result = self.controller.unack_site_all_arlarms(site_id, body)

        # Test response code
        assert self.response_catcher.response.status_code == 200

        # Test headers
        expected_headers = {}
        expected_headers['content-type'] = 'application/json'

        assert ComparisonHelper.match_headers(expected_headers, self.response_catcher.response.headers)


    # Ack Site Alarm
    def test_ack_site_alarm(self):
        # Parameters for the API call
        site_id = '000000ab-00ab-00ab-00ab-0000000000ab'
        alarm_id = '000000ab-00ab-00ab-00ab-0000000000ab'
        body = APIHelper.json_deserialize('{"note":"maintenance window"}', Note.from_dictionary)

        # Perform the API call through the SDK function
        result = self.controller.ack_site_alarm(site_id, alarm_id, body)

        # Test response code
        assert self.response_catcher.response.status_code == 200

        # Test headers
        expected_headers = {}
        expected_headers['content-type'] = 'application/json'

        assert ComparisonHelper.match_headers(expected_headers, self.response_catcher.response.headers)


    # Unack Site Alarm
    def test_unack_site_alarm(self):
        # Parameters for the API call
        site_id = '000000ab-00ab-00ab-00ab-0000000000ab'
        alarm_id = '000000ab-00ab-00ab-00ab-0000000000ab'
        body = APIHelper.json_deserialize('{"note":"maintenance window"}', Note.from_dictionary)

        # Perform the API call through the SDK function
        result = self.controller.unack_site_alarm(site_id, alarm_id, body)

        # Test response code
        assert self.response_catcher.response.status_code == 200

        # Test headers
        expected_headers = {}
        expected_headers['content-type'] = 'application/json'

        assert ComparisonHelper.match_headers(expected_headers, self.response_catcher.response.headers)


