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
from mistapi.models.count import Count
from mistapi.models.rogue_events_search import RogueEventsSearch
from mistapi.models.api_v_1_sites_rogues_response import ApiV1SitesRoguesResponse
from mistapi.exceptions.api_exception import APIException
from mistapi.exceptions.api_v_1_sites_rogues_events_count_401_error_exception import ApiV1SitesRoguesEventsCount401ErrorException
from mistapi.exceptions.api_v_1_sites_rogues_events_count_403_error_exception import ApiV1SitesRoguesEventsCount403ErrorException
from mistapi.exceptions.api_v_1_sites_rogues_events_count_404_error_exception import ApiV1SitesRoguesEventsCount404ErrorException
from mistapi.exceptions.api_v_1_sites_rogues_events_search_401_error_exception import ApiV1SitesRoguesEventsSearch401ErrorException
from mistapi.exceptions.api_v_1_sites_rogues_events_search_403_error_exception import ApiV1SitesRoguesEventsSearch403ErrorException
from mistapi.exceptions.api_v_1_sites_rogues_events_search_404_error_exception import ApiV1SitesRoguesEventsSearch404ErrorException
from mistapi.exceptions.api_v_1_sites_rogues_401_error_exception import ApiV1SitesRogues401ErrorException
from mistapi.exceptions.api_v_1_sites_rogues_403_error_exception import ApiV1SitesRogues403ErrorException
from mistapi.exceptions.api_v_1_sites_rogues_404_error_exception import ApiV1SitesRogues404ErrorException
from mistapi.exceptions.api_v_1_sites_rogues_deauth_clients_401_error_exception import ApiV1SitesRoguesDeauthClients401ErrorException
from mistapi.exceptions.api_v_1_sites_rogues_deauth_clients_403_error_exception import ApiV1SitesRoguesDeauthClients403ErrorException
from mistapi.exceptions.api_v_1_sites_rogues_deauth_clients_404_error_exception import ApiV1SitesRoguesDeauthClients404ErrorException


class SitesRoguesController(BaseController):

    """A Controller to access Endpoints in the mistapi API."""
    def __init__(self, config):
        super(SitesRoguesController, self).__init__(config)

    def count_site_rogue_events(self,
                                site_id,
                                distinct='bssid',
                                mtype=None,
                                ssid=None,
                                bssid=None,
                                ap_mac=None,
                                channel=None,
                                seen_on_lan=None,
                                page=1,
                                limit=100,
                                start=0,
                                end=0,
                                duration='1d'):
        """Does a GET request to /api/v1/sites/{site_id}/rogues/events/count.

        Count Rogue Events

        Args:
            site_id (uuid|string): TODO: type description here.
            distinct (Distinct14Enum, optional): TODO: type description here.
                Example: bssid
            mtype (Type57Enum, optional): TODO: type description here.
            ssid (string, optional): ssid of the network detected as threat
            bssid (string, optional): bssid of the network detected as threat
            ap_mac (string, optional): mac of the device that had strongest
                signal strength for ssid/bssid pair
            channel (string, optional): channel over which ap_mac heard
                ssid/bssid pair
            seen_on_lan (bool, optional): whether the reporting AP see a
                wireless client (on LAN) connecting to it
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
            .path('/api/v1/sites/{site_id}/rogues/events/count')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('site_id')
                            .value(site_id)
                            .should_encode(True))
            .query_param(Parameter()
                         .key('distinct')
                         .value(distinct))
            .query_param(Parameter()
                         .key('type')
                         .value(mtype))
            .query_param(Parameter()
                         .key('ssid')
                         .value(ssid))
            .query_param(Parameter()
                         .key('bssid')
                         .value(bssid))
            .query_param(Parameter()
                         .key('ap_mac')
                         .value(ap_mac))
            .query_param(Parameter()
                         .key('channel')
                         .value(channel))
            .query_param(Parameter()
                         .key('seen_on_lan')
                         .value(seen_on_lan))
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
            .local_error('401', 'Unauthorized', ApiV1SitesRoguesEventsCount401ErrorException)
            .local_error('403', 'Permission Denied', ApiV1SitesRoguesEventsCount403ErrorException)
            .local_error('404', 'Not found. The API endpoint doesn\'t exist or resource doesn\'t exist', ApiV1SitesRoguesEventsCount404ErrorException)
        ).execute()

    def search_site_rogue_events(self,
                                 site_id,
                                 mtype=None,
                                 ssid=None,
                                 bssid=None,
                                 ap_mac=None,
                                 channel=None,
                                 seen_on_lan=None,
                                 limit=100,
                                 start=0,
                                 end=0,
                                 duration='1d'):
        """Does a GET request to /api/v1/sites/{site_id}/rogues/events/search.

        Search Rogue Events

        Args:
            site_id (uuid|string): TODO: type description here.
            mtype (Type57Enum, optional): TODO: type description here.
            ssid (string, optional): ssid of the network detected as threat
            bssid (string, optional): bssid of the network detected as threat
            ap_mac (string, optional): mac of the device that had strongest
                signal strength for ssid/bssid pair
            channel (int, optional): channel over which ap_mac heard
                ssid/bssid pair
            seen_on_lan (bool, optional): whether the reporting AP see a
                wireless client (on LAN) connecting to it
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
            RogueEventsSearch: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/api/v1/sites/{site_id}/rogues/events/search')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('site_id')
                            .value(site_id)
                            .should_encode(True))
            .query_param(Parameter()
                         .key('type')
                         .value(mtype))
            .query_param(Parameter()
                         .key('ssid')
                         .value(ssid))
            .query_param(Parameter()
                         .key('bssid')
                         .value(bssid))
            .query_param(Parameter()
                         .key('ap_mac')
                         .value(ap_mac))
            .query_param(Parameter()
                         .key('channel')
                         .value(channel))
            .query_param(Parameter()
                         .key('seen_on_lan')
                         .value(seen_on_lan))
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
            .deserialize_into(RogueEventsSearch.from_dictionary)
            .local_error('400', 'The API endpoint exists but its syntax/payload is incorrect, detail may be given', APIException)
            .local_error('401', 'Unauthorized', ApiV1SitesRoguesEventsSearch401ErrorException)
            .local_error('403', 'Permission Denied', ApiV1SitesRoguesEventsSearch403ErrorException)
            .local_error('404', 'Not found. The API endpoint doesn\'t exist or resource doesn\'t exist', ApiV1SitesRoguesEventsSearch404ErrorException)
        ).execute()

    def get_site_rogue_ap(self,
                          site_id,
                          rogue_bssid):
        """Does a GET request to /api/v1/sites/{site_id}/rogues/{rogue_bssid}.

        Get Rogue AP Details

        Args:
            site_id (uuid|string): TODO: type description here.
            rogue_bssid (string): TODO: type description here.

        Returns:
            ApiV1SitesRoguesResponse: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/api/v1/sites/{site_id}/rogues/{rogue_bssid}')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('site_id')
                            .value(site_id)
                            .should_encode(True))
            .template_param(Parameter()
                            .key('rogue_bssid')
                            .value(rogue_bssid)
                            .should_encode(True))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('global'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ApiV1SitesRoguesResponse.from_dictionary)
            .local_error('400', 'The API endpoint exists but its syntax/payload is incorrect, detail may be given', APIException)
            .local_error('401', 'Unauthorized', ApiV1SitesRogues401ErrorException)
            .local_error('403', 'Permission Denied', ApiV1SitesRogues403ErrorException)
            .local_error('404', 'Not found. The API endpoint doesn\'t exist or resource doesn\'t exist', ApiV1SitesRogues404ErrorException)
        ).execute()

    def deauth_site_wireless_clients_connected_to_a_rogue(self,
                                                          site_id,
                                                          rogue_bssid):
        """Does a POST request to /api/v1/sites/{site_id}/rogues/{rogue_bssid}/deauth_clients.

        Send Deauth frame to clients connected to a Rogue AP

        Args:
            site_id (uuid|string): TODO: type description here.
            rogue_bssid (string): TODO: type description here.

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
            .path('/api/v1/sites/{site_id}/rogues/{rogue_bssid}/deauth_clients')
            .http_method(HttpMethodEnum.POST)
            .template_param(Parameter()
                            .key('site_id')
                            .value(site_id)
                            .should_encode(True))
            .template_param(Parameter()
                            .key('rogue_bssid')
                            .value(rogue_bssid)
                            .should_encode(True))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('global'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .local_error('400', 'The API endpoint exists but its syntax/payload is incorrect, detail may be given', APIException)
            .local_error('401', 'Unauthorized', ApiV1SitesRoguesDeauthClients401ErrorException)
            .local_error('403', 'Permission Denied', ApiV1SitesRoguesDeauthClients403ErrorException)
            .local_error('404', 'Not found. The API endpoint doesn\'t exist or resource doesn\'t exist', ApiV1SitesRoguesDeauthClients404ErrorException)
        ).execute()
