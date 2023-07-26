# -*- coding: utf-8 -*-

"""
mistapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class ApiV1SitesWxtagsClientsResponse(object):

    """Implementation of the 'Api V1 Sites Wxtags Clients Response' model.

    TODO: type model description here.

    Attributes:
        mac (string): TODO: type description here.
        since (float): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "mac": 'mac',
        "since": 'since'
    }

    def __init__(self,
                 mac=None,
                 since=None):
        """Constructor for the ApiV1SitesWxtagsClientsResponse class"""

        # Initialize members of the class
        self.mac = mac 
        self.since = since 

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

        mac = dictionary.get("mac") if dictionary.get("mac") else None
        since = dictionary.get("since") if dictionary.get("since") else None
        # Return an object of this model
        return cls(mac,
                   since)
