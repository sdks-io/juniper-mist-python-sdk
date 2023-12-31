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
from mistapi.models.webhook import Webhook
from mistapi.models.webhook_delivery_search import WebhookDeliverySearch
from mistapi.exceptions.api_exception import APIException
from mistapi.exceptions.api_v_1_sites_webhooks_401_error_exception import ApiV1SitesWebhooks401ErrorException
from mistapi.exceptions.api_v_1_sites_webhooks_403_error_exception import ApiV1SitesWebhooks403ErrorException
from mistapi.exceptions.api_v_1_sites_webhooks_404_error_exception import ApiV1SitesWebhooks404ErrorException
from mistapi.exceptions.api_v_1_sites_webhooks_400_error_exception import ApiV1SitesWebhooks400ErrorException
from mistapi.exceptions.api_v_1_sites_webhooks_events_search_401_error_exception import ApiV1SitesWebhooksEventsSearch401ErrorException
from mistapi.exceptions.api_v_1_sites_webhooks_events_search_403_error_exception import ApiV1SitesWebhooksEventsSearch403ErrorException
from mistapi.exceptions.api_v_1_sites_webhooks_events_search_404_error_exception import ApiV1SitesWebhooksEventsSearch404ErrorException
from mistapi.exceptions.api_v_1_sites_webhooks_ping_401_error_exception import ApiV1SitesWebhooksPing401ErrorException
from mistapi.exceptions.api_v_1_sites_webhooks_ping_403_error_exception import ApiV1SitesWebhooksPing403ErrorException
from mistapi.exceptions.api_v_1_sites_webhooks_ping_404_error_exception import ApiV1SitesWebhooksPing404ErrorException


class SitesWebhooksController(BaseController):

    """A Controller to access Endpoints in the mistapi API."""
    def __init__(self, config):
        super(SitesWebhooksController, self).__init__(config)

    def list_site_webhooks(self,
                           site_id):
        """Does a GET request to /api/v1/sites/{site_id}/webhooks.

        Get List of Site Webhooks

        Args:
            site_id (uuid|string): TODO: type description here.

        Returns:
            list of Webhook: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/api/v1/sites/{site_id}/webhooks')
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
            .deserialize_into(Webhook.from_dictionary)
            .local_error('400', 'The API endpoint exists but its syntax/payload is incorrect, detail may be given', APIException)
            .local_error('401', 'Unauthorized', ApiV1SitesWebhooks401ErrorException)
            .local_error('403', 'Permission Denied', ApiV1SitesWebhooks403ErrorException)
            .local_error('404', 'Not found. The API endpoint doesn\'t exist or resource doesn\'t exist', ApiV1SitesWebhooks404ErrorException)
        ).execute()

    def create_site_webhook(self,
                            site_id,
                            body=None):
        """Does a POST request to /api/v1/sites/{site_id}/webhooks.

        Webhook defines a webhook, modeled after [github’s
        model](https://developer.github.com/webhooks/).
        There is two types of webhooks:
        * webhooks
        ([examples](https://www.postman.com/juniper-mist/workspace/mist-systems
        -s-public-workspace/folder/224925-be01e694-7253-4195-8563-78e2a745e114)
        )
        * raw data webhooks
        ([examples](https://www.postman.com/juniper-mist/workspace/mist-systems
        -s-public-workspace/folder/224925-e2d5d5f8-4bdb-4efc-93e4-90f4b33d0b2b)
        )
        ##### Webhooks
        Webhooks can be configured at the org level (subset of topics only)
        and at the site level. It is possible to have multiple topics in the
        same webhook configuration and/or to have multiple webhooks configured
        at the same time.
        ##### Client Raw Data Webhooks
        Raw data webhooks are a special subset of webhooks that provide
        insight into raw data packets emitted by a client, identified by their
        advertising MAC address (assets, discovered ble, connected wifi,
        unconnected wifi). The data that client raw data webhooks encompasses
        are reporting AP information, RSSI Data, and any special
        packets/telemetry packets that the client may emit. Note that client
        raw webhooks are the raw data coming from the client and do not
        contain the X,Y location data of the client. In order to get the
        location data for a client please see our location webhooks. Clients
        can be identified uniquely across these client raw data topics and
        location webhook topic using MAC address as the Unique identifier
        (client identifier).
        ###### Client Raw Data Webhooks Topics
        Topics that correspond to client raw data for different client types.
                * `asset-raw-rssi` - Raw data from packets emitted by named and
        filtered assets 
        * `discovered-raw-rssi` - Raw data from packets emitted by passive BLE
        devices 
        * `wifi-conn-raw` - Raw data from packets emitted by connected devices
                * `wifi-unconn-raw` - Raw data from packets emitted by unconnected
        devices (passive)
        ###### Rules for configuring client raw data webhooks
        1. Only one instance of a webhook object containing a client raw data
        webhook topic is allowed. (a site level entry will override an org
        level entry for the client raw data webhook topic in question)
        2. Only one client raw data webhook topic is allowed per `http-post`
        message to webhooks api

        Args:
            site_id (uuid|string): TODO: type description here.
            body (Webhook, optional): Request Body

        Returns:
            Webhook: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/api/v1/sites/{site_id}/webhooks')
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
            .deserialize_into(Webhook.from_dictionary)
            .local_error('400', 'Bad request', ApiV1SitesWebhooks400ErrorException)
            .local_error('401', 'Unauthorized', ApiV1SitesWebhooks401ErrorException)
            .local_error('403', 'Permission Denied', ApiV1SitesWebhooks403ErrorException)
            .local_error('404', 'Not found. The API endpoint doesn\'t exist or resource doesn\'t exist', ApiV1SitesWebhooks404ErrorException)
        ).execute()

    def delete_site_webhook(self,
                            site_id,
                            webhook_id):
        """Does a DELETE request to /api/v1/sites/{site_id}/webhooks/{webhook_id}.

        Delete Site Webhook

        Args:
            site_id (uuid|string): TODO: type description here.
            webhook_id (uuid|string): TODO: type description here.

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
            .path('/api/v1/sites/{site_id}/webhooks/{webhook_id}')
            .http_method(HttpMethodEnum.DELETE)
            .template_param(Parameter()
                            .key('site_id')
                            .value(site_id)
                            .should_encode(True))
            .template_param(Parameter()
                            .key('webhook_id')
                            .value(webhook_id)
                            .should_encode(True))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('global'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .local_error('400', 'The API endpoint exists but its syntax/payload is incorrect, detail may be given', APIException)
            .local_error('401', 'Unauthorized', ApiV1SitesWebhooks401ErrorException)
            .local_error('403', 'Permission Denied', ApiV1SitesWebhooks403ErrorException)
            .local_error('404', 'Not found. The API endpoint doesn\'t exist or resource doesn\'t exist', ApiV1SitesWebhooks404ErrorException)
        ).execute()

    def get_site_webhook(self,
                         site_id,
                         webhook_id):
        """Does a GET request to /api/v1/sites/{site_id}/webhooks/{webhook_id}.

        Get Site Webhook Details

        Args:
            site_id (uuid|string): TODO: type description here.
            webhook_id (uuid|string): TODO: type description here.

        Returns:
            Webhook: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/api/v1/sites/{site_id}/webhooks/{webhook_id}')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('site_id')
                            .value(site_id)
                            .should_encode(True))
            .template_param(Parameter()
                            .key('webhook_id')
                            .value(webhook_id)
                            .should_encode(True))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('global'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(Webhook.from_dictionary)
            .local_error('400', 'The API endpoint exists but its syntax/payload is incorrect, detail may be given', APIException)
            .local_error('401', 'Unauthorized', ApiV1SitesWebhooks401ErrorException)
            .local_error('403', 'Permission Denied', ApiV1SitesWebhooks403ErrorException)
            .local_error('404', 'Not found. The API endpoint doesn\'t exist or resource doesn\'t exist', ApiV1SitesWebhooks404ErrorException)
        ).execute()

    def update_site_webhook(self,
                            site_id,
                            webhook_id,
                            body=None):
        """Does a PUT request to /api/v1/sites/{site_id}/webhooks/{webhook_id}.

        Update Site Webhook

        Args:
            site_id (uuid|string): TODO: type description here.
            webhook_id (uuid|string): TODO: type description here.
            body (Webhook, optional): Request Body

        Returns:
            Webhook: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/api/v1/sites/{site_id}/webhooks/{webhook_id}')
            .http_method(HttpMethodEnum.PUT)
            .template_param(Parameter()
                            .key('site_id')
                            .value(site_id)
                            .should_encode(True))
            .template_param(Parameter()
                            .key('webhook_id')
                            .value(webhook_id)
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
            .deserialize_into(Webhook.from_dictionary)
            .local_error('400', 'The API endpoint exists but its syntax/payload is incorrect, detail may be given', APIException)
            .local_error('401', 'Unauthorized', ApiV1SitesWebhooks401ErrorException)
            .local_error('403', 'Permission Denied', ApiV1SitesWebhooks403ErrorException)
            .local_error('404', 'Not found. The API endpoint doesn\'t exist or resource doesn\'t exist', ApiV1SitesWebhooks404ErrorException)
        ).execute()

    def search_site_webhooks_deliveries(self,
                                        site_id,
                                        webhook_id,
                                        status_code=None,
                                        error=None,
                                        topic=None,
                                        start=0,
                                        end=0,
                                        duration='1d',
                                        limit=100):
        """Does a GET request to /api/v1/sites/{site_id}/webhooks/{webhook_id}/events/search.

        Search webhooks deliveries
        To get a list of webhook deliveries in error, use the query parameter
        `?error=*`

        Args:
            site_id (uuid|string): TODO: type description here.
            webhook_id (uuid|string): TODO: type description here.
            status_code (int, optional): TODO: type description here.
            error (string, optional): TODO: type description here.
            topic (Topic2Enum, optional): webhook topic
            start (int, optional): TODO: type description here. Example: 0
            end (int, optional): TODO: type description here. Example: 0
            duration (string, optional): For historical stats and/or logs
                where time range is needed, you can specify the time range in
                a few different ways:   * ?start=1430000000&end=1430864000
                specify the start / end   * ?end=1430864000&duration=1d
                specify end time and duration   * ?duration=1d specify
                duration, end will be now() in seconds
            limit (int, optional): TODO: type description here. Example: 100

        Returns:
            WebhookDeliverySearch: Response from the API. Example response

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/api/v1/sites/{site_id}/webhooks/{webhook_id}/events/search')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('site_id')
                            .value(site_id)
                            .should_encode(True))
            .template_param(Parameter()
                            .key('webhook_id')
                            .value(webhook_id)
                            .should_encode(True))
            .query_param(Parameter()
                         .key('status_code')
                         .value(status_code))
            .query_param(Parameter()
                         .key('error')
                         .value(error))
            .query_param(Parameter()
                         .key('topic')
                         .value(topic))
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
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('global'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(WebhookDeliverySearch.from_dictionary)
            .local_error('400', 'The API endpoint exists but its syntax/payload is incorrect, detail may be given', APIException)
            .local_error('401', 'Unauthorized', ApiV1SitesWebhooksEventsSearch401ErrorException)
            .local_error('403', 'Permission Denied', ApiV1SitesWebhooksEventsSearch403ErrorException)
            .local_error('404', 'Not found. The API endpoint doesn\'t exist or resource doesn\'t exist', ApiV1SitesWebhooksEventsSearch404ErrorException)
        ).execute()

    def ping_site_webhook(self,
                          site_id,
                          webhook_id):
        """Does a POST request to /api/v1/sites/{site_id}/webhooks/{webhook_id}/ping.

        send a Ping event to the webhook

        Args:
            site_id (uuid|string): TODO: type description here.
            webhook_id (uuid|string): TODO: type description here.

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
            .path('/api/v1/sites/{site_id}/webhooks/{webhook_id}/ping')
            .http_method(HttpMethodEnum.POST)
            .template_param(Parameter()
                            .key('site_id')
                            .value(site_id)
                            .should_encode(True))
            .template_param(Parameter()
                            .key('webhook_id')
                            .value(webhook_id)
                            .should_encode(True))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('global'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .local_error('400', 'The API endpoint exists but its syntax/payload is incorrect, detail may be given', APIException)
            .local_error('401', 'Unauthorized', ApiV1SitesWebhooksPing401ErrorException)
            .local_error('403', 'Permission Denied', ApiV1SitesWebhooksPing403ErrorException)
            .local_error('404', 'Not found. The API endpoint doesn\'t exist or resource doesn\'t exist', ApiV1SitesWebhooksPing404ErrorException)
        ).execute()
