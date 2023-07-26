# -*- coding: utf-8 -*-

"""
mistapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from mistapi.api_helper import APIHelper


class Notify(object):

    """Implementation of the 'Notify' model.

    TODO: type model description here.

    Attributes:
        name (string): TODO: type description here.
        tag (string): TODO: type description here.
        mtype (Type26Enum): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "name": 'name',
        "tag": 'tag',
        "mtype": 'type'
    }

    _optionals = [
        'name',
        'tag',
        'mtype',
    ]

    def __init__(self,
                 name=APIHelper.SKIP,
                 tag=APIHelper.SKIP,
                 mtype=APIHelper.SKIP):
        """Constructor for the Notify class"""

        # Initialize members of the class
        if name is not APIHelper.SKIP:
            self.name = name 
        if tag is not APIHelper.SKIP:
            self.tag = tag 
        if mtype is not APIHelper.SKIP:
            self.mtype = mtype 

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
        tag = dictionary.get("tag") if dictionary.get("tag") else APIHelper.SKIP
        mtype = dictionary.get("type") if dictionary.get("type") else APIHelper.SKIP
        # Return an object of this model
        return cls(name,
                   tag,
                   mtype)