# -*- coding: utf-8 -*-

"""
mistapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from mistapi.api_helper import APIHelper


class Band62(object):

    """Implementation of the 'Band62' model.

    radio stat of 6G radio

    Attributes:
        bandwidth (Bandwidth4Enum): current channel bandwidth
        channel (int): current channel the radio is running on
        dynamic_chaining_enalbed (bool): Use dynamic chaining for downlink
        mac (string): radio (base) mac, it can have 16 bssids (e.g.
            5c5b350001a0-5c5b350001af)
        num_clients (float): TODO: type description here.
        power (int): transmit power (in dBm)
        rx_bytes (float): TODO: type description here.
        rx_pkts (float): TODO: type description here.
        tx_bytes (float): TODO: type description here.
        tx_pkts (float): TODO: type description here.
        util_all (int): all utilization in percentage
        util_non_wifi (int): reception of “No Packets” utilization in
            percentage, received frames with invalid PLCPs and CRS glitches as
            noise
        util_rx_in_bss (int): reception of “In BSS” utilization in percentage,
            only frames that are received from AP/STAs within the BSS
        util_rx_other_bss (int): reception of “Other BSS” utilization in
            percentage, all frames received from AP/STAs that are outside the
            BSS
        util_tx (int): transmission utilization in percentage
        util_unknown_wifi (int): reception of “No Category” utilization in
            percentage, all 802.11 frames that are corrupted at the receiver

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "bandwidth": 'bandwidth',
        "channel": 'channel',
        "dynamic_chaining_enalbed": 'dynamic_chaining_enalbed',
        "mac": 'mac',
        "num_clients": 'num_clients',
        "power": 'power',
        "rx_bytes": 'rx_bytes',
        "rx_pkts": 'rx_pkts',
        "tx_bytes": 'tx_bytes',
        "tx_pkts": 'tx_pkts',
        "util_all": 'util_all',
        "util_non_wifi": 'util_non_wifi',
        "util_rx_in_bss": 'util_rx_in_bss',
        "util_rx_other_bss": 'util_rx_other_bss',
        "util_tx": 'util_tx',
        "util_unknown_wifi": 'util_unknown_wifi'
    }

    _optionals = [
        'bandwidth',
        'channel',
        'dynamic_chaining_enalbed',
        'mac',
        'num_clients',
        'power',
        'rx_bytes',
        'rx_pkts',
        'tx_bytes',
        'tx_pkts',
        'util_all',
        'util_non_wifi',
        'util_rx_in_bss',
        'util_rx_other_bss',
        'util_tx',
        'util_unknown_wifi',
    ]

    def __init__(self,
                 bandwidth=APIHelper.SKIP,
                 channel=APIHelper.SKIP,
                 dynamic_chaining_enalbed=APIHelper.SKIP,
                 mac=APIHelper.SKIP,
                 num_clients=APIHelper.SKIP,
                 power=APIHelper.SKIP,
                 rx_bytes=APIHelper.SKIP,
                 rx_pkts=APIHelper.SKIP,
                 tx_bytes=APIHelper.SKIP,
                 tx_pkts=APIHelper.SKIP,
                 util_all=APIHelper.SKIP,
                 util_non_wifi=APIHelper.SKIP,
                 util_rx_in_bss=APIHelper.SKIP,
                 util_rx_other_bss=APIHelper.SKIP,
                 util_tx=APIHelper.SKIP,
                 util_unknown_wifi=APIHelper.SKIP):
        """Constructor for the Band62 class"""

        # Initialize members of the class
        if bandwidth is not APIHelper.SKIP:
            self.bandwidth = bandwidth 
        if channel is not APIHelper.SKIP:
            self.channel = channel 
        if dynamic_chaining_enalbed is not APIHelper.SKIP:
            self.dynamic_chaining_enalbed = dynamic_chaining_enalbed 
        if mac is not APIHelper.SKIP:
            self.mac = mac 
        if num_clients is not APIHelper.SKIP:
            self.num_clients = num_clients 
        if power is not APIHelper.SKIP:
            self.power = power 
        if rx_bytes is not APIHelper.SKIP:
            self.rx_bytes = rx_bytes 
        if rx_pkts is not APIHelper.SKIP:
            self.rx_pkts = rx_pkts 
        if tx_bytes is not APIHelper.SKIP:
            self.tx_bytes = tx_bytes 
        if tx_pkts is not APIHelper.SKIP:
            self.tx_pkts = tx_pkts 
        if util_all is not APIHelper.SKIP:
            self.util_all = util_all 
        if util_non_wifi is not APIHelper.SKIP:
            self.util_non_wifi = util_non_wifi 
        if util_rx_in_bss is not APIHelper.SKIP:
            self.util_rx_in_bss = util_rx_in_bss 
        if util_rx_other_bss is not APIHelper.SKIP:
            self.util_rx_other_bss = util_rx_other_bss 
        if util_tx is not APIHelper.SKIP:
            self.util_tx = util_tx 
        if util_unknown_wifi is not APIHelper.SKIP:
            self.util_unknown_wifi = util_unknown_wifi 

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

        bandwidth = dictionary.get("bandwidth") if dictionary.get("bandwidth") else APIHelper.SKIP
        channel = dictionary.get("channel") if dictionary.get("channel") else APIHelper.SKIP
        dynamic_chaining_enalbed = dictionary.get("dynamic_chaining_enalbed") if "dynamic_chaining_enalbed" in dictionary.keys() else APIHelper.SKIP
        mac = dictionary.get("mac") if dictionary.get("mac") else APIHelper.SKIP
        num_clients = dictionary.get("num_clients") if dictionary.get("num_clients") else APIHelper.SKIP
        power = dictionary.get("power") if dictionary.get("power") else APIHelper.SKIP
        rx_bytes = dictionary.get("rx_bytes") if dictionary.get("rx_bytes") else APIHelper.SKIP
        rx_pkts = dictionary.get("rx_pkts") if dictionary.get("rx_pkts") else APIHelper.SKIP
        tx_bytes = dictionary.get("tx_bytes") if dictionary.get("tx_bytes") else APIHelper.SKIP
        tx_pkts = dictionary.get("tx_pkts") if dictionary.get("tx_pkts") else APIHelper.SKIP
        util_all = dictionary.get("util_all") if dictionary.get("util_all") else APIHelper.SKIP
        util_non_wifi = dictionary.get("util_non_wifi") if dictionary.get("util_non_wifi") else APIHelper.SKIP
        util_rx_in_bss = dictionary.get("util_rx_in_bss") if dictionary.get("util_rx_in_bss") else APIHelper.SKIP
        util_rx_other_bss = dictionary.get("util_rx_other_bss") if dictionary.get("util_rx_other_bss") else APIHelper.SKIP
        util_tx = dictionary.get("util_tx") if dictionary.get("util_tx") else APIHelper.SKIP
        util_unknown_wifi = dictionary.get("util_unknown_wifi") if dictionary.get("util_unknown_wifi") else APIHelper.SKIP
        # Return an object of this model
        return cls(bandwidth,
                   channel,
                   dynamic_chaining_enalbed,
                   mac,
                   num_clients,
                   power,
                   rx_bytes,
                   rx_pkts,
                   tx_bytes,
                   tx_pkts,
                   util_all,
                   util_non_wifi,
                   util_rx_in_bss,
                   util_rx_other_bss,
                   util_tx,
                   util_unknown_wifi)
