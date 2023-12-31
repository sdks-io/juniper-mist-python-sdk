# -*- coding: utf-8 -*-

"""
mistapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from mistapi.api_helper import APIHelper


class MajorVersion(object):

    """Implementation of the 'MajorVersion' model.

    TODO: type model description here.

    Attributes:
        major_count (float): TODO: type description here.
        model (string): TODO: type description here.
        system_names (list of string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "major_count": 'major_count',
        "model": 'model',
        "system_names": 'system_names'
    }

    _optionals = [
        'system_names',
    ]

    def __init__(self,
                 major_count=None,
                 model=None,
                 system_names=APIHelper.SKIP):
        """Constructor for the MajorVersion class"""

        # Initialize members of the class
        self.major_count = major_count 
        self.model = model 
        if system_names is not APIHelper.SKIP:
            self.system_names = system_names 

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

        major_count = dictionary.get("major_count") if dictionary.get("major_count") else None
        model = dictionary.get("model") if dictionary.get("model") else None
        system_names = dictionary.get("system_names") if dictionary.get("system_names") else APIHelper.SKIP
        # Return an object of this model
        return cls(major_count,
                   model,
                   system_names)
