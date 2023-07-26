# -*- coding: utf-8 -*-

"""
mistapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from mistapi.api_helper import APIHelper
from mistapi.models.services import Services


class WlanBonjour(object):

    """Implementation of the 'wlan_bonjour' model.

    bonjour gateway wlan settings

    Attributes:
        additional_vlan_ids (list of int): additional VLAN IDs (on the LAN
            side or from other WLANs) should we be forwarding bonjour
            queries/responses
        enabled (bool): whether to enable bonjour for this WLAN. Once enabled,
            limit_bcast is assumed true, allow_mdns is assumed false
        services (dict): what services are allowed

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "additional_vlan_ids": 'additional_vlan_ids',
        "services": 'services',
        "enabled": 'enabled'
    }

    _optionals = [
        'enabled',
    ]

    def __init__(self,
                 additional_vlan_ids=None,
                 services=None,
                 enabled=False):
        """Constructor for the WlanBonjour class"""

        # Initialize members of the class
        self.additional_vlan_ids = additional_vlan_ids 
        self.enabled = enabled 
        self.services = services 

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

        additional_vlan_ids = dictionary.get("additional_vlan_ids") if dictionary.get("additional_vlan_ids") else None
        services = Services.from_dictionary(dictionary.get('services')) if dictionary.get('services') else None
        enabled = dictionary.get("enabled") if dictionary.get("enabled") else False
        # Return an object of this model
        return cls(additional_vlan_ids,
                   services,
                   enabled)
