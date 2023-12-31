# -*- coding: utf-8 -*-

"""
mistapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class Result12(object):

    """Implementation of the 'Result12' model.

    TODO: type model description here.

    Attributes:
        count (int): TODO: type description here.
        model (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "count": 'count',
        "model": 'model'
    }

    def __init__(self,
                 count=None,
                 model=None):
        """Constructor for the Result12 class"""

        # Initialize members of the class
        self.count = count 
        self.model = model 

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
        model = dictionary.get("model") if dictionary.get("model") else None
        # Return an object of this model
        return cls(count,
                   model)
