# -*- coding: utf-8 -*-

"""
mistapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from mistapi.api_helper import APIHelper


class VcLink(object):

    """Implementation of the 'VcLink' model.

    TODO: type model description here.

    Attributes:
        neighbor_module_idx (int): TODO: type description here.
        neighbor_port_id (string): TODO: type description here.
        port_id (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "neighbor_module_idx": 'neighbor_module_idx',
        "neighbor_port_id": 'neighbor_port_id',
        "port_id": 'port_id'
    }

    _optionals = [
        'neighbor_module_idx',
        'neighbor_port_id',
        'port_id',
    ]

    def __init__(self,
                 neighbor_module_idx=APIHelper.SKIP,
                 neighbor_port_id=APIHelper.SKIP,
                 port_id=APIHelper.SKIP):
        """Constructor for the VcLink class"""

        # Initialize members of the class
        if neighbor_module_idx is not APIHelper.SKIP:
            self.neighbor_module_idx = neighbor_module_idx 
        if neighbor_port_id is not APIHelper.SKIP:
            self.neighbor_port_id = neighbor_port_id 
        if port_id is not APIHelper.SKIP:
            self.port_id = port_id 

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

        neighbor_module_idx = dictionary.get("neighbor_module_idx") if dictionary.get("neighbor_module_idx") else APIHelper.SKIP
        neighbor_port_id = dictionary.get("neighbor_port_id") if dictionary.get("neighbor_port_id") else APIHelper.SKIP
        port_id = dictionary.get("port_id") if dictionary.get("port_id") else APIHelper.SKIP
        # Return an object of this model
        return cls(neighbor_module_idx,
                   neighbor_port_id,
                   port_id)