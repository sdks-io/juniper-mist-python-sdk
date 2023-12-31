# -*- coding: utf-8 -*-

"""
mistapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from mistapi.api_helper import APIHelper
from mistapi.models.rssizone_1 import Rssizone1
from mistapi.models.zone_4 import Zone4


class StatsAsset(object):

    """Implementation of the 'stats_asset' model.

    Asset statistics

    Attributes:
        battery_voltage (float): battery voltage, in mV
        eddystone_uid_instance (string): TODO: type description here.
        eddystone_uid_namespace (string): TODO: type description here.
        eddystone_url_url (string): TODO: type description here.
        ibeacon_major (int): TODO: type description here.
        ibeacon_minor (int): TODO: type description here.
        ibeacon_uuid (uuid|string): TODO: type description here.
        last_seen (float): last seen timestamp
        mac (string): bluetooth MAC
        map_id (uuid|string): map where the device belongs to
        name (string): name / label of the device
        rssizones (list of Rssizone1): only send this for individual asset
            stat
        x (float): x in pixel
        y (float): y in pixel
        zones (list of Zone4): only send this for individual asset stat

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "mac": 'mac',
        "battery_voltage": 'battery_voltage',
        "eddystone_uid_instance": 'eddystone_uid_instance',
        "eddystone_uid_namespace": 'eddystone_uid_namespace',
        "eddystone_url_url": 'eddystone_url_url',
        "ibeacon_major": 'ibeacon_major',
        "ibeacon_minor": 'ibeacon_minor',
        "ibeacon_uuid": 'ibeacon_uuid',
        "last_seen": 'last_seen',
        "map_id": 'map_id',
        "name": 'name',
        "rssizones": 'rssizones',
        "x": 'x',
        "y": 'y',
        "zones": 'zones'
    }

    _optionals = [
        'battery_voltage',
        'eddystone_uid_instance',
        'eddystone_uid_namespace',
        'eddystone_url_url',
        'ibeacon_major',
        'ibeacon_minor',
        'ibeacon_uuid',
        'last_seen',
        'map_id',
        'name',
        'rssizones',
        'x',
        'y',
        'zones',
    ]

    def __init__(self,
                 mac=None,
                 battery_voltage=APIHelper.SKIP,
                 eddystone_uid_instance=APIHelper.SKIP,
                 eddystone_uid_namespace=APIHelper.SKIP,
                 eddystone_url_url=APIHelper.SKIP,
                 ibeacon_major=APIHelper.SKIP,
                 ibeacon_minor=APIHelper.SKIP,
                 ibeacon_uuid=APIHelper.SKIP,
                 last_seen=APIHelper.SKIP,
                 map_id=APIHelper.SKIP,
                 name=APIHelper.SKIP,
                 rssizones=APIHelper.SKIP,
                 x=APIHelper.SKIP,
                 y=APIHelper.SKIP,
                 zones=APIHelper.SKIP):
        """Constructor for the StatsAsset class"""

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
        if last_seen is not APIHelper.SKIP:
            self.last_seen = last_seen 
        self.mac = mac 
        if map_id is not APIHelper.SKIP:
            self.map_id = map_id 
        if name is not APIHelper.SKIP:
            self.name = name 
        if rssizones is not APIHelper.SKIP:
            self.rssizones = rssizones 
        if x is not APIHelper.SKIP:
            self.x = x 
        if y is not APIHelper.SKIP:
            self.y = y 
        if zones is not APIHelper.SKIP:
            self.zones = zones 

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

        mac = dictionary.get("mac") if dictionary.get("mac") else None
        battery_voltage = dictionary.get("battery_voltage") if dictionary.get("battery_voltage") else APIHelper.SKIP
        eddystone_uid_instance = dictionary.get("eddystone_uid_instance") if dictionary.get("eddystone_uid_instance") else APIHelper.SKIP
        eddystone_uid_namespace = dictionary.get("eddystone_uid_namespace") if dictionary.get("eddystone_uid_namespace") else APIHelper.SKIP
        eddystone_url_url = dictionary.get("eddystone_url_url") if dictionary.get("eddystone_url_url") else APIHelper.SKIP
        ibeacon_major = dictionary.get("ibeacon_major") if dictionary.get("ibeacon_major") else APIHelper.SKIP
        ibeacon_minor = dictionary.get("ibeacon_minor") if dictionary.get("ibeacon_minor") else APIHelper.SKIP
        ibeacon_uuid = dictionary.get("ibeacon_uuid") if dictionary.get("ibeacon_uuid") else APIHelper.SKIP
        last_seen = dictionary.get("last_seen") if dictionary.get("last_seen") else APIHelper.SKIP
        map_id = dictionary.get("map_id") if dictionary.get("map_id") else APIHelper.SKIP
        name = dictionary.get("name") if dictionary.get("name") else APIHelper.SKIP
        rssizones = None
        if dictionary.get('rssizones') is not None:
            rssizones = [Rssizone1.from_dictionary(x) for x in dictionary.get('rssizones')]
        else:
            rssizones = APIHelper.SKIP
        x = dictionary.get("x") if dictionary.get("x") else APIHelper.SKIP
        y = dictionary.get("y") if dictionary.get("y") else APIHelper.SKIP
        zones = None
        if dictionary.get('zones') is not None:
            zones = [Zone4.from_dictionary(x) for x in dictionary.get('zones')]
        else:
            zones = APIHelper.SKIP
        # Return an object of this model
        return cls(mac,
                   battery_voltage,
                   eddystone_uid_instance,
                   eddystone_uid_namespace,
                   eddystone_url_url,
                   ibeacon_major,
                   ibeacon_minor,
                   ibeacon_uuid,
                   last_seen,
                   map_id,
                   name,
                   rssizones,
                   x,
                   y,
                   zones)
