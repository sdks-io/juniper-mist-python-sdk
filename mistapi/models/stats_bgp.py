# -*- coding: utf-8 -*-

"""
mistapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from mistapi.api_helper import APIHelper


class StatsBgp(object):

    """Implementation of the 'stats_bgp' model.

    TODO: type model description here.

    Attributes:
        evpn_overlay (bool): if this is created for evpn overlay
        for_overlay (bool): if this is created for overlay
        local_as (int): AS
        mac (string): router mac address
        neighbor (string): TODO: type description here.
        neighbor_as (int): TODO: type description here.
        neighbor_mac (string): if it's another device in the same org
        node (string): node0/node1
        org_id (string): router org ID
        rx_pkts (int): TODO: type description here.
        rx_routes (int): number of received routes
        site_id (string): router site ID
        state (StateEnum): TODO: type description here.
        timestamp (float): TODO: type description here.
        tx_pkts (int): TODO: type description here.
        tx_routes (int): TODO: type description here.
        up (bool): TODO: type description here.
        uptime (int): TODO: type description here.
        vrf_name (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "evpn_overlay": 'evpn_overlay',
        "for_overlay": 'for_overlay',
        "local_as": 'local_as',
        "mac": 'mac',
        "neighbor": 'neighbor',
        "neighbor_as": 'neighbor_as',
        "neighbor_mac": 'neighbor_mac',
        "node": 'node',
        "org_id": 'org_id',
        "rx_pkts": 'rx_pkts',
        "rx_routes": 'rx_routes',
        "site_id": 'site_id',
        "state": 'state',
        "timestamp": 'timestamp',
        "tx_pkts": 'tx_pkts',
        "tx_routes": 'tx_routes',
        "up": 'up',
        "uptime": 'uptime',
        "vrf_name": 'vrf_name'
    }

    _optionals = [
        'evpn_overlay',
        'for_overlay',
        'local_as',
        'mac',
        'neighbor',
        'neighbor_as',
        'neighbor_mac',
        'node',
        'org_id',
        'rx_pkts',
        'rx_routes',
        'site_id',
        'state',
        'timestamp',
        'tx_pkts',
        'tx_routes',
        'up',
        'uptime',
        'vrf_name',
    ]

    def __init__(self,
                 evpn_overlay=APIHelper.SKIP,
                 for_overlay=APIHelper.SKIP,
                 local_as=APIHelper.SKIP,
                 mac=APIHelper.SKIP,
                 neighbor=APIHelper.SKIP,
                 neighbor_as=APIHelper.SKIP,
                 neighbor_mac=APIHelper.SKIP,
                 node=APIHelper.SKIP,
                 org_id=APIHelper.SKIP,
                 rx_pkts=APIHelper.SKIP,
                 rx_routes=APIHelper.SKIP,
                 site_id=APIHelper.SKIP,
                 state=APIHelper.SKIP,
                 timestamp=APIHelper.SKIP,
                 tx_pkts=APIHelper.SKIP,
                 tx_routes=APIHelper.SKIP,
                 up=APIHelper.SKIP,
                 uptime=APIHelper.SKIP,
                 vrf_name=APIHelper.SKIP):
        """Constructor for the StatsBgp class"""

        # Initialize members of the class
        if evpn_overlay is not APIHelper.SKIP:
            self.evpn_overlay = evpn_overlay 
        if for_overlay is not APIHelper.SKIP:
            self.for_overlay = for_overlay 
        if local_as is not APIHelper.SKIP:
            self.local_as = local_as 
        if mac is not APIHelper.SKIP:
            self.mac = mac 
        if neighbor is not APIHelper.SKIP:
            self.neighbor = neighbor 
        if neighbor_as is not APIHelper.SKIP:
            self.neighbor_as = neighbor_as 
        if neighbor_mac is not APIHelper.SKIP:
            self.neighbor_mac = neighbor_mac 
        if node is not APIHelper.SKIP:
            self.node = node 
        if org_id is not APIHelper.SKIP:
            self.org_id = org_id 
        if rx_pkts is not APIHelper.SKIP:
            self.rx_pkts = rx_pkts 
        if rx_routes is not APIHelper.SKIP:
            self.rx_routes = rx_routes 
        if site_id is not APIHelper.SKIP:
            self.site_id = site_id 
        if state is not APIHelper.SKIP:
            self.state = state 
        if timestamp is not APIHelper.SKIP:
            self.timestamp = timestamp 
        if tx_pkts is not APIHelper.SKIP:
            self.tx_pkts = tx_pkts 
        if tx_routes is not APIHelper.SKIP:
            self.tx_routes = tx_routes 
        if up is not APIHelper.SKIP:
            self.up = up 
        if uptime is not APIHelper.SKIP:
            self.uptime = uptime 
        if vrf_name is not APIHelper.SKIP:
            self.vrf_name = vrf_name 

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

        evpn_overlay = dictionary.get("evpn_overlay") if "evpn_overlay" in dictionary.keys() else APIHelper.SKIP
        for_overlay = dictionary.get("for_overlay") if "for_overlay" in dictionary.keys() else APIHelper.SKIP
        local_as = dictionary.get("local_as") if dictionary.get("local_as") else APIHelper.SKIP
        mac = dictionary.get("mac") if dictionary.get("mac") else APIHelper.SKIP
        neighbor = dictionary.get("neighbor") if dictionary.get("neighbor") else APIHelper.SKIP
        neighbor_as = dictionary.get("neighbor_as") if dictionary.get("neighbor_as") else APIHelper.SKIP
        neighbor_mac = dictionary.get("neighbor_mac") if dictionary.get("neighbor_mac") else APIHelper.SKIP
        node = dictionary.get("node") if dictionary.get("node") else APIHelper.SKIP
        org_id = dictionary.get("org_id") if dictionary.get("org_id") else APIHelper.SKIP
        rx_pkts = dictionary.get("rx_pkts") if dictionary.get("rx_pkts") else APIHelper.SKIP
        rx_routes = dictionary.get("rx_routes") if dictionary.get("rx_routes") else APIHelper.SKIP
        site_id = dictionary.get("site_id") if dictionary.get("site_id") else APIHelper.SKIP
        state = dictionary.get("state") if dictionary.get("state") else APIHelper.SKIP
        timestamp = dictionary.get("timestamp") if dictionary.get("timestamp") else APIHelper.SKIP
        tx_pkts = dictionary.get("tx_pkts") if dictionary.get("tx_pkts") else APIHelper.SKIP
        tx_routes = dictionary.get("tx_routes") if dictionary.get("tx_routes") else APIHelper.SKIP
        up = dictionary.get("up") if "up" in dictionary.keys() else APIHelper.SKIP
        uptime = dictionary.get("uptime") if dictionary.get("uptime") else APIHelper.SKIP
        vrf_name = dictionary.get("vrf_name") if dictionary.get("vrf_name") else APIHelper.SKIP
        # Return an object of this model
        return cls(evpn_overlay,
                   for_overlay,
                   local_as,
                   mac,
                   neighbor,
                   neighbor_as,
                   neighbor_mac,
                   node,
                   org_id,
                   rx_pkts,
                   rx_routes,
                   site_id,
                   state,
                   timestamp,
                   tx_pkts,
                   tx_routes,
                   up,
                   uptime,
                   vrf_name)
