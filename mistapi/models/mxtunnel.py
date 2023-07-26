# -*- coding: utf-8 -*-

"""
mistapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from mistapi.api_helper import APIHelper
from mistapi.models.auto_preemption_1 import AutoPreemption1
from mistapi.models.ipsec import Ipsec


class Mxtunnel(object):

    """Implementation of the 'mxtunnel' model.

    MxTunnel

    Attributes:
        anchor_mxtunnel_ids (list of uuid|string): list of anchor mxtunnels
            used for forming edge to edge tunnels
        auto_preemption (AutoPreemption1): TODO: type description here.
        created_time (float): TODO: type description here.
        for_site (bool): TODO: type description here.
        hello_interval (int): in seconds, used as heartbeat to detect if a
            tunnel is alive. AP will try another peer after missing N hellos
            specified by `hello_retries`.
        hello_retries (int): TODO: type description here.
        id (uuid|string): TODO: type description here.
        ipsec (Ipsec): TODO: type description here.
        modified_time (float): TODO: type description here.
        mtu (int): 0 to enable PMTU, 552-1500 to start PMTU with a lower MTU
        mxcluster_ids (list of uuid|string): list of mxclusters to deploy this
            tunnel to
        name (string): TODO: type description here.
        org_id (uuid|string): TODO: type description here.
        protocol (Protocol3Enum): TODO: type description here.
        site_id (uuid|string): TODO: type description here.
        vlan_ids (list of int): list of vlan_ids that will be used

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "anchor_mxtunnel_ids": 'anchor_mxtunnel_ids',
        "auto_preemption": 'auto_preemption',
        "created_time": 'created_time',
        "for_site": 'for_site',
        "hello_interval": 'hello_interval',
        "hello_retries": 'hello_retries',
        "id": 'id',
        "ipsec": 'ipsec',
        "modified_time": 'modified_time',
        "mtu": 'mtu',
        "mxcluster_ids": 'mxcluster_ids',
        "name": 'name',
        "org_id": 'org_id',
        "protocol": 'protocol',
        "site_id": 'site_id',
        "vlan_ids": 'vlan_ids'
    }

    _optionals = [
        'anchor_mxtunnel_ids',
        'auto_preemption',
        'created_time',
        'for_site',
        'hello_interval',
        'hello_retries',
        'id',
        'ipsec',
        'modified_time',
        'mtu',
        'mxcluster_ids',
        'name',
        'org_id',
        'protocol',
        'site_id',
        'vlan_ids',
    ]

    _nullables = [
        'hello_interval',
        'hello_retries',
        'name',
    ]

    def __init__(self,
                 anchor_mxtunnel_ids=APIHelper.SKIP,
                 auto_preemption=APIHelper.SKIP,
                 created_time=APIHelper.SKIP,
                 for_site=APIHelper.SKIP,
                 hello_interval=60,
                 hello_retries=7,
                 id=APIHelper.SKIP,
                 ipsec=APIHelper.SKIP,
                 modified_time=APIHelper.SKIP,
                 mtu=0,
                 mxcluster_ids=APIHelper.SKIP,
                 name=APIHelper.SKIP,
                 org_id=APIHelper.SKIP,
                 protocol='udp',
                 site_id=APIHelper.SKIP,
                 vlan_ids=APIHelper.SKIP):
        """Constructor for the Mxtunnel class"""

        # Initialize members of the class
        if anchor_mxtunnel_ids is not APIHelper.SKIP:
            self.anchor_mxtunnel_ids = anchor_mxtunnel_ids 
        if auto_preemption is not APIHelper.SKIP:
            self.auto_preemption = auto_preemption 
        if created_time is not APIHelper.SKIP:
            self.created_time = created_time 
        if for_site is not APIHelper.SKIP:
            self.for_site = for_site 
        self.hello_interval = hello_interval 
        self.hello_retries = hello_retries 
        if id is not APIHelper.SKIP:
            self.id = id 
        if ipsec is not APIHelper.SKIP:
            self.ipsec = ipsec 
        if modified_time is not APIHelper.SKIP:
            self.modified_time = modified_time 
        self.mtu = mtu 
        if mxcluster_ids is not APIHelper.SKIP:
            self.mxcluster_ids = mxcluster_ids 
        if name is not APIHelper.SKIP:
            self.name = name 
        if org_id is not APIHelper.SKIP:
            self.org_id = org_id 
        self.protocol = protocol 
        if site_id is not APIHelper.SKIP:
            self.site_id = site_id 
        if vlan_ids is not APIHelper.SKIP:
            self.vlan_ids = vlan_ids 

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

        anchor_mxtunnel_ids = dictionary.get("anchor_mxtunnel_ids") if dictionary.get("anchor_mxtunnel_ids") else APIHelper.SKIP
        auto_preemption = AutoPreemption1.from_dictionary(dictionary.get('auto_preemption')) if 'auto_preemption' in dictionary.keys() else APIHelper.SKIP
        created_time = dictionary.get("created_time") if dictionary.get("created_time") else APIHelper.SKIP
        for_site = dictionary.get("for_site") if "for_site" in dictionary.keys() else APIHelper.SKIP
        hello_interval = dictionary.get("hello_interval") if dictionary.get("hello_interval") else 60
        hello_retries = dictionary.get("hello_retries") if dictionary.get("hello_retries") else 7
        id = dictionary.get("id") if dictionary.get("id") else APIHelper.SKIP
        ipsec = Ipsec.from_dictionary(dictionary.get('ipsec')) if 'ipsec' in dictionary.keys() else APIHelper.SKIP
        modified_time = dictionary.get("modified_time") if dictionary.get("modified_time") else APIHelper.SKIP
        mtu = dictionary.get("mtu") if dictionary.get("mtu") else 0
        mxcluster_ids = dictionary.get("mxcluster_ids") if dictionary.get("mxcluster_ids") else APIHelper.SKIP
        name = dictionary.get("name") if "name" in dictionary.keys() else APIHelper.SKIP
        org_id = dictionary.get("org_id") if dictionary.get("org_id") else APIHelper.SKIP
        protocol = dictionary.get("protocol") if dictionary.get("protocol") else 'udp'
        site_id = dictionary.get("site_id") if dictionary.get("site_id") else APIHelper.SKIP
        vlan_ids = dictionary.get("vlan_ids") if dictionary.get("vlan_ids") else APIHelper.SKIP
        # Return an object of this model
        return cls(anchor_mxtunnel_ids,
                   auto_preemption,
                   created_time,
                   for_site,
                   hello_interval,
                   hello_retries,
                   id,
                   ipsec,
                   modified_time,
                   mtu,
                   mxcluster_ids,
                   name,
                   org_id,
                   protocol,
                   site_id,
                   vlan_ids)