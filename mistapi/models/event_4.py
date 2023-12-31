# -*- coding: utf-8 -*-

"""
mistapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class Event4(object):

    """Implementation of the 'Event4' model.

    TODO: type model description here.

    Attributes:
        ap (string): mac address of the AP the client roamed or disconnected
            from
        ap_name (string): user-friendly name of the AP the client roamed or
            disconnected from.
        band (string): 5GHz or 2.4GHz band
        bssid (string): TODO: type description here.
        client_family (string): device family E.g. “Mac”, “iPhone”, “Apple
            watch”
        client_manufacture (string): device manufacturer E.g. “Apple”
        client_model (string): device model E.g. “8+”, “XS”
        client_os (string): device operating system E.g. “Mojave”, “Windows
            10”, “Linux”
        connect (int): time when the user connects
        connect_float (float): floating point connect timestamp with
            millisecond precision
        disconnect (int): time when the user disconnects
        disconnect_float (float): floating point disconnect timestamp with
            millisecond precision
        duration (int): the duration of the roamed or complete session
            indicated by termination_reason field.
        mac (string): the client’s mac
        next_ap (string): the AP the client has roamed to.
        org_id (uuid|string): TODO: type description here.
        rssi (float): latest average RSSI before the user disconnects
        site_id (uuid|string): TODO: type description here.
        site_name (string): TODO: type description here.
        ssid (string): TODO: type description here.
        termination_reason (int): 1 disassociate - when the client
            disassociates. 2 inactive - when the client is timeout. 3 roamed -
            when the client is roamed between APs
        timestamp (float): TODO: type description here.
        version (float): schema version of this message
        wlan_id (uuid|string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "ap": 'ap',
        "ap_name": 'ap_name',
        "band": 'band',
        "bssid": 'bssid',
        "client_family": 'client_family',
        "client_manufacture": 'client_manufacture',
        "client_model": 'client_model',
        "client_os": 'client_os',
        "connect": 'connect',
        "connect_float": 'connect_float',
        "disconnect": 'disconnect',
        "disconnect_float": 'disconnect_float',
        "duration": 'duration',
        "mac": 'mac',
        "next_ap": 'next_ap',
        "org_id": 'org_id',
        "rssi": 'rssi',
        "site_id": 'site_id',
        "site_name": 'site_name',
        "ssid": 'ssid',
        "termination_reason": 'termination_reason',
        "timestamp": 'timestamp',
        "version": 'version',
        "wlan_id": 'wlan_id'
    }

    def __init__(self,
                 ap=None,
                 ap_name=None,
                 band=None,
                 bssid=None,
                 client_family=None,
                 client_manufacture=None,
                 client_model=None,
                 client_os=None,
                 connect=None,
                 connect_float=None,
                 disconnect=None,
                 disconnect_float=None,
                 duration=None,
                 mac=None,
                 next_ap=None,
                 org_id=None,
                 rssi=None,
                 site_id=None,
                 site_name=None,
                 ssid=None,
                 termination_reason=None,
                 timestamp=None,
                 version=None,
                 wlan_id=None):
        """Constructor for the Event4 class"""

        # Initialize members of the class
        self.ap = ap 
        self.ap_name = ap_name 
        self.band = band 
        self.bssid = bssid 
        self.client_family = client_family 
        self.client_manufacture = client_manufacture 
        self.client_model = client_model 
        self.client_os = client_os 
        self.connect = connect 
        self.connect_float = connect_float 
        self.disconnect = disconnect 
        self.disconnect_float = disconnect_float 
        self.duration = duration 
        self.mac = mac 
        self.next_ap = next_ap 
        self.org_id = org_id 
        self.rssi = rssi 
        self.site_id = site_id 
        self.site_name = site_name 
        self.ssid = ssid 
        self.termination_reason = termination_reason 
        self.timestamp = timestamp 
        self.version = version 
        self.wlan_id = wlan_id 

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

        ap = dictionary.get("ap") if dictionary.get("ap") else None
        ap_name = dictionary.get("ap_name") if dictionary.get("ap_name") else None
        band = dictionary.get("band") if dictionary.get("band") else None
        bssid = dictionary.get("bssid") if dictionary.get("bssid") else None
        client_family = dictionary.get("client_family") if dictionary.get("client_family") else None
        client_manufacture = dictionary.get("client_manufacture") if dictionary.get("client_manufacture") else None
        client_model = dictionary.get("client_model") if dictionary.get("client_model") else None
        client_os = dictionary.get("client_os") if dictionary.get("client_os") else None
        connect = dictionary.get("connect") if dictionary.get("connect") else None
        connect_float = dictionary.get("connect_float") if dictionary.get("connect_float") else None
        disconnect = dictionary.get("disconnect") if dictionary.get("disconnect") else None
        disconnect_float = dictionary.get("disconnect_float") if dictionary.get("disconnect_float") else None
        duration = dictionary.get("duration") if dictionary.get("duration") else None
        mac = dictionary.get("mac") if dictionary.get("mac") else None
        next_ap = dictionary.get("next_ap") if dictionary.get("next_ap") else None
        org_id = dictionary.get("org_id") if dictionary.get("org_id") else None
        rssi = dictionary.get("rssi") if dictionary.get("rssi") else None
        site_id = dictionary.get("site_id") if dictionary.get("site_id") else None
        site_name = dictionary.get("site_name") if dictionary.get("site_name") else None
        ssid = dictionary.get("ssid") if dictionary.get("ssid") else None
        termination_reason = dictionary.get("termination_reason") if dictionary.get("termination_reason") else None
        timestamp = dictionary.get("timestamp") if dictionary.get("timestamp") else None
        version = dictionary.get("version") if dictionary.get("version") else None
        wlan_id = dictionary.get("wlan_id") if dictionary.get("wlan_id") else None
        # Return an object of this model
        return cls(ap,
                   ap_name,
                   band,
                   bssid,
                   client_family,
                   client_manufacture,
                   client_model,
                   client_os,
                   connect,
                   connect_float,
                   disconnect,
                   disconnect_float,
                   duration,
                   mac,
                   next_ap,
                   org_id,
                   rssi,
                   site_id,
                   site_name,
                   ssid,
                   termination_reason,
                   timestamp,
                   version,
                   wlan_id)
