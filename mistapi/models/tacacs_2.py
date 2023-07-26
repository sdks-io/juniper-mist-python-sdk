# -*- coding: utf-8 -*-

"""
mistapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from mistapi.api_helper import APIHelper
from mistapi.models.acct_server_2 import AcctServer2
from mistapi.models.tacplus_server import TacplusServer


class Tacacs2(object):

    """Implementation of the 'Tacacs2' model.

    TODO: type model description here.

    Attributes:
        acct_servers (list of AcctServer2): TODO: type description here.
        enabled (bool): TODO: type description here.
        network (string): TODO: type description here.
        tacplus_servers (list of TacplusServer): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "acct_servers": 'acct_servers',
        "enabled": 'enabled',
        "network": 'network',
        "tacplus_servers": 'tacplus_servers'
    }

    _optionals = [
        'acct_servers',
        'enabled',
        'network',
        'tacplus_servers',
    ]

    def __init__(self,
                 acct_servers=APIHelper.SKIP,
                 enabled=APIHelper.SKIP,
                 network=APIHelper.SKIP,
                 tacplus_servers=APIHelper.SKIP):
        """Constructor for the Tacacs2 class"""

        # Initialize members of the class
        if acct_servers is not APIHelper.SKIP:
            self.acct_servers = acct_servers 
        if enabled is not APIHelper.SKIP:
            self.enabled = enabled 
        if network is not APIHelper.SKIP:
            self.network = network 
        if tacplus_servers is not APIHelper.SKIP:
            self.tacplus_servers = tacplus_servers 

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
            acct_servers = [AcctServer2.from_dictionary(x) for x in dictionary.get('acct_servers')]
        else:
            acct_servers = APIHelper.SKIP
        enabled = dictionary.get("enabled") if "enabled" in dictionary.keys() else APIHelper.SKIP
        network = dictionary.get("network") if dictionary.get("network") else APIHelper.SKIP
        tacplus_servers = None
        if dictionary.get('tacplus_servers') is not None:
            tacplus_servers = [TacplusServer.from_dictionary(x) for x in dictionary.get('tacplus_servers')]
        else:
            tacplus_servers = APIHelper.SKIP
        # Return an object of this model
        return cls(acct_servers,
                   enabled,
                   network,
                   tacplus_servers)
