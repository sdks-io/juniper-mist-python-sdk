# -*- coding: utf-8 -*-

"""
mistapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from mistapi.api_helper import APIHelper


class Account1(object):

    """Implementation of the 'Account1' model.

    TODO: type model description here.

    Attributes:
        linked_by (string): TODO: type description here.
        name (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "linked_by": 'linked_by',
        "name": 'name'
    }

    _optionals = [
        'linked_by',
        'name',
    ]

    def __init__(self,
                 linked_by=APIHelper.SKIP,
                 name=APIHelper.SKIP):
        """Constructor for the Account1 class"""

        # Initialize members of the class
        if linked_by is not APIHelper.SKIP:
            self.linked_by = linked_by 
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

        linked_by = dictionary.get("linked_by") if dictionary.get("linked_by") else APIHelper.SKIP
        name = dictionary.get("name") if dictionary.get("name") else APIHelper.SKIP
        # Return an object of this model
        return cls(linked_by,
                   name)
