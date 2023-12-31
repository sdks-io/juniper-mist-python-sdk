# -*- coding: utf-8 -*-

"""
mistapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from mistapi.api_helper import APIHelper
from mistapi.models.networks_1 import Networks1


class JunosOspfAreas(object):

    """Implementation of the 'junos_ospf_areas' model.

    Junos OSPF areas

    Attributes:
        include_loopback (bool): TODO: type description here.
        networks (dict): networks to participate in an OSPF area. The property
            key is the network name
        mtype (Type25Enum): OSPF type, default (default) / stub / nssa

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "include_loopback": 'include_loopback',
        "networks": 'networks',
        "mtype": 'type'
    }

    _optionals = [
        'include_loopback',
        'networks',
        'mtype',
    ]

    def __init__(self,
                 include_loopback=False,
                 networks=APIHelper.SKIP,
                 mtype='default'):
        """Constructor for the JunosOspfAreas class"""

        # Initialize members of the class
        self.include_loopback = include_loopback 
        if networks is not APIHelper.SKIP:
            self.networks = networks 
        self.mtype = mtype 

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

        include_loopback = dictionary.get("include_loopback") if dictionary.get("include_loopback") else False
        networks = Networks1.from_dictionary(dictionary.get('networks')) if 'networks' in dictionary.keys() else APIHelper.SKIP
        mtype = dictionary.get("type") if dictionary.get("type") else 'default'
        # Return an object of this model
        return cls(include_loopback,
                   networks,
                   mtype)
