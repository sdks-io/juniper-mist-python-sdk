# -*- coding: utf-8 -*-

"""
mistapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from mistapi.api_helper import APIHelper


class ApiV1ConstLicenseTypesResponse(object):

    """Implementation of the 'Api V1 Const License Types Response' model.

    TODO: type model description here.

    Attributes:
        description (string): TODO: type description here.
        includes (list of string): TODO: type description here.
        key (string): TODO: type description here.
        name (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "description": 'description',
        "includes": 'includes',
        "key": 'key',
        "name": 'name'
    }

    _optionals = [
        'description',
        'includes',
        'key',
        'name',
    ]

    def __init__(self,
                 description=APIHelper.SKIP,
                 includes=APIHelper.SKIP,
                 key=APIHelper.SKIP,
                 name=APIHelper.SKIP):
        """Constructor for the ApiV1ConstLicenseTypesResponse class"""

        # Initialize members of the class
        if description is not APIHelper.SKIP:
            self.description = description 
        if includes is not APIHelper.SKIP:
            self.includes = includes 
        if key is not APIHelper.SKIP:
            self.key = key 
        if name is not APIHelper.SKIP:
            self.name = name 

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
        includes = dictionary.get("includes") if dictionary.get("includes") else APIHelper.SKIP
        key = dictionary.get("key") if dictionary.get("key") else APIHelper.SKIP
        name = dictionary.get("name") if dictionary.get("name") else APIHelper.SKIP
        # Return an object of this model
        return cls(description,
                   includes,
                   key,
                   name)
