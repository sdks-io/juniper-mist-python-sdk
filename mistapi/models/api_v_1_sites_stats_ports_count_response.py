# -*- coding: utf-8 -*-

"""
mistapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from mistapi.models.result_27 import Result27


class ApiV1SitesStatsPortsCountResponse(object):

    """Implementation of the 'Api V1 Sites Stats Ports Count Response' model.

    TODO: type model description here.

    Attributes:
        distinct (string): TODO: type description here.
        end (int): TODO: type description here.
        limit (int): TODO: type description here.
        results (list of Result27): TODO: type description here.
        start (int): TODO: type description here.
        total (int): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "distinct": 'distinct',
        "end": 'end',
        "limit": 'limit',
        "results": 'results',
        "start": 'start',
        "total": 'total'
    }

    def __init__(self,
                 distinct=None,
                 end=None,
                 limit=None,
                 results=None,
                 start=None,
                 total=None):
        """Constructor for the ApiV1SitesStatsPortsCountResponse class"""

        # Initialize members of the class
        self.distinct = distinct 
        self.end = end 
        self.limit = limit 
        self.results = results 
        self.start = start 
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

        distinct = dictionary.get("distinct") if dictionary.get("distinct") else None
        end = dictionary.get("end") if dictionary.get("end") else None
        limit = dictionary.get("limit") if dictionary.get("limit") else None
        results = None
        if dictionary.get('results') is not None:
            results = [Result27.from_dictionary(x) for x in dictionary.get('results')]
        start = dictionary.get("start") if dictionary.get("start") else None
        total = dictionary.get("total") if dictionary.get("total") else None
        # Return an object of this model
        return cls(distinct,
                   end,
                   limit,
                   results,
                   start,
                   total)