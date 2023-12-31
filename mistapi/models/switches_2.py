# -*- coding: utf-8 -*-

"""
mistapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from mistapi.api_helper import APIHelper


class Switches2(object):

    """Implementation of the 'Switches2' model.

    TODO: type model description here.

    Attributes:
        interfaces (list of string): TODO: type description here.
        switch_mac (string): TODO: type description here.
        switch_name (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "interfaces": 'interfaces',
        "switch_mac": 'switch_mac',
        "switch_name": 'switch_name'
    }

    _optionals = [
        'interfaces',
        'switch_mac',
        'switch_name',
    ]

    def __init__(self,
                 interfaces=APIHelper.SKIP,
                 switch_mac=APIHelper.SKIP,
                 switch_name=APIHelper.SKIP):
        """Constructor for the Switches2 class"""

        # Initialize members of the class
        if interfaces is not APIHelper.SKIP:
            self.interfaces = interfaces 
        if switch_mac is not APIHelper.SKIP:
            self.switch_mac = switch_mac 
        if switch_name is not APIHelper.SKIP:
            self.switch_name = switch_name 

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

        interfaces = dictionary.get("interfaces") if dictionary.get("interfaces") else APIHelper.SKIP
        switch_mac = dictionary.get("switch_mac") if dictionary.get("switch_mac") else APIHelper.SKIP
        switch_name = dictionary.get("switch_name") if dictionary.get("switch_name") else APIHelper.SKIP
        # Return an object of this model
        return cls(interfaces,
                   switch_mac,
                   switch_name)
