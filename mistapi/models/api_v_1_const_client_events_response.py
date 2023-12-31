# -*- coding: utf-8 -*-

"""
mistapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class ApiV1ConstClientEventsResponse(object):

    """Implementation of the 'Api V1 Const Client Events Response' model.

    TODO: type model description here.

    Attributes:
        display (string): TODO: type description here.
        key (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "display": 'display',
        "key": 'key'
    }

    def __init__(self,
                 display=None,
                 key=None):
        """Constructor for the ApiV1ConstClientEventsResponse class"""

        # Initialize members of the class
        self.display = display 
        self.key = key 

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

        display = dictionary.get("display") if dictionary.get("display") else None
        key = dictionary.get("key") if dictionary.get("key") else None
        # Return an object of this model
        return cls(display,
                   key)
