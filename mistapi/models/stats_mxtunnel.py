# -*- coding: utf-8 -*-

"""
mistapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from mistapi.api_helper import APIHelper
from mistapi.models.sessions_1 import Sessions1


class StatsMxtunnel(object):

    """Implementation of the 'stats_mxtunnel' model.

    MxTunnels statistics

    Attributes:
        ap (string): TODO: type description here.
        for_site (bool): TODO: type description here.
        last_seen (int): TODO: type description here.
        mxcluster_id (uuid|string): TODO: type description here.
        mxedge_id (uuid|string): TODO: type description here.
        mxtunnel_id (uuid|string): TODO: type description here.
        org_id (uuid|string): TODO: type description here.
        peer_mxedge_id (uuid|string): MxEdge ID of the peer(mist edge to mist
            edge tunnel)
        remote_ip (string): TODO: type description here.
        remote_port (int): TODO: type description here.
        rx_control_pkts (int): TODO: type description here.
        sessions (list of Sessions1): list of sessions
        site_id (uuid|string): TODO: type description here.
        state (State1Enum): idle / wait-ctrl-reply / wait-ctrl-conn /
            established / established_with_sessions
        tx_control_pkts (int): TODO: type description here.
        uptime (int): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "ap": 'ap',
        "for_site": 'for_site',
        "last_seen": 'last_seen',
        "mxcluster_id": 'mxcluster_id',
        "mxedge_id": 'mxedge_id',
        "mxtunnel_id": 'mxtunnel_id',
        "org_id": 'org_id',
        "peer_mxedge_id": 'peer_mxedge_id',
        "remote_ip": 'remote_ip',
        "remote_port": 'remote_port',
        "rx_control_pkts": 'rx_control_pkts',
        "sessions": 'sessions',
        "site_id": 'site_id',
        "state": 'state',
        "tx_control_pkts": 'tx_control_pkts',
        "uptime": 'uptime'
    }

    _optionals = [
        'ap',
        'for_site',
        'last_seen',
        'mxcluster_id',
        'mxedge_id',
        'mxtunnel_id',
        'org_id',
        'peer_mxedge_id',
        'remote_ip',
        'remote_port',
        'rx_control_pkts',
        'sessions',
        'site_id',
        'state',
        'tx_control_pkts',
        'uptime',
    ]

    def __init__(self,
                 ap=APIHelper.SKIP,
                 for_site=APIHelper.SKIP,
                 last_seen=APIHelper.SKIP,
                 mxcluster_id=APIHelper.SKIP,
                 mxedge_id=APIHelper.SKIP,
                 mxtunnel_id=APIHelper.SKIP,
                 org_id=APIHelper.SKIP,
                 peer_mxedge_id=APIHelper.SKIP,
                 remote_ip=APIHelper.SKIP,
                 remote_port=APIHelper.SKIP,
                 rx_control_pkts=APIHelper.SKIP,
                 sessions=APIHelper.SKIP,
                 site_id=APIHelper.SKIP,
                 state=APIHelper.SKIP,
                 tx_control_pkts=APIHelper.SKIP,
                 uptime=APIHelper.SKIP):
        """Constructor for the StatsMxtunnel class"""

        # Initialize members of the class
        if ap is not APIHelper.SKIP:
            self.ap = ap 
        if for_site is not APIHelper.SKIP:
            self.for_site = for_site 
        if last_seen is not APIHelper.SKIP:
            self.last_seen = last_seen 
        if mxcluster_id is not APIHelper.SKIP:
            self.mxcluster_id = mxcluster_id 
        if mxedge_id is not APIHelper.SKIP:
            self.mxedge_id = mxedge_id 
        if mxtunnel_id is not APIHelper.SKIP:
            self.mxtunnel_id = mxtunnel_id 
        if org_id is not APIHelper.SKIP:
            self.org_id = org_id 
        if peer_mxedge_id is not APIHelper.SKIP:
            self.peer_mxedge_id = peer_mxedge_id 
        if remote_ip is not APIHelper.SKIP:
            self.remote_ip = remote_ip 
        if remote_port is not APIHelper.SKIP:
            self.remote_port = remote_port 
        if rx_control_pkts is not APIHelper.SKIP:
            self.rx_control_pkts = rx_control_pkts 
        if sessions is not APIHelper.SKIP:
            self.sessions = sessions 
        if site_id is not APIHelper.SKIP:
            self.site_id = site_id 
        if state is not APIHelper.SKIP:
            self.state = state 
        if tx_control_pkts is not APIHelper.SKIP:
            self.tx_control_pkts = tx_control_pkts 
        if uptime is not APIHelper.SKIP:
            self.uptime = uptime 

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

        ap = dictionary.get("ap") if dictionary.get("ap") else APIHelper.SKIP
        for_site = dictionary.get("for_site") if "for_site" in dictionary.keys() else APIHelper.SKIP
        last_seen = dictionary.get("last_seen") if dictionary.get("last_seen") else APIHelper.SKIP
        mxcluster_id = dictionary.get("mxcluster_id") if dictionary.get("mxcluster_id") else APIHelper.SKIP
        mxedge_id = dictionary.get("mxedge_id") if dictionary.get("mxedge_id") else APIHelper.SKIP
        mxtunnel_id = dictionary.get("mxtunnel_id") if dictionary.get("mxtunnel_id") else APIHelper.SKIP
        org_id = dictionary.get("org_id") if dictionary.get("org_id") else APIHelper.SKIP
        peer_mxedge_id = dictionary.get("peer_mxedge_id") if dictionary.get("peer_mxedge_id") else APIHelper.SKIP
        remote_ip = dictionary.get("remote_ip") if dictionary.get("remote_ip") else APIHelper.SKIP
        remote_port = dictionary.get("remote_port") if dictionary.get("remote_port") else APIHelper.SKIP
        rx_control_pkts = dictionary.get("rx_control_pkts") if dictionary.get("rx_control_pkts") else APIHelper.SKIP
        sessions = None
        if dictionary.get('sessions') is not None:
            sessions = [Sessions1.from_dictionary(x) for x in dictionary.get('sessions')]
        else:
            sessions = APIHelper.SKIP
        site_id = dictionary.get("site_id") if dictionary.get("site_id") else APIHelper.SKIP
        state = dictionary.get("state") if dictionary.get("state") else APIHelper.SKIP
        tx_control_pkts = dictionary.get("tx_control_pkts") if dictionary.get("tx_control_pkts") else APIHelper.SKIP
        uptime = dictionary.get("uptime") if dictionary.get("uptime") else APIHelper.SKIP
        # Return an object of this model
        return cls(ap,
                   for_site,
                   last_seen,
                   mxcluster_id,
                   mxedge_id,
                   mxtunnel_id,
                   org_id,
                   peer_mxedge_id,
                   remote_ip,
                   remote_port,
                   rx_control_pkts,
                   sessions,
                   site_id,
                   state,
                   tx_control_pkts,
                   uptime)
