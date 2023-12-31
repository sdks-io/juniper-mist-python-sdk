# -*- coding: utf-8 -*-

"""
mistapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from mistapi.api_helper import APIHelper


class BleConfig(object):

    """Implementation of the 'BleConfig' model.

    TODO: type model description here.

    Attributes:
        beacon_rate (int): TODO: type description here.
        beacon_rate_model (string): TODO: type description here.
        beam_disabled (list of int): TODO: type description here.
        power (int): TODO: type description here.
        power_mode (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "beacon_rate": 'beacon_rate',
        "beacon_rate_model": 'beacon_rate_model',
        "beam_disabled": 'beam_disabled',
        "power": 'power',
        "power_mode": 'power_mode'
    }

    _optionals = [
        'beacon_rate',
        'beacon_rate_model',
        'beam_disabled',
        'power',
        'power_mode',
    ]

    def __init__(self,
                 beacon_rate=APIHelper.SKIP,
                 beacon_rate_model=APIHelper.SKIP,
                 beam_disabled=APIHelper.SKIP,
                 power=APIHelper.SKIP,
                 power_mode=APIHelper.SKIP):
        """Constructor for the BleConfig class"""

        # Initialize members of the class
        if beacon_rate is not APIHelper.SKIP:
            self.beacon_rate = beacon_rate 
        if beacon_rate_model is not APIHelper.SKIP:
            self.beacon_rate_model = beacon_rate_model 
        if beam_disabled is not APIHelper.SKIP:
            self.beam_disabled = beam_disabled 
        if power is not APIHelper.SKIP:
            self.power = power 
        if power_mode is not APIHelper.SKIP:
            self.power_mode = power_mode 

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

        beacon_rate = dictionary.get("beacon_rate") if dictionary.get("beacon_rate") else APIHelper.SKIP
        beacon_rate_model = dictionary.get("beacon_rate_model") if dictionary.get("beacon_rate_model") else APIHelper.SKIP
        beam_disabled = dictionary.get("beam_disabled") if dictionary.get("beam_disabled") else APIHelper.SKIP
        power = dictionary.get("power") if dictionary.get("power") else APIHelper.SKIP
        power_mode = dictionary.get("power_mode") if dictionary.get("power_mode") else APIHelper.SKIP
        # Return an object of this model
        return cls(beacon_rate,
                   beacon_rate_model,
                   beam_disabled,
                   power,
                   power_mode)
