# -*- coding: utf-8 -*-

"""
mistapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class Zone2(object):

    """Implementation of the 'Zone2' model.

    TODO: type model description here.

    Attributes:
        id (uuid|string): TODO: type description here.
        since (float): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id": 'id',
        "since": 'since'
    }

    def __init__(self,
                 id=None,
                 since=None):
        """Constructor for the Zone2 class"""

        # Initialize members of the class
        self.id = id 
        self.since = since 

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
        since = dictionary.get("since") if dictionary.get("since") else None
        # Return an object of this model
        return cls(id,
                   since)
