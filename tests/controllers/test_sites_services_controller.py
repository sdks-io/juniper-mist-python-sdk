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


class SitesServicesControllerTests(ControllerTestBase):

    @classmethod
    def setUpClass(cls):
        super(SitesServicesControllerTests, cls).setUpClass()
        cls.controller = cls.client.sites_services
        cls.response_catcher = cls.controller.http_call_back

    # Retrieves the list of Services available for the Site
    def test_list_site_services_derived(self):
        # Parameters for the API call
        site_id = '000000ab-00ab-00ab-00ab-0000000000ab'
        resolve = False

        # Perform the API call through the SDK function
        result = self.controller.list_site_services_derived(site_id, resolve)

        # Test response code
        assert self.response_catcher.response.status_code == 200

        # Test headers
        expected_headers = {}
        expected_headers['content-type'] = 'application/json'

        assert ComparisonHelper.match_headers(expected_headers, self.response_catcher.response.headers)

        
        # Test whether the captured response is as we expected
        assert result is not None
        expected_body = APIHelper.json_deserialize('[{"addresses":["string"],"apps":["string"],"dscp_class":"string","'
            'hostnames":["string"],"max_jitter":0,"max_latency":"string","max_l'
            'oss":0,"name":"string","specs":[{"port_range":"0","protocol":"any"'
            '}],"traffic_class":"best_effort","traffic_type":"default","type":"'
            'custom","vpn_name":"addresses"}]')
        received_body = APIHelper.json_deserialize(self.response_catcher.response.text)
        assert ComparisonHelper.match_body(expected_body, received_body)
