# -*- coding: utf-8 -*-

"""
mistapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from mistapi.api_helper import APIHelper


class Aps4(object):

    """Implementation of the 'Aps4' model.

    TODO: type model description here.

    Attributes:
        hostname (string): TODO: type description here.
        mac (string): TODO: type description here.
        poe_status (bool): TODO: type description here.
        port (string): TODO: type description here.
        port_id (string): TODO: type description here.
        power_draw (float): TODO: type description here.
        when (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "hostname": 'hostname',
        "mac": 'mac',
        "poe_status": 'poe_status',
        "port": 'port',
        "port_id": 'port_id',
        "power_draw": 'power_draw',
        "when": 'when'
    }

    _optionals = [
        'hostname',
        'mac',
        'poe_status',
        'port',
        'port_id',
        'power_draw',
        'when',
    ]

    def __init__(self,
                 hostname=APIHelper.SKIP,
                 mac=APIHelper.SKIP,
                 poe_status=APIHelper.SKIP,
                 port=APIHelper.SKIP,
                 port_id=APIHelper.SKIP,
                 power_draw=APIHelper.SKIP,
                 when=APIHelper.SKIP):
        """Constructor for the Aps4 class"""

        # Initialize members of the class
        if hostname is not APIHelper.SKIP:
            self.hostname = hostname 
        if mac is not APIHelper.SKIP:
            self.mac = mac 
        if poe_status is not APIHelper.SKIP:
            self.poe_status = poe_status 
        if port is not APIHelper.SKIP:
            self.port = port 
        if port_id is not APIHelper.SKIP:
            self.port_id = port_id 
        if power_draw is not APIHelper.SKIP:
            self.power_draw = power_draw 
        if when is not APIHelper.SKIP:
            self.when = when 

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

        hostname = dictionary.get("hostname") if dictionary.get("hostname") else APIHelper.SKIP
        mac = dictionary.get("mac") if dictionary.get("mac") else APIHelper.SKIP
        poe_status = dictionary.get("poe_status") if "poe_status" in dictionary.keys() else APIHelper.SKIP
        port = dictionary.get("port") if dictionary.get("port") else APIHelper.SKIP
        port_id = dictionary.get("port_id") if dictionary.get("port_id") else APIHelper.SKIP
        power_draw = dictionary.get("power_draw") if dictionary.get("power_draw") else APIHelper.SKIP
        when = dictionary.get("when") if dictionary.get("when") else APIHelper.SKIP
        # Return an object of this model
        return cls(hostname,
                   mac,
                   poe_status,
                   port,
                   port_id,
                   power_draw,
                   when)