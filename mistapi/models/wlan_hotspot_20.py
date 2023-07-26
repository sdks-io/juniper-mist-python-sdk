# -*- coding: utf-8 -*-

"""
mistapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from mistapi.api_helper import APIHelper


class WlanHotspot20(object):

    """Implementation of the 'wlan_hotspot_20' model.

    hostspot 2.0 wlan settings

    Attributes:
        enabled (bool): whether to enable hotspot 2.0 config
        operators (list of string): list of operators to support, options:
            att, google, tmobile, charter, boingo, hughes_systique,
            single_digits, global_reach
        venue_name (string): venue name, default is site name

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "enabled": 'enabled',
        "operators": 'operators',
        "venue_name": 'venue_name'
    }

    _optionals = [
        'enabled',
        'operators',
        'venue_name',
    ]

    def __init__(self,
                 enabled=APIHelper.SKIP,
                 operators=APIHelper.SKIP,
                 venue_name=APIHelper.SKIP):
        """Constructor for the WlanHotspot20 class"""

        # Initialize members of the class
        if enabled is not APIHelper.SKIP:
            self.enabled = enabled 
        if operators is not APIHelper.SKIP:
            self.operators = operators 
        if venue_name is not APIHelper.SKIP:
            self.venue_name = venue_name 

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

        enabled = dictionary.get("enabled") if "enabled" in dictionary.keys() else APIHelper.SKIP
        operators = dictionary.get("operators") if dictionary.get("operators") else APIHelper.SKIP
        venue_name = dictionary.get("venue_name") if dictionary.get("venue_name") else APIHelper.SKIP
        # Return an object of this model
        return cls(enabled,
                   operators,
                   venue_name)
