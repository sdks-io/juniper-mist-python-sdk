# -*- coding: utf-8 -*-

"""
mistapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from mistapi.api_helper import APIHelper


class WlanAirwatch(object):

    """Implementation of the 'wlan_airwatch' model.

    airwatch wlan settings

    Attributes:
        api_key (string): API Key
        console_url (string): console URL
        enabled (bool): TODO: type description here.
        password (string): password
        username (string): username

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "api_key": 'api_key',
        "console_url": 'console_url',
        "enabled": 'enabled',
        "password": 'password',
        "username": 'username'
    }

    _optionals = [
        'api_key',
        'console_url',
        'enabled',
        'password',
        'username',
    ]

    def __init__(self,
                 api_key=APIHelper.SKIP,
                 console_url=APIHelper.SKIP,
                 enabled=APIHelper.SKIP,
                 password=APIHelper.SKIP,
                 username=APIHelper.SKIP):
        """Constructor for the WlanAirwatch class"""

        # Initialize members of the class
        if api_key is not APIHelper.SKIP:
            self.api_key = api_key 
        if console_url is not APIHelper.SKIP:
            self.console_url = console_url 
        if enabled is not APIHelper.SKIP:
            self.enabled = enabled 
        if password is not APIHelper.SKIP:
            self.password = password 
        if username is not APIHelper.SKIP:
            self.username = username 

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

        api_key = dictionary.get("api_key") if dictionary.get("api_key") else APIHelper.SKIP
        console_url = dictionary.get("console_url") if dictionary.get("console_url") else APIHelper.SKIP
        enabled = dictionary.get("enabled") if "enabled" in dictionary.keys() else APIHelper.SKIP
        password = dictionary.get("password") if dictionary.get("password") else APIHelper.SKIP
        username = dictionary.get("username") if dictionary.get("username") else APIHelper.SKIP
        # Return an object of this model
        return cls(api_key,
                   console_url,
                   enabled,
                   password,
                   username)
