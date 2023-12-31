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
from mistapi.models.call_events_array_search import CallEventsArraySearch
from mistapi.models.call_stats_array import CallStatsArray
from mistapi.exceptions.api_exception import APIException
from mistapi.exceptions.api_v_1_sites_call_events_count_401_error_exception import ApiV1SitesCallEventsCount401ErrorException
from mistapi.exceptions.api_v_1_sites_call_events_count_403_error_exception import ApiV1SitesCallEventsCount403ErrorException
from mistapi.exceptions.api_v_1_sites_call_events_count_404_error_exception import ApiV1SitesCallEventsCount404ErrorException
from mistapi.exceptions.api_v_1_sites_call_events_search_401_error_exception import ApiV1SitesCallEventsSearch401ErrorException
from mistapi.exceptions.api_v_1_sites_call_events_search_403_error_exception import ApiV1SitesCallEventsSearch403ErrorException
from mistapi.exceptions.api_v_1_sites_call_events_search_404_error_exception import ApiV1SitesCallEventsSearch404ErrorException
from mistapi.exceptions.api_v_1_sites_stats_calls_count_401_error_exception import ApiV1SitesStatsCallsCount401ErrorException
from mistapi.exceptions.api_v_1_sites_stats_calls_count_403_error_exception import ApiV1SitesStatsCallsCount403ErrorException
from mistapi.exceptions.api_v_1_sites_stats_calls_count_404_error_exception import ApiV1SitesStatsCallsCount404ErrorException
from mistapi.exceptions.api_v_1_sites_stats_calls_search_401_error_exception import ApiV1SitesStatsCallsSearch401ErrorException
from mistapi.exceptions.api_v_1_sites_stats_calls_search_403_error_exception import ApiV1SitesStatsCallsSearch403ErrorException
from mistapi.exceptions.api_v_1_sites_stats_calls_search_404_error_exception import ApiV1SitesStatsCallsSearch404ErrorException


class SitesCallsController(BaseController):

    """A Controller to access Endpoints in the mistapi API."""
    def __init__(self, config):
        super(SitesCallsController, self).__init__(config)

    def count_site_call_events(self,
                               site_id,
                               distinct=None):
        """Does a GET request to /api/v1/sites/{site_id}/call/events/count.

        Count Site Call Events

        Args:
            site_id (uuid|string): TODO: type description here.
            distinct (Distinct4Enum, optional): TODO: type description here.

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
            .path('/api/v1/sites/{site_id}/call/events/count')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('site_id')
                            .value(site_id)
                            .should_encode(True))
            .query_param(Parameter()
                         .key('distinct')
                         .value(distinct))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('global'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(Count.from_dictionary)
            .local_error('400', 'The API endpoint exists but its syntax/payload is incorrect, detail may be given', APIException)
            .local_error('401', 'Unauthorized', ApiV1SitesCallEventsCount401ErrorException)
            .local_error('403', 'Permission Denied', ApiV1SitesCallEventsCount403ErrorException)
            .local_error('404', 'Not found. The API endpoint doesn\'t exist or resource doesn\'t exist', ApiV1SitesCallEventsCount404ErrorException)
        ).execute()

    def search_site_call_events(self,
                                site_id,
                                mtype=None,
                                ap=None,
                                mac=None,
                                app=None):
        """Does a GET request to /api/v1/sites/{site_id}/call/events/search.

        Search Site Call Events

        Args:
            site_id (uuid|string): TODO: type description here.
            mtype (string, optional): Event Type. See
                [listCallEventsDefinitions](/#operation/listCallEventsDefinitio
                ns)
            ap (string, optional): TODO: type description here.
            mac (string, optional): TODO: type description here.
            app (string, optional): TODO: type description here.

        Returns:
            CallEventsArraySearch: Response from the API. Example response

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/api/v1/sites/{site_id}/call/events/search')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('site_id')
                            .value(site_id)
                            .should_encode(True))
            .query_param(Parameter()
                         .key('type')
                         .value(mtype))
            .query_param(Parameter()
                         .key('ap')
                         .value(ap))
            .query_param(Parameter()
                         .key('mac')
                         .value(mac))
            .query_param(Parameter()
                         .key('app')
                         .value(app))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('global'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(CallEventsArraySearch.from_dictionary)
            .local_error('400', 'The API endpoint exists but its syntax/payload is incorrect, detail may be given', APIException)
            .local_error('401', 'Unauthorized', ApiV1SitesCallEventsSearch401ErrorException)
            .local_error('403', 'Permission Denied', ApiV1SitesCallEventsSearch403ErrorException)
            .local_error('404', 'Not found. The API endpoint doesn\'t exist or resource doesn\'t exist', ApiV1SitesCallEventsSearch404ErrorException)
        ).execute()

    def count_site_calls(self,
                         site_id,
                         distrinct='mac',
                         rating=None,
                         app=None,
                         start=None,
                         end=None):
        """Does a GET request to /api/v1/sites/{site_id}/stats/calls/count.

        Count by Distinct Attributes of Calls

        Args:
            site_id (uuid|string): TODO: type description here.
            distrinct (DistrinctEnum, optional): TODO: type description here.
                Example: mac
            rating (int, optional): feedback rating (e.g. "rating=1" or
                "rating=1,2")
            app (string, optional): TODO: type description here.
            start (string, optional): TODO: type description here.
            end (string, optional): TODO: type description here.

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
            .path('/api/v1/sites/{site_id}/stats/calls/count')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('site_id')
                            .value(site_id)
                            .should_encode(True))
            .query_param(Parameter()
                         .key('distrinct')
                         .value(distrinct))
            .query_param(Parameter()
                         .key('rating')
                         .value(rating))
            .query_param(Parameter()
                         .key('app')
                         .value(app))
            .query_param(Parameter()
                         .key('start')
                         .value(start))
            .query_param(Parameter()
                         .key('end')
                         .value(end))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('global'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(Count.from_dictionary)
            .local_error('400', 'The API endpoint exists but its syntax/payload is incorrect, detail may be given', APIException)
            .local_error('401', 'Unauthorized', ApiV1SitesStatsCallsCount401ErrorException)
            .local_error('403', 'Permission Denied', ApiV1SitesStatsCallsCount403ErrorException)
            .local_error('404', 'Not found. The API endpoint doesn\'t exist or resource doesn\'t exist', ApiV1SitesStatsCallsCount404ErrorException)
        ).execute()

    def search_site_calls(self,
                          site_id,
                          mac=None,
                          app=None,
                          limit=100,
                          start=0,
                          end=0,
                          duration='1d'):
        """Does a GET request to /api/v1/sites/{site_id}/stats/calls/search.

        Search Calls

        Args:
            site_id (uuid|string): TODO: type description here.
            mac (string, optional): device identifier
            app (string, optional): Third party app name
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
            CallStatsArray: Response from the API. Example response

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/api/v1/sites/{site_id}/stats/calls/search')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('site_id')
                            .value(site_id)
                            .should_encode(True))
            .query_param(Parameter()
                         .key('mac')
                         .value(mac))
            .query_param(Parameter()
                         .key('app')
                         .value(app))
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
            .deserialize_into(CallStatsArray.from_dictionary)
            .local_error('400', 'The API endpoint exists but its syntax/payload is incorrect, detail may be given', APIException)
            .local_error('401', 'Unauthorized', ApiV1SitesStatsCallsSearch401ErrorException)
            .local_error('403', 'Permission Denied', ApiV1SitesStatsCallsSearch403ErrorException)
            .local_error('404', 'Not found. The API endpoint doesn\'t exist or resource doesn\'t exist', ApiV1SitesStatsCallsSearch404ErrorException)
        ).execute()
