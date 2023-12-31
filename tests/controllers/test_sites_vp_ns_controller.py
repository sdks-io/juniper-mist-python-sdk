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


class SitesVPNsControllerTests(ControllerTestBase):

    @classmethod
    def setUpClass(cls):
        super(SitesVPNsControllerTests, cls).setUpClass()
        cls.controller = cls.client.sites_vp_ns
        cls.response_catcher = cls.controller.http_call_back

    # VPN object represents an overlay network where gateways can participate in and optionally expose routes to.
    def test_list_site_vpns_derived(self):
        # Parameters for the API call
        site_id = '000000ab-00ab-00ab-00ab-0000000000ab'
        resolve = False

        # Perform the API call through the SDK function
        result = self.controller.list_site_vpns_derived(site_id, resolve)

        # Test response code
        assert self.response_catcher.response.status_code == 200

        # Test headers
        expected_headers = {}
        expected_headers['content-type'] = 'application/json'

        assert ComparisonHelper.match_headers(expected_headers, self.response_catcher.response.headers)

        
        # Test whether the captured response is as we expected
        assert result is not None
        expected_body = APIHelper.json_deserialize('[{"name":"string","paths":{"property1":{"bfd_profile":"broadband",'
            '"ip":"string"},"property2":{"bfd_profile":"lte","ip":"string"}}}]')
        received_body = APIHelper.json_deserialize(self.response_catcher.response.text)
        assert ComparisonHelper.match_body(expected_body, received_body)

