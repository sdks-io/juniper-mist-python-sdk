# -*- coding: utf-8 -*-

"""
mistapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from mistapi.api_helper import APIHelper


class PassphraseRules(object):

    """Implementation of the 'PassphraseRules' model.

    TODO: type model description here.

    Attributes:
        alphaberts_enabled (bool): TODO: type description here.
        length (int): TODO: type description here.
        max_length (int): for valid `max_length` and `min_length`, passphrase
            size is set randomly from that range. - if `max_length` and/or
            `min_length` are invalid, passphrase size is equal to `length`
            parameter - if `length` is not set or is invalid, default
            passphrase size is 8. valid `max_length`, `min_length`, `length`
            should be an integer between 8 to 63. Also, `max_length` >
            `min_length`
        min_length (int): for valid `max_length` and `min_length`, passphrase
            size is set randomly from that range. - if `max_length` and/or
            `min_length` are invalid, passphrase size is equal to `length`
            parameter - if `length` is not set or is invalid, default
            passphrase size is 8. valid `max_length`, `min_length`, `length`
            should be an integer between 8 to 63. Also, `max_length` >
            `min_length`
        numerics_enabled (bool): TODO: type description here.
        symbols (string): TODO: type description here.
        symbols_enabled (bool): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "alphaberts_enabled": 'alphaberts_enabled',
        "length": 'length',
        "max_length": 'max_length',
        "min_length": 'min_length',
        "numerics_enabled": 'numerics_enabled',
        "symbols": 'symbols',
        "symbols_enabled": 'symbols_enabled'
    }

    _optionals = [
        'alphaberts_enabled',
        'length',
        'max_length',
        'min_length',
        'numerics_enabled',
        'symbols',
        'symbols_enabled',
    ]

    def __init__(self,
                 alphaberts_enabled=True,
                 length=APIHelper.SKIP,
                 max_length=APIHelper.SKIP,
                 min_length=APIHelper.SKIP,
                 numerics_enabled=True,
                 symbols=APIHelper.SKIP,
                 symbols_enabled=True):
        """Constructor for the PassphraseRules class"""

        # Initialize members of the class
        self.alphaberts_enabled = alphaberts_enabled 
        if length is not APIHelper.SKIP:
            self.length = length 
        if max_length is not APIHelper.SKIP:
            self.max_length = max_length 
        if min_length is not APIHelper.SKIP:
            self.min_length = min_length 
        self.numerics_enabled = numerics_enabled 
        if symbols is not APIHelper.SKIP:
            self.symbols = symbols 
        self.symbols_enabled = symbols_enabled 

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

        alphaberts_enabled = dictionary.get("alphaberts_enabled") if dictionary.get("alphaberts_enabled") else True
        length = dictionary.get("length") if dictionary.get("length") else APIHelper.SKIP
        max_length = dictionary.get("max_length") if dictionary.get("max_length") else APIHelper.SKIP
        min_length = dictionary.get("min_length") if dictionary.get("min_length") else APIHelper.SKIP
        numerics_enabled = dictionary.get("numerics_enabled") if dictionary.get("numerics_enabled") else True
        symbols = dictionary.get("symbols") if dictionary.get("symbols") else APIHelper.SKIP
        symbols_enabled = dictionary.get("symbols_enabled") if dictionary.get("symbols_enabled") else True
        # Return an object of this model
        return cls(alphaberts_enabled,
                   length,
                   max_length,
                   min_length,
                   numerics_enabled,
                   symbols,
                   symbols_enabled)
