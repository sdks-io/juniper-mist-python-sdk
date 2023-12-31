# -*- coding: utf-8 -*-

"""
mistapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class ApiV1ConstCountriesResponse(object):

    """Implementation of the 'Api V1 Const Countries Response' model.

    TODO: type model description here.

    Attributes:
        alpha_2 (string): TODO: type description here.
        certified (bool): TODO: type description here.
        name (string): TODO: type description here.
        numeric (float): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "alpha_2": 'alpha2',
        "certified": 'certified',
        "name": 'name',
        "numeric": 'numeric'
    }

    def __init__(self,
                 alpha_2=None,
                 certified=None,
                 name=None,
                 numeric=None):
        """Constructor for the ApiV1ConstCountriesResponse class"""

        # Initialize members of the class
        self.alpha_2 = alpha_2 
        self.certified = certified 
        self.name = name 
        self.numeric = numeric 

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

        alpha_2 = dictionary.get("alpha2") if dictionary.get("alpha2") else None
        certified = dictionary.get("certified") if "certified" in dictionary.keys() else None
        name = dictionary.get("name") if dictionary.get("name") else None
        numeric = dictionary.get("numeric") if dictionary.get("numeric") else None
        # Return an object of this model
        return cls(alpha_2,
                   certified,
                   name,
                   numeric)
