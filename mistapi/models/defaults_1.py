# -*- coding: utf-8 -*-

"""
mistapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from mistapi.api_helper import APIHelper


class Defaults1(object):

    """Implementation of the 'Defaults1' model.

    Object Key is the interface type name (e.g. "lan_ports", "wan_ports",
    ...)

    Attributes:
        ports (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "ports": '_ports'
    }

    _optionals = [
        'ports',
    ]

    def __init__(self,
                 ports=APIHelper.SKIP):
        """Constructor for the Defaults1 class"""

        # Initialize members of the class
        if ports is not APIHelper.SKIP:
            self.ports = ports 

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

        ports = dictionary.get("_ports") if dictionary.get("_ports") else APIHelper.SKIP
        # Return an object of this model
        return cls(ports)
