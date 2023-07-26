# -*- coding: utf-8 -*-

"""
mistapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from mistapi.api_helper import APIHelper


class Switches1(object):

    """Implementation of the 'Switches1' model.

    TODO: type model description here.

    Attributes:
        deviceprofile_id (string): TODO: type description here.
        downlink_ips (list of string): TODO: type description here.
        downlinks (list of string): TODO: type description here.
        esilaglinks (list of string): TODO: type description here.
        evpn_id (int): TODO: type description here.
        mac (string): TODO: type description here.
        pod (int): optionally, for distribution / access / esilag-access, they
            can be placed into different pods. e.g.  * for CLOS, to group dist
            / access switches into pods * for ERB/CRB, to group dist /
            esilag-access into pods
        role (Role5Enum): use `role`==`none` to remove a switch from the
            topology
        site_id (string): TODO: type description here.
        uplinks (list of string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "deviceprofile_id": 'deviceprofile_id',
        "downlink_ips": 'downlink_ips',
        "downlinks": 'downlinks',
        "esilaglinks": 'esilaglinks',
        "evpn_id": 'evpn_id',
        "mac": 'mac',
        "pod": 'pod',
        "role": 'role',
        "site_id": 'site_id',
        "uplinks": 'uplinks'
    }

    _optionals = [
        'deviceprofile_id',
        'downlink_ips',
        'downlinks',
        'esilaglinks',
        'evpn_id',
        'mac',
        'pod',
        'role',
        'site_id',
        'uplinks',
    ]

    def __init__(self,
                 deviceprofile_id=APIHelper.SKIP,
                 downlink_ips=APIHelper.SKIP,
                 downlinks=APIHelper.SKIP,
                 esilaglinks=APIHelper.SKIP,
                 evpn_id=APIHelper.SKIP,
                 mac=APIHelper.SKIP,
                 pod=1,
                 role=APIHelper.SKIP,
                 site_id=APIHelper.SKIP,
                 uplinks=APIHelper.SKIP):
        """Constructor for the Switches1 class"""

        # Initialize members of the class
        if deviceprofile_id is not APIHelper.SKIP:
            self.deviceprofile_id = deviceprofile_id 
        if downlink_ips is not APIHelper.SKIP:
            self.downlink_ips = downlink_ips 
        if downlinks is not APIHelper.SKIP:
            self.downlinks = downlinks 
        if esilaglinks is not APIHelper.SKIP:
            self.esilaglinks = esilaglinks 
        if evpn_id is not APIHelper.SKIP:
            self.evpn_id = evpn_id 
        if mac is not APIHelper.SKIP:
            self.mac = mac 
        self.pod = pod 
        if role is not APIHelper.SKIP:
            self.role = role 
        if site_id is not APIHelper.SKIP:
            self.site_id = site_id 
        if uplinks is not APIHelper.SKIP:
            self.uplinks = uplinks 

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

        deviceprofile_id = dictionary.get("deviceprofile_id") if dictionary.get("deviceprofile_id") else APIHelper.SKIP
        downlink_ips = dictionary.get("downlink_ips") if dictionary.get("downlink_ips") else APIHelper.SKIP
        downlinks = dictionary.get("downlinks") if dictionary.get("downlinks") else APIHelper.SKIP
        esilaglinks = dictionary.get("esilaglinks") if dictionary.get("esilaglinks") else APIHelper.SKIP
        evpn_id = dictionary.get("evpn_id") if dictionary.get("evpn_id") else APIHelper.SKIP
        mac = dictionary.get("mac") if dictionary.get("mac") else APIHelper.SKIP
        pod = dictionary.get("pod") if dictionary.get("pod") else 1
        role = dictionary.get("role") if dictionary.get("role") else APIHelper.SKIP
        site_id = dictionary.get("site_id") if dictionary.get("site_id") else APIHelper.SKIP
        uplinks = dictionary.get("uplinks") if dictionary.get("uplinks") else APIHelper.SKIP
        # Return an object of this model
        return cls(deviceprofile_id,
                   downlink_ips,
                   downlinks,
                   esilaglinks,
                   evpn_id,
                   mac,
                   pod,
                   role,
                   site_id,
                   uplinks)
