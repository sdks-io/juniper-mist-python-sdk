# -*- coding: utf-8 -*-

"""
mistapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from mistapi.api_helper import APIHelper


class Session(object):

    """Implementation of the 'Session' model.

    TODO: type model description here.

    Attributes:
        local_sid (int): remote sessions id (dynamically unless Tunnel is said
            to be static)
        remote_id (string): WxlanTunnel Remote ID (user-configured)
        remote_sid (int): remote sessions id (dynamically unless Tunnel is
            said to be static)
        state (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "local_sid": 'local_sid',
        "remote_id": 'remote_id',
        "remote_sid": 'remote_sid',
        "state": 'state'
    }

    _optionals = [
        'local_sid',
        'remote_id',
        'remote_sid',
        'state',
    ]

    def __init__(self,
                 local_sid=APIHelper.SKIP,
                 remote_id=APIHelper.SKIP,
                 remote_sid=APIHelper.SKIP,
                 state=APIHelper.SKIP):
        """Constructor for the Session class"""

        # Initialize members of the class
        if local_sid is not APIHelper.SKIP:
            self.local_sid = local_sid 
        if remote_id is not APIHelper.SKIP:
            self.remote_id = remote_id 
        if remote_sid is not APIHelper.SKIP:
            self.remote_sid = remote_sid 
        if state is not APIHelper.SKIP:
            self.state = state 

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

        local_sid = dictionary.get("local_sid") if dictionary.get("local_sid") else APIHelper.SKIP
        remote_id = dictionary.get("remote_id") if dictionary.get("remote_id") else APIHelper.SKIP
        remote_sid = dictionary.get("remote_sid") if dictionary.get("remote_sid") else APIHelper.SKIP
        state = dictionary.get("state") if dictionary.get("state") else APIHelper.SKIP
        # Return an object of this model
        return cls(local_sid,
                   remote_id,
                   remote_sid,
                   state)
