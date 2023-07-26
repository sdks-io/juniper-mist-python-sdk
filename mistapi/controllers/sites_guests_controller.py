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
from mistapi.models.guest import Guest
from mistapi.models.count import Count
from mistapi.models.guests_search import GuestsSearch
from mistapi.exceptions.api_exception import APIException
from mistapi.exceptions.api_v_1_sites_guests_401_error_exception import ApiV1SitesGuests401ErrorException
from mistapi.exceptions.api_v_1_sites_guests_403_error_exception import ApiV1SitesGuests403ErrorException
from mistapi.exceptions.api_v_1_sites_guests_404_error_exception import ApiV1SitesGuests404ErrorException
from mistapi.exceptions.api_v_1_sites_guests_count_401_error_exception import ApiV1SitesGuestsCount401ErrorException
from mistapi.exceptions.api_v_1_sites_guests_count_403_error_exception import ApiV1SitesGuestsCount403ErrorException
from mistapi.exceptions.api_v_1_sites_guests_count_404_error_exception import ApiV1SitesGuestsCount404ErrorException
from mistapi.exceptions.api_v_1_sites_guests_search_401_error_exception import ApiV1SitesGuestsSearch401ErrorException
from mistapi.exceptions.api_v_1_sites_guests_search_403_error_exception import ApiV1SitesGuestsSearch403ErrorException
from mistapi.exceptions.api_v_1_sites_guests_search_404_error_exception import ApiV1SitesGuestsSearch404ErrorException


class SitesGuestsController(BaseController):

    """A Controller to access Endpoints in the mistapi API."""
    def __init__(self, config):
        super(SitesGuestsController, self).__init__(config)

    def list_site_all_guest_authorizations(self,
                                           site_id,
                                           wlan_id=None):
        """Does a GET request to /api/v1/sites/{site_id}/guests.

        Get List of Site Guest Authorizations

        Args:
            site_id (uuid|string): TODO: type description here.
            wlan_id (string, optional): UUID of single or multiple (Comma
                separated) WLAN under Site `site_id` (to filter by WLAN)

        Returns:
            list of Guest: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/api/v1/sites/{site_id}/guests')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('site_id')
                            .value(site_id)
                            .should_encode(True))
            .query_param(Parameter()
                         .key('wlan_id')
                         .value(wlan_id))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('global'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(Guest.from_dictionary)
            .local_error('400', 'The API endpoint exists but its syntax/payload is incorrect, detail may be given', APIException)
            .local_error('401', 'Unauthorized', ApiV1SitesGuests401ErrorException)
            .local_error('403', 'Permission Denied', ApiV1SitesGuests403ErrorException)
            .local_error('404', 'Not found. The API endpoint doesn\'t exist or resource doesn\'t exist', ApiV1SitesGuests404ErrorException)
        ).execute()

    def count_site_guest_authorizations(self,
                                        site_id,
                                        distinct='auth_method',
                                        page=1,
                                        limit=100,
                                        start=0,
                                        end=0,
                                        duration='1d'):
        """Does a GET request to /api/v1/sites/{site_id}/guests/count.

        Count Authorized Guest

        Args:
            site_id (uuid|string): TODO: type description here.
            distinct (Distinct12Enum, optional): TODO: type description here.
                Example: auth_method
            page (int, optional): TODO: type description here. Example: 1
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
            Count: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/api/v1/sites/{site_id}/guests/count')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('site_id')
                            .value(site_id)
                            .should_encode(True))
            .query_param(Parameter()
                         .key('distinct')
                         .value(distinct))
            .query_param(Parameter()
                         .key('page')
                         .value(page))
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
            .deserialize_into(Count.from_dictionary)
            .local_error('400', 'The API endpoint exists but its syntax/payload is incorrect, detail may be given', APIException)
            .local_error('401', 'Unauthorized', ApiV1SitesGuestsCount401ErrorException)
            .local_error('403', 'Permission Denied', ApiV1SitesGuestsCount403ErrorException)
            .local_error('404', 'Not found. The API endpoint doesn\'t exist or resource doesn\'t exist', ApiV1SitesGuestsCount404ErrorException)
        ).execute()

    def search_site_guest_authorization(self,
                                        site_id,
                                        wlan_id=None,
                                        auth_method=None,
                                        ssid=None,
                                        limit=100,
                                        start=0,
                                        end=0,
                                        duration='1d'):
        """Does a GET request to /api/v1/sites/{site_id}/guests/search.

        Search Authorized Guest

        Args:
            site_id (uuid|string): TODO: type description here.
            wlan_id (string, optional): TODO: type description here.
            auth_method (string, optional): TODO: type description here.
            ssid (string, optional): TODO: type description here.
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
            GuestsSearch: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/api/v1/sites/{site_id}/guests/search')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('site_id')
                            .value(site_id)
                            .should_encode(True))
            .query_param(Parameter()
                         .key('wlan_id')
                         .value(wlan_id))
            .query_param(Parameter()
                         .key('auth_method')
                         .value(auth_method))
            .query_param(Parameter()
                         .key('ssid')
                         .value(ssid))
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
            .deserialize_into(GuestsSearch.from_dictionary)
            .local_error('400', 'The API endpoint exists but its syntax/payload is incorrect, detail may be given', APIException)
            .local_error('401', 'Unauthorized', ApiV1SitesGuestsSearch401ErrorException)
            .local_error('403', 'Permission Denied', ApiV1SitesGuestsSearch403ErrorException)
            .local_error('404', 'Not found. The API endpoint doesn\'t exist or resource doesn\'t exist', ApiV1SitesGuestsSearch404ErrorException)
        ).execute()

    def delete_site_guest_authorization(self,
                                        site_id,
                                        guest_mac):
        """Does a DELETE request to /api/v1/sites/{site_id}/guests/{guest_mac}.

        Delete Guest Authorization

        Args:
            site_id (uuid|string): TODO: type description here.
            guest_mac (string): TODO: type description here.

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
            .path('/api/v1/sites/{site_id}/guests/{guest_mac}')
            .http_method(HttpMethodEnum.DELETE)
            .template_param(Parameter()
                            .key('site_id')
                            .value(site_id)
                            .should_encode(True))
            .template_param(Parameter()
                            .key('guest_mac')
                            .value(guest_mac)
                            .should_encode(True))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('global'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .local_error('400', 'The API endpoint exists but its syntax/payload is incorrect, detail may be given', APIException)
            .local_error('401', 'Unauthorized', ApiV1SitesGuests401ErrorException)
            .local_error('403', 'Permission Denied', ApiV1SitesGuests403ErrorException)
            .local_error('404', 'Not found. The API endpoint doesn\'t exist or resource doesn\'t exist', ApiV1SitesGuests404ErrorException)
        ).execute()

    def get_site_guest_authorization(self,
                                     site_id,
                                     guest_mac):
        """Does a GET request to /api/v1/sites/{site_id}/guests/{guest_mac}.

        Get Guest Authorization

        Args:
            site_id (uuid|string): TODO: type description here.
            guest_mac (string): TODO: type description here.

        Returns:
            Guest: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/api/v1/sites/{site_id}/guests/{guest_mac}')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('site_id')
                            .value(site_id)
                            .should_encode(True))
            .template_param(Parameter()
                            .key('guest_mac')
                            .value(guest_mac)
                            .should_encode(True))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('global'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(Guest.from_dictionary)
            .local_error('400', 'The API endpoint exists but its syntax/payload is incorrect, detail may be given', APIException)
            .local_error('401', 'Unauthorized', ApiV1SitesGuests401ErrorException)
            .local_error('403', 'Permission Denied', ApiV1SitesGuests403ErrorException)
            .local_error('404', 'Not found. The API endpoint doesn\'t exist or resource doesn\'t exist', ApiV1SitesGuests404ErrorException)
        ).execute()

    def update_site_guest_authorization(self,
                                        site_id,
                                        guest_mac,
                                        body=None):
        """Does a PUT request to /api/v1/sites/{site_id}/guests/{guest_mac}.

        Update Guest Authorization  

        Args:
            site_id (uuid|string): TODO: type description here.
            guest_mac (string): TODO: type description here.
            body (Guest, optional): Request Body

        Returns:
            Guest: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/api/v1/sites/{site_id}/guests/{guest_mac}')
            .http_method(HttpMethodEnum.PUT)
            .template_param(Parameter()
                            .key('site_id')
                            .value(site_id)
                            .should_encode(True))
            .template_param(Parameter()
                            .key('guest_mac')
                            .value(guest_mac)
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
            .deserialize_into(Guest.from_dictionary)
            .local_error('400', 'The API endpoint exists but its syntax/payload is incorrect, detail may be given', APIException)
            .local_error('401', 'Unauthorized', ApiV1SitesGuests401ErrorException)
            .local_error('403', 'Permission Denied', ApiV1SitesGuests403ErrorException)
            .local_error('404', 'Not found. The API endpoint doesn\'t exist or resource doesn\'t exist', ApiV1SitesGuests404ErrorException)
        ).execute()
