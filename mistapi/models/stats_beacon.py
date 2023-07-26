# -*- coding: utf-8 -*-

"""
mistapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from mistapi.api_helper import APIHelper


class StatsBeacon(object):

    """Implementation of the 'stats_beacon' model.

    TODO: type model description here.

    Attributes:
        battery_voltage (float): battery voltage, in mV
        eddystone_instance (string): TODO: type description here.
        eddystone_namespace (string): TODO: type description here.
        last_seen (float): TODO: type description here.
        mac (string): TODO: type description here.
        map_id (uuid|string): TODO: type description here.
        name (string): TODO: type description here.
        power (int): TODO: type description here.
        mtype (string): TODO: type description here.
        x (float): TODO: type description here.
        y (float): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "last_seen": 'last_seen',
        "mac": 'mac',
        "map_id": 'map_id',
        "name": 'name',
        "power": 'power',
        "mtype": 'type',
        "x": 'x',
        "y": 'y',
        "battery_voltage": 'battery_voltage',
        "eddystone_instance": 'eddystone_instance',
        "eddystone_namespace": 'eddystone_namespace'
    }

    _optionals = [
        'battery_voltage',
        'eddystone_instance',
        'eddystone_namespace',
    ]

    def __init__(self,
                 last_seen=None,
                 mac=None,
                 map_id=None,
                 name=None,
                 power=None,
                 mtype=None,
                 x=None,
                 y=None,
                 battery_voltage=APIHelper.SKIP,
                 eddystone_instance=APIHelper.SKIP,
                 eddystone_namespace=APIHelper.SKIP):
        """Constructor for the StatsBeacon class"""

        # Initialize members of the class
        if battery_voltage is not APIHelper.SKIP:
            self.battery_voltage = battery_voltage 
        if eddystone_instance is not APIHelper.SKIP:
            self.eddystone_instance = eddystone_instance 
        if eddystone_namespace is not APIHelper.SKIP:
            self.eddystone_namespace = eddystone_namespace 
        self.last_seen = last_seen 
        self.mac = mac 
        self.map_id = map_id 
        self.name = name 
        self.power = power 
        self.mtype = mtype 
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

        last_seen = dictionary.get("last_seen") if dictionary.get("last_seen") else None
        mac = dictionary.get("mac") if dictionary.get("mac") else None
        map_id = dictionary.get("map_id") if dictionary.get("map_id") else None
        name = dictionary.get("name") if dictionary.get("name") else None
        power = dictionary.get("power") if dictionary.get("power") else None
        mtype = dictionary.get("type") if dictionary.get("type") else None
        x = dictionary.get("x") if dictionary.get("x") else None
        y = dictionary.get("y") if dictionary.get("y") else None
        battery_voltage = dictionary.get("battery_voltage") if dictionary.get("battery_voltage") else APIHelper.SKIP
        eddystone_instance = dictionary.get("eddystone_instance") if dictionary.get("eddystone_instance") else APIHelper.SKIP
        eddystone_namespace = dictionary.get("eddystone_namespace") if dictionary.get("eddystone_namespace") else APIHelper.SKIP
        # Return an object of this model
        return cls(last_seen,
                   mac,
                   map_id,
                   name,
                   power,
                   mtype,
                   x,
                   y,
                   battery_voltage,
                   eddystone_instance,
                   eddystone_namespace)
