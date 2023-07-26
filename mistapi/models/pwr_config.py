# -*- coding: utf-8 -*-

"""
mistapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from mistapi.api_helper import APIHelper


class PwrConfig(object):

    """Implementation of the 'PwrConfig' model.

    power related configs

    Attributes:
        base (float): additional power to request during negotiating with PSE
            over PoE, in mW
        prefer_usb_over_wifi (bool): whether to enable power out to
            peripheral, meanwhile will reduce power to wifi (only for AP45 at
            power mode)

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "base": 'base',
        "prefer_usb_over_wifi": 'prefer_usb_over_wifi'
    }

    _optionals = [
        'base',
        'prefer_usb_over_wifi',
    ]

    def __init__(self,
                 base=0,
                 prefer_usb_over_wifi=False):
        """Constructor for the PwrConfig class"""

        # Initialize members of the class
        self.base = base 
        self.prefer_usb_over_wifi = prefer_usb_over_wifi 

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

        base = dictionary.get("base") if dictionary.get("base") else 0
        prefer_usb_over_wifi = dictionary.get("prefer_usb_over_wifi") if dictionary.get("prefer_usb_over_wifi") else False
        # Return an object of this model
        return cls(base,
                   prefer_usb_over_wifi)
