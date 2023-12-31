# -*- coding: utf-8 -*-

"""
mistapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from mistapi.api_helper import APIHelper
from mistapi.models.acl_tags import AclTags
from mistapi.models.extra_routes_1 import ExtraRoutes1
from mistapi.models.junos_acl_policies import JunosAclPolicies
from mistapi.models.junos_dhcp_snooping import JunosDhcpSnooping
from mistapi.models.junos_dhcpd import JunosDhcpd
from mistapi.models.junos_evpn_config import JunosEvpnConfig
from mistapi.models.junos_ip_config import JunosIpConfig
from mistapi.models.junos_networks import JunosNetworks
from mistapi.models.junos_oob_ip_config import JunosOobIpConfig
from mistapi.models.junos_ospf_config import JunosOspfConfig
from mistapi.models.junos_other_ip_configs import JunosOtherIpConfigs
from mistapi.models.junos_port_config import JunosPortConfig
from mistapi.models.junos_radius_config import JunosRadiusConfig
from mistapi.models.junos_vrf_config import JunosVrfConfig
from mistapi.models.junos_vrrp_config import JunosVrrpConfig
from mistapi.models.port_mirroring_1 import PortMirroring1
from mistapi.models.port_usages import PortUsages
from mistapi.models.switch_mgmt import SwitchMgmt
from mistapi.models.virtual_chassis import VirtualChassis


class DeviceSwitch(object):

    """Implementation of the 'device_switch' model.

    Switch Configuration
    You can configure `port_usages` and `networks` settings at the device
    level, but most of the time it's better use the Site Setting to achieve
    better consistency and be able to re-use the same settings across switches
    entries defined here will "replace" those defined in Site Setting/Network
    Template

    Attributes:
        acl_policies (list of JunosAclPolicies): TODO: type description here.
        acl_tags (AclTags): ACL Tags to identify traffic source or
            destination. Key name is the tag name
        additional_config_cmds (list of string): TODO: type description here.
        created_time (float): TODO: type description here.
        deviceprofile_id (uuid|string): TODO: type description here.
        dhcp_config (JunosDhcpd): if DHCP Server/Relay is intended. The
            property key is the network name
        dhcp_snooping (JunosDhcpSnooping): TODO: type description here.
        disable_auto_config (bool): for a claimed switch, we control the
            configs by default. This option (disables the behavior)
        dns_servers (list of string): Global dns settings. To keep
            compatibility, dns settings in `ip_config` and `oob_ip_config`
            will overwrite this setting
        dns_suffix (list of string): Global dns settings. To keep
            compatibility, dns settings in `ip_config` and `oob_ip_config`
            will overwrite this setting
        evpn_config (JunosEvpnConfig): EVPN Junos settings
        extra_routes (dict): The property key is the network name or a CIDR
        id (uuid|string): TODO: type description here.
        image_1_url (string): TODO: type description here.
        image_2_url (string): TODO: type description here.
        image_3_url (string): TODO: type description here.
        ip_config (JunosIpConfig): Junos IP Config
        managed (bool): for an adopted switch, we don’t overwrite their
            existing configs automatically
        modified_time (float): TODO: type description here.
        name (string): TODO: type description here.
        networks (JunosNetworks): A network represents a network segment. It
            can either represent a VLAN (then usually ties to a L3 subnet),
            optionally associate it with a subnet which can later be used to
            create addition routes. Used for ports doing `family
            ethernet-switching`. It can also be a pure L3-subnet that can then
            be used against a port that with `family inet`.
        notes (string): TODO: type description here.
        ntp_servers (list of string): list of NTP servers specific to this
            device. By default, those in Site Settings will be used
        oob_ip_config (JunosOobIpConfig): Junos out-of-band (vme/em0/fxp0) IP
            config
        org_id (uuid|string): TODO: type description here.
        ospf_config (JunosOspfConfig): Junos OSPF config
        other_ip_configs (dict): The property key is the network name
        port_config (dict): The property key is the port name or range (e.g.
            "ge-0/0/0-10")
        port_mirroring (PortMirroring1): TODO: type description here.
        port_usages (PortUsages): The property key is the port profile name
        radius_config (JunosRadiusConfig): Junos Radius config
        role (Role4Enum): TODO: type description here.
        router_id (string): used for OSPF / BGP / EVPN
        site_id (uuid|string): TODO: type description here.
        switch_mgmt (SwitchMgmt): TODO: type description here.
        use_router_id_as_source_ip (bool): whether to use it for snmp / syslog
            / tacplus / radius
        vars (object): a dictionary of name->value, the vars can then be used
            in Wlans. This can overwrite those from Site Vars
        virtual_chassis (VirtualChassis): required for preprovisioned Virtual
            Chassis
        vrf_config (JunosVrfConfig): TODO: type description here.
        vrrp_config (JunosVrrpConfig): Junos VRRP config

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "acl_policies": 'acl_policies',
        "acl_tags": 'acl_tags',
        "additional_config_cmds": 'additional_config_cmds',
        "created_time": 'created_time',
        "deviceprofile_id": 'deviceprofile_id',
        "dhcp_config": 'dhcp_config',
        "dhcp_snooping": 'dhcp_snooping',
        "disable_auto_config": 'disable_auto_config',
        "dns_servers": 'dns_servers',
        "dns_suffix": 'dns_suffix',
        "evpn_config": 'evpn_config',
        "extra_routes": 'extra_routes',
        "id": 'id',
        "image_1_url": 'image1_url',
        "image_2_url": 'image2_url',
        "image_3_url": 'image3_url',
        "ip_config": 'ip_config',
        "managed": 'managed',
        "modified_time": 'modified_time',
        "name": 'name',
        "networks": 'networks',
        "notes": 'notes',
        "ntp_servers": 'ntp_servers',
        "oob_ip_config": 'oob_ip_config',
        "org_id": 'org_id',
        "ospf_config": 'ospf_config',
        "other_ip_configs": 'other_ip_configs',
        "port_config": 'port_config',
        "port_mirroring": 'port_mirroring',
        "port_usages": 'port_usages',
        "radius_config": 'radius_config',
        "role": 'role',
        "router_id": 'router_id',
        "site_id": 'site_id',
        "switch_mgmt": 'switch_mgmt',
        "use_router_id_as_source_ip": 'use_router_id_as_source_ip',
        "vars": 'vars',
        "virtual_chassis": 'virtual_chassis',
        "vrf_config": 'vrf_config',
        "vrrp_config": 'vrrp_config'
    }

    _optionals = [
        'acl_policies',
        'acl_tags',
        'additional_config_cmds',
        'created_time',
        'deviceprofile_id',
        'dhcp_config',
        'dhcp_snooping',
        'disable_auto_config',
        'dns_servers',
        'dns_suffix',
        'evpn_config',
        'extra_routes',
        'id',
        'image_1_url',
        'image_2_url',
        'image_3_url',
        'ip_config',
        'managed',
        'modified_time',
        'name',
        'networks',
        'notes',
        'ntp_servers',
        'oob_ip_config',
        'org_id',
        'ospf_config',
        'other_ip_configs',
        'port_config',
        'port_mirroring',
        'port_usages',
        'radius_config',
        'role',
        'router_id',
        'site_id',
        'switch_mgmt',
        'use_router_id_as_source_ip',
        'vars',
        'virtual_chassis',
        'vrf_config',
        'vrrp_config',
    ]

    _nullables = [
        'image_1_url',
        'image_2_url',
        'image_3_url',
    ]

    def __init__(self,
                 acl_policies=APIHelper.SKIP,
                 acl_tags=APIHelper.SKIP,
                 additional_config_cmds=APIHelper.SKIP,
                 created_time=APIHelper.SKIP,
                 deviceprofile_id=APIHelper.SKIP,
                 dhcp_config=APIHelper.SKIP,
                 dhcp_snooping=APIHelper.SKIP,
                 disable_auto_config=False,
                 dns_servers=APIHelper.SKIP,
                 dns_suffix=APIHelper.SKIP,
                 evpn_config=APIHelper.SKIP,
                 extra_routes=APIHelper.SKIP,
                 id=APIHelper.SKIP,
                 image_1_url=APIHelper.SKIP,
                 image_2_url=APIHelper.SKIP,
                 image_3_url=APIHelper.SKIP,
                 ip_config=APIHelper.SKIP,
                 managed=False,
                 modified_time=APIHelper.SKIP,
                 name=APIHelper.SKIP,
                 networks=APIHelper.SKIP,
                 notes=APIHelper.SKIP,
                 ntp_servers=APIHelper.SKIP,
                 oob_ip_config=APIHelper.SKIP,
                 org_id=APIHelper.SKIP,
                 ospf_config=APIHelper.SKIP,
                 other_ip_configs=APIHelper.SKIP,
                 port_config=APIHelper.SKIP,
                 port_mirroring=APIHelper.SKIP,
                 port_usages=APIHelper.SKIP,
                 radius_config=APIHelper.SKIP,
                 role='access',
                 router_id=APIHelper.SKIP,
                 site_id=APIHelper.SKIP,
                 switch_mgmt=APIHelper.SKIP,
                 use_router_id_as_source_ip=False,
                 vars=APIHelper.SKIP,
                 virtual_chassis=APIHelper.SKIP,
                 vrf_config=APIHelper.SKIP,
                 vrrp_config=APIHelper.SKIP):
        """Constructor for the DeviceSwitch class"""

        # Initialize members of the class
        if acl_policies is not APIHelper.SKIP:
            self.acl_policies = acl_policies 
        if acl_tags is not APIHelper.SKIP:
            self.acl_tags = acl_tags 
        if additional_config_cmds is not APIHelper.SKIP:
            self.additional_config_cmds = additional_config_cmds 
        if created_time is not APIHelper.SKIP:
            self.created_time = created_time 
        if deviceprofile_id is not APIHelper.SKIP:
            self.deviceprofile_id = deviceprofile_id 
        if dhcp_config is not APIHelper.SKIP:
            self.dhcp_config = dhcp_config 
        if dhcp_snooping is not APIHelper.SKIP:
            self.dhcp_snooping = dhcp_snooping 
        self.disable_auto_config = disable_auto_config 
        if dns_servers is not APIHelper.SKIP:
            self.dns_servers = dns_servers 
        if dns_suffix is not APIHelper.SKIP:
            self.dns_suffix = dns_suffix 
        if evpn_config is not APIHelper.SKIP:
            self.evpn_config = evpn_config 
        if extra_routes is not APIHelper.SKIP:
            self.extra_routes = extra_routes 
        if id is not APIHelper.SKIP:
            self.id = id 
        if image_1_url is not APIHelper.SKIP:
            self.image_1_url = image_1_url 
        if image_2_url is not APIHelper.SKIP:
            self.image_2_url = image_2_url 
        if image_3_url is not APIHelper.SKIP:
            self.image_3_url = image_3_url 
        if ip_config is not APIHelper.SKIP:
            self.ip_config = ip_config 
        self.managed = managed 
        if modified_time is not APIHelper.SKIP:
            self.modified_time = modified_time 
        if name is not APIHelper.SKIP:
            self.name = name 
        if networks is not APIHelper.SKIP:
            self.networks = networks 
        if notes is not APIHelper.SKIP:
            self.notes = notes 
        if ntp_servers is not APIHelper.SKIP:
            self.ntp_servers = ntp_servers 
        if oob_ip_config is not APIHelper.SKIP:
            self.oob_ip_config = oob_ip_config 
        if org_id is not APIHelper.SKIP:
            self.org_id = org_id 
        if ospf_config is not APIHelper.SKIP:
            self.ospf_config = ospf_config 
        if other_ip_configs is not APIHelper.SKIP:
            self.other_ip_configs = other_ip_configs 
        if port_config is not APIHelper.SKIP:
            self.port_config = port_config 
        if port_mirroring is not APIHelper.SKIP:
            self.port_mirroring = port_mirroring 
        if port_usages is not APIHelper.SKIP:
            self.port_usages = port_usages 
        if radius_config is not APIHelper.SKIP:
            self.radius_config = radius_config 
        self.role = role 
        if router_id is not APIHelper.SKIP:
            self.router_id = router_id 
        if site_id is not APIHelper.SKIP:
            self.site_id = site_id 
        if switch_mgmt is not APIHelper.SKIP:
            self.switch_mgmt = switch_mgmt 
        self.use_router_id_as_source_ip = use_router_id_as_source_ip 
        if vars is not APIHelper.SKIP:
            self.vars = vars 
        if virtual_chassis is not APIHelper.SKIP:
            self.virtual_chassis = virtual_chassis 
        if vrf_config is not APIHelper.SKIP:
            self.vrf_config = vrf_config 
        if vrrp_config is not APIHelper.SKIP:
            self.vrrp_config = vrrp_config 

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

        acl_policies = None
        if dictionary.get('acl_policies') is not None:
            acl_policies = [JunosAclPolicies.from_dictionary(x) for x in dictionary.get('acl_policies')]
        else:
            acl_policies = APIHelper.SKIP
        acl_tags = AclTags.from_dictionary(dictionary.get('acl_tags')) if 'acl_tags' in dictionary.keys() else APIHelper.SKIP
        additional_config_cmds = dictionary.get("additional_config_cmds") if dictionary.get("additional_config_cmds") else APIHelper.SKIP
        created_time = dictionary.get("created_time") if dictionary.get("created_time") else APIHelper.SKIP
        deviceprofile_id = dictionary.get("deviceprofile_id") if dictionary.get("deviceprofile_id") else APIHelper.SKIP
        dhcp_config = JunosDhcpd.from_dictionary(dictionary.get('dhcp_config')) if 'dhcp_config' in dictionary.keys() else APIHelper.SKIP
        dhcp_snooping = JunosDhcpSnooping.from_dictionary(dictionary.get('dhcp_snooping')) if 'dhcp_snooping' in dictionary.keys() else APIHelper.SKIP
        disable_auto_config = dictionary.get("disable_auto_config") if dictionary.get("disable_auto_config") else False
        dns_servers = dictionary.get("dns_servers") if dictionary.get("dns_servers") else APIHelper.SKIP
        dns_suffix = dictionary.get("dns_suffix") if dictionary.get("dns_suffix") else APIHelper.SKIP
        evpn_config = JunosEvpnConfig.from_dictionary(dictionary.get('evpn_config')) if 'evpn_config' in dictionary.keys() else APIHelper.SKIP
        extra_routes = ExtraRoutes1.from_dictionary(dictionary.get('extra_routes')) if 'extra_routes' in dictionary.keys() else APIHelper.SKIP
        id = dictionary.get("id") if dictionary.get("id") else APIHelper.SKIP
        image_1_url = dictionary.get("image1_url") if "image1_url" in dictionary.keys() else APIHelper.SKIP
        image_2_url = dictionary.get("image2_url") if "image2_url" in dictionary.keys() else APIHelper.SKIP
        image_3_url = dictionary.get("image3_url") if "image3_url" in dictionary.keys() else APIHelper.SKIP
        ip_config = JunosIpConfig.from_dictionary(dictionary.get('ip_config')) if 'ip_config' in dictionary.keys() else APIHelper.SKIP
        managed = dictionary.get("managed") if dictionary.get("managed") else False
        modified_time = dictionary.get("modified_time") if dictionary.get("modified_time") else APIHelper.SKIP
        name = dictionary.get("name") if dictionary.get("name") else APIHelper.SKIP
        networks = JunosNetworks.from_dictionary(dictionary.get('networks')) if 'networks' in dictionary.keys() else APIHelper.SKIP
        notes = dictionary.get("notes") if dictionary.get("notes") else APIHelper.SKIP
        ntp_servers = dictionary.get("ntp_servers") if dictionary.get("ntp_servers") else APIHelper.SKIP
        oob_ip_config = JunosOobIpConfig.from_dictionary(dictionary.get('oob_ip_config')) if 'oob_ip_config' in dictionary.keys() else APIHelper.SKIP
        org_id = dictionary.get("org_id") if dictionary.get("org_id") else APIHelper.SKIP
        ospf_config = JunosOspfConfig.from_dictionary(dictionary.get('ospf_config')) if 'ospf_config' in dictionary.keys() else APIHelper.SKIP
        other_ip_configs = JunosOtherIpConfigs.from_dictionary(dictionary.get('other_ip_configs')) if 'other_ip_configs' in dictionary.keys() else APIHelper.SKIP
        port_config = JunosPortConfig.from_dictionary(dictionary.get('port_config')) if 'port_config' in dictionary.keys() else APIHelper.SKIP
        port_mirroring = PortMirroring1.from_dictionary(dictionary.get('port_mirroring')) if 'port_mirroring' in dictionary.keys() else APIHelper.SKIP
        port_usages = PortUsages.from_dictionary(dictionary.get('port_usages')) if 'port_usages' in dictionary.keys() else APIHelper.SKIP
        radius_config = JunosRadiusConfig.from_dictionary(dictionary.get('radius_config')) if 'radius_config' in dictionary.keys() else APIHelper.SKIP
        role = dictionary.get("role") if dictionary.get("role") else 'access'
        router_id = dictionary.get("router_id") if dictionary.get("router_id") else APIHelper.SKIP
        site_id = dictionary.get("site_id") if dictionary.get("site_id") else APIHelper.SKIP
        switch_mgmt = SwitchMgmt.from_dictionary(dictionary.get('switch_mgmt')) if 'switch_mgmt' in dictionary.keys() else APIHelper.SKIP
        use_router_id_as_source_ip = dictionary.get("use_router_id_as_source_ip") if dictionary.get("use_router_id_as_source_ip") else False
        vars = dictionary.get("vars") if dictionary.get("vars") else APIHelper.SKIP
        virtual_chassis = VirtualChassis.from_dictionary(dictionary.get('virtual_chassis')) if 'virtual_chassis' in dictionary.keys() else APIHelper.SKIP
        vrf_config = JunosVrfConfig.from_dictionary(dictionary.get('vrf_config')) if 'vrf_config' in dictionary.keys() else APIHelper.SKIP
        vrrp_config = JunosVrrpConfig.from_dictionary(dictionary.get('vrrp_config')) if 'vrrp_config' in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(acl_policies,
                   acl_tags,
                   additional_config_cmds,
                   created_time,
                   deviceprofile_id,
                   dhcp_config,
                   dhcp_snooping,
                   disable_auto_config,
                   dns_servers,
                   dns_suffix,
                   evpn_config,
                   extra_routes,
                   id,
                   image_1_url,
                   image_2_url,
                   image_3_url,
                   ip_config,
                   managed,
                   modified_time,
                   name,
                   networks,
                   notes,
                   ntp_servers,
                   oob_ip_config,
                   org_id,
                   ospf_config,
                   other_ip_configs,
                   port_config,
                   port_mirroring,
                   port_usages,
                   radius_config,
                   role,
                   router_id,
                   site_id,
                   switch_mgmt,
                   use_router_id_as_source_ip,
                   vars,
                   virtual_chassis,
                   vrf_config,
                   vrrp_config)
