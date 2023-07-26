# -*- coding: utf-8 -*-

"""
mistapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from mistapi.api_helper import APIHelper
from mistapi.models.groups import Groups


class JunosVrrpConfig(object):

    """Implementation of the 'junos_vrrp_config' model.

    Junos VRRP config

    Attributes:
        enabled (bool): TODO: type description here.
        groups (Groups): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "enabled": 'enabled',
        "groups": 'groups'
    }

    _optionals = [
        'enabled',
        'groups',
    ]

    def __init__(self,
                 enabled=APIHelper.SKIP,
                 groups=APIHelper.SKIP):
        """Constructor for the JunosVrrpConfig class"""

        # Initialize members of the class
        if enabled is not APIHelper.SKIP:
            self.enabled = enabled 
        if groups is not APIHelper.SKIP:
            self.groups = groups 

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

        enabled = dictionary.get("enabled") if "enabled" in dictionary.keys() else APIHelper.SKIP
        groups = Groups.from_dictionary(dictionary.get('groups')) if 'groups' in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(enabled,
                   groups)