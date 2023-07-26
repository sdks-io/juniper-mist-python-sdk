# -*- coding: utf-8 -*-

"""
mistapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from mistapi.api_helper import APIHelper


class ApiV1MspsInventoryResponse(object):

    """Implementation of the 'Api V1 Msps Inventory Response' model.

    TODO: type model description here.

    Attributes:
        for_site (bool): TODO: type description here.
        mac (string): TODO: type description here.
        model (string): TODO: type description here.
        org_id (uuid|string): TODO: type description here.
        serial (string): TODO: type description here.
        site_id (uuid|string): TODO: type description here.
        mtype (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "mac": 'mac',
        "model": 'model',
        "org_id": 'org_id',
        "serial": 'serial',
        "site_id": 'site_id',
        "mtype": 'type',
        "for_site": 'for_site'
    }

    _optionals = [
        'for_site',
    ]

    def __init__(self,
                 mac=None,
                 model=None,
                 org_id=None,
                 serial=None,
                 site_id=None,
                 mtype=None,
                 for_site=APIHelper.SKIP):
        """Constructor for the ApiV1MspsInventoryResponse class"""

        # Initialize members of the class
        if for_site is not APIHelper.SKIP:
            self.for_site = for_site 
        self.mac = mac 
        self.model = model 
        self.org_id = org_id 
        self.serial = serial 
        self.site_id = site_id 
        self.mtype = mtype 

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
        model = dictionary.get("model") if dictionary.get("model") else None
        org_id = dictionary.get("org_id") if dictionary.get("org_id") else None
        serial = dictionary.get("serial") if dictionary.get("serial") else None
        site_id = dictionary.get("site_id") if dictionary.get("site_id") else None
        mtype = dictionary.get("type") if dictionary.get("type") else None
        for_site = dictionary.get("for_site") if "for_site" in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(mac,
                   model,
                   org_id,
                   serial,
                   site_id,
                   mtype,
                   for_site)
