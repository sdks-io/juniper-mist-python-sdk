# -*- coding: utf-8 -*-

"""
mistapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class ApiV1SelfOauthResponse1(object):

    """Implementation of the 'Api V1 Self Oauth Response1' model.

    TODO: type model description here.

    Attributes:
        action (string): TODO: type description here.
        id (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "action": 'action',
        "id": 'id'
    }

    def __init__(self,
                 action=None,
                 id=None):
        """Constructor for the ApiV1SelfOauthResponse1 class"""

        # Initialize members of the class
        self.action = action 
        self.id = id 

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
        # Return an object of this model
        return cls(action,
                   id)
