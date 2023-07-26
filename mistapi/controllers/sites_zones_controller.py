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
from mistapi.models.zone import Zone
from mistapi.models.api_v_1_sites_count_response import ApiV1SitesCountResponse
from mistapi.models.api_v_1_sites_visits_search_response import ApiV1SitesVisitsSearchResponse
from mistapi.exceptions.api_exception import APIException
from mistapi.exceptions.api_v_1_sites_zones_401_error_exception import ApiV1SitesZones401ErrorException
from mistapi.exceptions.api_v_1_sites_zones_403_error_exception import ApiV1SitesZones403ErrorException
from mistapi.exceptions.api_v_1_sites_zones_404_error_exception import ApiV1SitesZones404ErrorException
from mistapi.exceptions.api_v_1_sites_count_401_error_exception import ApiV1SitesCount401ErrorException
from mistapi.exceptions.api_v_1_sites_count_403_error_exception import ApiV1SitesCount403ErrorException
from mistapi.exceptions.api_v_1_sites_count_404_error_exception import ApiV1SitesCount404ErrorException
from mistapi.exceptions.api_v_1_sites_visits_search_401_error_exception import ApiV1SitesVisitsSearch401ErrorException
from mistapi.exceptions.api_v_1_sites_visits_search_403_error_exception import ApiV1SitesVisitsSearch403ErrorException
from mistapi.exceptions.api_v_1_sites_visits_search_404_error_exception import ApiV1SitesVisitsSearch404ErrorException


class SitesZonesController(BaseController):

    """A Controller to access Endpoints in the mistapi API."""
    def __init__(self, config):
        super(SitesZonesController, self).__init__(config)

    def list_site_zones(self,
                        site_id):
        """Does a GET request to /api/v1/sites/{site_id}/zones.

        Get List of Site Zones

        Args:
            site_id (uuid|string): TODO: type description here.

        Returns:
            list of Zone: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/api/v1/sites/{site_id}/zones')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('site_id')
                            .value(site_id)
                            .should_encode(True))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('global'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(Zone.from_dictionary)
            .local_error('400', 'The API endpoint exists but its syntax/payload is incorrect, detail may be given', APIException)
            .local_error('401', 'Unauthorized', ApiV1SitesZones401ErrorException)
            .local_error('403', 'Permission Denied', ApiV1SitesZones403ErrorException)
            .local_error('404', 'Not found. The API endpoint doesn\'t exist or resource doesn\'t exist', ApiV1SitesZones404ErrorException)
        ).execute()

    def create_site_zone(self,
                         site_id,
                         body=None):
        """Does a POST request to /api/v1/sites/{site_id}/zones.

        Create Site Zone 

        Args:
            site_id (uuid|string): TODO: type description here.
            body (Zone, optional): Request Body

        Returns:
            Zone: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/api/v1/sites/{site_id}/zones')
            .http_method(HttpMethodEnum.POST)
            .template_param(Parameter()
                            .key('site_id')
                            .value(site_id)
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
            .deserialize_into(Zone.from_dictionary)
            .local_error('400', 'The API endpoint exists but its syntax/payload is incorrect, detail may be given', APIException)
            .local_error('401', 'Unauthorized', ApiV1SitesZones401ErrorException)
            .local_error('403', 'Permission Denied', ApiV1SitesZones403ErrorException)
            .local_error('404', 'Not found. The API endpoint doesn\'t exist or resource doesn\'t exist', ApiV1SitesZones404ErrorException)
        ).execute()

    def delete_site_zone(self,
                         site_id,
                         zone_id):
        """Does a DELETE request to /api/v1/sites/{site_id}/zones/{zone_id}.

        Delete Site Zone

        Args:
            site_id (uuid|string): TODO: type description here.
            zone_id (uuid|string): TODO: type description here.

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
            .path('/api/v1/sites/{site_id}/zones/{zone_id}')
            .http_method(HttpMethodEnum.DELETE)
            .template_param(Parameter()
                            .key('site_id')
                            .value(site_id)
                            .should_encode(True))
            .template_param(Parameter()
                            .key('zone_id')
                            .value(zone_id)
                            .should_encode(True))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('global'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .local_error('400', 'The API endpoint exists but its syntax/payload is incorrect, detail may be given', APIException)
            .local_error('401', 'Unauthorized', ApiV1SitesZones401ErrorException)
            .local_error('403', 'Permission Denied', ApiV1SitesZones403ErrorException)
            .local_error('404', 'Not found. The API endpoint doesn\'t exist or resource doesn\'t exist', ApiV1SitesZones404ErrorException)
        ).execute()

    def get_site_zone(self,
                      site_id,
                      zone_id):
        """Does a GET request to /api/v1/sites/{site_id}/zones/{zone_id}.

        Get Site Zone Details

        Args:
            site_id (uuid|string): TODO: type description here.
            zone_id (uuid|string): TODO: type description here.

        Returns:
            Zone: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/api/v1/sites/{site_id}/zones/{zone_id}')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('site_id')
                            .value(site_id)
                            .should_encode(True))
            .template_param(Parameter()
                            .key('zone_id')
                            .value(zone_id)
                            .should_encode(True))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('global'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(Zone.from_dictionary)
            .local_error('400', 'The API endpoint exists but its syntax/payload is incorrect, detail may be given', APIException)
            .local_error('401', 'Unauthorized', ApiV1SitesZones401ErrorException)
            .local_error('403', 'Permission Denied', ApiV1SitesZones403ErrorException)
            .local_error('404', 'Not found. The API endpoint doesn\'t exist or resource doesn\'t exist', ApiV1SitesZones404ErrorException)
        ).execute()

    def update_site_zone(self,
                         site_id,
                         zone_id,
                         body=None):
        """Does a PUT request to /api/v1/sites/{site_id}/zones/{zone_id}.

        Update Site Zone

        Args:
            site_id (uuid|string): TODO: type description here.
            zone_id (uuid|string): TODO: type description here.
            body (Zone, optional): Request Body

        Returns:
            Zone: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/api/v1/sites/{site_id}/zones/{zone_id}')
            .http_method(HttpMethodEnum.PUT)
            .template_param(Parameter()
                            .key('site_id')
                            .value(site_id)
                            .should_encode(True))
            .template_param(Parameter()
                            .key('zone_id')
                            .value(zone_id)
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
            .deserialize_into(Zone.from_dictionary)
            .local_error('400', 'The API endpoint exists but its syntax/payload is incorrect, detail may be given', APIException)
            .local_error('401', 'Unauthorized', ApiV1SitesZones401ErrorException)
            .local_error('403', 'Permission Denied', ApiV1SitesZones403ErrorException)
            .local_error('404', 'Not found. The API endpoint doesn\'t exist or resource doesn\'t exist', ApiV1SitesZones404ErrorException)
        ).execute()

    def count_site_zone_sessions(self,
                                 site_id,
                                 zone_type,
                                 distinct='scope_id',
                                 user_type='client',
                                 user=None,
                                 scope_id=None,
                                 scope='site',
                                 page=1,
                                 limit=100,
                                 start=0,
                                 end=0,
                                 duration='1d'):
        """Does a GET request to /api/v1/sites/{site_id}/{zone_type}/count.

        Count Site Zone Sessions

        Args:
            site_id (uuid|string): TODO: type description here.
            zone_type (ZoneTypeEnum): TODO: type description here.
            distinct (Distinct24Enum, optional): TODO: type description here.
                Example: scope_id
            user_type (UserTypeEnum, optional): user type
            user (string, optional): client MAC / Asset MAC / SDK UUID
            scope_id (string, optional): if `scope`==`map`/`zone`/`rssizone`,
                the scope id
            scope (Scope19Enum, optional): scope
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
            ApiV1SitesCountResponse: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/api/v1/sites/{site_id}/{zone_type}/count')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('site_id')
                            .value(site_id)
                            .should_encode(True))
            .template_param(Parameter()
                            .key('zone_type')
                            .value(zone_type)
                            .should_encode(True))
            .query_param(Parameter()
                         .key('distinct')
                         .value(distinct))
            .query_param(Parameter()
                         .key('user_type')
                         .value(user_type))
            .query_param(Parameter()
                         .key('user')
                         .value(user))
            .query_param(Parameter()
                         .key('scope_id')
                         .value(scope_id))
            .query_param(Parameter()
                         .key('scope')
                         .value(scope))
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
            .deserialize_into(ApiV1SitesCountResponse.from_dictionary)
            .local_error('400', 'The API endpoint exists but its syntax/payload is incorrect, detail may be given', APIException)
            .local_error('401', 'Unauthorized', ApiV1SitesCount401ErrorException)
            .local_error('403', 'Permission Denied', ApiV1SitesCount403ErrorException)
            .local_error('404', 'Not found. The API endpoint doesn\'t exist or resource doesn\'t exist', ApiV1SitesCount404ErrorException)
        ).execute()

    def search_site_zone_sessions(self,
                                  site_id,
                                  zone_type,
                                  user_type='client',
                                  user=None,
                                  scope_id=None,
                                  scope='site',
                                  page=1,
                                  limit=100,
                                  start=0,
                                  end=0,
                                  duration='1d'):
        """Does a GET request to /api/v1/sites/{site_id}/{zone_type}/visits/search.

        Search Zone Sessions

        Args:
            site_id (uuid|string): TODO: type description here.
            zone_type (ZoneTypeEnum): TODO: type description here.
            user_type (UserTypeEnum, optional): user type, client (default) /
                sdkclient / asset
            user (string, optional): client MAC / Asset MAC / SDK UUID
            scope_id (string, optional): if `scope`==`map`/`zone`/`rssizone`,
                the scope id
            scope (Scope19Enum, optional): scope
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
            ApiV1SitesVisitsSearchResponse: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/api/v1/sites/{site_id}/{zone_type}/visits/search')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('site_id')
                            .value(site_id)
                            .should_encode(True))
            .template_param(Parameter()
                            .key('zone_type')
                            .value(zone_type)
                            .should_encode(True))
            .query_param(Parameter()
                         .key('user_type')
                         .value(user_type))
            .query_param(Parameter()
                         .key('user')
                         .value(user))
            .query_param(Parameter()
                         .key('scope_id')
                         .value(scope_id))
            .query_param(Parameter()
                         .key('scope')
                         .value(scope))
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
            .deserialize_into(ApiV1SitesVisitsSearchResponse.from_dictionary)
            .local_error('400', 'The API endpoint exists but its syntax/payload is incorrect, detail may be given', APIException)
            .local_error('401', 'Unauthorized', ApiV1SitesVisitsSearch401ErrorException)
            .local_error('403', 'Permission Denied', ApiV1SitesVisitsSearch403ErrorException)
            .local_error('404', 'Not found. The API endpoint doesn\'t exist or resource doesn\'t exist', ApiV1SitesVisitsSearch404ErrorException)
        ).execute()
