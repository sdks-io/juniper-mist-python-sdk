# -*- coding: utf-8 -*-

"""
mistapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from mistapi.api_helper import APIHelper


class ArpFailure(object):

    """Implementation of the 'ArpFailure' model.

    TODO: type model description here.

    Attributes:
        client_count (int): TODO: type description here.
        duration (int): failing within minutes
        incident_count (int): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "client_count": 'client_count',
        "duration": 'duration',
        "incident_count": 'incident_count'
    }

    _optionals = [
        'client_count',
        'duration',
        'incident_count',
    ]

    def __init__(self,
                 client_count=10,
                 duration=20,
                 incident_count=10):
        """Constructor for the ArpFailure class"""

        # Initialize members of the class
        self.client_count = client_count 
        self.duration = duration 
        self.incident_count = incident_count 

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

        client_count = dictionary.get("client_count") if dictionary.get("client_count") else 10
        duration = dictionary.get("duration") if dictionary.get("duration") else 20
        incident_count = dictionary.get("incident_count") if dictionary.get("incident_count") else 10
        # Return an object of this model
        return cls(client_count,
                   duration,
                   incident_count)
