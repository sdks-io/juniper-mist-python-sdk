# -*- coding: utf-8 -*-

"""
mistapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from mistapi.models.datum import Datum


class SleHistogram(object):

    """Implementation of the 'sle_histogram' model.

    TODO: type model description here.

    Attributes:
        data (list of Datum): TODO: type description here.
        end (float): TODO: type description here.
        metric (string): TODO: type description here.
        start (float): TODO: type description here.
        x_label (string): TODO: type description here.
        y_label (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "data": 'data',
        "end": 'end',
        "metric": 'metric',
        "start": 'start',
        "x_label": 'x_label',
        "y_label": 'y_label'
    }

    def __init__(self,
                 data=None,
                 end=None,
                 metric=None,
                 start=None,
                 x_label=None,
                 y_label=None):
        """Constructor for the SleHistogram class"""

        # Initialize members of the class
        self.data = data 
        self.end = end 
        self.metric = metric 
        self.start = start 
        self.x_label = x_label 
        self.y_label = y_label 

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

        data = None
        if dictionary.get('data') is not None:
            data = [Datum.from_dictionary(x) for x in dictionary.get('data')]
        end = dictionary.get("end") if dictionary.get("end") else None
        metric = dictionary.get("metric") if dictionary.get("metric") else None
        start = dictionary.get("start") if dictionary.get("start") else None
        x_label = dictionary.get("x_label") if dictionary.get("x_label") else None
        y_label = dictionary.get("y_label") if dictionary.get("y_label") else None
        # Return an object of this model
        return cls(data,
                   end,
                   metric,
                   start,
                   x_label,
                   y_label)
