# -*- coding: utf-8 -*-

"""
mistapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class Node3(object):

    """Implementation of the 'Node3' model.

    TODO: type model description here.

    Attributes:
        mac (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "mac": 'mac'
    }

    def __init__(self,
                 mac=None):
        """Constructor for the Node3 class"""

        # Initialize members of the class
        self.mac = mac 

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

        mac = dictionary.get("mac") if dictionary.get("mac") else None
        # Return an object of this model
        return cls(mac)
