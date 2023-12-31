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
from mistapi.models.insight_metric import InsightMetric
from mistapi.models.device_metric import DeviceMetric
from mistapi.models.insight_rogue import InsightRogue
from mistapi.models.insight_rogue_clients import InsightRogueClients
from mistapi.exceptions.api_exception import APIException
from mistapi.exceptions.api_v_1_sites_insights_client_metric_401_error_exception import ApiV1SitesInsightsClientMetric401ErrorException
from mistapi.exceptions.api_v_1_sites_insights_client_metric_403_error_exception import ApiV1SitesInsightsClientMetric403ErrorException
from mistapi.exceptions.api_v_1_sites_insights_client_metric_404_error_exception import ApiV1SitesInsightsClientMetric404ErrorException
from mistapi.exceptions.api_v_1_sites_insights_device_metric_401_error_exception import ApiV1SitesInsightsDeviceMetric401ErrorException
from mistapi.exceptions.api_v_1_sites_insights_device_metric_403_error_exception import ApiV1SitesInsightsDeviceMetric403ErrorException
from mistapi.exceptions.api_v_1_sites_insights_device_metric_404_error_exception import ApiV1SitesInsightsDeviceMetric404ErrorException
from mistapi.exceptions.api_v_1_sites_insights_rogues_401_error_exception import ApiV1SitesInsightsRogues401ErrorException
from mistapi.exceptions.api_v_1_sites_insights_rogues_403_error_exception import ApiV1SitesInsightsRogues403ErrorException
from mistapi.exceptions.api_v_1_sites_insights_rogues_404_error_exception import ApiV1SitesInsightsRogues404ErrorException
from mistapi.exceptions.api_v_1_sites_insights_rogues_clients_401_error_exception import ApiV1SitesInsightsRoguesClients401ErrorException
from mistapi.exceptions.api_v_1_sites_insights_rogues_clients_403_error_exception import ApiV1SitesInsightsRoguesClients403ErrorException
from mistapi.exceptions.api_v_1_sites_insights_rogues_clients_404_error_exception import ApiV1SitesInsightsRoguesClients404ErrorException
from mistapi.exceptions.api_v_1_sites_insights_401_error_exception import ApiV1SitesInsights401ErrorException
from mistapi.exceptions.api_v_1_sites_insights_403_error_exception import ApiV1SitesInsights403ErrorException
from mistapi.exceptions.api_v_1_sites_insights_404_error_exception import ApiV1SitesInsights404ErrorException


class SitesInsightsController(BaseController):

    """A Controller to access Endpoints in the mistapi API."""
    def __init__(self, config):
        super(SitesInsightsController, self).__init__(config)

    def get_site_insight_metrics_for_client(self,
                                            site_id,
                                            client_mac,
                                            metric,
                                            page=1,
                                            limit=100,
                                            start=0,
                                            end=0,
                                            duration='1d',
                                            interval=None):
        """Does a GET request to /api/v1/sites/{site_id}/insights/client/{client_mac}/{metric}.

        Get Client Insight Metrics
        See metrics possibilities at /api/v1/const/insight_metrics

        Args:
            site_id (uuid|string): TODO: type description here.
            client_mac (string): TODO: type description here.
            metric (string): see /api/v1/const/insight_metrics for available
                metrics
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
            interval (string, optional): Aggregation works by giving a time
                range plus interval (e.g. 1d, 1h, 10m) where aggregation
                function would be applied to.

        Returns:
            InsightMetric: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/api/v1/sites/{site_id}/insights/client/{client_mac}/{metric}')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('site_id')
                            .value(site_id)
                            .should_encode(True))
            .template_param(Parameter()
                            .key('client_mac')
                            .value(client_mac)
                            .should_encode(True))
            .template_param(Parameter()
                            .key('metric')
                            .value(metric)
                            .should_encode(True))
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
            .query_param(Parameter()
                         .key('interval')
                         .value(interval))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('global'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(InsightMetric.from_dictionary)
            .local_error('400', 'The API endpoint exists but its syntax/payload is incorrect, detail may be given', APIException)
            .local_error('401', 'Unauthorized', ApiV1SitesInsightsClientMetric401ErrorException)
            .local_error('403', 'Permission Denied', ApiV1SitesInsightsClientMetric403ErrorException)
            .local_error('404', 'Not found. The API endpoint doesn\'t exist or resource doesn\'t exist', ApiV1SitesInsightsClientMetric404ErrorException)
        ).execute()

    def get_site_insight_metrics_for_device(self,
                                            site_id,
                                            metric,
                                            device_mac,
                                            page=1,
                                            limit=100,
                                            start=0,
                                            end=0,
                                            duration='1d',
                                            interval=None):
        """Does a GET request to /api/v1/sites/{site_id}/insights/device/{device_mac}/{metric}.

        Get AP Insight Metrics
        See metrics possibilities at /api/v1/const/insight_metrics

        Args:
            site_id (uuid|string): TODO: type description here.
            metric (string): see /api/v1/const/insight_metrics for available
                metrics
            device_mac (string): TODO: type description here.
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
            interval (string, optional): Aggregation works by giving a time
                range plus interval (e.g. 1d, 1h, 10m) where aggregation
                function would be applied to.

        Returns:
            DeviceMetric: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/api/v1/sites/{site_id}/insights/device/{device_mac}/{metric}')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('site_id')
                            .value(site_id)
                            .should_encode(True))
            .template_param(Parameter()
                            .key('metric')
                            .value(metric)
                            .should_encode(True))
            .template_param(Parameter()
                            .key('device_mac')
                            .value(device_mac)
                            .should_encode(True))
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
            .query_param(Parameter()
                         .key('interval')
                         .value(interval))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('global'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(DeviceMetric.from_dictionary)
            .local_error('400', 'The API endpoint exists but its syntax/payload is incorrect, detail may be given', APIException)
            .local_error('401', 'Unauthorized', ApiV1SitesInsightsDeviceMetric401ErrorException)
            .local_error('403', 'Permission Denied', ApiV1SitesInsightsDeviceMetric403ErrorException)
            .local_error('404', 'Not found. The API endpoint doesn\'t exist or resource doesn\'t exist', ApiV1SitesInsightsDeviceMetric404ErrorException)
        ).execute()

    def list_site_rogue_a_ps(self,
                             site_id,
                             mtype=None,
                             limit=100,
                             start=0,
                             end=0,
                             duration='1d',
                             interval=None):
        """Does a GET request to /api/v1/sites/{site_id}/insights/rogues.

        Get List of Site Rogue/Neighbor APs

        Args:
            site_id (uuid|string): TODO: type description here.
            mtype (Type57Enum, optional): TODO: type description here.
            limit (int, optional): TODO: type description here. Example: 100
            start (int, optional): TODO: type description here. Example: 0
            end (int, optional): TODO: type description here. Example: 0
            duration (string, optional): For historical stats and/or logs
                where time range is needed, you can specify the time range in
                a few different ways:   * ?start=1430000000&end=1430864000
                specify the start / end   * ?end=1430864000&duration=1d
                specify end time and duration   * ?duration=1d specify
                duration, end will be now() in seconds
            interval (string, optional): Aggregation works by giving a time
                range plus interval (e.g. 1d, 1h, 10m) where aggregation
                function would be applied to.

        Returns:
            InsightRogue: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/api/v1/sites/{site_id}/insights/rogues')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('site_id')
                            .value(site_id)
                            .should_encode(True))
            .query_param(Parameter()
                         .key('type')
                         .value(mtype))
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
            .query_param(Parameter()
                         .key('interval')
                         .value(interval))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('global'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(InsightRogue.from_dictionary)
            .local_error('400', 'The API endpoint exists but its syntax/payload is incorrect, detail may be given', APIException)
            .local_error('401', 'Unauthorized', ApiV1SitesInsightsRogues401ErrorException)
            .local_error('403', 'Permission Denied', ApiV1SitesInsightsRogues403ErrorException)
            .local_error('404', 'Not found. The API endpoint doesn\'t exist or resource doesn\'t exist', ApiV1SitesInsightsRogues404ErrorException)
        ).execute()

    def list_site_rogue_clients(self,
                                site_id,
                                limit=100,
                                start=0,
                                end=0,
                                duration='1d',
                                interval=None):
        """Does a GET request to /api/v1/sites/{site_id}/insights/rogues/clients.

        Get List of Site Rogue Clients

        Args:
            site_id (uuid|string): TODO: type description here.
            limit (int, optional): TODO: type description here. Example: 100
            start (int, optional): TODO: type description here. Example: 0
            end (int, optional): TODO: type description here. Example: 0
            duration (string, optional): For historical stats and/or logs
                where time range is needed, you can specify the time range in
                a few different ways:   * ?start=1430000000&end=1430864000
                specify the start / end   * ?end=1430864000&duration=1d
                specify end time and duration   * ?duration=1d specify
                duration, end will be now() in seconds
            interval (string, optional): Aggregation works by giving a time
                range plus interval (e.g. 1d, 1h, 10m) where aggregation
                function would be applied to.

        Returns:
            InsightRogueClients: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/api/v1/sites/{site_id}/insights/rogues/clients')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('site_id')
                            .value(site_id)
                            .should_encode(True))
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
            .query_param(Parameter()
                         .key('interval')
                         .value(interval))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('global'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(InsightRogueClients.from_dictionary)
            .local_error('400', 'The API endpoint exists but its syntax/payload is incorrect, detail may be given', APIException)
            .local_error('401', 'Unauthorized', ApiV1SitesInsightsRoguesClients401ErrorException)
            .local_error('403', 'Permission Denied', ApiV1SitesInsightsRoguesClients403ErrorException)
            .local_error('404', 'Not found. The API endpoint doesn\'t exist or resource doesn\'t exist', ApiV1SitesInsightsRoguesClients404ErrorException)
        ).execute()

    def get_site_insight_metrics(self,
                                 site_id,
                                 metric,
                                 page=1,
                                 limit=100,
                                 start=0,
                                 end=0,
                                 duration='1d',
                                 interval=None):
        """Does a GET request to /api/v1/sites/{site_id}/insights/{metric}.

        Get Site Insight Metrics
        See metrics possibilities at /api/v1/const/insight_metrics

        Args:
            site_id (uuid|string): TODO: type description here.
            metric (string): see /api/v1/const/insight_metrics for available
                metrics
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
            interval (string, optional): Aggregation works by giving a time
                range plus interval (e.g. 1d, 1h, 10m) where aggregation
                function would be applied to.

        Returns:
            InsightMetric: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/api/v1/sites/{site_id}/insights/{metric}')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('site_id')
                            .value(site_id)
                            .should_encode(True))
            .template_param(Parameter()
                            .key('metric')
                            .value(metric)
                            .should_encode(True))
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
            .query_param(Parameter()
                         .key('interval')
                         .value(interval))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('global'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(InsightMetric.from_dictionary)
            .local_error('400', 'The API endpoint exists but its syntax/payload is incorrect, detail may be given', APIException)
            .local_error('401', 'Unauthorized', ApiV1SitesInsights401ErrorException)
            .local_error('403', 'Permission Denied', ApiV1SitesInsights403ErrorException)
            .local_error('404', 'Not found. The API endpoint doesn\'t exist or resource doesn\'t exist', ApiV1SitesInsights404ErrorException)
        ).execute()
