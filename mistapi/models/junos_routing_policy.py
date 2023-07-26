# -*- coding: utf-8 -*-

"""
mistapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from mistapi.api_helper import APIHelper
from mistapi.models.term import Term


class JunosRoutingPolicy(object):

    """Implementation of the 'junos_routing_policy' model.

    TODO: type model description here.

    Attributes:
        terms (list of Term): zero or more criteria/filter can be specified to
            match the term, all criteria have to be met

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "terms": 'terms'
    }

    _optionals = [
        'terms',
    ]

    def __init__(self,
                 terms=APIHelper.SKIP):
        """Constructor for the JunosRoutingPolicy class"""

        # Initialize members of the class
        if terms is not APIHelper.SKIP:
            self.terms = terms 

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

        terms = None
        if dictionary.get('terms') is not None:
            terms = [Term.from_dictionary(x) for x in dictionary.get('terms')]
        else:
            terms = APIHelper.SKIP
        # Return an object of this model
        return cls(terms)
