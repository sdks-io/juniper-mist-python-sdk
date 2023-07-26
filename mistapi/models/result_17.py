# -*- coding: utf-8 -*-

"""
mistapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from mistapi.api_helper import APIHelper


class Result17(object):

    """Implementation of the 'Result17' model.

    TODO: type model description here.

    Attributes:
        ap_id (uuid|string): TODO: type description here.
        band (int): TODO: type description here.
        channel_util (float): TODO: type description here.
        channels (list of int): TODO: type description here.
        rssi (float): TODO: type description here.
        source (string): TODO: type description here.
        timestamp (float): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "ap_id": 'ap_id',
        "band": 'band',
        "channel_util": 'channel_util',
        "rssi": 'rssi',
        "source": 'source',
        "timestamp": 'timestamp',
        "channels": 'channels'
    }

    _optionals = [
        'channels',
    ]

    def __init__(self,
                 ap_id=None,
                 band=None,
                 channel_util=None,
                 rssi=None,
                 source=None,
                 timestamp=None,
                 channels=APIHelper.SKIP):
        """Constructor for the Result17 class"""

        # Initialize members of the class
        self.ap_id = ap_id 
        self.band = band 
        self.channel_util = channel_util 
        if channels is not APIHelper.SKIP:
            self.channels = channels 
        self.rssi = rssi 
        self.source = source 
        self.timestamp = timestamp 

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

        ap_id = dictionary.get("ap_id") if dictionary.get("ap_id") else None
        band = dictionary.get("band") if dictionary.get("band") else None
        channel_util = dictionary.get("channel_util") if dictionary.get("channel_util") else None
        rssi = dictionary.get("rssi") if dictionary.get("rssi") else None
        source = dictionary.get("source") if dictionary.get("source") else None
        timestamp = dictionary.get("timestamp") if dictionary.get("timestamp") else None
        channels = dictionary.get("channels") if dictionary.get("channels") else APIHelper.SKIP
        # Return an object of this model
        return cls(ap_id,
                   band,
                   channel_util,
                   rssi,
                   source,
                   timestamp,
                   channels)