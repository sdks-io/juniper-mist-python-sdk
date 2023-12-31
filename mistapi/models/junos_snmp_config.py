# -*- coding: utf-8 -*-

"""
mistapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from mistapi.api_helper import APIHelper
from mistapi.models.client_list import ClientList
from mistapi.models.trap_group import TrapGroup
from mistapi.models.v_2_c_config import V2cConfig
from mistapi.models.v_3_config import V3Config
from mistapi.models.views import Views


class JunosSnmpConfig(object):

    """Implementation of the 'junos_snmp_config' model.

    TODO: type model description here.

    Attributes:
        client_list (list of ClientList): TODO: type description here.
        contact (string): TODO: type description here.
        description (string): TODO: type description here.
        enabled (bool): TODO: type description here.
        engine_id (EngineIdEnum): TODO: type description here.
        location (string): TODO: type description here.
        name (string): TODO: type description here.
        network (string): TODO: type description here.
        trap_groups (list of TrapGroup): TODO: type description here.
        v_2_c_config (list of V2cConfig): TODO: type description here.
        v_3_config (V3Config): TODO: type description here.
        views (Views): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "client_list": 'client_list',
        "contact": 'contact',
        "description": 'description',
        "enabled": 'enabled',
        "engine_id": 'engine_id',
        "location": 'location',
        "name": 'name',
        "network": 'network',
        "trap_groups": 'trap_groups',
        "v_2_c_config": 'v2c_config',
        "v_3_config": 'v3_config',
        "views": 'views'
    }

    _optionals = [
        'client_list',
        'contact',
        'description',
        'enabled',
        'engine_id',
        'location',
        'name',
        'network',
        'trap_groups',
        'v_2_c_config',
        'v_3_config',
        'views',
    ]

    def __init__(self,
                 client_list=APIHelper.SKIP,
                 contact=APIHelper.SKIP,
                 description=APIHelper.SKIP,
                 enabled=True,
                 engine_id=APIHelper.SKIP,
                 location=APIHelper.SKIP,
                 name=APIHelper.SKIP,
                 network='default',
                 trap_groups=APIHelper.SKIP,
                 v_2_c_config=APIHelper.SKIP,
                 v_3_config=APIHelper.SKIP,
                 views=APIHelper.SKIP):
        """Constructor for the JunosSnmpConfig class"""

        # Initialize members of the class
        if client_list is not APIHelper.SKIP:
            self.client_list = client_list 
        if contact is not APIHelper.SKIP:
            self.contact = contact 
        if description is not APIHelper.SKIP:
            self.description = description 
        self.enabled = enabled 
        if engine_id is not APIHelper.SKIP:
            self.engine_id = engine_id 
        if location is not APIHelper.SKIP:
            self.location = location 
        if name is not APIHelper.SKIP:
            self.name = name 
        self.network = network 
        if trap_groups is not APIHelper.SKIP:
            self.trap_groups = trap_groups 
        if v_2_c_config is not APIHelper.SKIP:
            self.v_2_c_config = v_2_c_config 
        if v_3_config is not APIHelper.SKIP:
            self.v_3_config = v_3_config 
        if views is not APIHelper.SKIP:
            self.views = views 

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

        client_list = None
        if dictionary.get('client_list') is not None:
            client_list = [ClientList.from_dictionary(x) for x in dictionary.get('client_list')]
        else:
            client_list = APIHelper.SKIP
        contact = dictionary.get("contact") if dictionary.get("contact") else APIHelper.SKIP
        description = dictionary.get("description") if dictionary.get("description") else APIHelper.SKIP
        enabled = dictionary.get("enabled") if dictionary.get("enabled") else True
        engine_id = dictionary.get("engine_id") if dictionary.get("engine_id") else APIHelper.SKIP
        location = dictionary.get("location") if dictionary.get("location") else APIHelper.SKIP
        name = dictionary.get("name") if dictionary.get("name") else APIHelper.SKIP
        network = dictionary.get("network") if dictionary.get("network") else 'default'
        trap_groups = None
        if dictionary.get('trap_groups') is not None:
            trap_groups = [TrapGroup.from_dictionary(x) for x in dictionary.get('trap_groups')]
        else:
            trap_groups = APIHelper.SKIP
        v_2_c_config = None
        if dictionary.get('v2c_config') is not None:
            v_2_c_config = [V2cConfig.from_dictionary(x) for x in dictionary.get('v2c_config')]
        else:
            v_2_c_config = APIHelper.SKIP
        v_3_config = V3Config.from_dictionary(dictionary.get('v3_config')) if 'v3_config' in dictionary.keys() else APIHelper.SKIP
        views = Views.from_dictionary(dictionary.get('views')) if 'views' in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(client_list,
                   contact,
                   description,
                   enabled,
                   engine_id,
                   location,
                   name,
                   network,
                   trap_groups,
                   v_2_c_config,
                   v_3_config,
                   views)
