# -*- coding: utf-8 -*-

"""
mistapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from mistapi.api_helper import APIHelper


class Floorplan(object):

    """Implementation of the 'Floorplan' model.

    TODO: type model description here.

    Attributes:
        action (string): TODO: type description here.
        id (uuid|string): TODO: type description here.
        map_id (uuid|string): TODO: type description here.
        name (string): TODO: type description here.
        reason (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "action": 'action',
        "id": 'id',
        "map_id": 'map_id',
        "name": 'name',
        "reason": 'reason'
    }

    _optionals = [
        'reason',
    ]

    def __init__(self,
                 action=None,
                 id=None,
                 map_id=None,
                 name=None,
                 reason=APIHelper.SKIP):
        """Constructor for the Floorplan class"""

        # Initialize members of the class
        self.action = action 
        self.id = id 
        self.map_id = map_id 
        self.name = name 
        if reason is not APIHelper.SKIP:
            self.reason = reason 

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

        action = dictionary.get("action") if dictionary.get("action") else None
        id = dictionary.get("id") if dictionary.get("id") else None
        map_id = dictionary.get("map_id") if dictionary.get("map_id") else None
        name = dictionary.get("name") if dictionary.get("name") else None
        reason = dictionary.get("reason") if dictionary.get("reason") else APIHelper.SKIP
        # Return an object of this model
        return cls(action,
                   id,
                   map_id,
                   name,
                   reason)
