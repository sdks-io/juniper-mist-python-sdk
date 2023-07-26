# -*- coding: utf-8 -*-

"""
mistapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from mistapi.api_helper import APIHelper
from mistapi.models.destination_nat_1 import DestinationNat1
from mistapi.models.source_nat import SourceNat
from mistapi.models.static_nat import StaticNat


class VpnAccess(object):

    """Implementation of the 'VpnAccess' model.

    TODO: type model description here.

    Attributes:
        affinity (AffinityEnum): DRAFT - when used in path preference, whether
            we should prefer the same hub or by path
        allow_ping (bool): whether to allow ping from vpn into this routed
            network
        destination_nat (dict): Property key is the external IP / port (e.g.
            "172.16.0.5/30" or "172.16.0.3:8443")
        nat_pool (string): if `routed`==`false` (usually at Spoke), but some
            hosts needs to be reachable from Hub, a subnet is required to
            create and advertise the route to Hub
        no_readvertise_to_lan_bgp (bool): toward LAN-side BGP peers
        no_readvertise_to_overlay (bool): toward overlay how HUB should deal
            with routes it received from Spokes
        routed (bool): whether this network is routable
        source_nat (SourceNat): if `routed`==`false` (usually at Spoke), but
            some hosts needs to be reachable from Hub
        static_nat (dict): The property key may be an IP Address (i.e.
            "172.16.0.1"), and IP Address and Port (i.e. "172.16.0.1:8443") or
            a CIDR (i.e. "172.16.0.12/20")
        summarized_subnet (string): toward overlay how HUB should deal with
            routes it received from Spokes
        summarized_subnet_to_lan_bgp (string): toward LAN-side BGP peers

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "affinity": 'affinity',
        "allow_ping": 'allow_ping',
        "destination_nat": 'destination_nat',
        "nat_pool": 'nat_pool',
        "no_readvertise_to_lan_bgp": 'no_readvertise_to_lan_bgp',
        "no_readvertise_to_overlay": 'no_readvertise_to_overlay',
        "routed": 'routed',
        "source_nat": 'source_nat',
        "static_nat": 'static_nat',
        "summarized_subnet": 'summarized_subnet',
        "summarized_subnet_to_lan_bgp": 'summarized_subnet_to_lan_bgp'
    }

    _optionals = [
        'affinity',
        'allow_ping',
        'destination_nat',
        'nat_pool',
        'no_readvertise_to_lan_bgp',
        'no_readvertise_to_overlay',
        'routed',
        'source_nat',
        'static_nat',
        'summarized_subnet',
        'summarized_subnet_to_lan_bgp',
    ]

    def __init__(self,
                 affinity='hub',
                 allow_ping=APIHelper.SKIP,
                 destination_nat=APIHelper.SKIP,
                 nat_pool=APIHelper.SKIP,
                 no_readvertise_to_lan_bgp=False,
                 no_readvertise_to_overlay=APIHelper.SKIP,
                 routed=APIHelper.SKIP,
                 source_nat=APIHelper.SKIP,
                 static_nat=APIHelper.SKIP,
                 summarized_subnet=APIHelper.SKIP,
                 summarized_subnet_to_lan_bgp=APIHelper.SKIP):
        """Constructor for the VpnAccess class"""

        # Initialize members of the class
        self.affinity = affinity 
        if allow_ping is not APIHelper.SKIP:
            self.allow_ping = allow_ping 
        if destination_nat is not APIHelper.SKIP:
            self.destination_nat = destination_nat 
        if nat_pool is not APIHelper.SKIP:
            self.nat_pool = nat_pool 
        self.no_readvertise_to_lan_bgp = no_readvertise_to_lan_bgp 
        if no_readvertise_to_overlay is not APIHelper.SKIP:
            self.no_readvertise_to_overlay = no_readvertise_to_overlay 
        if routed is not APIHelper.SKIP:
            self.routed = routed 
        if source_nat is not APIHelper.SKIP:
            self.source_nat = source_nat 
        if static_nat is not APIHelper.SKIP:
            self.static_nat = static_nat 
        if summarized_subnet is not APIHelper.SKIP:
            self.summarized_subnet = summarized_subnet 
        if summarized_subnet_to_lan_bgp is not APIHelper.SKIP:
            self.summarized_subnet_to_lan_bgp = summarized_subnet_to_lan_bgp 

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

        affinity = dictionary.get("affinity") if dictionary.get("affinity") else 'hub'
        allow_ping = dictionary.get("allow_ping") if "allow_ping" in dictionary.keys() else APIHelper.SKIP
        destination_nat = DestinationNat1.from_dictionary(dictionary.get('destination_nat')) if 'destination_nat' in dictionary.keys() else APIHelper.SKIP
        nat_pool = dictionary.get("nat_pool") if dictionary.get("nat_pool") else APIHelper.SKIP
        no_readvertise_to_lan_bgp = dictionary.get("no_readvertise_to_lan_bgp") if dictionary.get("no_readvertise_to_lan_bgp") else False
        no_readvertise_to_overlay = dictionary.get("no_readvertise_to_overlay") if "no_readvertise_to_overlay" in dictionary.keys() else APIHelper.SKIP
        routed = dictionary.get("routed") if "routed" in dictionary.keys() else APIHelper.SKIP
        source_nat = SourceNat.from_dictionary(dictionary.get('source_nat')) if 'source_nat' in dictionary.keys() else APIHelper.SKIP
        static_nat = StaticNat.from_dictionary(dictionary.get('static_nat')) if 'static_nat' in dictionary.keys() else APIHelper.SKIP
        summarized_subnet = dictionary.get("summarized_subnet") if dictionary.get("summarized_subnet") else APIHelper.SKIP
        summarized_subnet_to_lan_bgp = dictionary.get("summarized_subnet_to_lan_bgp") if dictionary.get("summarized_subnet_to_lan_bgp") else APIHelper.SKIP
        # Return an object of this model
        return cls(affinity,
                   allow_ping,
                   destination_nat,
                   nat_pool,
                   no_readvertise_to_lan_bgp,
                   no_readvertise_to_overlay,
                   routed,
                   source_nat,
                   static_nat,
                   summarized_subnet,
                   summarized_subnet_to_lan_bgp)
