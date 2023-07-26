# -*- coding: utf-8 -*-

"""
mistapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from mistapi.api_helper import APIHelper


class V2cConfig(object):

    """Implementation of the 'V2cConfig' model.

    TODO: type model description here.

    Attributes:
        authorization (string): TODO: type description here.
        client_list_name (string): client_list_name here should refer to
            client_list above
        community_name (string): TODO: type description here.
        view (string): view name here should be defined in views above

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "authorization": 'authorization',
        "client_list_name": 'client_list_name',
        "community_name": 'community_name',
        "view": 'view'
    }

    _optionals = [
        'authorization',
        'client_list_name',
        'community_name',
        'view',
    ]

    def __init__(self,
                 authorization=APIHelper.SKIP,
                 client_list_name=APIHelper.SKIP,
                 community_name=APIHelper.SKIP,
                 view=APIHelper.SKIP):
        """Constructor for the V2cConfig class"""

        # Initialize members of the class
        if authorization is not APIHelper.SKIP:
            self.authorization = authorization 
        if client_list_name is not APIHelper.SKIP:
            self.client_list_name = client_list_name 
        if community_name is not APIHelper.SKIP:
            self.community_name = community_name 
        if view is not APIHelper.SKIP:
            self.view = view 

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

        authorization = dictionary.get("authorization") if dictionary.get("authorization") else APIHelper.SKIP
        client_list_name = dictionary.get("client_list_name") if dictionary.get("client_list_name") else APIHelper.SKIP
        community_name = dictionary.get("community_name") if dictionary.get("community_name") else APIHelper.SKIP
        view = dictionary.get("view") if dictionary.get("view") else APIHelper.SKIP
        # Return an object of this model
        return cls(authorization,
                   client_list_name,
                   community_name,
                   view)
