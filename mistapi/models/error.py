# -*- coding: utf-8 -*-

"""
mistapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from mistapi.api_helper import APIHelper


class Error(object):

    """Implementation of the 'Error' model.

    TODO: type model description here.

    Attributes:
        feature (string): TODO: type description here.
        minimum_version (string): TODO: type description here.
        reason (string): TODO: type description here.
        since (int): TODO: type description here.
        mtype (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "since": 'since',
        "mtype": 'type',
        "feature": 'feature',
        "minimum_version": 'minimum_version',
        "reason": 'reason'
    }

    _optionals = [
        'feature',
        'minimum_version',
        'reason',
    ]

    def __init__(self,
                 since=None,
                 mtype=None,
                 feature=APIHelper.SKIP,
                 minimum_version=APIHelper.SKIP,
                 reason=APIHelper.SKIP):
        """Constructor for the Error class"""

        # Initialize members of the class
        if feature is not APIHelper.SKIP:
            self.feature = feature 
        if minimum_version is not APIHelper.SKIP:
            self.minimum_version = minimum_version 
        if reason is not APIHelper.SKIP:
            self.reason = reason 
        self.since = since 
        self.mtype = mtype 

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

        since = dictionary.get("since") if dictionary.get("since") else None
        mtype = dictionary.get("type") if dictionary.get("type") else None
        feature = dictionary.get("feature") if dictionary.get("feature") else APIHelper.SKIP
        minimum_version = dictionary.get("minimum_version") if dictionary.get("minimum_version") else APIHelper.SKIP
        reason = dictionary.get("reason") if dictionary.get("reason") else APIHelper.SKIP
        # Return an object of this model
        return cls(since,
                   mtype,
                   feature,
                   minimum_version,
                   reason)