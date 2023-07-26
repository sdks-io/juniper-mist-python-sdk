# -*- coding: utf-8 -*-

"""
mistapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from mistapi.api_helper import APIHelper


class VrrpGroup(object):

    """Implementation of the 'VrrpGroup' model.

    TODO: type model description here.

    Attributes:
        priority (int): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "priority": 'priority'
    }

    _optionals = [
        'priority',
    ]

    def __init__(self,
                 priority=APIHelper.SKIP):
        """Constructor for the VrrpGroup class"""

        # Initialize members of the class
        if priority is not APIHelper.SKIP:
            self.priority = priority 

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

        priority = dictionary.get("priority") if dictionary.get("priority") else APIHelper.SKIP
        # Return an object of this model
        return cls(priority)
