# -*- coding: utf-8 -*-

"""
mistapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from mistapi.api_helper import APIHelper
from mistapi.models.wifi_beacon_extended_info import WifiBeaconExtendedInfo


class Event8(object):

    """Implementation of the 'Event8' model.

    TODO: type model description here.

    Attributes:
        battery_voltage (int): TODO: type description here.
        eddystone_uid_instance (string): TODO: type description here.
        eddystone_uid_namespace (string): TODO: type description here.
        eddystone_url_url (string): TODO: type description here.
        ibeacon_major (int): TODO: type description here.
        ibeacon_minor (int): TODO: type description here.
        ibeacon_uuid (uuid|string): TODO: type description here.
        id (uuid|string): unique id of the client (a client would have
            different id for different org)
        mac (string): TODO: type description here.
        map_id (uuid|string): map id
        mfg_company_id (int): optional, BLE manufacturing company ID
        mfg_data (string): optional, BLE manufacturing data in hex byte-string
            format (ie "112233AABBCC")
        name (string): name of the client, may be empty
        site_id (uuid|string): TODO: type description here.
        timestamp (int): timestamp of the event, epoch
        mtype (string): TODO: type description here.
        wifi_beacon_extended_info (list of WifiBeaconExtendedInfo): optional,
            list of extended beacon info packets heard from the client, frame
            and sequence control included with the payload
        x (int): x, in meter
        y (int): y, in meter

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id": 'id',
        "map_id": 'map_id',
        "site_id": 'site_id',
        "timestamp": 'timestamp',
        "mtype": 'type',
        "x": 'x',
        "y": 'y',
        "battery_voltage": 'battery_voltage',
        "eddystone_uid_instance": 'eddystone_uid_instance',
        "eddystone_uid_namespace": 'eddystone_uid_namespace',
        "eddystone_url_url": 'eddystone_url_url',
        "ibeacon_major": 'ibeacon_major',
        "ibeacon_minor": 'ibeacon_minor',
        "ibeacon_uuid": 'ibeacon_uuid',
        "mac": 'mac',
        "mfg_company_id": 'mfg_company_id',
        "mfg_data": 'mfg_data',
        "name": 'name',
        "wifi_beacon_extended_info": 'wifi_beacon_extended_info'
    }

    _optionals = [
        'battery_voltage',
        'eddystone_uid_instance',
        'eddystone_uid_namespace',
        'eddystone_url_url',
        'ibeacon_major',
        'ibeacon_minor',
        'ibeacon_uuid',
        'mac',
        'mfg_company_id',
        'mfg_data',
        'name',
        'wifi_beacon_extended_info',
    ]

    def __init__(self,
                 id=None,
                 map_id=None,
                 site_id=None,
                 timestamp=None,
                 mtype=None,
                 x=None,
                 y=None,
                 battery_voltage=APIHelper.SKIP,
                 eddystone_uid_instance=APIHelper.SKIP,
                 eddystone_uid_namespace=APIHelper.SKIP,
                 eddystone_url_url=APIHelper.SKIP,
                 ibeacon_major=APIHelper.SKIP,
                 ibeacon_minor=APIHelper.SKIP,
                 ibeacon_uuid=APIHelper.SKIP,
                 mac=APIHelper.SKIP,
                 mfg_company_id=APIHelper.SKIP,
                 mfg_data=APIHelper.SKIP,
                 name=APIHelper.SKIP,
                 wifi_beacon_extended_info=APIHelper.SKIP):
        """Constructor for the Event8 class"""

        # Initialize members of the class
        if battery_voltage is not APIHelper.SKIP:
            self.battery_voltage = battery_voltage 
        if eddystone_uid_instance is not APIHelper.SKIP:
            self.eddystone_uid_instance = eddystone_uid_instance 
        if eddystone_uid_namespace is not APIHelper.SKIP:
            self.eddystone_uid_namespace = eddystone_uid_namespace 
        if eddystone_url_url is not APIHelper.SKIP:
            self.eddystone_url_url = eddystone_url_url 
        if ibeacon_major is not APIHelper.SKIP:
            self.ibeacon_major = ibeacon_major 
        if ibeacon_minor is not APIHelper.SKIP:
            self.ibeacon_minor = ibeacon_minor 
        if ibeacon_uuid is not APIHelper.SKIP:
            self.ibeacon_uuid = ibeacon_uuid 
        self.id = id 
        if mac is not APIHelper.SKIP:
            self.mac = mac 
        self.map_id = map_id 
        if mfg_company_id is not APIHelper.SKIP:
            self.mfg_company_id = mfg_company_id 
        if mfg_data is not APIHelper.SKIP:
            self.mfg_data = mfg_data 
        if name is not APIHelper.SKIP:
            self.name = name 
        self.site_id = site_id 
        self.timestamp = timestamp 
        self.mtype = mtype 
        if wifi_beacon_extended_info is not APIHelper.SKIP:
            self.wifi_beacon_extended_info = wifi_beacon_extended_info 
        self.x = x 
        self.y = y 

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

        id = dictionary.get("id") if dictionary.get("id") else None
        map_id = dictionary.get("map_id") if dictionary.get("map_id") else None
        site_id = dictionary.get("site_id") if dictionary.get("site_id") else None
        timestamp = dictionary.get("timestamp") if dictionary.get("timestamp") else None
        mtype = dictionary.get("type") if dictionary.get("type") else None
        x = dictionary.get("x") if dictionary.get("x") else None
        y = dictionary.get("y") if dictionary.get("y") else None
        battery_voltage = dictionary.get("battery_voltage") if dictionary.get("battery_voltage") else APIHelper.SKIP
        eddystone_uid_instance = dictionary.get("eddystone_uid_instance") if dictionary.get("eddystone_uid_instance") else APIHelper.SKIP
        eddystone_uid_namespace = dictionary.get("eddystone_uid_namespace") if dictionary.get("eddystone_uid_namespace") else APIHelper.SKIP
        eddystone_url_url = dictionary.get("eddystone_url_url") if dictionary.get("eddystone_url_url") else APIHelper.SKIP
        ibeacon_major = dictionary.get("ibeacon_major") if dictionary.get("ibeacon_major") else APIHelper.SKIP
        ibeacon_minor = dictionary.get("ibeacon_minor") if dictionary.get("ibeacon_minor") else APIHelper.SKIP
        ibeacon_uuid = dictionary.get("ibeacon_uuid") if dictionary.get("ibeacon_uuid") else APIHelper.SKIP
        mac = dictionary.get("mac") if dictionary.get("mac") else APIHelper.SKIP
        mfg_company_id = dictionary.get("mfg_company_id") if dictionary.get("mfg_company_id") else APIHelper.SKIP
        mfg_data = dictionary.get("mfg_data") if dictionary.get("mfg_data") else APIHelper.SKIP
        name = dictionary.get("name") if dictionary.get("name") else APIHelper.SKIP
        wifi_beacon_extended_info = None
        if dictionary.get('wifi_beacon_extended_info') is not None:
            wifi_beacon_extended_info = [WifiBeaconExtendedInfo.from_dictionary(x) for x in dictionary.get('wifi_beacon_extended_info')]
        else:
            wifi_beacon_extended_info = APIHelper.SKIP
        # Return an object of this model
        return cls(id,
                   map_id,
                   site_id,
                   timestamp,
                   mtype,
                   x,
                   y,
                   battery_voltage,
                   eddystone_uid_instance,
                   eddystone_uid_namespace,
                   eddystone_url_url,
                   ibeacon_major,
                   ibeacon_minor,
                   ibeacon_uuid,
                   mac,
                   mfg_company_id,
                   mfg_data,
                   name,
                   wifi_beacon_extended_info)
