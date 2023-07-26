# -*- coding: utf-8 -*-

"""
mistapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class Device(object):

    """Implementation of the 'Device' model.

    TODO: type model description here.

    Attributes:
        device_id (uuid|string): TODO: type description here.
        rssi (int): RSSI threshold

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "device_id": 'device_id',
        "rssi": 'rssi'
    }

    def __init__(self,
                 device_id=None,
                 rssi=None):
        """Constructor for the Device class"""

        # Initialize members of the class
        self.device_id = device_id 
        self.rssi = rssi 

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

        device_id = dictionary.get("device_id") if dictionary.get("device_id") else None
        rssi = dictionary.get("rssi") if dictionary.get("rssi") else None
        # Return an object of this model
        return cls(device_id,
                   rssi)