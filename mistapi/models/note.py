# -*- coding: utf-8 -*-

"""
mistapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from mistapi.api_helper import APIHelper


class Note(object):

    """Implementation of the 'note' model.

    TODO: type model description here.

    Attributes:
        note (string): Some text note describing the intent

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "note": 'note'
    }

    _optionals = [
        'note',
    ]

    def __init__(self,
                 note=APIHelper.SKIP):
        """Constructor for the Note class"""

        # Initialize members of the class
        if note is not APIHelper.SKIP:
            self.note = note 

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

        note = dictionary.get("note") if dictionary.get("note") else APIHelper.SKIP
        # Return an object of this model
        return cls(note)
