# -*- coding: utf-8 -*-

"""
mistapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class ApiV1ConstApChannelsResponse(object):

    """Implementation of the 'Api V1 Const Ap Channels Response' model.

    TODO: type model description here.

    Attributes:
        band_24_channels (dict): The property key is the channel width
        band_24_enabled (bool): TODO: type description here.
        band_5_channels (dict): The property key is the channel width
        band_5_enabled (bool): TODO: type description here.
        code (int): TODO: type description here.
        dfs_ok (bool): TODO: type description here.
        key (string): TODO: type description here.
        name (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "band_24_channels": 'band24_channels',
        "band_24_enabled": 'band24_enabled',
        "band_5_channels": 'band5_channels',
        "band_5_enabled": 'band5_enabled',
        "code": 'code',
        "dfs_ok": 'dfs_ok',
        "key": 'key',
        "name": 'name'
    }

    def __init__(self,
                 band_24_channels=None,
                 band_24_enabled=None,
                 band_5_channels=None,
                 band_5_enabled=None,
                 code=None,
                 dfs_ok=None,
                 key=None,
                 name=None):
        """Constructor for the ApiV1ConstApChannelsResponse class"""

        # Initialize members of the class
        self.band_24_channels = band_24_channels 
        self.band_24_enabled = band_24_enabled 
        self.band_5_channels = band_5_channels 
        self.band_5_enabled = band_5_enabled 
        self.code = code 
        self.dfs_ok = dfs_ok 
        self.key = key 
        self.name = name 

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

        band_24_channels = dictionary.get("band24_channels") if dictionary.get("band24_channels") else None
        band_24_enabled = dictionary.get("band24_enabled") if "band24_enabled" in dictionary.keys() else None
        band_5_channels = dictionary.get("band5_channels") if dictionary.get("band5_channels") else None
        band_5_enabled = dictionary.get("band5_enabled") if "band5_enabled" in dictionary.keys() else None
        code = dictionary.get("code") if dictionary.get("code") else None
        dfs_ok = dictionary.get("dfs_ok") if "dfs_ok" in dictionary.keys() else None
        key = dictionary.get("key") if dictionary.get("key") else None
        name = dictionary.get("name") if dictionary.get("name") else None
        # Return an object of this model
        return cls(band_24_channels,
                   band_24_enabled,
                   band_5_channels,
                   band_5_enabled,
                   code,
                   dfs_ok,
                   key,
                   name)
