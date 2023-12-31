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
from mistapi.models.session_1 import Session1
from mistapi.exceptions.api_exception import APIException
from mistapi.exceptions.api_v_1_sites_devices_clear_arp_401_error_exception import ApiV1SitesDevicesClearArp401ErrorException
from mistapi.exceptions.api_v_1_sites_devices_clear_arp_403_error_exception import ApiV1SitesDevicesClearArp403ErrorException
from mistapi.exceptions.api_v_1_sites_devices_clear_arp_404_error_exception import ApiV1SitesDevicesClearArp404ErrorException
from mistapi.exceptions.api_v_1_sites_devices_clear_bgp_401_error_exception import ApiV1SitesDevicesClearBgp401ErrorException
from mistapi.exceptions.api_v_1_sites_devices_clear_bgp_403_error_exception import ApiV1SitesDevicesClearBgp403ErrorException
from mistapi.exceptions.api_v_1_sites_devices_clear_bgp_404_error_exception import ApiV1SitesDevicesClearBgp404ErrorException
from mistapi.exceptions.api_v_1_sites_devices_release_dhcp_401_error_exception import ApiV1SitesDevicesReleaseDhcp401ErrorException
from mistapi.exceptions.api_v_1_sites_devices_release_dhcp_403_error_exception import ApiV1SitesDevicesReleaseDhcp403ErrorException
from mistapi.exceptions.api_v_1_sites_devices_release_dhcp_404_error_exception import ApiV1SitesDevicesReleaseDhcp404ErrorException
from mistapi.exceptions.api_v_1_sites_devices_resolve_dns_401_error_exception import ApiV1SitesDevicesResolveDns401ErrorException
from mistapi.exceptions.api_v_1_sites_devices_resolve_dns_403_error_exception import ApiV1SitesDevicesResolveDns403ErrorException
from mistapi.exceptions.api_v_1_sites_devices_resolve_dns_404_error_exception import ApiV1SitesDevicesResolveDns404ErrorException
from mistapi.exceptions.api_v_1_sites_devices_service_ping_401_error_exception import ApiV1SitesDevicesServicePing401ErrorException
from mistapi.exceptions.api_v_1_sites_devices_service_ping_403_error_exception import ApiV1SitesDevicesServicePing403ErrorException
from mistapi.exceptions.api_v_1_sites_devices_service_ping_404_error_exception import ApiV1SitesDevicesServicePing404ErrorException
from mistapi.exceptions.api_v_1_sites_devices_show_route_401_error_exception import ApiV1SitesDevicesShowRoute401ErrorException
from mistapi.exceptions.api_v_1_sites_devices_show_route_403_error_exception import ApiV1SitesDevicesShowRoute403ErrorException
from mistapi.exceptions.api_v_1_sites_devices_show_route_404_error_exception import ApiV1SitesDevicesShowRoute404ErrorException
from mistapi.exceptions.api_v_1_sites_devices_show_service_path_401_error_exception import ApiV1SitesDevicesShowServicePath401ErrorException
from mistapi.exceptions.api_v_1_sites_devices_show_service_path_403_error_exception import ApiV1SitesDevicesShowServicePath403ErrorException
from mistapi.exceptions.api_v_1_sites_devices_show_service_path_404_error_exception import ApiV1SitesDevicesShowServicePath404ErrorException
from mistapi.exceptions.api_v_1_sites_devices_show_session_401_error_exception import ApiV1SitesDevicesShowSession401ErrorException
from mistapi.exceptions.api_v_1_sites_devices_show_session_403_error_exception import ApiV1SitesDevicesShowSession403ErrorException
from mistapi.exceptions.api_v_1_sites_devices_show_session_404_error_exception import ApiV1SitesDevicesShowSession404ErrorException


class SitesDevicesWANController(BaseController):

    """A Controller to access Endpoints in the mistapi API."""
    def __init__(self, config):
        super(SitesDevicesWANController, self).__init__(config)

    def clear_site_ssr_arp_cache(self,
                                 site_id,
                                 device_id,
                                 body=None):
        """Does a POST request to /api/v1/sites/{site_id}/devices/{device_id}/clear_arp.

        Clear the entire ARP cache or a subset if arguments are provided.
        *Note*: port_id is optional if neither vlan nor ip is specified

        Args:
            site_id (uuid|string): TODO: type description here.
            device_id (uuid|string): TODO: type description here.
            body (ApiV1SitesDevicesClearArpRequest, optional): TODO: type
                description here.

        Returns:
            Session1: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/api/v1/sites/{site_id}/devices/{device_id}/clear_arp')
            .http_method(HttpMethodEnum.POST)
            .template_param(Parameter()
                            .key('site_id')
                            .value(site_id)
                            .should_encode(True))
            .template_param(Parameter()
                            .key('device_id')
                            .value(device_id)
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
            .deserialize_into(Session1.from_dictionary)
            .local_error('400', 'port_id must be specified with vlan or ip Both vlan and ip cannot be specified', APIException)
            .local_error('401', 'Unauthorized', ApiV1SitesDevicesClearArp401ErrorException)
            .local_error('403', 'Permission Denied', ApiV1SitesDevicesClearArp403ErrorException)
            .local_error('404', 'Not found. The API endpoint doesn\'t exist or resource doesn\'t exist', ApiV1SitesDevicesClearArp404ErrorException)
        ).execute()

    def clear_site_ssr_bgp_routes(self,
                                  site_id,
                                  device_id,
                                  body=None):
        """Does a POST request to /api/v1/sites/{site_id}/devices/{device_id}/clear_bgp.

        Clear routes associated with one or all BGP neighbors

        Args:
            site_id (uuid|string): TODO: type description here.
            device_id (uuid|string): TODO: type description here.
            body (ApiV1SitesDevicesClearBgpRequest, optional): TODO: type
                description here.

        Returns:
            Session1: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/api/v1/sites/{site_id}/devices/{device_id}/clear_bgp')
            .http_method(HttpMethodEnum.POST)
            .template_param(Parameter()
                            .key('site_id')
                            .value(site_id)
                            .should_encode(True))
            .template_param(Parameter()
                            .key('device_id')
                            .value(device_id)
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
            .deserialize_into(Session1.from_dictionary)
            .local_error('400', 'parameter neighbor absent', APIException)
            .local_error('401', 'Unauthorized', ApiV1SitesDevicesClearBgp401ErrorException)
            .local_error('403', 'Permission Denied', ApiV1SitesDevicesClearBgp403ErrorException)
            .local_error('404', 'Not found. The API endpoint doesn\'t exist or resource doesn\'t exist', ApiV1SitesDevicesClearBgp404ErrorException)
        ).execute()

    def release_site_ssr_dhcp_lease(self,
                                    site_id,
                                    device_id,
                                    body=None):
        """Does a POST request to /api/v1/sites/{site_id}/devices/{device_id}/release_dhcp.

        Releases an active DHCP lease.

        Args:
            site_id (uuid|string): TODO: type description here.
            device_id (uuid|string): TODO: type description here.
            body (ApiV1SitesDevicesReleaseDhcpRequest, optional): TODO: type
                description here.

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
            .path('/api/v1/sites/{site_id}/devices/{device_id}/release_dhcp')
            .http_method(HttpMethodEnum.POST)
            .template_param(Parameter()
                            .key('site_id')
                            .value(site_id)
                            .should_encode(True))
            .template_param(Parameter()
                            .key('device_id')
                            .value(device_id)
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
            .local_error('400', 'Parameter `port ` absent', APIException)
            .local_error('401', 'Unauthorized', ApiV1SitesDevicesReleaseDhcp401ErrorException)
            .local_error('403', 'Permission Denied', ApiV1SitesDevicesReleaseDhcp403ErrorException)
            .local_error('404', 'Not found. The API endpoint doesn\'t exist or resource doesn\'t exist', ApiV1SitesDevicesReleaseDhcp404ErrorException)
        ).execute()

    def test_site_ssr_dns_resolution(self,
                                     site_id,
                                     device_id):
        """Does a POST request to /api/v1/sites/{site_id}/devices/{device_id}/resolve_dns.

        DNS resolutions are performed on the Device. The output will be
        available through websocket. As there can be multiple command issued
        against the same SSR at the same time and the output all goes through
        the same websocket stream, `session` is used for demux.
         
         #### Subscribe to Device Command outputs
        `WS /api-ws/v1/stream`
        ```json
        {
            "subscribe": "/sites/{site_id}/devices/{device_id}/cmd"
        }
        ```
        ##### Example output from ws stream
        ```
         Router      | Hostname               | Resolved | Last Resolved      
         | Expiration
        -------------|------------------------|----------|---------------------
        -|---------------------
         test-device | xxx.yyy.net            | Y        |
         2022-03-28T03:56:49Z | 2022-03-28T03:57:49Z
        ```

        Args:
            site_id (uuid|string): TODO: type description here.
            device_id (uuid|string): TODO: type description here.

        Returns:
            Session1: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/api/v1/sites/{site_id}/devices/{device_id}/resolve_dns')
            .http_method(HttpMethodEnum.POST)
            .template_param(Parameter()
                            .key('site_id')
                            .value(site_id)
                            .should_encode(True))
            .template_param(Parameter()
                            .key('device_id')
                            .value(device_id)
                            .should_encode(True))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('global'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(Session1.from_dictionary)
            .local_error('400', 'The API endpoint exists but its syntax/payload is incorrect, detail may be given', APIException)
            .local_error('401', 'Unauthorized', ApiV1SitesDevicesResolveDns401ErrorException)
            .local_error('403', 'Permission Denied', ApiV1SitesDevicesResolveDns403ErrorException)
            .local_error('404', 'Not found. The API endpoint doesn\'t exist or resource doesn\'t exist', ApiV1SitesDevicesResolveDns404ErrorException)
        ).execute()

    def service_ping_from_ssr(self,
                              site_id,
                              device_id,
                              body=None):
        """Does a POST request to /api/v1/sites/{site_id}/devices/{device_id}/service_ping.

        Ping from SSR
        Service Ping can be performed from the Device. The output will be
        available through websocket. As there can be multiple command issued
        against the same device at the same time and the output all goes
        through the same websocket stream, session is introduced for demux.
        #### Subscribe to Device Command outputs
        `WS /api-ws/v1/stream`
        ```json
        {
            "subscribe": "/sites/{site_id}/devices/{device_id}/cmd"
        }
        ```
        ##### Example output from ws stream
        ```json
        {
            "event": "data",
            "channel":
            "/sites/4ac1dcf4-9d8b-7211-65c4-057819f0862b/devices/00000000-0000-
            0000-1000-5c5b350e0060/cmd",
            "data": {
                "session": "session_id",
                "raw": "64 bytes from 23.211.0.110: seq=8 ttl=58 time=12.323
                ms\n"
            }
        }
        ```

        Args:
            site_id (uuid|string): TODO: type description here.
            device_id (uuid|string): TODO: type description here.
            body (ApiV1SitesDevicesServicePingRequest, optional): Request
                Body

        Returns:
            Session1: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/api/v1/sites/{site_id}/devices/{device_id}/service_ping')
            .http_method(HttpMethodEnum.POST)
            .template_param(Parameter()
                            .key('site_id')
                            .value(site_id)
                            .should_encode(True))
            .template_param(Parameter()
                            .key('device_id')
                            .value(device_id)
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
            .deserialize_into(Session1.from_dictionary)
            .local_error('400', 'The API endpoint exists but its syntax/payload is incorrect, detail may be given', APIException)
            .local_error('401', 'Unauthorized', ApiV1SitesDevicesServicePing401ErrorException)
            .local_error('403', 'Permission Denied', ApiV1SitesDevicesServicePing403ErrorException)
            .local_error('404', 'Not found. The API endpoint doesn\'t exist or resource doesn\'t exist', ApiV1SitesDevicesServicePing404ErrorException)
        ).execute()

    def get_site_ssr_and_srx_routes(self,
                                    site_id,
                                    device_id,
                                    body=None):
        """Does a POST request to /api/v1/sites/{site_id}/devices/{device_id}/show_route.

        Get routes from the Device. The output will be available through
        websocket. As there can be multiple command issued against the same
        device at the same time and the output all goes through the same
        websocket stream, `session` is introduced for demux.
        #### Subscribe to Device Command outputs
        `WS /api-ws/v1/stream`
        ```json
        {
            "subscribe": "/sites/{site_id}/devices/{device_id}/cmd"
        }
        ```
        ##### Example output from ws stream
        ```
        admin@labsystem1.fiedler# show bgp neighbors
        BGP neighbor is 192.168.4.1, remote AS 4200000001, local AS
        4200000128, external
        link
          BGP version 4, remote router ID 1.1.1.1
          BGP state = Established, up for 00:27:25
          Last read 00:00:25, hold time is 90, keepalive interval is 30
          seconds
          Configured hold time is 90, keepalive interval is 30 seconds
          Neighbor capabilities:
            4 Byte AS: advertised and received
            Route refresh: advertised and received(old &amp; new)
            Address family IPv4 Unicast: advertised and received
            Graceful Restart Capabilty: advertised and received
              Remote Restart timer is 120 seconds
              Address families by peer:
                none
                ...
        ```

        Args:
            site_id (uuid|string): TODO: type description here.
            device_id (uuid|string): TODO: type description here.
            body (ApiV1SitesDevicesShowRouteRequest, optional): all attributes
                are optional

        Returns:
            Session1: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/api/v1/sites/{site_id}/devices/{device_id}/show_route')
            .http_method(HttpMethodEnum.POST)
            .template_param(Parameter()
                            .key('site_id')
                            .value(site_id)
                            .should_encode(True))
            .template_param(Parameter()
                            .key('device_id')
                            .value(device_id)
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
            .deserialize_into(Session1.from_dictionary)
            .local_error('400', 'The API endpoint exists but its syntax/payload is incorrect, detail may be given', APIException)
            .local_error('401', 'Unauthorized', ApiV1SitesDevicesShowRoute401ErrorException)
            .local_error('403', 'Permission Denied', ApiV1SitesDevicesShowRoute403ErrorException)
            .local_error('404', 'Not found. The API endpoint doesn\'t exist or resource doesn\'t exist', ApiV1SitesDevicesShowRoute404ErrorException)
        ).execute()

    def get_site_ssr_service_path(self,
                                  site_id,
                                  device_id,
                                  body=None):
        """Does a POST request to /api/v1/sites/{site_id}/devices/{device_id}/show_service_path.

        Get service path information of the Device. The output will be
        available through websocket. As there can be multiple command issued
        against the same device at the same time and the output all goes
        through the same websocket stream, session is introduced for demux.
        #### Subscribe to Device Command outputs
        `WS /api-ws/v1/stream`
        ```json
        {
            "subscribe": "/sites/{site_id}/devices/{device_id}/cmd"
        }
        ```
        ##### Example output from ws stream
        ```
        show service-path
        Service    Service-route     Type              Destination  Next-Hop 
        Interface  Vector  Cost  Rate  Capacity        State
        Web        web-route1        service-agent     4.4.4.4      1.1.1.2   
        lan        red     10    1    200/3000       Up*
        Web        web-route1        service-agent     4.4.4.4      1.1.1.3   
        lan        red     10    1    200/3000       Up
        Web        web-route2        service-agent     5.5.5.5      2.2.2.2   
        lan       blue     20    2    50/unlimited   Down
        Login      <None>            BgpOverSVR        10.1.1.1     1.2.3.4   
        wan        red     10    3        -          Up
        Login      <None>            BgpOverSVR        11.1.1.1     1.2.3.4   
        wan        red     10    1        -          Up
        App1       <None>            Routed                -           -      
        -          -      -     -        -          -
        App1       learned-routed    Routed                -           -      
        -          -      -     -        -          -
        ```

        Args:
            site_id (uuid|string): TODO: type description here.
            device_id (uuid|string): TODO: type description here.
            body (ApiV1SitesDevicesShowServicePathRequest, optional): TODO:
                type description here.

        Returns:
            Session1: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/api/v1/sites/{site_id}/devices/{device_id}/show_service_path')
            .http_method(HttpMethodEnum.POST)
            .template_param(Parameter()
                            .key('site_id')
                            .value(site_id)
                            .should_encode(True))
            .template_param(Parameter()
                            .key('device_id')
                            .value(device_id)
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
            .deserialize_into(Session1.from_dictionary)
            .local_error('400', 'The API endpoint exists but its syntax/payload is incorrect, detail may be given', APIException)
            .local_error('401', 'Unauthorized', ApiV1SitesDevicesShowServicePath401ErrorException)
            .local_error('403', 'Permission Denied', ApiV1SitesDevicesShowServicePath403ErrorException)
            .local_error('404', 'Not found. The API endpoint doesn\'t exist or resource doesn\'t exist', ApiV1SitesDevicesShowServicePath404ErrorException)
        ).execute()

    def get_site_ssr_and_srx_sessions(self,
                                      site_id,
                                      device_id,
                                      body=None):
        """Does a POST request to /api/v1/sites/{site_id}/devices/{device_id}/show_session.

        Get active sessions passing through the Device. The output will be
        available through websocket. As there can be multiple command issued
        against the same device at the same time and the output all goes
        through the same websocket stream, session is introduced for demux.
        #### Subscribe to Device Command outputs
        `WS /api-ws/v1/stream`
        ```json
        {
            "subscribe": "/sites/{site_id}/devices/{device_id}/cmd"
        }
        ```
        ##### Example output from ws stream
        ```
        admin@ssr.node# show sessions
        Fri 2020-04-17 16:55:34 UTC
        Node: node1
        ====================================== ===== ============= ===========
        ========== ====== ======= ================= ==========
        ================= =========== ================= ==========
        =================== ========= =================
         Session Id                             Dir   Service       Tenant    
         Dev Name   VLAN   Proto   Src IP            Src Port   Dest IP       
         Dest Port   NAT IP            NAT Port   Payload Encrypted   Timeout 
         Uptime
        ====================================== ===== ============= ===========
        ========== ====== ======= ================= ==========
        ================= =========== ================= ==========
        =================== ========= =================
         01187fb8-765a-45e5-ae90-37d77f15e292   fwd   Internet      lanSubnet 
         lan           0   udp     192.168.0.28         44674   35.166.173.18 
         9930   96.230.191.130       19569   false                   154   0
         days  0:00:28
         01187fb8-765a-45e5-ae90-37d77f15e292   rev   Internet      lanSubnet 
         wan           0   udp     35.166.173.18         9930   96.230.191.130
         19569   0.0.0.0                  0   false                   154   0
         days  0:00:28
         0859a4ae-bcff-4aa6-b812-79a5236a6c13   fwd   Internet      lanSubnet 
         lan           0   tcp     192.168.0.41         60843   17.249.171.246
         443   96.230.191.130       51941   false                     2   0
         days  0:00:10
        ```

        Args:
            site_id (uuid|string): TODO: type description here.
            device_id (string): TODO: type description here.
            body (ApiV1SitesDevicesShowSessionRequest, optional): TODO: type
                description here.

        Returns:
            Session1: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/api/v1/sites/{site_id}/devices/{device_id}/show_session')
            .http_method(HttpMethodEnum.POST)
            .template_param(Parameter()
                            .key('site_id')
                            .value(site_id)
                            .should_encode(True))
            .template_param(Parameter()
                            .key('device_id')
                            .value(device_id)
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
            .deserialize_into(Session1.from_dictionary)
            .local_error('400', 'The API endpoint exists but its syntax/payload is incorrect, detail may be given', APIException)
            .local_error('401', 'Unauthorized', ApiV1SitesDevicesShowSession401ErrorException)
            .local_error('403', 'Permission Denied', ApiV1SitesDevicesShowSession403ErrorException)
            .local_error('404', 'Not found. The API endpoint doesn\'t exist or resource doesn\'t exist', ApiV1SitesDevicesShowSession404ErrorException)
        ).execute()
