# -*- coding: utf-8 -*-

"""
mistapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from mistapi.api_helper import APIHelper
from mistapi.models.coa_server_1 import CoaServer1


class MxedgeDas(object):

    """Implementation of the 'mxedge_das' model.

    configure cloud-assisted dynamic authorization service on this cluster of
    mist edges

    Attributes:
        coa_servers (list of CoaServer1): dynamic authorization clients
            configured to send CoA|DM to mist edges on port 3799
        enabled (bool): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "coa_servers": 'coa_servers',
        "enabled": 'enabled'
    }

    _optionals = [
        'coa_servers',
        'enabled',
    ]

    def __init__(self,
                 coa_servers=APIHelper.SKIP,
                 enabled=False):
        """Constructor for the MxedgeDas class"""

        # Initialize members of the class
        if coa_servers is not APIHelper.SKIP:
            self.coa_servers = coa_servers 
        self.enabled = enabled 

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

        coa_servers = None
        if dictionary.get('coa_servers') is not None:
            coa_servers = [CoaServer1.from_dictionary(x) for x in dictionary.get('coa_servers')]
        else:
            coa_servers = APIHelper.SKIP
        enabled = dictionary.get("enabled") if dictionary.get("enabled") else False
        # Return an object of this model
        return cls(coa_servers,
                   enabled)
