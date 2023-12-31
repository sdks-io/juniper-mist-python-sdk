# -*- coding: utf-8 -*-

"""
mistapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class DeviceRadioChannels(object):

    """Implementation of the 'DeviceRadioChannels' model.

    TODO: type model description here.

    Attributes:
        band_24_40_mhz_allowed (bool): TODO: type description here.
        band_24_channels (object): TODO: type description here.
        band_24_enabled (bool): TODO: type description here.
        band_5_channels (object): TODO: type description here.
        band_5_enabled (bool): TODO: type description here.
        certified (bool): TODO: type description here.
        code (int): TODO: type description here.
        dfs_ok (bool): TODO: type description here.
        key (string): TODO: type description here.
        name (string): TODO: type description here.
        uses (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "band_24_40_mhz_allowed": 'band24_40mhz_allowed',
        "band_24_channels": 'band24_channels',
        "band_24_enabled": 'band24_enabled',
        "band_5_channels": 'band5_channels',
        "band_5_enabled": 'band5_enabled',
        "certified": 'certified',
        "code": 'code',
        "dfs_ok": 'dfs_ok',
        "key": 'key',
        "name": 'name',
        "uses": 'uses'
    }

    def __init__(self,
                 band_24_40_mhz_allowed=None,
                 band_24_channels=None,
                 band_24_enabled=None,
                 band_5_channels=None,
                 band_5_enabled=None,
                 certified=None,
                 code=None,
                 dfs_ok=None,
                 key=None,
                 name=None,
                 uses=None):
        """Constructor for the DeviceRadioChannels class"""

        # Initialize members of the class
        self.band_24_40_mhz_allowed = band_24_40_mhz_allowed 
        self.band_24_channels = band_24_channels 
        self.band_24_enabled = band_24_enabled 
        self.band_5_channels = band_5_channels 
        self.band_5_enabled = band_5_enabled 
        self.certified = certified 
        self.code = code 
        self.dfs_ok = dfs_ok 
        self.key = key 
        self.name = name 
        self.uses = uses 

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

        band_24_40_mhz_allowed = dictionary.get("band24_40mhz_allowed") if "band24_40mhz_allowed" in dictionary.keys() else None
        band_24_channels = dictionary.get("band24_channels") if dictionary.get("band24_channels") else None
        band_24_enabled = dictionary.get("band24_enabled") if "band24_enabled" in dictionary.keys() else None
        band_5_channels = dictionary.get("band5_channels") if dictionary.get("band5_channels") else None
        band_5_enabled = dictionary.get("band5_enabled") if "band5_enabled" in dictionary.keys() else None
        certified = dictionary.get("certified") if "certified" in dictionary.keys() else None
        code = dictionary.get("code") if dictionary.get("code") else None
        dfs_ok = dictionary.get("dfs_ok") if "dfs_ok" in dictionary.keys() else None
        key = dictionary.get("key") if dictionary.get("key") else None
        name = dictionary.get("name") if dictionary.get("name") else None
        uses = dictionary.get("uses") if dictionary.get("uses") else None
        # Return an object of this model
        return cls(band_24_40_mhz_allowed,
                   band_24_channels,
                   band_24_enabled,
                   band_5_channels,
                   band_5_enabled,
                   certified,
                   code,
                   dfs_ok,
                   key,
                   name,
                   uses)
