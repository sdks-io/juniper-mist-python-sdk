# -*- coding: utf-8 -*-

"""
mistapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from mistapi.api_helper import APIHelper
from mistapi.models.fixed_bindings import FixedBindings


class DhcpdConfig(object):

    """Implementation of the 'DhcpdConfig' model.

    TODO: type model description here.

    Attributes:
        dns_servers (list of string): TODO: type description here.
        dns_suffix (list of string): TODO: type description here.
        fixed_bindings (dict): The property key is the device MAC address
        gateway (string): TODO: type description here.
        ip_end (string): TODO: type description here.
        ip_start (string): TODO: type description here.
        servers (list of string): TODO: type description here.
        mtype (Type18Enum): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "dns_servers": 'dns_servers',
        "dns_suffix": 'dns_suffix',
        "fixed_bindings": 'fixed_bindings',
        "gateway": 'gateway',
        "ip_end": 'ip_end',
        "ip_start": 'ip_start',
        "servers": 'servers',
        "mtype": 'type'
    }

    _optionals = [
        'dns_servers',
        'dns_suffix',
        'fixed_bindings',
        'gateway',
        'ip_end',
        'ip_start',
        'servers',
        'mtype',
    ]

    def __init__(self,
                 dns_servers=APIHelper.SKIP,
                 dns_suffix=APIHelper.SKIP,
                 fixed_bindings=APIHelper.SKIP,
                 gateway=APIHelper.SKIP,
                 ip_end=APIHelper.SKIP,
                 ip_start=APIHelper.SKIP,
                 servers=APIHelper.SKIP,
                 mtype='local'):
        """Constructor for the DhcpdConfig class"""

        # Initialize members of the class
        if dns_servers is not APIHelper.SKIP:
            self.dns_servers = dns_servers 
        if dns_suffix is not APIHelper.SKIP:
            self.dns_suffix = dns_suffix 
        if fixed_bindings is not APIHelper.SKIP:
            self.fixed_bindings = fixed_bindings 
        if gateway is not APIHelper.SKIP:
            self.gateway = gateway 
        if ip_end is not APIHelper.SKIP:
            self.ip_end = ip_end 
        if ip_start is not APIHelper.SKIP:
            self.ip_start = ip_start 
        if servers is not APIHelper.SKIP:
            self.servers = servers 
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

        dns_servers = dictionary.get("dns_servers") if dictionary.get("dns_servers") else APIHelper.SKIP
        dns_suffix = dictionary.get("dns_suffix") if dictionary.get("dns_suffix") else APIHelper.SKIP
        fixed_bindings = FixedBindings.from_dictionary(dictionary.get('fixed_bindings')) if 'fixed_bindings' in dictionary.keys() else APIHelper.SKIP
        gateway = dictionary.get("gateway") if dictionary.get("gateway") else APIHelper.SKIP
        ip_end = dictionary.get("ip_end") if dictionary.get("ip_end") else APIHelper.SKIP
        ip_start = dictionary.get("ip_start") if dictionary.get("ip_start") else APIHelper.SKIP
        servers = dictionary.get("servers") if dictionary.get("servers") else APIHelper.SKIP
        mtype = dictionary.get("type") if dictionary.get("type") else 'local'
        # Return an object of this model
        return cls(dns_servers,
                   dns_suffix,
                   fixed_bindings,
                   gateway,
                   ip_end,
                   ip_start,
                   servers,
                   mtype)