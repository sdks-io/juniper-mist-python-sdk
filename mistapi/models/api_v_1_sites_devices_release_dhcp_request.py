# -*- coding: utf-8 -*-

"""
mistapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from mistapi.api_helper import APIHelper


class ApiV1SitesDevicesReleaseDhcpRequest(object):

    """Implementation of the 'Api V1 Sites Devices Release Dhcp Request' model.

    TODO: type model description here.

    Attributes:
        node (NodeEnum): only for HA
        port (string): The nework interface on which to release the current
            DHCP release

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "port": 'port',
        "node": 'node'
    }

    _optionals = [
        'node',
    ]

    def __init__(self,
                 port=None,
                 node=APIHelper.SKIP):
        """Constructor for the ApiV1SitesDevicesReleaseDhcpRequest class"""

        # Initialize members of the class
        if node is not APIHelper.SKIP:
            self.node = node 
        self.port = port 

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

        port = dictionary.get("port") if dictionary.get("port") else None
        node = dictionary.get("node") if dictionary.get("node") else APIHelper.SKIP
        # Return an object of this model
        return cls(port,
                   node)
