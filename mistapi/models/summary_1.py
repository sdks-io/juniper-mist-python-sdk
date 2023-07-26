# -*- coding: utf-8 -*-

"""
mistapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from mistapi.api_helper import APIHelper


class Summary1(object):

    """Implementation of the 'Summary1' model.

    TODO: type model description here.

    Attributes:
        num_ap_assigned (float): TODO: type description here.
        num_inv_assigned (float): TODO: type description here.
        num_map_assigned (float): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "num_ap_assigned": 'num_ap_assigned',
        "num_inv_assigned": 'num_inv_assigned',
        "num_map_assigned": 'num_map_assigned'
    }

    _optionals = [
        'num_inv_assigned',
        'num_map_assigned',
    ]

    def __init__(self,
                 num_ap_assigned=None,
                 num_inv_assigned=APIHelper.SKIP,
                 num_map_assigned=APIHelper.SKIP):
        """Constructor for the Summary1 class"""

        # Initialize members of the class
        self.num_ap_assigned = num_ap_assigned 
        if num_inv_assigned is not APIHelper.SKIP:
            self.num_inv_assigned = num_inv_assigned 
        if num_map_assigned is not APIHelper.SKIP:
            self.num_map_assigned = num_map_assigned 

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

        num_ap_assigned = dictionary.get("num_ap_assigned") if dictionary.get("num_ap_assigned") else None
        num_inv_assigned = dictionary.get("num_inv_assigned") if dictionary.get("num_inv_assigned") else APIHelper.SKIP
        num_map_assigned = dictionary.get("num_map_assigned") if dictionary.get("num_map_assigned") else APIHelper.SKIP
        # Return an object of this model
        return cls(num_ap_assigned,
                   num_inv_assigned,
                   num_map_assigned)
