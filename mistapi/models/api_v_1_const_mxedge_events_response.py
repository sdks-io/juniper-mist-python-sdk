# -*- coding: utf-8 -*-

"""
mistapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from mistapi.api_helper import APIHelper


class ApiV1ConstMxedgeEventsResponse(object):

    """Implementation of the 'Api V1 Const Mxedge Events Response' model.

    TODO: type model description here.

    Attributes:
        description (string): TODO: type description here.
        display (string): TODO: type description here.
        example (object): TODO: type description here.
        key (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "description": 'description',
        "display": 'display',
        "example": 'example',
        "key": 'key'
    }

    _optionals = [
        'description',
        'display',
        'example',
        'key',
    ]

    def __init__(self,
                 description=APIHelper.SKIP,
                 display=APIHelper.SKIP,
                 example=APIHelper.SKIP,
                 key=APIHelper.SKIP):
        """Constructor for the ApiV1ConstMxedgeEventsResponse class"""

        # Initialize members of the class
        if description is not APIHelper.SKIP:
            self.description = description 
        if display is not APIHelper.SKIP:
            self.display = display 
        if example is not APIHelper.SKIP:
            self.example = example 
        if key is not APIHelper.SKIP:
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

        description = dictionary.get("description") if dictionary.get("description") else APIHelper.SKIP
        display = dictionary.get("display") if dictionary.get("display") else APIHelper.SKIP
        example = dictionary.get("example") if dictionary.get("example") else APIHelper.SKIP
        key = dictionary.get("key") if dictionary.get("key") else APIHelper.SKIP
        # Return an object of this model
        return cls(description,
                   display,
                   example,
                   key)
