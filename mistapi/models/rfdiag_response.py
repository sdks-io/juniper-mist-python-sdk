# -*- coding: utf-8 -*-

"""
mistapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from mistapi.api_helper import APIHelper


class RfdiagResponse(object):

    """Implementation of the 'rfdiag.response' model.

    TODO: type model description here.

    Attributes:
        asset_id (uuid|string): if `type`==`asset`, id of the asset
        asset_name (string): if `type`==`asset`, name of the asset
        client_name (string): if `type`==`client`, hostname of the client
        duration (int): recording length in seconds, max is 120
        end_time (int): timestamp of end of recording
        frame_count (int): Number of frames in the output
        id (string): TODO: type description here.
        mac (string): if `type`==`client` or `asset`, mac of the device
        map_id (uuid|string): TODO: type description here.
        name (string): TODO: type description here.
        next (string): Optional. id of the next recoding if present. Only
            valid for site survey.
        raw_events (string): URL to a JSON file that contains array of raw
            location diag events
        ready (bool): whether it’s ready for playback
        sdkclient_id (uuid|string): if `type`==`sdkclient`, sdkclient_id of
            this recording
        sdkclient_name (string): if `type`==`sdkclient`, name of the
            sdkclient
        sdkclient_uuid (uuid|string): if `type`==`sdkclient`, device_id of
            sdkclient
        start_time (int): timestamp of the recording (the start)
        mtype (Type37Enum): sdkclient / client / asset
        url (string): URL to a JSON file that contains an array of frames,
            each frame is the same format

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "duration": 'duration',
        "end_time": 'end_time',
        "frame_count": 'frame_count',
        "map_id": 'map_id',
        "name": 'name',
        "raw_events": 'raw_events',
        "ready": 'ready',
        "start_time": 'start_time',
        "mtype": 'type',
        "url": 'url',
        "asset_id": 'asset_id',
        "asset_name": 'asset_name',
        "client_name": 'client_name',
        "id": 'id',
        "mac": 'mac',
        "next": 'next',
        "sdkclient_id": 'sdkclient_id',
        "sdkclient_name": 'sdkclient_name',
        "sdkclient_uuid": 'sdkclient_uuid'
    }

    _optionals = [
        'asset_id',
        'asset_name',
        'client_name',
        'id',
        'mac',
        'next',
        'sdkclient_id',
        'sdkclient_name',
        'sdkclient_uuid',
    ]

    def __init__(self,
                 duration=None,
                 end_time=None,
                 frame_count=None,
                 map_id=None,
                 name=None,
                 raw_events=None,
                 ready=None,
                 start_time=None,
                 mtype=None,
                 url=None,
                 asset_id=APIHelper.SKIP,
                 asset_name=APIHelper.SKIP,
                 client_name=APIHelper.SKIP,
                 id=APIHelper.SKIP,
                 mac=APIHelper.SKIP,
                 next=APIHelper.SKIP,
                 sdkclient_id=APIHelper.SKIP,
                 sdkclient_name=APIHelper.SKIP,
                 sdkclient_uuid=APIHelper.SKIP):
        """Constructor for the RfdiagResponse class"""

        # Initialize members of the class
        if asset_id is not APIHelper.SKIP:
            self.asset_id = asset_id 
        if asset_name is not APIHelper.SKIP:
            self.asset_name = asset_name 
        if client_name is not APIHelper.SKIP:
            self.client_name = client_name 
        self.duration = duration 
        self.end_time = end_time 
        self.frame_count = frame_count 
        if id is not APIHelper.SKIP:
            self.id = id 
        if mac is not APIHelper.SKIP:
            self.mac = mac 
        self.map_id = map_id 
        self.name = name 
        if next is not APIHelper.SKIP:
            self.next = next 
        self.raw_events = raw_events 
        self.ready = ready 
        if sdkclient_id is not APIHelper.SKIP:
            self.sdkclient_id = sdkclient_id 
        if sdkclient_name is not APIHelper.SKIP:
            self.sdkclient_name = sdkclient_name 
        if sdkclient_uuid is not APIHelper.SKIP:
            self.sdkclient_uuid = sdkclient_uuid 
        self.start_time = start_time 
        self.mtype = mtype 
        self.url = url 

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

        duration = dictionary.get("duration") if dictionary.get("duration") else None
        end_time = dictionary.get("end_time") if dictionary.get("end_time") else None
        frame_count = dictionary.get("frame_count") if dictionary.get("frame_count") else None
        map_id = dictionary.get("map_id") if dictionary.get("map_id") else None
        name = dictionary.get("name") if dictionary.get("name") else None
        raw_events = dictionary.get("raw_events") if dictionary.get("raw_events") else None
        ready = dictionary.get("ready") if "ready" in dictionary.keys() else None
        start_time = dictionary.get("start_time") if dictionary.get("start_time") else None
        mtype = dictionary.get("type") if dictionary.get("type") else None
        url = dictionary.get("url") if dictionary.get("url") else None
        asset_id = dictionary.get("asset_id") if dictionary.get("asset_id") else APIHelper.SKIP
        asset_name = dictionary.get("asset_name") if dictionary.get("asset_name") else APIHelper.SKIP
        client_name = dictionary.get("client_name") if dictionary.get("client_name") else APIHelper.SKIP
        id = dictionary.get("id") if dictionary.get("id") else APIHelper.SKIP
        mac = dictionary.get("mac") if dictionary.get("mac") else APIHelper.SKIP
        next = dictionary.get("next") if dictionary.get("next") else APIHelper.SKIP
        sdkclient_id = dictionary.get("sdkclient_id") if dictionary.get("sdkclient_id") else APIHelper.SKIP
        sdkclient_name = dictionary.get("sdkclient_name") if dictionary.get("sdkclient_name") else APIHelper.SKIP
        sdkclient_uuid = dictionary.get("sdkclient_uuid") if dictionary.get("sdkclient_uuid") else APIHelper.SKIP
        # Return an object of this model
        return cls(duration,
                   end_time,
                   frame_count,
                   map_id,
                   name,
                   raw_events,
                   ready,
                   start_time,
                   mtype,
                   url,
                   asset_id,
                   asset_name,
                   client_name,
                   id,
                   mac,
                   next,
                   sdkclient_id,
                   sdkclient_name,
                   sdkclient_uuid)
