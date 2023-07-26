# -*- coding: utf-8 -*-

"""
mistapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from mistapi.api_helper import APIHelper
from mistapi.models.junos_port_config import JunosPortConfig
from mistapi.models.switch_mgmt_1 import SwitchMgmt1


class Rules4(object):

    """Implementation of the 'Rules4' model.

    TODO: type model description here.

    Attributes:
        additional_config_cmds (list of string): TODO: type description here.
        match_role (string): role to match
        name (string): TODO: type description here.
        port_config (dict): TODO: type description here.
        switch_mgmt (SwitchMgmt1): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "additional_config_cmds": 'additional_config_cmds',
        "match_role": 'match_role',
        "name": 'name',
        "port_config": 'port_config',
        "switch_mgmt": 'switch_mgmt'
    }

    _optionals = [
        'additional_config_cmds',
        'match_role',
        'name',
        'port_config',
        'switch_mgmt',
    ]

    def __init__(self,
                 additional_config_cmds=APIHelper.SKIP,
                 match_role=APIHelper.SKIP,
                 name=APIHelper.SKIP,
                 port_config=APIHelper.SKIP,
                 switch_mgmt=APIHelper.SKIP):
        """Constructor for the Rules4 class"""

        # Initialize members of the class
        if additional_config_cmds is not APIHelper.SKIP:
            self.additional_config_cmds = additional_config_cmds 
        if match_role is not APIHelper.SKIP:
            self.match_role = match_role 
        if name is not APIHelper.SKIP:
            self.name = name 
        if port_config is not APIHelper.SKIP:
            self.port_config = port_config 
        if switch_mgmt is not APIHelper.SKIP:
            self.switch_mgmt = switch_mgmt 

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

        additional_config_cmds = dictionary.get("additional_config_cmds") if dictionary.get("additional_config_cmds") else APIHelper.SKIP
        match_role = dictionary.get("match_role") if dictionary.get("match_role") else APIHelper.SKIP
        name = dictionary.get("name") if dictionary.get("name") else APIHelper.SKIP
        port_config = JunosPortConfig.from_dictionary(dictionary.get('port_config')) if 'port_config' in dictionary.keys() else APIHelper.SKIP
        switch_mgmt = SwitchMgmt1.from_dictionary(dictionary.get('switch_mgmt')) if 'switch_mgmt' in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(additional_config_cmds,
                   match_role,
                   name,
                   port_config,
                   switch_mgmt)
