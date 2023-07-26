# -*- coding: utf-8 -*-

"""
mistapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from mistapi.api_helper import APIHelper
from mistapi.models.tunterm_ip_config_1 import TuntermIpConfig1
from mistapi.models.tunterm_port_config_2 import TuntermPortConfig2


class ApiV1SitesMxedgesSupportResponse(object):

    """Implementation of the 'Api V1 Sites Mxedges Support Response' model.

    TODO: type model description here.

    Attributes:
        created_time (int): TODO: type description here.
        for_site (bool): TODO: type description here.
        id (string): TODO: type description here.
        magic (string): TODO: type description here.
        model (string): TODO: type description here.
        modified_time (int): TODO: type description here.
        mxagent_registered (bool): TODO: type description here.
        mxcluster_id (uuid|string): TODO: type description here.
        name (string): TODO: type description here.
        org_id (string): TODO: type description here.
        services (list of string): TODO: type description here.
        site_id (string): TODO: type description here.
        status (string): TODO: type description here.
        tunterm_ip_config (TuntermIpConfig1): TODO: type description here.
        tunterm_port_config (TuntermPortConfig2): TODO: type description
            here.
        tunterm_registered (bool): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "created_time": 'created_time',
        "for_site": 'for_site',
        "id": 'id',
        "magic": 'magic',
        "model": 'model',
        "modified_time": 'modified_time',
        "mxagent_registered": 'mxagent_registered',
        "mxcluster_id": 'mxcluster_id',
        "name": 'name',
        "org_id": 'org_id',
        "services": 'services',
        "site_id": 'site_id',
        "status": 'status',
        "tunterm_ip_config": 'tunterm_ip_config',
        "tunterm_port_config": 'tunterm_port_config',
        "tunterm_registered": 'tunterm_registered'
    }

    _optionals = [
        'created_time',
        'for_site',
        'id',
        'magic',
        'model',
        'modified_time',
        'mxagent_registered',
        'mxcluster_id',
        'name',
        'org_id',
        'services',
        'site_id',
        'status',
        'tunterm_ip_config',
        'tunterm_port_config',
        'tunterm_registered',
    ]

    def __init__(self,
                 created_time=APIHelper.SKIP,
                 for_site=APIHelper.SKIP,
                 id=APIHelper.SKIP,
                 magic=APIHelper.SKIP,
                 model=APIHelper.SKIP,
                 modified_time=APIHelper.SKIP,
                 mxagent_registered=APIHelper.SKIP,
                 mxcluster_id=APIHelper.SKIP,
                 name=APIHelper.SKIP,
                 org_id=APIHelper.SKIP,
                 services=APIHelper.SKIP,
                 site_id=APIHelper.SKIP,
                 status=APIHelper.SKIP,
                 tunterm_ip_config=APIHelper.SKIP,
                 tunterm_port_config=APIHelper.SKIP,
                 tunterm_registered=APIHelper.SKIP):
        """Constructor for the ApiV1SitesMxedgesSupportResponse class"""

        # Initialize members of the class
        if created_time is not APIHelper.SKIP:
            self.created_time = created_time 
        if for_site is not APIHelper.SKIP:
            self.for_site = for_site 
        if id is not APIHelper.SKIP:
            self.id = id 
        if magic is not APIHelper.SKIP:
            self.magic = magic 
        if model is not APIHelper.SKIP:
            self.model = model 
        if modified_time is not APIHelper.SKIP:
            self.modified_time = modified_time 
        if mxagent_registered is not APIHelper.SKIP:
            self.mxagent_registered = mxagent_registered 
        if mxcluster_id is not APIHelper.SKIP:
            self.mxcluster_id = mxcluster_id 
        if name is not APIHelper.SKIP:
            self.name = name 
        if org_id is not APIHelper.SKIP:
            self.org_id = org_id 
        if services is not APIHelper.SKIP:
            self.services = services 
        if site_id is not APIHelper.SKIP:
            self.site_id = site_id 
        if status is not APIHelper.SKIP:
            self.status = status 
        if tunterm_ip_config is not APIHelper.SKIP:
            self.tunterm_ip_config = tunterm_ip_config 
        if tunterm_port_config is not APIHelper.SKIP:
            self.tunterm_port_config = tunterm_port_config 
        if tunterm_registered is not APIHelper.SKIP:
            self.tunterm_registered = tunterm_registered 

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
        for_site = dictionary.get("for_site") if "for_site" in dictionary.keys() else APIHelper.SKIP
        id = dictionary.get("id") if dictionary.get("id") else APIHelper.SKIP
        magic = dictionary.get("magic") if dictionary.get("magic") else APIHelper.SKIP
        model = dictionary.get("model") if dictionary.get("model") else APIHelper.SKIP
        modified_time = dictionary.get("modified_time") if dictionary.get("modified_time") else APIHelper.SKIP
        mxagent_registered = dictionary.get("mxagent_registered") if "mxagent_registered" in dictionary.keys() else APIHelper.SKIP
        mxcluster_id = dictionary.get("mxcluster_id") if dictionary.get("mxcluster_id") else APIHelper.SKIP
        name = dictionary.get("name") if dictionary.get("name") else APIHelper.SKIP
        org_id = dictionary.get("org_id") if dictionary.get("org_id") else APIHelper.SKIP
        services = dictionary.get("services") if dictionary.get("services") else APIHelper.SKIP
        site_id = dictionary.get("site_id") if dictionary.get("site_id") else APIHelper.SKIP
        status = dictionary.get("status") if dictionary.get("status") else APIHelper.SKIP
        tunterm_ip_config = TuntermIpConfig1.from_dictionary(dictionary.get('tunterm_ip_config')) if 'tunterm_ip_config' in dictionary.keys() else APIHelper.SKIP
        tunterm_port_config = TuntermPortConfig2.from_dictionary(dictionary.get('tunterm_port_config')) if 'tunterm_port_config' in dictionary.keys() else APIHelper.SKIP
        tunterm_registered = dictionary.get("tunterm_registered") if "tunterm_registered" in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(created_time,
                   for_site,
                   id,
                   magic,
                   model,
                   modified_time,
                   mxagent_registered,
                   mxcluster_id,
                   name,
                   org_id,
                   services,
                   site_id,
                   status,
                   tunterm_ip_config,
                   tunterm_port_config,
                   tunterm_registered)