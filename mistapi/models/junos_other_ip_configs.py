# -*- coding: utf-8 -*-

"""
mistapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from mistapi.api_helper import APIHelper


class JunosOtherIpConfigs(object):

    """Implementation of the 'junos_other_ip_configs' model.

    optional, if it's required to have switch's L3 presense on a network/vlan

    Attributes:
        evpn_anycast (bool): for EVPN, if anycast is desired
        ip (string): required if `type`==`static`
        netmask (string): optional, `subnet` from `network` definition will be
            used if defined
        mtype (Type6Enum): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "evpn_anycast": 'evpn_anycast',
        "ip": 'ip',
        "netmask": 'netmask',
        "mtype": 'type'
    }

    _optionals = [
        'evpn_anycast',
        'ip',
        'netmask',
        'mtype',
    ]

    def __init__(self,
                 evpn_anycast=False,
                 ip=APIHelper.SKIP,
                 netmask=APIHelper.SKIP,
                 mtype='dhcp'):
        """Constructor for the JunosOtherIpConfigs class"""

        # Initialize members of the class
        self.evpn_anycast = evpn_anycast 
        if ip is not APIHelper.SKIP:
            self.ip = ip 
        if netmask is not APIHelper.SKIP:
            self.netmask = netmask 
        self.mtype = mtype 

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

        evpn_anycast = dictionary.get("evpn_anycast") if dictionary.get("evpn_anycast") else False
        ip = dictionary.get("ip") if dictionary.get("ip") else APIHelper.SKIP
        netmask = dictionary.get("netmask") if dictionary.get("netmask") else APIHelper.SKIP
        mtype = dictionary.get("type") if dictionary.get("type") else 'dhcp'
        # Return an object of this model
        return cls(evpn_anycast,
                   ip,
                   netmask,
                   mtype)
