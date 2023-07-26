# -*- coding: utf-8 -*-

"""
mistapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class LicenseDuplicated(object):

    """Implementation of the 'LicenseDuplicated' model.

    TODO: type model description here.

    Attributes:
        end (int): TODO: type description here.
        quantity (int): TODO: type description here.
        start (int): TODO: type description here.
        mtype (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "end": 'end',
        "quantity": 'quantity',
        "start": 'start',
        "mtype": 'type'
    }

    def __init__(self,
                 end=None,
                 quantity=None,
                 start=None,
                 mtype=None):
        """Constructor for the LicenseDuplicated class"""

        # Initialize members of the class
        self.end = end 
        self.quantity = quantity 
        self.start = start 
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

        end = dictionary.get("end") if dictionary.get("end") else None
        quantity = dictionary.get("quantity") if dictionary.get("quantity") else None
        start = dictionary.get("start") if dictionary.get("start") else None
        mtype = dictionary.get("type") if dictionary.get("type") else None
        # Return an object of this model
        return cls(end,
                   quantity,
                   start,
                   mtype)