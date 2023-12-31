# -*- coding: utf-8 -*-

"""
mistapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from mistapi.api_helper import APIHelper
from mistapi.models.hosts import Hosts
from mistapi.models.internal_access import InternalAccess
from mistapi.models.internet_access import InternetAccess
from mistapi.models.tenants import Tenants
from mistapi.models.vpn_access import VpnAccess


class Network(object):

    """Implementation of the 'network' model.

    Networks are usually subnets that have cross-site significance.
    `networks`in Org Settings will got merged into `networks`in Site Setting.
    For gateways, they can be used to define Service Routes.

    Attributes:
        created_time (float): TODO: type description here.
        disallow_mist_services (bool): whether to disallow Mist Devices in the
            network
        gateway (string): TODO: type description here.
        hosts (dict): TODO: type description here.
        id (uuid|string): TODO: type description here.
        internal_access (InternalAccess): TODO: type description here.
        internet_access (InternetAccess): whether this network has direct
            internet access
        isolation (bool): whether to allow clients in the network to talk to
            each other
        modified_time (float): TODO: type description here.
        name (string): TODO: type description here.
        org_id (uuid|string): TODO: type description here.
        subnet (string): TODO: type description here.
        tenants (dict): TODO: type description here.
        vlan_id (int): TODO: type description here.
        vpn_access (dict): whether this network can be accessed from vpn

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "created_time": 'created_time',
        "disallow_mist_services": 'disallow_mist_services',
        "gateway": 'gateway',
        "hosts": 'hosts',
        "id": 'id',
        "internal_access": 'internal_access',
        "internet_access": 'internet_access',
        "isolation": 'isolation',
        "modified_time": 'modified_time',
        "name": 'name',
        "org_id": 'org_id',
        "subnet": 'subnet',
        "tenants": 'tenants',
        "vlan_id": 'vlan_id',
        "vpn_access": 'vpn_access'
    }

    _optionals = [
        'created_time',
        'disallow_mist_services',
        'gateway',
        'hosts',
        'id',
        'internal_access',
        'internet_access',
        'isolation',
        'modified_time',
        'name',
        'org_id',
        'subnet',
        'tenants',
        'vlan_id',
        'vpn_access',
    ]

    def __init__(self,
                 created_time=APIHelper.SKIP,
                 disallow_mist_services=False,
                 gateway=APIHelper.SKIP,
                 hosts=APIHelper.SKIP,
                 id=APIHelper.SKIP,
                 internal_access=APIHelper.SKIP,
                 internet_access=APIHelper.SKIP,
                 isolation=APIHelper.SKIP,
                 modified_time=APIHelper.SKIP,
                 name=APIHelper.SKIP,
                 org_id=APIHelper.SKIP,
                 subnet=APIHelper.SKIP,
                 tenants=APIHelper.SKIP,
                 vlan_id=APIHelper.SKIP,
                 vpn_access=APIHelper.SKIP):
        """Constructor for the Network class"""

        # Initialize members of the class
        if created_time is not APIHelper.SKIP:
            self.created_time = created_time 
        self.disallow_mist_services = disallow_mist_services 
        if gateway is not APIHelper.SKIP:
            self.gateway = gateway 
        if hosts is not APIHelper.SKIP:
            self.hosts = hosts 
        if id is not APIHelper.SKIP:
            self.id = id 
        if internal_access is not APIHelper.SKIP:
            self.internal_access = internal_access 
        if internet_access is not APIHelper.SKIP:
            self.internet_access = internet_access 
        if isolation is not APIHelper.SKIP:
            self.isolation = isolation 
        if modified_time is not APIHelper.SKIP:
            self.modified_time = modified_time 
        if name is not APIHelper.SKIP:
            self.name = name 
        if org_id is not APIHelper.SKIP:
            self.org_id = org_id 
        if subnet is not APIHelper.SKIP:
            self.subnet = subnet 
        if tenants is not APIHelper.SKIP:
            self.tenants = tenants 
        if vlan_id is not APIHelper.SKIP:
            self.vlan_id = vlan_id 
        if vpn_access is not APIHelper.SKIP:
            self.vpn_access = vpn_access 

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
        disallow_mist_services = dictionary.get("disallow_mist_services") if dictionary.get("disallow_mist_services") else False
        gateway = dictionary.get("gateway") if dictionary.get("gateway") else APIHelper.SKIP
        hosts = Hosts.from_dictionary(dictionary.get('hosts')) if 'hosts' in dictionary.keys() else APIHelper.SKIP
        id = dictionary.get("id") if dictionary.get("id") else APIHelper.SKIP
        internal_access = InternalAccess.from_dictionary(dictionary.get('internal_access')) if 'internal_access' in dictionary.keys() else APIHelper.SKIP
        internet_access = InternetAccess.from_dictionary(dictionary.get('internet_access')) if 'internet_access' in dictionary.keys() else APIHelper.SKIP
        isolation = dictionary.get("isolation") if "isolation" in dictionary.keys() else APIHelper.SKIP
        modified_time = dictionary.get("modified_time") if dictionary.get("modified_time") else APIHelper.SKIP
        name = dictionary.get("name") if dictionary.get("name") else APIHelper.SKIP
        org_id = dictionary.get("org_id") if dictionary.get("org_id") else APIHelper.SKIP
        subnet = dictionary.get("subnet") if dictionary.get("subnet") else APIHelper.SKIP
        tenants = Tenants.from_dictionary(dictionary.get('tenants')) if 'tenants' in dictionary.keys() else APIHelper.SKIP
        vlan_id = dictionary.get("vlan_id") if dictionary.get("vlan_id") else APIHelper.SKIP
        vpn_access = VpnAccess.from_dictionary(dictionary.get('vpn_access')) if 'vpn_access' in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(created_time,
                   disallow_mist_services,
                   gateway,
                   hosts,
                   id,
                   internal_access,
                   internet_access,
                   isolation,
                   modified_time,
                   name,
                   org_id,
                   subnet,
                   tenants,
                   vlan_id,
                   vpn_access)
