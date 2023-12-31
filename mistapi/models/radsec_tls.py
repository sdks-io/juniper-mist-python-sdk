# -*- coding: utf-8 -*-

"""
mistapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from mistapi.api_helper import APIHelper


class RadsecTls(object):

    """Implementation of the 'RadsecTls' model.

    TODO: type model description here.

    Attributes:
        keypair (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "keypair": 'keypair'
    }

    _optionals = [
        'keypair',
    ]

    def __init__(self,
                 keypair=APIHelper.SKIP):
        """Constructor for the RadsecTls class"""

        # Initialize members of the class
        if keypair is not APIHelper.SKIP:
            self.keypair = keypair 

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

        keypair = dictionary.get("keypair") if dictionary.get("keypair") else APIHelper.SKIP
        # Return an object of this model
        return cls(keypair)
