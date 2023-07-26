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
from mistapi.models.api_v_1_sites_skyatp_events_search_response import ApiV1SitesSkyatpEventsSearchResponse
from mistapi.exceptions.api_exception import APIException
from mistapi.exceptions.api_v_1_sites_skyatp_events_count_401_error_exception import ApiV1SitesSkyatpEventsCount401ErrorException
from mistapi.exceptions.api_v_1_sites_skyatp_events_count_403_error_exception import ApiV1SitesSkyatpEventsCount403ErrorException
from mistapi.exceptions.api_v_1_sites_skyatp_events_count_404_error_exception import ApiV1SitesSkyatpEventsCount404ErrorException
from mistapi.exceptions.api_v_1_sites_skyatp_events_search_401_error_exception import ApiV1SitesSkyatpEventsSearch401ErrorException
from mistapi.exceptions.api_v_1_sites_skyatp_events_search_403_error_exception import ApiV1SitesSkyatpEventsSearch403ErrorException
from mistapi.exceptions.api_v_1_sites_skyatp_events_search_404_error_exception import ApiV1SitesSkyatpEventsSearch404ErrorException


class SitesSkyatpController(BaseController):

    """A Controller to access Endpoints in the mistapi API."""
    def __init__(self, config):
        super(SitesSkyatpController, self).__init__(config)

    def count_site_skyatp_events(self,
                                 site_id,
                                 distinct='type',
                                 mtype=None,
                                 mac=None,
                                 device_mac=None,
                                 threat_level=None,
                                 ip_address=None,
                                 page=1,
                                 limit=100,
                                 start=0,
                                 end=0,
                                 duration='1d'):
        """Does a GET request to /api/v1/sites/{site_id}/skyatp/events/count.

        Count by Distinct Attributes of Skyatp Events (WIP)

        Args:
            site_id (uuid|string): TODO: type description here.
            distinct (Distinct15Enum, optional): TODO: type description here.
                Example: type
            mtype (string, optional): event type, e.g. cc, fs, mw
            mac (string, optional): client MAC
            device_mac (string, optional): device MAC
            threat_level (int, optional): threat level
            ip_address (string, optional): TODO: type description here.
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
            .path('/api/v1/sites/{site_id}/skyatp/events/count')
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
                         .key('mac')
                         .value(mac))
            .query_param(Parameter()
                         .key('device_mac')
                         .value(device_mac))
            .query_param(Parameter()
                         .key('threat_level')
                         .value(threat_level))
            .query_param(Parameter()
                         .key('ip address')
                         .value(ip_address))
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
            .local_error('401', 'Unauthorized', ApiV1SitesSkyatpEventsCount401ErrorException)
            .local_error('403', 'Permission Denied', ApiV1SitesSkyatpEventsCount403ErrorException)
            .local_error('404', 'Not found. The API endpoint doesn\'t exist or resource doesn\'t exist', ApiV1SitesSkyatpEventsCount404ErrorException)
        ).execute()

    def search_site_skyatp_events(self,
                                  site_id,
                                  mtype=None,
                                  mac=None,
                                  device_mac=None,
                                  threat_level=None,
                                  ip_address=None,
                                  limit=100,
                                  start=0,
                                  end=0,
                                  duration='1d'):
        """Does a GET request to /api/v1/sites/{site_id}/skyatp/events/search.

        Search Skyatp Events (WIP)

        Args:
            site_id (uuid|string): TODO: type description here.
            mtype (string, optional): event type, e.g. cc, fs, mw
            mac (string, optional): client MAC
            device_mac (string, optional): device MAC
            threat_level (int, optional): threat level
            ip_address (string, optional): TODO: type description here.
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
            ApiV1SitesSkyatpEventsSearchResponse: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/api/v1/sites/{site_id}/skyatp/events/search')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('site_id')
                            .value(site_id)
                            .should_encode(True))
            .query_param(Parameter()
                         .key('type')
                         .value(mtype))
            .query_param(Parameter()
                         .key('mac')
                         .value(mac))
            .query_param(Parameter()
                         .key('device_mac')
                         .value(device_mac))
            .query_param(Parameter()
                         .key('threat_level')
                         .value(threat_level))
            .query_param(Parameter()
                         .key('ip address')
                         .value(ip_address))
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
            .deserialize_into(ApiV1SitesSkyatpEventsSearchResponse.from_dictionary)
            .local_error('400', 'The API endpoint exists but its syntax/payload is incorrect, detail may be given', APIException)
            .local_error('401', 'Unauthorized', ApiV1SitesSkyatpEventsSearch401ErrorException)
            .local_error('403', 'Permission Denied', ApiV1SitesSkyatpEventsSearch403ErrorException)
            .local_error('404', 'Not found. The API endpoint doesn\'t exist or resource doesn\'t exist', ApiV1SitesSkyatpEventsSearch404ErrorException)
        ).execute()
