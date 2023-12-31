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
from mistapi.models.msp import Msp


class MspsControllerTests(ControllerTestBase):

    @classmethod
    def setUpClass(cls):
        super(MspsControllerTests, cls).setUpClass()
        cls.controller = cls.client.msps
        cls.response_catcher = cls.controller.http_call_back

    # Create MSP account
    def test_create_msp(self):
        # Parameters for the API call
        body = APIHelper.json_deserialize('{"name":"MSP"}', Msp.from_dictionary)

        # Perform the API call through the SDK function
        result = self.controller.create_msp(body)

        # Test response code
        assert self.response_catcher.response.status_code == 200

        # Test headers
        expected_headers = {}
        expected_headers['content-type'] = 'application/json'

        assert ComparisonHelper.match_headers(expected_headers, self.response_catcher.response.headers)

        
        # Test whether the captured response is as we expected
        assert result is not None
        expected_body = APIHelper.json_deserialize('{"created_time":0,"id":"b069b358-4c97-5319-1f8c-7c5ca64d6ab1","mod'
            'ified_time":0,"name":"string"}')
        received_body = APIHelper.json_deserialize(self.response_catcher.response.text)
        assert ComparisonHelper.match_body(expected_body, received_body)

    # Deleting MSP removes the MSP and OrgGroup under the MSP as well as all privileges associated with them. It does not remove any Org or Admins
    def test_delete_msp(self):
        # Parameters for the API call
        msp_id = '000000ab-00ab-00ab-00ab-0000000000ab'

        # Perform the API call through the SDK function
        result = self.controller.delete_msp(msp_id)

        # Test response code
        assert self.response_catcher.response.status_code == 200

        # Test headers
        expected_headers = {}
        expected_headers['content-type'] = 'application/json'

        assert ComparisonHelper.match_headers(expected_headers, self.response_catcher.response.headers)


    # Get MSP Detail
    def test_get_msp_details(self):
        # Parameters for the API call
        msp_id = '000000ab-00ab-00ab-00ab-0000000000ab'

        # Perform the API call through the SDK function
        result = self.controller.get_msp_details(msp_id)

        # Test response code
        assert self.response_catcher.response.status_code == 200

        # Test headers
        expected_headers = {}
        expected_headers['content-type'] = 'application/json'

        assert ComparisonHelper.match_headers(expected_headers, self.response_catcher.response.headers)

        
        # Test whether the captured response is as we expected
        assert result is not None
        expected_body = APIHelper.json_deserialize('{"created_time":0,"id":"b069b358-4c97-5319-1f8c-7c5ca64d6ab1","mod'
            'ified_time":0,"name":"string"}')
        received_body = APIHelper.json_deserialize(self.response_catcher.response.text)
        assert ComparisonHelper.match_body(expected_body, received_body)

    # Update MSP
    def test_update_msp(self):
        # Parameters for the API call
        msp_id = '000000ab-00ab-00ab-00ab-0000000000ab'
        body = APIHelper.json_deserialize('{"name":"MSP"}', Msp.from_dictionary)

        # Perform the API call through the SDK function
        result = self.controller.update_msp(msp_id, body)

        # Test response code
        assert self.response_catcher.response.status_code == 200

        # Test headers
        expected_headers = {}
        expected_headers['content-type'] = 'application/json'

        assert ComparisonHelper.match_headers(expected_headers, self.response_catcher.response.headers)

        
        # Test whether the captured response is as we expected
        assert result is not None
        expected_body = APIHelper.json_deserialize('{"created_time":0,"id":"b069b358-4c97-5319-1f8c-7c5ca64d6ab1","mod'
            'ified_time":0,"name":"string"}')
        received_body = APIHelper.json_deserialize(self.response_catcher.response.text)
        assert ComparisonHelper.match_body(expected_body, received_body)

