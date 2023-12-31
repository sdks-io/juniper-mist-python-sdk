# -*- coding: utf-8 -*-

"""
mistapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from mistapi.api_helper import APIHelper


class Hours(object):

    """Implementation of the 'Hours' model.

    hours of operation filter, the available days (mon, tue, wed, thu, fri,
    sat, sun). 
    **Note**: If the dow is not defined then it’s treated as 00:00-23:59.

    Attributes:
        fri (string): TODO: type description here.
        mon (string): TODO: type description here.
        sta (string): TODO: type description here.
        sun (string): TODO: type description here.
        thu (string): TODO: type description here.
        tue (string): TODO: type description here.
        wed (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "fri": 'fri',
        "mon": 'mon',
        "sta": 'sta',
        "sun": 'sun',
        "thu": 'thu',
        "tue": 'tue',
        "wed": 'wed'
    }

    _optionals = [
        'fri',
        'mon',
        'sta',
        'sun',
        'thu',
        'tue',
        'wed',
    ]

    def __init__(self,
                 fri=APIHelper.SKIP,
                 mon=APIHelper.SKIP,
                 sta=APIHelper.SKIP,
                 sun=APIHelper.SKIP,
                 thu=APIHelper.SKIP,
                 tue=APIHelper.SKIP,
                 wed=APIHelper.SKIP):
        """Constructor for the Hours class"""

        # Initialize members of the class
        if fri is not APIHelper.SKIP:
            self.fri = fri 
        if mon is not APIHelper.SKIP:
            self.mon = mon 
        if sta is not APIHelper.SKIP:
            self.sta = sta 
        if sun is not APIHelper.SKIP:
            self.sun = sun 
        if thu is not APIHelper.SKIP:
            self.thu = thu 
        if tue is not APIHelper.SKIP:
            self.tue = tue 
        if wed is not APIHelper.SKIP:
            self.wed = wed 

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

        fri = dictionary.get("fri") if dictionary.get("fri") else APIHelper.SKIP
        mon = dictionary.get("mon") if dictionary.get("mon") else APIHelper.SKIP
        sta = dictionary.get("sta") if dictionary.get("sta") else APIHelper.SKIP
        sun = dictionary.get("sun") if dictionary.get("sun") else APIHelper.SKIP
        thu = dictionary.get("thu") if dictionary.get("thu") else APIHelper.SKIP
        tue = dictionary.get("tue") if dictionary.get("tue") else APIHelper.SKIP
        wed = dictionary.get("wed") if dictionary.get("wed") else APIHelper.SKIP
        # Return an object of this model
        return cls(fri,
                   mon,
                   sta,
                   sun,
                   thu,
                   tue,
                   wed)
