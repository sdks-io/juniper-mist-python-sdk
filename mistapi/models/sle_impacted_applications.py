# -*- coding: utf-8 -*-

"""
mistapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from mistapi.api_helper import APIHelper
from mistapi.models.apps_1 import Apps1


class SleImpactedApplications(object):

    """Implementation of the 'sle_impacted_applications' model.

    TODO: type model description here.

    Attributes:
        apps (list of Apps1): TODO: type description here.
        classifier (string): TODO: type description here.
        end (int): TODO: type description here.
        failure (string): TODO: type description here.
        limit (string): TODO: type description here.
        metric (string): TODO: type description here.
        page (int): TODO: type description here.
        start (int): TODO: type description here.
        total_count (int): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "apps": 'apps',
        "classifier": 'classifier',
        "end": 'end',
        "failure": 'failure',
        "limit": 'limit',
        "metric": 'metric',
        "page": 'page',
        "start": 'start',
        "total_count": 'total_count'
    }

    _optionals = [
        'apps',
        'classifier',
        'end',
        'failure',
        'limit',
        'metric',
        'page',
        'start',
        'total_count',
    ]

    def __init__(self,
                 apps=APIHelper.SKIP,
                 classifier=APIHelper.SKIP,
                 end=APIHelper.SKIP,
                 failure=APIHelper.SKIP,
                 limit=APIHelper.SKIP,
                 metric=APIHelper.SKIP,
                 page=APIHelper.SKIP,
                 start=APIHelper.SKIP,
                 total_count=APIHelper.SKIP):
        """Constructor for the SleImpactedApplications class"""

        # Initialize members of the class
        if apps is not APIHelper.SKIP:
            self.apps = apps 
        if classifier is not APIHelper.SKIP:
            self.classifier = classifier 
        if end is not APIHelper.SKIP:
            self.end = end 
        if failure is not APIHelper.SKIP:
            self.failure = failure 
        if limit is not APIHelper.SKIP:
            self.limit = limit 
        if metric is not APIHelper.SKIP:
            self.metric = metric 
        if page is not APIHelper.SKIP:
            self.page = page 
        if start is not APIHelper.SKIP:
            self.start = start 
        if total_count is not APIHelper.SKIP:
            self.total_count = total_count 

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

        apps = None
        if dictionary.get('apps') is not None:
            apps = [Apps1.from_dictionary(x) for x in dictionary.get('apps')]
        else:
            apps = APIHelper.SKIP
        classifier = dictionary.get("classifier") if dictionary.get("classifier") else APIHelper.SKIP
        end = dictionary.get("end") if dictionary.get("end") else APIHelper.SKIP
        failure = dictionary.get("failure") if dictionary.get("failure") else APIHelper.SKIP
        limit = dictionary.get("limit") if dictionary.get("limit") else APIHelper.SKIP
        metric = dictionary.get("metric") if dictionary.get("metric") else APIHelper.SKIP
        page = dictionary.get("page") if dictionary.get("page") else APIHelper.SKIP
        start = dictionary.get("start") if dictionary.get("start") else APIHelper.SKIP
        total_count = dictionary.get("total_count") if dictionary.get("total_count") else APIHelper.SKIP
        # Return an object of this model
        return cls(apps,
                   classifier,
                   end,
                   failure,
                   limit,
                   metric,
                   page,
                   start,
                   total_count)
