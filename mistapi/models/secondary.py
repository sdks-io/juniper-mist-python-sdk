# -*- coding: utf-8 -*-

"""
mistapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from mistapi.api_helper import APIHelper


class Secondary(object):

    """Implementation of the 'Secondary' model.

    TODO: type model description here.

    Attributes:
        num_hosts (string): TODO: type description here.
        wan_names (list of string): optional, only needed if
            `vars_only`==`false`

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "num_hosts": 'num_hosts',
        "wan_names": 'wan_names'
    }

    _optionals = [
        'num_hosts',
        'wan_names',
    ]

    def __init__(self,
                 num_hosts=APIHelper.SKIP,
                 wan_names=APIHelper.SKIP):
        """Constructor for the Secondary class"""

        # Initialize members of the class
        if num_hosts is not APIHelper.SKIP:
            self.num_hosts = num_hosts 
        if wan_names is not APIHelper.SKIP:
            self.wan_names = wan_names 

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

        num_hosts = dictionary.get("num_hosts") if dictionary.get("num_hosts") else APIHelper.SKIP
        wan_names = dictionary.get("wan_names") if dictionary.get("wan_names") else APIHelper.SKIP
        # Return an object of this model
        return cls(num_hosts,
                   wan_names)