# -*- coding: utf-8 -*-

"""
mistapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from mistapi.api_helper import APIHelper
from mistapi.models.ap_aeroscout import ApAeroscout
from mistapi.models.ap_ble import ApBle
from mistapi.models.ap_client_bridge import ApClientBridge
from mistapi.models.ap_esl_config import ApEslConfig
from mistapi.models.ap_iot import ApIot
from mistapi.models.ap_ip import ApIp
from mistapi.models.ap_led import ApLed
from mistapi.models.ap_mesh import ApMesh
from mistapi.models.ap_port_config import ApPortConfig
from mistapi.models.ap_radio import ApRadio
from mistapi.models.ap_usb import ApUsb
from mistapi.models.centrak import Centrak
from mistapi.models.pwr_config import PwrConfig
from mistapi.models.uplink_port_config import UplinkPortConfig


class DeviceAp(object):

    """Implementation of the 'device_ap' model.

    AP

    Attributes:
        aeroscout (ApAeroscout): Aeroscout AP settings
        ble_config (ApBle): BLE AP settings
        centrak (Centrak): TODO: type description here.
        client_bridge (ApClientBridge): TODO: type description here.
        created_time (float): TODO: type description here.
        deviceprofile_id (uuid|string): TODO: type description here.
        disable_eth_1 (bool): whether to disable eth1 port
        disable_eth_2 (bool): whether to disable eth2 port
        disable_eth_3 (bool): whether to disable eth3 port
        disable_module (bool): whether to disable module port
        esl_config (ApEslConfig): TODO: type description here.
        for_site (bool): TODO: type description here.
        height (float): height, in meters, optional
        id (uuid|string): TODO: type description here.
        image_1_url (string): TODO: type description here.
        image_2_url (string): TODO: type description here.
        image_3_url (string): TODO: type description here.
        iot_config (ApIot): IoT AP settings
        ip_config (ApIp): IP AP settings
        led (ApLed): LED AP settings
        locked (bool): whether this map is considered locked down
        map_id (uuid|string): map where the device belongs to
        mesh (ApMesh): Mesh AP settings
        modified_time (float): TODO: type description here.
        name (string): TODO: type description here.
        notes (string): any notes about this AP
        ntp_servers (list of string): TODO: type description here.
        org_id (uuid|string): TODO: type description here.
        orientation (float): orientation, 0-359, in degrees, up is 0, right is
            90.
        poe_passthrough (bool): whether to enable power out through module
            port (for APH) or eth1 (for APL/BT11)
        port_config (dict): eth0 is allowed in mesh relay mode, otherwise eth0
            is not allowed here.  The property key is the interface(s) name
            (e.g. "eth1" or"eth1,eth2")
        pwr_config (PwrConfig): power related configs
        radio_config (ApRadio): Radio AP settings
        site_id (uuid|string): TODO: type description here.
        uplink_port_config (UplinkPortConfig): TODO: type description here.
        usb_config (ApUsb): USB AP settings Note: if native imagotag is
            enabled, BLE will be disabled automatically Note: legacy, new
            config moved to ESL Config.
        vars (object): a dictionary of name->value, the vars can then be used
            in Wlans. This can overwrite those from Site Vars
        x (float): x in pixel
        y (float): y in pixel

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "aeroscout": 'aeroscout',
        "ble_config": 'ble_config',
        "centrak": 'centrak',
        "client_bridge": 'client_bridge',
        "created_time": 'created_time',
        "deviceprofile_id": 'deviceprofile_id',
        "disable_eth_1": 'disable_eth1',
        "disable_eth_2": 'disable_eth2',
        "disable_eth_3": 'disable_eth3',
        "disable_module": 'disable_module',
        "esl_config": 'esl_config',
        "for_site": 'for_site',
        "height": 'height',
        "id": 'id',
        "image_1_url": 'image1_url',
        "image_2_url": 'image2_url',
        "image_3_url": 'image3_url',
        "iot_config": 'iot_config',
        "ip_config": 'ip_config',
        "led": 'led',
        "locked": 'locked',
        "map_id": 'map_id',
        "mesh": 'mesh',
        "modified_time": 'modified_time',
        "name": 'name',
        "notes": 'notes',
        "ntp_servers": 'ntp_servers',
        "org_id": 'org_id',
        "orientation": 'orientation',
        "poe_passthrough": 'poe_passthrough',
        "port_config": 'port_config',
        "pwr_config": 'pwr_config',
        "radio_config": 'radio_config',
        "site_id": 'site_id',
        "uplink_port_config": 'uplink_port_config',
        "usb_config": 'usb_config',
        "vars": 'vars',
        "x": 'x',
        "y": 'y'
    }

    _optionals = [
        'aeroscout',
        'ble_config',
        'centrak',
        'client_bridge',
        'created_time',
        'deviceprofile_id',
        'disable_eth_1',
        'disable_eth_2',
        'disable_eth_3',
        'disable_module',
        'esl_config',
        'for_site',
        'height',
        'id',
        'image_1_url',
        'image_2_url',
        'image_3_url',
        'iot_config',
        'ip_config',
        'led',
        'locked',
        'map_id',
        'mesh',
        'modified_time',
        'name',
        'notes',
        'ntp_servers',
        'org_id',
        'orientation',
        'poe_passthrough',
        'port_config',
        'pwr_config',
        'radio_config',
        'site_id',
        'uplink_port_config',
        'usb_config',
        'vars',
        'x',
        'y',
    ]

    _nullables = [
        'deviceprofile_id',
        'image_1_url',
        'image_2_url',
        'image_3_url',
    ]

    def __init__(self,
                 aeroscout=APIHelper.SKIP,
                 ble_config=APIHelper.SKIP,
                 centrak=APIHelper.SKIP,
                 client_bridge=APIHelper.SKIP,
                 created_time=APIHelper.SKIP,
                 deviceprofile_id=APIHelper.SKIP,
                 disable_eth_1=False,
                 disable_eth_2=False,
                 disable_eth_3=False,
                 disable_module=False,
                 esl_config=APIHelper.SKIP,
                 for_site=APIHelper.SKIP,
                 height=APIHelper.SKIP,
                 id=APIHelper.SKIP,
                 image_1_url=APIHelper.SKIP,
                 image_2_url=APIHelper.SKIP,
                 image_3_url=APIHelper.SKIP,
                 iot_config=APIHelper.SKIP,
                 ip_config=APIHelper.SKIP,
                 led=APIHelper.SKIP,
                 locked=APIHelper.SKIP,
                 map_id=APIHelper.SKIP,
                 mesh=APIHelper.SKIP,
                 modified_time=APIHelper.SKIP,
                 name=APIHelper.SKIP,
                 notes=APIHelper.SKIP,
                 ntp_servers=APIHelper.SKIP,
                 org_id=APIHelper.SKIP,
                 orientation=APIHelper.SKIP,
                 poe_passthrough=False,
                 port_config=APIHelper.SKIP,
                 pwr_config=APIHelper.SKIP,
                 radio_config=APIHelper.SKIP,
                 site_id=APIHelper.SKIP,
                 uplink_port_config=APIHelper.SKIP,
                 usb_config=APIHelper.SKIP,
                 vars=APIHelper.SKIP,
                 x=APIHelper.SKIP,
                 y=APIHelper.SKIP):
        """Constructor for the DeviceAp class"""

        # Initialize members of the class
        if aeroscout is not APIHelper.SKIP:
            self.aeroscout = aeroscout 
        if ble_config is not APIHelper.SKIP:
            self.ble_config = ble_config 
        if centrak is not APIHelper.SKIP:
            self.centrak = centrak 
        if client_bridge is not APIHelper.SKIP:
            self.client_bridge = client_bridge 
        if created_time is not APIHelper.SKIP:
            self.created_time = created_time 
        if deviceprofile_id is not APIHelper.SKIP:
            self.deviceprofile_id = deviceprofile_id 
        self.disable_eth_1 = disable_eth_1 
        self.disable_eth_2 = disable_eth_2 
        self.disable_eth_3 = disable_eth_3 
        self.disable_module = disable_module 
        if esl_config is not APIHelper.SKIP:
            self.esl_config = esl_config 
        if for_site is not APIHelper.SKIP:
            self.for_site = for_site 
        if height is not APIHelper.SKIP:
            self.height = height 
        if id is not APIHelper.SKIP:
            self.id = id 
        if image_1_url is not APIHelper.SKIP:
            self.image_1_url = image_1_url 
        if image_2_url is not APIHelper.SKIP:
            self.image_2_url = image_2_url 
        if image_3_url is not APIHelper.SKIP:
            self.image_3_url = image_3_url 
        if iot_config is not APIHelper.SKIP:
            self.iot_config = iot_config 
        if ip_config is not APIHelper.SKIP:
            self.ip_config = ip_config 
        if led is not APIHelper.SKIP:
            self.led = led 
        if locked is not APIHelper.SKIP:
            self.locked = locked 
        if map_id is not APIHelper.SKIP:
            self.map_id = map_id 
        if mesh is not APIHelper.SKIP:
            self.mesh = mesh 
        if modified_time is not APIHelper.SKIP:
            self.modified_time = modified_time 
        if name is not APIHelper.SKIP:
            self.name = name 
        if notes is not APIHelper.SKIP:
            self.notes = notes 
        if ntp_servers is not APIHelper.SKIP:
            self.ntp_servers = ntp_servers 
        if org_id is not APIHelper.SKIP:
            self.org_id = org_id 
        if orientation is not APIHelper.SKIP:
            self.orientation = orientation 
        self.poe_passthrough = poe_passthrough 
        if port_config is not APIHelper.SKIP:
            self.port_config = port_config 
        if pwr_config is not APIHelper.SKIP:
            self.pwr_config = pwr_config 
        if radio_config is not APIHelper.SKIP:
            self.radio_config = radio_config 
        if site_id is not APIHelper.SKIP:
            self.site_id = site_id 
        if uplink_port_config is not APIHelper.SKIP:
            self.uplink_port_config = uplink_port_config 
        if usb_config is not APIHelper.SKIP:
            self.usb_config = usb_config 
        if vars is not APIHelper.SKIP:
            self.vars = vars 
        if x is not APIHelper.SKIP:
            self.x = x 
        if y is not APIHelper.SKIP:
            self.y = y 

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

        aeroscout = ApAeroscout.from_dictionary(dictionary.get('aeroscout')) if 'aeroscout' in dictionary.keys() else APIHelper.SKIP
        ble_config = ApBle.from_dictionary(dictionary.get('ble_config')) if 'ble_config' in dictionary.keys() else APIHelper.SKIP
        centrak = Centrak.from_dictionary(dictionary.get('centrak')) if 'centrak' in dictionary.keys() else APIHelper.SKIP
        client_bridge = ApClientBridge.from_dictionary(dictionary.get('client_bridge')) if 'client_bridge' in dictionary.keys() else APIHelper.SKIP
        created_time = dictionary.get("created_time") if dictionary.get("created_time") else APIHelper.SKIP
        deviceprofile_id = dictionary.get("deviceprofile_id") if "deviceprofile_id" in dictionary.keys() else APIHelper.SKIP
        disable_eth_1 = dictionary.get("disable_eth1") if dictionary.get("disable_eth1") else False
        disable_eth_2 = dictionary.get("disable_eth2") if dictionary.get("disable_eth2") else False
        disable_eth_3 = dictionary.get("disable_eth3") if dictionary.get("disable_eth3") else False
        disable_module = dictionary.get("disable_module") if dictionary.get("disable_module") else False
        esl_config = ApEslConfig.from_dictionary(dictionary.get('esl_config')) if 'esl_config' in dictionary.keys() else APIHelper.SKIP
        for_site = dictionary.get("for_site") if "for_site" in dictionary.keys() else APIHelper.SKIP
        height = dictionary.get("height") if dictionary.get("height") else APIHelper.SKIP
        id = dictionary.get("id") if dictionary.get("id") else APIHelper.SKIP
        image_1_url = dictionary.get("image1_url") if "image1_url" in dictionary.keys() else APIHelper.SKIP
        image_2_url = dictionary.get("image2_url") if "image2_url" in dictionary.keys() else APIHelper.SKIP
        image_3_url = dictionary.get("image3_url") if "image3_url" in dictionary.keys() else APIHelper.SKIP
        iot_config = ApIot.from_dictionary(dictionary.get('iot_config')) if 'iot_config' in dictionary.keys() else APIHelper.SKIP
        ip_config = ApIp.from_dictionary(dictionary.get('ip_config')) if 'ip_config' in dictionary.keys() else APIHelper.SKIP
        led = ApLed.from_dictionary(dictionary.get('led')) if 'led' in dictionary.keys() else APIHelper.SKIP
        locked = dictionary.get("locked") if "locked" in dictionary.keys() else APIHelper.SKIP
        map_id = dictionary.get("map_id") if dictionary.get("map_id") else APIHelper.SKIP
        mesh = ApMesh.from_dictionary(dictionary.get('mesh')) if 'mesh' in dictionary.keys() else APIHelper.SKIP
        modified_time = dictionary.get("modified_time") if dictionary.get("modified_time") else APIHelper.SKIP
        name = dictionary.get("name") if dictionary.get("name") else APIHelper.SKIP
        notes = dictionary.get("notes") if dictionary.get("notes") else APIHelper.SKIP
        ntp_servers = dictionary.get("ntp_servers") if dictionary.get("ntp_servers") else APIHelper.SKIP
        org_id = dictionary.get("org_id") if dictionary.get("org_id") else APIHelper.SKIP
        orientation = dictionary.get("orientation") if dictionary.get("orientation") else APIHelper.SKIP
        poe_passthrough = dictionary.get("poe_passthrough") if dictionary.get("poe_passthrough") else False
        port_config = ApPortConfig.from_dictionary(dictionary.get('port_config')) if 'port_config' in dictionary.keys() else APIHelper.SKIP
        pwr_config = PwrConfig.from_dictionary(dictionary.get('pwr_config')) if 'pwr_config' in dictionary.keys() else APIHelper.SKIP
        radio_config = ApRadio.from_dictionary(dictionary.get('radio_config')) if 'radio_config' in dictionary.keys() else APIHelper.SKIP
        site_id = dictionary.get("site_id") if dictionary.get("site_id") else APIHelper.SKIP
        uplink_port_config = UplinkPortConfig.from_dictionary(dictionary.get('uplink_port_config')) if 'uplink_port_config' in dictionary.keys() else APIHelper.SKIP
        usb_config = ApUsb.from_dictionary(dictionary.get('usb_config')) if 'usb_config' in dictionary.keys() else APIHelper.SKIP
        vars = dictionary.get("vars") if dictionary.get("vars") else APIHelper.SKIP
        x = dictionary.get("x") if dictionary.get("x") else APIHelper.SKIP
        y = dictionary.get("y") if dictionary.get("y") else APIHelper.SKIP
        # Return an object of this model
        return cls(aeroscout,
                   ble_config,
                   centrak,
                   client_bridge,
                   created_time,
                   deviceprofile_id,
                   disable_eth_1,
                   disable_eth_2,
                   disable_eth_3,
                   disable_module,
                   esl_config,
                   for_site,
                   height,
                   id,
                   image_1_url,
                   image_2_url,
                   image_3_url,
                   iot_config,
                   ip_config,
                   led,
                   locked,
                   map_id,
                   mesh,
                   modified_time,
                   name,
                   notes,
                   ntp_servers,
                   org_id,
                   orientation,
                   poe_passthrough,
                   port_config,
                   pwr_config,
                   radio_config,
                   site_id,
                   uplink_port_config,
                   usb_config,
                   vars,
                   x,
                   y)
