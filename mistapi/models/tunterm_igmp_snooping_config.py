# -*- coding: utf-8 -*-

"""
mistapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from mistapi.api_helper import APIHelper
from mistapi.models.querier import Querier


class TuntermIgmpSnoopingConfig(object):

    """Implementation of the 'TuntermIgmpSnoopingConfig' model.

    TODO: type model description here.

    Attributes:
        enabled (bool): TODO: type description here.
        querier (Querier): TODO: type description here.
        vlan_ids (list of int): the list of vlans on which tunterm performs
            IGMP snooping

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "enabled": 'enabled',
        "querier": 'querier',
        "vlan_ids": 'vlan_ids'
    }

    _optionals = [
        'enabled',
        'querier',
        'vlan_ids',
    ]

    def __init__(self,
                 enabled=False,
                 querier=APIHelper.SKIP,
                 vlan_ids=APIHelper.SKIP):
        """Constructor for the TuntermIgmpSnoopingConfig class"""

        # Initialize members of the class
        self.enabled = enabled 
        if querier is not APIHelper.SKIP:
            self.querier = querier 
        if vlan_ids is not APIHelper.SKIP:
            self.vlan_ids = vlan_ids 

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

        enabled = dictionary.get("enabled") if dictionary.get("enabled") else False
        querier = Querier.from_dictionary(dictionary.get('querier')) if 'querier' in dictionary.keys() else APIHelper.SKIP
        vlan_ids = dictionary.get("vlan_ids") if dictionary.get("vlan_ids") else APIHelper.SKIP
        # Return an object of this model
        return cls(enabled,
                   querier,
                   vlan_ids)
