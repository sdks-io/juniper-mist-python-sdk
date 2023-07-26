# -*- coding: utf-8 -*-

"""
mistapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from mistapi.api_helper import APIHelper


class Ips1(object):

    """Implementation of the 'Ips1' model.

    TODO: type model description here.

    Attributes:
        vlan_1 (string): TODO: type description here.
        vlan_193 (string): TODO: type description here.
        vlan_3157 (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "vlan_1": 'vlan1',
        "vlan_193": 'vlan193',
        "vlan_3157": 'vlan3157'
    }

    _optionals = [
        'vlan_1',
        'vlan_193',
        'vlan_3157',
    ]

    def __init__(self,
                 vlan_1=APIHelper.SKIP,
                 vlan_193=APIHelper.SKIP,
                 vlan_3157=APIHelper.SKIP):
        """Constructor for the Ips1 class"""

        # Initialize members of the class
        if vlan_1 is not APIHelper.SKIP:
            self.vlan_1 = vlan_1 
        if vlan_193 is not APIHelper.SKIP:
            self.vlan_193 = vlan_193 
        if vlan_3157 is not APIHelper.SKIP:
            self.vlan_3157 = vlan_3157 

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

        vlan_1 = dictionary.get("vlan1") if dictionary.get("vlan1") else APIHelper.SKIP
        vlan_193 = dictionary.get("vlan193") if dictionary.get("vlan193") else APIHelper.SKIP
        vlan_3157 = dictionary.get("vlan3157") if dictionary.get("vlan3157") else APIHelper.SKIP
        # Return an object of this model
        return cls(vlan_1,
                   vlan_193,
                   vlan_3157)