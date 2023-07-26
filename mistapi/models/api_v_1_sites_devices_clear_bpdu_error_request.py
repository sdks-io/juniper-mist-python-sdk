# -*- coding: utf-8 -*-

"""
mistapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from mistapi.api_helper import APIHelper


class ApiV1SitesDevicesClearBpduErrorRequest(object):

    """Implementation of the 'Api V1 Sites Devices Clear Bpdu Error Request' model.

    TODO: type model description here.

    Attributes:
        port (string): the port on which to clear the detected BPDU error, or
            `all` for all ports

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "port": 'port'
    }

    _optionals = [
        'port',
    ]

    def __init__(self,
                 port=APIHelper.SKIP):
        """Constructor for the ApiV1SitesDevicesClearBpduErrorRequest class"""

        # Initialize members of the class
        if port is not APIHelper.SKIP:
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

        port = dictionary.get("port") if dictionary.get("port") else APIHelper.SKIP
        # Return an object of this model
        return cls(port)