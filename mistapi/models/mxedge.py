# -*- coding: utf-8 -*-

"""
mistapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from mistapi.api_helper import APIHelper
from mistapi.models.fips import Fips
from mistapi.models.mxedge_mgmt import MxedgeMgmt
from mistapi.models.oob_ip_config import OobIpConfig
from mistapi.models.proxy_1 import Proxy1
from mistapi.models.site_tunterm_monitoring import SiteTuntermMonitoring
from mistapi.models.tunterm_dhcpd_config_1 import TuntermDhcpdConfig1
from mistapi.models.tunterm_extra_routes import TuntermExtraRoutes
from mistapi.models.tunterm_igmp_snooping_config import TuntermIgmpSnoopingConfig
from mistapi.models.tunterm_ip_config import TuntermIpConfig
from mistapi.models.tunterm_other_ip_configs import TuntermOtherIpConfigs
from mistapi.models.tunterm_port_config import TuntermPortConfig
from mistapi.models.tunterm_switch_config import TuntermSwitchConfig
from mistapi.models.versions import Versions


class Mxedge(object):

    """Implementation of the 'mxedge' model.

    MxEdge

    Attributes:
        created_time (float): TODO: type description here.
        fips (Fips): FIPS configuration
        for_site (bool): TODO: type description here.
        id (uuid|string): TODO: type description here.
        magic (string): TODO: type description here.
        model (string): TODO: type description here.
        modified_time (float): TODO: type description here.
        mxagent_registered (bool): TODO: type description here.
        mxcluster_id (uuid|string): MxCluster this MxEdge belongs to
        mxedge_mgmt (MxedgeMgmt): TODO: type description here.
        name (string): TODO: type description here.
        note (string): TODO: type description here.
        ntp_servers (list of string): TODO: type description here.
        oob_ip_config (OobIpConfig): ip configuration of the Mist Edge
            out-of-band management interface
        org_id (uuid|string): TODO: type description here.
        proxy (Proxy1): TODO: type description here.
        services (list of string): list of services to run, tunterm only for
            now
        site_id (uuid|string): TODO: type description here.
        tunterm_dhcpd_config (TuntermDhcpdConfig1): global and per-VLAN. The
            property key is the VLAN ID
        tunterm_extra_routes (dict): The property key is a CIDR
        tunterm_igmp_snooping_config (TuntermIgmpSnoopingConfig): TODO: type
            description here.
        tunterm_ip_config (TuntermIpConfig): ip configuration of the Mist
            Tunnel interface
        tunterm_monitoring (list of SiteTuntermMonitoring): TODO: type
            description here.
        tunterm_other_ip_configs (dict): ip configs by VLAN ID. The property
            key is the VLAN ID
        tunterm_port_config (TuntermPortConfig): ethernet port configurations
        tunterm_registered (bool): TODO: type description here.
        tunterm_switch_config (TuntermSwitchConfig): if custom vlan settings
            are desired
        versions (Versions): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "model": 'model',
        "name": 'name',
        "created_time": 'created_time',
        "fips": 'fips',
        "for_site": 'for_site',
        "id": 'id',
        "magic": 'magic',
        "modified_time": 'modified_time',
        "mxagent_registered": 'mxagent_registered',
        "mxcluster_id": 'mxcluster_id',
        "mxedge_mgmt": 'mxedge_mgmt',
        "note": 'note',
        "ntp_servers": 'ntp_servers',
        "oob_ip_config": 'oob_ip_config',
        "org_id": 'org_id',
        "proxy": 'proxy',
        "services": 'services',
        "site_id": 'site_id',
        "tunterm_dhcpd_config": 'tunterm_dhcpd_config',
        "tunterm_extra_routes": 'tunterm_extra_routes',
        "tunterm_igmp_snooping_config": 'tunterm_igmp_snooping_config',
        "tunterm_ip_config": 'tunterm_ip_config',
        "tunterm_monitoring": 'tunterm_monitoring',
        "tunterm_other_ip_configs": 'tunterm_other_ip_configs',
        "tunterm_port_config": 'tunterm_port_config',
        "tunterm_registered": 'tunterm_registered',
        "tunterm_switch_config": 'tunterm_switch_config',
        "versions": 'versions'
    }

    _optionals = [
        'created_time',
        'fips',
        'for_site',
        'id',
        'magic',
        'modified_time',
        'mxagent_registered',
        'mxcluster_id',
        'mxedge_mgmt',
        'note',
        'ntp_servers',
        'oob_ip_config',
        'org_id',
        'proxy',
        'services',
        'site_id',
        'tunterm_dhcpd_config',
        'tunterm_extra_routes',
        'tunterm_igmp_snooping_config',
        'tunterm_ip_config',
        'tunterm_monitoring',
        'tunterm_other_ip_configs',
        'tunterm_port_config',
        'tunterm_registered',
        'tunterm_switch_config',
        'versions',
    ]

    def __init__(self,
                 model=None,
                 name=None,
                 created_time=APIHelper.SKIP,
                 fips=APIHelper.SKIP,
                 for_site=APIHelper.SKIP,
                 id=APIHelper.SKIP,
                 magic=APIHelper.SKIP,
                 modified_time=APIHelper.SKIP,
                 mxagent_registered=APIHelper.SKIP,
                 mxcluster_id=APIHelper.SKIP,
                 mxedge_mgmt=APIHelper.SKIP,
                 note=APIHelper.SKIP,
                 ntp_servers=APIHelper.SKIP,
                 oob_ip_config=APIHelper.SKIP,
                 org_id=APIHelper.SKIP,
                 proxy=APIHelper.SKIP,
                 services=APIHelper.SKIP,
                 site_id=APIHelper.SKIP,
                 tunterm_dhcpd_config=APIHelper.SKIP,
                 tunterm_extra_routes=APIHelper.SKIP,
                 tunterm_igmp_snooping_config=APIHelper.SKIP,
                 tunterm_ip_config=APIHelper.SKIP,
                 tunterm_monitoring=APIHelper.SKIP,
                 tunterm_other_ip_configs=APIHelper.SKIP,
                 tunterm_port_config=APIHelper.SKIP,
                 tunterm_registered=APIHelper.SKIP,
                 tunterm_switch_config=APIHelper.SKIP,
                 versions=APIHelper.SKIP):
        """Constructor for the Mxedge class"""

        # Initialize members of the class
        if created_time is not APIHelper.SKIP:
            self.created_time = created_time 
        if fips is not APIHelper.SKIP:
            self.fips = fips 
        if for_site is not APIHelper.SKIP:
            self.for_site = for_site 
        if id is not APIHelper.SKIP:
            self.id = id 
        if magic is not APIHelper.SKIP:
            self.magic = magic 
        self.model = model 
        if modified_time is not APIHelper.SKIP:
            self.modified_time = modified_time 
        if mxagent_registered is not APIHelper.SKIP:
            self.mxagent_registered = mxagent_registered 
        if mxcluster_id is not APIHelper.SKIP:
            self.mxcluster_id = mxcluster_id 
        if mxedge_mgmt is not APIHelper.SKIP:
            self.mxedge_mgmt = mxedge_mgmt 
        self.name = name 
        if note is not APIHelper.SKIP:
            self.note = note 
        if ntp_servers is not APIHelper.SKIP:
            self.ntp_servers = ntp_servers 
        if oob_ip_config is not APIHelper.SKIP:
            self.oob_ip_config = oob_ip_config 
        if org_id is not APIHelper.SKIP:
            self.org_id = org_id 
        if proxy is not APIHelper.SKIP:
            self.proxy = proxy 
        if services is not APIHelper.SKIP:
            self.services = services 
        if site_id is not APIHelper.SKIP:
            self.site_id = site_id 
        if tunterm_dhcpd_config is not APIHelper.SKIP:
            self.tunterm_dhcpd_config = tunterm_dhcpd_config 
        if tunterm_extra_routes is not APIHelper.SKIP:
            self.tunterm_extra_routes = tunterm_extra_routes 
        if tunterm_igmp_snooping_config is not APIHelper.SKIP:
            self.tunterm_igmp_snooping_config = tunterm_igmp_snooping_config 
        if tunterm_ip_config is not APIHelper.SKIP:
            self.tunterm_ip_config = tunterm_ip_config 
        if tunterm_monitoring is not APIHelper.SKIP:
            self.tunterm_monitoring = tunterm_monitoring 
        if tunterm_other_ip_configs is not APIHelper.SKIP:
            self.tunterm_other_ip_configs = tunterm_other_ip_configs 
        if tunterm_port_config is not APIHelper.SKIP:
            self.tunterm_port_config = tunterm_port_config 
        if tunterm_registered is not APIHelper.SKIP:
            self.tunterm_registered = tunterm_registered 
        if tunterm_switch_config is not APIHelper.SKIP:
            self.tunterm_switch_config = tunterm_switch_config 
        if versions is not APIHelper.SKIP:
            self.versions = versions 

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

        model = dictionary.get("model") if dictionary.get("model") else None
        name = dictionary.get("name") if dictionary.get("name") else None
        created_time = dictionary.get("created_time") if dictionary.get("created_time") else APIHelper.SKIP
        fips = Fips.from_dictionary(dictionary.get('fips')) if 'fips' in dictionary.keys() else APIHelper.SKIP
        for_site = dictionary.get("for_site") if "for_site" in dictionary.keys() else APIHelper.SKIP
        id = dictionary.get("id") if dictionary.get("id") else APIHelper.SKIP
        magic = dictionary.get("magic") if dictionary.get("magic") else APIHelper.SKIP
        modified_time = dictionary.get("modified_time") if dictionary.get("modified_time") else APIHelper.SKIP
        mxagent_registered = dictionary.get("mxagent_registered") if "mxagent_registered" in dictionary.keys() else APIHelper.SKIP
        mxcluster_id = dictionary.get("mxcluster_id") if dictionary.get("mxcluster_id") else APIHelper.SKIP
        mxedge_mgmt = MxedgeMgmt.from_dictionary(dictionary.get('mxedge_mgmt')) if 'mxedge_mgmt' in dictionary.keys() else APIHelper.SKIP
        note = dictionary.get("note") if dictionary.get("note") else APIHelper.SKIP
        ntp_servers = dictionary.get("ntp_servers") if dictionary.get("ntp_servers") else APIHelper.SKIP
        oob_ip_config = OobIpConfig.from_dictionary(dictionary.get('oob_ip_config')) if 'oob_ip_config' in dictionary.keys() else APIHelper.SKIP
        org_id = dictionary.get("org_id") if dictionary.get("org_id") else APIHelper.SKIP
        proxy = Proxy1.from_dictionary(dictionary.get('proxy')) if 'proxy' in dictionary.keys() else APIHelper.SKIP
        services = dictionary.get("services") if dictionary.get("services") else APIHelper.SKIP
        site_id = dictionary.get("site_id") if dictionary.get("site_id") else APIHelper.SKIP
        tunterm_dhcpd_config = TuntermDhcpdConfig1.from_dictionary(dictionary.get('tunterm_dhcpd_config')) if 'tunterm_dhcpd_config' in dictionary.keys() else APIHelper.SKIP
        tunterm_extra_routes = TuntermExtraRoutes.from_dictionary(dictionary.get('tunterm_extra_routes')) if 'tunterm_extra_routes' in dictionary.keys() else APIHelper.SKIP
        tunterm_igmp_snooping_config = TuntermIgmpSnoopingConfig.from_dictionary(dictionary.get('tunterm_igmp_snooping_config')) if 'tunterm_igmp_snooping_config' in dictionary.keys() else APIHelper.SKIP
        tunterm_ip_config = TuntermIpConfig.from_dictionary(dictionary.get('tunterm_ip_config')) if 'tunterm_ip_config' in dictionary.keys() else APIHelper.SKIP
        tunterm_monitoring = None
        if dictionary.get('tunterm_monitoring') is not None:
            tunterm_monitoring = [SiteTuntermMonitoring.from_dictionary(x) for x in dictionary.get('tunterm_monitoring')]
        else:
            tunterm_monitoring = APIHelper.SKIP
        tunterm_other_ip_configs = TuntermOtherIpConfigs.from_dictionary(dictionary.get('tunterm_other_ip_configs')) if 'tunterm_other_ip_configs' in dictionary.keys() else APIHelper.SKIP
        tunterm_port_config = TuntermPortConfig.from_dictionary(dictionary.get('tunterm_port_config')) if 'tunterm_port_config' in dictionary.keys() else APIHelper.SKIP
        tunterm_registered = dictionary.get("tunterm_registered") if "tunterm_registered" in dictionary.keys() else APIHelper.SKIP
        tunterm_switch_config = TuntermSwitchConfig.from_dictionary(dictionary.get('tunterm_switch_config')) if 'tunterm_switch_config' in dictionary.keys() else APIHelper.SKIP
        versions = Versions.from_dictionary(dictionary.get('versions')) if 'versions' in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(model,
                   name,
                   created_time,
                   fips,
                   for_site,
                   id,
                   magic,
                   modified_time,
                   mxagent_registered,
                   mxcluster_id,
                   mxedge_mgmt,
                   note,
                   ntp_servers,
                   oob_ip_config,
                   org_id,
                   proxy,
                   services,
                   site_id,
                   tunterm_dhcpd_config,
                   tunterm_extra_routes,
                   tunterm_igmp_snooping_config,
                   tunterm_ip_config,
                   tunterm_monitoring,
                   tunterm_other_ip_configs,
                   tunterm_port_config,
                   tunterm_registered,
                   tunterm_switch_config,
                   versions)
