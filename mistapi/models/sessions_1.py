# -*- coding: utf-8 -*-

"""
mistapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class Sessions1(object):

    """Implementation of the 'Sessions1' model.

    TODO: type model description here.

    Attributes:
        local_sid (int): remote sessions id (dynamically unless Tunnel is said
            to be static)
        remote_id (string): WxlanTunnel Remote ID
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

    def __init__(self,
                 local_sid=None,
                 remote_id=None,
                 remote_sid=None,
                 state=None):
        """Constructor for the Sessions1 class"""

        # Initialize members of the class
        self.local_sid = local_sid 
        self.remote_id = remote_id 
        self.remote_sid = remote_sid 
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

        local_sid = dictionary.get("local_sid") if dictionary.get("local_sid") else None
        remote_id = dictionary.get("remote_id") if dictionary.get("remote_id") else None
        remote_sid = dictionary.get("remote_sid") if dictionary.get("remote_sid") else None
        state = dictionary.get("state") if dictionary.get("state") else None
        # Return an object of this model
        return cls(local_sid,
                   remote_id,
                   remote_sid,
                   state)
