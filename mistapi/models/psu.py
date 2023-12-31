# -*- coding: utf-8 -*-

"""
mistapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from mistapi.api_helper import APIHelper


class Psu(object):

    """Implementation of the 'Psu' model.

    TODO: type model description here.

    Attributes:
        name (string): TODO: type description here.
        status (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "name": 'name',
        "status": 'status'
    }

    _optionals = [
        'name',
        'status',
    ]

    def __init__(self,
                 name=APIHelper.SKIP,
                 status=APIHelper.SKIP):
        """Constructor for the Psu class"""

        # Initialize members of the class
        if name is not APIHelper.SKIP:
            self.name = name 
        if status is not APIHelper.SKIP:
            self.status = status 

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

        name = dictionary.get("name") if dictionary.get("name") else APIHelper.SKIP
        status = dictionary.get("status") if dictionary.get("status") else APIHelper.SKIP
        # Return an object of this model
        return cls(name,
                   status)
