# -*- coding: utf-8 -*-

"""
mistapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from mistapi.api_helper import APIHelper


class Community(object):

    """Implementation of the 'Community' model.

    TODO: type model description here.

    Attributes:
        id (string): TODO: type description here.
        local_preference (int): TODO: type description here.
        vpn_name (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id": 'id',
        "local_preference": 'local_preference',
        "vpn_name": 'vpn_name'
    }

    _optionals = [
        'id',
        'local_preference',
        'vpn_name',
    ]

    def __init__(self,
                 id=APIHelper.SKIP,
                 local_preference=APIHelper.SKIP,
                 vpn_name=APIHelper.SKIP):
        """Constructor for the Community class"""

        # Initialize members of the class
        if id is not APIHelper.SKIP:
            self.id = id 
        if local_preference is not APIHelper.SKIP:
            self.local_preference = local_preference 
        if vpn_name is not APIHelper.SKIP:
            self.vpn_name = vpn_name 

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

        id = dictionary.get("id") if dictionary.get("id") else APIHelper.SKIP
        local_preference = dictionary.get("local_preference") if dictionary.get("local_preference") else APIHelper.SKIP
        vpn_name = dictionary.get("vpn_name") if dictionary.get("vpn_name") else APIHelper.SKIP
        # Return an object of this model
        return cls(id,
                   local_preference,
                   vpn_name)
