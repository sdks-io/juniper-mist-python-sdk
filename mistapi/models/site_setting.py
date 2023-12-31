# -*- coding: utf-8 -*-

"""
mistapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from mistapi.api_helper import APIHelper
from mistapi.models.analytic import Analytic
from mistapi.models.ap_ble import ApBle
from mistapi.models.ap_led import ApLed
from mistapi.models.ap_matching_1 import ApMatching1
from mistapi.models.ap_port_config_1 import ApPortConfig1
from mistapi.models.ap_radio import ApRadio
from mistapi.models.auto_placement import AutoPlacement
from mistapi.models.auto_preemption import AutoPreemption
from mistapi.models.junos_evpn_options import JunosEvpnOptions
from mistapi.models.junos_networks import JunosNetworks
from mistapi.models.junos_ospf_areas import JunosOspfAreas
from mistapi.models.junos_port_mirroring import JunosPortMirroring
from mistapi.models.junos_radius_config import JunosRadiusConfig
from mistapi.models.junos_vrf_instance import JunosVrfInstance
from mistapi.models.junos_vrrp_group import JunosVrrpGroup
from mistapi.models.mxedge_1 import Mxedge1
from mistapi.models.mxedge_mgmt import MxedgeMgmt
from mistapi.models.port_usages_2 import PortUsages2
from mistapi.models.proxy_2 import Proxy2
from mistapi.models.remote_syslog import RemoteSyslog
from mistapi.models.rtsa import Rtsa
from mistapi.models.simple_alert import SimpleAlert
from mistapi.models.site_auto_upgrade import SiteAutoUpgrade
from mistapi.models.site_engagement import SiteEngagement
from mistapi.models.site_gateway import SiteGateway
from mistapi.models.site_mxtunnel import SiteMxtunnel
from mistapi.models.site_occupancy_analytics import SiteOccupancyAnalytics
from mistapi.models.site_rogue import SiteRogue
from mistapi.models.site_ssr import SiteSsr
from mistapi.models.site_switch import SiteSwitch
from mistapi.models.site_tunterm_monitoring import SiteTuntermMonitoring
from mistapi.models.site_wids import SiteWids
from mistapi.models.site_wifi import SiteWifi
from mistapi.models.site_zone_occupancy_alert import SiteZoneOccupancyAlert
from mistapi.models.skyatp import Skyatp
from mistapi.models.srx_app import SrxApp
from mistapi.models.status_portal import StatusPortal
from mistapi.models.switch_matching import SwitchMatching
from mistapi.models.vna import Vna
from mistapi.models.vs_instances import VsInstances
from mistapi.models.wan_vna import WanVna
from mistapi.models.wired_vna import WiredVna


class SiteSetting(object):

    """Implementation of the 'site_setting' model.

    Site Settings

    Attributes:
        additional_config_cmds (list of string): additional CLI commands to
            append to the generated switches config
        analytic (Analytic): TODO: type description here.
        ap_matching (ApMatching1): TODO: type description here.
        ap_port_config (ApPortConfig1): TODO: type description here.
        auto_placement (AutoPlacement): if we're able to determine its
            x/y/orientation, this will be populated
        auto_preemption (AutoPreemption): schedule to preempt ap’s which are
            not connected to preferred peer
        auto_upgrade (SiteAutoUpgrade): Auto Upgrade Settings
        blacklist_url (string): TODO: type description here.
        ble_config (ApBle): BLE AP settings
        config_auto_revert (bool): whether to enable ap auto config revert
        created_time (float): TODO: type description here.
        device_updown_threshold (int): sending AP_DISCONNECTED event in
            device-updowns only if AP_CONNECTED is not seen within the
            threshold, in minutes
        dns_servers (list of string): list of NTP servers
        dns_suffix (list of string): list of NTP servers
        enable_channel_144 (bool): whether to enable channel 144 (some older
            clients may not support it)
        engagement (SiteEngagement): **Note**: if hours does not exist, it’s
            treated as everyday of the week, 00:00-23:59. Currently we don’t
            allow multiple ranges for the same day  **Note**: default values
            for `dwell_tags`: passerby (1,300) bounce (301, 14400) engaged
            (14401, 28800) stationed (28801, 42000)  **Note**: default values
            for `dwell_tag_names`: passerby = “Passerby”, bounce = “Visitor”,
            engaged = “Associates”, stationed = “Assets”
        evpn_options (JunosEvpnOptions): EVPN Options
        flags (dict): name/val pair objects for location engine to use
        for_site (bool): TODO: type description here.
        gateway_additional_config_cmds (list of string): additional CLI
            commands to append to the generated config for gateways  **Note**:
            no check is done
        gateway_mgmt (SiteGateway): Gateway Site settings
        id (uuid|string): TODO: type description here.
        led (ApLed): LED AP settings
        modified_time (float): TODO: type description here.
        mxedge (Mxedge1): site mist edges form a cluster of radsecproxy
            servers
        mxedge_mgmt (MxedgeMgmt): TODO: type description here.
        mxtunnels (SiteMxtunnel): Site MxTunnel
        networks (dict): the property key is the network name
        ntp_servers (list of string): list of NTP servers
        occupancy (SiteOccupancyAnalytics): Occupancy Analytics settings
        org_id (uuid|string): TODO: type description here.
        ospf_areas (dict): the property key is the OSPF area
        persist_config_on_device (bool): whether to store the config on AP
        port_mirroring (dict): Property key is the port mirroring instance
            name port_mirroring can be added under site/settings. It takes
            interface and ports as input for ingress, interface as input for
            egress and can take interface and port as output.
        port_usages (PortUsages2): the property key is the port usage name
        proxy (Proxy2): Proxy Configuration for APs and Site Edges to talk to
            Mist
        radio_config (ApRadio): Radio AP settings
        radius_config (JunosRadiusConfig): Junos Radius config
        remote_syslog (RemoteSyslog): TODO: type description here.
        report_gatt (bool): whether AP should periodically connect to BLE
            devices and report GATT device info (device name, manufacturer
            name, serial number, battery %, temperature, humidity)
        rogue (SiteRogue): Rogue site settings
        rtsa (Rtsa): managed mobility
        simple_alert (SimpleAlert): Set of heuristic rules will be enabled
            when marvis subscription is not available. It triggers when, in a
            Z minute window, there are more than Y distinct client encountring
            over X failures
        site_id (uuid|string): TODO: type description here.
        skyatp (Skyatp): TODO: type description here.
        srx_app (SrxApp): TODO: type description here.
        ssh_keys (list of string): when limit_ssh_access = true in Org
            Setting, list of SSH public keys provided by Mist Support to
            install onto APs (see Org:Setting)
        ssr (SiteSsr): TODO: type description here.
        status_portal (StatusPortal): TODO: type description here.
        switch_matching (SwitchMatching): TODO: type description here.
        switch_mgmt (SiteSwitch): Switch site settings
        track_anonymous_devices (bool): whether to track anonymous BLE assets
            (requires ‘track_asset’ enabled)
        tunterm_monitoring (list of SiteTuntermMonitoring): TODO: type
            description here.
        tunterm_monitoring_disabled (bool): TODO: type description here.
        vars (dict): TODO: type description here.
        vna (Vna): TODO: type description here.
        vrf_instances (dict): the property key is the network name
        vrrp_groups (dict): the property key is the vrrp group
        vs_instances (dict): virtual-switch (for EX92xx and QFX5130) all the
            networks not included here will be placed in default `evpn_vs`
            virtual-switch RI Property key is the instance name
        wan_vna (WanVna): TODO: type description here.
        watched_station_url (string): TODO: type description here.
        whitelist_url (string): TODO: type description here.
        wids (SiteWids): WIDS site settings
        wifi (SiteWifi): Wi-Fi site settings
        wired_vna (WiredVna): TODO: type description here.
        zone_occupancy_alert (SiteZoneOccupancyAlert): Zone Occupancy alert
            site settings

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "additional_config_cmds": 'additional_config_cmds',
        "analytic": 'analytic',
        "ap_matching": 'ap_matching',
        "ap_port_config": 'ap_port_config',
        "auto_placement": 'auto_placement',
        "auto_preemption": 'auto_preemption',
        "auto_upgrade": 'auto_upgrade',
        "blacklist_url": 'blacklist_url',
        "ble_config": 'ble_config',
        "config_auto_revert": 'config_auto_revert',
        "created_time": 'created_time',
        "device_updown_threshold": 'device_updown_threshold',
        "dns_servers": 'dns_servers',
        "dns_suffix": 'dns_suffix',
        "enable_channel_144": 'enable_channel_144',
        "engagement": 'engagement',
        "evpn_options": 'evpn_options',
        "flags": 'flags',
        "for_site": 'for_site',
        "gateway_additional_config_cmds": 'gateway_additional_config_cmds',
        "gateway_mgmt": 'gateway_mgmt',
        "id": 'id',
        "led": 'led',
        "modified_time": 'modified_time',
        "mxedge": 'mxedge',
        "mxedge_mgmt": 'mxedge_mgmt',
        "mxtunnels": 'mxtunnels',
        "networks": 'networks',
        "ntp_servers": 'ntp_servers',
        "occupancy": 'occupancy',
        "org_id": 'org_id',
        "ospf_areas": 'ospf_areas',
        "persist_config_on_device": 'persist_config_on_device',
        "port_mirroring": 'port_mirroring',
        "port_usages": 'port_usages',
        "proxy": 'proxy',
        "radio_config": 'radio_config',
        "radius_config": 'radius_config',
        "remote_syslog": 'remote_syslog',
        "report_gatt": 'report_gatt',
        "rogue": 'rogue',
        "rtsa": 'rtsa',
        "simple_alert": 'simple_alert',
        "site_id": 'site_id',
        "skyatp": 'skyatp',
        "srx_app": 'srx_app',
        "ssh_keys": 'ssh_keys',
        "ssr": 'ssr',
        "status_portal": 'status_portal',
        "switch_matching": 'switch_matching',
        "switch_mgmt": 'switch_mgmt',
        "track_anonymous_devices": 'track_anonymous_devices',
        "tunterm_monitoring": 'tunterm_monitoring',
        "tunterm_monitoring_disabled": 'tunterm_monitoring_disabled',
        "vars": 'vars',
        "vna": 'vna',
        "vrf_instances": 'vrf_instances',
        "vrrp_groups": 'vrrp_groups',
        "vs_instances": 'vs_instances',
        "wan_vna": 'wan_vna',
        "watched_station_url": 'watched_station_url',
        "whitelist_url": 'whitelist_url',
        "wids": 'wids',
        "wifi": 'wifi',
        "wired_vna": 'wired_vna',
        "zone_occupancy_alert": 'zone_occupancy_alert'
    }

    _optionals = [
        'additional_config_cmds',
        'analytic',
        'ap_matching',
        'ap_port_config',
        'auto_placement',
        'auto_preemption',
        'auto_upgrade',
        'blacklist_url',
        'ble_config',
        'config_auto_revert',
        'created_time',
        'device_updown_threshold',
        'dns_servers',
        'dns_suffix',
        'enable_channel_144',
        'engagement',
        'evpn_options',
        'flags',
        'for_site',
        'gateway_additional_config_cmds',
        'gateway_mgmt',
        'id',
        'led',
        'modified_time',
        'mxedge',
        'mxedge_mgmt',
        'mxtunnels',
        'networks',
        'ntp_servers',
        'occupancy',
        'org_id',
        'ospf_areas',
        'persist_config_on_device',
        'port_mirroring',
        'port_usages',
        'proxy',
        'radio_config',
        'radius_config',
        'remote_syslog',
        'report_gatt',
        'rogue',
        'rtsa',
        'simple_alert',
        'site_id',
        'skyatp',
        'srx_app',
        'ssh_keys',
        'ssr',
        'status_portal',
        'switch_matching',
        'switch_mgmt',
        'track_anonymous_devices',
        'tunterm_monitoring',
        'tunterm_monitoring_disabled',
        'vars',
        'vna',
        'vrf_instances',
        'vrrp_groups',
        'vs_instances',
        'wan_vna',
        'watched_station_url',
        'whitelist_url',
        'wids',
        'wifi',
        'wired_vna',
        'zone_occupancy_alert',
    ]

    def __init__(self,
                 additional_config_cmds=APIHelper.SKIP,
                 analytic=APIHelper.SKIP,
                 ap_matching=APIHelper.SKIP,
                 ap_port_config=APIHelper.SKIP,
                 auto_placement=APIHelper.SKIP,
                 auto_preemption=APIHelper.SKIP,
                 auto_upgrade=APIHelper.SKIP,
                 blacklist_url=APIHelper.SKIP,
                 ble_config=APIHelper.SKIP,
                 config_auto_revert=False,
                 created_time=APIHelper.SKIP,
                 device_updown_threshold=0,
                 dns_servers=APIHelper.SKIP,
                 dns_suffix=APIHelper.SKIP,
                 enable_channel_144=False,
                 engagement=APIHelper.SKIP,
                 evpn_options=APIHelper.SKIP,
                 flags=APIHelper.SKIP,
                 for_site=APIHelper.SKIP,
                 gateway_additional_config_cmds=APIHelper.SKIP,
                 gateway_mgmt=APIHelper.SKIP,
                 id=APIHelper.SKIP,
                 led=APIHelper.SKIP,
                 modified_time=APIHelper.SKIP,
                 mxedge=APIHelper.SKIP,
                 mxedge_mgmt=APIHelper.SKIP,
                 mxtunnels=APIHelper.SKIP,
                 networks=APIHelper.SKIP,
                 ntp_servers=APIHelper.SKIP,
                 occupancy=APIHelper.SKIP,
                 org_id=APIHelper.SKIP,
                 ospf_areas=APIHelper.SKIP,
                 persist_config_on_device=False,
                 port_mirroring=APIHelper.SKIP,
                 port_usages=APIHelper.SKIP,
                 proxy=APIHelper.SKIP,
                 radio_config=APIHelper.SKIP,
                 radius_config=APIHelper.SKIP,
                 remote_syslog=APIHelper.SKIP,
                 report_gatt=False,
                 rogue=APIHelper.SKIP,
                 rtsa=APIHelper.SKIP,
                 simple_alert=APIHelper.SKIP,
                 site_id=APIHelper.SKIP,
                 skyatp=APIHelper.SKIP,
                 srx_app=APIHelper.SKIP,
                 ssh_keys=APIHelper.SKIP,
                 ssr=APIHelper.SKIP,
                 status_portal=APIHelper.SKIP,
                 switch_matching=APIHelper.SKIP,
                 switch_mgmt=APIHelper.SKIP,
                 track_anonymous_devices=False,
                 tunterm_monitoring=APIHelper.SKIP,
                 tunterm_monitoring_disabled=APIHelper.SKIP,
                 vars=APIHelper.SKIP,
                 vna=APIHelper.SKIP,
                 vrf_instances=APIHelper.SKIP,
                 vrrp_groups=APIHelper.SKIP,
                 vs_instances=APIHelper.SKIP,
                 wan_vna=APIHelper.SKIP,
                 watched_station_url=APIHelper.SKIP,
                 whitelist_url=APIHelper.SKIP,
                 wids=APIHelper.SKIP,
                 wifi=APIHelper.SKIP,
                 wired_vna=APIHelper.SKIP,
                 zone_occupancy_alert=APIHelper.SKIP):
        """Constructor for the SiteSetting class"""

        # Initialize members of the class
        if additional_config_cmds is not APIHelper.SKIP:
            self.additional_config_cmds = additional_config_cmds 
        if analytic is not APIHelper.SKIP:
            self.analytic = analytic 
        if ap_matching is not APIHelper.SKIP:
            self.ap_matching = ap_matching 
        if ap_port_config is not APIHelper.SKIP:
            self.ap_port_config = ap_port_config 
        if auto_placement is not APIHelper.SKIP:
            self.auto_placement = auto_placement 
        if auto_preemption is not APIHelper.SKIP:
            self.auto_preemption = auto_preemption 
        if auto_upgrade is not APIHelper.SKIP:
            self.auto_upgrade = auto_upgrade 
        if blacklist_url is not APIHelper.SKIP:
            self.blacklist_url = blacklist_url 
        if ble_config is not APIHelper.SKIP:
            self.ble_config = ble_config 
        self.config_auto_revert = config_auto_revert 
        if created_time is not APIHelper.SKIP:
            self.created_time = created_time 
        self.device_updown_threshold = device_updown_threshold 
        if dns_servers is not APIHelper.SKIP:
            self.dns_servers = dns_servers 
        if dns_suffix is not APIHelper.SKIP:
            self.dns_suffix = dns_suffix 
        self.enable_channel_144 = enable_channel_144 
        if engagement is not APIHelper.SKIP:
            self.engagement = engagement 
        if evpn_options is not APIHelper.SKIP:
            self.evpn_options = evpn_options 
        if flags is not APIHelper.SKIP:
            self.flags = flags 
        if for_site is not APIHelper.SKIP:
            self.for_site = for_site 
        if gateway_additional_config_cmds is not APIHelper.SKIP:
            self.gateway_additional_config_cmds = gateway_additional_config_cmds 
        if gateway_mgmt is not APIHelper.SKIP:
            self.gateway_mgmt = gateway_mgmt 
        if id is not APIHelper.SKIP:
            self.id = id 
        if led is not APIHelper.SKIP:
            self.led = led 
        if modified_time is not APIHelper.SKIP:
            self.modified_time = modified_time 
        if mxedge is not APIHelper.SKIP:
            self.mxedge = mxedge 
        if mxedge_mgmt is not APIHelper.SKIP:
            self.mxedge_mgmt = mxedge_mgmt 
        if mxtunnels is not APIHelper.SKIP:
            self.mxtunnels = mxtunnels 
        if networks is not APIHelper.SKIP:
            self.networks = networks 
        if ntp_servers is not APIHelper.SKIP:
            self.ntp_servers = ntp_servers 
        if occupancy is not APIHelper.SKIP:
            self.occupancy = occupancy 
        if org_id is not APIHelper.SKIP:
            self.org_id = org_id 
        if ospf_areas is not APIHelper.SKIP:
            self.ospf_areas = ospf_areas 
        self.persist_config_on_device = persist_config_on_device 
        if port_mirroring is not APIHelper.SKIP:
            self.port_mirroring = port_mirroring 
        if port_usages is not APIHelper.SKIP:
            self.port_usages = port_usages 
        if proxy is not APIHelper.SKIP:
            self.proxy = proxy 
        if radio_config is not APIHelper.SKIP:
            self.radio_config = radio_config 
        if radius_config is not APIHelper.SKIP:
            self.radius_config = radius_config 
        if remote_syslog is not APIHelper.SKIP:
            self.remote_syslog = remote_syslog 
        self.report_gatt = report_gatt 
        if rogue is not APIHelper.SKIP:
            self.rogue = rogue 
        if rtsa is not APIHelper.SKIP:
            self.rtsa = rtsa 
        if simple_alert is not APIHelper.SKIP:
            self.simple_alert = simple_alert 
        if site_id is not APIHelper.SKIP:
            self.site_id = site_id 
        if skyatp is not APIHelper.SKIP:
            self.skyatp = skyatp 
        if srx_app is not APIHelper.SKIP:
            self.srx_app = srx_app 
        if ssh_keys is not APIHelper.SKIP:
            self.ssh_keys = ssh_keys 
        if ssr is not APIHelper.SKIP:
            self.ssr = ssr 
        if status_portal is not APIHelper.SKIP:
            self.status_portal = status_portal 
        if switch_matching is not APIHelper.SKIP:
            self.switch_matching = switch_matching 
        if switch_mgmt is not APIHelper.SKIP:
            self.switch_mgmt = switch_mgmt 
        self.track_anonymous_devices = track_anonymous_devices 
        if tunterm_monitoring is not APIHelper.SKIP:
            self.tunterm_monitoring = tunterm_monitoring 
        if tunterm_monitoring_disabled is not APIHelper.SKIP:
            self.tunterm_monitoring_disabled = tunterm_monitoring_disabled 
        if vars is not APIHelper.SKIP:
            self.vars = vars 
        if vna is not APIHelper.SKIP:
            self.vna = vna 
        if vrf_instances is not APIHelper.SKIP:
            self.vrf_instances = vrf_instances 
        if vrrp_groups is not APIHelper.SKIP:
            self.vrrp_groups = vrrp_groups 
        if vs_instances is not APIHelper.SKIP:
            self.vs_instances = vs_instances 
        if wan_vna is not APIHelper.SKIP:
            self.wan_vna = wan_vna 
        if watched_station_url is not APIHelper.SKIP:
            self.watched_station_url = watched_station_url 
        if whitelist_url is not APIHelper.SKIP:
            self.whitelist_url = whitelist_url 
        if wids is not APIHelper.SKIP:
            self.wids = wids 
        if wifi is not APIHelper.SKIP:
            self.wifi = wifi 
        if wired_vna is not APIHelper.SKIP:
            self.wired_vna = wired_vna 
        if zone_occupancy_alert is not APIHelper.SKIP:
            self.zone_occupancy_alert = zone_occupancy_alert 

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

        additional_config_cmds = dictionary.get("additional_config_cmds") if dictionary.get("additional_config_cmds") else APIHelper.SKIP
        analytic = Analytic.from_dictionary(dictionary.get('analytic')) if 'analytic' in dictionary.keys() else APIHelper.SKIP
        ap_matching = ApMatching1.from_dictionary(dictionary.get('ap_matching')) if 'ap_matching' in dictionary.keys() else APIHelper.SKIP
        ap_port_config = ApPortConfig1.from_dictionary(dictionary.get('ap_port_config')) if 'ap_port_config' in dictionary.keys() else APIHelper.SKIP
        auto_placement = AutoPlacement.from_dictionary(dictionary.get('auto_placement')) if 'auto_placement' in dictionary.keys() else APIHelper.SKIP
        auto_preemption = AutoPreemption.from_dictionary(dictionary.get('auto_preemption')) if 'auto_preemption' in dictionary.keys() else APIHelper.SKIP
        auto_upgrade = SiteAutoUpgrade.from_dictionary(dictionary.get('auto_upgrade')) if 'auto_upgrade' in dictionary.keys() else APIHelper.SKIP
        blacklist_url = dictionary.get("blacklist_url") if dictionary.get("blacklist_url") else APIHelper.SKIP
        ble_config = ApBle.from_dictionary(dictionary.get('ble_config')) if 'ble_config' in dictionary.keys() else APIHelper.SKIP
        config_auto_revert = dictionary.get("config_auto_revert") if dictionary.get("config_auto_revert") else False
        created_time = dictionary.get("created_time") if dictionary.get("created_time") else APIHelper.SKIP
        device_updown_threshold = dictionary.get("device_updown_threshold") if dictionary.get("device_updown_threshold") else 0
        dns_servers = dictionary.get("dns_servers") if dictionary.get("dns_servers") else APIHelper.SKIP
        dns_suffix = dictionary.get("dns_suffix") if dictionary.get("dns_suffix") else APIHelper.SKIP
        enable_channel_144 = dictionary.get("enable_channel_144") if dictionary.get("enable_channel_144") else False
        engagement = SiteEngagement.from_dictionary(dictionary.get('engagement')) if 'engagement' in dictionary.keys() else APIHelper.SKIP
        evpn_options = JunosEvpnOptions.from_dictionary(dictionary.get('evpn_options')) if 'evpn_options' in dictionary.keys() else APIHelper.SKIP
        flags = dictionary.get("flags") if dictionary.get("flags") else APIHelper.SKIP
        for_site = dictionary.get("for_site") if "for_site" in dictionary.keys() else APIHelper.SKIP
        gateway_additional_config_cmds = dictionary.get("gateway_additional_config_cmds") if dictionary.get("gateway_additional_config_cmds") else APIHelper.SKIP
        gateway_mgmt = SiteGateway.from_dictionary(dictionary.get('gateway_mgmt')) if 'gateway_mgmt' in dictionary.keys() else APIHelper.SKIP
        id = dictionary.get("id") if dictionary.get("id") else APIHelper.SKIP
        led = ApLed.from_dictionary(dictionary.get('led')) if 'led' in dictionary.keys() else APIHelper.SKIP
        modified_time = dictionary.get("modified_time") if dictionary.get("modified_time") else APIHelper.SKIP
        mxedge = Mxedge1.from_dictionary(dictionary.get('mxedge')) if 'mxedge' in dictionary.keys() else APIHelper.SKIP
        mxedge_mgmt = MxedgeMgmt.from_dictionary(dictionary.get('mxedge_mgmt')) if 'mxedge_mgmt' in dictionary.keys() else APIHelper.SKIP
        mxtunnels = SiteMxtunnel.from_dictionary(dictionary.get('mxtunnels')) if 'mxtunnels' in dictionary.keys() else APIHelper.SKIP
        networks = JunosNetworks.from_dictionary(dictionary.get('networks')) if 'networks' in dictionary.keys() else APIHelper.SKIP
        ntp_servers = dictionary.get("ntp_servers") if dictionary.get("ntp_servers") else APIHelper.SKIP
        occupancy = SiteOccupancyAnalytics.from_dictionary(dictionary.get('occupancy')) if 'occupancy' in dictionary.keys() else APIHelper.SKIP
        org_id = dictionary.get("org_id") if dictionary.get("org_id") else APIHelper.SKIP
        ospf_areas = JunosOspfAreas.from_dictionary(dictionary.get('ospf_areas')) if 'ospf_areas' in dictionary.keys() else APIHelper.SKIP
        persist_config_on_device = dictionary.get("persist_config_on_device") if dictionary.get("persist_config_on_device") else False
        port_mirroring = JunosPortMirroring.from_dictionary(dictionary.get('port_mirroring')) if 'port_mirroring' in dictionary.keys() else APIHelper.SKIP
        port_usages = PortUsages2.from_dictionary(dictionary.get('port_usages')) if 'port_usages' in dictionary.keys() else APIHelper.SKIP
        proxy = Proxy2.from_dictionary(dictionary.get('proxy')) if 'proxy' in dictionary.keys() else APIHelper.SKIP
        radio_config = ApRadio.from_dictionary(dictionary.get('radio_config')) if 'radio_config' in dictionary.keys() else APIHelper.SKIP
        radius_config = JunosRadiusConfig.from_dictionary(dictionary.get('radius_config')) if 'radius_config' in dictionary.keys() else APIHelper.SKIP
        remote_syslog = RemoteSyslog.from_dictionary(dictionary.get('remote_syslog')) if 'remote_syslog' in dictionary.keys() else APIHelper.SKIP
        report_gatt = dictionary.get("report_gatt") if dictionary.get("report_gatt") else False
        rogue = SiteRogue.from_dictionary(dictionary.get('rogue')) if 'rogue' in dictionary.keys() else APIHelper.SKIP
        rtsa = Rtsa.from_dictionary(dictionary.get('rtsa')) if 'rtsa' in dictionary.keys() else APIHelper.SKIP
        simple_alert = SimpleAlert.from_dictionary(dictionary.get('simple_alert')) if 'simple_alert' in dictionary.keys() else APIHelper.SKIP
        site_id = dictionary.get("site_id") if dictionary.get("site_id") else APIHelper.SKIP
        skyatp = Skyatp.from_dictionary(dictionary.get('skyatp')) if 'skyatp' in dictionary.keys() else APIHelper.SKIP
        srx_app = SrxApp.from_dictionary(dictionary.get('srx_app')) if 'srx_app' in dictionary.keys() else APIHelper.SKIP
        ssh_keys = dictionary.get("ssh_keys") if dictionary.get("ssh_keys") else APIHelper.SKIP
        ssr = SiteSsr.from_dictionary(dictionary.get('ssr')) if 'ssr' in dictionary.keys() else APIHelper.SKIP
        status_portal = StatusPortal.from_dictionary(dictionary.get('status_portal')) if 'status_portal' in dictionary.keys() else APIHelper.SKIP
        switch_matching = SwitchMatching.from_dictionary(dictionary.get('switch_matching')) if 'switch_matching' in dictionary.keys() else APIHelper.SKIP
        switch_mgmt = SiteSwitch.from_dictionary(dictionary.get('switch_mgmt')) if 'switch_mgmt' in dictionary.keys() else APIHelper.SKIP
        track_anonymous_devices = dictionary.get("track_anonymous_devices") if dictionary.get("track_anonymous_devices") else False
        tunterm_monitoring = None
        if dictionary.get('tunterm_monitoring') is not None:
            tunterm_monitoring = [SiteTuntermMonitoring.from_dictionary(x) for x in dictionary.get('tunterm_monitoring')]
        else:
            tunterm_monitoring = APIHelper.SKIP
        tunterm_monitoring_disabled = dictionary.get("tunterm_monitoring_disabled") if "tunterm_monitoring_disabled" in dictionary.keys() else APIHelper.SKIP
        vars = dictionary.get("vars") if dictionary.get("vars") else APIHelper.SKIP
        vna = Vna.from_dictionary(dictionary.get('vna')) if 'vna' in dictionary.keys() else APIHelper.SKIP
        vrf_instances = JunosVrfInstance.from_dictionary(dictionary.get('vrf_instances')) if 'vrf_instances' in dictionary.keys() else APIHelper.SKIP
        vrrp_groups = JunosVrrpGroup.from_dictionary(dictionary.get('vrrp_groups')) if 'vrrp_groups' in dictionary.keys() else APIHelper.SKIP
        vs_instances = VsInstances.from_dictionary(dictionary.get('vs_instances')) if 'vs_instances' in dictionary.keys() else APIHelper.SKIP
        wan_vna = WanVna.from_dictionary(dictionary.get('wan_vna')) if 'wan_vna' in dictionary.keys() else APIHelper.SKIP
        watched_station_url = dictionary.get("watched_station_url") if dictionary.get("watched_station_url") else APIHelper.SKIP
        whitelist_url = dictionary.get("whitelist_url") if dictionary.get("whitelist_url") else APIHelper.SKIP
        wids = SiteWids.from_dictionary(dictionary.get('wids')) if 'wids' in dictionary.keys() else APIHelper.SKIP
        wifi = SiteWifi.from_dictionary(dictionary.get('wifi')) if 'wifi' in dictionary.keys() else APIHelper.SKIP
        wired_vna = WiredVna.from_dictionary(dictionary.get('wired_vna')) if 'wired_vna' in dictionary.keys() else APIHelper.SKIP
        zone_occupancy_alert = SiteZoneOccupancyAlert.from_dictionary(dictionary.get('zone_occupancy_alert')) if 'zone_occupancy_alert' in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(additional_config_cmds,
                   analytic,
                   ap_matching,
                   ap_port_config,
                   auto_placement,
                   auto_preemption,
                   auto_upgrade,
                   blacklist_url,
                   ble_config,
                   config_auto_revert,
                   created_time,
                   device_updown_threshold,
                   dns_servers,
                   dns_suffix,
                   enable_channel_144,
                   engagement,
                   evpn_options,
                   flags,
                   for_site,
                   gateway_additional_config_cmds,
                   gateway_mgmt,
                   id,
                   led,
                   modified_time,
                   mxedge,
                   mxedge_mgmt,
                   mxtunnels,
                   networks,
                   ntp_servers,
                   occupancy,
                   org_id,
                   ospf_areas,
                   persist_config_on_device,
                   port_mirroring,
                   port_usages,
                   proxy,
                   radio_config,
                   radius_config,
                   remote_syslog,
                   report_gatt,
                   rogue,
                   rtsa,
                   simple_alert,
                   site_id,
                   skyatp,
                   srx_app,
                   ssh_keys,
                   ssr,
                   status_portal,
                   switch_matching,
                   switch_mgmt,
                   track_anonymous_devices,
                   tunterm_monitoring,
                   tunterm_monitoring_disabled,
                   vars,
                   vna,
                   vrf_instances,
                   vrrp_groups,
                   vs_instances,
                   wan_vna,
                   watched_station_url,
                   whitelist_url,
                   wids,
                   wifi,
                   wired_vna,
                   zone_occupancy_alert)
