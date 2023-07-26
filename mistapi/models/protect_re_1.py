# -*- coding: utf-8 -*-

"""
mistapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from mistapi.api_helper import APIHelper


class ProtectRe1(object):

    """Implementation of the 'ProtectRe1' model.

    TODO: type model description here.

    Attributes:
        enabled (bool): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "enabled": 'enabled'
    }

    _optionals = [
        'enabled',
    ]

    def __init__(self,
                 enabled=False):
        """Constructor for the ProtectRe1 class"""

        # Initialize members of the class
        self.enabled = enabled 

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
        # Return an object of this model
        return cls(enabled)