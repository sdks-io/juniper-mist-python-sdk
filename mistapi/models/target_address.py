# -*- coding: utf-8 -*-

"""
mistapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from mistapi.api_helper import APIHelper


class TargetAddress(object):

    """Implementation of the 'TargetAddress' model.

    TODO: type model description here.

    Attributes:
        address (string): TODO: type description here.
        address_mask (string): TODO: type description here.
        port (int): TODO: type description here.
        tag_list (string): <refer to notify tag, can be multiple with blank
        target_address_name (string): TODO: type description here.
        target_parameters (string): refer to notify target parameters name

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "address": 'address',
        "address_mask": 'address_mask',
        "port": 'port',
        "tag_list": 'tag_list',
        "target_address_name": 'target_address_name',
        "target_parameters": 'target_parameters'
    }

    _optionals = [
        'address',
        'address_mask',
        'port',
        'tag_list',
        'target_address_name',
        'target_parameters',
    ]

    def __init__(self,
                 address=APIHelper.SKIP,
                 address_mask=APIHelper.SKIP,
                 port=161,
                 tag_list=APIHelper.SKIP,
                 target_address_name=APIHelper.SKIP,
                 target_parameters=APIHelper.SKIP):
        """Constructor for the TargetAddress class"""

        # Initialize members of the class
        if address is not APIHelper.SKIP:
            self.address = address 
        if address_mask is not APIHelper.SKIP:
            self.address_mask = address_mask 
        self.port = port 
        if tag_list is not APIHelper.SKIP:
            self.tag_list = tag_list 
        if target_address_name is not APIHelper.SKIP:
            self.target_address_name = target_address_name 
        if target_parameters is not APIHelper.SKIP:
            self.target_parameters = target_parameters 

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

        address = dictionary.get("address") if dictionary.get("address") else APIHelper.SKIP
        address_mask = dictionary.get("address_mask") if dictionary.get("address_mask") else APIHelper.SKIP
        port = dictionary.get("port") if dictionary.get("port") else 161
        tag_list = dictionary.get("tag_list") if dictionary.get("tag_list") else APIHelper.SKIP
        target_address_name = dictionary.get("target_address_name") if dictionary.get("target_address_name") else APIHelper.SKIP
        target_parameters = dictionary.get("target_parameters") if dictionary.get("target_parameters") else APIHelper.SKIP
        # Return an object of this model
        return cls(address,
                   address_mask,
                   port,
                   tag_list,
                   target_address_name,
                   target_parameters)
