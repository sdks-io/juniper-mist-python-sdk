# -*- coding: utf-8 -*-

"""
mistapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from mistapi.api_helper import APIHelper


class LldpStat(object):

    """Implementation of the 'LldpStat' model.

    LLDP Stat (neighbor information, power negotiations)

    Attributes:
        chassis_id (string): TODO: type description here.
        lldp_med_supported (bool): whether it support LLDP-MED
        mgmt_addr (string): switch’s management address (if advertised), can
            be IPv4, IPv6, or MAC
        port_desc (string): port description, e.g. “2/20”, “Port 2 on
            Switch0”
        power_allocated (float): in mW, provided/allocated by PSE
        power_draw (float): in mW, total power needed by PD
        power_request_count (int): number of negotiations, if it keeps
            increasing, we don’t have a stable power
        power_requested (float): in mW, the current power requested by PD
        system_desc (string): description provided by switch, e.g. “HP J9729A
            2920-48G-POE+ Switch”
        system_name (string): name of the switch, e.g. “TC2-OWL-Stack-01”

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "chassis_id": 'chassis_id',
        "lldp_med_supported": 'lldp_med_supported',
        "mgmt_addr": 'mgmt_addr',
        "port_desc": 'port_desc',
        "power_allocated": 'power_allocated',
        "power_draw": 'power_draw',
        "power_request_count": 'power_request_count',
        "power_requested": 'power_requested',
        "system_desc": 'system_desc',
        "system_name": 'system_name'
    }

    _optionals = [
        'chassis_id',
        'lldp_med_supported',
        'mgmt_addr',
        'port_desc',
        'power_allocated',
        'power_draw',
        'power_request_count',
        'power_requested',
        'system_desc',
        'system_name',
    ]

    def __init__(self,
                 chassis_id=APIHelper.SKIP,
                 lldp_med_supported=APIHelper.SKIP,
                 mgmt_addr=APIHelper.SKIP,
                 port_desc=APIHelper.SKIP,
                 power_allocated=APIHelper.SKIP,
                 power_draw=APIHelper.SKIP,
                 power_request_count=APIHelper.SKIP,
                 power_requested=APIHelper.SKIP,
                 system_desc=APIHelper.SKIP,
                 system_name=APIHelper.SKIP):
        """Constructor for the LldpStat class"""

        # Initialize members of the class
        if chassis_id is not APIHelper.SKIP:
            self.chassis_id = chassis_id 
        if lldp_med_supported is not APIHelper.SKIP:
            self.lldp_med_supported = lldp_med_supported 
        if mgmt_addr is not APIHelper.SKIP:
            self.mgmt_addr = mgmt_addr 
        if port_desc is not APIHelper.SKIP:
            self.port_desc = port_desc 
        if power_allocated is not APIHelper.SKIP:
            self.power_allocated = power_allocated 
        if power_draw is not APIHelper.SKIP:
            self.power_draw = power_draw 
        if power_request_count is not APIHelper.SKIP:
            self.power_request_count = power_request_count 
        if power_requested is not APIHelper.SKIP:
            self.power_requested = power_requested 
        if system_desc is not APIHelper.SKIP:
            self.system_desc = system_desc 
        if system_name is not APIHelper.SKIP:
            self.system_name = system_name 

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

        chassis_id = dictionary.get("chassis_id") if dictionary.get("chassis_id") else APIHelper.SKIP
        lldp_med_supported = dictionary.get("lldp_med_supported") if "lldp_med_supported" in dictionary.keys() else APIHelper.SKIP
        mgmt_addr = dictionary.get("mgmt_addr") if dictionary.get("mgmt_addr") else APIHelper.SKIP
        port_desc = dictionary.get("port_desc") if dictionary.get("port_desc") else APIHelper.SKIP
        power_allocated = dictionary.get("power_allocated") if dictionary.get("power_allocated") else APIHelper.SKIP
        power_draw = dictionary.get("power_draw") if dictionary.get("power_draw") else APIHelper.SKIP
        power_request_count = dictionary.get("power_request_count") if dictionary.get("power_request_count") else APIHelper.SKIP
        power_requested = dictionary.get("power_requested") if dictionary.get("power_requested") else APIHelper.SKIP
        system_desc = dictionary.get("system_desc") if dictionary.get("system_desc") else APIHelper.SKIP
        system_name = dictionary.get("system_name") if dictionary.get("system_name") else APIHelper.SKIP
        # Return an object of this model
        return cls(chassis_id,
                   lldp_med_supported,
                   mgmt_addr,
                   port_desc,
                   power_allocated,
                   power_draw,
                   power_request_count,
                   power_requested,
                   system_desc,
                   system_name)