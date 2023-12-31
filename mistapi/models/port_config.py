# -*- coding: utf-8 -*-

"""
mistapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from mistapi.api_helper import APIHelper
from mistapi.models.dsl_config import DslConfig
from mistapi.models.junos_ip_config_gateway import JunosIpConfigGateway
from mistapi.models.traffic_shaping import TrafficShaping
from mistapi.models.vpn_paths import VpnPaths
from mistapi.models.wan_source_nat import WanSourceNat


class PortConfig(object):

    """Implementation of the 'PortConfig' model.

    The property key is the interface(s) name (e.g. "eth1,eth2")

    Attributes:
        description (string): TODO: type description here.
        disable_autoneg (bool): TODO: type description here.
        dsl_config (DslConfig): if `wan_type`==`dsl`
        duplex (DuplexEnum): TODO: type description here.
        ip_config (JunosIpConfigGateway): Junos IP Config
        lte_apn (string): if `wan_type`==`lte`
        lte_auth (LteAuthEnum): if `wan_type`==`lte`
        lte_backup (bool): TODO: type description here.
        lte_password (string): if `wan_type`==`lte`
        lte_username (string): if `wan_type`==`lte`
        mtu (int): TODO: type description here.
        name (string): name that we'll use to derive config
        networks (list of string): if `usage`==`lan`
        outer_vlan_id (int): for Q-in-Q
        poe_disabled (bool): TODO: type description here.
        port_network (string): if `usage`==`lan`
        preserve_dscp (bool): whether to preserve dscp when sending traffic
            over VPN (SSR-only)
        redundant (bool): if HA mode
        reth_idx (int): if HA mode
        reth_node (string): if HA mode
        speed (string): TODO: type description here.
        svr_port_range (string): For 128T only, 16385 - 65353
        traffic_shaping (TrafficShaping): TODO: type description here.
        usage (Usage1Enum): port usage name
        vlan_id (int): if WAN interface is on a VLAN
        vpn_paths (dict): TODO: type description here.
        wan_ext_ip (string): optional, if spoke should reach this port by a
            different IP
        wan_source_nat (WanSourceNat): optional, by default, source-NAT is
            performed on all WAN Ports using the interface-ip
        wan_type (WanTypeEnum): if `usage`==`wan`

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "usage": 'usage',
        "description": 'description',
        "disable_autoneg": 'disable_autoneg',
        "dsl_config": 'dsl_config',
        "duplex": 'duplex',
        "ip_config": 'ip_config',
        "lte_apn": 'lte_apn',
        "lte_auth": 'lte_auth',
        "lte_backup": 'lte_backup',
        "lte_password": 'lte_password',
        "lte_username": 'lte_username',
        "mtu": 'mtu',
        "name": 'name',
        "networks": 'networks',
        "outer_vlan_id": 'outer_vlan_id',
        "poe_disabled": 'poe_disabled',
        "port_network": 'port_network',
        "preserve_dscp": 'preserve_dscp',
        "redundant": 'redundant',
        "reth_idx": 'reth_idx',
        "reth_node": 'reth_node',
        "speed": 'speed',
        "svr_port_range": 'svr_port_range',
        "traffic_shaping": 'traffic_shaping',
        "vlan_id": 'vlan_id',
        "vpn_paths": 'vpn_paths',
        "wan_ext_ip": 'wan_ext_ip',
        "wan_source_nat": 'wan_source_nat',
        "wan_type": 'wan_type'
    }

    _optionals = [
        'description',
        'disable_autoneg',
        'dsl_config',
        'duplex',
        'ip_config',
        'lte_apn',
        'lte_auth',
        'lte_backup',
        'lte_password',
        'lte_username',
        'mtu',
        'name',
        'networks',
        'outer_vlan_id',
        'poe_disabled',
        'port_network',
        'preserve_dscp',
        'redundant',
        'reth_idx',
        'reth_node',
        'speed',
        'svr_port_range',
        'traffic_shaping',
        'vlan_id',
        'vpn_paths',
        'wan_ext_ip',
        'wan_source_nat',
        'wan_type',
    ]

    _nullables = [
        'svr_port_range',
    ]

    def __init__(self,
                 usage=None,
                 description=APIHelper.SKIP,
                 disable_autoneg=False,
                 dsl_config=APIHelper.SKIP,
                 duplex='auto',
                 ip_config=APIHelper.SKIP,
                 lte_apn=APIHelper.SKIP,
                 lte_auth='none',
                 lte_backup=APIHelper.SKIP,
                 lte_password=APIHelper.SKIP,
                 lte_username=APIHelper.SKIP,
                 mtu=APIHelper.SKIP,
                 name=APIHelper.SKIP,
                 networks=APIHelper.SKIP,
                 outer_vlan_id=APIHelper.SKIP,
                 poe_disabled=False,
                 port_network=APIHelper.SKIP,
                 preserve_dscp=True,
                 redundant=APIHelper.SKIP,
                 reth_idx=APIHelper.SKIP,
                 reth_node=APIHelper.SKIP,
                 speed='auto',
                 svr_port_range=APIHelper.SKIP,
                 traffic_shaping=APIHelper.SKIP,
                 vlan_id=APIHelper.SKIP,
                 vpn_paths=APIHelper.SKIP,
                 wan_ext_ip=APIHelper.SKIP,
                 wan_source_nat=APIHelper.SKIP,
                 wan_type='broadband'):
        """Constructor for the PortConfig class"""

        # Initialize members of the class
        if description is not APIHelper.SKIP:
            self.description = description 
        self.disable_autoneg = disable_autoneg 
        if dsl_config is not APIHelper.SKIP:
            self.dsl_config = dsl_config 
        self.duplex = duplex 
        if ip_config is not APIHelper.SKIP:
            self.ip_config = ip_config 
        if lte_apn is not APIHelper.SKIP:
            self.lte_apn = lte_apn 
        self.lte_auth = lte_auth 
        if lte_backup is not APIHelper.SKIP:
            self.lte_backup = lte_backup 
        if lte_password is not APIHelper.SKIP:
            self.lte_password = lte_password 
        if lte_username is not APIHelper.SKIP:
            self.lte_username = lte_username 
        if mtu is not APIHelper.SKIP:
            self.mtu = mtu 
        if name is not APIHelper.SKIP:
            self.name = name 
        if networks is not APIHelper.SKIP:
            self.networks = networks 
        if outer_vlan_id is not APIHelper.SKIP:
            self.outer_vlan_id = outer_vlan_id 
        self.poe_disabled = poe_disabled 
        if port_network is not APIHelper.SKIP:
            self.port_network = port_network 
        self.preserve_dscp = preserve_dscp 
        if redundant is not APIHelper.SKIP:
            self.redundant = redundant 
        if reth_idx is not APIHelper.SKIP:
            self.reth_idx = reth_idx 
        if reth_node is not APIHelper.SKIP:
            self.reth_node = reth_node 
        self.speed = speed 
        if svr_port_range is not APIHelper.SKIP:
            self.svr_port_range = svr_port_range 
        if traffic_shaping is not APIHelper.SKIP:
            self.traffic_shaping = traffic_shaping 
        self.usage = usage 
        if vlan_id is not APIHelper.SKIP:
            self.vlan_id = vlan_id 
        if vpn_paths is not APIHelper.SKIP:
            self.vpn_paths = vpn_paths 
        if wan_ext_ip is not APIHelper.SKIP:
            self.wan_ext_ip = wan_ext_ip 
        if wan_source_nat is not APIHelper.SKIP:
            self.wan_source_nat = wan_source_nat 
        self.wan_type = wan_type 

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

        usage = dictionary.get("usage") if dictionary.get("usage") else None
        description = dictionary.get("description") if dictionary.get("description") else APIHelper.SKIP
        disable_autoneg = dictionary.get("disable_autoneg") if dictionary.get("disable_autoneg") else False
        dsl_config = DslConfig.from_dictionary(dictionary.get('dsl_config')) if 'dsl_config' in dictionary.keys() else APIHelper.SKIP
        duplex = dictionary.get("duplex") if dictionary.get("duplex") else 'auto'
        ip_config = JunosIpConfigGateway.from_dictionary(dictionary.get('ip_config')) if 'ip_config' in dictionary.keys() else APIHelper.SKIP
        lte_apn = dictionary.get("lte_apn") if dictionary.get("lte_apn") else APIHelper.SKIP
        lte_auth = dictionary.get("lte_auth") if dictionary.get("lte_auth") else 'none'
        lte_backup = dictionary.get("lte_backup") if "lte_backup" in dictionary.keys() else APIHelper.SKIP
        lte_password = dictionary.get("lte_password") if dictionary.get("lte_password") else APIHelper.SKIP
        lte_username = dictionary.get("lte_username") if dictionary.get("lte_username") else APIHelper.SKIP
        mtu = dictionary.get("mtu") if dictionary.get("mtu") else APIHelper.SKIP
        name = dictionary.get("name") if dictionary.get("name") else APIHelper.SKIP
        networks = dictionary.get("networks") if dictionary.get("networks") else APIHelper.SKIP
        outer_vlan_id = dictionary.get("outer_vlan_id") if dictionary.get("outer_vlan_id") else APIHelper.SKIP
        poe_disabled = dictionary.get("poe_disabled") if dictionary.get("poe_disabled") else False
        port_network = dictionary.get("port_network") if dictionary.get("port_network") else APIHelper.SKIP
        preserve_dscp = dictionary.get("preserve_dscp") if dictionary.get("preserve_dscp") else True
        redundant = dictionary.get("redundant") if "redundant" in dictionary.keys() else APIHelper.SKIP
        reth_idx = dictionary.get("reth_idx") if dictionary.get("reth_idx") else APIHelper.SKIP
        reth_node = dictionary.get("reth_node") if dictionary.get("reth_node") else APIHelper.SKIP
        speed = dictionary.get("speed") if dictionary.get("speed") else 'auto'
        svr_port_range = dictionary.get("svr_port_range") if "svr_port_range" in dictionary.keys() else APIHelper.SKIP
        traffic_shaping = TrafficShaping.from_dictionary(dictionary.get('traffic_shaping')) if 'traffic_shaping' in dictionary.keys() else APIHelper.SKIP
        vlan_id = dictionary.get("vlan_id") if dictionary.get("vlan_id") else APIHelper.SKIP
        vpn_paths = VpnPaths.from_dictionary(dictionary.get('vpn_paths')) if 'vpn_paths' in dictionary.keys() else APIHelper.SKIP
        wan_ext_ip = dictionary.get("wan_ext_ip") if dictionary.get("wan_ext_ip") else APIHelper.SKIP
        wan_source_nat = WanSourceNat.from_dictionary(dictionary.get('wan_source_nat')) if 'wan_source_nat' in dictionary.keys() else APIHelper.SKIP
        wan_type = dictionary.get("wan_type") if dictionary.get("wan_type") else 'broadband'
        # Return an object of this model
        return cls(usage,
                   description,
                   disable_autoneg,
                   dsl_config,
                   duplex,
                   ip_config,
                   lte_apn,
                   lte_auth,
                   lte_backup,
                   lte_password,
                   lte_username,
                   mtu,
                   name,
                   networks,
                   outer_vlan_id,
                   poe_disabled,
                   port_network,
                   preserve_dscp,
                   redundant,
                   reth_idx,
                   reth_node,
                   speed,
                   svr_port_range,
                   traffic_shaping,
                   vlan_id,
                   vpn_paths,
                   wan_ext_ip,
                   wan_source_nat,
                   wan_type)
