# -*- coding: utf-8 -*-

"""
mistapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

from mistapi.api_helper import APIHelper
from mistapi.configuration import Server
from mistapi.controllers.base_controller import BaseController
from apimatic_core.request_builder import RequestBuilder
from apimatic_core.response_handler import ResponseHandler
from apimatic_core.types.parameter import Parameter
from mistapi.http.http_method_enum import HttpMethodEnum
from apimatic_core.authentication.multiple.single_auth import Single
from apimatic_core.authentication.multiple.and_auth_group import And
from apimatic_core.authentication.multiple.or_auth_group import Or
from mistapi.models.api_v_1_register_verify_response import ApiV1RegisterVerifyResponse
from mistapi.exceptions.api_v_1_register_verify_400_error_exception import ApiV1RegisterVerify400ErrorException
from mistapi.exceptions.api_v_1_register_verify_401_error_exception import ApiV1RegisterVerify401ErrorException
from mistapi.exceptions.api_v_1_register_verify_403_error_exception import ApiV1RegisterVerify403ErrorException
from mistapi.exceptions.api_v_1_register_verify_404_error_exception import ApiV1RegisterVerify404ErrorException


class OrgsAdminsController(BaseController):

    """A Controller to access Endpoints in the mistapi API."""
    def __init__(self, config):
        super(OrgsAdminsController, self).__init__(config)

    def verify_registration(self,
                            token):
        """Does a POST request to /api/v1/register/verify/{token}.

        Verify registration

        Args:
            token (string): TODO: type description here.

        Returns:
            ApiV1RegisterVerifyResponse: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/api/v1/register/verify/{token}')
            .http_method(HttpMethodEnum.POST)
            .template_param(Parameter()
                            .key('token')
                            .value(token)
                            .should_encode(True))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('global'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ApiV1RegisterVerifyResponse.from_dictionary)
            .local_error('400', 'Response if verification expired or already registered', ApiV1RegisterVerify400ErrorException)
            .local_error('401', 'Unauthorized', ApiV1RegisterVerify401ErrorException)
            .local_error('403', 'Permission Denied', ApiV1RegisterVerify403ErrorException)
            .local_error('404', 'Response if secret is invalid', ApiV1RegisterVerify404ErrorException)
        ).execute()