# -*- coding: utf-8 -*-

"""
mistapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from mistapi.api_helper import APIHelper
from mistapi.models.acct_server import AcctServer
from mistapi.models.auth_server import AuthServer


class Radsec1(object):

    """Implementation of the 'Radsec1' model.

    TODO: type model description here.

    Attributes:
        acct_servers (list of AcctServer): TODO: type description here.
        auth_servers (list of AuthServer): TODO: type description here.
        enabled (bool): TODO: type description here.
        use_mxedge (bool): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "acct_servers": 'acct_servers',
        "auth_servers": 'auth_servers',
        "enabled": 'enabled',
        "use_mxedge": 'use_mxedge'
    }

    _optionals = [
        'acct_servers',
        'auth_servers',
        'enabled',
        'use_mxedge',
    ]

    def __init__(self,
                 acct_servers=APIHelper.SKIP,
                 auth_servers=APIHelper.SKIP,
                 enabled=APIHelper.SKIP,
                 use_mxedge=APIHelper.SKIP):
        """Constructor for the Radsec1 class"""

        # Initialize members of the class
        if acct_servers is not APIHelper.SKIP:
            self.acct_servers = acct_servers 
        if auth_servers is not APIHelper.SKIP:
            self.auth_servers = auth_servers 
        if enabled is not APIHelper.SKIP:
            self.enabled = enabled 
        if use_mxedge is not APIHelper.SKIP:
            self.use_mxedge = use_mxedge 

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
            acct_servers = [AcctServer.from_dictionary(x) for x in dictionary.get('acct_servers')]
        else:
            acct_servers = APIHelper.SKIP
        auth_servers = None
        if dictionary.get('auth_servers') is not None:
            auth_servers = [AuthServer.from_dictionary(x) for x in dictionary.get('auth_servers')]
        else:
            auth_servers = APIHelper.SKIP
        enabled = dictionary.get("enabled") if "enabled" in dictionary.keys() else APIHelper.SKIP
        use_mxedge = dictionary.get("use_mxedge") if "use_mxedge" in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(acct_servers,
                   auth_servers,
                   enabled,
                   use_mxedge)
