# -*- coding: utf-8 -*-

"""
mistapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from mistapi.api_helper import APIHelper
from mistapi.models.acct_server_1 import AcctServer1
from mistapi.models.auth_server_1 import AuthServer1


class MxclusterRadsec(object):

    """Implementation of the 'mxcluster_radsec' model.

    MxEdge Radsec Configuration

    Attributes:
        acct_servers (list of AcctServer1): list of RADIUS accounting servers,
            optional, order matters where the first one is treated as primary
        auth_servers (list of AuthServer1): list of RADIUS authentication
            servers, order matters where the first one is treated as primary
        enabled (bool): whether to enable service on Mist Edge i.e. RADIUS
            proxy over TLS
        match_ssid (bool): whether to match ssid in request message to select
            from a subset of RADIUS servers
        proxy_hosts (list of string): hostnames or IPs for Mist AP to use as
            the TLS Server (i.e. they are reachable from AP) in addition to
            `tunterm_hosts`
        server_selection (ServerSelectionEnum): ordered (default) / unordered.
            When ordered, Mist Edge will prefer and go back to the first
            radius server if possible
        source (SourceEnum): Specify source address to use when connecting to
            RADIUS servers

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "acct_servers": 'acct_servers',
        "auth_servers": 'auth_servers',
        "enabled": 'enabled',
        "match_ssid": 'match_ssid',
        "proxy_hosts": 'proxy_hosts',
        "server_selection": 'server_selection',
        "source": 'source'
    }

    _optionals = [
        'acct_servers',
        'auth_servers',
        'enabled',
        'match_ssid',
        'proxy_hosts',
        'server_selection',
        'source',
    ]

    def __init__(self,
                 acct_servers=APIHelper.SKIP,
                 auth_servers=APIHelper.SKIP,
                 enabled=APIHelper.SKIP,
                 match_ssid=APIHelper.SKIP,
                 proxy_hosts=APIHelper.SKIP,
                 server_selection='ordered',
                 source='any'):
        """Constructor for the MxclusterRadsec class"""

        # Initialize members of the class
        if acct_servers is not APIHelper.SKIP:
            self.acct_servers = acct_servers 
        if auth_servers is not APIHelper.SKIP:
            self.auth_servers = auth_servers 
        if enabled is not APIHelper.SKIP:
            self.enabled = enabled 
        if match_ssid is not APIHelper.SKIP:
            self.match_ssid = match_ssid 
        if proxy_hosts is not APIHelper.SKIP:
            self.proxy_hosts = proxy_hosts 
        self.server_selection = server_selection 
        self.source = source 

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

        acct_servers = None
        if dictionary.get('acct_servers') is not None:
            acct_servers = [AcctServer1.from_dictionary(x) for x in dictionary.get('acct_servers')]
        else:
            acct_servers = APIHelper.SKIP
        auth_servers = None
        if dictionary.get('auth_servers') is not None:
            auth_servers = [AuthServer1.from_dictionary(x) for x in dictionary.get('auth_servers')]
        else:
            auth_servers = APIHelper.SKIP
        enabled = dictionary.get("enabled") if "enabled" in dictionary.keys() else APIHelper.SKIP
        match_ssid = dictionary.get("match_ssid") if "match_ssid" in dictionary.keys() else APIHelper.SKIP
        proxy_hosts = dictionary.get("proxy_hosts") if dictionary.get("proxy_hosts") else APIHelper.SKIP
        server_selection = dictionary.get("server_selection") if dictionary.get("server_selection") else 'ordered'
        source = dictionary.get("source") if dictionary.get("source") else 'any'
        # Return an object of this model
        return cls(acct_servers,
                   auth_servers,
                   enabled,
                   match_ssid,
                   proxy_hosts,
                   server_selection,
                   source)
