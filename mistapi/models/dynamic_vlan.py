# -*- coding: utf-8 -*-

"""
mistapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from mistapi.api_helper import APIHelper


class DynamicVlan(object):

    """Implementation of the 'DynamicVlan' model.

    optional dynamic vlan

    Attributes:
        default_vlan_id (int): TODO: type description here.
        enabled (bool): TODO: type description here.
        mtype (string): TODO: type description here.
        vlans (dict): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "default_vlan_id": 'default_vlan_id',
        "enabled": 'enabled',
        "mtype": 'type',
        "vlans": 'vlans'
    }

    _optionals = [
        'default_vlan_id',
        'enabled',
        'mtype',
        'vlans',
    ]

    def __init__(self,
                 default_vlan_id=APIHelper.SKIP,
                 enabled=APIHelper.SKIP,
                 mtype=APIHelper.SKIP,
                 vlans=APIHelper.SKIP):
        """Constructor for the DynamicVlan class"""

        # Initialize members of the class
        if default_vlan_id is not APIHelper.SKIP:
            self.default_vlan_id = default_vlan_id 
        if enabled is not APIHelper.SKIP:
            self.enabled = enabled 
        if mtype is not APIHelper.SKIP:
            self.mtype = mtype 
        if vlans is not APIHelper.SKIP:
            self.vlans = vlans 

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

        default_vlan_id = dictionary.get("default_vlan_id") if dictionary.get("default_vlan_id") else APIHelper.SKIP
        enabled = dictionary.get("enabled") if "enabled" in dictionary.keys() else APIHelper.SKIP
        mtype = dictionary.get("type") if dictionary.get("type") else APIHelper.SKIP
        vlans = dictionary.get("vlans") if dictionary.get("vlans") else APIHelper.SKIP
        # Return an object of this model
        return cls(default_vlan_id,
                   enabled,
                   mtype,
                   vlans)