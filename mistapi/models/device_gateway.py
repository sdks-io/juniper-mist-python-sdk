# -*- coding: utf-8 -*-

"""
mistapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from mistapi.api_helper import APIHelper
from mistapi.models.extra_routes import ExtraRoutes
from mistapi.models.junos_dhcpd import JunosDhcpd
from mistapi.models.junos_ip_config import JunosIpConfig
from mistapi.models.junos_oob_ip_config import JunosOobIpConfig
from mistapi.models.junos_port_config_gateway import JunosPortConfigGateway
from mistapi.models.networks import Networks
from mistapi.models.port_mirroring import PortMirroring


class DeviceGateway(object):

    """Implementation of the 'device_gateway' model.

    device gateway

    Attributes:
        additional_config_cmds (list of string): TODO: type description here.
        created_time (float): TODO: type description here.
        deviceprofile_id (uuid|string): TODO: type description here.
        dhcpd_config (JunosDhcpd): if DHCP Server/Relay is intended. The
            property key is the network name
        extra_routes (dict): The property key is the destination
        for_site (bool): TODO: type description here.
        id (uuid|string): TODO: type description here.
        image_1_url (string): TODO: type description here.
        image_2_url (string): TODO: type description here.
        image_3_url (string): TODO: type description here.
        ip_config (JunosIpConfig): Junos IP Config
        managed (bool): TODO: type description here.
        modified_time (float): TODO: type description here.
        msp_id (uuid|string): TODO: type description here.
        name (string): TODO: type description here.
        networks (dict): The property key is the network name or a CIDR
        ntp_servers (list of string): TODO: type description here.
        oob_ip_config (JunosOobIpConfig): Junos out-of-band (vme/em0/fxp0) IP
            config
        org_id (uuid|string): TODO: type description here.
        port_config (dict): The property key is the port name or range (e.g.
            "ge-0/0/0-10")
        port_mirroring (PortMirroring): TODO: type description here.
        site_id (uuid|string): TODO: type description here.
        vars (object): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "additional_config_cmds": 'additional_config_cmds',
        "created_time": 'created_time',
        "deviceprofile_id": 'deviceprofile_id',
        "dhcpd_config": 'dhcpd_config',
        "extra_routes": 'extra_routes',
        "for_site": 'for_site',
        "id": 'id',
        "image_1_url": 'image1_url',
        "image_2_url": 'image2_url',
        "image_3_url": 'image3_url',
        "ip_config": 'ip_config',
        "managed": 'managed',
        "modified_time": 'modified_time',
        "msp_id": 'msp_id',
        "name": 'name',
        "networks": 'networks',
        "ntp_servers": 'ntp_servers',
        "oob_ip_config": 'oob_ip_config',
        "org_id": 'org_id',
        "port_config": 'port_config',
        "port_mirroring": 'port_mirroring',
        "site_id": 'site_id',
        "vars": 'vars'
    }

    _optionals = [
        'additional_config_cmds',
        'created_time',
        'deviceprofile_id',
        'dhcpd_config',
        'extra_routes',
        'for_site',
        'id',
        'image_1_url',
        'image_2_url',
        'image_3_url',
        'ip_config',
        'managed',
        'modified_time',
        'msp_id',
        'name',
        'networks',
        'ntp_servers',
        'oob_ip_config',
        'org_id',
        'port_config',
        'port_mirroring',
        'site_id',
        'vars',
    ]

    def __init__(self,
                 additional_config_cmds=APIHelper.SKIP,
                 created_time=APIHelper.SKIP,
                 deviceprofile_id=APIHelper.SKIP,
                 dhcpd_config=APIHelper.SKIP,
                 extra_routes=APIHelper.SKIP,
                 for_site=APIHelper.SKIP,
                 id=APIHelper.SKIP,
                 image_1_url=APIHelper.SKIP,
                 image_2_url=APIHelper.SKIP,
                 image_3_url=APIHelper.SKIP,
                 ip_config=APIHelper.SKIP,
                 managed=APIHelper.SKIP,
                 modified_time=APIHelper.SKIP,
                 msp_id=APIHelper.SKIP,
                 name=APIHelper.SKIP,
                 networks=APIHelper.SKIP,
                 ntp_servers=APIHelper.SKIP,
                 oob_ip_config=APIHelper.SKIP,
                 org_id=APIHelper.SKIP,
                 port_config=APIHelper.SKIP,
                 port_mirroring=APIHelper.SKIP,
                 site_id=APIHelper.SKIP,
                 vars=APIHelper.SKIP):
        """Constructor for the DeviceGateway class"""

        # Initialize members of the class
        if additional_config_cmds is not APIHelper.SKIP:
            self.additional_config_cmds = additional_config_cmds 
        if created_time is not APIHelper.SKIP:
            self.created_time = created_time 
        if deviceprofile_id is not APIHelper.SKIP:
            self.deviceprofile_id = deviceprofile_id 
        if dhcpd_config is not APIHelper.SKIP:
            self.dhcpd_config = dhcpd_config 
        if extra_routes is not APIHelper.SKIP:
            self.extra_routes = extra_routes 
        if for_site is not APIHelper.SKIP:
            self.for_site = for_site 
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
        if managed is not APIHelper.SKIP:
            self.managed = managed 
        if modified_time is not APIHelper.SKIP:
            self.modified_time = modified_time 
        if msp_id is not APIHelper.SKIP:
            self.msp_id = msp_id 
        if name is not APIHelper.SKIP:
            self.name = name 
        if networks is not APIHelper.SKIP:
            self.networks = networks 
        if ntp_servers is not APIHelper.SKIP:
            self.ntp_servers = ntp_servers 
        if oob_ip_config is not APIHelper.SKIP:
            self.oob_ip_config = oob_ip_config 
        if org_id is not APIHelper.SKIP:
            self.org_id = org_id 
        if port_config is not APIHelper.SKIP:
            self.port_config = port_config 
        if port_mirroring is not APIHelper.SKIP:
            self.port_mirroring = port_mirroring 
        if site_id is not APIHelper.SKIP:
            self.site_id = site_id 
        if vars is not APIHelper.SKIP:
            self.vars = vars 

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
        created_time = dictionary.get("created_time") if dictionary.get("created_time") else APIHelper.SKIP
        deviceprofile_id = dictionary.get("deviceprofile_id") if dictionary.get("deviceprofile_id") else APIHelper.SKIP
        dhcpd_config = JunosDhcpd.from_dictionary(dictionary.get('dhcpd_config')) if 'dhcpd_config' in dictionary.keys() else APIHelper.SKIP
        extra_routes = ExtraRoutes.from_dictionary(dictionary.get('extra_routes')) if 'extra_routes' in dictionary.keys() else APIHelper.SKIP
        for_site = dictionary.get("for_site") if "for_site" in dictionary.keys() else APIHelper.SKIP
        id = dictionary.get("id") if dictionary.get("id") else APIHelper.SKIP
        image_1_url = dictionary.get("image1_url") if dictionary.get("image1_url") else APIHelper.SKIP
        image_2_url = dictionary.get("image2_url") if dictionary.get("image2_url") else APIHelper.SKIP
        image_3_url = dictionary.get("image3_url") if dictionary.get("image3_url") else APIHelper.SKIP
        ip_config = JunosIpConfig.from_dictionary(dictionary.get('ip_config')) if 'ip_config' in dictionary.keys() else APIHelper.SKIP
        managed = dictionary.get("managed") if "managed" in dictionary.keys() else APIHelper.SKIP
        modified_time = dictionary.get("modified_time") if dictionary.get("modified_time") else APIHelper.SKIP
        msp_id = dictionary.get("msp_id") if dictionary.get("msp_id") else APIHelper.SKIP
        name = dictionary.get("name") if dictionary.get("name") else APIHelper.SKIP
        networks = Networks.from_dictionary(dictionary.get('networks')) if 'networks' in dictionary.keys() else APIHelper.SKIP
        ntp_servers = dictionary.get("ntp_servers") if dictionary.get("ntp_servers") else APIHelper.SKIP
        oob_ip_config = JunosOobIpConfig.from_dictionary(dictionary.get('oob_ip_config')) if 'oob_ip_config' in dictionary.keys() else APIHelper.SKIP
        org_id = dictionary.get("org_id") if dictionary.get("org_id") else APIHelper.SKIP
        port_config = JunosPortConfigGateway.from_dictionary(dictionary.get('port_config')) if 'port_config' in dictionary.keys() else APIHelper.SKIP
        port_mirroring = PortMirroring.from_dictionary(dictionary.get('port_mirroring')) if 'port_mirroring' in dictionary.keys() else APIHelper.SKIP
        site_id = dictionary.get("site_id") if dictionary.get("site_id") else APIHelper.SKIP
        vars = dictionary.get("vars") if dictionary.get("vars") else APIHelper.SKIP
        # Return an object of this model
        return cls(additional_config_cmds,
                   created_time,
                   deviceprofile_id,
                   dhcpd_config,
                   extra_routes,
                   for_site,
                   id,
                   image_1_url,
                   image_2_url,
                   image_3_url,
                   ip_config,
                   managed,
                   modified_time,
                   msp_id,
                   name,
                   networks,
                   ntp_servers,
                   oob_ip_config,
                   org_id,
                   port_config,
                   port_mirroring,
                   site_id,
                   vars)
