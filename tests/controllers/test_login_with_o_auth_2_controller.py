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
from mistapi.models.api_v_1_login_two_factor_request import ApiV1LoginTwoFactorRequest


class LoginWithOAuth2ControllerTests(ControllerTestBase):

    @classmethod
    def setUpClass(cls):
        super(LoginWithOAuth2ControllerTests, cls).setUpClass()
        cls.controller = cls.client.login_with_o_auth_2
        cls.response_catcher = cls.controller.http_call_back

    # Send 2FA Code
    def test_two_factor(self):
        # Parameters for the API call
        body = APIHelper.json_deserialize('{"two_factor":"123456"}', ApiV1LoginTwoFactorRequest.from_dictionary)

        # Perform the API call through the SDK function
        result = self.controller.two_factor(body)

        # Test response code
        assert self.response_catcher.response.status_code == 200

        # Test headers
        expected_headers = {}
        expected_headers['content-type'] = 'application/json'

        assert ComparisonHelper.match_headers(expected_headers, self.response_catcher.response.headers)


