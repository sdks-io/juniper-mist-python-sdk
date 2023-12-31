# -*- coding: utf-8 -*-

"""
mistapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from mistapi.api_helper import APIHelper


class Details4(object):

    """Implementation of the 'Details4' model.

    TODO: type model description here.

    Attributes:
        config_success_count (int): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "config_success_count": 'config_success_count'
    }

    _optionals = [
        'config_success_count',
    ]

    def __init__(self,
                 config_success_count=APIHelper.SKIP):
        """Constructor for the Details4 class"""

        # Initialize members of the class
        if config_success_count is not APIHelper.SKIP:
            self.config_success_count = config_success_count 

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

        config_success_count = dictionary.get("config_success_count") if dictionary.get("config_success_count") else APIHelper.SKIP
        # Return an object of this model
        return cls(config_success_count)
