# -*- coding: utf-8 -*-

"""
mistapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from mistapi.api_helper import APIHelper
from mistapi.models.network_connection import NetworkConnection
from mistapi.models.vbeacon_1 import Vbeacon1
from mistapi.models.zone_2 import Zone2


class StatsSdkclientDetails(object):

    """Implementation of the 'stats_sdkclient_details' model.

    SDK Client Details statistics

    Attributes:
        id (uuid|string): TODO: type description here.
        last_seen (float): last seen timestamp
        map_id (uuid|string): map_id of the sdk client (if known), or null
        name (string): name of the sdk client (if provided)
        network_connection (NetworkConnection): various network connection
            info for the SDK client (if known, else omitted), with RSSI in
            dBm, and signal level as
        uuid (uuid|string): uuid of the sdk client
        vbeacons (list of Vbeacon1): list of beacon_id’s of the sdk client is
            in and since when (if known)
        x (float): x (in pixels) of user location on the map (if known)
        y (float): y (in pixels) of user location on the map (if known)
        zones (list of Zone2): list of zone_id’s of the sdk client is in and
            since when (if known)

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id": 'id',
        "last_seen": 'last_seen',
        "uuid": 'uuid',
        "map_id": 'map_id',
        "name": 'name',
        "network_connection": 'network_connection',
        "vbeacons": 'vbeacons',
        "x": 'x',
        "y": 'y',
        "zones": 'zones'
    }

    _optionals = [
        'map_id',
        'name',
        'network_connection',
        'vbeacons',
        'x',
        'y',
        'zones',
    ]

    _nullables = [
        'map_id',
    ]

    def __init__(self,
                 id=None,
                 last_seen=None,
                 uuid=None,
                 map_id=APIHelper.SKIP,
                 name=APIHelper.SKIP,
                 network_connection=APIHelper.SKIP,
                 vbeacons=APIHelper.SKIP,
                 x=APIHelper.SKIP,
                 y=APIHelper.SKIP,
                 zones=APIHelper.SKIP):
        """Constructor for the StatsSdkclientDetails class"""

        # Initialize members of the class
        self.id = id 
        self.last_seen = last_seen 
        if map_id is not APIHelper.SKIP:
            self.map_id = map_id 
        if name is not APIHelper.SKIP:
            self.name = name 
        if network_connection is not APIHelper.SKIP:
            self.network_connection = network_connection 
        self.uuid = uuid 
        if vbeacons is not APIHelper.SKIP:
            self.vbeacons = vbeacons 
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

        id = dictionary.get("id") if dictionary.get("id") else None
        last_seen = dictionary.get("last_seen") if dictionary.get("last_seen") else None
        uuid = dictionary.get("uuid") if dictionary.get("uuid") else None
        map_id = dictionary.get("map_id") if "map_id" in dictionary.keys() else APIHelper.SKIP
        name = dictionary.get("name") if dictionary.get("name") else APIHelper.SKIP
        network_connection = NetworkConnection.from_dictionary(dictionary.get('network_connection')) if 'network_connection' in dictionary.keys() else APIHelper.SKIP
        vbeacons = None
        if dictionary.get('vbeacons') is not None:
            vbeacons = [Vbeacon1.from_dictionary(x) for x in dictionary.get('vbeacons')]
        else:
            vbeacons = APIHelper.SKIP
        x = dictionary.get("x") if dictionary.get("x") else APIHelper.SKIP
        y = dictionary.get("y") if dictionary.get("y") else APIHelper.SKIP
        zones = None
        if dictionary.get('zones') is not None:
            zones = [Zone2.from_dictionary(x) for x in dictionary.get('zones')]
        else:
            zones = APIHelper.SKIP
        # Return an object of this model
        return cls(id,
                   last_seen,
                   uuid,
                   map_id,
                   name,
                   network_connection,
                   vbeacons,
                   x,
                   y,
                   zones)
