# -*- coding: utf-8 -*-

"""
mistapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from mistapi.api_helper import APIHelper


class ApiV1SitesMapsSetMapResponse(object):

    """Implementation of the 'Api V1 Sites Maps Set Map Response' model.

    TODO: type model description here.

    Attributes:
        locked (list of string): TODO: type description here.
        moved (list of string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "locked": 'locked',
        "moved": 'moved'
    }

    _optionals = [
        'locked',
        'moved',
    ]

    def __init__(self,
                 locked=APIHelper.SKIP,
                 moved=APIHelper.SKIP):
        """Constructor for the ApiV1SitesMapsSetMapResponse class"""

        # Initialize members of the class
        if locked is not APIHelper.SKIP:
            self.locked = locked 
        if moved is not APIHelper.SKIP:
            self.moved = moved 

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

        locked = dictionary.get("locked") if dictionary.get("locked") else APIHelper.SKIP
        moved = dictionary.get("moved") if dictionary.get("moved") else APIHelper.SKIP
        # Return an object of this model
        return cls(locked,
                   moved)