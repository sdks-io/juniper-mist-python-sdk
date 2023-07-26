# -*- coding: utf-8 -*-

"""
mistapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from mistapi.api_helper import APIHelper


class Alarm(object):

    """Implementation of the 'alarm' model.

    additional information per alarm type

    Attributes:
        ack_admin_id (uuid|string): UUID of the admin who acked the alarm
        ack_admin_name (string): Name & Email ID of the admin who acked the
            alarm
        acked (bool): Whether the alarm is acked or not
        acked_time (int): Epoch (seconds) when the alarm was acked
        aps (list of string): additional information: List of MACs of the APs
            e.g. [“ffeeddccbbaa”, “ffeeddccbbab”]
        bssids (list of string): List of BSSIDs
        count (int): Number of incident within an alarm window
        gateways (list of string): additional information: List of MACs of the
            gateways e.g. [“ffeeddccbbaa”, “ffeeddccbbab”]
        group (string): Group of the alarm
        hostnames (list of string): additional information: List of Hostnames
            of the devices (AP/Switch/Gateway)
        id (uuid|string): UUID of the alarm
        last_seen (int): Epoch (seconds) of the last incident/alarm within an
            alarm window
        note (string): Text describing the alarm
        org_id (uuid|string): UUID of the org
        severity (string): Severity of the alarm
        site_id (uuid|string): UUID of the site
        ssids (list of string): List of SSIDs
        switches (list of string): additional information: List of MACs of the
            switches e.g. [“ffeeddccbbaa”, “ffeeddccbbab”]
        timestamp (int): Epoch (seconds) of the first incident/alarm
        mtype (string): Key-name of the alarm type

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "count": 'count',
        "group": 'group',
        "id": 'id',
        "last_seen": 'last_seen',
        "severity": 'severity',
        "timestamp": 'timestamp',
        "mtype": 'type',
        "ack_admin_id": 'ack_admin_id',
        "ack_admin_name": 'ack_admin_name',
        "acked": 'acked',
        "acked_time": 'acked_time',
        "aps": 'aps',
        "bssids": 'bssids',
        "gateways": 'gateways',
        "hostnames": 'hostnames',
        "note": 'note',
        "org_id": 'org_id',
        "site_id": 'site_id',
        "ssids": 'ssids',
        "switches": 'switches'
    }

    _optionals = [
        'ack_admin_id',
        'ack_admin_name',
        'acked',
        'acked_time',
        'aps',
        'bssids',
        'gateways',
        'hostnames',
        'note',
        'org_id',
        'site_id',
        'ssids',
        'switches',
    ]

    def __init__(self,
                 count=None,
                 group=None,
                 id=None,
                 last_seen=None,
                 severity=None,
                 timestamp=None,
                 mtype=None,
                 ack_admin_id=APIHelper.SKIP,
                 ack_admin_name=APIHelper.SKIP,
                 acked=APIHelper.SKIP,
                 acked_time=APIHelper.SKIP,
                 aps=APIHelper.SKIP,
                 bssids=APIHelper.SKIP,
                 gateways=APIHelper.SKIP,
                 hostnames=APIHelper.SKIP,
                 note=APIHelper.SKIP,
                 org_id=APIHelper.SKIP,
                 site_id=APIHelper.SKIP,
                 ssids=APIHelper.SKIP,
                 switches=APIHelper.SKIP):
        """Constructor for the Alarm class"""

        # Initialize members of the class
        if ack_admin_id is not APIHelper.SKIP:
            self.ack_admin_id = ack_admin_id 
        if ack_admin_name is not APIHelper.SKIP:
            self.ack_admin_name = ack_admin_name 
        if acked is not APIHelper.SKIP:
            self.acked = acked 
        if acked_time is not APIHelper.SKIP:
            self.acked_time = acked_time 
        if aps is not APIHelper.SKIP:
            self.aps = aps 
        if bssids is not APIHelper.SKIP:
            self.bssids = bssids 
        self.count = count 
        if gateways is not APIHelper.SKIP:
            self.gateways = gateways 
        self.group = group 
        if hostnames is not APIHelper.SKIP:
            self.hostnames = hostnames 
        self.id = id 
        self.last_seen = last_seen 
        if note is not APIHelper.SKIP:
            self.note = note 
        if org_id is not APIHelper.SKIP:
            self.org_id = org_id 
        self.severity = severity 
        if site_id is not APIHelper.SKIP:
            self.site_id = site_id 
        if ssids is not APIHelper.SKIP:
            self.ssids = ssids 
        if switches is not APIHelper.SKIP:
            self.switches = switches 
        self.timestamp = timestamp 
        self.mtype = mtype 

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

        count = dictionary.get("count") if dictionary.get("count") else None
        group = dictionary.get("group") if dictionary.get("group") else None
        id = dictionary.get("id") if dictionary.get("id") else None
        last_seen = dictionary.get("last_seen") if dictionary.get("last_seen") else None
        severity = dictionary.get("severity") if dictionary.get("severity") else None
        timestamp = dictionary.get("timestamp") if dictionary.get("timestamp") else None
        mtype = dictionary.get("type") if dictionary.get("type") else None
        ack_admin_id = dictionary.get("ack_admin_id") if dictionary.get("ack_admin_id") else APIHelper.SKIP
        ack_admin_name = dictionary.get("ack_admin_name") if dictionary.get("ack_admin_name") else APIHelper.SKIP
        acked = dictionary.get("acked") if "acked" in dictionary.keys() else APIHelper.SKIP
        acked_time = dictionary.get("acked_time") if dictionary.get("acked_time") else APIHelper.SKIP
        aps = dictionary.get("aps") if dictionary.get("aps") else APIHelper.SKIP
        bssids = dictionary.get("bssids") if dictionary.get("bssids") else APIHelper.SKIP
        gateways = dictionary.get("gateways") if dictionary.get("gateways") else APIHelper.SKIP
        hostnames = dictionary.get("hostnames") if dictionary.get("hostnames") else APIHelper.SKIP
        note = dictionary.get("note") if dictionary.get("note") else APIHelper.SKIP
        org_id = dictionary.get("org_id") if dictionary.get("org_id") else APIHelper.SKIP
        site_id = dictionary.get("site_id") if dictionary.get("site_id") else APIHelper.SKIP
        ssids = dictionary.get("ssids") if dictionary.get("ssids") else APIHelper.SKIP
        switches = dictionary.get("switches") if dictionary.get("switches") else APIHelper.SKIP
        # Return an object of this model
        return cls(count,
                   group,
                   id,
                   last_seen,
                   severity,
                   timestamp,
                   mtype,
                   ack_admin_id,
                   ack_admin_name,
                   acked,
                   acked_time,
                   aps,
                   bssids,
                   gateways,
                   hostnames,
                   note,
                   org_id,
                   site_id,
                   ssids,
                   switches)
