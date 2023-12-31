# -*- coding: utf-8 -*-

"""
mistapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class ApiV1MobileVerifyResponse(object):

    """Implementation of the 'Api V1 Mobile Verify Response' model.

    TODO: type model description here.

    Attributes:
        name (string): TODO: type description here.
        org_id (uuid|string): TODO: type description here.
        secret (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "name": 'name',
        "org_id": 'org_id',
        "secret": 'secret'
    }

    def __init__(self,
                 name=None,
                 org_id=None,
                 secret=None):
        """Constructor for the ApiV1MobileVerifyResponse class"""

        # Initialize members of the class
        self.name = name 
        self.org_id = org_id 
        self.secret = secret 

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

        name = dictionary.get("name") if dictionary.get("name") else None
        org_id = dictionary.get("org_id") if dictionary.get("org_id") else None
        secret = dictionary.get("secret") if dictionary.get("secret") else None
        # Return an object of this model
        return cls(name,
                   org_id,
                   secret)
