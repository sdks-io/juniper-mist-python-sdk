# -*- coding: utf-8 -*-

"""
mistapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from mistapi.api_helper import APIHelper


class Areas(object):

    """Implementation of the 'Areas' model.

    TODO: type model description here.

    Attributes:
        no_summary (bool): for a stub/nssa area, where to avoid forwarding
            type-3 LSA to this area

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "no_summary": 'no_summary'
    }

    _optionals = [
        'no_summary',
    ]

    def __init__(self,
                 no_summary=APIHelper.SKIP):
        """Constructor for the Areas class"""

        # Initialize members of the class
        if no_summary is not APIHelper.SKIP:
            self.no_summary = no_summary 

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

        no_summary = dictionary.get("no_summary") if "no_summary" in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(no_summary)
