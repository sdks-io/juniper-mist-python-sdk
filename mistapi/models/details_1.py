# -*- coding: utf-8 -*-

"""
mistapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class Details1(object):

    """Implementation of the 'Details1' model.

    TODO: type model description here.

    Attributes:
        system_name (list of string): TODO: type description here.
        threshold (float): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "system_name": 'system_name',
        "threshold": 'threshold'
    }

    def __init__(self,
                 system_name=None,
                 threshold=None):
        """Constructor for the Details1 class"""

        # Initialize members of the class
        self.system_name = system_name 
        self.threshold = threshold 

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

        system_name = dictionary.get("system_name") if dictionary.get("system_name") else None
        threshold = dictionary.get("threshold") if dictionary.get("threshold") else None
        # Return an object of this model
        return cls(system_name,
                   threshold)