# -*- coding: utf-8 -*-

"""
mistapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from mistapi.api_helper import APIHelper


class Sessions(object):

    """Implementation of the 'Sessions' model.

    TODO: type model description here.

    Attributes:
        current (float): TODO: type description here.
        max (float): TODO: type description here.
        pending (float): TODO: type description here.
        valid (float): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "current": 'current',
        "max": 'max',
        "pending": 'pending',
        "valid": 'valid'
    }

    _optionals = [
        'current',
        'max',
        'pending',
        'valid',
    ]

    def __init__(self,
                 current=APIHelper.SKIP,
                 max=APIHelper.SKIP,
                 pending=APIHelper.SKIP,
                 valid=APIHelper.SKIP):
        """Constructor for the Sessions class"""

        # Initialize members of the class
        if current is not APIHelper.SKIP:
            self.current = current 
        if max is not APIHelper.SKIP:
            self.max = max 
        if pending is not APIHelper.SKIP:
            self.pending = pending 
        if valid is not APIHelper.SKIP:
            self.valid = valid 

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

        current = dictionary.get("current") if dictionary.get("current") else APIHelper.SKIP
        max = dictionary.get("max") if dictionary.get("max") else APIHelper.SKIP
        pending = dictionary.get("pending") if dictionary.get("pending") else APIHelper.SKIP
        valid = dictionary.get("valid") if dictionary.get("valid") else APIHelper.SKIP
        # Return an object of this model
        return cls(current,
                   max,
                   pending,
                   valid)