# -*- coding: utf-8 -*-

"""
mistapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from mistapi.api_helper import APIHelper


class Hosts(object):

    """Implementation of the 'Hosts' model.

    TODO: type model description here.

    Attributes:
        external_ips (string): TODO: type description here.
        ips (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "external_ips": 'external_ips',
        "ips": 'ips'
    }

    _optionals = [
        'external_ips',
        'ips',
    ]

    def __init__(self,
                 external_ips=APIHelper.SKIP,
                 ips=APIHelper.SKIP):
        """Constructor for the Hosts class"""

        # Initialize members of the class
        if external_ips is not APIHelper.SKIP:
            self.external_ips = external_ips 
        if ips is not APIHelper.SKIP:
            self.ips = ips 

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

        external_ips = dictionary.get("external_ips") if dictionary.get("external_ips") else APIHelper.SKIP
        ips = dictionary.get("ips") if dictionary.get("ips") else APIHelper.SKIP
        # Return an object of this model
        return cls(external_ips,
                   ips)