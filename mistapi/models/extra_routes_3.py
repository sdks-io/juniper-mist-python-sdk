# -*- coding: utf-8 -*-

"""
mistapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from mistapi.api_helper import APIHelper


class ExtraRoutes3(object):

    """Implementation of the 'ExtraRoutes3' model.

    The property key is a CIDR

    Attributes:
        via (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "via": 'via'
    }

    _optionals = [
        'via',
    ]

    def __init__(self,
                 via=APIHelper.SKIP):
        """Constructor for the ExtraRoutes3 class"""

        # Initialize members of the class
        if via is not APIHelper.SKIP:
            self.via = via 

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

        via = dictionary.get("via") if dictionary.get("via") else APIHelper.SKIP
        # Return an object of this model
        return cls(via)
