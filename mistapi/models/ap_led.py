# -*- coding: utf-8 -*-

"""
mistapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from mistapi.api_helper import APIHelper


class ApLed(object):

    """Implementation of the 'ap_led' model.

    LED AP settings

    Attributes:
        brightness (int): TODO: type description here.
        enabled (bool): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "brightness": 'brightness',
        "enabled": 'enabled'
    }

    _optionals = [
        'brightness',
        'enabled',
    ]

    def __init__(self,
                 brightness=APIHelper.SKIP,
                 enabled=APIHelper.SKIP):
        """Constructor for the ApLed class"""

        # Initialize members of the class
        if brightness is not APIHelper.SKIP:
            self.brightness = brightness 
        if enabled is not APIHelper.SKIP:
            self.enabled = enabled 

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

        brightness = dictionary.get("brightness") if dictionary.get("brightness") else APIHelper.SKIP
        enabled = dictionary.get("enabled") if "enabled" in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(brightness,
                   enabled)