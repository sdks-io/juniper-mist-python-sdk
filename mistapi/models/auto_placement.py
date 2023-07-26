# -*- coding: utf-8 -*-

"""
mistapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from mistapi.api_helper import APIHelper


class AutoPlacement(object):

    """Implementation of the 'AutoPlacement' model.

    if we're able to determine its x/y/orientation, this will be populated

    Attributes:
        orientation (float): TODO: type description here.
        x (float): TODO: type description here.
        y (float): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "orientation": 'orientation',
        "x": 'x',
        "y": 'y'
    }

    _optionals = [
        'orientation',
        'x',
        'y',
    ]

    def __init__(self,
                 orientation=APIHelper.SKIP,
                 x=APIHelper.SKIP,
                 y=APIHelper.SKIP):
        """Constructor for the AutoPlacement class"""

        # Initialize members of the class
        if orientation is not APIHelper.SKIP:
            self.orientation = orientation 
        if x is not APIHelper.SKIP:
            self.x = x 
        if y is not APIHelper.SKIP:
            self.y = y 

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

        orientation = dictionary.get("orientation") if dictionary.get("orientation") else APIHelper.SKIP
        x = dictionary.get("x") if dictionary.get("x") else APIHelper.SKIP
        y = dictionary.get("y") if dictionary.get("y") else APIHelper.SKIP
        # Return an object of this model
        return cls(orientation,
                   x,
                   y)
