# -*- coding: utf-8 -*-

"""
mistapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from mistapi.api_helper import APIHelper
from mistapi.models.auth import Auth


class ApClientBridge(object):

    """Implementation of the 'ap_client_bridge' model.

    TODO: type model description here.

    Attributes:
        auth (Auth): TODO: type description here.
        enabled (bool): when acted as client bridge: * only 5G radio can be
            used * will not serve as AP on any radios
        ssid (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "auth": 'auth',
        "enabled": 'enabled',
        "ssid": 'ssid'
    }

    _optionals = [
        'auth',
        'enabled',
        'ssid',
    ]

    def __init__(self,
                 auth=APIHelper.SKIP,
                 enabled=APIHelper.SKIP,
                 ssid=APIHelper.SKIP):
        """Constructor for the ApClientBridge class"""

        # Initialize members of the class
        if auth is not APIHelper.SKIP:
            self.auth = auth 
        if enabled is not APIHelper.SKIP:
            self.enabled = enabled 
        if ssid is not APIHelper.SKIP:
            self.ssid = ssid 

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

        auth = Auth.from_dictionary(dictionary.get('auth')) if 'auth' in dictionary.keys() else APIHelper.SKIP
        enabled = dictionary.get("enabled") if "enabled" in dictionary.keys() else APIHelper.SKIP
        ssid = dictionary.get("ssid") if dictionary.get("ssid") else APIHelper.SKIP
        # Return an object of this model
        return cls(auth,
                   enabled,
                   ssid)
