# -*- coding: utf-8 -*-

"""
mistapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from mistapi.api_helper import APIHelper
from mistapi.models.scan_datum import ScanDatum


class Event11(object):

    """Implementation of the 'Event11' model.

    TODO: type model description here.

    Attributes:
        connection_ap (string): mac address of the AP the client is connected
            to
        connection_band (string): 5GHz or 2.4GHz band, of the BSSID the client
            is connected to
        connection_bssid (string): BSSID of the AP the client is connected to
        connection_channel (int): channel of the band the client is connected
            to
        connection_rssi (float): RSSI of the client’s connection to the
            AP/BSSID
        last_seen (float): time client last seen with scan data
        mac (string): the client’s mac
        scan_data (list of ScanDatum): TODO: type description here.
        site_id (string): Site ID

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "connection_ap": 'connection_ap',
        "connection_band": 'connection_band',
        "connection_bssid": 'connection_bssid',
        "connection_channel": 'connection_channel',
        "connection_rssi": 'connection_rssi',
        "last_seen": 'last_seen',
        "mac": 'mac',
        "site_id": 'site_id',
        "scan_data": 'scan_data'
    }

    _optionals = [
        'scan_data',
    ]

    def __init__(self,
                 connection_ap=None,
                 connection_band=None,
                 connection_bssid=None,
                 connection_channel=None,
                 connection_rssi=None,
                 last_seen=None,
                 mac=None,
                 site_id=None,
                 scan_data=APIHelper.SKIP):
        """Constructor for the Event11 class"""

        # Initialize members of the class
        self.connection_ap = connection_ap 
        self.connection_band = connection_band 
        self.connection_bssid = connection_bssid 
        self.connection_channel = connection_channel 
        self.connection_rssi = connection_rssi 
        self.last_seen = last_seen 
        self.mac = mac 
        if scan_data is not APIHelper.SKIP:
            self.scan_data = scan_data 
        self.site_id = site_id 

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

        connection_ap = dictionary.get("connection_ap") if dictionary.get("connection_ap") else None
        connection_band = dictionary.get("connection_band") if dictionary.get("connection_band") else None
        connection_bssid = dictionary.get("connection_bssid") if dictionary.get("connection_bssid") else None
        connection_channel = dictionary.get("connection_channel") if dictionary.get("connection_channel") else None
        connection_rssi = dictionary.get("connection_rssi") if dictionary.get("connection_rssi") else None
        last_seen = dictionary.get("last_seen") if dictionary.get("last_seen") else None
        mac = dictionary.get("mac") if dictionary.get("mac") else None
        site_id = dictionary.get("site_id") if dictionary.get("site_id") else None
        scan_data = None
        if dictionary.get('scan_data') is not None:
            scan_data = [ScanDatum.from_dictionary(x) for x in dictionary.get('scan_data')]
        else:
            scan_data = APIHelper.SKIP
        # Return an object of this model
        return cls(connection_ap,
                   connection_band,
                   connection_bssid,
                   connection_channel,
                   connection_rssi,
                   last_seen,
                   mac,
                   site_id,
                   scan_data)
