# -*- coding: utf-8 -*-

"""
mistapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class Result30(object):

    """Implementation of the 'Result30' model.

    TODO: type model description here.

    Attributes:
        enter (int): TODO: type description here.
        scope (string): TODO: type description here.
        timestamp (float): TODO: type description here.
        user (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "enter": 'enter',
        "scope": 'scope',
        "timestamp": 'timestamp',
        "user": 'user'
    }

    def __init__(self,
                 enter=None,
                 scope=None,
                 timestamp=None,
                 user=None):
        """Constructor for the Result30 class"""

        # Initialize members of the class
        self.enter = enter 
        self.scope = scope 
        self.timestamp = timestamp 
        self.user = user 

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

        enter = dictionary.get("enter") if dictionary.get("enter") else None
        scope = dictionary.get("scope") if dictionary.get("scope") else None
        timestamp = dictionary.get("timestamp") if dictionary.get("timestamp") else None
        user = dictionary.get("user") if dictionary.get("user") else None
        # Return an object of this model
        return cls(enter,
                   scope,
                   timestamp,
                   user)