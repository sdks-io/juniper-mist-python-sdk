# -*- coding: utf-8 -*-

"""
mistapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class User2(object):

    """Implementation of the 'User2' model.

    TODO: type model description here.

    Attributes:
        ap_mac (string): TODO: type description here.
        ap_name (string): TODO: type description here.
        degraded (float): TODO: type description here.
        device_os (string): TODO: type description here.
        device_type (string): TODO: type description here.
        duration (float): TODO: type description here.
        mac (string): TODO: type description here.
        name (string): TODO: type description here.
        ssid (string): TODO: type description here.
        total (float): TODO: type description here.
        wlan_id (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "ap_mac": 'ap_mac',
        "ap_name": 'ap_name',
        "degraded": 'degraded',
        "device_os": 'device_os',
        "device_type": 'device_type',
        "duration": 'duration',
        "mac": 'mac',
        "name": 'name',
        "ssid": 'ssid',
        "total": 'total',
        "wlan_id": 'wlan_id'
    }

    def __init__(self,
                 ap_mac=None,
                 ap_name=None,
                 degraded=None,
                 device_os=None,
                 device_type=None,
                 duration=None,
                 mac=None,
                 name=None,
                 ssid=None,
                 total=None,
                 wlan_id=None):
        """Constructor for the User2 class"""

        # Initialize members of the class
        self.ap_mac = ap_mac 
        self.ap_name = ap_name 
        self.degraded = degraded 
        self.device_os = device_os 
        self.device_type = device_type 
        self.duration = duration 
        self.mac = mac 
        self.name = name 
        self.ssid = ssid 
        self.total = total 
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

        ap_mac = dictionary.get("ap_mac") if dictionary.get("ap_mac") else None
        ap_name = dictionary.get("ap_name") if dictionary.get("ap_name") else None
        degraded = dictionary.get("degraded") if dictionary.get("degraded") else None
        device_os = dictionary.get("device_os") if dictionary.get("device_os") else None
        device_type = dictionary.get("device_type") if dictionary.get("device_type") else None
        duration = dictionary.get("duration") if dictionary.get("duration") else None
        mac = dictionary.get("mac") if dictionary.get("mac") else None
        name = dictionary.get("name") if dictionary.get("name") else None
        ssid = dictionary.get("ssid") if dictionary.get("ssid") else None
        total = dictionary.get("total") if dictionary.get("total") else None
        wlan_id = dictionary.get("wlan_id") if dictionary.get("wlan_id") else None
        # Return an object of this model
        return cls(ap_mac,
                   ap_name,
                   degraded,
                   device_os,
                   device_type,
                   duration,
                   mac,
                   name,
                   ssid,
                   total,
                   wlan_id)
