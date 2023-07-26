# -*- coding: utf-8 -*-

"""
mistapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from mistapi.api_helper import APIHelper


class TuntermDhcpdConfig(object):

    """Implementation of the 'TuntermDhcpdConfig' model.

    DHCP server/relay configuration of Mist Tunneled VLANs. The property key
    is the VLAN ID

    Attributes:
        enabled (bool): TODO: type description here.
        servers (list of string): TODO: type description here.
        mtype (Type31Enum): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "enabled": 'enabled',
        "servers": 'servers',
        "mtype": 'type'
    }

    _optionals = [
        'enabled',
        'servers',
        'mtype',
    ]

    def __init__(self,
                 enabled=False,
                 servers=APIHelper.SKIP,
                 mtype='relay'):
        """Constructor for the TuntermDhcpdConfig class"""

        # Initialize members of the class
        self.enabled = enabled 
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

        enabled = dictionary.get("enabled") if dictionary.get("enabled") else False
        servers = dictionary.get("servers") if dictionary.get("servers") else APIHelper.SKIP
        mtype = dictionary.get("type") if dictionary.get("type") else 'relay'
        # Return an object of this model
        return cls(enabled,
                   servers,
                   mtype)
