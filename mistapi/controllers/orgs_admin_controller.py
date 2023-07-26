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
from mistapi.exceptions.api_exception import APIException
from mistapi.exceptions.api_v_1_register_401_error_exception import ApiV1Register401ErrorException
from mistapi.exceptions.api_v_1_register_403_error_exception import ApiV1Register403ErrorException
from mistapi.exceptions.api_v_1_register_404_error_exception import ApiV1Register404ErrorException


class OrgsAdminController(BaseController):

    """A Controller to access Endpoints in the mistapi API."""
    def __init__(self, config):
        super(OrgsAdminController, self).__init__(config)

    def register_new_admin(self,
                           body=None):
        """Does a POST request to /api/v1/register.

        Register a new admin and his/her org
        An email will also be sent to the user with a link to
        https://manage.mist.com/verify/register?token=:token

        Args:
            body (ApiV1RegisterRequest, optional): Request Body

        Returns:
            object: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/api/v1/register')
            .http_method(HttpMethodEnum.POST)
            .header_param(Parameter()
                          .key('Content-Type')
                          .value('application/json'))
            .body_param(Parameter()
                        .value(body))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .body_serializer(APIHelper.json_serialize)
            .auth(Single('global'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .local_error('400', 'The API endpoint exists but its syntax/payload is incorrect, detail may be given', APIException)
            .local_error('401', 'Unauthorized', ApiV1Register401ErrorException)
            .local_error('403', 'Permission Denied', ApiV1Register403ErrorException)
            .local_error('404', 'Not found. The API endpoint doesn\'t exist or resource doesn\'t exist', ApiV1Register404ErrorException)
        ).execute()
