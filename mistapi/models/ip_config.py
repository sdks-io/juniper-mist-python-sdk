# -*- coding: utf-8 -*-

"""
mistapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from mistapi.api_helper import APIHelper


class IpConfig(object):

    """Implementation of the 'IpConfig' model.

    TODO: type model description here.

    Attributes:
        dns (list of string): TODO: type description here.
        dns_suffix (list of string): TODO: type description here.
        gateway (string): TODO: type description here.
        ip (string): TODO: type description here.
        netmask (string): TODO: type description here.
        mtype (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "dns": 'dns',
        "dns_suffix": 'dns_suffix',
        "gateway": 'gateway',
        "ip": 'ip',
        "netmask": 'netmask',
        "mtype": 'type'
    }

    _optionals = [
        'dns',
        'dns_suffix',
        'gateway',
        'ip',
        'netmask',
        'mtype',
    ]

    def __init__(self,
                 dns=APIHelper.SKIP,
                 dns_suffix=APIHelper.SKIP,
                 gateway=APIHelper.SKIP,
                 ip=APIHelper.SKIP,
                 netmask=APIHelper.SKIP,
                 mtype=APIHelper.SKIP):
        """Constructor for the IpConfig class"""

        # Initialize members of the class
        if dns is not APIHelper.SKIP:
            self.dns = dns 
        if dns_suffix is not APIHelper.SKIP:
            self.dns_suffix = dns_suffix 
        if gateway is not APIHelper.SKIP:
            self.gateway = gateway 
        if ip is not APIHelper.SKIP:
            self.ip = ip 
        if netmask is not APIHelper.SKIP:
            self.netmask = netmask 
        if mtype is not APIHelper.SKIP:
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

        dns = dictionary.get("dns") if dictionary.get("dns") else APIHelper.SKIP
        dns_suffix = dictionary.get("dns_suffix") if dictionary.get("dns_suffix") else APIHelper.SKIP
        gateway = dictionary.get("gateway") if dictionary.get("gateway") else APIHelper.SKIP
        ip = dictionary.get("ip") if dictionary.get("ip") else APIHelper.SKIP
        netmask = dictionary.get("netmask") if dictionary.get("netmask") else APIHelper.SKIP
        mtype = dictionary.get("type") if dictionary.get("type") else APIHelper.SKIP
        # Return an object of this model
        return cls(dns,
                   dns_suffix,
                   gateway,
                   ip,
                   netmask,
                   mtype)
