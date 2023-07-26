# -*- coding: utf-8 -*-

"""
mistapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class DeviceO(object):

    """Implementation of the 'DeviceO' model.

    TODO: type model description here.

    Attributes:
        degraded (float): TODO: type description here.
        device_os (string): TODO: type description here.
        duration (float): TODO: type description here.
        name (string): TODO: type description here.
        total (float): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "degraded": 'degraded',
        "device_os": 'device_os',
        "duration": 'duration',
        "name": 'name',
        "total": 'total'
    }

    def __init__(self,
                 degraded=None,
                 device_os=None,
                 duration=None,
                 name=None,
                 total=None):
        """Constructor for the DeviceO class"""

        # Initialize members of the class
        self.degraded = degraded 
        self.device_os = device_os 
        self.duration = duration 
        self.name = name 
        self.total = total 

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

        degraded = dictionary.get("degraded") if dictionary.get("degraded") else None
        device_os = dictionary.get("device_os") if dictionary.get("device_os") else None
        duration = dictionary.get("duration") if dictionary.get("duration") else None
        name = dictionary.get("name") if dictionary.get("name") else None
        total = dictionary.get("total") if dictionary.get("total") else None
        # Return an object of this model
        return cls(degraded,
                   device_os,
                   duration,
                   name,
                   total)