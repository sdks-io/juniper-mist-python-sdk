# -*- coding: utf-8 -*-

"""
mistapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

from deprecation import deprecated
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
from mistapi.exceptions.api_exception import APIException
from mistapi.exceptions.api_v_1_sites_devices_ha_401_error_exception import ApiV1SitesDevicesHa401ErrorException
from mistapi.exceptions.api_v_1_sites_devices_ha_403_error_exception import ApiV1SitesDevicesHa403ErrorException
from mistapi.exceptions.api_v_1_sites_devices_ha_404_error_exception import ApiV1SitesDevicesHa404ErrorException


class SitesDevicesWANHAController(BaseController):

    """A Controller to access Endpoints in the mistapi API."""
    def __init__(self, config):
        super(SitesDevicesWANHAController, self).__init__(config)

    def delete_site_device_ha_cluster(self,
                                      site_id,
                                      device_id):
        """Does a DELETE request to /api/v1/sites/{site_id}/devices/{device_id}/ha.

        Delete HA Cluster

        Args:
            site_id (uuid|string): TODO: type description here.
            device_id (uuid|string): TODO: type description here.

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
            .path('/api/v1/sites/{site_id}/devices/{device_id}/ha')
            .http_method(HttpMethodEnum.DELETE)
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
            .local_error('400', 'The API endpoint exists but its syntax/payload is incorrect, detail may be given', APIException)
            .local_error('401', 'Unauthorized', ApiV1SitesDevicesHa401ErrorException)
            .local_error('403', 'Permission Denied', ApiV1SitesDevicesHa403ErrorException)
            .local_error('404', 'Not found. The API endpoint doesn\'t exist or resource doesn\'t exist', ApiV1SitesDevicesHa404ErrorException)
        ).execute()

    def create_site_device_ha_cluster(self,
                                      site_id,
                                      device_id,
                                      body=None):
        """Does a POST request to /api/v1/sites/{site_id}/devices/{device_id}/ha.

        Create HA Cluster
        Both nodes has to be in the same site. We expect the user to configure
        ha_sync / ha_data port in port_configs already
        ### SRX cabling
        see [Chassis Cluster User Guide for SRX Series
        Devices](https://www.juniper.net/documentation/us/en/software/junos/cha
        ssis-cluster-security-devices/topics/concept/chassis-cluster-srx-series
        -node-interface-understanding.html) Here’s the recommended cabling.
        #### SRX300
        From ZTP / default state, ge-0/0/0 and ge-0/0/7 (SFP) are default WAN
        ports and will get DHCP IP. However, ge-0/0/0 becomes OOB/fxp0 after
        cluster is enabled (i.e. using it for reach Mist is not recommended)
        1.  form cluster in UI
        2.  configure ge-0/0/7,ge-1/0/7 for WAN (reth0)
        3.  configure ge-0/0/2,ge-1/0/2 for ha_data
        4.  configure ge-0/0/3- for LAN or additional WAN e.g.
            
        ``` json
        {
            "port_config": {
                "ge-0/0/2,ge-1/0/2": {
                    "usage": "ha_data"
                },
                "ge-0/0/7,ge-1/0/7": {
                    "usage": "wan",
                    "redundant": true,
                    "reth_idx": 0,
                    "ip_config": {"type": "dhcp"}
                },
            }
        }
        ```
        1.  connect ge-0/0/1 back to back for ha_control
        2.  connect ge-0/0/2 back to back for ha_data
        3.  connect both ge-0/0/7 to uplink switch to WAN and to reach Mist
        4.  power up both devices
        5.  it takes about 30 minutes for the cluster to form
            
        #### SRX320
        From ZTP / default state, ge-0/0/0, ge-0/0/7 (SFP) and cl-1/0/0 (LTE)
        are default WAN ports and will get DHCP IP. However, ge-0/0/0 becomes
        OOB/fxp0 after cluster is enabled (i.e. using it for reach Mist is not
        recommended)
        ##### ZTP via ge-0/0/7
        Similar to SRX300
        ##### ZTP via cl-1/0/0 (LTE)
        1.  form cluster in UI
        2.  configure cl-1/0/0, cl-3/0/0 as WAN (reth0)
        3.  configure ge-0/0/2,ge-3/0/2 for ha_data
        4.  same as above
            
        #### SRX340 / SRX345 / SRX380
        SRX340/SRX345 has dedicated OOB/fxp0 ports
        1.  form cluster in UI
        2.  configure ge-0/0/0,ge-5/0/0 for WAN (reth0)
        3.  configure ge-0/0/2,ge-5/0/2 for ha_data
        4.  configure ge-0/0/3- for LAN or additional WAN
        5.  connect ge-0/0/0 to uplink switch to WAN and to reach Mist
        6.  connect ge-0/0/1 back-to-back for ha_control
        7.  connect ge-0/0/2 back-to-back for ha_data (fabric); or for SRX380,
        xe-0/0/16 if 10G SFP+ is used
        8.  connect ge-0/0/3- to LAN or additional WANs
            
        #### SRX550
        ge-0/0/0 becomes OOB/fxp0 after cluster is enabled, make suenable
        oob_ip_config as dhcp to maintain cloud connectivity
        1.  connect ge-0/0/0 to reach Mist (after cluster is fully up, this
        port becomes OOB/fxp0)
        2.  connect ge-0/0/1 back-to-back for ha_control
        3.  connect ge-0/0/2 back-to-back for ha_data (fabric)
        4.  connect ge-0/0/3 to WAN (after cluster is up, intended to be used
        for reth0)
        5.  connect ge-0/0/4- to LAN or additional WANs
            
        #### SRX1500
        SRX1500 has, additionally, dedicated HA Control port
        1.  form cluster in UI
        2.  configure ge-0/0/0,ge-5/0/0 for WAN (reth0)
        3.  configure ge-0/0/1,ge-5/0/1 for ha_data
        4.  configure ge-0/0/2- for LAN or additional WAN
        5.  connect dedicated ha_control back-to-back
        6.  connect ge-0/0/0 to uplink switch to WAN and to reach Mist
        7.  connect ge-0/0/1 back-to-back for ha_data
        8.  connect ge-0/0/2- to LAN or additional WANs
            
        #### SRX4100
        SRX4100 has dedicated ha_control and ha_data (fabric) ports
        1.  connect dedicated ha_control back-to-back
        2.  connect dedicated ha_data back-to-back
        3.  connect xe-0/0/0 to WAN to reach Mist
        4.  connect xe-0/0/1- to LAN or additional WANs
            
        #### VSRX
        When standalone, VSRX has fxp0 as first Network Adapter, then
        ge-0/0/0-N When clustered, VSRX has fxp0, em0, then ge-0/0/0-N
        1.  connect net0 (fxp0) to WAN to reach Mist
        2.  connect net1 back-to-back for ha_control
        3.  connect net2 (ge-0/0/0) back-to-back for ha_data (fab0/fab1)
        4.  connect net3 (ge-0/0/1) to WAN, intended to be used for reth0
        5.  connect net4 (ge-0/0/2) to LAN
            
        SRX340/SRX345 has dedicated OOB/fxp0 ports VSRX has fxp0 as first
        Network Adapter, then ge-0/0/0-N
        1.  connect ge-0/0/0 to WAN to reach Mist
        2.  connect ge-0/0/1 back-to-back for ha_control
        3.  connect ge-0/0/2 back-to-back for ha_data (fabric); or for SRX380,
        xe-0/0/16 if 10G SFP+ is used
        4.  connect ge-0/0/3- to LAN or additional WANs
            
        #### SRX550
        ge-0/0/0 becomes OOB/fxp0 after cluster is enabled, make suenable
        oob_ip_config as dhcp to maintain cloud connectivity
        1.  connect ge-0/0/0 to reach Mist (after cluster is fully up, this
        port becomes OOB/fxp0)
        2.  connect ge-0/0/1 back-to-back for ha_control
        3.  connect ge-0/0/2 back-to-back for ha_data (fabric)
        4.  connect ge-0/0/3 to WAN (after cluster is up, intended to be used
        for reth0)
        5.  connect ge-0/0/4- to LAN or additional WANs
            
        #### SRX1500
        SRX1500 has, additionally, dedicated HA Control port
        1.  connect dedicated ha_control back-to-back
        2.  connect ge-0/0/0 to WAN to reach mist
        3.  connect ge-0/0/1 back-to-back for ha_data
        4.  connect ge-0/0/2- to LAN or additional WANs
            
        #### SRX4100
        SRX4100 has dedicated ha_control and ha_data (fabric) ports
        1.  connect dedicated ha_control back-to-back
        2.  connect dedicated ha_data back-to-back
        3.  connect xe-0/0/0 to WAN to reach Mist
        4.  connect xe-0/0/1- to LAN or additional WANs

        Args:
            site_id (uuid|string): TODO: type description here.
            device_id (uuid|string): TODO: type description here.
            body (ApiV1SitesDevicesHaRequest, optional): TODO: type
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
            .path('/api/v1/sites/{site_id}/devices/{device_id}/ha')
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
            .local_error('400', 'The API endpoint exists but its syntax/payload is incorrect, detail may be given', APIException)
            .local_error('401', 'Unauthorized', ApiV1SitesDevicesHa401ErrorException)
            .local_error('403', 'Permission Denied', ApiV1SitesDevicesHa403ErrorException)
            .local_error('404', 'Not found. The API endpoint doesn\'t exist or resource doesn\'t exist', ApiV1SitesDevicesHa404ErrorException)
        ).execute()

    @deprecated()
    def swap_site_device_ha_cluster_node(self,
                                         site_id,
                                         device_id,
                                         body=None):
        """Does a PUT request to /api/v1/sites/{site_id}/devices/{device_id}/ha.

        Swap nodes on the HA Cluster

        Args:
            site_id (uuid|string): TODO: type description here.
            device_id (uuid|string): TODO: type description here.
            body (ApiV1SitesDevicesHaRequest1, optional): TODO: type
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
            .path('/api/v1/sites/{site_id}/devices/{device_id}/ha')
            .http_method(HttpMethodEnum.PUT)
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
            .local_error('400', 'The API endpoint exists but its syntax/payload is incorrect, detail may be given', APIException)
            .local_error('401', 'Unauthorized', ApiV1SitesDevicesHa401ErrorException)
            .local_error('403', 'Permission Denied', ApiV1SitesDevicesHa403ErrorException)
            .local_error('404', 'Not found. The API endpoint doesn\'t exist or resource doesn\'t exist', ApiV1SitesDevicesHa404ErrorException)
        ).execute()
