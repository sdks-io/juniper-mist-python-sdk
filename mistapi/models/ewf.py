# -*- coding: utf-8 -*-

"""
mistapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from mistapi.api_helper import APIHelper


class Ewf(object):

    """Implementation of the 'Ewf' model.

    TODO: type model description here.

    Attributes:
        alert_only (bool): TODO: type description here.
        block_message (string): TODO: type description here.
        enabled (bool): TODO: type description here.
        profille (ProfilleEnum): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "alert_only": 'alert_only',
        "block_message": 'block_message',
        "enabled": 'enabled',
        "profille": 'profille'
    }

    _optionals = [
        'alert_only',
        'block_message',
        'enabled',
        'profille',
    ]

    def __init__(self,
                 alert_only=APIHelper.SKIP,
                 block_message=APIHelper.SKIP,
                 enabled=False,
                 profille='strict'):
        """Constructor for the Ewf class"""

        # Initialize members of the class
        if alert_only is not APIHelper.SKIP:
            self.alert_only = alert_only 
        if block_message is not APIHelper.SKIP:
            self.block_message = block_message 
        self.enabled = enabled 
        self.profille = profille 

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

        alert_only = dictionary.get("alert_only") if "alert_only" in dictionary.keys() else APIHelper.SKIP
        block_message = dictionary.get("block_message") if dictionary.get("block_message") else APIHelper.SKIP
        enabled = dictionary.get("enabled") if dictionary.get("enabled") else False
        profille = dictionary.get("profille") if dictionary.get("profille") else 'strict'
        # Return an object of this model
        return cls(alert_only,
                   block_message,
                   enabled,
                   profille)