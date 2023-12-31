# -*- coding: utf-8 -*-

"""
mistapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from mistapi.api_helper import APIHelper


class StatsWantunnel(object):

    """Implementation of the 'stats_wantunnel' model.

    TODO: type model description here.

    Attributes:
        auth_algo (string): authentication algorithm
        encrypt_algo (string): encryption algorithm
        ike_version (string): ike version
        ip (string): ip address
        last_event (string): reason of why the tunnel is down
        mac (string): router mac address
        node (string): node0/node1
        org_id (string): TODO: type description here.
        peer_host (string): peer host
        peer_ip (string): peer ip address
        protocol (Protocol8Enum): TODO: type description here.
        rx_bytes (int): TODO: type description here.
        rx_pkts (int): TODO: type description here.
        site_id (string): TODO: type description here.
        tunnel_name (string): Mist Tunnel Name
        tx_bytes (int): TODO: type description here.
        tx_pkts (int): TODO: type description here.
        up (bool): TODO: type description here.
        uptime (int): duration from first (or last) SA was established

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "auth_algo": 'auth_algo',
        "encrypt_algo": 'encrypt_algo',
        "ike_version": 'ike_version',
        "ip": 'ip',
        "last_event": 'last_event',
        "mac": 'mac',
        "node": 'node',
        "org_id": 'org_id',
        "peer_host": 'peer_host',
        "peer_ip": 'peer_ip',
        "protocol": 'protocol',
        "rx_bytes": 'rx_bytes',
        "rx_pkts": 'rx_pkts',
        "site_id": 'site_id',
        "tunnel_name": 'tunnel_name',
        "tx_bytes": 'tx_bytes',
        "tx_pkts": 'tx_pkts',
        "up": 'up',
        "uptime": 'uptime'
    }

    _optionals = [
        'auth_algo',
        'encrypt_algo',
        'ike_version',
        'ip',
        'last_event',
        'mac',
        'node',
        'org_id',
        'peer_host',
        'peer_ip',
        'protocol',
        'rx_bytes',
        'rx_pkts',
        'site_id',
        'tunnel_name',
        'tx_bytes',
        'tx_pkts',
        'up',
        'uptime',
    ]

    def __init__(self,
                 auth_algo=APIHelper.SKIP,
                 encrypt_algo=APIHelper.SKIP,
                 ike_version=APIHelper.SKIP,
                 ip=APIHelper.SKIP,
                 last_event=APIHelper.SKIP,
                 mac=APIHelper.SKIP,
                 node=APIHelper.SKIP,
                 org_id=APIHelper.SKIP,
                 peer_host=APIHelper.SKIP,
                 peer_ip=APIHelper.SKIP,
                 protocol=APIHelper.SKIP,
                 rx_bytes=APIHelper.SKIP,
                 rx_pkts=APIHelper.SKIP,
                 site_id=APIHelper.SKIP,
                 tunnel_name=APIHelper.SKIP,
                 tx_bytes=APIHelper.SKIP,
                 tx_pkts=APIHelper.SKIP,
                 up=APIHelper.SKIP,
                 uptime=APIHelper.SKIP):
        """Constructor for the StatsWantunnel class"""

        # Initialize members of the class
        if auth_algo is not APIHelper.SKIP:
            self.auth_algo = auth_algo 
        if encrypt_algo is not APIHelper.SKIP:
            self.encrypt_algo = encrypt_algo 
        if ike_version is not APIHelper.SKIP:
            self.ike_version = ike_version 
        if ip is not APIHelper.SKIP:
            self.ip = ip 
        if last_event is not APIHelper.SKIP:
            self.last_event = last_event 
        if mac is not APIHelper.SKIP:
            self.mac = mac 
        if node is not APIHelper.SKIP:
            self.node = node 
        if org_id is not APIHelper.SKIP:
            self.org_id = org_id 
        if peer_host is not APIHelper.SKIP:
            self.peer_host = peer_host 
        if peer_ip is not APIHelper.SKIP:
            self.peer_ip = peer_ip 
        if protocol is not APIHelper.SKIP:
            self.protocol = protocol 
        if rx_bytes is not APIHelper.SKIP:
            self.rx_bytes = rx_bytes 
        if rx_pkts is not APIHelper.SKIP:
            self.rx_pkts = rx_pkts 
        if site_id is not APIHelper.SKIP:
            self.site_id = site_id 
        if tunnel_name is not APIHelper.SKIP:
            self.tunnel_name = tunnel_name 
        if tx_bytes is not APIHelper.SKIP:
            self.tx_bytes = tx_bytes 
        if tx_pkts is not APIHelper.SKIP:
            self.tx_pkts = tx_pkts 
        if up is not APIHelper.SKIP:
            self.up = up 
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

        auth_algo = dictionary.get("auth_algo") if dictionary.get("auth_algo") else APIHelper.SKIP
        encrypt_algo = dictionary.get("encrypt_algo") if dictionary.get("encrypt_algo") else APIHelper.SKIP
        ike_version = dictionary.get("ike_version") if dictionary.get("ike_version") else APIHelper.SKIP
        ip = dictionary.get("ip") if dictionary.get("ip") else APIHelper.SKIP
        last_event = dictionary.get("last_event") if dictionary.get("last_event") else APIHelper.SKIP
        mac = dictionary.get("mac") if dictionary.get("mac") else APIHelper.SKIP
        node = dictionary.get("node") if dictionary.get("node") else APIHelper.SKIP
        org_id = dictionary.get("org_id") if dictionary.get("org_id") else APIHelper.SKIP
        peer_host = dictionary.get("peer_host") if dictionary.get("peer_host") else APIHelper.SKIP
        peer_ip = dictionary.get("peer_ip") if dictionary.get("peer_ip") else APIHelper.SKIP
        protocol = dictionary.get("protocol") if dictionary.get("protocol") else APIHelper.SKIP
        rx_bytes = dictionary.get("rx_bytes") if dictionary.get("rx_bytes") else APIHelper.SKIP
        rx_pkts = dictionary.get("rx_pkts") if dictionary.get("rx_pkts") else APIHelper.SKIP
        site_id = dictionary.get("site_id") if dictionary.get("site_id") else APIHelper.SKIP
        tunnel_name = dictionary.get("tunnel_name") if dictionary.get("tunnel_name") else APIHelper.SKIP
        tx_bytes = dictionary.get("tx_bytes") if dictionary.get("tx_bytes") else APIHelper.SKIP
        tx_pkts = dictionary.get("tx_pkts") if dictionary.get("tx_pkts") else APIHelper.SKIP
        up = dictionary.get("up") if "up" in dictionary.keys() else APIHelper.SKIP
        uptime = dictionary.get("uptime") if dictionary.get("uptime") else APIHelper.SKIP
        # Return an object of this model
        return cls(auth_algo,
                   encrypt_algo,
                   ike_version,
                   ip,
                   last_event,
                   mac,
                   node,
                   org_id,
                   peer_host,
                   peer_ip,
                   protocol,
                   rx_bytes,
                   rx_pkts,
                   site_id,
                   tunnel_name,
                   tx_bytes,
                   tx_pkts,
                   up,
                   uptime)
