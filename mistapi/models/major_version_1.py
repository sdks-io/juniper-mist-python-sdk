# -*- coding: utf-8 -*-

"""
mistapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from mistapi.api_helper import APIHelper


class MajorVersion1(object):

    """Implementation of the 'MajorVersion1' model.

    TODO: type model description here.

    Attributes:
        major_count (int): TODO: type description here.
        major_version (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "major_count": 'major_count',
        "major_version": 'major_version'
    }

    _optionals = [
        'major_count',
        'major_version',
    ]

    def __init__(self,
                 major_count=APIHelper.SKIP,
                 major_version=APIHelper.SKIP):
        """Constructor for the MajorVersion1 class"""

        # Initialize members of the class
        if major_count is not APIHelper.SKIP:
            self.major_count = major_count 
        if major_version is not APIHelper.SKIP:
            self.major_version = major_version 

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

        major_count = dictionary.get("major_count") if dictionary.get("major_count") else APIHelper.SKIP
        major_version = dictionary.get("major_version") if dictionary.get("major_version") else APIHelper.SKIP
        # Return an object of this model
        return cls(major_count,
                   major_version)