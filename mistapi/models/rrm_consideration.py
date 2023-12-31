# -*- coding: utf-8 -*-

"""
mistapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from mistapi.models.result_22 import Result22


class RrmConsideration(object):

    """Implementation of the 'RrmConsideration' model.

    TODO: type model description here.

    Attributes:
        results (list of Result22): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "results": 'results'
    }

    def __init__(self,
                 results=None):
        """Constructor for the RrmConsideration class"""

        # Initialize members of the class
        self.results = results 

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

        results = None
        if dictionary.get('results') is not None:
            results = [Result22.from_dictionary(x) for x in dictionary.get('results')]
        # Return an object of this model
        return cls(results)
