# -*- coding: utf-8 -*-

"""
mistapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from mistapi.api_helper import APIHelper
from mistapi.models.di_2 import DI2


class IotStat(object):

    """Implementation of the 'IotStat' model.

    TODO: type model description here.

    Attributes:
        di_2 (DI2): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "di_2": 'DI2'
    }

    _optionals = [
        'di_2',
    ]

    def __init__(self,
                 di_2=APIHelper.SKIP):
        """Constructor for the IotStat class"""

        # Initialize members of the class
        if di_2 is not APIHelper.SKIP:
            self.di_2 = di_2 

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

        di_2 = DI2.from_dictionary(dictionary.get('DI2')) if 'DI2' in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(di_2)