# -*- coding: utf-8 -*-

"""
mistapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from mistapi.api_helper import APIHelper


class AutoSignatureUpdate(object):

    """Implementation of the 'AutoSignatureUpdate' model.

    TODO: type model description here.

    Attributes:
        day_of_week (string): optional, daily if omitted
        enable (bool): TODO: type description here.
        time_of_day (string): optional, Mist will decide the timing

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "day_of_week": 'day_of_week',
        "enable": 'enable',
        "time_of_day": 'time_of_day'
    }

    _optionals = [
        'day_of_week',
        'enable',
        'time_of_day',
    ]

    def __init__(self,
                 day_of_week=APIHelper.SKIP,
                 enable=True,
                 time_of_day=APIHelper.SKIP):
        """Constructor for the AutoSignatureUpdate class"""

        # Initialize members of the class
        if day_of_week is not APIHelper.SKIP:
            self.day_of_week = day_of_week 
        self.enable = enable 
        if time_of_day is not APIHelper.SKIP:
            self.time_of_day = time_of_day 

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

        day_of_week = dictionary.get("day_of_week") if dictionary.get("day_of_week") else APIHelper.SKIP
        enable = dictionary.get("enable") if dictionary.get("enable") else True
        time_of_day = dictionary.get("time_of_day") if dictionary.get("time_of_day") else APIHelper.SKIP
        # Return an object of this model
        return cls(day_of_week,
                   enable,
                   time_of_day)