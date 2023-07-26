# -*- coding: utf-8 -*-

"""
mistapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from mistapi.api_helper import APIHelper
from mistapi.models.wlan import Wlan


class Secpolicy(object):

    """Implementation of the 'secpolicy' model.

    Security Policy is designed to audit / catch discripancies between “what’s
    intended to be running” versus “what’s actually running” in a network.
    Many big organizations have separated Security and IT team (for good
    reasons). Each site can be assigned a security policy. Whenever an AP is
    provisioned, the configuration will be checked against the security
    policy. Any violations will be flagged in Device Config History where you
    can search for the when and where the violation occurs.

    Attributes:
        created_time (float): TODO: type description here.
        id (uuid|string): TODO: type description here.
        modified_time (float): TODO: type description here.
        name (string): TODO: type description here.
        org_id (uuid|string): TODO: type description here.
        site_id (uuid|string): TODO: type description here.
        wlans (list of Wlan): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "created_time": 'created_time',
        "id": 'id',
        "modified_time": 'modified_time',
        "name": 'name',
        "org_id": 'org_id',
        "site_id": 'site_id',
        "wlans": 'wlans'
    }

    _optionals = [
        'created_time',
        'id',
        'modified_time',
        'name',
        'org_id',
        'site_id',
        'wlans',
    ]

    def __init__(self,
                 created_time=APIHelper.SKIP,
                 id=APIHelper.SKIP,
                 modified_time=APIHelper.SKIP,
                 name=APIHelper.SKIP,
                 org_id=APIHelper.SKIP,
                 site_id=APIHelper.SKIP,
                 wlans=APIHelper.SKIP):
        """Constructor for the Secpolicy class"""

        # Initialize members of the class
        if created_time is not APIHelper.SKIP:
            self.created_time = created_time 
        if id is not APIHelper.SKIP:
            self.id = id 
        if modified_time is not APIHelper.SKIP:
            self.modified_time = modified_time 
        if name is not APIHelper.SKIP:
            self.name = name 
        if org_id is not APIHelper.SKIP:
            self.org_id = org_id 
        if site_id is not APIHelper.SKIP:
            self.site_id = site_id 
        if wlans is not APIHelper.SKIP:
            self.wlans = wlans 

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

        created_time = dictionary.get("created_time") if dictionary.get("created_time") else APIHelper.SKIP
        id = dictionary.get("id") if dictionary.get("id") else APIHelper.SKIP
        modified_time = dictionary.get("modified_time") if dictionary.get("modified_time") else APIHelper.SKIP
        name = dictionary.get("name") if dictionary.get("name") else APIHelper.SKIP
        org_id = dictionary.get("org_id") if dictionary.get("org_id") else APIHelper.SKIP
        site_id = dictionary.get("site_id") if dictionary.get("site_id") else APIHelper.SKIP
        wlans = None
        if dictionary.get('wlans') is not None:
            wlans = [Wlan.from_dictionary(x) for x in dictionary.get('wlans')]
        else:
            wlans = APIHelper.SKIP
        # Return an object of this model
        return cls(created_time,
                   id,
                   modified_time,
                   name,
                   org_id,
                   site_id,
                   wlans)