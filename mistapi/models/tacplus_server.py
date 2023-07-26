# -*- coding: utf-8 -*-

"""
mistapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from mistapi.api_helper import APIHelper


class TacplusServer(object):

    """Implementation of the 'TacplusServer' model.

    TODO: type model description here.

    Attributes:
        host (string): TODO: type description here.
        port (string): TODO: type description here.
        secret (string): TODO: type description here.
        timeout (int): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "host": 'host',
        "port": 'port',
        "secret": 'secret',
        "timeout": 'timeout'
    }

    _optionals = [
        'host',
        'port',
        'secret',
        'timeout',
    ]

    def __init__(self,
                 host=APIHelper.SKIP,
                 port=APIHelper.SKIP,
                 secret=APIHelper.SKIP,
                 timeout=10):
        """Constructor for the TacplusServer class"""

        # Initialize members of the class
        if host is not APIHelper.SKIP:
            self.host = host 
        if port is not APIHelper.SKIP:
            self.port = port 
        if secret is not APIHelper.SKIP:
            self.secret = secret 
        self.timeout = timeout 

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

        host = dictionary.get("host") if dictionary.get("host") else APIHelper.SKIP
        port = dictionary.get("port") if dictionary.get("port") else APIHelper.SKIP
        secret = dictionary.get("secret") if dictionary.get("secret") else APIHelper.SKIP
        timeout = dictionary.get("timeout") if dictionary.get("timeout") else 10
        # Return an object of this model
        return cls(host,
                   port,
                   secret,
                   timeout)