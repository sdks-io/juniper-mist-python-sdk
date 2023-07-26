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
from mistapi.models.api_v_1_msps_insights_response import ApiV1MspsInsightsResponse
from mistapi.exceptions.api_exception import APIException
from mistapi.exceptions.api_v_1_msps_insights_401_error_exception import ApiV1MspsInsights401ErrorException
from mistapi.exceptions.api_v_1_msps_insights_403_error_exception import ApiV1MspsInsights403ErrorException
from mistapi.exceptions.api_v_1_msps_insights_404_error_exception import ApiV1MspsInsights404ErrorException


class MspsSLEsController(BaseController):

    """A Controller to access Endpoints in the mistapi API."""
    def __init__(self, config):
        super(MspsSLEsController, self).__init__(config)

    def get_msp_sle(self,
                    msp_id,
                    metric,
                    sle=None,
                    duration='1d',
                    interval=None,
                    start=0,
                    end=0):
        """Does a GET request to /api/v1/msps/{msp_id}/insights/{metric}.

        Get MSP SLEs (all/worst Orgs ...)

        Args:
            msp_id (uuid|string): TODO: type description here.
            metric (string): see /api/v1/const/insight_metrics for available
                metrics
            sle (string, optional): see /api/v1/const/insight_metrics for more
                details
            duration (string, optional): For historical stats and/or logs
                where time range is needed, you can specify the time range in
                a few different ways:   * ?start=1430000000&end=1430864000
                specify the start / end   * ?end=1430864000&duration=1d
                specify end time and duration   * ?duration=1d specify
                duration, end will be now() in seconds
            interval (string, optional): Aggregation works by giving a time
                range plus interval (e.g. 1d, 1h, 10m) where aggregation
                function would be applied to.
            start (int, optional): TODO: type description here. Example: 0
            end (int, optional): TODO: type description here. Example: 0

        Returns:
            ApiV1MspsInsightsResponse: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/api/v1/msps/{msp_id}/insights/{metric}')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('msp_id')
                            .value(msp_id)
                            .should_encode(True))
            .template_param(Parameter()
                            .key('metric')
                            .value(metric)
                            .should_encode(True))
            .query_param(Parameter()
                         .key('sle')
                         .value(sle))
            .query_param(Parameter()
                         .key('duration')
                         .value(duration))
            .query_param(Parameter()
                         .key('interval')
                         .value(interval))
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
            .deserialize_into(ApiV1MspsInsightsResponse.from_dictionary)
            .local_error('400', 'The API endpoint exists but its syntax/payload is incorrect, detail may be given', APIException)
            .local_error('401', 'Unauthorized', ApiV1MspsInsights401ErrorException)
            .local_error('403', 'Permission Denied', ApiV1MspsInsights403ErrorException)
            .local_error('404', 'Not found. The API endpoint doesn\'t exist or resource doesn\'t exist', ApiV1MspsInsights404ErrorException)
        ).execute()