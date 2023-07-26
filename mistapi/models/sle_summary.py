# -*- coding: utf-8 -*-

"""
mistapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from mistapi.models.classifier_1 import Classifier1
from mistapi.models.impact_1 import Impact1
from mistapi.models.sle import Sle


class SleSummary(object):

    """Implementation of the 'sle_summary' model.

    TODO: type model description here.

    Attributes:
        classifiers (list of Classifier1): TODO: type description here.
        end (float): TODO: type description here.
        events (list of object): TODO: type description here.
        impact (Impact1): TODO: type description here.
        sle (Sle): TODO: type description here.
        start (float): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "classifiers": 'classifiers',
        "end": 'end',
        "events": 'events',
        "impact": 'impact',
        "sle": 'sle',
        "start": 'start'
    }

    def __init__(self,
                 classifiers=None,
                 end=None,
                 events=None,
                 impact=None,
                 sle=None,
                 start=None):
        """Constructor for the SleSummary class"""

        # Initialize members of the class
        self.classifiers = classifiers 
        self.end = end 
        self.events = events 
        self.impact = impact 
        self.sle = sle 
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

        classifiers = None
        if dictionary.get('classifiers') is not None:
            classifiers = [Classifier1.from_dictionary(x) for x in dictionary.get('classifiers')]
        end = dictionary.get("end") if dictionary.get("end") else None
        events = dictionary.get("events") if dictionary.get("events") else None
        impact = Impact1.from_dictionary(dictionary.get('impact')) if dictionary.get('impact') else None
        sle = Sle.from_dictionary(dictionary.get('sle')) if dictionary.get('sle') else None
        start = dictionary.get("start") if dictionary.get("start") else None
        # Return an object of this model
        return cls(classifiers,
                   end,
                   events,
                   impact,
                   sle,
                   start)