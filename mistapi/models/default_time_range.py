# -*- coding: utf-8 -*-

"""
mistapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from mistapi.api_helper import APIHelper


class DefaultTimeRange(object):

    """Implementation of the 'DefaultTimeRange' model.

    TODO: type model description here.

    Attributes:
        end (int): TODO: type description here.
        end_date (string): TODO: type description here.
        interval (string): TODO: type description here.
        name (string): TODO: type description here.
        short_name (string): TODO: type description here.
        start (int): TODO: type description here.
        use_preset (bool): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "end": 'end',
        "end_date": 'endDate',
        "interval": 'interval',
        "name": 'name',
        "short_name": 'shortName',
        "start": 'start',
        "use_preset": 'usePreset'
    }

    _optionals = [
        'end',
        'end_date',
        'interval',
        'name',
        'short_name',
        'start',
        'use_preset',
    ]

    def __init__(self,
                 end=APIHelper.SKIP,
                 end_date=APIHelper.SKIP,
                 interval=APIHelper.SKIP,
                 name=APIHelper.SKIP,
                 short_name=APIHelper.SKIP,
                 start=APIHelper.SKIP,
                 use_preset=APIHelper.SKIP):
        """Constructor for the DefaultTimeRange class"""

        # Initialize members of the class
        if end is not APIHelper.SKIP:
            self.end = end 
        if end_date is not APIHelper.SKIP:
            self.end_date = end_date 
        if interval is not APIHelper.SKIP:
            self.interval = interval 
        if name is not APIHelper.SKIP:
            self.name = name 
        if short_name is not APIHelper.SKIP:
            self.short_name = short_name 
        if start is not APIHelper.SKIP:
            self.start = start 
        if use_preset is not APIHelper.SKIP:
            self.use_preset = use_preset 

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

        end = dictionary.get("end") if dictionary.get("end") else APIHelper.SKIP
        end_date = dictionary.get("endDate") if dictionary.get("endDate") else APIHelper.SKIP
        interval = dictionary.get("interval") if dictionary.get("interval") else APIHelper.SKIP
        name = dictionary.get("name") if dictionary.get("name") else APIHelper.SKIP
        short_name = dictionary.get("shortName") if dictionary.get("shortName") else APIHelper.SKIP
        start = dictionary.get("start") if dictionary.get("start") else APIHelper.SKIP
        use_preset = dictionary.get("usePreset") if "usePreset" in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(end,
                   end_date,
                   interval,
                   name,
                   short_name,
                   start,
                   use_preset)
