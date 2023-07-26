# -*- coding: utf-8 -*-

"""
mistapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from mistapi.api_helper import APIHelper
from mistapi.models.dynamic_vlan import DynamicVlan
from mistapi.models.junos_radius_config import JunosRadiusConfig
from mistapi.models.radsec import Radsec


class ApPortConfig(object):

    """Implementation of the 'ap_port_config' model.

    TODO: type model description here.

    Attributes:
        additional_vlan_ids (list of int): additional VLAN IDs, only valid in
            mesh base mode
        authentication_protocol (AuthenticationProtocolEnum): if
            `enable_mac_auth`==`true`, allows user to select an authentication
            protocol
        disabled (bool): TODO: type description here.
        dynamic_vlan (DynamicVlan): optional dynamic vlan
        enable_mac_auth (bool): TODO: type description here.
        forwarding (ForwardingEnum): TODO: type description here.
        mx_tunnel_id (uuid|string): if `forwarding`==`mxtunnel`, vlan_ids
            comes from mxtunnel
        mxtunnel_name (string): if `forwarding`==`site_mxedge`, vlan_ids comes
            from site_mxedge (`mxtunnels` under site setting)
        port_auth (PortAuthEnum): When doing port auth
        port_vlan_id (int): if `forwrding`==`limited`
        radius_config (JunosRadiusConfig): Junos Radius config
        radsec (Radsec): Radsec settings
        vlan_id (int): optional to specify the vlan id for a tunnel if
            forwarding is for `wxtunnel`, `mxtunnel` or `site_mxedge`. * if
            vlan_id is not specified then it will use first one in vlan_ids[]
            of the mxtunnel. * if forwarding == site_mxedge, vlan_ids comes
            from site_mxedge (`mxtunnels` under site setting)
        vland_ids (list of int): if `forwrding`==`limited`
        wxtunnel_id (string): if `forwarding`==`wxtunnel`, the port is bridged
            to the vlan of the session
        wxtunnel_remote_id (string): if `forwarding`==`wxtunnel`, the port is
            bridged to the vlan of the session

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "additional_vlan_ids": 'additional_vlan_ids',
        "authentication_protocol": 'authentication_protocol',
        "disabled": 'disabled',
        "dynamic_vlan": 'dynamic_vlan',
        "enable_mac_auth": 'enable_mac_auth',
        "forwarding": 'forwarding',
        "mx_tunnel_id": 'mx_tunnel_id',
        "mxtunnel_name": 'mxtunnel_name',
        "port_auth": 'port_auth',
        "port_vlan_id": 'port_vlan_id',
        "radius_config": 'radius_config',
        "radsec": 'radsec',
        "vlan_id": 'vlan_id',
        "vland_ids": 'vland_ids',
        "wxtunnel_id": 'wxtunnel_id',
        "wxtunnel_remote_id": 'wxtunnel_remote_id'
    }

    _optionals = [
        'additional_vlan_ids',
        'authentication_protocol',
        'disabled',
        'dynamic_vlan',
        'enable_mac_auth',
        'forwarding',
        'mx_tunnel_id',
        'mxtunnel_name',
        'port_auth',
        'port_vlan_id',
        'radius_config',
        'radsec',
        'vlan_id',
        'vland_ids',
        'wxtunnel_id',
        'wxtunnel_remote_id',
    ]

    def __init__(self,
                 additional_vlan_ids=APIHelper.SKIP,
                 authentication_protocol='pap',
                 disabled=APIHelper.SKIP,
                 dynamic_vlan=APIHelper.SKIP,
                 enable_mac_auth=APIHelper.SKIP,
                 forwarding='all',
                 mx_tunnel_id=APIHelper.SKIP,
                 mxtunnel_name=APIHelper.SKIP,
                 port_auth='none',
                 port_vlan_id=APIHelper.SKIP,
                 radius_config=APIHelper.SKIP,
                 radsec=APIHelper.SKIP,
                 vlan_id=APIHelper.SKIP,
                 vland_ids=APIHelper.SKIP,
                 wxtunnel_id=APIHelper.SKIP,
                 wxtunnel_remote_id=APIHelper.SKIP):
        """Constructor for the ApPortConfig class"""

        # Initialize members of the class
        if additional_vlan_ids is not APIHelper.SKIP:
            self.additional_vlan_ids = additional_vlan_ids 
        self.authentication_protocol = authentication_protocol 
        if disabled is not APIHelper.SKIP:
            self.disabled = disabled 
        if dynamic_vlan is not APIHelper.SKIP:
            self.dynamic_vlan = dynamic_vlan 
        if enable_mac_auth is not APIHelper.SKIP:
            self.enable_mac_auth = enable_mac_auth 
        self.forwarding = forwarding 
        if mx_tunnel_id is not APIHelper.SKIP:
            self.mx_tunnel_id = mx_tunnel_id 
        if mxtunnel_name is not APIHelper.SKIP:
            self.mxtunnel_name = mxtunnel_name 
        self.port_auth = port_auth 
        if port_vlan_id is not APIHelper.SKIP:
            self.port_vlan_id = port_vlan_id 
        if radius_config is not APIHelper.SKIP:
            self.radius_config = radius_config 
        if radsec is not APIHelper.SKIP:
            self.radsec = radsec 
        if vlan_id is not APIHelper.SKIP:
            self.vlan_id = vlan_id 
        if vland_ids is not APIHelper.SKIP:
            self.vland_ids = vland_ids 
        if wxtunnel_id is not APIHelper.SKIP:
            self.wxtunnel_id = wxtunnel_id 
        if wxtunnel_remote_id is not APIHelper.SKIP:
            self.wxtunnel_remote_id = wxtunnel_remote_id 

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

        additional_vlan_ids = dictionary.get("additional_vlan_ids") if dictionary.get("additional_vlan_ids") else APIHelper.SKIP
        authentication_protocol = dictionary.get("authentication_protocol") if dictionary.get("authentication_protocol") else 'pap'
        disabled = dictionary.get("disabled") if "disabled" in dictionary.keys() else APIHelper.SKIP
        dynamic_vlan = DynamicVlan.from_dictionary(dictionary.get('dynamic_vlan')) if 'dynamic_vlan' in dictionary.keys() else APIHelper.SKIP
        enable_mac_auth = dictionary.get("enable_mac_auth") if "enable_mac_auth" in dictionary.keys() else APIHelper.SKIP
        forwarding = dictionary.get("forwarding") if dictionary.get("forwarding") else 'all'
        mx_tunnel_id = dictionary.get("mx_tunnel_id") if dictionary.get("mx_tunnel_id") else APIHelper.SKIP
        mxtunnel_name = dictionary.get("mxtunnel_name") if dictionary.get("mxtunnel_name") else APIHelper.SKIP
        port_auth = dictionary.get("port_auth") if dictionary.get("port_auth") else 'none'
        port_vlan_id = dictionary.get("port_vlan_id") if dictionary.get("port_vlan_id") else APIHelper.SKIP
        radius_config = JunosRadiusConfig.from_dictionary(dictionary.get('radius_config')) if 'radius_config' in dictionary.keys() else APIHelper.SKIP
        radsec = Radsec.from_dictionary(dictionary.get('radsec')) if 'radsec' in dictionary.keys() else APIHelper.SKIP
        vlan_id = dictionary.get("vlan_id") if dictionary.get("vlan_id") else APIHelper.SKIP
        vland_ids = dictionary.get("vland_ids") if dictionary.get("vland_ids") else APIHelper.SKIP
        wxtunnel_id = dictionary.get("wxtunnel_id") if dictionary.get("wxtunnel_id") else APIHelper.SKIP
        wxtunnel_remote_id = dictionary.get("wxtunnel_remote_id") if dictionary.get("wxtunnel_remote_id") else APIHelper.SKIP
        # Return an object of this model
        return cls(additional_vlan_ids,
                   authentication_protocol,
                   disabled,
                   dynamic_vlan,
                   enable_mac_auth,
                   forwarding,
                   mx_tunnel_id,
                   mxtunnel_name,
                   port_auth,
                   port_vlan_id,
                   radius_config,
                   radsec,
                   vlan_id,
                   vland_ids,
                   wxtunnel_id,
                   wxtunnel_remote_id)