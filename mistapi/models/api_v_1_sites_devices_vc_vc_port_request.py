# -*- coding: utf-8 -*-

"""
mistapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from mistapi.models.member_2 import Member2


class ApiV1SitesDevicesVcVcPortRequest(object):

    """Implementation of the 'Api V1 Sites Devices Vc Vc Port Request' model.

    TODO: type model description here.

    Attributes:
        members (list of Member2): TODO: type description here.
        op (Op5Enum): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "members": 'members',
        "op": 'op'
    }

    def __init__(self,
                 members=None,
                 op=None):
        """Constructor for the ApiV1SitesDevicesVcVcPortRequest class"""

        # Initialize members of the class
        self.members = members 
        self.op = op 

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

        members = None
        if dictionary.get('members') is not None:
            members = [Member2.from_dictionary(x) for x in dictionary.get('members')]
        op = dictionary.get("op") if dictionary.get("op") else None
        # Return an object of this model
        return cls(members,
                   op)
