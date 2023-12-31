# -*- coding: utf-8 -*-

"""
mistapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from mistapi.api_helper import APIHelper


class Interface1(object):

    """Implementation of the 'Interface1' model.

    TODO: type model description here.

    Attributes:
        degraded (float): TODO: type description here.
        duration (float): TODO: type description here.
        interface_name (string): TODO: type description here.
        switch_mac (string): TODO: type description here.
        switch_name (string): TODO: type description here.
        total (float): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "degraded": 'degraded',
        "duration": 'duration',
        "interface_name": 'interface_name',
        "switch_mac": 'switch_mac',
        "switch_name": 'switch_name',
        "total": 'total'
    }

    _optionals = [
        'degraded',
        'duration',
        'interface_name',
        'switch_mac',
        'switch_name',
        'total',
    ]

    def __init__(self,
                 degraded=APIHelper.SKIP,
                 duration=APIHelper.SKIP,
                 interface_name=APIHelper.SKIP,
                 switch_mac=APIHelper.SKIP,
                 switch_name=APIHelper.SKIP,
                 total=APIHelper.SKIP):
        """Constructor for the Interface1 class"""

        # Initialize members of the class
        if degraded is not APIHelper.SKIP:
            self.degraded = degraded 
        if duration is not APIHelper.SKIP:
            self.duration = duration 
        if interface_name is not APIHelper.SKIP:
            self.interface_name = interface_name 
        if switch_mac is not APIHelper.SKIP:
            self.switch_mac = switch_mac 
        if switch_name is not APIHelper.SKIP:
            self.switch_name = switch_name 
        if total is not APIHelper.SKIP:
            self.total = total 

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

        degraded = dictionary.get("degraded") if dictionary.get("degraded") else APIHelper.SKIP
        duration = dictionary.get("duration") if dictionary.get("duration") else APIHelper.SKIP
        interface_name = dictionary.get("interface_name") if dictionary.get("interface_name") else APIHelper.SKIP
        switch_mac = dictionary.get("switch_mac") if dictionary.get("switch_mac") else APIHelper.SKIP
        switch_name = dictionary.get("switch_name") if dictionary.get("switch_name") else APIHelper.SKIP
        total = dictionary.get("total") if dictionary.get("total") else APIHelper.SKIP
        # Return an object of this model
        return cls(degraded,
                   duration,
                   interface_name,
                   switch_mac,
                   switch_name,
                   total)
