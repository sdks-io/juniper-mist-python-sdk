# -*- coding: utf-8 -*-

"""
mistapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from mistapi.api_helper import APIHelper


class Action(object):

    """Implementation of the 'Action' model.

    TODO: type model description here.

    Attributes:
        action (Action1Enum): TODO: type description here.
        dst_tag (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "action": 'action',
        "dst_tag": 'dst_tag'
    }

    _optionals = [
        'action',
        'dst_tag',
    ]

    def __init__(self,
                 action=APIHelper.SKIP,
                 dst_tag=APIHelper.SKIP):
        """Constructor for the Action class"""

        # Initialize members of the class
        if action is not APIHelper.SKIP:
            self.action = action 
        if dst_tag is not APIHelper.SKIP:
            self.dst_tag = dst_tag 

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

        action = dictionary.get("action") if dictionary.get("action") else APIHelper.SKIP
        dst_tag = dictionary.get("dst_tag") if dictionary.get("dst_tag") else APIHelper.SKIP
        # Return an object of this model
        return cls(action,
                   dst_tag)
