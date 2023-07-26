# -*- coding: utf-8 -*-

"""
mistapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from mistapi.api_helper import APIHelper
from mistapi.models.user_minutes import UserMinutes


class Sle1(object):

    """Implementation of the 'Sle1' model.

    TODO: type model description here.

    Attributes:
        path (string): TODO: type description here.
        user_minutes (UserMinutes): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "path": 'path',
        "user_minutes": 'user_minutes'
    }

    _optionals = [
        'user_minutes',
    ]

    def __init__(self,
                 path=None,
                 user_minutes=APIHelper.SKIP):
        """Constructor for the Sle1 class"""

        # Initialize members of the class
        self.path = path 
        if user_minutes is not APIHelper.SKIP:
            self.user_minutes = user_minutes 

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

        path = dictionary.get("path") if dictionary.get("path") else None
        user_minutes = UserMinutes.from_dictionary(dictionary.get('user_minutes')) if 'user_minutes' in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(path,
                   user_minutes)
