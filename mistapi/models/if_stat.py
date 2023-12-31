# -*- coding: utf-8 -*-

"""
mistapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from mistapi.api_helper import APIHelper


class IfStat(object):

    """Implementation of the 'IfStat' model.

    TODO: type model description here.

    Attributes:
        ips (list of string): TODO: type description here.
        port_id (string): TODO: type description here.
        rx_bytes (int): TODO: type description here.
        rx_pkts (int): TODO: type description here.
        tx_bytes (int): TODO: type description here.
        tx_pkts (int): TODO: type description here.
        up (bool): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "ips": 'ips',
        "port_id": 'port_id',
        "rx_bytes": 'rx_bytes',
        "rx_pkts": 'rx_pkts',
        "tx_bytes": 'tx_bytes',
        "tx_pkts": 'tx_pkts',
        "up": 'up'
    }

    _optionals = [
        'ips',
        'port_id',
        'rx_bytes',
        'rx_pkts',
        'tx_bytes',
        'tx_pkts',
        'up',
    ]

    def __init__(self,
                 ips=APIHelper.SKIP,
                 port_id=APIHelper.SKIP,
                 rx_bytes=APIHelper.SKIP,
                 rx_pkts=APIHelper.SKIP,
                 tx_bytes=APIHelper.SKIP,
                 tx_pkts=APIHelper.SKIP,
                 up=APIHelper.SKIP):
        """Constructor for the IfStat class"""

        # Initialize members of the class
        if ips is not APIHelper.SKIP:
            self.ips = ips 
        if port_id is not APIHelper.SKIP:
            self.port_id = port_id 
        if rx_bytes is not APIHelper.SKIP:
            self.rx_bytes = rx_bytes 
        if rx_pkts is not APIHelper.SKIP:
            self.rx_pkts = rx_pkts 
        if tx_bytes is not APIHelper.SKIP:
            self.tx_bytes = tx_bytes 
        if tx_pkts is not APIHelper.SKIP:
            self.tx_pkts = tx_pkts 
        if up is not APIHelper.SKIP:
            self.up = up 

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

        ips = dictionary.get("ips") if dictionary.get("ips") else APIHelper.SKIP
        port_id = dictionary.get("port_id") if dictionary.get("port_id") else APIHelper.SKIP
        rx_bytes = dictionary.get("rx_bytes") if dictionary.get("rx_bytes") else APIHelper.SKIP
        rx_pkts = dictionary.get("rx_pkts") if dictionary.get("rx_pkts") else APIHelper.SKIP
        tx_bytes = dictionary.get("tx_bytes") if dictionary.get("tx_bytes") else APIHelper.SKIP
        tx_pkts = dictionary.get("tx_pkts") if dictionary.get("tx_pkts") else APIHelper.SKIP
        up = dictionary.get("up") if "up" in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(ips,
                   port_id,
                   rx_bytes,
                   rx_pkts,
                   tx_bytes,
                   tx_pkts,
                   up)
