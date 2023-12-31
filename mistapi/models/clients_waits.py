# -*- coding: utf-8 -*-

"""
mistapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from mistapi.api_helper import APIHelper


class ClientsWaits(object):

    """Implementation of the 'ClientsWaits' model.

    client wait time right now

    Attributes:
        avg (float): average wait time in seconds
        max (float): longest wait time in seconds
        min (float): shortest wait time in seconds
        p_95 (float): 95th percentile of all the wait time(s)

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "avg": 'avg',
        "max": 'max',
        "min": 'min',
        "p_95": 'p95'
    }

    _optionals = [
        'avg',
        'max',
        'min',
        'p_95',
    ]

    def __init__(self,
                 avg=APIHelper.SKIP,
                 max=APIHelper.SKIP,
                 min=APIHelper.SKIP,
                 p_95=APIHelper.SKIP):
        """Constructor for the ClientsWaits class"""

        # Initialize members of the class
        if avg is not APIHelper.SKIP:
            self.avg = avg 
        if max is not APIHelper.SKIP:
            self.max = max 
        if min is not APIHelper.SKIP:
            self.min = min 
        if p_95 is not APIHelper.SKIP:
            self.p_95 = p_95 

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

        avg = dictionary.get("avg") if dictionary.get("avg") else APIHelper.SKIP
        max = dictionary.get("max") if dictionary.get("max") else APIHelper.SKIP
        min = dictionary.get("min") if dictionary.get("min") else APIHelper.SKIP
        p_95 = dictionary.get("p95") if dictionary.get("p95") else APIHelper.SKIP
        # Return an object of this model
        return cls(avg,
                   max,
                   min,
                   p_95)
