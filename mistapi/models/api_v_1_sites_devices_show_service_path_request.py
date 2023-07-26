# -*- coding: utf-8 -*-

"""
mistapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from mistapi.api_helper import APIHelper


class ApiV1SitesDevicesShowServicePathRequest(object):

    """Implementation of the 'Api V1 Sites Devices Show Service Path Request' model.

    The exact service name for which to display the service path

    Attributes:
        node (NodeEnum): only for HA
        service_name (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "node": 'node',
        "service_name": 'service_name'
    }

    _optionals = [
        'node',
        'service_name',
    ]

    def __init__(self,
                 node=APIHelper.SKIP,
                 service_name=APIHelper.SKIP):
        """Constructor for the ApiV1SitesDevicesShowServicePathRequest class"""

        # Initialize members of the class
        if node is not APIHelper.SKIP:
            self.node = node 
        if service_name is not APIHelper.SKIP:
            self.service_name = service_name 

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

        node = dictionary.get("node") if dictionary.get("node") else APIHelper.SKIP
        service_name = dictionary.get("service_name") if dictionary.get("service_name") else APIHelper.SKIP
        # Return an object of this model
        return cls(node,
                   service_name)