# -*- coding: utf-8 -*-

"""
mistapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from mistapi.api_helper import APIHelper


class OobIpConfig(object):

    """Implementation of the 'OobIpConfig' model.

    ip configuration of the Mist Edge out-of-band management interface

    Attributes:
        dns (list of string): if `type`=`static`
        gateway (string): if `type`=`static`
        gateway_6 (string): TODO: type description here.
        ip (string): if `type`=`static`
        ip_6 (string): TODO: type description here.
        netmask (string): if `type`=`static`
        netmask_6 (string): TODO: type description here.
        mtype (Type6Enum): TODO: type description here.
        type_6 (Type6Enum): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "dns": 'dns',
        "gateway": 'gateway',
        "gateway_6": 'gateway6',
        "ip": 'ip',
        "ip_6": 'ip6',
        "netmask": 'netmask',
        "netmask_6": 'netmask6',
        "mtype": 'type',
        "type_6": 'type6'
    }

    _optionals = [
        'dns',
        'gateway',
        'gateway_6',
        'ip',
        'ip_6',
        'netmask',
        'netmask_6',
        'mtype',
        'type_6',
    ]

    def __init__(self,
                 dns=None,
                 gateway=APIHelper.SKIP,
                 gateway_6=APIHelper.SKIP,
                 ip=APIHelper.SKIP,
                 ip_6=APIHelper.SKIP,
                 netmask=APIHelper.SKIP,
                 netmask_6=APIHelper.SKIP,
                 mtype='dhcp',
                 type_6=APIHelper.SKIP):
        """Constructor for the OobIpConfig class"""

        # Initialize members of the class
        self.dns = dns 
        if gateway is not APIHelper.SKIP:
            self.gateway = gateway 
        if gateway_6 is not APIHelper.SKIP:
            self.gateway_6 = gateway_6 
        if ip is not APIHelper.SKIP:
            self.ip = ip 
        if ip_6 is not APIHelper.SKIP:
            self.ip_6 = ip_6 
        if netmask is not APIHelper.SKIP:
            self.netmask = netmask 
        if netmask_6 is not APIHelper.SKIP:
            self.netmask_6 = netmask_6 
        self.mtype = mtype 
        if type_6 is not APIHelper.SKIP:
            self.type_6 = type_6 

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

        dns = dictionary.get("dns") if dictionary.get("dns") else None
        gateway = dictionary.get("gateway") if dictionary.get("gateway") else APIHelper.SKIP
        gateway_6 = dictionary.get("gateway6") if dictionary.get("gateway6") else APIHelper.SKIP
        ip = dictionary.get("ip") if dictionary.get("ip") else APIHelper.SKIP
        ip_6 = dictionary.get("ip6") if dictionary.get("ip6") else APIHelper.SKIP
        netmask = dictionary.get("netmask") if dictionary.get("netmask") else APIHelper.SKIP
        netmask_6 = dictionary.get("netmask6") if dictionary.get("netmask6") else APIHelper.SKIP
        mtype = dictionary.get("type") if dictionary.get("type") else 'dhcp'
        type_6 = dictionary.get("type6") if dictionary.get("type6") else APIHelper.SKIP
        # Return an object of this model
        return cls(dns,
                   gateway,
                   gateway_6,
                   ip,
                   ip_6,
                   netmask,
                   netmask_6,
                   mtype,
                   type_6)
