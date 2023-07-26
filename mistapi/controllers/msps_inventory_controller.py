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
from mistapi.models.api_v_1_msps_inventory_response import ApiV1MspsInventoryResponse
from mistapi.exceptions.api_exception import APIException
from mistapi.exceptions.api_v_1_msps_inventory_401_error_exception import ApiV1MspsInventory401ErrorException
from mistapi.exceptions.api_v_1_msps_inventory_403_error_exception import ApiV1MspsInventory403ErrorException
from mistapi.exceptions.api_v_1_msps_inventory_404_error_exception import ApiV1MspsInventory404ErrorException


class MspsInventoryController(BaseController):

    """A Controller to access Endpoints in the mistapi API."""
    def __init__(self, config):
        super(MspsInventoryController, self).__init__(config)

    def get_msp_inventory_by_mac(self,
                                 msp_id,
                                 device_mac):
        """Does a GET request to /api/v1/msps/{msp_id}/inventory/{device_mac}.

        Get Inventoy By device MAC address

        Args:
            msp_id (uuid|string): TODO: type description here.
            device_mac (string): TODO: type description here.

        Returns:
            ApiV1MspsInventoryResponse: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/api/v1/msps/{msp_id}/inventory/{device_mac}')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('msp_id')
                            .value(msp_id)
                            .should_encode(True))
            .template_param(Parameter()
                            .key('device_mac')
                            .value(device_mac)
                            .should_encode(True))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('global'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ApiV1MspsInventoryResponse.from_dictionary)
            .local_error('400', 'The API endpoint exists but its syntax/payload is incorrect, detail may be given', APIException)
            .local_error('401', 'Unauthorized', ApiV1MspsInventory401ErrorException)
            .local_error('403', 'Permission Denied', ApiV1MspsInventory403ErrorException)
            .local_error('404', 'Not found. The API endpoint doesn\'t exist or resource doesn\'t exist', ApiV1MspsInventory404ErrorException)
        ).execute()