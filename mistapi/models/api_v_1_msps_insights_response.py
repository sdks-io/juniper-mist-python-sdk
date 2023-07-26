# -*- coding: utf-8 -*-

"""
mistapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class ApiV1MspsInsightsResponse(object):

    """Implementation of the 'Api V1 Msps Insights Response' model.

    TODO: type model description here.

    Attributes:
        end (float): TODO: type description here.
        interval (float): TODO: type description here.
        limit (float): TODO: type description here.
        results (list of object): TODO: type description here.
        start (float): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "end": 'end',
        "interval": 'interval',
        "limit": 'limit',
        "results": 'results',
        "start": 'start'
    }

    def __init__(self,
                 end=None,
                 interval=None,
                 limit=None,
                 results=None,
                 start=None):
        """Constructor for the ApiV1MspsInsightsResponse class"""

        # Initialize members of the class
        self.end = end 
        self.interval = interval 
        self.limit = limit 
        self.results = results 
        self.start = start 

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
        interval = dictionary.get("interval") if dictionary.get("interval") else None
        limit = dictionary.get("limit") if dictionary.get("limit") else None
        results = dictionary.get("results") if dictionary.get("results") else None
        start = dictionary.get("start") if dictionary.get("start") else None
        # Return an object of this model
        return cls(end,
                   interval,
                   limit,
                   results,
                   start)