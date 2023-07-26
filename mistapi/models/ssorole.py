# -*- coding: utf-8 -*-

"""
mistapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from mistapi.api_helper import APIHelper
from mistapi.models.privileges import Privileges


class Ssorole(object):

    """Implementation of the 'ssorole' model.

    SSO Role response

    Attributes:
        created_time (float): TODO: type description here.
        for_site (bool): TODO: type description here.
        id (uuid|string): TODO: type description here.
        modified_time (float): TODO: type description here.
        msp_id (uuid|string): TODO: type description here.
        name (string): TODO: type description here.
        org_id (uuid|string): TODO: type description here.
        privileges (list of Privileges): TODO: type description here.
        site_id (uuid|string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "name": 'name',
        "privileges": 'privileges',
        "created_time": 'created_time',
        "for_site": 'for_site',
        "id": 'id',
        "modified_time": 'modified_time',
        "msp_id": 'msp_id',
        "org_id": 'org_id',
        "site_id": 'site_id'
    }

    _optionals = [
        'created_time',
        'for_site',
        'id',
        'modified_time',
        'msp_id',
        'org_id',
        'site_id',
    ]

    def __init__(self,
                 name=None,
                 privileges=None,
                 created_time=APIHelper.SKIP,
                 for_site=APIHelper.SKIP,
                 id=APIHelper.SKIP,
                 modified_time=APIHelper.SKIP,
                 msp_id=APIHelper.SKIP,
                 org_id=APIHelper.SKIP,
                 site_id=APIHelper.SKIP):
        """Constructor for the Ssorole class"""

        # Initialize members of the class
        if created_time is not APIHelper.SKIP:
            self.created_time = created_time 
        if for_site is not APIHelper.SKIP:
            self.for_site = for_site 
        if id is not APIHelper.SKIP:
            self.id = id 
        if modified_time is not APIHelper.SKIP:
            self.modified_time = modified_time 
        if msp_id is not APIHelper.SKIP:
            self.msp_id = msp_id 
        self.name = name 
        if org_id is not APIHelper.SKIP:
            self.org_id = org_id 
        self.privileges = privileges 
        if site_id is not APIHelper.SKIP:
            self.site_id = site_id 

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
        privileges = None
        if dictionary.get('privileges') is not None:
            privileges = [Privileges.from_dictionary(x) for x in dictionary.get('privileges')]
        created_time = dictionary.get("created_time") if dictionary.get("created_time") else APIHelper.SKIP
        for_site = dictionary.get("for_site") if "for_site" in dictionary.keys() else APIHelper.SKIP
        id = dictionary.get("id") if dictionary.get("id") else APIHelper.SKIP
        modified_time = dictionary.get("modified_time") if dictionary.get("modified_time") else APIHelper.SKIP
        msp_id = dictionary.get("msp_id") if dictionary.get("msp_id") else APIHelper.SKIP
        org_id = dictionary.get("org_id") if dictionary.get("org_id") else APIHelper.SKIP
        site_id = dictionary.get("site_id") if dictionary.get("site_id") else APIHelper.SKIP
        # Return an object of this model
        return cls(name,
                   privileges,
                   created_time,
                   for_site,
                   id,
                   modified_time,
                   msp_id,
                   org_id,
                   site_id)
