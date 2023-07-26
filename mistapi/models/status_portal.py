# -*- coding: utf-8 -*-

"""
mistapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from mistapi.api_helper import APIHelper


class StatusPortal(object):

    """Implementation of the 'StatusPortal' model.

    TODO: type model description here.

    Attributes:
        enabled (bool): TODO: type description here.
        hostnames (list of string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "enabled": 'enabled',
        "hostnames": 'hostnames'
    }

    _optionals = [
        'enabled',
        'hostnames',
    ]

    def __init__(self,
                 enabled=APIHelper.SKIP,
                 hostnames=APIHelper.SKIP):
        """Constructor for the StatusPortal class"""

        # Initialize members of the class
        if enabled is not APIHelper.SKIP:
            self.enabled = enabled 
        if hostnames is not APIHelper.SKIP:
            self.hostnames = hostnames 

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

        enabled = dictionary.get("enabled") if "enabled" in dictionary.keys() else APIHelper.SKIP
        hostnames = dictionary.get("hostnames") if dictionary.get("hostnames") else APIHelper.SKIP
        # Return an object of this model
        return cls(enabled,
                   hostnames)
