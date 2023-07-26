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


class MspsInventoryControllerTests(ControllerTestBase):

    @classmethod
    def setUpClass(cls):
        super(MspsInventoryControllerTests, cls).setUpClass()
        cls.controller = cls.client.msps_inventory
        cls.response_catcher = cls.controller.http_call_back

    # Get Inventoy By device MAC address
    def test_get_msp_inventory_by_mac(self):
        # Parameters for the API call
        msp_id = '000000ab-00ab-00ab-00ab-0000000000ab'
        device_mac = '0000000000ab'

        # Perform the API call through the SDK function
        result = self.controller.get_msp_inventory_by_mac(msp_id, device_mac)

        # Test response code
        assert self.response_catcher.response.status_code == 200

        # Test headers
        expected_headers = {}
        expected_headers['content-type'] = 'application/json'

        assert ComparisonHelper.match_headers(expected_headers, self.response_catcher.response.headers)

        
        # Test whether the captured response is as we expected
        assert result is not None
        expected_body = APIHelper.json_deserialize('{"mac":"5c5b35000018","model":"AP200","org_id":"b069b358-4c97-5319'
            '-1f8c-7c5ca64d6ab1","serial":"FXLH2015150025","site_id":"4ac1dcf4-'
            '9d8b-7211-65c4-057819f0862b","type":"ap"}')
        received_body = APIHelper.json_deserialize(self.response_catcher.response.text)
        assert ComparisonHelper.match_body(expected_body, received_body)

