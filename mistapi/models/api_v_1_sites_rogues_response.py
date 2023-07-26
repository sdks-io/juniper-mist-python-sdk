# -*- coding: utf-8 -*-

"""
mistapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class ApiV1SitesRoguesResponse(object):

    """Implementation of the 'Api V1 Sites Rogues Response' model.

    TODO: type model description here.

    Attributes:
        manufacture (string): TODO: type description here.
        seen_as_client (bool): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "manufacture": 'manufacture',
        "seen_as_client": 'seen_as_client'
    }

    def __init__(self,
                 manufacture=None,
                 seen_as_client=None):
        """Constructor for the ApiV1SitesRoguesResponse class"""

        # Initialize members of the class
        self.manufacture = manufacture 
        self.seen_as_client = seen_as_client 

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

        manufacture = dictionary.get("manufacture") if dictionary.get("manufacture") else None
        seen_as_client = dictionary.get("seen_as_client") if "seen_as_client" in dictionary.keys() else None
        # Return an object of this model
        return cls(manufacture,
                   seen_as_client)