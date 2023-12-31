# -*- coding: utf-8 -*-

"""
mistapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from mistapi.api_helper import APIHelper


class Privileges(object):

    """Implementation of the 'privileges' model.

    Privilieges settings

    Attributes:
        for_site (bool): TODO: type description here.
        msp_id (uuid|string): id of the MSP (if the org belongs to an MSP)
        msp_logo_url (string): logo of the MSP (if the MSP belongs to an
            Advanced tier)
        msp_name (string): name of the MSP (if the org belongs to an MSP)
        msp_url (string): custom url of the MSP (if the MSP belongs to an
            Advanced tier)
        name (string): name of the org/site/MSP depending on object scope
        org_id (uuid|string): id of the org
        org_name (string): name of the org (for a site belonging to org)
        orggroup_ids (list of uuid|string): list of orggroup ids (if the org
            belongs to an MSP)
        role (RoleEnum): access permissions
        scope (ScopeEnum): list of privileges the admin has on the MSP /
            OrgGroups / Orgs / Sites
        site_id (uuid|string): id of the site
        sitegroup_ids (list of uuid|string): list of sitegroup ids
        views (list of string): Custom roles restrict Org users to specific UI
            views. This is useful for limiting UI access of Org users.  You
            can invite a new user or update existing users in your Org to this
            custom role. For this, specify view along with role when assigning
            privileges.  Below are the list of supported UI views. Note that
            this is UI only feature Custom roles restrict Org users to
            specific UI views. This is useful for limiting UI access of Org
            users.  You can invite a new user or update existing users in your
            Org to this custom role. For this, specify `view` along with
            `role` when assigning privileges.  Below are the list of supported
            UI views. Note that this is UI only feature  | UI View |
            Description | | --- | --- | | `reporting` | full access to all
            analytics tools | | `marketing` | can view analytics and location
            maps | | `location` | can view and manage location maps | |
            `security` | can view and manage WLAN, rogues and authentication |
            | `switch_admin` | can view and manage Switch ports | |
            `mxedge_admin` | can view and manage Mist edges and Mist tunnels |
            | `lobby_admin` | full access to Org and Site Pre-shared keys |

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "role": 'role',
        "scope": 'scope',
        "for_site": 'for_site',
        "msp_id": 'msp_id',
        "msp_logo_url": 'msp_logo_url',
        "msp_name": 'msp_name',
        "msp_url": 'msp_url',
        "name": 'name',
        "org_id": 'org_id',
        "org_name": 'org_name',
        "orggroup_ids": 'orggroup_ids',
        "site_id": 'site_id',
        "sitegroup_ids": 'sitegroup_ids',
        "views": 'views'
    }

    _optionals = [
        'for_site',
        'msp_id',
        'msp_logo_url',
        'msp_name',
        'msp_url',
        'name',
        'org_id',
        'org_name',
        'orggroup_ids',
        'site_id',
        'sitegroup_ids',
        'views',
    ]

    _nullables = [
        'msp_id',
        'msp_name',
        'org_id',
        'site_id',
    ]

    def __init__(self,
                 role=None,
                 scope=None,
                 for_site=APIHelper.SKIP,
                 msp_id=APIHelper.SKIP,
                 msp_logo_url=APIHelper.SKIP,
                 msp_name=APIHelper.SKIP,
                 msp_url=APIHelper.SKIP,
                 name=APIHelper.SKIP,
                 org_id=APIHelper.SKIP,
                 org_name=APIHelper.SKIP,
                 orggroup_ids=APIHelper.SKIP,
                 site_id=APIHelper.SKIP,
                 sitegroup_ids=APIHelper.SKIP,
                 views=APIHelper.SKIP):
        """Constructor for the Privileges class"""

        # Initialize members of the class
        if for_site is not APIHelper.SKIP:
            self.for_site = for_site 
        if msp_id is not APIHelper.SKIP:
            self.msp_id = msp_id 
        if msp_logo_url is not APIHelper.SKIP:
            self.msp_logo_url = msp_logo_url 
        if msp_name is not APIHelper.SKIP:
            self.msp_name = msp_name 
        if msp_url is not APIHelper.SKIP:
            self.msp_url = msp_url 
        if name is not APIHelper.SKIP:
            self.name = name 
        if org_id is not APIHelper.SKIP:
            self.org_id = org_id 
        if org_name is not APIHelper.SKIP:
            self.org_name = org_name 
        if orggroup_ids is not APIHelper.SKIP:
            self.orggroup_ids = orggroup_ids 
        self.role = role 
        self.scope = scope 
        if site_id is not APIHelper.SKIP:
            self.site_id = site_id 
        if sitegroup_ids is not APIHelper.SKIP:
            self.sitegroup_ids = sitegroup_ids 
        if views is not APIHelper.SKIP:
            self.views = views 

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

        role = dictionary.get("role") if dictionary.get("role") else None
        scope = dictionary.get("scope") if dictionary.get("scope") else None
        for_site = dictionary.get("for_site") if "for_site" in dictionary.keys() else APIHelper.SKIP
        msp_id = dictionary.get("msp_id") if "msp_id" in dictionary.keys() else APIHelper.SKIP
        msp_logo_url = dictionary.get("msp_logo_url") if dictionary.get("msp_logo_url") else APIHelper.SKIP
        msp_name = dictionary.get("msp_name") if "msp_name" in dictionary.keys() else APIHelper.SKIP
        msp_url = dictionary.get("msp_url") if dictionary.get("msp_url") else APIHelper.SKIP
        name = dictionary.get("name") if dictionary.get("name") else APIHelper.SKIP
        org_id = dictionary.get("org_id") if "org_id" in dictionary.keys() else APIHelper.SKIP
        org_name = dictionary.get("org_name") if dictionary.get("org_name") else APIHelper.SKIP
        orggroup_ids = dictionary.get("orggroup_ids") if dictionary.get("orggroup_ids") else APIHelper.SKIP
        site_id = dictionary.get("site_id") if "site_id" in dictionary.keys() else APIHelper.SKIP
        sitegroup_ids = dictionary.get("sitegroup_ids") if dictionary.get("sitegroup_ids") else APIHelper.SKIP
        views = dictionary.get("views") if dictionary.get("views") else APIHelper.SKIP
        # Return an object of this model
        return cls(role,
                   scope,
                   for_site,
                   msp_id,
                   msp_logo_url,
                   msp_name,
                   msp_url,
                   name,
                   org_id,
                   org_name,
                   orggroup_ids,
                   site_id,
                   sitegroup_ids,
                   views)
