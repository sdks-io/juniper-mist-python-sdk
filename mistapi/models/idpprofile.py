# -*- coding: utf-8 -*-

"""
mistapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from mistapi.api_helper import APIHelper
from mistapi.models.overwrite import Overwrite


class Idpprofile(object):

    """Implementation of the 'idpprofile' model.

    TODO: type model description here.

    Attributes:
        base_profile (BaseProfileEnum): TODO: type description here.
        created_time (int): TODO: type description here.
        id (uuid|string): TODO: type description here.
        modified_time (int): TODO: type description here.
        name (string): TODO: type description here.
        overwrites (list of Overwrite): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "base_profile": 'base_profile',
        "created_time": 'created_time',
        "id": 'id',
        "modified_time": 'modified_time',
        "name": 'name',
        "overwrites": 'overwrites'
    }

    _optionals = [
        'base_profile',
        'created_time',
        'id',
        'modified_time',
        'name',
        'overwrites',
    ]

    def __init__(self,
                 base_profile=APIHelper.SKIP,
                 created_time=APIHelper.SKIP,
                 id=APIHelper.SKIP,
                 modified_time=APIHelper.SKIP,
                 name=APIHelper.SKIP,
                 overwrites=APIHelper.SKIP):
        """Constructor for the Idpprofile class"""

        # Initialize members of the class
        if base_profile is not APIHelper.SKIP:
            self.base_profile = base_profile 
        if created_time is not APIHelper.SKIP:
            self.created_time = created_time 
        if id is not APIHelper.SKIP:
            self.id = id 
        if modified_time is not APIHelper.SKIP:
            self.modified_time = modified_time 
        if name is not APIHelper.SKIP:
            self.name = name 
        if overwrites is not APIHelper.SKIP:
            self.overwrites = overwrites 

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

        base_profile = dictionary.get("base_profile") if dictionary.get("base_profile") else APIHelper.SKIP
        created_time = dictionary.get("created_time") if dictionary.get("created_time") else APIHelper.SKIP
        id = dictionary.get("id") if dictionary.get("id") else APIHelper.SKIP
        modified_time = dictionary.get("modified_time") if dictionary.get("modified_time") else APIHelper.SKIP
        name = dictionary.get("name") if dictionary.get("name") else APIHelper.SKIP
        overwrites = None
        if dictionary.get('overwrites') is not None:
            overwrites = [Overwrite.from_dictionary(x) for x in dictionary.get('overwrites')]
        else:
            overwrites = APIHelper.SKIP
        # Return an object of this model
        return cls(base_profile,
                   created_time,
                   id,
                   modified_time,
                   name,
                   overwrites)
