# -*- coding: utf-8 -*-

"""
mistapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from mistapi.api_helper import APIHelper


class MeshDownlinks(object):

    """Implementation of the 'MeshDownlinks' model.

    the property key is the mesh downlink id

    Attributes:
        band (string): TODO: type description here.
        channel (int): TODO: type description here.
        idle_time (int): TODO: type description here.
        last_seen (int): TODO: type description here.
        proto (string): TODO: type description here.
        rssi (int): TODO: type description here.
        rx_bps (int): TODO: type description here.
        rx_bytes (int): TODO: type description here.
        rx_packets (int): TODO: type description here.
        rx_rate (int): TODO: type description here.
        rx_retries (int): TODO: type description here.
        site_id (uuid|string): TODO: type description here.
        snr (int): TODO: type description here.
        tx_bps (int): TODO: type description here.
        tx_bytes (int): TODO: type description here.
        tx_packets (int): TODO: type description here.
        tx_rate (int): TODO: type description here.
        tx_retries (int): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "band": 'band',
        "channel": 'channel',
        "idle_time": 'idle_time',
        "last_seen": 'last_seen',
        "proto": 'proto',
        "rssi": 'rssi',
        "rx_bps": 'rx_bps',
        "rx_bytes": 'rx_bytes',
        "rx_packets": 'rx_packets',
        "rx_rate": 'rx_rate',
        "rx_retries": 'rx_retries',
        "site_id": 'site_id',
        "snr": 'snr',
        "tx_bps": 'tx_bps',
        "tx_bytes": 'tx_bytes',
        "tx_packets": 'tx_packets',
        "tx_rate": 'tx_rate',
        "tx_retries": 'tx_retries'
    }

    _optionals = [
        'band',
        'channel',
        'idle_time',
        'last_seen',
        'proto',
        'rssi',
        'rx_bps',
        'rx_bytes',
        'rx_packets',
        'rx_rate',
        'rx_retries',
        'site_id',
        'snr',
        'tx_bps',
        'tx_bytes',
        'tx_packets',
        'tx_rate',
        'tx_retries',
    ]

    def __init__(self,
                 band=APIHelper.SKIP,
                 channel=APIHelper.SKIP,
                 idle_time=APIHelper.SKIP,
                 last_seen=APIHelper.SKIP,
                 proto=APIHelper.SKIP,
                 rssi=APIHelper.SKIP,
                 rx_bps=APIHelper.SKIP,
                 rx_bytes=APIHelper.SKIP,
                 rx_packets=APIHelper.SKIP,
                 rx_rate=APIHelper.SKIP,
                 rx_retries=APIHelper.SKIP,
                 site_id=APIHelper.SKIP,
                 snr=APIHelper.SKIP,
                 tx_bps=APIHelper.SKIP,
                 tx_bytes=APIHelper.SKIP,
                 tx_packets=APIHelper.SKIP,
                 tx_rate=APIHelper.SKIP,
                 tx_retries=APIHelper.SKIP):
        """Constructor for the MeshDownlinks class"""

        # Initialize members of the class
        if band is not APIHelper.SKIP:
            self.band = band 
        if channel is not APIHelper.SKIP:
            self.channel = channel 
        if idle_time is not APIHelper.SKIP:
            self.idle_time = idle_time 
        if last_seen is not APIHelper.SKIP:
            self.last_seen = last_seen 
        if proto is not APIHelper.SKIP:
            self.proto = proto 
        if rssi is not APIHelper.SKIP:
            self.rssi = rssi 
        if rx_bps is not APIHelper.SKIP:
            self.rx_bps = rx_bps 
        if rx_bytes is not APIHelper.SKIP:
            self.rx_bytes = rx_bytes 
        if rx_packets is not APIHelper.SKIP:
            self.rx_packets = rx_packets 
        if rx_rate is not APIHelper.SKIP:
            self.rx_rate = rx_rate 
        if rx_retries is not APIHelper.SKIP:
            self.rx_retries = rx_retries 
        if site_id is not APIHelper.SKIP:
            self.site_id = site_id 
        if snr is not APIHelper.SKIP:
            self.snr = snr 
        if tx_bps is not APIHelper.SKIP:
            self.tx_bps = tx_bps 
        if tx_bytes is not APIHelper.SKIP:
            self.tx_bytes = tx_bytes 
        if tx_packets is not APIHelper.SKIP:
            self.tx_packets = tx_packets 
        if tx_rate is not APIHelper.SKIP:
            self.tx_rate = tx_rate 
        if tx_retries is not APIHelper.SKIP:
            self.tx_retries = tx_retries 

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

        band = dictionary.get("band") if dictionary.get("band") else APIHelper.SKIP
        channel = dictionary.get("channel") if dictionary.get("channel") else APIHelper.SKIP
        idle_time = dictionary.get("idle_time") if dictionary.get("idle_time") else APIHelper.SKIP
        last_seen = dictionary.get("last_seen") if dictionary.get("last_seen") else APIHelper.SKIP
        proto = dictionary.get("proto") if dictionary.get("proto") else APIHelper.SKIP
        rssi = dictionary.get("rssi") if dictionary.get("rssi") else APIHelper.SKIP
        rx_bps = dictionary.get("rx_bps") if dictionary.get("rx_bps") else APIHelper.SKIP
        rx_bytes = dictionary.get("rx_bytes") if dictionary.get("rx_bytes") else APIHelper.SKIP
        rx_packets = dictionary.get("rx_packets") if dictionary.get("rx_packets") else APIHelper.SKIP
        rx_rate = dictionary.get("rx_rate") if dictionary.get("rx_rate") else APIHelper.SKIP
        rx_retries = dictionary.get("rx_retries") if dictionary.get("rx_retries") else APIHelper.SKIP
        site_id = dictionary.get("site_id") if dictionary.get("site_id") else APIHelper.SKIP
        snr = dictionary.get("snr") if dictionary.get("snr") else APIHelper.SKIP
        tx_bps = dictionary.get("tx_bps") if dictionary.get("tx_bps") else APIHelper.SKIP
        tx_bytes = dictionary.get("tx_bytes") if dictionary.get("tx_bytes") else APIHelper.SKIP
        tx_packets = dictionary.get("tx_packets") if dictionary.get("tx_packets") else APIHelper.SKIP
        tx_rate = dictionary.get("tx_rate") if dictionary.get("tx_rate") else APIHelper.SKIP
        tx_retries = dictionary.get("tx_retries") if dictionary.get("tx_retries") else APIHelper.SKIP
        # Return an object of this model
        return cls(band,
                   channel,
                   idle_time,
                   last_seen,
                   proto,
                   rssi,
                   rx_bps,
                   rx_bytes,
                   rx_packets,
                   rx_rate,
                   rx_retries,
                   site_id,
                   snr,
                   tx_bps,
                   tx_bytes,
                   tx_packets,
                   tx_rate,
                   tx_retries)
