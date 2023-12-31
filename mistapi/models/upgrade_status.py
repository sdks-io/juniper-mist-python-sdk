# -*- coding: utf-8 -*-

"""
mistapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class UpgradeStatus(object):

    """Implementation of the 'UpgradeStatus' model.

    TODO: type model description here.

    Attributes:
        status (Status7Enum): TODO: type description here.
        status_id (int): the internal status id
        timestamp (float): timestamp

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "status": 'status',
        "status_id": 'status_id',
        "timestamp": 'timestamp'
    }

    def __init__(self,
                 status=None,
                 status_id=None,
                 timestamp=None):
        """Constructor for the UpgradeStatus class"""

        # Initialize members of the class
        self.status = status 
        self.status_id = status_id 
        self.timestamp = timestamp 

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

        status = dictionary.get("status") if dictionary.get("status") else None
        status_id = dictionary.get("status_id") if dictionary.get("status_id") else None
        timestamp = dictionary.get("timestamp") if dictionary.get("timestamp") else None
        # Return an object of this model
        return cls(status,
                   status_id,
                   timestamp)
