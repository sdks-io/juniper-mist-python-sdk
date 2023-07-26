# -*- coding: utf-8 -*-

"""
mistapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from mistapi.api_helper import APIHelper


class ApiV1SitesMapsUseAutoApValuesRequest(object):

    """Implementation of the 'Api V1 Sites Maps Use Auto Ap Values Request' model.

    TODO: type model description here.

    Attributes:
        accept (bool): If accept is true, accepts placement for devices in
            list otherwise. If false, reject for devices in list.
        device_macs (list of string): A list of macs to accept/reject. If a
            list is not provided the API will accept/reject for the full map.
        mfor (ForEnum): The selector to choose auto placement or auto
            orientation.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "accept": 'accept',
        "device_macs": 'device_macs',
        "mfor": 'for'
    }

    _optionals = [
        'accept',
        'device_macs',
        'mfor',
    ]

    def __init__(self,
                 accept=False,
                 device_macs=APIHelper.SKIP,
                 mfor='placement'):
        """Constructor for the ApiV1SitesMapsUseAutoApValuesRequest class"""

        # Initialize members of the class
        self.accept = accept 
        if device_macs is not APIHelper.SKIP:
            self.device_macs = device_macs 
        self.mfor = mfor 

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

        accept = dictionary.get("accept") if dictionary.get("accept") else False
        device_macs = dictionary.get("device_macs") if dictionary.get("device_macs") else APIHelper.SKIP
        mfor = dictionary.get("for") if dictionary.get("for") else 'placement'
        # Return an object of this model
        return cls(accept,
                   device_macs,
                   mfor)