# -*- coding: utf-8 -*-

"""
mistapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from mistapi.api_helper import APIHelper


class Custom1(object):

    """Implementation of the 'Custom1' model.

    TODO: type model description here.

    Attributes:
        port_range (string): matched dst port, `0` means any
        protocol (ProtocolEnum): TODO: type description here.
        subnets (list of string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "port_range": 'port_range',
        "protocol": 'protocol',
        "subnets": 'subnets'
    }

    _optionals = [
        'port_range',
        'protocol',
        'subnets',
    ]

    def __init__(self,
                 port_range=APIHelper.SKIP,
                 protocol='any',
                 subnets=APIHelper.SKIP):
        """Constructor for the Custom1 class"""

        # Initialize members of the class
        if port_range is not APIHelper.SKIP:
            self.port_range = port_range 
        self.protocol = protocol 
        if subnets is not APIHelper.SKIP:
            self.subnets = subnets 

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

        port_range = dictionary.get("port_range") if dictionary.get("port_range") else APIHelper.SKIP
        protocol = dictionary.get("protocol") if dictionary.get("protocol") else 'any'
        subnets = dictionary.get("subnets") if dictionary.get("subnets") else APIHelper.SKIP
        # Return an object of this model
        return cls(port_range,
                   protocol,
                   subnets)
