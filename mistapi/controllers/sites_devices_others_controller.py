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
from mistapi.models.device_other import DeviceOther
from mistapi.models.count import Count
from mistapi.models.events_other_devices_search import EventsOtherDevicesSearch
from mistapi.exceptions.api_exception import APIException
from mistapi.exceptions.api_v_1_sites_otherdevices_401_error_exception import ApiV1SitesOtherdevices401ErrorException
from mistapi.exceptions.api_v_1_sites_otherdevices_403_error_exception import ApiV1SitesOtherdevices403ErrorException
from mistapi.exceptions.api_v_1_sites_otherdevices_404_error_exception import ApiV1SitesOtherdevices404ErrorException
from mistapi.exceptions.api_v_1_sites_otherdevices_events_count_401_error_exception import ApiV1SitesOtherdevicesEventsCount401ErrorException
from mistapi.exceptions.api_v_1_sites_otherdevices_events_count_403_error_exception import ApiV1SitesOtherdevicesEventsCount403ErrorException
from mistapi.exceptions.api_v_1_sites_otherdevices_events_count_404_error_exception import ApiV1SitesOtherdevicesEventsCount404ErrorException
from mistapi.exceptions.api_v_1_sites_otherdevices_events_search_401_error_exception import ApiV1SitesOtherdevicesEventsSearch401ErrorException
from mistapi.exceptions.api_v_1_sites_otherdevices_events_search_403_error_exception import ApiV1SitesOtherdevicesEventsSearch403ErrorException
from mistapi.exceptions.api_v_1_sites_otherdevices_events_search_404_error_exception import ApiV1SitesOtherdevicesEventsSearch404ErrorException


class SitesDevicesOthersController(BaseController):

    """A Controller to access Endpoints in the mistapi API."""
    def __init__(self, config):
        super(SitesDevicesOthersController, self).__init__(config)

    def list_site_other_devices(self,
                                site_id,
                                vendor=None,
                                mac=None,
                                serial=None,
                                model=None,
                                name=None,
                                page=1,
                                limit=100):
        """Does a GET request to /api/v1/sites/{site_id}/otherdevices.

        Get List of Site other devices (3rd party devices)

        Args:
            site_id (uuid|string): TODO: type description here.
            vendor (string, optional): TODO: type description here.
            mac (string, optional): TODO: type description here.
            serial (string, optional): TODO: type description here.
            model (string, optional): TODO: type description here.
            name (string, optional): TODO: type description here.
            page (int, optional): TODO: type description here. Example: 1
            limit (int, optional): TODO: type description here. Example: 100

        Returns:
            list of DeviceOther: Response from the API. Example response

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/api/v1/sites/{site_id}/otherdevices')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('site_id')
                            .value(site_id)
                            .should_encode(True))
            .query_param(Parameter()
                         .key('vendor')
                         .value(vendor))
            .query_param(Parameter()
                         .key('mac')
                         .value(mac))
            .query_param(Parameter()
                         .key('serial')
                         .value(serial))
            .query_param(Parameter()
                         .key('model')
                         .value(model))
            .query_param(Parameter()
                         .key('name')
                         .value(name))
            .query_param(Parameter()
                         .key('page')
                         .value(page))
            .query_param(Parameter()
                         .key('limit')
                         .value(limit))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('global'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(DeviceOther.from_dictionary)
            .local_error('400', 'The API endpoint exists but its syntax/payload is incorrect, detail may be given', APIException)
            .local_error('401', 'Unauthorized', ApiV1SitesOtherdevices401ErrorException)
            .local_error('403', 'Permission Denied', ApiV1SitesOtherdevices403ErrorException)
            .local_error('404', 'Not found. The API endpoint doesn\'t exist or resource doesn\'t exist', ApiV1SitesOtherdevices404ErrorException)
        ).execute()

    def count_site_other_devices_events(self,
                                        site_id,
                                        distinct='mac',
                                        start=0,
                                        end=0,
                                        duration='1d',
                                        limit=100,
                                        page=1):
        """Does a GET request to /api/v1/sites/{site_id}/otherdevices/events/count.

        Count Site OtherDevices Events

        Args:
            site_id (uuid|string): TODO: type description here.
            distinct (Distinct13Enum, optional): TODO: type description here.
                Example: mac
            start (int, optional): TODO: type description here. Example: 0
            end (int, optional): TODO: type description here. Example: 0
            duration (string, optional): For historical stats and/or logs
                where time range is needed, you can specify the time range in
                a few different ways:   * ?start=1430000000&end=1430864000
                specify the start / end   * ?end=1430864000&duration=1d
                specify end time and duration   * ?duration=1d specify
                duration, end will be now() in seconds
            limit (int, optional): TODO: type description here. Example: 100
            page (int, optional): TODO: type description here. Example: 1

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
            .path('/api/v1/sites/{site_id}/otherdevices/events/count')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('site_id')
                            .value(site_id)
                            .should_encode(True))
            .query_param(Parameter()
                         .key('distinct')
                         .value(distinct))
            .query_param(Parameter()
                         .key('start')
                         .value(start))
            .query_param(Parameter()
                         .key('end')
                         .value(end))
            .query_param(Parameter()
                         .key('duration')
                         .value(duration))
            .query_param(Parameter()
                         .key('limit')
                         .value(limit))
            .query_param(Parameter()
                         .key('page')
                         .value(page))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('global'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(Count.from_dictionary)
            .local_error('400', 'The API endpoint exists but its syntax/payload is incorrect, detail may be given', APIException)
            .local_error('401', 'Unauthorized', ApiV1SitesOtherdevicesEventsCount401ErrorException)
            .local_error('403', 'Permission Denied', ApiV1SitesOtherdevicesEventsCount403ErrorException)
            .local_error('404', 'Not found. The API endpoint doesn\'t exist or resource doesn\'t exist', ApiV1SitesOtherdevicesEventsCount404ErrorException)
        ).execute()

    def search_site_other_devices_events(self,
                                         site_id,
                                         mac=None,
                                         device_mac=None,
                                         vendor=None,
                                         mtype=None,
                                         start=0,
                                         end=0,
                                         duration='1d',
                                         limit=100,
                                         page=1):
        """Does a GET request to /api/v1/sites/{site_id}/otherdevices/events/search.

        Search Site OtherDevices Events

        Args:
            site_id (uuid|string): TODO: type description here.
            mac (string, optional): mac
            device_mac (string, optional): mac of attached device
            vendor (string, optional): vendor name
            mtype (string, optional): event type
            start (int, optional): TODO: type description here. Example: 0
            end (int, optional): TODO: type description here. Example: 0
            duration (string, optional): For historical stats and/or logs
                where time range is needed, you can specify the time range in
                a few different ways:   * ?start=1430000000&end=1430864000
                specify the start / end   * ?end=1430864000&duration=1d
                specify end time and duration   * ?duration=1d specify
                duration, end will be now() in seconds
            limit (int, optional): TODO: type description here. Example: 100
            page (int, optional): TODO: type description here. Example: 1

        Returns:
            EventsOtherDevicesSearch: Response from the API. Example response

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/api/v1/sites/{site_id}/otherdevices/events/search')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('site_id')
                            .value(site_id)
                            .should_encode(True))
            .query_param(Parameter()
                         .key('mac')
                         .value(mac))
            .query_param(Parameter()
                         .key('device_mac')
                         .value(device_mac))
            .query_param(Parameter()
                         .key('vendor')
                         .value(vendor))
            .query_param(Parameter()
                         .key('type')
                         .value(mtype))
            .query_param(Parameter()
                         .key('start')
                         .value(start))
            .query_param(Parameter()
                         .key('end')
                         .value(end))
            .query_param(Parameter()
                         .key('duration')
                         .value(duration))
            .query_param(Parameter()
                         .key('limit')
                         .value(limit))
            .query_param(Parameter()
                         .key('page')
                         .value(page))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('global'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(EventsOtherDevicesSearch.from_dictionary)
            .local_error('400', 'The API endpoint exists but its syntax/payload is incorrect, detail may be given', APIException)
            .local_error('401', 'Unauthorized', ApiV1SitesOtherdevicesEventsSearch401ErrorException)
            .local_error('403', 'Permission Denied', ApiV1SitesOtherdevicesEventsSearch403ErrorException)
            .local_error('404', 'Not found. The API endpoint doesn\'t exist or resource doesn\'t exist', ApiV1SitesOtherdevicesEventsSearch404ErrorException)
        ).execute()
