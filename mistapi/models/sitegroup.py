# -*- coding: utf-8 -*-

"""
mistapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from mistapi.api_helper import APIHelper


class Sitegroup(object):

    """Implementation of the 'sitegroup' model.

    Sites Group

    Attributes:
        created_time (float): TODO: type description here.
        id (uuid|string): TODO: type description here.
        modified_time (float): TODO: type description here.
        name (string): TODO: type description here.
        org_id (uuid|string): TODO: type description here.
        site_ids (list of uuid|string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "name": 'name',
        "created_time": 'created_time',
        "id": 'id',
        "modified_time": 'modified_time',
        "org_id": 'org_id',
        "site_ids": 'site_ids'
    }

    _optionals = [
        'created_time',
        'id',
        'modified_time',
        'org_id',
        'site_ids',
    ]

    def __init__(self,
                 name=None,
                 created_time=APIHelper.SKIP,
                 id=APIHelper.SKIP,
                 modified_time=APIHelper.SKIP,
                 org_id=APIHelper.SKIP,
                 site_ids=APIHelper.SKIP):
        """Constructor for the Sitegroup class"""

        # Initialize members of the class
        if created_time is not APIHelper.SKIP:
            self.created_time = created_time 
        if id is not APIHelper.SKIP:
            self.id = id 
        if modified_time is not APIHelper.SKIP:
            self.modified_time = modified_time 
        self.name = name 
        if org_id is not APIHelper.SKIP:
            self.org_id = org_id 
        if site_ids is not APIHelper.SKIP:
            self.site_ids = site_ids 

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

        name = dictionary.get("name") if dictionary.get("name") else None
        created_time = dictionary.get("created_time") if dictionary.get("created_time") else APIHelper.SKIP
        id = dictionary.get("id") if dictionary.get("id") else APIHelper.SKIP
        modified_time = dictionary.get("modified_time") if dictionary.get("modified_time") else APIHelper.SKIP
        org_id = dictionary.get("org_id") if dictionary.get("org_id") else APIHelper.SKIP
        site_ids = dictionary.get("site_ids") if dictionary.get("site_ids") else APIHelper.SKIP
        # Return an object of this model
        return cls(name,
                   created_time,
                   id,
                   modified_time,
                   org_id,
                   site_ids)
