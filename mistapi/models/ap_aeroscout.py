# -*- coding: utf-8 -*-

"""
mistapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from mistapi.api_helper import APIHelper


class ApAeroscout(object):

    """Implementation of the 'ap_aeroscout' model.

    Aeroscout AP settings

    Attributes:
        enabled (bool): whether to enable aeroscout config
        host (string): required if enabled, aeroscout server host
        locate_connected (bool): whether to enable the feature to allow
            wireless clients data received and sent to AES server for location
            calculation

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "enabled": 'enabled',
        "host": 'host',
        "locate_connected": 'locate_connected'
    }

    _optionals = [
        'enabled',
        'host',
        'locate_connected',
    ]

    _nullables = [
        'host',
    ]

    def __init__(self,
                 enabled=False,
                 host=APIHelper.SKIP,
                 locate_connected=APIHelper.SKIP):
        """Constructor for the ApAeroscout class"""

        # Initialize members of the class
        self.enabled = enabled 
        if host is not APIHelper.SKIP:
            self.host = host 
        if locate_connected is not APIHelper.SKIP:
            self.locate_connected = locate_connected 

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
        host = dictionary.get("host") if "host" in dictionary.keys() else APIHelper.SKIP
        locate_connected = dictionary.get("locate_connected") if "locate_connected" in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(enabled,
                   host,
                   locate_connected)