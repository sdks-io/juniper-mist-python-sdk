# -*- coding: utf-8 -*-

"""
mistapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from mistapi.api_helper import APIHelper
from mistapi.models.ips_3 import Ips3


class IpStat5(object):

    """Implementation of the 'IpStat5' model.

    TODO: type model description here.

    Attributes:
        dns (list of string): TODO: type description here.
        dns_suffix (list of string): TODO: type description here.
        gateway (string): TODO: type description here.
        gateway_6 (string): TODO: type description here.
        ip (string): TODO: type description here.
        ip_6 (string): TODO: type description here.
        ips (Ips3): TODO: type description here.
        netmask (string): TODO: type description here.
        netmask_6 (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "dns": 'dns',
        "dns_suffix": 'dns_suffix',
        "gateway": 'gateway',
        "gateway_6": 'gateway6',
        "ip": 'ip',
        "ip_6": 'ip6',
        "ips": 'ips',
        "netmask": 'netmask',
        "netmask_6": 'netmask6'
    }

    _optionals = [
        'dns',
        'dns_suffix',
        'gateway',
        'gateway_6',
        'ip',
        'ip_6',
        'ips',
        'netmask',
        'netmask_6',
    ]

    def __init__(self,
                 dns=APIHelper.SKIP,
                 dns_suffix=APIHelper.SKIP,
                 gateway=APIHelper.SKIP,
                 gateway_6=APIHelper.SKIP,
                 ip=APIHelper.SKIP,
                 ip_6=APIHelper.SKIP,
                 ips=APIHelper.SKIP,
                 netmask=APIHelper.SKIP,
                 netmask_6=APIHelper.SKIP):
        """Constructor for the IpStat5 class"""

        # Initialize members of the class
        if dns is not APIHelper.SKIP:
            self.dns = dns 
        if dns_suffix is not APIHelper.SKIP:
            self.dns_suffix = dns_suffix 
        if gateway is not APIHelper.SKIP:
            self.gateway = gateway 
        if gateway_6 is not APIHelper.SKIP:
            self.gateway_6 = gateway_6 
        if ip is not APIHelper.SKIP:
            self.ip = ip 
        if ip_6 is not APIHelper.SKIP:
            self.ip_6 = ip_6 
        if ips is not APIHelper.SKIP:
            self.ips = ips 
        if netmask is not APIHelper.SKIP:
            self.netmask = netmask 
        if netmask_6 is not APIHelper.SKIP:
            self.netmask_6 = netmask_6 

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
        gateway_6 = dictionary.get("gateway6") if dictionary.get("gateway6") else APIHelper.SKIP
        ip = dictionary.get("ip") if dictionary.get("ip") else APIHelper.SKIP
        ip_6 = dictionary.get("ip6") if dictionary.get("ip6") else APIHelper.SKIP
        ips = Ips3.from_dictionary(dictionary.get('ips')) if 'ips' in dictionary.keys() else APIHelper.SKIP
        netmask = dictionary.get("netmask") if dictionary.get("netmask") else APIHelper.SKIP
        netmask_6 = dictionary.get("netmask6") if dictionary.get("netmask6") else APIHelper.SKIP
        # Return an object of this model
        return cls(dns,
                   dns_suffix,
                   gateway,
                   gateway_6,
                   ip,
                   ip_6,
                   ips,
                   netmask,
                   netmask_6)
