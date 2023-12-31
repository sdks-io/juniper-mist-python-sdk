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
from mistapi.models.junos_evpn_topology import JunosEvpnTopology
from mistapi.exceptions.api_exception import APIException
from mistapi.exceptions.api_v_1_sites_evpn_topologies_401_error_exception import ApiV1SitesEvpnTopologies401ErrorException
from mistapi.exceptions.api_v_1_sites_evpn_topologies_403_error_exception import ApiV1SitesEvpnTopologies403ErrorException
from mistapi.exceptions.api_v_1_sites_evpn_topologies_404_error_exception import ApiV1SitesEvpnTopologies404ErrorException


class SitesEVPNTopologiesController(BaseController):

    """A Controller to access Endpoints in the mistapi API."""
    def __init__(self, config):
        super(SitesEVPNTopologiesController, self).__init__(config)

    def get_site_evpn_topology(self,
                               site_id):
        """Does a GET request to /api/v1/sites/{site_id}/evpn_topologies.

        Get the existing EVPN topology

        Args:
            site_id (uuid|string): TODO: type description here.

        Returns:
            JunosEvpnTopology: Response from the API. Example response

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/api/v1/sites/{site_id}/evpn_topologies')
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
            .deserialize_into(JunosEvpnTopology.from_dictionary)
            .local_error('400', 'The API endpoint exists but its syntax/payload is incorrect, detail may be given', APIException)
            .local_error('401', 'Unauthorized', ApiV1SitesEvpnTopologies401ErrorException)
            .local_error('403', 'Permission Denied', ApiV1SitesEvpnTopologies403ErrorException)
            .local_error('404', 'Not found. The API endpoint doesn\'t exist or resource doesn\'t exist', ApiV1SitesEvpnTopologies404ErrorException)
        ).execute()

    def create_site_evpn_topology(self,
                                  site_id,
                                  body=None):
        """Does a POST request to /api/v1/sites/{site_id}/evpn_topologies.

        While all the `evpn_id` / `downlink_ips` can be specifidd by hand, the
        easiest way is to call the `build_vpn_topology` API, allowing you to
        examine the diff, and update it yourself. You can also simply call it
        with `overwrite=true` which will apply the updates for you.
        **Notes:**
        1. You can use `core` / `distribution` / `access` to create a CLOS
        topology
        2. You can also use `core` / `distribution` to form a 2-tier EVPN
        topology where ESI-Lag is configured distribution to connect to access
        switches
        3. In a small/medium campus, `collapsed-core` can be used where core
        switches are the inter-connected to do EVPN
        4. The API uses a few pre-defined parameters and best-practices to
        generate the configs. It can be customized by using `evpn_options` in
        Site Setting / Network Template. (e.g. a different subnet for the
        underlay)
        #### Collapsed Core
        In a small-medium campus, EVPN can also be enabled only at the core
        switches (up to 4) by assigning all participating switches with
        `collapsed-core role`. When there are more than 2 switches, a
        ring-like topology will be formed.
        #### ESI-Lag
        If the access switchess does not have EVPN support, you can take
        advantage of EVPN by setting up ESI-Lag on distribution switches
        #### Leaf / Access / Collapsed-Core
        For leaf nodes in a EVPN topology, you’d have to configure the IPs for
        networks that would participate in EVPN. Optionally, VRFs to isolate
        traffic from one tenant verus another

        Args:
            site_id (uuid|string): TODO: type description here.
            body (JunosEvpnTopology, optional): TODO: type description here.

        Returns:
            JunosEvpnTopology: Response from the API. Example response

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/api/v1/sites/{site_id}/evpn_topologies')
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
            .deserialize_into(JunosEvpnTopology.from_dictionary)
            .local_error('400', 'The API endpoint exists but its syntax/payload is incorrect, detail may be given', APIException)
            .local_error('401', 'Unauthorized', ApiV1SitesEvpnTopologies401ErrorException)
            .local_error('403', 'Permission Denied', ApiV1SitesEvpnTopologies403ErrorException)
            .local_error('404', 'Not found. The API endpoint doesn\'t exist or resource doesn\'t exist', ApiV1SitesEvpnTopologies404ErrorException)
        ).execute()

    def delete_site_evpn_topology(self,
                                  site_id,
                                  evpn_topology_id):
        """Does a DELETE request to /api/v1/sites/{site_id}/evpn_topologies/{evpn_topology_id}.

        Delete the site EVPN Topology

        Args:
            site_id (uuid|string): TODO: type description here.
            evpn_topology_id (uuid|string): TODO: type description here.

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
            .path('/api/v1/sites/{site_id}/evpn_topologies/{evpn_topology_id}')
            .http_method(HttpMethodEnum.DELETE)
            .template_param(Parameter()
                            .key('site_id')
                            .value(site_id)
                            .should_encode(True))
            .template_param(Parameter()
                            .key('evpn_topology_id')
                            .value(evpn_topology_id)
                            .should_encode(True))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('global'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .local_error('400', 'The API endpoint exists but its syntax/payload is incorrect, detail may be given', APIException)
            .local_error('401', 'Unauthorized', ApiV1SitesEvpnTopologies401ErrorException)
            .local_error('403', 'Permission Denied', ApiV1SitesEvpnTopologies403ErrorException)
            .local_error('404', 'Not found. The API endpoint doesn\'t exist or resource doesn\'t exist', ApiV1SitesEvpnTopologies404ErrorException)
        ).execute()

    def get_site_evpn_tolopogy(self,
                               site_id,
                               evpn_topology_id):
        """Does a GET request to /api/v1/sites/{site_id}/evpn_topologies/{evpn_topology_id}.

        Get One EVPN Topology Detail

        Args:
            site_id (uuid|string): TODO: type description here.
            evpn_topology_id (uuid|string): TODO: type description here.

        Returns:
            void: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/api/v1/sites/{site_id}/evpn_topologies/{evpn_topology_id}')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('site_id')
                            .value(site_id)
                            .should_encode(True))
            .template_param(Parameter()
                            .key('evpn_topology_id')
                            .value(evpn_topology_id)
                            .should_encode(True))
            .auth(Single('global'))
        ).execute()

    def update_site_evpn_topology(self,
                                  site_id,
                                  evpn_topology_id,
                                  body=None):
        """Does a PUT request to /api/v1/sites/{site_id}/evpn_topologies/{evpn_topology_id}.

        Update the EVPN Topolgy

        Args:
            site_id (uuid|string): TODO: type description here.
            evpn_topology_id (uuid|string): TODO: type description here.
            body (JunosEvpnTopology, optional): TODO: type description here.

        Returns:
            JunosEvpnTopology: Response from the API. Example response

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/api/v1/sites/{site_id}/evpn_topologies/{evpn_topology_id}')
            .http_method(HttpMethodEnum.PUT)
            .template_param(Parameter()
                            .key('site_id')
                            .value(site_id)
                            .should_encode(True))
            .template_param(Parameter()
                            .key('evpn_topology_id')
                            .value(evpn_topology_id)
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
            .deserialize_into(JunosEvpnTopology.from_dictionary)
            .local_error('400', 'The API endpoint exists but its syntax/payload is incorrect, detail may be given', APIException)
            .local_error('401', 'Unauthorized', ApiV1SitesEvpnTopologies401ErrorException)
            .local_error('403', 'Permission Denied', ApiV1SitesEvpnTopologies403ErrorException)
            .local_error('404', 'Not found. The API endpoint doesn\'t exist or resource doesn\'t exist', ApiV1SitesEvpnTopologies404ErrorException)
        ).execute()
