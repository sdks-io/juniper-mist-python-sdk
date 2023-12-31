# -*- coding: utf-8 -*-

"""
mistapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from mistapi.api_helper import APIHelper
from mistapi.models.result_8 import Result8


class ApiV1MspsSuggestionCountResponse(object):

    """Implementation of the 'Api V1 Msps Suggestion Count Response' model.

    TODO: type model description here.

    Attributes:
        distinct (string): TODO: type description here.
        limit (int): TODO: type description here.
        results (list of Result8): TODO: type description here.
        total (int): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "distinct": 'distinct',
        "limit": 'limit',
        "results": 'results',
        "total": 'total'
    }

    _optionals = [
        'distinct',
        'limit',
        'results',
        'total',
    ]

    def __init__(self,
                 distinct=APIHelper.SKIP,
                 limit=APIHelper.SKIP,
                 results=APIHelper.SKIP,
                 total=APIHelper.SKIP):
        """Constructor for the ApiV1MspsSuggestionCountResponse class"""

        # Initialize members of the class
        if distinct is not APIHelper.SKIP:
            self.distinct = distinct 
        if limit is not APIHelper.SKIP:
            self.limit = limit 
        if results is not APIHelper.SKIP:
            self.results = results 
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

        distinct = dictionary.get("distinct") if dictionary.get("distinct") else APIHelper.SKIP
        limit = dictionary.get("limit") if dictionary.get("limit") else APIHelper.SKIP
        results = None
        if dictionary.get('results') is not None:
            results = [Result8.from_dictionary(x) for x in dictionary.get('results')]
        else:
            results = APIHelper.SKIP
        total = dictionary.get("total") if dictionary.get("total") else APIHelper.SKIP
        # Return an object of this model
        return cls(distinct,
                   limit,
                   results,
                   total)
