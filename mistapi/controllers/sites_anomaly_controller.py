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
from mistapi.models.anomaly_metrics import AnomalyMetrics
from mistapi.exceptions.api_exception import APIException
from mistapi.exceptions.api_v_1_sites_anomaly_client_metric_401_error_exception import ApiV1SitesAnomalyClientMetric401ErrorException
from mistapi.exceptions.api_v_1_sites_anomaly_client_metric_403_error_exception import ApiV1SitesAnomalyClientMetric403ErrorException
from mistapi.exceptions.api_v_1_sites_anomaly_client_metric_404_error_exception import ApiV1SitesAnomalyClientMetric404ErrorException
from mistapi.exceptions.api_v_1_sites_anomaly_device_metric_401_error_exception import ApiV1SitesAnomalyDeviceMetric401ErrorException
from mistapi.exceptions.api_v_1_sites_anomaly_device_metric_403_error_exception import ApiV1SitesAnomalyDeviceMetric403ErrorException
from mistapi.exceptions.api_v_1_sites_anomaly_device_metric_404_error_exception import ApiV1SitesAnomalyDeviceMetric404ErrorException
from mistapi.exceptions.api_v_1_sites_anomaly_401_error_exception import ApiV1SitesAnomaly401ErrorException
from mistapi.exceptions.api_v_1_sites_anomaly_403_error_exception import ApiV1SitesAnomaly403ErrorException
from mistapi.exceptions.api_v_1_sites_anomaly_404_error_exception import ApiV1SitesAnomaly404ErrorException


class SitesAnomalyController(BaseController):

    """A Controller to access Endpoints in the mistapi API."""
    def __init__(self, config):
        super(SitesAnomalyController, self).__init__(config)

    def get_site_anomaly_events_for_client(self,
                                           site_id,
                                           client_mac,
                                           metric):
        """Does a GET request to /api/v1/sites/{site_id}/anomaly/client/{client_mac}/{metric}.

        Get Client Anomaly Events

        Args:
            site_id (uuid|string): TODO: type description here.
            client_mac (string): TODO: type description here.
            metric (string): see /api/v1/const/insight_metrics for available
                metrics

        Returns:
            AnomalyMetrics: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/api/v1/sites/{site_id}/anomaly/client/{client_mac}/{metric}')
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
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('global'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(AnomalyMetrics.from_dictionary)
            .local_error('400', 'The API endpoint exists but its syntax/payload is incorrect, detail may be given', APIException)
            .local_error('401', 'Unauthorized', ApiV1SitesAnomalyClientMetric401ErrorException)
            .local_error('403', 'Permission Denied', ApiV1SitesAnomalyClientMetric403ErrorException)
            .local_error('404', 'Not found. The API endpoint doesn\'t exist or resource doesn\'t exist', ApiV1SitesAnomalyClientMetric404ErrorException)
        ).execute()

    def get_site_anomaly_eventsfor_device(self,
                                          site_id,
                                          metric,
                                          device_mac):
        """Does a GET request to /api/v1/sites/{site_id}/anomaly/device/{device_mac}/{metric}.

        Get Device Anomaly Events

        Args:
            site_id (uuid|string): TODO: type description here.
            metric (string): see /api/v1/const/insight_metrics for available
                metrics
            device_mac (string): TODO: type description here.

        Returns:
            AnomalyMetrics: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/api/v1/sites/{site_id}/anomaly/device/{device_mac}/{metric}')
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
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('global'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(AnomalyMetrics.from_dictionary)
            .local_error('400', 'The API endpoint exists but its syntax/payload is incorrect, detail may be given', APIException)
            .local_error('401', 'Unauthorized', ApiV1SitesAnomalyDeviceMetric401ErrorException)
            .local_error('403', 'Permission Denied', ApiV1SitesAnomalyDeviceMetric403ErrorException)
            .local_error('404', 'Not found. The API endpoint doesn\'t exist or resource doesn\'t exist', ApiV1SitesAnomalyDeviceMetric404ErrorException)
        ).execute()

    def get_site_anomaly_events(self,
                                site_id,
                                metric):
        """Does a GET request to /api/v1/sites/{site_id}/anomaly/{metric}.

        Get Site Anomaly Events

        Args:
            site_id (uuid|string): TODO: type description here.
            metric (string): see /api/v1/const/insight_metrics for available
                metrics

        Returns:
            AnomalyMetrics: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/api/v1/sites/{site_id}/anomaly/{metric}')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('site_id')
                            .value(site_id)
                            .should_encode(True))
            .template_param(Parameter()
                            .key('metric')
                            .value(metric)
                            .should_encode(True))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('global'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(AnomalyMetrics.from_dictionary)
            .local_error('400', 'The API endpoint exists but its syntax/payload is incorrect, detail may be given', APIException)
            .local_error('401', 'Unauthorized', ApiV1SitesAnomaly401ErrorException)
            .local_error('403', 'Permission Denied', ApiV1SitesAnomaly403ErrorException)
            .local_error('404', 'Not found. The API endpoint doesn\'t exist or resource doesn\'t exist', ApiV1SitesAnomaly404ErrorException)
        ).execute()