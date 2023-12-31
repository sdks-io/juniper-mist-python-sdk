# -*- coding: utf-8 -*-

"""
mistapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class Result25(object):

    """Implementation of the 'Result25' model.

    TODO: type model description here.

    Attributes:
        count (int): TODO: type description here.
        system_name (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "count": 'count',
        "system_name": 'system_name'
    }

    def __init__(self,
                 count=None,
                 system_name=None):
        """Constructor for the Result25 class"""

        # Initialize members of the class
        self.count = count 
        self.system_name = system_name 

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

        count = dictionary.get("count") if dictionary.get("count") else None
        system_name = dictionary.get("system_name") if dictionary.get("system_name") else None
        # Return an object of this model
        return cls(count,
                   system_name)
