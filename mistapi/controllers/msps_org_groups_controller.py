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
from mistapi.models.orggroup import Orggroup
from mistapi.models.orggroups_search import OrggroupsSearch
from mistapi.exceptions.api_exception import APIException
from mistapi.exceptions.api_v_1_msps_orggroups_401_error_exception import ApiV1MspsOrggroups401ErrorException
from mistapi.exceptions.api_v_1_msps_orggroups_403_error_exception import ApiV1MspsOrggroups403ErrorException
from mistapi.exceptions.api_v_1_msps_orggroups_404_error_exception import ApiV1MspsOrggroups404ErrorException
from mistapi.exceptions.api_v_1_msps_search_401_error_exception import ApiV1MspsSearch401ErrorException
from mistapi.exceptions.api_v_1_msps_search_403_error_exception import ApiV1MspsSearch403ErrorException
from mistapi.exceptions.api_v_1_msps_search_404_error_exception import ApiV1MspsSearch404ErrorException


class MspsOrgGroupsController(BaseController):

    """A Controller to access Endpoints in the mistapi API."""
    def __init__(self, config):
        super(MspsOrgGroupsController, self).__init__(config)

    def list_msp_org_groups(self,
                            msp_id):
        """Does a GET request to /api/v1/msps/{msp_id}/orggroups.

        Get List of MSP Org Groups

        Args:
            msp_id (uuid|string): TODO: type description here.

        Returns:
            list of Orggroup: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/api/v1/msps/{msp_id}/orggroups')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('msp_id')
                            .value(msp_id)
                            .should_encode(True))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('global'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(Orggroup.from_dictionary)
            .local_error('400', 'The API endpoint exists but its syntax/payload is incorrect, detail may be given', APIException)
            .local_error('401', 'Unauthorized', ApiV1MspsOrggroups401ErrorException)
            .local_error('403', 'Permission Denied', ApiV1MspsOrggroups403ErrorException)
            .local_error('404', 'Not found. The API endpoint doesn\'t exist or resource doesn\'t exist', ApiV1MspsOrggroups404ErrorException)
        ).execute()

    def create_msp_org_group(self,
                             msp_id,
                             body=None):
        """Does a POST request to /api/v1/msps/{msp_id}/orggroups.

        Create MSP Org Group

        Args:
            msp_id (uuid|string): TODO: type description here.
            body (Orggroup, optional): Request Body

        Returns:
            Orggroup: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/api/v1/msps/{msp_id}/orggroups')
            .http_method(HttpMethodEnum.POST)
            .template_param(Parameter()
                            .key('msp_id')
                            .value(msp_id)
                            .should_encode(True))
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
            .deserialize_into(Orggroup.from_dictionary)
            .local_error('400', 'The API endpoint exists but its syntax/payload is incorrect, detail may be given', APIException)
            .local_error('401', 'Unauthorized', ApiV1MspsOrggroups401ErrorException)
            .local_error('403', 'Permission Denied', ApiV1MspsOrggroups403ErrorException)
            .local_error('404', 'Not found. The API endpoint doesn\'t exist or resource doesn\'t exist', ApiV1MspsOrggroups404ErrorException)
        ).execute()

    def delete_msp_org_group(self,
                             msp_id,
                             orggroup_id):
        """Does a DELETE request to /api/v1/msps/{msp_id}/orggroups/{orggroup_id}.

        Delete MSP Org Group

        Args:
            msp_id (uuid|string): TODO: type description here.
            orggroup_id (uuid|string): TODO: type description here.

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
            .path('/api/v1/msps/{msp_id}/orggroups/{orggroup_id}')
            .http_method(HttpMethodEnum.DELETE)
            .template_param(Parameter()
                            .key('msp_id')
                            .value(msp_id)
                            .should_encode(True))
            .template_param(Parameter()
                            .key('orggroup_id')
                            .value(orggroup_id)
                            .should_encode(True))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('global'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .local_error('400', 'The API endpoint exists but its syntax/payload is incorrect, detail may be given', APIException)
            .local_error('401', 'Unauthorized', ApiV1MspsOrggroups401ErrorException)
            .local_error('403', 'Permission Denied', ApiV1MspsOrggroups403ErrorException)
            .local_error('404', 'Not found. The API endpoint doesn\'t exist or resource doesn\'t exist', ApiV1MspsOrggroups404ErrorException)
        ).execute()

    def get_msp_org_group(self,
                          msp_id,
                          orggroup_id):
        """Does a GET request to /api/v1/msps/{msp_id}/orggroups/{orggroup_id}.

        Get MSP Org Group Details

        Args:
            msp_id (uuid|string): TODO: type description here.
            orggroup_id (uuid|string): TODO: type description here.

        Returns:
            Orggroup: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/api/v1/msps/{msp_id}/orggroups/{orggroup_id}')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('msp_id')
                            .value(msp_id)
                            .should_encode(True))
            .template_param(Parameter()
                            .key('orggroup_id')
                            .value(orggroup_id)
                            .should_encode(True))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('global'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(Orggroup.from_dictionary)
            .local_error('400', 'The API endpoint exists but its syntax/payload is incorrect, detail may be given', APIException)
            .local_error('401', 'Unauthorized', ApiV1MspsOrggroups401ErrorException)
            .local_error('403', 'Permission Denied', ApiV1MspsOrggroups403ErrorException)
            .local_error('404', 'Not found. The API endpoint doesn\'t exist or resource doesn\'t exist', ApiV1MspsOrggroups404ErrorException)
        ).execute()

    def update_msp_org_group(self,
                             msp_id,
                             orggroup_id,
                             body=None):
        """Does a PUT request to /api/v1/msps/{msp_id}/orggroups/{orggroup_id}.

        Update MSP Org Group

        Args:
            msp_id (uuid|string): TODO: type description here.
            orggroup_id (uuid|string): TODO: type description here.
            body (Orggroup, optional): Request Body

        Returns:
            Orggroup: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/api/v1/msps/{msp_id}/orggroups/{orggroup_id}')
            .http_method(HttpMethodEnum.PUT)
            .template_param(Parameter()
                            .key('msp_id')
                            .value(msp_id)
                            .should_encode(True))
            .template_param(Parameter()
                            .key('orggroup_id')
                            .value(orggroup_id)
                            .should_encode(True))
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
            .deserialize_into(Orggroup.from_dictionary)
            .local_error('400', 'The API endpoint exists but its syntax/payload is incorrect, detail may be given', APIException)
            .local_error('401', 'Unauthorized', ApiV1MspsOrggroups401ErrorException)
            .local_error('403', 'Permission Denied', ApiV1MspsOrggroups403ErrorException)
            .local_error('404', 'Not found. The API endpoint doesn\'t exist or resource doesn\'t exist', ApiV1MspsOrggroups404ErrorException)
        ).execute()

    def search_msp_org_group(self,
                             msp_id,
                             mtype,
                             q=None,
                             limit=100,
                             start=0,
                             end=0,
                             duration='1d'):
        """Does a GET request to /api/v1/msps/{msp_id}/search.

        Search in MSP Orgs

        Args:
            msp_id (uuid|string): TODO: type description here.
            mtype (Type45Enum): orgs
            q (string, optional): search string
            limit (int, optional): TODO: type description here. Example: 100
            start (int, optional): TODO: type description here. Example: 0
            end (int, optional): TODO: type description here. Example: 0
            duration (string, optional): For historical stats and/or logs
                where time range is needed, you can specify the time range in
                a few different ways:   * ?start=1430000000&end=1430864000
                specify the start / end   * ?end=1430864000&duration=1d
                specify end time and duration   * ?duration=1d specify
                duration, end will be now() in seconds

        Returns:
            OrggroupsSearch: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/api/v1/msps/{msp_id}/search')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('msp_id')
                            .value(msp_id)
                            .should_encode(True))
            .query_param(Parameter()
                         .key('type')
                         .value(mtype))
            .query_param(Parameter()
                         .key('q')
                         .value(q))
            .query_param(Parameter()
                         .key('limit')
                         .value(limit))
            .query_param(Parameter()
                         .key('start')
                         .value(start))
            .query_param(Parameter()
                         .key('end')
                         .value(end))
            .query_param(Parameter()
                         .key('duration')
                         .value(duration))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('global'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(OrggroupsSearch.from_dictionary)
            .local_error('400', 'The API endpoint exists but its syntax/payload is incorrect, detail may be given', APIException)
            .local_error('401', 'Unauthorized', ApiV1MspsSearch401ErrorException)
            .local_error('403', 'Permission Denied', ApiV1MspsSearch403ErrorException)
            .local_error('404', 'Not found. The API endpoint doesn\'t exist or resource doesn\'t exist', ApiV1MspsSearch404ErrorException)
        ).execute()
