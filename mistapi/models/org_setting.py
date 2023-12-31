# -*- coding: utf-8 -*-

"""
mistapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from mistapi.api_helper import APIHelper
from mistapi.models.auto_device_naming import AutoDeviceNaming
from mistapi.models.auto_deviceprofile_assignment import AutoDeviceprofileAssignment
from mistapi.models.auto_site_assignment import AutoSiteAssignment
from mistapi.models.celona import Celona
from mistapi.models.cloudshark import Cloudshark
from mistapi.models.cradlepoint import Cradlepoint
from mistapi.models.device_cert import DeviceCert
from mistapi.models.gateway_mgmt import GatewayMgmt
from mistapi.models.installer import Installer
from mistapi.models.juniper import Juniper
from mistapi.models.mgmt import Mgmt
from mistapi.models.mist_nac_1 import MistNac1
from mistapi.models.mxedge_mgmt import MxedgeMgmt
from mistapi.models.password_policy import PasswordPolicy
from mistapi.models.pcap import Pcap
from mistapi.models.security import Security
from mistapi.models.simple_alert import SimpleAlert
from mistapi.models.switch_mgmt_3 import SwitchMgmt3
from mistapi.models.synthetic_test import SyntheticTest
from mistapi.models.vpn_options import VpnOptions
from mistapi.models.wan_pma import WanPma
from mistapi.models.wired_pma import WiredPma


class OrgSetting(object):

    """Implementation of the 'org_setting' model.

    Org Settings

    Attributes:
        auto_device_naming (AutoDeviceNaming): TODO: type description here.
        auto_deviceprofile_assignment (AutoDeviceprofileAssignment): TODO:
            type description here.
        auto_site_assignment (AutoSiteAssignment): TODO: type description
            here.
        blacklist_url (string): TODO: type description here.
        cacerts (list of string): list of PEM-encoded ca certs
        celona (Celona): TODO: type description here.
        cloudshark (Cloudshark): TODO: type description here.
        cradlepoint (Cradlepoint): TODO: type description here.
        created_time (float): TODO: type description here.
        device_cert (DeviceCert): common device cert, optional
        device_updown_threshold (int): enable threshold-based device down
            delivery via  1) device-updowns webhooks topic,  2) Mist Alert
            Framework; e.g. send AP/SW/GW down event only if AP/SW/GW Up is
            not seen within the threshold in minutes; 0 - 240, default is 0
            (trigger immediate)
        disable_pcap (bool): whether to disallow Mist to analyze pcap files
            (this is required for marvis pcap)
        disable_remote_shell (bool): whether to disable remote shell access
            for an entire org
        for_site (bool): TODO: type description here.
        gateway_mgmt (GatewayMgmt): TODO: type description here.
        id (uuid|string): TODO: type description here.
        installer (Installer): TODO: type description here.
        juniper (Juniper): TODO: type description here.
        mgmt (Mgmt): management-related properties
        mist_nac (MistNac1): TODO: type description here.
        modified_time (float): TODO: type description here.
        msp_id (uuid|string): TODO: type description here.
        mxedge_mgmt (MxedgeMgmt): TODO: type description here.
        org_id (uuid|string): TODO: type description here.
        password_policy (PasswordPolicy): password policy
        pcap (Pcap): TODO: type description here.
        pcap_bucket_verified (bool): TODO: type description here.
        security (Security): TODO: type description here.
        simple_alert (SimpleAlert): Set of heuristic rules will be enabled
            when marvis subscription is not available. It triggers when, in a
            Z minute window, there are more than Y distinct client encountring
            over X failures
        site_id (uuid|string): TODO: type description here.
        switch_mgmt (SwitchMgmt3): TODO: type description here.
        synthetic_test (SyntheticTest): TODO: type description here.
        tags (list of string): list of tags
        ui_idle_timeout (int): automatically logout the user when UI session
            is inactive. `0` means disabled
        vpn_options (VpnOptions): TODO: type description here.
        wan_pma (WanPma): TODO: type description here.
        wired_pma (WiredPma): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "auto_device_naming": 'auto_device_naming',
        "auto_deviceprofile_assignment": 'auto_deviceprofile_assignment',
        "auto_site_assignment": 'auto_site_assignment',
        "blacklist_url": 'blacklist_url',
        "cacerts": 'cacerts',
        "celona": 'celona',
        "cloudshark": 'cloudshark',
        "cradlepoint": 'cradlepoint',
        "created_time": 'created_time',
        "device_cert": 'device_cert',
        "device_updown_threshold": 'device_updown_threshold',
        "disable_pcap": 'disable_pcap',
        "disable_remote_shell": 'disable_remote_shell',
        "for_site": 'for_site',
        "gateway_mgmt": 'gateway_mgmt',
        "id": 'id',
        "installer": 'installer',
        "juniper": 'juniper',
        "mgmt": 'mgmt',
        "mist_nac": 'mist_nac',
        "modified_time": 'modified_time',
        "msp_id": 'msp_id',
        "mxedge_mgmt": 'mxedge_mgmt',
        "org_id": 'org_id',
        "password_policy": 'password_policy',
        "pcap": 'pcap',
        "pcap_bucket_verified": 'pcap_bucket_verified',
        "security": 'security',
        "simple_alert": 'simple_alert',
        "site_id": 'site_id',
        "switch_mgmt": 'switch_mgmt',
        "synthetic_test": 'synthetic_test',
        "tags": 'tags',
        "ui_idle_timeout": 'ui_idle_timeout',
        "vpn_options": 'vpn_options',
        "wan_pma": 'wan_pma',
        "wired_pma": 'wired_pma'
    }

    _optionals = [
        'auto_device_naming',
        'auto_deviceprofile_assignment',
        'auto_site_assignment',
        'blacklist_url',
        'cacerts',
        'celona',
        'cloudshark',
        'cradlepoint',
        'created_time',
        'device_cert',
        'device_updown_threshold',
        'disable_pcap',
        'disable_remote_shell',
        'for_site',
        'gateway_mgmt',
        'id',
        'installer',
        'juniper',
        'mgmt',
        'mist_nac',
        'modified_time',
        'msp_id',
        'mxedge_mgmt',
        'org_id',
        'password_policy',
        'pcap',
        'pcap_bucket_verified',
        'security',
        'simple_alert',
        'site_id',
        'switch_mgmt',
        'synthetic_test',
        'tags',
        'ui_idle_timeout',
        'vpn_options',
        'wan_pma',
        'wired_pma',
    ]

    def __init__(self,
                 auto_device_naming=APIHelper.SKIP,
                 auto_deviceprofile_assignment=APIHelper.SKIP,
                 auto_site_assignment=APIHelper.SKIP,
                 blacklist_url=APIHelper.SKIP,
                 cacerts=APIHelper.SKIP,
                 celona=APIHelper.SKIP,
                 cloudshark=APIHelper.SKIP,
                 cradlepoint=APIHelper.SKIP,
                 created_time=APIHelper.SKIP,
                 device_cert=APIHelper.SKIP,
                 device_updown_threshold=0,
                 disable_pcap=False,
                 disable_remote_shell=False,
                 for_site=APIHelper.SKIP,
                 gateway_mgmt=APIHelper.SKIP,
                 id=APIHelper.SKIP,
                 installer=APIHelper.SKIP,
                 juniper=APIHelper.SKIP,
                 mgmt=APIHelper.SKIP,
                 mist_nac=APIHelper.SKIP,
                 modified_time=APIHelper.SKIP,
                 msp_id=APIHelper.SKIP,
                 mxedge_mgmt=APIHelper.SKIP,
                 org_id=APIHelper.SKIP,
                 password_policy=APIHelper.SKIP,
                 pcap=APIHelper.SKIP,
                 pcap_bucket_verified=APIHelper.SKIP,
                 security=APIHelper.SKIP,
                 simple_alert=APIHelper.SKIP,
                 site_id=APIHelper.SKIP,
                 switch_mgmt=APIHelper.SKIP,
                 synthetic_test=APIHelper.SKIP,
                 tags=APIHelper.SKIP,
                 ui_idle_timeout=0,
                 vpn_options=APIHelper.SKIP,
                 wan_pma=APIHelper.SKIP,
                 wired_pma=APIHelper.SKIP):
        """Constructor for the OrgSetting class"""

        # Initialize members of the class
        if auto_device_naming is not APIHelper.SKIP:
            self.auto_device_naming = auto_device_naming 
        if auto_deviceprofile_assignment is not APIHelper.SKIP:
            self.auto_deviceprofile_assignment = auto_deviceprofile_assignment 
        if auto_site_assignment is not APIHelper.SKIP:
            self.auto_site_assignment = auto_site_assignment 
        if blacklist_url is not APIHelper.SKIP:
            self.blacklist_url = blacklist_url 
        if cacerts is not APIHelper.SKIP:
            self.cacerts = cacerts 
        if celona is not APIHelper.SKIP:
            self.celona = celona 
        if cloudshark is not APIHelper.SKIP:
            self.cloudshark = cloudshark 
        if cradlepoint is not APIHelper.SKIP:
            self.cradlepoint = cradlepoint 
        if created_time is not APIHelper.SKIP:
            self.created_time = created_time 
        if device_cert is not APIHelper.SKIP:
            self.device_cert = device_cert 
        self.device_updown_threshold = device_updown_threshold 
        self.disable_pcap = disable_pcap 
        self.disable_remote_shell = disable_remote_shell 
        if for_site is not APIHelper.SKIP:
            self.for_site = for_site 
        if gateway_mgmt is not APIHelper.SKIP:
            self.gateway_mgmt = gateway_mgmt 
        if id is not APIHelper.SKIP:
            self.id = id 
        if installer is not APIHelper.SKIP:
            self.installer = installer 
        if juniper is not APIHelper.SKIP:
            self.juniper = juniper 
        if mgmt is not APIHelper.SKIP:
            self.mgmt = mgmt 
        if mist_nac is not APIHelper.SKIP:
            self.mist_nac = mist_nac 
        if modified_time is not APIHelper.SKIP:
            self.modified_time = modified_time 
        if msp_id is not APIHelper.SKIP:
            self.msp_id = msp_id 
        if mxedge_mgmt is not APIHelper.SKIP:
            self.mxedge_mgmt = mxedge_mgmt 
        if org_id is not APIHelper.SKIP:
            self.org_id = org_id 
        if password_policy is not APIHelper.SKIP:
            self.password_policy = password_policy 
        if pcap is not APIHelper.SKIP:
            self.pcap = pcap 
        if pcap_bucket_verified is not APIHelper.SKIP:
            self.pcap_bucket_verified = pcap_bucket_verified 
        if security is not APIHelper.SKIP:
            self.security = security 
        if simple_alert is not APIHelper.SKIP:
            self.simple_alert = simple_alert 
        if site_id is not APIHelper.SKIP:
            self.site_id = site_id 
        if switch_mgmt is not APIHelper.SKIP:
            self.switch_mgmt = switch_mgmt 
        if synthetic_test is not APIHelper.SKIP:
            self.synthetic_test = synthetic_test 
        if tags is not APIHelper.SKIP:
            self.tags = tags 
        self.ui_idle_timeout = ui_idle_timeout 
        if vpn_options is not APIHelper.SKIP:
            self.vpn_options = vpn_options 
        if wan_pma is not APIHelper.SKIP:
            self.wan_pma = wan_pma 
        if wired_pma is not APIHelper.SKIP:
            self.wired_pma = wired_pma 

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

        auto_device_naming = AutoDeviceNaming.from_dictionary(dictionary.get('auto_device_naming')) if 'auto_device_naming' in dictionary.keys() else APIHelper.SKIP
        auto_deviceprofile_assignment = AutoDeviceprofileAssignment.from_dictionary(dictionary.get('auto_deviceprofile_assignment')) if 'auto_deviceprofile_assignment' in dictionary.keys() else APIHelper.SKIP
        auto_site_assignment = AutoSiteAssignment.from_dictionary(dictionary.get('auto_site_assignment')) if 'auto_site_assignment' in dictionary.keys() else APIHelper.SKIP
        blacklist_url = dictionary.get("blacklist_url") if dictionary.get("blacklist_url") else APIHelper.SKIP
        cacerts = dictionary.get("cacerts") if dictionary.get("cacerts") else APIHelper.SKIP
        celona = Celona.from_dictionary(dictionary.get('celona')) if 'celona' in dictionary.keys() else APIHelper.SKIP
        cloudshark = Cloudshark.from_dictionary(dictionary.get('cloudshark')) if 'cloudshark' in dictionary.keys() else APIHelper.SKIP
        cradlepoint = Cradlepoint.from_dictionary(dictionary.get('cradlepoint')) if 'cradlepoint' in dictionary.keys() else APIHelper.SKIP
        created_time = dictionary.get("created_time") if dictionary.get("created_time") else APIHelper.SKIP
        device_cert = DeviceCert.from_dictionary(dictionary.get('device_cert')) if 'device_cert' in dictionary.keys() else APIHelper.SKIP
        device_updown_threshold = dictionary.get("device_updown_threshold") if dictionary.get("device_updown_threshold") else 0
        disable_pcap = dictionary.get("disable_pcap") if dictionary.get("disable_pcap") else False
        disable_remote_shell = dictionary.get("disable_remote_shell") if dictionary.get("disable_remote_shell") else False
        for_site = dictionary.get("for_site") if "for_site" in dictionary.keys() else APIHelper.SKIP
        gateway_mgmt = GatewayMgmt.from_dictionary(dictionary.get('gateway_mgmt')) if 'gateway_mgmt' in dictionary.keys() else APIHelper.SKIP
        id = dictionary.get("id") if dictionary.get("id") else APIHelper.SKIP
        installer = Installer.from_dictionary(dictionary.get('installer')) if 'installer' in dictionary.keys() else APIHelper.SKIP
        juniper = Juniper.from_dictionary(dictionary.get('juniper')) if 'juniper' in dictionary.keys() else APIHelper.SKIP
        mgmt = Mgmt.from_dictionary(dictionary.get('mgmt')) if 'mgmt' in dictionary.keys() else APIHelper.SKIP
        mist_nac = MistNac1.from_dictionary(dictionary.get('mist_nac')) if 'mist_nac' in dictionary.keys() else APIHelper.SKIP
        modified_time = dictionary.get("modified_time") if dictionary.get("modified_time") else APIHelper.SKIP
        msp_id = dictionary.get("msp_id") if dictionary.get("msp_id") else APIHelper.SKIP
        mxedge_mgmt = MxedgeMgmt.from_dictionary(dictionary.get('mxedge_mgmt')) if 'mxedge_mgmt' in dictionary.keys() else APIHelper.SKIP
        org_id = dictionary.get("org_id") if dictionary.get("org_id") else APIHelper.SKIP
        password_policy = PasswordPolicy.from_dictionary(dictionary.get('password_policy')) if 'password_policy' in dictionary.keys() else APIHelper.SKIP
        pcap = Pcap.from_dictionary(dictionary.get('pcap')) if 'pcap' in dictionary.keys() else APIHelper.SKIP
        pcap_bucket_verified = dictionary.get("pcap_bucket_verified") if "pcap_bucket_verified" in dictionary.keys() else APIHelper.SKIP
        security = Security.from_dictionary(dictionary.get('security')) if 'security' in dictionary.keys() else APIHelper.SKIP
        simple_alert = SimpleAlert.from_dictionary(dictionary.get('simple_alert')) if 'simple_alert' in dictionary.keys() else APIHelper.SKIP
        site_id = dictionary.get("site_id") if dictionary.get("site_id") else APIHelper.SKIP
        switch_mgmt = SwitchMgmt3.from_dictionary(dictionary.get('switch_mgmt')) if 'switch_mgmt' in dictionary.keys() else APIHelper.SKIP
        synthetic_test = SyntheticTest.from_dictionary(dictionary.get('synthetic_test')) if 'synthetic_test' in dictionary.keys() else APIHelper.SKIP
        tags = dictionary.get("tags") if dictionary.get("tags") else APIHelper.SKIP
        ui_idle_timeout = dictionary.get("ui_idle_timeout") if dictionary.get("ui_idle_timeout") else 0
        vpn_options = VpnOptions.from_dictionary(dictionary.get('vpn_options')) if 'vpn_options' in dictionary.keys() else APIHelper.SKIP
        wan_pma = WanPma.from_dictionary(dictionary.get('wan_pma')) if 'wan_pma' in dictionary.keys() else APIHelper.SKIP
        wired_pma = WiredPma.from_dictionary(dictionary.get('wired_pma')) if 'wired_pma' in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(auto_device_naming,
                   auto_deviceprofile_assignment,
                   auto_site_assignment,
                   blacklist_url,
                   cacerts,
                   celona,
                   cloudshark,
                   cradlepoint,
                   created_time,
                   device_cert,
                   device_updown_threshold,
                   disable_pcap,
                   disable_remote_shell,
                   for_site,
                   gateway_mgmt,
                   id,
                   installer,
                   juniper,
                   mgmt,
                   mist_nac,
                   modified_time,
                   msp_id,
                   mxedge_mgmt,
                   org_id,
                   password_policy,
                   pcap,
                   pcap_bucket_verified,
                   security,
                   simple_alert,
                   site_id,
                   switch_mgmt,
                   synthetic_test,
                   tags,
                   ui_idle_timeout,
                   vpn_options,
                   wan_pma,
                   wired_pma)
