# -*- coding: utf-8 -*-

"""
mistapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from mistapi.api_helper import APIHelper
from mistapi.models.map_node import MapNode


class SitesurveyPath(object):

    """Implementation of the 'SitesurveyPath' model.

    TODO: type model description here.

    Attributes:
        coordinate (string): TODO: type description here.
        id (uuid|string): TODO: type description here.
        name (string): TODO: type description here.
        nodes (list of MapNode): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "coordinate": 'coordinate',
        "id": 'id',
        "name": 'name',
        "nodes": 'nodes'
    }

    _optionals = [
        'coordinate',
        'id',
        'name',
        'nodes',
    ]

    def __init__(self,
                 coordinate=APIHelper.SKIP,
                 id=APIHelper.SKIP,
                 name=APIHelper.SKIP,
                 nodes=APIHelper.SKIP):
        """Constructor for the SitesurveyPath class"""

        # Initialize members of the class
        if coordinate is not APIHelper.SKIP:
            self.coordinate = coordinate 
        if id is not APIHelper.SKIP:
            self.id = id 
        if name is not APIHelper.SKIP:
            self.name = name 
        if nodes is not APIHelper.SKIP:
            self.nodes = nodes 

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

        coordinate = dictionary.get("coordinate") if dictionary.get("coordinate") else APIHelper.SKIP
        id = dictionary.get("id") if dictionary.get("id") else APIHelper.SKIP
        name = dictionary.get("name") if dictionary.get("name") else APIHelper.SKIP
        nodes = None
        if dictionary.get('nodes') is not None:
            nodes = [MapNode.from_dictionary(x) for x in dictionary.get('nodes')]
        else:
            nodes = APIHelper.SKIP
        # Return an object of this model
        return cls(coordinate,
                   id,
                   name,
                   nodes)
