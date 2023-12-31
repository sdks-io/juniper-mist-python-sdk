# -*- coding: utf-8 -*-

"""
mistapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from mistapi.api_helper import APIHelper
from mistapi.models.networks_2 import Networks2


class JunosVrrpGroup(object):

    """Implementation of the 'junos_vrrp_group' model.

    Junos VRRP group

    Attributes:
        auth_key (string): if `auth_type`==`md5`
        auth_password (string): if `auth_type`==`simple`
        auth_type (AuthType1Enum): TODO: type description here.
        networks (dict): The property key is the network name

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "auth_key": 'auth_key',
        "auth_password": 'auth_password',
        "auth_type": 'auth_type',
        "networks": 'networks'
    }

    _optionals = [
        'auth_key',
        'auth_password',
        'auth_type',
        'networks',
    ]

    def __init__(self,
                 auth_key=APIHelper.SKIP,
                 auth_password=APIHelper.SKIP,
                 auth_type='md5',
                 networks=APIHelper.SKIP):
        """Constructor for the JunosVrrpGroup class"""

        # Initialize members of the class
        if auth_key is not APIHelper.SKIP:
            self.auth_key = auth_key 
        if auth_password is not APIHelper.SKIP:
            self.auth_password = auth_password 
        self.auth_type = auth_type 
        if networks is not APIHelper.SKIP:
            self.networks = networks 

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

        auth_key = dictionary.get("auth_key") if dictionary.get("auth_key") else APIHelper.SKIP
        auth_password = dictionary.get("auth_password") if dictionary.get("auth_password") else APIHelper.SKIP
        auth_type = dictionary.get("auth_type") if dictionary.get("auth_type") else 'md5'
        networks = Networks2.from_dictionary(dictionary.get('networks')) if 'networks' in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(auth_key,
                   auth_password,
                   auth_type,
                   networks)
