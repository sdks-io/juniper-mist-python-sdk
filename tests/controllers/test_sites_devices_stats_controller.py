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


class SitesDevicesStatsControllerTests(ControllerTestBase):

    @classmethod
    def setUpClass(cls):
        super(SitesDevicesStatsControllerTests, cls).setUpClass()
        cls.controller = cls.client.sites_devices_stats
        cls.response_catcher = cls.controller.http_call_back

    # Count BGP Stats
    def test_count_site_bgp_stats(self):
        # Parameters for the API call
        site_id = '000000ab-00ab-00ab-00ab-0000000000ab'
        state = None
        distinct = None

        # Perform the API call through the SDK function
        result = self.controller.count_site_bgp_stats(site_id, state, distinct)

        # Test response code
        assert self.response_catcher.response.status_code == 200

        # Test headers
        expected_headers = {}
        expected_headers['content-type'] = 'application/json'

        assert ComparisonHelper.match_headers(expected_headers, self.response_catcher.response.headers)

        
        # Test whether the captured response is as we expected
        assert result is not None
        expected_body = APIHelper.json_deserialize('{"distinct":"string","end":0,"limit":0,"percentage":0,"results":[{'
            '"count":0,"property":"string"}],"start":0,"total":0}')
        received_body = APIHelper.json_deserialize(self.response_catcher.response.text)
        assert ComparisonHelper.match_body(expected_body, received_body)

    # Search BGP Stats
    def test_search_site_bgp_stats(self):
        # Parameters for the API call
        site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

        # Perform the API call through the SDK function
        result = self.controller.search_site_bgp_stats(site_id)

        # Test response code
        assert self.response_catcher.response.status_code == 200

        # Test headers
        expected_headers = {}
        expected_headers['content-type'] = 'application/json'

        assert ComparisonHelper.match_headers(expected_headers, self.response_catcher.response.headers)

        
        # Test whether the captured response is as we expected
        assert result is not None
        expected_body = APIHelper.json_deserialize('{"end":1619518989.4989712,"limit":10,"results":[{"as":65000,"mac":'
            '"020001c04668","neighbor":"15.8.3.5","neighbor_mac":"c15353123096"'
            ',"org_id":"0c160b7f-1027-4cd1-923b-744534c4b070","rx_pkts":63366,"'
            'rx_routes":60,"site_id":"725a8d34-a126-4f2c-b990-d1219421cb75","st'
            'ate":"established","tx_pkts":1735,"uptime":31355,"vrf_name":"defau'
            'lt"}],"start":1619518689.4989705,"total":1}')
        received_body = APIHelper.json_deserialize(self.response_catcher.response.text)
        assert ComparisonHelper.match_body(expected_body, received_body)

    # Get List of Site Devices Stats
    def test_list_site_devices_stats(self):
        # Parameters for the API call
        site_id = '000000ab-00ab-00ab-00ab-0000000000ab'
        mtype = 'ap'
        status = 'all'
        page = 1
        limit = 100

        # Perform the API call through the SDK function
        result = self.controller.list_site_devices_stats(site_id, mtype, status, page, limit)

        # Test response code
        assert self.response_catcher.response.status_code == 200

        # Test headers
        expected_headers = {}
        expected_headers['content-type'] = 'application/json'

        assert ComparisonHelper.match_headers(expected_headers, self.response_catcher.response.headers)

        
        # Test whether the captured response is as we expected
        assert result is not None
        expected_body = APIHelper.json_deserialize('[{"ble_config":{"beacon_rate":3,"beacon_rate_model":"custom","beam'
            '_disabled":[1,3,6],"power":10,"power_mode":"custom"},"ble_stat":{"'
            'beacon_rate":3,"eddystone_uid_enabled":false,"eddystone_uid_freq_m'
            'sec":200,"eddystone_uid_instance":"5c5b35000001","eddystone_uid_na'
            'mespace":"2818e3868dec25629ede","eddystone_url_enabled":true,"eddy'
            'stone_url_freq_msec":100,"eddystone_url_url":"https://www.abc.com"'
            ',"ibeacon_enabled":true,"ibeacon_major":13,"ibeacon_minor":138,"ib'
            'eacon_uuid":"f3f17139-704a-f03a-2786-0400279e37c3","major":12345,"'
            'minors":[201,202,203,204,205,206,207,208],"power":10,"rx_bytes":13'
            '5,"rx_pkts":135,"tx_bytes":5231513353,"tx_pkts":135135135,"tx_rese'
            'ts":0,"uuid":"ada72f8f-1643-e5c6-94db-f2a5636f1a64"},"cert_expiry"'
            ':1534534392,"ext_ip":"73.92.124.103","fwupdate":{"progress":10,"st'
            'atus":"inprogress","status_id":5,"timestamp":1428949501},"iot_stat'
            '":{"DI2":{"value":0}},"ip":"10.2.9.159","ip_config":{"dns":["8.8.8'
            '.8","4.4.4.4"],"dns_suffix":[".mist.local",".mist.com"],"gateway":'
            '"10.2.1.254","ip":"10.2.1.1","netmask":"255.255.255.0","type":"sta'
            'tic"},"ip_stat":{"dns":["8.8.8.8","4.4.4.4"],"dns_suffix":[".mist.'
            'local",".mist.com"],"gateway":"10.2.1.254","gateway6":"2607:f8b0:4'
            '005:808::1","ip":"10.2.1.1","ip6":"2607:f8b0:4005:808::2004","ips"'
            ':{"vlan1":"10.2.1.1/24,2607:f8b0:4005:808::1/32","vlan193":"10.73.'
            '1.31/16","vlan3157":"10.72.11.14/24"},"netmask":"255.255.255.0","n'
            'etmask6":"/32"},"l2tp_stat":{"7dae216d-7c98-a51b-e068-dd7d477b7216'
            '":{"sessions":[{"local_sid":31,"remote_id":"vpn1","remote_sid":13,'
            '"state":"established"}],"state":"established_with_sessions","uptim'
            'e":135,"wxtunnel_id":"7dae216d-7c98-a51b-e068-dd7d477b7216"}},"las'
            't_seen":1470417522,"last_trouble":{"code":"03","timestamp":1428949'
            '501},"led":{"brightness":255,"enabled":true},"lldp_stat":{"chassis'
            '_id":"63:68:61:73:73:69","lldp_med_supported":false,"mgmt_addr":"1'
            '0.1.5.2","port_desc":"2/26","power_allocated":15500,"power_draw":1'
            '5000,"power_request_count":3,"power_requested":25500,"system_desc"'
            ':"HP J9729A 2920-48G-POE+ Switch","system_name":"TC2-OWL-Stack-01"'
            '},"locating":false,"mac":"5c5b35000010","map_id":"63eda950-c6da-11'
            'e4-a628-60f81dd250cc","mesh_downlinks":{"00000000-0000-0000-1000-5'
            'c5b356be59f":{"band":"24","channel":7,"idle_time":3,"last_seen":14'
            '70417522,"proto":"a","rssi":-65,"rx_bps":12,"rx_bytes":217416,"rx_'
            'packets":2337,"rx_rate":65,"rx_retries":5,"snr":31,"tx_bps":6,"tx_'
            'bytes":175132,"tx_packets":1566,"tx_rate":65,"tx_retries":500}},"m'
            'esh_uplink":{"band":"24","channel":7,"idle_time":3,"last_seen":147'
            '0417522,"proto":"a","rssi":-65,"rx_bps":12,"rx_bytes":217416,"rx_p'
            'ackets":2337,"rx_rate":65,"rx_retries":5,"snr":31,"tx_bps":6,"tx_b'
            'ytes":175132,"tx_packets":1566,"tx_rate":65,"tx_retries":500,"upli'
            'nk_ap_id":"00000000-0000-0000-1000-5c5b35000010"},"model":"AP200",'
            '"name":"conference room","num_clients":10,"port_stat":{"eth0":{"fu'
            'll_duplex":true,"rx_bytes":2056,"rx_errors":0,"rx_pkts":670,"speed'
            '":1000,"tx_bytes":2056,"tx_pkts":670,"up":true},"eth1":{"up":false'
            '},"module":{"up":false}},"power_budget":-12000,"power_src":"PoE 80'
            '2.3af","radio_config":{"band_24":{"bandwidth":20,"channel":0,"dyna'
            'mic_chaining_enabled":false,"power":0,"rx_chain":4,"tx_chain":4},"'
            'band_5":{"bandwidth":40,"channel":0,"dynamic_chaining_enabled":fal'
            'se,"power":0,"rx_chain":4,"tx_chain":1},"scanning_enabled":true},"'
            'radio_stat":{"band_24":{"bandwidth":20,"channel":6,"mac":"5c5b3500'
            '04a0","num_clients":6,"power":19,"rx_bytes":8504737800,"rx_pkts":5'
            '7731964,"tx_bytes":211166512114,"tx_pkts":812058566},"band_5":{"ba'
            'ndwidth":80,"channel":44,"mac":"5c5b350004b0","num_clients":4,"pow'
            'er":15,"rx_bytes":10366616,"rx_pkts":38603,"tx_bytes":50877568,"tx'
            '_pkts":145496}},"rx_bps":60003,"rx_bytes":8515104416,"rx_pkts":577'
            '70567,"serial":"FXLH2015170017","status":"connected","tx_bps":6343'
            '01,"tx_bytes":211217389682,"tx_pkts":812204062,"type":"ap","uptime'
            '":13500,"usb_stat":{"channel":3,"connected":true,"last_activity":1'
            '586873254,"type":"imagotag","up":true},"version":"1.0.0","x":53.5,'
            '"y":173.1}]')
        received_body = APIHelper.json_deserialize(self.response_catcher.response.text)
        assert ComparisonHelper.match_body(expected_body, received_body)

    # Get Site Device Stats Details
    def test_get_site_device_stats(self):
        # Parameters for the API call
        site_id = '000000ab-00ab-00ab-00ab-0000000000ab'
        device_id = '000000ab-00ab-00ab-00ab-0000000000ab'

        # Perform the API call through the SDK function
        result = self.controller.get_site_device_stats(site_id, device_id)

        # Test response code
        assert self.response_catcher.response.status_code == 200

        # Test headers
        expected_headers = {}
        expected_headers['content-type'] = 'application/json'

        assert ComparisonHelper.match_headers(expected_headers, self.response_catcher.response.headers)

        
        # Test whether the captured response is as we expected
        assert result is not None
        expected_body = APIHelper.json_deserialize('{"ble_config":{"beacon_rate":3,"beacon_rate_model":"custom","beam_'
            'disabled":[1,3,6],"power":10,"power_mode":"custom"},"ble_stat":{"b'
            'eacon_rate":3,"eddystone_uid_enabled":false,"eddystone_uid_freq_ms'
            'ec":200,"eddystone_uid_instance":"5c5b35000001","eddystone_uid_nam'
            'espace":"2818e3868dec25629ede","eddystone_url_enabled":true,"eddys'
            'tone_url_freq_msec":100,"eddystone_url_url":"https://www.abc.com",'
            '"ibeacon_enabled":true,"ibeacon_major":13,"ibeacon_minor":138,"ibe'
            'acon_uuid":"f3f17139-704a-f03a-2786-0400279e37c3","major":12345,"m'
            'inors":[201,202,203,204,205,206,207,208],"power":10,"rx_bytes":135'
            ',"rx_pkts":135,"tx_bytes":5231513353,"tx_pkts":135135135,"tx_reset'
            's":0,"uuid":"ada72f8f-1643-e5c6-94db-f2a5636f1a64"},"cert_expiry":'
            '1534534392,"ext_ip":"73.92.124.103","fwupdate":{"progress":10,"sta'
            'tus":"inprogress","status_id":5,"timestamp":1428949501},"iot_stat"'
            ':{"DI2":{"value":0}},"ip":"10.2.9.159","ip_config":{"dns":["8.8.8.'
            '8","4.4.4.4"],"dns_suffix":[".mist.local",".mist.com"],"gateway":"'
            '10.2.1.254","ip":"10.2.1.1","netmask":"255.255.255.0","type":"stat'
            'ic"},"ip_stat":{"dns":["8.8.8.8","4.4.4.4"],"dns_suffix":[".mist.l'
            'ocal",".mist.com"],"gateway":"10.2.1.254","gateway6":"2607:f8b0:40'
            '05:808::1","ip":"10.2.1.1","ip6":"2607:f8b0:4005:808::2004","ips":'
            '{"vlan1":"10.2.1.1/24,2607:f8b0:4005:808::1/32","vlan193":"10.73.1'
            '.31/16","vlan3157":"10.72.11.14/24"},"netmask":"255.255.255.0","ne'
            'tmask6":"/32"},"l2tp_stat":{"7dae216d-7c98-a51b-e068-dd7d477b7216"'
            ':{"sessions":[{"local_sid":31,"remote_id":"vpn1","remote_sid":13,"'
            'state":"established"}],"state":"established_with_sessions","uptime'
            '":135,"wxtunnel_id":"7dae216d-7c98-a51b-e068-dd7d477b7216"}},"last'
            '_seen":1470417522,"last_trouble":{"code":"03","timestamp":14289495'
            '01},"led":{"brightness":255,"enabled":true},"lldp_stat":{"chassis_'
            'id":"63:68:61:73:73:69","lldp_med_supported":false,"mgmt_addr":"10'
            '.1.5.2","port_desc":"2/26","power_allocated":15500,"power_draw":15'
            '000,"power_request_count":3,"power_requested":25500,"system_desc":'
            '"HP J9729A 2920-48G-POE+ Switch","system_name":"TC2-OWL-Stack-01"}'
            ',"locating":false,"mac":"5c5b35000010","map_id":"63eda950-c6da-11e'
            '4-a628-60f81dd250cc","mesh_downlinks":{"00000000-0000-0000-1000-5c'
            '5b356be59f":{"band":"24","channel":7,"idle_time":3,"last_seen":147'
            '0417522,"proto":"a","rssi":-65,"rx_bps":12,"rx_bytes":217416,"rx_p'
            'ackets":2337,"rx_rate":65,"rx_retries":5,"snr":31,"tx_bps":6,"tx_b'
            'ytes":175132,"tx_packets":1566,"tx_rate":65,"tx_retries":500}},"me'
            'sh_uplink":{"band":"24","channel":7,"idle_time":3,"last_seen":1470'
            '417522,"proto":"a","rssi":-65,"rx_bps":12,"rx_bytes":217416,"rx_pa'
            'ckets":2337,"rx_rate":65,"rx_retries":5,"snr":31,"tx_bps":6,"tx_by'
            'tes":175132,"tx_packets":1566,"tx_rate":65,"tx_retries":500,"uplin'
            'k_ap_id":"00000000-0000-0000-1000-5c5b35000010"},"model":"AP200","'
            'name":"conference room","num_clients":10,"port_stat":{"eth0":{"ful'
            'l_duplex":true,"rx_bytes":2056,"rx_errors":0,"rx_pkts":670,"speed"'
            ':1000,"tx_bytes":2056,"tx_pkts":670,"up":true},"eth1":{"up":false}'
            ',"module":{"up":false}},"power_budget":-12000,"power_src":"PoE 802'
            '.3af","radio_config":{"band_24":{"bandwidth":20,"channel":0,"dynam'
            'ic_chaining_enabled":false,"power":0,"rx_chain":4,"tx_chain":4},"b'
            'and_5":{"bandwidth":40,"channel":0,"dynamic_chaining_enabled":fals'
            'e,"power":0,"rx_chain":4,"tx_chain":1},"scanning_enabled":true},"r'
            'adio_stat":{"band_24":{"bandwidth":20,"channel":6,"mac":"5c5b35000'
            '4a0","num_clients":6,"power":19,"rx_bytes":8504737800,"rx_pkts":57'
            '731964,"tx_bytes":211166512114,"tx_pkts":812058566},"band_5":{"ban'
            'dwidth":80,"channel":44,"mac":"5c5b350004b0","num_clients":4,"powe'
            'r":15,"rx_bytes":10366616,"rx_pkts":38603,"tx_bytes":50877568,"tx_'
            'pkts":145496}},"rx_bps":60003,"rx_bytes":8515104416,"rx_pkts":5777'
            '0567,"serial":"FXLH2015170017","status":"connected","tx_bps":63430'
            '1,"tx_bytes":211217389682,"tx_pkts":812204062,"type":"ap","uptime"'
            ':13500,"usb_stat":{"channel":3,"connected":true,"last_activity":15'
            '86873254,"type":"imagotag","up":true},"version":"1.0.0","x":53.5,"'
            'y":173.1}')
        received_body = APIHelper.json_deserialize(self.response_catcher.response.text)
        assert ComparisonHelper.match_body(expected_body, received_body)

    # Get wireless client stat by Device
    def test_get_site_all_clients_stats_by_device(self):
        # Parameters for the API call
        site_id = '000000ab-00ab-00ab-00ab-0000000000ab'
        device_id = '000000ab-00ab-00ab-00ab-0000000000ab'

        # Perform the API call through the SDK function
        result = self.controller.get_site_all_clients_stats_by_device(site_id, device_id)

        # Test response code
        assert self.response_catcher.response.status_code == 200

        # Test headers
        expected_headers = {}
        expected_headers['content-type'] = 'application/json'

        assert ComparisonHelper.match_headers(expected_headers, self.response_catcher.response.headers)

        
        # Test whether the captured response is as we expected
        assert result is not None
        expected_body = APIHelper.json_deserialize('[{"_ttl":0,"accuracy":0,"airespace_ifname":"string","airwatch":{"a'
            'uthorized":true},"ap_id":"b069b358-4c97-5319-1f8c-7c5ca64d6ab1","a'
            'p_mac":"string","band":"24","channel":0,"dual_band":true,"family":'
            '"string","guest":{"authorized":true,"authorized_expiring_time":0,"'
            'authorized_time":0,"company":"string","email":"string","field1":"s'
            'tring","name":"string"},"hostname":"string","id":"b069b358-4c97-53'
            '19-1f8c-7c5ca64d6ab1","idle_time":0,"ip":"192.168.1.2","is_guest":'
            'true,"key_mgmt":"string","last_seen":0,"mac":"string","manufacture'
            '":"string","map_id":"b069b358-4c97-5319-1f8c-7c5ca64d6ab1","model"'
            ':"string","name":"string","num_locating_aps":0,"os":"string","powe'
            'r_saving":true,"proto":"ac","psk_id":"6f4bf402-45f9-2a56-6c8b-7f83'
            'd3bc98e9","rssi":0,"rx_bps":0,"rx_bytes":0,"rx_packets":0,"rx_rate'
            '":0,"rx_retries":0,"snr":0,"ssid":"string","tx_bps":0,"tx_bytes":0'
            ',"tx_packets":0,"tx_rate":0,"tx_retries":0,"type":"string","uptime'
            '":0,"username":"string","vlan_id":1,"wlan_id":"b069b358-4c97-5319-'
            '1f8c-7c5ca64d6ab1","x":0,"y":0}]')
        received_body = APIHelper.json_deserialize(self.response_catcher.response.text)
        assert ComparisonHelper.match_body(expected_body, received_body)

    # Get List of Site MxEdges Stats
    def test_list_site_mx_edges_stats(self):
        # Parameters for the API call
        site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

        # Perform the API call through the SDK function
        result = self.controller.list_site_mx_edges_stats(site_id)

        # Test response code
        assert self.response_catcher.response.status_code == 200

        # Test headers
        expected_headers = {}
        expected_headers['content-type'] = 'application/json'

        assert ComparisonHelper.match_headers(expected_headers, self.response_catcher.response.headers)

        
        # Test whether the captured response is as we expected
        assert result is not None
        expected_body = APIHelper.json_deserialize('[{"cpu_stat":{"cpus":{"property1":{"idle":0,"interrupt":0,"system"'
            ':0,"usage":0,"user":0},"property2":{"idle":0,"interrupt":0,"system'
            '":0,"usage":0,"user":0}},"idle":0,"interrupt":0,"system":0,"usage"'
            ':0,"user":0},"created_time":0,"for_site":true,"id":"493f6eca-6276-'
            '4993-bfeb-83cbbbba6f08","ip_stat":{"ip":"string","ips":{"property1'
            '":"string","property2":"string"}},"lag_stat":{},"last_seen":0,"mac'
            '":"string","memory_stat":{"active":0,"available":0,"buffers":0,"ca'
            'ched":0,"free":0,"inactive":0,"swap_cached":0,"swap_free":0,"swap_'
            'total":0,"total":0,"usage":0},"model":"string","modified_time":0,"'
            'mxagent_registered":true,"mxcluster_id":"de779d5f-583c-4a9c-b212-6'
            '105ad1a78b6","name":"string","num_tunnels":0,"org_id":"a40f5d1f-d8'
            '89-42e9-94ea-b9b33585fc6b","port_stat":{"property1":{"full_duplex"'
            ':true,"mac":"string","rx_bytes":0,"rx_errors":0,"rx_pkts":0,"speed'
            '":0,"state":"string","tx_bytes":0,"tx_errors":0,"tx_pkts":0,"up":t'
            'rue},"property2":{"full_duplex":true,"mac":"string","rx_bytes":0,"'
            'rx_errors":0,"rx_pkts":0,"speed":0,"state":"string","tx_bytes":0,"'
            'tx_errors":0,"tx_pkts":0,"up":true}},"sensor_stat":{},"service_sta'
            't":{"mxagent":{"ext_ip":"string","last_seen":0,"package_state":"st'
            'ring","package_version":"string","running_state":"string","uptime"'
            ':0},"tunterm":{"ext_ip":"string","last_seen":0,"package_state":"st'
            'ring","package_version":"string","running_state":"string","uptime"'
            ':0}},"services":[{}],"site_id":"72771e6a-6f5e-4de4-a5b9-1266c41978'
            '11","status":"string","tunterm_id":"811edbcf-b497-4977-b6d1-40d54c'
            'f871a5","tunterm_ip_config":{"gateway":"string","ip":"string","net'
            'mask":"string"},"tunterm_port_config":{"downstream_ports":[{}],"se'
            'parate_upstream_downstream":true,"upstream_ports":[{}]},"tunterm_r'
            'egistered":true,"tunterm_stat":{"monitoring_failed":true},"uptime"'
            ':0,"virtualization_type":"string"}]')
        received_body = APIHelper.json_deserialize(self.response_catcher.response.text)
        assert ComparisonHelper.match_body(expected_body, received_body)

    # Get One Site MxEdge Stats
    def test_get_site_mx_edge_stats(self):
        # Parameters for the API call
        site_id = '000000ab-00ab-00ab-00ab-0000000000ab'
        mxedge_id = '000000ab-00ab-00ab-00ab-0000000000ab'

        # Perform the API call through the SDK function
        result = self.controller.get_site_mx_edge_stats(site_id, mxedge_id)

        # Test response code
        assert self.response_catcher.response.status_code == 200

        # Test headers
        expected_headers = {}
        expected_headers['content-type'] = 'application/json'

        assert ComparisonHelper.match_headers(expected_headers, self.response_catcher.response.headers)

        
        # Test whether the captured response is as we expected
        assert result is not None
        expected_body = APIHelper.json_deserialize('{"cpu_stat":{"cpus":{"property1":{"idle":0,"interrupt":0,"system":'
            '0,"usage":0,"user":0},"property2":{"idle":0,"interrupt":0,"system"'
            ':0,"usage":0,"user":0}},"idle":0,"interrupt":0,"system":0,"usage":'
            '0,"user":0},"created_time":0,"for_site":true,"id":"492f6eca-6276-4'
            '993-bfeb-93cbbbba6f08","ip_stat":{"ip":"string","ips":{"property1"'
            ':"string","property2":"string"}},"lag_stat":{},"last_seen":0,"mac"'
            ':"string","memory_stat":{"active":0,"available":0,"buffers":0,"cac'
            'hed":0,"free":0,"inactive":0,"swap_cached":0,"swap_free":0,"swap_t'
            'otal":0,"total":0,"usage":0},"model":"string","modified_time":0,"m'
            'xagent_registered":true,"mxcluster_id":"de779d5f-583c-4a9c-b212-61'
            '05ad1a78b6","name":"string","num_tunnels":0,"org_id":"a40f5d1f-d88'
            '9-42e9-94ea-b9b33585fc6b","port_stat":{"property1":{"full_duplex":'
            'true,"mac":"string","rx_bytes":0,"rx_errors":0,"rx_pkts":0,"speed"'
            ':0,"state":"string","tx_bytes":0,"tx_errors":0,"tx_pkts":0,"up":tr'
            'ue},"property2":{"full_duplex":true,"mac":"string","rx_bytes":0,"r'
            'x_errors":0,"rx_pkts":0,"speed":0,"state":"string","tx_bytes":0,"t'
            'x_errors":0,"tx_pkts":0,"up":true}},"sensor_stat":{},"service_stat'
            '":{"mxagent":{"ext_ip":"string","last_seen":0,"package_state":"str'
            'ing","package_version":"string","running_state":"string","uptime":'
            '0},"tunterm":{"ext_ip":"string","last_seen":0,"package_state":"str'
            'ing","package_version":"string","running_state":"string","uptime":'
            '0}},"services":[{}],"site_id":"72771e6a-6f5e-4de4-a5b9-1266c419781'
            '1","status":"string","tunterm_id":"811edbcf-b497-4977-b6d1-40d54cf'
            '871a5","tunterm_ip_config":{"gateway":"string","ip":"string","netm'
            'ask":"string"},"tunterm_port_config":{"downstream_ports":[{}],"sep'
            'arate_upstream_downstream":true,"upstream_ports":[{}]},"tunterm_re'
            'gistered":true,"tunterm_stat":{"monitoring_failed":true},"uptime":'
            '0,"virtualization_type":"string"}')
        received_body = APIHelper.json_deserialize(self.response_catcher.response.text)
        assert ComparisonHelper.match_body(expected_body, received_body)

    # Count by Distinct Attributes of Switch/Gateway Ports
    def test_count_site_sw_or_gw_ports(self):
        # Parameters for the API call
        site_id = '000000ab-00ab-00ab-00ab-0000000000ab'
        distinct = 'mac'
        full_duplex = None
        mac = None
        neighbor_mac = None
        neighbor_port_desc = None
        neighbor_system_name = None
        poe_disabled = None
        poe_mode = None
        poe_on = None
        port_id = None
        port_mac = None
        power_draw = None
        tx_pkts = None
        rx_pkts = None
        rx_bytes = None
        tx_bps = None
        rx_bps = None
        tx_mcast_pkts = None
        tx_bcast_pkts = None
        rx_mcast_pkts = None
        rx_bcast_pkts = None
        speed = None
        stp_state = None
        stp_role = None
        auth_state = None
        up = None
        page = 1
        limit = 100
        start = 0
        end = 0
        duration = '1d'

        # Perform the API call through the SDK function
        result = self.controller.count_site_sw_or_gw_ports(site_id, distinct, full_duplex, mac, neighbor_mac, neighbor_port_desc, neighbor_system_name, poe_disabled, poe_mode, poe_on, port_id, port_mac, power_draw, tx_pkts, rx_pkts, rx_bytes, tx_bps, rx_bps, tx_mcast_pkts, tx_bcast_pkts, rx_mcast_pkts, rx_bcast_pkts, speed, stp_state, stp_role, auth_state, up, page, limit, start, end, duration)

        # Test response code
        assert self.response_catcher.response.status_code == 200

        # Test headers
        expected_headers = {}
        expected_headers['content-type'] = 'application/json'

        assert ComparisonHelper.match_headers(expected_headers, self.response_catcher.response.headers)

        
        # Test whether the captured response is as we expected
        assert result is not None
        expected_body = APIHelper.json_deserialize('{"distinct":"mac","end":1513177200,"limit":100,"results":[{"count"'
            ':217,"mac":"112233445566"},{"count":35,"mac":"001122334455"}],"sta'
            'rt":1511967600,"total":20}')
        received_body = APIHelper.json_deserialize(self.response_catcher.response.text)
        assert ComparisonHelper.match_body(expected_body, received_body)

    # Search Switch / Gateway Ports
    def test_search_site_sw_or_gw_ports(self):
        # Parameters for the API call
        site_id = '000000ab-00ab-00ab-00ab-0000000000ab'
        full_duplex = None
        mac = None
        mtype = None
        neighbor_mac = None
        neighbor_port_desc = None
        neighbor_system_name = None
        poe_disabled = None
        poe_mode = None
        poe_on = None
        port_id = None
        port_mac = None
        power_draw = None
        tx_pkts = None
        rx_pkts = None
        rx_bytes = None
        tx_bps = None
        rx_bps = None
        tx_errors = None
        rx_errors = None
        tx_mcast_pkts = None
        tx_bcast_pkts = None
        rx_mcast_pkts = None
        rx_bcast_pkts = None
        speed = None
        mac_limit = None
        mac_count = None
        up = None
        active = None
        jitter = None
        loss = None
        latency = None
        stp_state = None
        stp_role = None
        xcvr_part_number = None
        auth_state = None
        lte_imsi = None
        lte_iccid = None
        lte_imei = None
        limit = 100
        start = 0
        end = 0
        duration = '1d'

        # Perform the API call through the SDK function
        result = self.controller.search_site_sw_or_gw_ports(site_id, full_duplex, mac, mtype, neighbor_mac, neighbor_port_desc, neighbor_system_name, poe_disabled, poe_mode, poe_on, port_id, port_mac, power_draw, tx_pkts, rx_pkts, rx_bytes, tx_bps, rx_bps, tx_errors, rx_errors, tx_mcast_pkts, tx_bcast_pkts, rx_mcast_pkts, rx_bcast_pkts, speed, mac_limit, mac_count, up, active, jitter, loss, latency, stp_state, stp_role, xcvr_part_number, auth_state, lte_imsi, lte_iccid, lte_imei, limit, start, end, duration)

        # Test response code
        assert self.response_catcher.response.status_code == 200

        # Test headers
        expected_headers = {}
        expected_headers['content-type'] = 'application/json'

        assert ComparisonHelper.match_headers(expected_headers, self.response_catcher.response.headers)

        
        # Test whether the captured response is as we expected
        assert result is not None
        expected_body = APIHelper.json_deserialize('{"end":1513177200,"limit":10,"results":[{"mac":"5c4527a96580","nei'
            'ghbor_mac":"64d814353400","neighbor_port_desc":"GigabitEthernet1/0'
            '/21","neighbor_system_name":"CORP-D-SW-2","org_id":"c168ddee-c14c-'
            '11e5-8e81-1258369c38a9","poe_disabled":true,"port_id":"me0","port_'
            'mac":"5c4527a96580","rx_bytes":4563443626,"rx_pkts":30360265,"site'
            '_id":"c1698122-c14c-11e5-8e81-1258369c38a9","speed":1000,"tx_bytes'
            '":11299516780,"tx_pkts":14610886,"up":true},{"full_duplex":true,"m'
            'ac":"0c8126c6ff6c","neighbor_mac":"5c5b350eb361","neighbor_port_de'
            'sc":"ETH0","neighbor_system_name":"kevinsap","org_id":"c168ddee-c1'
            '4c-11e5-8e81-1258369c38a9","poe_mode":"802.3at","poe_on":true,"por'
            't_id":"ge-0/0/0","port_mac":"0c8126c6ff6f","power_draw":5.4,"rx_bp'
            's":1176,"rx_bytes":2628451,"rx_pkts":11829,"site_id":"c1698122-c14'
            'c-11e5-8e81-1258369c38a9","speed":1000,"tx_bps":14264,"tx_bytes":9'
            '6810192,"tx_pkts":492176,"up":true}],"start":1511967600,"total":10'
            '0}')
        received_body = APIHelper.json_deserialize(self.response_catcher.response.text)
        assert ComparisonHelper.match_body(expected_body, received_body)

    # Count by Distinct Attributes of Switch/Gateway Ports
    def test_count_site_switch_ports(self):
        # Parameters for the API call
        site_id = '000000ab-00ab-00ab-00ab-0000000000ab'
        distinct = 'mac'
        full_duplex = None
        mac = None
        neighbor_mac = None
        neighbor_port_desc = None
        neighbor_system_name = None
        poe_disabled = None
        poe_mode = None
        poe_on = None
        port_id = None
        port_mac = None
        power_draw = None
        tx_pkts = None
        rx_pkts = None
        rx_bytes = None
        tx_bps = None
        rx_bps = None
        tx_mcast_pkts = None
        tx_bcast_pkts = None
        rx_mcast_pkts = None
        rx_bcast_pkts = None
        speed = None
        stp_state = None
        stp_role = None
        auth_state = None
        up = None
        page = 1
        limit = 100
        start = 0
        end = 0
        duration = '1d'

        # Perform the API call through the SDK function
        result = self.controller.count_site_switch_ports(site_id, distinct, full_duplex, mac, neighbor_mac, neighbor_port_desc, neighbor_system_name, poe_disabled, poe_mode, poe_on, port_id, port_mac, power_draw, tx_pkts, rx_pkts, rx_bytes, tx_bps, rx_bps, tx_mcast_pkts, tx_bcast_pkts, rx_mcast_pkts, rx_bcast_pkts, speed, stp_state, stp_role, auth_state, up, page, limit, start, end, duration)

        # Test response code
        assert self.response_catcher.response.status_code == 200

        # Test headers
        expected_headers = {}
        expected_headers['content-type'] = 'application/json'

        assert ComparisonHelper.match_headers(expected_headers, self.response_catcher.response.headers)

        
        # Test whether the captured response is as we expected
        assert result is not None
        expected_body = APIHelper.json_deserialize('{"distinct":"mac","end":1513177200,"limit":100,"results":[{"count"'
            ':217,"mac":"112233445566"},{"count":35,"mac":"001122334455"}],"sta'
            'rt":1511967600,"total":20}')
        received_body = APIHelper.json_deserialize(self.response_catcher.response.text)
        assert ComparisonHelper.match_body(expected_body, received_body)

    # Search Switch / Gateway Ports
    def test_search_site_switch_ports(self):
        # Parameters for the API call
        site_id = '000000ab-00ab-00ab-00ab-0000000000ab'
        full_duplex = None
        mac = None
        neighbor_mac = None
        neighbor_port_desc = None
        neighbor_system_name = None
        poe_disabled = None
        poe_mode = None
        poe_on = None
        port_id = None
        port_mac = None
        power_draw = None
        tx_pkts = None
        rx_pkts = None
        rx_bytes = None
        tx_bps = None
        rx_bps = None
        tx_mcast_pkts = None
        tx_bcast_pkts = None
        rx_mcast_pkts = None
        rx_bcast_pkts = None
        speed = None
        stp_state = None
        stp_role = None
        auth_state = None
        up = None
        limit = 100
        start = 0
        end = 0
        duration = '1d'

        # Perform the API call through the SDK function
        result = self.controller.search_site_switch_ports(site_id, full_duplex, mac, neighbor_mac, neighbor_port_desc, neighbor_system_name, poe_disabled, poe_mode, poe_on, port_id, port_mac, power_draw, tx_pkts, rx_pkts, rx_bytes, tx_bps, rx_bps, tx_mcast_pkts, tx_bcast_pkts, rx_mcast_pkts, rx_bcast_pkts, speed, stp_state, stp_role, auth_state, up, limit, start, end, duration)

        # Test response code
        assert self.response_catcher.response.status_code == 200

        # Test headers
        expected_headers = {}
        expected_headers['content-type'] = 'application/json'

        assert ComparisonHelper.match_headers(expected_headers, self.response_catcher.response.headers)

        
        # Test whether the captured response is as we expected
        assert result is not None
        expected_body = APIHelper.json_deserialize('{"end":1513177200,"limit":10,"results":[{"mac":"5c4527a96580","nei'
            'ghbor_mac":"64d814353400","neighbor_port_desc":"GigabitEthernet1/0'
            '/21","neighbor_system_name":"CORP-D-SW-2","org_id":"c168ddee-c14c-'
            '11e5-8e81-1258369c38a9","poe_disabled":true,"port_id":"me0","port_'
            'mac":"5c4527a96580","rx_bytes":4563443626,"rx_pkts":30360265,"site'
            '_id":"c1698122-c14c-11e5-8e81-1258369c38a9","speed":1000,"tx_bytes'
            '":11299516780,"tx_pkts":14610886,"up":true},{"full_duplex":true,"m'
            'ac":"0c8126c6ff6c","neighbor_mac":"5c5b350eb361","neighbor_port_de'
            'sc":"ETH0","neighbor_system_name":"kevinsap","org_id":"c168ddee-c1'
            '4c-11e5-8e81-1258369c38a9","poe_mode":"802.3at","poe_on":true,"por'
            't_id":"ge-0/0/0","port_mac":"0c8126c6ff6f","power_draw":5.4,"rx_bp'
            's":1176,"rx_bytes":2628451,"rx_pkts":11829,"site_id":"c1698122-c14'
            'c-11e5-8e81-1258369c38a9","speed":1000,"tx_bps":14264,"tx_bytes":9'
            '6810192,"tx_pkts":492176,"up":true}],"start":1511967600,"total":10'
            '0}')
        received_body = APIHelper.json_deserialize(self.response_catcher.response.text)
        assert ComparisonHelper.match_body(expected_body, received_body)

