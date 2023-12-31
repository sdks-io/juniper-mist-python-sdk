# -*- coding: utf-8 -*-

"""
mistapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from mistapi.models.stats_switch_port import StatsSwitchPort


class ApiV1SitesStatsPortsSearchResponse(object):

    """Implementation of the 'Api V1 Sites Stats Ports Search Response' model.

    TODO: type model description here.

    Attributes:
        end (int): TODO: type description here.
        limit (int): TODO: type description here.
        results (list of StatsSwitchPort): TODO: type description here.
        start (int): TODO: type description here.
        total (int): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "end": 'end',
        "limit": 'limit',
        "results": 'results',
        "start": 'start',
        "total": 'total'
    }

    def __init__(self,
                 end=None,
                 limit=None,
                 results=None,
                 start=None,
                 total=None):
        """Constructor for the ApiV1SitesStatsPortsSearchResponse class"""

        # Initialize members of the class
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

        end = dictionary.get("end") if dictionary.get("end") else None
        limit = dictionary.get("limit") if dictionary.get("limit") else None
        results = None
        if dictionary.get('results') is not None:
            results = [StatsSwitchPort.from_dictionary(x) for x in dictionary.get('results')]
        start = dictionary.get("start") if dictionary.get("start") else None
        total = dictionary.get("total") if dictionary.get("total") else None
        # Return an object of this model
        return cls(end,
                   limit,
                   results,
                   start,
                   total)
