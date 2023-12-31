# -*- coding: utf-8 -*-

"""
mistapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class ApiV1SitesDevicesCableTestRequest(object):

    """Implementation of the 'Api V1 Sites Devices Cable Test Request' model.

    TODO: type model description here.

    Attributes:
        port (string): the port to run the cable test

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "port": 'port'
    }

    def __init__(self,
                 port=None):
        """Constructor for the ApiV1SitesDevicesCableTestRequest class"""

        # Initialize members of the class
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
        # Return an object of this model
        return cls(port)
