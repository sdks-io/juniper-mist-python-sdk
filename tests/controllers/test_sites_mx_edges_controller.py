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
from mistapi.models.mxedge import Mxedge


class SitesMxEdgesControllerTests(ControllerTestBase):

    @classmethod
    def setUpClass(cls):
        super(SitesMxEdgesControllerTests, cls).setUpClass()
        cls.controller = cls.client.sites_mx_edges
        cls.response_catcher = cls.controller.http_call_back

    # Get List of Site Mist Edges
    def test_list_site_mx_edges(self):
        # Parameters for the API call
        site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

        # Perform the API call through the SDK function
        result = self.controller.list_site_mx_edges(site_id)

        # Test response code
        assert self.response_catcher.response.status_code == 200

        # Test headers
        expected_headers = {}
        expected_headers['content-type'] = 'application/json'

        assert ComparisonHelper.match_headers(expected_headers, self.response_catcher.response.headers)

        
        # Test whether the captured response is as we expected
        assert result is not None
        expected_body = APIHelper.json_deserialize('[{"cpu_stat":{"cpus":{"cpu0":{"idle":79,"interrupt":0,"system":4,"'
            'usage":20,"user":16},"cpu1":{"idle":93,"interrupt":0,"system":4,"u'
            'sage":6,"user":1}},"idle":87,"interrupt":0,"system":5,"usage":12,"'
            'user":7},"ext_ip":"116.187.144.16","id":"387804a7-3474-85ce-15a2-f'
            '9a9684c9c90","ip_stat":{"ip":"172.16.5.3","ips":{"ens192":"172.16.'
            '5.3/24,fe81::20c:29ff:fef8:d18e/64"}},"lag_stat":{"lag0":{"active_'
            'ports":["0","1"]}},"last_seen":1547437078,"magic":"ExNpT5gi-ADR8WT'
            'Fd4EiQPY3cP5WdSoD","memory_stats":{"active":1061085184,"available"'
            ':4124860416,"buffers":789495808,"cached":718016512,"free":28188385'
            '28,"inactive":458158080,"swap_cached":0,"swap_free":8161062912,"sw'
            'ap_total":8161062912,"total":7947616256,"usage":65},"model":"ME-S2'
            '019","mxagent_registered":false,"mxcluster_id":"572586b7-f97b-a22b'
            '-526c-8b97a3f609c4","name":"Guest","num_tunnels":31,"port_stat":{"'
            'eth0":{"full_duplex":true,"lldp_stats":{"mgmt_addr":"122.16.3.11",'
            '"port_desc":"GigabitEthernet4/0/16","port_id":"\\u0005Gi4/0/16","s'
            'ystem_desc":"Cisco IOS Software","system_name":"ME-DC2-DIS-SW"},"r'
            'x_bytes":2056,"rx_errors":0,"rx_pkts":670,"speed":1000,"tx_bytes":'
            '2056,"tx_pkts":670,"up":true},"eth1":{"up":false},"module":{"up":f'
            'alse}},"status":"connected","tunterm_registered":false,"tunterm_st'
            'at":{"monitoring_failed":false},"uptime":884221,"version":"0.1.2",'
            '"virtualization_type":"VirtualizationVMware"}]')
        received_body = APIHelper.json_deserialize(self.response_catcher.response.text)
        assert ComparisonHelper.match_body(expected_body, received_body)

    # Create Site Mist Edge
    def test_create_site_mx_edge(self):
        # Parameters for the API call
        site_id = '000000ab-00ab-00ab-00ab-0000000000ab'
        body = None

        # Perform the API call through the SDK function
        result = self.controller.create_site_mx_edge(site_id, body)

        # Test response code
        assert self.response_catcher.response.status_code == 200

        # Test headers
        expected_headers = {}
        expected_headers['content-type'] = 'application/json'

        assert ComparisonHelper.match_headers(expected_headers, self.response_catcher.response.headers)

        
        # Test whether the captured response is as we expected
        assert result is not None
        expected_body = APIHelper.json_deserialize('{"id":"95ddd29a-6a3c-929e-a431-51a5b09f36a6","magic":"L-NpT5gi-ADR'
            '8WTFd4EiQPY3cP5WdSoD","model":"ME-100","mxagent_registered":true,"'
            'mxcluster_id":"572586b7-f97b-a22b-526c-8b97a3f609c4","mxedge_mgmt"'
            ':{"mist_password":"MIST_PASSWORD","root_password":"ROOT_PASSWORD"}'
            ',"name":"Guest","ntp_servers":[],"oob_ip_config":{"dns":["8.8.8.8"'
            ',"4.4.4.4"],"gateway":"10.2.1.254","ip":"10.2.1.10","netmask":"255'
            '.255.255.0","type":"static"},"tunterm_dhcpd_config":{"2":{"enabled'
            '":true,"servers":["11.2.3.44"]},"enabled":false,"servers":["11.2.3'
            '.4"]},"tunterm_extra_routes":{"11.0.0.0/8":{"via":"10.3.3.1"}},"tu'
            'nterm_ip_config":{"dns":["8.8.8.8"],"dns_suffix":[".mist.local"],"'
            'gateway":"10.2.1.254","ip":"10.2.1.1","netmask":"255.255.255.0"},"'
            'tunterm_monitoring":[{"host":"10.2.8.15","port":80,"protocol":"pin'
            'g","timeout":300}],"tunterm_other_ip_configs":{"5":{"ip":"10.3.3.1'
            '","netmask":"255.255.255.0"}},"tunterm_port_config":{"downstream_p'
            'orts":["3"],"separate_upstream_downstream":true,"upstream_port_vla'
            'n_id":30,"upstream_ports":["0","1","2"]},"tunterm_registered":true'
            ',"tunterm_switch_config":{"0":{"port_vlan_id":1,"vlan_ids":[1,3055'
            ']},"enabled":true}}')
        received_body = APIHelper.json_deserialize(self.response_catcher.response.text)
        assert ComparisonHelper.match_body(expected_body, received_body)

    # Delete Site Mist Edge
    def test_delete_site_mx_edge(self):
        # Parameters for the API call
        site_id = '000000ab-00ab-00ab-00ab-0000000000ab'
        mxedge_id = '000000ab-00ab-00ab-00ab-0000000000ab'

        # Perform the API call through the SDK function
        result = self.controller.delete_site_mx_edge(site_id, mxedge_id)

        # Test response code
        assert self.response_catcher.response.status_code == 200

        # Test headers
        expected_headers = {}
        expected_headers['content-type'] = 'application/json'

        assert ComparisonHelper.match_headers(expected_headers, self.response_catcher.response.headers)


    # get Site Mist Edge
    def test_get_site_mx_edge(self):
        # Parameters for the API call
        site_id = '000000ab-00ab-00ab-00ab-0000000000ab'
        mxedge_id = '000000ab-00ab-00ab-00ab-0000000000ab'

        # Perform the API call through the SDK function
        self.controller.get_site_mx_edge(site_id, mxedge_id)

        # Test response code
        assert self.response_catcher.response.status_code == 200

    # Update Site Mist Edge settings
    def test_update_site_mx_edge(self):
        # Parameters for the API call
        site_id = '000000ab-00ab-00ab-00ab-0000000000ab'
        mxedge_id = '000000ab-00ab-00ab-00ab-0000000000ab'
        body = None

        # Perform the API call through the SDK function
        result = self.controller.update_site_mx_edge(site_id, mxedge_id, body)

        # Test response code
        assert self.response_catcher.response.status_code == 200

        # Test headers
        expected_headers = {}
        expected_headers['content-type'] = 'application/json'

        assert ComparisonHelper.match_headers(expected_headers, self.response_catcher.response.headers)

        
        # Test whether the captured response is as we expected
        assert result is not None
        expected_body = APIHelper.json_deserialize('{"id":"95ddd29a-6a3c-929e-a431-51a5b09f36a6","magic":"L-NpT5gi-ADR'
            '8WTFd4EiQPY3cP5WdSoD","model":"ME-100","mxagent_registered":true,"'
            'mxcluster_id":"572586b7-f97b-a22b-526c-8b97a3f609c4","mxedge_mgmt"'
            ':{"mist_password":"MIST_PASSWORD","root_password":"ROOT_PASSWORD"}'
            ',"name":"Guest","ntp_servers":[],"oob_ip_config":{"dns":["8.8.8.8"'
            ',"4.4.4.4"],"gateway":"10.2.1.254","ip":"10.2.1.10","netmask":"255'
            '.255.255.0","type":"static"},"tunterm_dhcpd_config":{"2":{"enabled'
            '":true,"servers":["11.2.3.44"]},"enabled":false,"servers":["11.2.3'
            '.4"]},"tunterm_extra_routes":{"11.0.0.0/8":{"via":"10.3.3.1"}},"tu'
            'nterm_ip_config":{"dns":["8.8.8.8"],"dns_suffix":[".mist.local"],"'
            'gateway":"10.2.1.254","ip":"10.2.1.1","netmask":"255.255.255.0"},"'
            'tunterm_monitoring":[{"host":"10.2.8.15","port":80,"protocol":"pin'
            'g","timeout":300}],"tunterm_other_ip_configs":{"5":{"ip":"10.3.3.1'
            '","netmask":"255.255.255.0"}},"tunterm_port_config":{"downstream_p'
            'orts":["3"],"separate_upstream_downstream":true,"upstream_port_vla'
            'n_id":30,"upstream_ports":["0","1","2"]},"tunterm_registered":true'
            ',"tunterm_switch_config":{"0":{"port_vlan_id":1,"vlan_ids":[1,3055'
            ']},"enabled":true}}')
        received_body = APIHelper.json_deserialize(self.response_catcher.response.text)
        assert ComparisonHelper.match_body(expected_body, received_body)

