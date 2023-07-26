# -*- coding: utf-8 -*-

"""
mistapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from mistapi.api_helper import APIHelper
from mistapi.models.overlay import Overlay
from mistapi.models.underlay import Underlay


class JunosEvpnOptions(object):

    """Implementation of the 'junos_evpn_options' model.

    EVPN Options

    Attributes:
        auto_loopback_subnet (string): optional, for dhcp_relay, unique
            loopback IPs are required for ERB or IPClos where we can set
            option-82 server-id-overrides
        auto_router_id_subnet (string): optional, this generates router_id
            automatically, if specified, `router_id_prefix` is ignored
        core_as_border (bool): optional, for ERB or CLOS, you can either use
            esilag to upstream routers or to also be the virtual-gateway when
            `routed_at` != `core`, whether to do virtual-gateway at core as
            well
        overlay (Overlay): TODO: type description here.
        per_vlan_vga_v_4_mac (bool): by default, JUNOS uses 00-00-5e-00-01-01
            as the virtual-gateway-address's v4-mac if enabled,
            00-00-5e-00-XX-YY will be used (where XX=vlan_id/256,
            YY=vlan_id%256)
        routed_at (RoutedAtEnum): optional, where virtual-gateway should
            reside
        underlay (Underlay): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "auto_loopback_subnet": 'auto_loopback_subnet',
        "auto_router_id_subnet": 'auto_router_id_subnet',
        "core_as_border": 'core_as_border',
        "overlay": 'overlay',
        "per_vlan_vga_v_4_mac": 'per_vlan_vga_v4_mac',
        "routed_at": 'routed_at',
        "underlay": 'underlay'
    }

    _optionals = [
        'auto_loopback_subnet',
        'auto_router_id_subnet',
        'core_as_border',
        'overlay',
        'per_vlan_vga_v_4_mac',
        'routed_at',
        'underlay',
    ]

    def __init__(self,
                 auto_loopback_subnet=APIHelper.SKIP,
                 auto_router_id_subnet=APIHelper.SKIP,
                 core_as_border=False,
                 overlay=APIHelper.SKIP,
                 per_vlan_vga_v_4_mac=False,
                 routed_at='edge',
                 underlay=APIHelper.SKIP):
        """Constructor for the JunosEvpnOptions class"""

        # Initialize members of the class
        if auto_loopback_subnet is not APIHelper.SKIP:
            self.auto_loopback_subnet = auto_loopback_subnet 
        if auto_router_id_subnet is not APIHelper.SKIP:
            self.auto_router_id_subnet = auto_router_id_subnet 
        self.core_as_border = core_as_border 
        if overlay is not APIHelper.SKIP:
            self.overlay = overlay 
        self.per_vlan_vga_v_4_mac = per_vlan_vga_v_4_mac 
        self.routed_at = routed_at 
        if underlay is not APIHelper.SKIP:
            self.underlay = underlay 

    @classmethod
    def from_dictionary(cls,
                        dictionary):
        """Creates an instance of this model from a dictionary

        Args:
            dictionary (dictionary): A dictionary representation of the object
            as obtained from the deserialization of the server's response. The
            keys MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.

        """
        if dictionary is None:
            return None

        # Extract variables from the dictionary

        auto_loopback_subnet = dictionary.get("auto_loopback_subnet") if dictionary.get("auto_loopback_subnet") else APIHelper.SKIP
        auto_router_id_subnet = dictionary.get("auto_router_id_subnet") if dictionary.get("auto_router_id_subnet") else APIHelper.SKIP
        core_as_border = dictionary.get("core_as_border") if dictionary.get("core_as_border") else False
        overlay = Overlay.from_dictionary(dictionary.get('overlay')) if 'overlay' in dictionary.keys() else APIHelper.SKIP
        per_vlan_vga_v_4_mac = dictionary.get("per_vlan_vga_v4_mac") if dictionary.get("per_vlan_vga_v4_mac") else False
        routed_at = dictionary.get("routed_at") if dictionary.get("routed_at") else 'edge'
        underlay = Underlay.from_dictionary(dictionary.get('underlay')) if 'underlay' in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(auto_loopback_subnet,
                   auto_router_id_subnet,
                   core_as_border,
                   overlay,
                   per_vlan_vga_v_4_mac,
                   routed_at,
                   underlay)
