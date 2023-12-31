# -*- coding: utf-8 -*-

"""
mistapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class ApiV1RecoverRequest(object):

    """Implementation of the 'Api V1 Recover Request' model.

    TODO: type model description here.

    Attributes:
        email (string): TODO: type description here.
        recaptcha (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "email": 'email',
        "recaptcha": 'recaptcha'
    }

    def __init__(self,
                 email=None,
                 recaptcha=None):
        """Constructor for the ApiV1RecoverRequest class"""

        # Initialize members of the class
        self.email = email 
        self.recaptcha = recaptcha 

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

        email = dictionary.get("email") if dictionary.get("email") else None
        recaptcha = dictionary.get("recaptcha") if dictionary.get("recaptcha") else None
        # Return an object of this model
        return cls(email,
                   recaptcha)
