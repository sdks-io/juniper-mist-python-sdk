# -*- coding: utf-8 -*-

"""
mistapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from mistapi.api_helper import APIHelper
from mistapi.models.spec_1 import Spec1


class Service(object):

    """Implementation of the 'service' model.

    WIP

    Attributes:
        addresses (list of string): if `type`==`custom`, ip subnets
        app_caetgories (list of string): list of application categories are
            available through /api/v1/const/app_categories
        apps (list of string): when `type`==`app`, comes from
            `/api/v1/const/apps` when `type`==`ssr_app`, comes from
            `/api/v1/const/ssr_apps` when `type`==`srx_app`, comes from
            `/api/v1/const/srx_apps` when `type`==`app_categories`, comes from
            `/api/v1/const/app_categories`
        created_time (int): TODO: type description here.
        description (string): TODO: type description here.
        dscp (int): when `traffic_type`==`custom`
        failover_policy (FailoverPolicyEnum): TODO: type description here.
        hostnames (list of string): if `type`==`custom`, web filtering
        id (uuid|string): TODO: type description here.
        max_jitter (int): when `traffic_type`==`custom`, for uplink selection
        max_latency (string): when `traffic_type`==`custom`, for uplink
            selection
        max_loss (int): when `traffic_type`==`custom`, for uplink selection
        modified_time (int): TODO: type description here.
        name (string): TODO: type description here.
        org_id (uuid|string): TODO: type description here.
        sle_enabled (bool): whether to enable measure SLE
        specs (list of Spec1): when `type`==`addresses` or `type`==`hostnames`
            if `type`==`custom`, specs is optional. If it doesn't exist, http
            and https is assumed.
        traffic_class (TrafficClassEnum): when `traffic_type`==`custom`
        traffic_type (string): values from `/api/v1/consts/traffic_types` *
            when `type`==`apps`, we'll choose traffic_type automatically *
            when `type`==`addresses` or `type`==`hostnames`, you can provide
            your own settings (optional)
        mtype (Type40Enum): TODO: type description here.
        vpn_name (VpnNameEnum): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "addresses": 'addresses',
        "app_caetgories": 'app_caetgories',
        "apps": 'apps',
        "created_time": 'created_time',
        "description": 'description',
        "dscp": 'dscp',
        "failover_policy": 'failover_policy',
        "hostnames": 'hostnames',
        "id": 'id',
        "max_jitter": 'max_jitter',
        "max_latency": 'max_latency',
        "max_loss": 'max_loss',
        "modified_time": 'modified_time',
        "name": 'name',
        "org_id": 'org_id',
        "sle_enabled": 'sle_enabled',
        "specs": 'specs',
        "traffic_class": 'traffic_class',
        "traffic_type": 'traffic_type',
        "mtype": 'type',
        "vpn_name": 'vpn_name'
    }

    _optionals = [
        'addresses',
        'app_caetgories',
        'apps',
        'created_time',
        'description',
        'dscp',
        'failover_policy',
        'hostnames',
        'id',
        'max_jitter',
        'max_latency',
        'max_loss',
        'modified_time',
        'name',
        'org_id',
        'sle_enabled',
        'specs',
        'traffic_class',
        'traffic_type',
        'mtype',
        'vpn_name',
    ]

    def __init__(self,
                 addresses=APIHelper.SKIP,
                 app_caetgories=APIHelper.SKIP,
                 apps=APIHelper.SKIP,
                 created_time=APIHelper.SKIP,
                 description=APIHelper.SKIP,
                 dscp=APIHelper.SKIP,
                 failover_policy='revertable',
                 hostnames=APIHelper.SKIP,
                 id=APIHelper.SKIP,
                 max_jitter=APIHelper.SKIP,
                 max_latency=APIHelper.SKIP,
                 max_loss=APIHelper.SKIP,
                 modified_time=APIHelper.SKIP,
                 name=APIHelper.SKIP,
                 org_id=APIHelper.SKIP,
                 sle_enabled=False,
                 specs=APIHelper.SKIP,
                 traffic_class='best_effort',
                 traffic_type='data_best_effort',
                 mtype='custom',
                 vpn_name=APIHelper.SKIP):
        """Constructor for the Service class"""

        # Initialize members of the class
        if addresses is not APIHelper.SKIP:
            self.addresses = addresses 
        if app_caetgories is not APIHelper.SKIP:
            self.app_caetgories = app_caetgories 
        if apps is not APIHelper.SKIP:
            self.apps = apps 
        if created_time is not APIHelper.SKIP:
            self.created_time = created_time 
        if description is not APIHelper.SKIP:
            self.description = description 
        if dscp is not APIHelper.SKIP:
            self.dscp = dscp 
        self.failover_policy = failover_policy 
        if hostnames is not APIHelper.SKIP:
            self.hostnames = hostnames 
        if id is not APIHelper.SKIP:
            self.id = id 
        if max_jitter is not APIHelper.SKIP:
            self.max_jitter = max_jitter 
        if max_latency is not APIHelper.SKIP:
            self.max_latency = max_latency 
        if max_loss is not APIHelper.SKIP:
            self.max_loss = max_loss 
        if modified_time is not APIHelper.SKIP:
            self.modified_time = modified_time 
        if name is not APIHelper.SKIP:
            self.name = name 
        if org_id is not APIHelper.SKIP:
            self.org_id = org_id 
        self.sle_enabled = sle_enabled 
        if specs is not APIHelper.SKIP:
            self.specs = specs 
        self.traffic_class = traffic_class 
        self.traffic_type = traffic_type 
        self.mtype = mtype 
        if vpn_name is not APIHelper.SKIP:
            self.vpn_name = vpn_name 

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

        addresses = dictionary.get("addresses") if dictionary.get("addresses") else APIHelper.SKIP
        app_caetgories = dictionary.get("app_caetgories") if dictionary.get("app_caetgories") else APIHelper.SKIP
        apps = dictionary.get("apps") if dictionary.get("apps") else APIHelper.SKIP
        created_time = dictionary.get("created_time") if dictionary.get("created_time") else APIHelper.SKIP
        description = dictionary.get("description") if dictionary.get("description") else APIHelper.SKIP
        dscp = dictionary.get("dscp") if dictionary.get("dscp") else APIHelper.SKIP
        failover_policy = dictionary.get("failover_policy") if dictionary.get("failover_policy") else 'revertable'
        hostnames = dictionary.get("hostnames") if dictionary.get("hostnames") else APIHelper.SKIP
        id = dictionary.get("id") if dictionary.get("id") else APIHelper.SKIP
        max_jitter = dictionary.get("max_jitter") if dictionary.get("max_jitter") else APIHelper.SKIP
        max_latency = dictionary.get("max_latency") if dictionary.get("max_latency") else APIHelper.SKIP
        max_loss = dictionary.get("max_loss") if dictionary.get("max_loss") else APIHelper.SKIP
        modified_time = dictionary.get("modified_time") if dictionary.get("modified_time") else APIHelper.SKIP
        name = dictionary.get("name") if dictionary.get("name") else APIHelper.SKIP
        org_id = dictionary.get("org_id") if dictionary.get("org_id") else APIHelper.SKIP
        sle_enabled = dictionary.get("sle_enabled") if dictionary.get("sle_enabled") else False
        specs = None
        if dictionary.get('specs') is not None:
            specs = [Spec1.from_dictionary(x) for x in dictionary.get('specs')]
        else:
            specs = APIHelper.SKIP
        traffic_class = dictionary.get("traffic_class") if dictionary.get("traffic_class") else 'best_effort'
        traffic_type = dictionary.get("traffic_type") if dictionary.get("traffic_type") else 'data_best_effort'
        mtype = dictionary.get("type") if dictionary.get("type") else 'custom'
        vpn_name = dictionary.get("vpn_name") if dictionary.get("vpn_name") else APIHelper.SKIP
        # Return an object of this model
        return cls(addresses,
                   app_caetgories,
                   apps,
                   created_time,
                   description,
                   dscp,
                   failover_policy,
                   hostnames,
                   id,
                   max_jitter,
                   max_latency,
                   max_loss,
                   modified_time,
                   name,
                   org_id,
                   sle_enabled,
                   specs,
                   traffic_class,
                   traffic_type,
                   mtype,
                   vpn_name)
