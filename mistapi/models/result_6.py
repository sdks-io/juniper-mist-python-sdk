# -*- coding: utf-8 -*-

"""
mistapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class Result6(object):

    """Implementation of the 'Result6' model.

    TODO: type model description here.

    Attributes:
        id (uuid|string): TODO: type description here.
        text (string): TODO: type description here.
        mtype (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id": 'id',
        "text": 'text',
        "mtype": 'type'
    }

    def __init__(self,
                 id=None,
                 text=None,
                 mtype=None):
        """Constructor for the Result6 class"""

        # Initialize members of the class
        self.id = id 
        self.text = text 
        self.mtype = mtype 

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

        id = dictionary.get("id") if dictionary.get("id") else None
        text = dictionary.get("text") if dictionary.get("text") else None
        mtype = dictionary.get("type") if dictionary.get("type") else None
        # Return an object of this model
        return cls(id,
                   text,
                   mtype)
