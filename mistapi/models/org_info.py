# -*- coding: utf-8 -*-

"""
mistapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from mistapi.api_helper import APIHelper


class OrgInfo(object):

    """Implementation of the 'org_info' model.

    TODO: type model description here.

    Attributes:
        alarmtemplate_id (uuid|string): TODO: type description here.
        allow_mist (bool): TODO: type description here.
        created_time (float): TODO: type description here.
        id (uuid|string): TODO: type description here.
        modified_time (float): TODO: type description here.
        msp_id (uuid|string): TODO: type description here.
        msp_logo_url (string): logo uploaded by the MSP with advanced tier,
            only present if provided
        msp_name (string): name of the msp the org belongs to
        name (string): TODO: type description here.
        orggroup_ids (list of uuid|string): TODO: type description here.
        session_expiry (float): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id": 'id',
        "name": 'name',
        "alarmtemplate_id": 'alarmtemplate_id',
        "allow_mist": 'allow_mist',
        "created_time": 'created_time',
        "modified_time": 'modified_time',
        "msp_id": 'msp_id',
        "msp_logo_url": 'msp_logo_url',
        "msp_name": 'msp_name',
        "orggroup_ids": 'orggroup_ids',
        "session_expiry": 'session_expiry'
    }

    _optionals = [
        'alarmtemplate_id',
        'allow_mist',
        'created_time',
        'modified_time',
        'msp_id',
        'msp_logo_url',
        'msp_name',
        'orggroup_ids',
        'session_expiry',
    ]

    _nullables = [
        'alarmtemplate_id',
    ]

    def __init__(self,
                 id=None,
                 name=None,
                 alarmtemplate_id=APIHelper.SKIP,
                 allow_mist=True,
                 created_time=APIHelper.SKIP,
                 modified_time=APIHelper.SKIP,
                 msp_id=APIHelper.SKIP,
                 msp_logo_url=APIHelper.SKIP,
                 msp_name=APIHelper.SKIP,
                 orggroup_ids=APIHelper.SKIP,
                 session_expiry=1440):
        """Constructor for the OrgInfo class"""

        # Initialize members of the class
        if alarmtemplate_id is not APIHelper.SKIP:
            self.alarmtemplate_id = alarmtemplate_id 
        self.allow_mist = allow_mist 
        if created_time is not APIHelper.SKIP:
            self.created_time = created_time 
        self.id = id 
        if modified_time is not APIHelper.SKIP:
            self.modified_time = modified_time 
        if msp_id is not APIHelper.SKIP:
            self.msp_id = msp_id 
        if msp_logo_url is not APIHelper.SKIP:
            self.msp_logo_url = msp_logo_url 
        if msp_name is not APIHelper.SKIP:
            self.msp_name = msp_name 
        self.name = name 
        if orggroup_ids is not APIHelper.SKIP:
            self.orggroup_ids = orggroup_ids 
        self.session_expiry = session_expiry 

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

        id = dictionary.get("id") if dictionary.get("id") else None
        name = dictionary.get("name") if dictionary.get("name") else None
        alarmtemplate_id = dictionary.get("alarmtemplate_id") if "alarmtemplate_id" in dictionary.keys() else APIHelper.SKIP
        allow_mist = dictionary.get("allow_mist") if dictionary.get("allow_mist") else True
        created_time = dictionary.get("created_time") if dictionary.get("created_time") else APIHelper.SKIP
        modified_time = dictionary.get("modified_time") if dictionary.get("modified_time") else APIHelper.SKIP
        msp_id = dictionary.get("msp_id") if dictionary.get("msp_id") else APIHelper.SKIP
        msp_logo_url = dictionary.get("msp_logo_url") if dictionary.get("msp_logo_url") else APIHelper.SKIP
        msp_name = dictionary.get("msp_name") if dictionary.get("msp_name") else APIHelper.SKIP
        orggroup_ids = dictionary.get("orggroup_ids") if dictionary.get("orggroup_ids") else APIHelper.SKIP
        session_expiry = dictionary.get("session_expiry") if dictionary.get("session_expiry") else 1440
        # Return an object of this model
        return cls(id,
                   name,
                   alarmtemplate_id,
                   allow_mist,
                   created_time,
                   modified_time,
                   msp_id,
                   msp_logo_url,
                   msp_name,
                   orggroup_ids,
                   session_expiry)