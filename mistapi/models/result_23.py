# -*- coding: utf-8 -*-

"""
mistapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class Result23(object):

    """Implementation of the 'Result23' model.

    TODO: type model description here.

    Attributes:
        ap_id (uuid|string): TODO: type description here.
        band (Band8Enum): TODO: type description here.
        bandwidth (Bandwidth5Enum): channel width for the band
        channel (int): channel for the band from rrm
        event (Event13Enum): schedule-site-rrm / triggered-site-rrm /
            interference-ap-co-channel / rrm-radar
        power (int): tx power of the radio
        pre_bandwidth (PreBandwidthEnum): (previously) channel width for the
            band , 0 means no previously available
        pre_channel (int): (previously) channel for the band, 0 means no
            previously available
        pre_power (float): (previously) tx power of the radio, 0 means no
            previously available
        pre_usage (string): TODO: type description here.
        timestamp (float): timestamp of the event
        usage (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "ap_id": 'ap_id',
        "band": 'band',
        "bandwidth": 'bandwidth',
        "channel": 'channel',
        "event": 'event',
        "power": 'power',
        "pre_bandwidth": 'pre_bandwidth',
        "pre_channel": 'pre_channel',
        "pre_power": 'pre_power',
        "pre_usage": 'pre_usage',
        "timestamp": 'timestamp',
        "usage": 'usage'
    }

    def __init__(self,
                 ap_id=None,
                 band=None,
                 bandwidth=None,
                 channel=None,
                 event=None,
                 power=None,
                 pre_bandwidth=None,
                 pre_channel=None,
                 pre_power=None,
                 pre_usage=None,
                 timestamp=None,
                 usage=None):
        """Constructor for the Result23 class"""

        # Initialize members of the class
        self.ap_id = ap_id 
        self.band = band 
        self.bandwidth = bandwidth 
        self.channel = channel 
        self.event = event 
        self.power = power 
        self.pre_bandwidth = pre_bandwidth 
        self.pre_channel = pre_channel 
        self.pre_power = pre_power 
        self.pre_usage = pre_usage 
        self.timestamp = timestamp 
        self.usage = usage 

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
        bandwidth = dictionary.get("bandwidth") if dictionary.get("bandwidth") else None
        channel = dictionary.get("channel") if dictionary.get("channel") else None
        event = dictionary.get("event") if dictionary.get("event") else None
        power = dictionary.get("power") if dictionary.get("power") else None
        pre_bandwidth = dictionary.get("pre_bandwidth") if dictionary.get("pre_bandwidth") else None
        pre_channel = dictionary.get("pre_channel") if dictionary.get("pre_channel") else None
        pre_power = dictionary.get("pre_power") if dictionary.get("pre_power") else None
        pre_usage = dictionary.get("pre_usage") if dictionary.get("pre_usage") else None
        timestamp = dictionary.get("timestamp") if dictionary.get("timestamp") else None
        usage = dictionary.get("usage") if dictionary.get("usage") else None
        # Return an object of this model
        return cls(ap_id,
                   band,
                   bandwidth,
                   channel,
                   event,
                   power,
                   pre_bandwidth,
                   pre_channel,
                   pre_power,
                   pre_usage,
                   timestamp,
                   usage)
