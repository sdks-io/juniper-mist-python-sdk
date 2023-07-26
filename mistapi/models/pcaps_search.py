# -*- coding: utf-8 -*-

"""
mistapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from mistapi.api_helper import APIHelper
from mistapi.models.result_21 import Result21


class PcapsSearch(object):

    """Implementation of the 'PcapsSearch' model.

    TODO: type model description here.

    Attributes:
        end (int): TODO: type description here.
        limit (int): TODO: type description here.
        next (string): TODO: type description here.
        results (list of Result21): TODO: type description here.
        start (int): TODO: type description here.
        total (int): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "end": 'end',
        "limit": 'limit',
        "next": 'next',
        "results": 'results',
        "start": 'start',
        "total": 'total'
    }

    _optionals = [
        'total',
    ]

    def __init__(self,
                 end=None,
                 limit=None,
                 next=None,
                 results=None,
                 start=None,
                 total=APIHelper.SKIP):
        """Constructor for the PcapsSearch class"""

        # Initialize members of the class
        self.end = end 
        self.limit = limit 
        self.next = next 
        self.results = results 
        self.start = start 
        if total is not APIHelper.SKIP:
            self.total = total 

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

        end = dictionary.get("end") if dictionary.get("end") else None
        limit = dictionary.get("limit") if dictionary.get("limit") else None
        next = dictionary.get("next") if dictionary.get("next") else None
        results = None
        if dictionary.get('results') is not None:
            results = [Result21.from_dictionary(x) for x in dictionary.get('results')]
        start = dictionary.get("start") if dictionary.get("start") else None
        total = dictionary.get("total") if dictionary.get("total") else APIHelper.SKIP
        # Return an object of this model
        return cls(end,
                   limit,
                   next,
                   results,
                   start,
                   total)
