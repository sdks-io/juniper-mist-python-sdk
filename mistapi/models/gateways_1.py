# -*- coding: utf-8 -*-

"""
mistapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from mistapi.api_helper import APIHelper


class Gateways1(object):

    """Implementation of the 'Gateways1' model.

    TODO: type model description here.

    Attributes:
        degraded (float): TODO: type description here.
        duration (int): TODO: type description here.
        gateway_mac (string): TODO: type description here.
        gateway_model (string): TODO: type description here.
        gateway_version (string): TODO: type description here.
        name (string): TODO: type description here.
        total (int): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "degraded": 'degraded',
        "duration": 'duration',
        "gateway_mac": 'gateway_mac',
        "gateway_model": 'gateway_model',
        "gateway_version": 'gateway_version',
        "name": 'name',
        "total": 'total'
    }

    _optionals = [
        'degraded',
        'duration',
        'gateway_mac',
        'gateway_model',
        'gateway_version',
        'name',
        'total',
    ]

    def __init__(self,
                 degraded=APIHelper.SKIP,
                 duration=APIHelper.SKIP,
                 gateway_mac=APIHelper.SKIP,
                 gateway_model=APIHelper.SKIP,
                 gateway_version=APIHelper.SKIP,
                 name=APIHelper.SKIP,
                 total=APIHelper.SKIP):
        """Constructor for the Gateways1 class"""

        # Initialize members of the class
        if degraded is not APIHelper.SKIP:
            self.degraded = degraded 
        if duration is not APIHelper.SKIP:
            self.duration = duration 
        if gateway_mac is not APIHelper.SKIP:
            self.gateway_mac = gateway_mac 
        if gateway_model is not APIHelper.SKIP:
            self.gateway_model = gateway_model 
        if gateway_version is not APIHelper.SKIP:
            self.gateway_version = gateway_version 
        if name is not APIHelper.SKIP:
            self.name = name 
        if total is not APIHelper.SKIP:
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

        degraded = dictionary.get("degraded") if dictionary.get("degraded") else APIHelper.SKIP
        duration = dictionary.get("duration") if dictionary.get("duration") else APIHelper.SKIP
        gateway_mac = dictionary.get("gateway_mac") if dictionary.get("gateway_mac") else APIHelper.SKIP
        gateway_model = dictionary.get("gateway_model") if dictionary.get("gateway_model") else APIHelper.SKIP
        gateway_version = dictionary.get("gateway_version") if dictionary.get("gateway_version") else APIHelper.SKIP
        name = dictionary.get("name") if dictionary.get("name") else APIHelper.SKIP
        total = dictionary.get("total") if dictionary.get("total") else APIHelper.SKIP
        # Return an object of this model
        return cls(degraded,
                   duration,
                   gateway_mac,
                   gateway_model,
                   gateway_version,
                   name,
                   total)
