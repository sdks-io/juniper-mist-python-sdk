# -*- coding: utf-8 -*-

"""
mistapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

import json
import dateutil.parser

from tests.controllers.controller_test_base import ControllerTestBase
from apimatic_core.utilities.comparison_helper import ComparisonHelper
from mistapi.api_helper import APIHelper


class ConstantsControllerTests(ControllerTestBase):

    @classmethod
    def setUpClass(cls):
        super(ConstantsControllerTests, cls).setUpClass()
        cls.controller = cls.client.constants
        cls.response_catcher = cls.controller.http_call_back

    # Get List of brief definitions of all the supported alarm types.  The example field contains an example payload as you would recieve in the alarm webhook output.
    def test_list_alarm_definitions(self):

        # Perform the API call through the SDK function
        result = self.controller.list_alarm_definitions()

        # Test response code
        assert self.response_catcher.response.status_code == 200

        # Test headers
        expected_headers = {}
        expected_headers['content-type'] = 'application/json'

        assert ComparisonHelper.match_headers(expected_headers, self.response_catcher.response.headers)

        
        # Test whether the captured response is as we expected
        assert result is not None
        expected_body = APIHelper.json_deserialize('[{"display":"Device offline","example":{"aps":["d420b02000fa"],"co'
            'unt":1,"group":"infrastructure","hostnames":["Vendor_AP2"],"id":"f'
            '70c308f-7007-4866-9ecd-0d01842979ea","last_seen":1629753888,"org_i'
            'd":"09dac91f-6e73-4100-89f7-698e0fafbb1b","severity":"warn","site_'
            'id":"dcfb31a1-d615-4361-8c95-b9dde05aa704","timestamp":1629753888,'
            '"type":"device_down"},"fields":["aps","hostnames"],"group":"infras'
            'tructure","key":"device_down","severity":"warn"}]')
        received_body = APIHelper.json_deserialize(self.response_catcher.response.text)
        assert ComparisonHelper.match_body(expected_body, received_body)

    # Get List of List of Available channels per country code
    def test_list_ap_channels(self):
        # Parameters for the API call
        country_code = 'US'

        # Perform the API call through the SDK function
        result = self.controller.list_ap_channels(country_code)

        # Test response code
        assert self.response_catcher.response.status_code == 200

        # Test headers
        expected_headers = {}
        expected_headers['content-type'] = 'application/json'

        assert ComparisonHelper.match_headers(expected_headers, self.response_catcher.response.headers)

        
        # Test whether the captured response is as we expected
        assert result is not None
        expected_body = APIHelper.json_deserialize('{"band24_channels":{"20":[1,2,3,4,5,6,7,8,9,10,11],"40":[1,2,3,4,5'
            ',6,7,8,9,10,11]},"band24_enabled":true,"band5_channels":{"20":[36,'
            '40,44,48,52,56,60,64,100,104,108,112,116,132,136,140,149,153,157,1'
            '61,165],"40":[36,40,44,48,52,56,60,64,100,104,108,112,132,136,149,'
            '153,157,161],"80":[36,40,44,48,52,56,60,64,100,104,108,112,132,136'
            ',149,153,157,161],"dfs":[52,56,60,64,100,104,108,112,116,132,136,1'
            '40]},"band5_enabled":true,"code":840,"dfs_ok":true,"key":"US","nam'
            'e":"United States"}')
        received_body = APIHelper.json_deserialize(self.response_catcher.response.text)
        assert ComparisonHelper.match_body(expected_body, received_body)

    # Get List of AP LED definition
    def test_list_ap_led_definition(self):

        # Perform the API call through the SDK function
        result = self.controller.list_ap_led_definition()

        # Test response code
        assert self.response_catcher.response.status_code == 200

        # Test headers
        expected_headers = {}
        expected_headers['content-type'] = 'application/json'

        assert ComparisonHelper.match_headers(expected_headers, self.response_catcher.response.headers)

        
        # Test whether the captured response is as we expected
        assert result is not None
        expected_body = APIHelper.json_deserialize('[{"code":"02","description":"Has no link (Seen using power injecto'
            'rs, but not connected to a switch)","key":"NO_ETHERNET_LINK","name'
            '":"No ethernet link"}]')
        received_body = APIHelper.json_deserialize(self.response_catcher.response.text)
        assert ComparisonHelper.match_body(expected_body, received_body)

    # Get List of a list of applications that Juniper-Mist APs recognize
    def test_list_applications(self):

        # Perform the API call through the SDK function
        result = self.controller.list_applications()

        # Test response code
        assert self.response_catcher.response.status_code == 200

        # Test headers
        expected_headers = {}
        expected_headers['content-type'] = 'application/json'

        assert ComparisonHelper.match_headers(expected_headers, self.response_catcher.response.headers)

        
        # Test whether the captured response is as we expected
        assert result is not None
        expected_body = APIHelper.json_deserialize('[{"app_id":true,"group":"Emails","key":"all-email","name":"All Ema'
            'ils"},{"app_id":true,"category":"Collaboration","group":"Emails","'
            'key":"gmail","name":"Gmail","ssr_app_id":true},{"app_id":true,"cat'
            'egory":"Collaboration","group":"Emails","key":"yahoo-mail","name":'
            '"Yahoo Mail","ssr_app_id":true},{"app_id":true,"app_image_url":"",'
            '"app_probe":true,"category":"FileSharing","group":"File Sharing","'
            'key":"dropbox","name":"Dropbox","ssr_app_id":true},{"app_id":true,'
            '"group":"Online Backup","key":"icloud-backup","name":"iCloud backu'
            'p"},{"app_id":true,"category":"FileSharing","group":"Peer 2 Peer",'
            '"key":"bit-torrent","name":"BitTorrent","ssr_app_id":true},{"app_i'
            'd":true,"group":"Social","key":"all-social","name":"All Socials"},'
            '{"app_id":true,"app_image_url":"","app_probe":true,"category":"Soc'
            'ialMedia","group":"Social","key":"facebook","name":"Facebook","ssr'
            '_app_id":true}]')
        received_body = APIHelper.json_deserialize(self.response_catcher.response.text)
        assert ComparisonHelper.match_body(expected_body, received_body)

    # Get List of Call Event Definitions
    def test_list_call_events_definitions(self):

        # Perform the API call through the SDK function
        result = self.controller.list_call_events_definitions()

        # Test response code
        assert self.response_catcher.response.status_code == 200

        # Test headers
        expected_headers = {}
        expected_headers['content-type'] = 'application/json'

        assert ComparisonHelper.match_headers(expected_headers, self.response_catcher.response.headers)

        
        # Test whether the captured response is as we expected
        assert result is not None
        expected_body = APIHelper.json_deserialize('[{"description":"Client joined the call","display":"Client joined '
            'the call","example":{"app":"zoom","meeting_id":"87609329850","org_'
            'id":"2818e386-8dec-2562-9ede-5b8a0fbbdc71","site_id":"1916d52a-4a9'
            '0-11e5-8b45-1258369c38a9","timestamp":1674777600,"type":"CLIENTS_J'
            'OINED_CALL","wcid":"82c70a73-e2e1-42f9-6da0-97db44b7b9ad"},"key":"'
            'CLIENT_JOINED_CALL"},{"description":"Client got abruptly disconnec'
            'ted from the call","display":"Client disconnected abruptly from th'
            'e call","example":{"app":"zoom","meeting_id":"87609329850","org_id'
            '":"2818e386-8dec-2562-9ede-5b8a0fbbdc71","reason":"Network connect'
            'ion error.","site_id":"1916d52a-4a90-11e5-8b45-1258369c38a9","time'
            'stamp":1674777600,"type":"CLIENT_DISCONNECTED_FROM_CALL","wcid":"8'
            '2c70a73-e2e1-42f9-6da0-97db44b7b9ad"},"key":"CLIENT_DISCONNECTED_F'
            'ROM_CALL"},{"description":"Client left the call","display":"Client'
            ' left the call","example":{"app":"zoom","meeting_id":"87609329850"'
            ',"org_id":"2818e386-8dec-2562-9ede-5b8a0fbbdc71","site_id":"1916d5'
            '2a-4a90-11e5-8b45-1258369c38a9","timestamp":1674777600,"type":"CLI'
            'ENT_LEFT_CALL","wcid":"82c70a73-e2e1-42f9-6da0-97db44b7b9ad"},"key'
            '":"CLIENT_LEFT_CALL"},{"description":"Zoom/Teams CPU usage is high'
            '","display":"High CPU Observed","example":{"app":"zoom","org_id":"'
            '2818e386-8dec-2562-9ede-5b8a0fbbdc71","timestamp":1674777600,"type'
            '":"HIGH_CPU_OBSERVED"},"key":"HIGH_CPU_OBSERVED"}]')
        received_body = APIHelper.json_deserialize(self.response_catcher.response.text)
        assert ComparisonHelper.match_body(expected_body, received_body)

    # Get List of List of available Client Events
    def test_list_client_events_definitions(self):

        # Perform the API call through the SDK function
        result = self.controller.list_client_events_definitions()

        # Test response code
        assert self.response_catcher.response.status_code == 200

        # Test headers
        expected_headers = {}
        expected_headers['content-type'] = 'application/json'

        assert ComparisonHelper.match_headers(expected_headers, self.response_catcher.response.headers)

        
        # Test whether the captured response is as we expected
        assert result is not None
        expected_body = APIHelper.json_deserialize('[{"display":"DHCP Success","key":"CLIENT_IP_ASSIGNED"}]')
        received_body = APIHelper.json_deserialize(self.response_catcher.response.text)
        assert ComparisonHelper.match_body(expected_body, received_body)

    # Get List of List of available Country Codes
    def test_list_country_codes(self):

        # Perform the API call through the SDK function
        result = self.controller.list_country_codes()

        # Test response code
        assert self.response_catcher.response.status_code == 200

        # Test headers
        expected_headers = {}
        expected_headers['content-type'] = 'application/json'

        assert ComparisonHelper.match_headers(expected_headers, self.response_catcher.response.headers)

        
        # Test whether the captured response is as we expected
        assert result is not None
        expected_body = APIHelper.json_deserialize('[{"alpha2":"US","certified":true,"name":"United States","numeric":'
            '840},{"alpha2":"JP","certified":true,"name":"Japan","numeric":392}'
            ']')
        received_body = APIHelper.json_deserialize(self.response_catcher.response.text)
        assert ComparisonHelper.match_body(expected_body, received_body)

    # Generate Default Gateway Config
    def test_get_gataway_default_config(self):
        # Parameters for the API call
        model = None
        ha = None

        # Perform the API call through the SDK function
        result = self.controller.get_gataway_default_config(model, ha)

        # Test response code
        assert self.response_catcher.response.status_code == 200

        # Test headers
        expected_headers = {}
        expected_headers['content-type'] = 'application/json'

        assert ComparisonHelper.match_headers(expected_headers, self.response_catcher.response.headers)

        
        # Test whether the captured response is as we expected
        assert result is not None
        expected_body = APIHelper.json_deserialize('{"dhcpd_config":{"lan":{"ip_end":"192.168.1.254","ip_start":"192.1'
            '68.1.2"}},"ip_configs":{"lan":{"ip":"192.168.1.1","type":"static"}'
            '},"networks":{"lan":{"name":"lan","subnet":"192.168.1.0/24","vlan_'
            'id":1}},"path_preferences":{"wan":{"paths":[{"name":"wan","type":"'
            'wan"}]}},"port_config":{"cl-1/0/0":{"ip_config":{"type":"dhcp"},"n'
            'ame":"lte","usage":"wan","wan_type":"lte"},"ge-0/0/0,ge-0/0/7":{"i'
            'p_config":{"type":"dhcp"},"name":"wan","usage":"wan"},"ge-0/0/1-6"'
            ':{"port_network":"lan","usage":"lan"}},"service_policies":[{"actio'
            'n":"allow","name":"Internet","path_preference":"wan","services":["'
            'any"],"tenants":["lan"]}]}')
        received_body = APIHelper.json_deserialize(self.response_catcher.response.text)
        assert ComparisonHelper.match_body(expected_body, received_body)

    # Get list of available Device Events
    def test_list_device_events_definitions(self):

        # Perform the API call through the SDK function
        result = self.controller.list_device_events_definitions()

        # Test response code
        assert self.response_catcher.response.status_code == 200

        # Test headers
        expected_headers = {}
        expected_headers['content-type'] = 'application/json'

        assert ComparisonHelper.match_headers(expected_headers, self.response_catcher.response.headers)

        
        # Test whether the captured response is as we expected
        assert result is not None
        expected_body = APIHelper.json_deserialize('[{"description":"AP was assigned to a site","display":"AP Assigned'
            '","example":{"ap":"5c5b35000001","audit_id":"e9a88814-fa81-5bdc-34'
            'b0-84e8735420e5","org_id":"2818e386-8dec-2562-9ede-5b8a0fbbdc71","'
            'site_id":"4ac1dcf4-9d8b-7211-65c4-057819f0862b","timestamp":155240'
            '8871,"type":"AP_ASSIGNED"},"key":"AP_ASSIGNED"}]')
        received_body = APIHelper.json_deserialize(self.response_catcher.response.text)
        assert ComparisonHelper.match_body(expected_body, received_body)

    # Get list of AP device models for the Mist Site
    def test_list_device_models(self):

        # Perform the API call through the SDK function
        result = self.controller.list_device_models()

        # Test response code
        assert self.response_catcher.response.status_code == 200

        # Test headers
        expected_headers = {}
        expected_headers['content-type'] = 'application/json'

        assert ComparisonHelper.match_headers(expected_headers, self.response_catcher.response.headers)

        
        # Test whether the captured response is as we expected
        assert result is not None
        expected_body = APIHelper.json_deserialize('[{"alias":"string","ap_type":"string","band24":{"max_clients":0,"m'
            'ax_power":0,"min_power":0},"band5":{"max_clients":0,"max_power":0,'
            '"min_power":0},"band6":{"max_clients":0,"max_power":0,"min_power":'
            '0},"ce_dfs_ok":true,"cisco_pace":true,"defaults":{"_ports":"string'
            '","property1":"string","property2":"string"},"description":"string'
            '","disallowed_channels":{"property1":{"property1":[0],"property2":'
            '[0]},"property2":{"property1":[0],"property2":[0]}},"display":"str'
            'ing","evolved_os":false,"evpn_ri_type":"string","experimental":fal'
            'se,"extio":{"property1":{"default_dir":"IN","input":true,"output":'
            'true},"property2":{"default_dir":"IN","input":true,"output":true}}'
            ',"fans_pluggable":true,"fcc_dfs_ok":true,"ha_node0_fpc":0,"ha_node'
            '1_fpc":0,"has_11ax":true,"has_bgp":false,"has_compass":true,"has_e'
            'ts":false,"has_evpn":false,"has_ext_ant":true,"has_extio":true,"ha'
            's_fxp0":true,"has_ha_control":false,"has_ha_data":false,"has_heigh'
            't":true,"has_irb":false,"has_module_port":true,"has_poe_out":true,'
            '"has_scanning_radio":true,"has_selectable_radio":true,"has_snapsho'
            't":true,"has_usb":true,"has_vble":true,"has_vc":true,"has_wifi_ban'
            'd24":true,"has_wifi_band5":true,"has_wifi_band6":true,"irb_disable'
            'd_by_default":false,"max_poe_out":0,"max_wlans":0,"model":"string"'
            ',"modular":false,"no_shaping_rate":false,"number_fans":0,"oc_devic'
            'e":false,"oob_interface":"string","other_dfs_ok":true,"outdoor":tr'
            'ue,"packet_action_drop_only":false,"pic":{"property1":"string","pr'
            'operty2":"string"},"ports":{"display":"string","pci_address":"stri'
            'ng","speed":0},"radios":{"property1":"string","property2":"string"'
            '},"shared_scanning_radio":true,"sub_required":"string","t128_devic'
            'e":false,"type":"gateway","unmanaged":true,"vble":{"beacon_rate":0'
            ',"beams":0,"power":0}}]')
        received_body = APIHelper.json_deserialize(self.response_catcher.response.text)
        assert ComparisonHelper.match_body(expected_body, received_body)

    # List Insight Metrics
    def test_list_insight_metrics(self):

        # Perform the API call through the SDK function
        result = self.controller.list_insight_metrics()

        # Test response code
        assert self.response_catcher.response.status_code == 200

        # Test headers
        expected_headers = {}
        expected_headers['content-type'] = 'application/json'

        assert ComparisonHelper.match_headers(expected_headers, self.response_catcher.response.headers)

        
        # Test whether the captured response is as we expected
        assert result is not None
        expected_body = APIHelper.json_deserialize('{"bytes":{"description":"aggregated bytes over time","example":[18'
            '5,197,250],"intervals":{"10m":{"interval":600,"max_age":86400},"1h'
            '":{"interval":3600,"max_age":1209600}},"report_durations":{"1d":{"'
            'duration":86400,"interval":3600},"1w":{"duration":604800,"interval'
            '":3600}},"report_scopes":["site","org"],"scopes":["site","ap","cli'
            'ent"],"type":"timeseries","unit":"byte"},"num_clients":{"descripti'
            'on":"number of client over time","example":[18,null,15],"intervals'
            '":{"10m":{"interval":600,"max_age":86400},"1h":{"interval":3600,"m'
            'ax_age":1209600}},"report_durations":{"1d":{"duration":86400,"inte'
            'rval":3600},"1w":{"duration":604800,"interval":3600}},"report_scop'
            'es":["site","org"],"scopes":["site","ap","device"],"type":"timeser'
            'ies","unit":""}}')
        received_body = APIHelper.json_deserialize(self.response_catcher.response.text)
        assert ComparisonHelper.match_body(expected_body, received_body)

    # Get List of Languages
    def test_list_site_languages(self):

        # Perform the API call through the SDK function
        result = self.controller.list_site_languages()

        # Test response code
        assert self.response_catcher.response.status_code == 200

        # Test headers
        expected_headers = {}
        expected_headers['content-type'] = 'application/json'

        assert ComparisonHelper.match_headers(expected_headers, self.response_catcher.response.headers)

        
        # Test whether the captured response is as we expected
        assert result is not None
        expected_body = APIHelper.json_deserialize('[{"display":"English (US)","display_native":"English (US)","key":"'
            'en-US"},{"display":"Chinese Traditional (Taiwan)","display_native"'
            ':"中文（台灣）","key":"zh-TW"}]')
        received_body = APIHelper.json_deserialize(self.response_catcher.response.text)
        assert ComparisonHelper.match_body(expected_body, received_body)

    # Get License Types
    #
    def test_get_license_types(self):

        # Perform the API call through the SDK function
        result = self.controller.get_license_types()

        # Test response code
        assert self.response_catcher.response.status_code == 200

        # Test headers
        expected_headers = {}
        expected_headers['content-type'] = 'application/json'

        assert ComparisonHelper.match_headers(expected_headers, self.response_catcher.response.headers)

        
        # Test whether the captured response is as we expected
        assert result is not None
        expected_body = APIHelper.json_deserialize('[{"description":"Asset Visibility","key":"sub_ast","name":"SUB-AST'
            '"},{"description":"IoT Assurance","key":"sub_clnt","name":"SUB-CLN'
            'T"},{"description":"vBLE Engagement","key":"sub_eng","name":"SUB-E'
            'NG"},{"description":"Wired Assurance 12","includes":["sub_ex12a","'
            'sub_ex12p"],"key":"sub_ex12","name":"SUB-EX12"},{"description":"Wi'
            'red Assurance 12 Advanced","key":"sub_ex12a","name":"SUB-EX12A"},{'
            '"description":"Wired Assurance 12 Premium","key":"sub_ex12p","name'
            '":"SUB-EX12P"},{"description":"Wired Assurance 24","includes":["su'
            'b_ex24a","sub_ex24p"],"key":"sub_ex24","name":"SUB-EX24"},{"descri'
            'ption":"Wired Assurance 24 Advanced","key":"sub_ex24a","name":"SUB'
            '-EX24A"},{"description":"Wired Assurance 24 Premium","key":"sub_ex'
            '24p","name":"SUB-EX24P"},{"description":"Wired Assurance 48","incl'
            'udes":["sub_ex48a","sub_ex48p"],"key":"sub_ex48","name":"SUB-EX48"'
            '},{"description":"Wired Assurance 48 Advanced","key":"sub_ex48a","'
            'name":"SUB-EX48A"},{"description":"Wired Assurance 48 Premium","ke'
            'y":"sub_ex48p","name":"SUB-EX48P"},{"description":"WiFi Management'
            ' and Assurance","key":"sub_man","name":"SUB-MAN"},{"description":"'
            'Mist Edge","key":"sub_me","name":"SUB-ME"},{"description":"Premium'
            ' Analytics","key":"sub_pma","name":"SUB-PMA"},{"description":"Marv'
            'is for Wired Network","includes":["sub_svna4"],"key":"sub_svna","n'
            'ame":"SUB-SVNA"},{"description":"Marvis for Wired/EX and QFX Class'
            ' 4 devices","key":"sub_svna4","name":"SUB-SVNA4"},{"description":"'
            'Wired Assurance for Class 4","includes":["sub_sw4a","sub_sw4p"],"k'
            'ey":"sub_sw4","name":"SUB-SW4"},{"description":"Wired Assurance fo'
            'r Class 4 Advanced","key":"sub_sw4a","name":"SUB-SW4A"},{"descript'
            'ion":"Wired Assurance for Class 4 Premium","key":"sub_sw4p","name"'
            ':"SUB-SW4P"},{"description":"Marvis for Wireless","key":"sub_vna",'
            '"name":"SUB-VNA"},{"description":"WAN Assurance","key":"sub_wan","'
            'name":"SUB-WAN"},{"description":"WAN Assurance for Class 1","key":'
            '"sub_wan1","name":"SUB-WAN1"},{"description":"WAN Assurance for Cl'
            'ass 2","key":"sub_wan2","name":"SUB-WAN2"},{"description":"WAN Ass'
            'urance for Class 3","key":"sub_wan3","name":"SUB-WAN3"},{"descript'
            'ion":"WAN Assurance for Class 4","key":"sub_wan4","name":"SUB-WAN4'
            '"},{"description":"WAN Assurance for Class 5","key":"sub_wan5","na'
            'me":"SUB-WAN5"},{"description":"WAN Assurance for Class 6","key":"'
            'sub_wan6","name":"SUB-WAN6"},{"description":"Marvis for WAN","incl'
            'udes":["sub_wvna1","sub_wvna2","sub_wvna3","sub_wvna4","sub_wvna5"'
            ',"sub_wvna6"],"key":"sub_wvna","name":"SUB-WVNA"},{"description":"'
            'Marvis for WAN for SRX Class 1 devices","key":"sub_wvna1","name":"'
            'SUB-WVNA1"},{"description":"Marvis for WAN for SRX Class 2 devices'
            '","key":"sub_wvna2","name":"SUB-WVNA2"},{"description":"Marvis for'
            ' WAN for SRX Class 3 devices","key":"sub_wvna3","name":"SUB-WVNA3"'
            '},{"description":"Marvis for WAN for SRX Class 4 devices","key":"s'
            'ub_wvna4","name":"SUB-WVNA4"},{"description":"Marvis for WAN for S'
            'RX Class 5 devices","key":"sub_wvna5","name":"SUB-WVNA5"},{"descri'
            'ption":"Marvis for WAN for SRX Class 6 devices","key":"sub_wvna6",'
            '"name":"SUB-WVNA6"}]')
        received_body = APIHelper.json_deserialize(self.response_catcher.response.text)
        assert ComparisonHelper.match_body(expected_body, received_body)

    # Get List of available MX Edge Events
    def test_list_mx_edge_events_definitions(self):

        # Perform the API call through the SDK function
        result = self.controller.list_mx_edge_events_definitions()

        # Test response code
        assert self.response_catcher.response.status_code == 200

        # Test headers
        expected_headers = {}
        expected_headers['content-type'] = 'application/json'

        assert ComparisonHelper.match_headers(expected_headers, self.response_catcher.response.headers)

        
        # Test whether the captured response is as we expected
        assert result is not None
        expected_body = APIHelper.json_deserialize('[{"description":"Config change on ME was triggered as a result of '
            'change made by user","display":"ME Config changed by user","exampl'
            'e":{"audit_id":"e9a88814-fa81-5bdc-34b0-84e8735420e5","mxcluster_i'
            'd":"ed4665ed-c9ad-4835-8ca5-dda642765ad3","mxedge_id":"387804a7-34'
            '74-85ce-15a2-f9a9684c9c90","org_id":"2818e386-8dec-2562-9ede-5b8a0'
            'fbbdc71","service":"mxagent","site_id":"4ac1dcf4-9d8b-7211-65c4-05'
            '7819f0862b","timestamp":1552408871,"type":"ME_CONFIG_CHANGED_BY_US'
            'ER"},"key":"ME_CONFIG_CHANGED_BY_USER"}]')
        received_body = APIHelper.json_deserialize(self.response_catcher.response.text)
        assert ComparisonHelper.match_body(expected_body, received_body)

    # Get List of available Mx Edge models
    def test_list_mx_edge_models(self):

        # Perform the API call through the SDK function
        result = self.controller.list_mx_edge_models()

        # Test response code
        assert self.response_catcher.response.status_code == 200

        # Test headers
        expected_headers = {}
        expected_headers['content-type'] = 'application/json'

        assert ComparisonHelper.match_headers(expected_headers, self.response_catcher.response.headers)

        
        # Test whether the captured response is as we expected
        assert result is not None
        expected_body = APIHelper.json_deserialize('[{"custom_ports":true,"display":"string","model":"string","ports":'
            '{"0":{"display":"string","speed":0},"1":{"display":"string","speed'
            '":0},"2":{"display":"string","speed":0},"3":{"display":"string","s'
            'peed":0}}}]')
        received_body = APIHelper.json_deserialize(self.response_catcher.response.text)
        assert ComparisonHelper.match_body(expected_body, received_body)

    # Supported Events Type
    #
    def test_list_other_device_events_definitions(self):

        # Perform the API call through the SDK function
        result = self.controller.list_other_device_events_definitions()

        # Test response code
        assert self.response_catcher.response.status_code == 200

        # Test headers
        expected_headers = {}
        expected_headers['content-type'] = 'application/json'

        assert ComparisonHelper.match_headers(expected_headers, self.response_catcher.response.headers)

        
        # Test whether the captured response is as we expected
        assert result is not None
        expected_body = APIHelper.json_deserialize('[{"display":"Connected to NCM","example":{"device_mac":"5c5b351e13'
            'b5","mac":"0030447771c0","org_id":"c080ce4d-4e35-4373-bdc4-08df15d'
            '257f5","site_id":"1df889ad-9111-4c0e-a00b-8a008b83eb68","text":"Co'
            'nnected to NCM","timestamp":1675827825.765,"type":"CELLULAR_EDGE_C'
            'ONNECTED_TO_NCM","vendor":"cradlepoint"},"key":"CELLULAR_EDGE_CONN'
            'ECTED_TO_NCM"},{"display":"Disconnected from NCM","example":{"devi'
            'ce_mac":"5c5b351e13b5","mac":"0030447771c0","org_id":"c080ce4d-4e3'
            '5-4373-bdc4-08df15d257f5","site_id":"1df889ad-9111-4c0e-a00b-8a008'
            'b83eb68","text":"Disconnected from NCM","timestamp":1675827825.765'
            ',"type":"CELLULAR_EDGE_DISCONNECTED_FROM_NCM","vendor":"cradlepoin'
            't"},"key":"CELLULAR_EDGE_DISCONNECTED_FROM_NCM"}]')
        received_body = APIHelper.json_deserialize(self.response_catcher.response.text)
        assert ComparisonHelper.match_body(expected_body, received_body)

    # Get List of identified traffic
    def test_list_traffic_types(self):

        # Perform the API call through the SDK function
        result = self.controller.list_traffic_types()

        # Test response code
        assert self.response_catcher.response.status_code == 200

        # Test headers
        expected_headers = {}
        expected_headers['content-type'] = 'application/json'

        assert ComparisonHelper.match_headers(expected_headers, self.response_catcher.response.headers)

        
        # Test whether the captured response is as we expected
        assert result is not None
        expected_body = APIHelper.json_deserialize('[{"dscp":0,"failover_policy":"string","name":"string","traffic_cla'
            'ss":"string"}]')
        received_body = APIHelper.json_deserialize(self.response_catcher.response.text)
        assert ComparisonHelper.match_body(expected_body, received_body)

