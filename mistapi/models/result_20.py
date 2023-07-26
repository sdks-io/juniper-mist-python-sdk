# -*- coding: utf-8 -*-

"""
mistapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class Result20(object):

    """Implementation of the 'Result20' model.

    TODO: type model description here.

    Attributes:
        annotation (string): TODO: type description here.
        ap_mac (string): TODO: type description here.
        avg_rssi (float): TODO: type description here.
        band (string): TODO: type description here.
        bssid (string): TODO: type description here.
        client_mac (string): TODO: type description here.
        num_aps (int): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "annotation": 'annotation',
        "ap_mac": 'ap_mac',
        "avg_rssi": 'avg_rssi',
        "band": 'band',
        "bssid": 'bssid',
        "client_mac": 'client_mac',
        "num_aps": 'num_aps'
    }

    def __init__(self,
                 annotation=None,
                 ap_mac=None,
                 avg_rssi=None,
                 band=None,
                 bssid=None,
                 client_mac=None,
                 num_aps=None):
        """Constructor for the Result20 class"""

        # Initialize members of the class
        self.annotation = annotation 
        self.ap_mac = ap_mac 
        self.avg_rssi = avg_rssi 
        self.band = band 
        self.bssid = bssid 
        self.client_mac = client_mac 
        self.num_aps = num_aps 

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

        annotation = dictionary.get("annotation") if dictionary.get("annotation") else None
        ap_mac = dictionary.get("ap_mac") if dictionary.get("ap_mac") else None
        avg_rssi = dictionary.get("avg_rssi") if dictionary.get("avg_rssi") else None
        band = dictionary.get("band") if dictionary.get("band") else None
        bssid = dictionary.get("bssid") if dictionary.get("bssid") else None
        client_mac = dictionary.get("client_mac") if dictionary.get("client_mac") else None
        num_aps = dictionary.get("num_aps") if dictionary.get("num_aps") else None
        # Return an object of this model
        return cls(annotation,
                   ap_mac,
                   avg_rssi,
                   band,
                   bssid,
                   client_mac,
                   num_aps)
