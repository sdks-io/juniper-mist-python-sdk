# -*- coding: utf-8 -*-

"""
mistapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from mistapi.api_helper import APIHelper


class WxlanRule(object):

    """Implementation of the 'wxlan_rule' model.

    WXlan

    Attributes:
        action (Action7Enum): type of action, allow / block
        blocked_apps (list of string): blocked apps (always blocking, ignoring
            action), the key of Get Application List
        created_time (float): TODO: type description here.
        dst_allow_wxtags (list of string): tag list to indicate these tags are
            allowed access
        dst_deny_wxtags (list of string): tag list to indicate these tags are
            blocked access
        enabled (bool): TODO: type description here.
        for_site (bool): TODO: type description here.
        id (uuid|string): TODO: type description here.
        modified_time (float): TODO: type description here.
        order (float): the order how rules would be looked up, > 0 and bigger
            order got matched first, -1 means LAST, uniqueness not checked
        org_id (uuid|string): TODO: type description here.
        site_id (uuid|string): TODO: type description here.
        src_wxtags (list of string): tag list to determine if this rule would
            match

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "order": 'order',
        "src_wxtags": 'src_wxtags',
        "action": 'action',
        "blocked_apps": 'blocked_apps',
        "created_time": 'created_time',
        "dst_allow_wxtags": 'dst_allow_wxtags',
        "dst_deny_wxtags": 'dst_deny_wxtags',
        "enabled": 'enabled',
        "for_site": 'for_site',
        "id": 'id',
        "modified_time": 'modified_time',
        "org_id": 'org_id',
        "site_id": 'site_id'
    }

    _optionals = [
        'action',
        'blocked_apps',
        'created_time',
        'dst_allow_wxtags',
        'dst_deny_wxtags',
        'enabled',
        'for_site',
        'id',
        'modified_time',
        'org_id',
        'site_id',
    ]

    def __init__(self,
                 order=None,
                 src_wxtags=None,
                 action=APIHelper.SKIP,
                 blocked_apps=APIHelper.SKIP,
                 created_time=APIHelper.SKIP,
                 dst_allow_wxtags=APIHelper.SKIP,
                 dst_deny_wxtags=APIHelper.SKIP,
                 enabled=True,
                 for_site=APIHelper.SKIP,
                 id=APIHelper.SKIP,
                 modified_time=APIHelper.SKIP,
                 org_id=APIHelper.SKIP,
                 site_id=APIHelper.SKIP):
        """Constructor for the WxlanRule class"""

        # Initialize members of the class
        if action is not APIHelper.SKIP:
            self.action = action 
        if blocked_apps is not APIHelper.SKIP:
            self.blocked_apps = blocked_apps 
        if created_time is not APIHelper.SKIP:
            self.created_time = created_time 
        if dst_allow_wxtags is not APIHelper.SKIP:
            self.dst_allow_wxtags = dst_allow_wxtags 
        if dst_deny_wxtags is not APIHelper.SKIP:
            self.dst_deny_wxtags = dst_deny_wxtags 
        self.enabled = enabled 
        if for_site is not APIHelper.SKIP:
            self.for_site = for_site 
        if id is not APIHelper.SKIP:
            self.id = id 
        if modified_time is not APIHelper.SKIP:
            self.modified_time = modified_time 
        self.order = order 
        if org_id is not APIHelper.SKIP:
            self.org_id = org_id 
        if site_id is not APIHelper.SKIP:
            self.site_id = site_id 
        self.src_wxtags = src_wxtags 

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

        order = dictionary.get("order") if dictionary.get("order") else None
        src_wxtags = dictionary.get("src_wxtags") if dictionary.get("src_wxtags") else None
        action = dictionary.get("action") if dictionary.get("action") else APIHelper.SKIP
        blocked_apps = dictionary.get("blocked_apps") if dictionary.get("blocked_apps") else APIHelper.SKIP
        created_time = dictionary.get("created_time") if dictionary.get("created_time") else APIHelper.SKIP
        dst_allow_wxtags = dictionary.get("dst_allow_wxtags") if dictionary.get("dst_allow_wxtags") else APIHelper.SKIP
        dst_deny_wxtags = dictionary.get("dst_deny_wxtags") if dictionary.get("dst_deny_wxtags") else APIHelper.SKIP
        enabled = dictionary.get("enabled") if dictionary.get("enabled") else True
        for_site = dictionary.get("for_site") if "for_site" in dictionary.keys() else APIHelper.SKIP
        id = dictionary.get("id") if dictionary.get("id") else APIHelper.SKIP
        modified_time = dictionary.get("modified_time") if dictionary.get("modified_time") else APIHelper.SKIP
        org_id = dictionary.get("org_id") if dictionary.get("org_id") else APIHelper.SKIP
        site_id = dictionary.get("site_id") if dictionary.get("site_id") else APIHelper.SKIP
        # Return an object of this model
        return cls(order,
                   src_wxtags,
                   action,
                   blocked_apps,
                   created_time,
                   dst_allow_wxtags,
                   dst_deny_wxtags,
                   enabled,
                   for_site,
                   id,
                   modified_time,
                   org_id,
                   site_id)