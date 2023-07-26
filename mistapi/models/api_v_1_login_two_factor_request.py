# -*- coding: utf-8 -*-

"""
mistapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class ApiV1LoginTwoFactorRequest(object):

    """Implementation of the 'Api V1 Login Two Factor Request' model.

    TODO: type model description here.

    Attributes:
        two_factor (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "two_factor": 'two_factor'
    }

    def __init__(self,
                 two_factor=None):
        """Constructor for the ApiV1LoginTwoFactorRequest class"""

        # Initialize members of the class
        self.two_factor = two_factor 

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

        two_factor = dictionary.get("two_factor") if dictionary.get("two_factor") else None
        # Return an object of this model
        return cls(two_factor)