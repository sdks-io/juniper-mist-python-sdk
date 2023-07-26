# -*- coding: utf-8 -*-

"""
mistapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from mistapi.api_helper import APIHelper
from mistapi.models.acct_server import AcctServer
from mistapi.models.auth_server import AuthServer


class JunosRadiusConfig(object):

    """Implementation of the 'junos_radius_config' model.

    Junos Radius config

    Attributes:
        acct_interim_interval (int): how frequently should interim accounting
            be reported, 60-65535. default is 0 (use one specified in
            Access-Accept request from RADIUS Server). Very frequent messages
            can affect the performance of the radius server, 600 and up is
            recommended when enabled
        acct_servers (list of AcctServer): TODO: type description here.
        auth_servers (list of AuthServer): TODO: type description here.
        auth_servers_retries (int): radius auth session retries
        auth_servers_timeout (int): radius auth session timeout
        coa_enabled (bool): TODO: type description here.
        coa_port (int): TODO: type description here.
        network (string): use `network`or `source_ip` which network the RADIUS
            server resides, if there's static IP for this network, we'd use it
            as source-ip
        source_ip (string): use `network`or `source_ip`

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "acct_interim_interval": 'acct_interim_interval',
        "acct_servers": 'acct_servers',
        "auth_servers": 'auth_servers',
        "auth_servers_retries": 'auth_servers_retries',
        "auth_servers_timeout": 'auth_servers_timeout',
        "coa_enabled": 'coa_enabled',
        "coa_port": 'coa_port',
        "network": 'network',
        "source_ip": 'source_ip'
    }

    _optionals = [
        'acct_interim_interval',
        'acct_servers',
        'auth_servers',
        'auth_servers_retries',
        'auth_servers_timeout',
        'coa_enabled',
        'coa_port',
        'network',
        'source_ip',
    ]

    def __init__(self,
                 acct_interim_interval=0,
                 acct_servers=APIHelper.SKIP,
                 auth_servers=APIHelper.SKIP,
                 auth_servers_retries=3,
                 auth_servers_timeout=5,
                 coa_enabled=False,
                 coa_port=3799,
                 network=APIHelper.SKIP,
                 source_ip=APIHelper.SKIP):
        """Constructor for the JunosRadiusConfig class"""

        # Initialize members of the class
        self.acct_interim_interval = acct_interim_interval 
        if acct_servers is not APIHelper.SKIP:
            self.acct_servers = acct_servers 
        if auth_servers is not APIHelper.SKIP:
            self.auth_servers = auth_servers 
        self.auth_servers_retries = auth_servers_retries 
        self.auth_servers_timeout = auth_servers_timeout 
        self.coa_enabled = coa_enabled 
        self.coa_port = coa_port 
        if network is not APIHelper.SKIP:
            self.network = network 
        if source_ip is not APIHelper.SKIP:
            self.source_ip = source_ip 

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

        acct_interim_interval = dictionary.get("acct_interim_interval") if dictionary.get("acct_interim_interval") else 0
        acct_servers = None
        if dictionary.get('acct_servers') is not None:
            acct_servers = [AcctServer.from_dictionary(x) for x in dictionary.get('acct_servers')]
        else:
            acct_servers = APIHelper.SKIP
        auth_servers = None
        if dictionary.get('auth_servers') is not None:
            auth_servers = [AuthServer.from_dictionary(x) for x in dictionary.get('auth_servers')]
        else:
            auth_servers = APIHelper.SKIP
        auth_servers_retries = dictionary.get("auth_servers_retries") if dictionary.get("auth_servers_retries") else 3
        auth_servers_timeout = dictionary.get("auth_servers_timeout") if dictionary.get("auth_servers_timeout") else 5
        coa_enabled = dictionary.get("coa_enabled") if dictionary.get("coa_enabled") else False
        coa_port = dictionary.get("coa_port") if dictionary.get("coa_port") else 3799
        network = dictionary.get("network") if dictionary.get("network") else APIHelper.SKIP
        source_ip = dictionary.get("source_ip") if dictionary.get("source_ip") else APIHelper.SKIP
        # Return an object of this model
        return cls(acct_interim_interval,
                   acct_servers,
                   auth_servers,
                   auth_servers_retries,
                   auth_servers_timeout,
                   coa_enabled,
                   coa_port,
                   network,
                   source_ip)