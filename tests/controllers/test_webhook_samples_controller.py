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
from mistapi.models.webhook_alarms import WebhookAlarms
from mistapi.models.webhook_asset_raw import WebhookAssetRaw
from mistapi.models.webhook_audits import WebhookAudits
from mistapi.models.webhook_client_join import WebhookClientJoin
from mistapi.models.webhook_client_sessions import WebhookClientSessions
from mistapi.models.webhook_device_events import WebhookDeviceEvents
from mistapi.models.webhook_device_updowns import WebhookDeviceUpdowns
from mistapi.models.webhook_discovered_raw_rssi import WebhookDiscoveredRawRssi
from mistapi.models.webhook_location import WebhookLocation
from mistapi.models.webhook_occupancy_alerts import WebhookOccupancyAlerts
from mistapi.models.webhook_ping import WebhookPing
from mistapi.models.webhook_sdkclient_scan_data import WebhookSdkclientScanData
from mistapi.models.webhook_zone import WebhookZone


class WebhookSamplesControllerTests(ControllerTestBase):

    @classmethod
    def setUpClass(cls):
        super(WebhookSamplesControllerTests, cls).setUpClass()
        cls.controller = cls.client.webhook_samples
        cls.response_catcher = cls.controller.http_call_back

    # Webhook sample for `alarm` topic
    #
    #**Note**: The server host will be your own server FQDN where the Mist Cloud is sending the webhook messages
    def test_alarms(self):
        # Parameters for the API call
        body = APIHelper.json_deserialize('{"events":[{"aps":["string"],"bssids":["string"],"count":0,"event_'
            'id":"a7a26ff2-e851-45b6-9634-d595f45458b7","for_site":true,"id":"4'
            '89f6eca-6276-4993-bfeb-c3cbbbba6f08","last_seen":0,"org_id":"a40f5'
            'd1f-d889-42e9-94ea-b9b33585fc6b","site_id":"72771e6a-6f5e-4de4-a5b'
            '9-1266c4197811","ssids":["string"],"timestamp":0,"type":"string","'
            'update":true}],"topic":"alarms"}', WebhookAlarms.from_dictionary)

        # Perform the API call through the SDK function
        result = self.controller.alarms(body)

        # Test response code
        assert self.response_catcher.response.status_code == 200

        # Test headers
        expected_headers = {}
        expected_headers['content-type'] = 'application/json'

        assert ComparisonHelper.match_headers(expected_headers, self.response_catcher.response.headers)


    # Webhook sample for `asset_raw` topic
    #
    #**Note**: The server host will be your own server FQDN where the Mist Cloud is sending the webhook messages
    #
    #**will be deprecated after 03/31/2024**
    def test_asset_raw(self):
        # Parameters for the API call
        body = APIHelper.json_deserialize('{"events":[{"asset_id":"b4695157-0d1d-4da0-8f9e-5c53149389e4","bea'
            'm":0,"device_id":"3bafab7b-4400-4bcf-8e6e-09f954699940","ibeacon_m'
            'ajor":0,"ibeacon_minor":0,"ibeacon_uuid":"1f89bc00-d0af-481b-82fe-'
            'a6629259a39f","mac":"string","map_id":"09d2b626-2e4e-45ef-a3c4-e6a'
            'eb6c83db1","mfg_company_id":0,"mfg_data":"string","rssi":0,"site_i'
            'd":"72771e6a-6f5e-4de4-a5b9-1266c4197811","timestamp":0}],"topic":'
            '"asset-raw"}', WebhookAssetRaw.from_dictionary)

        # Perform the API call through the SDK function
        result = self.controller.asset_raw(body)

        # Test response code
        assert self.response_catcher.response.status_code == 200

        # Test headers
        expected_headers = {}
        expected_headers['content-type'] = 'application/json'

        assert ComparisonHelper.match_headers(expected_headers, self.response_catcher.response.headers)


    # Webhook sample for `audit` topic
    #
    #**Note**: The server host will be your own server FQDN where the Mist Cloud is sending the webhook messages
    #
    def test_audits(self):
        # Parameters for the API call
        body = APIHelper.json_deserialize('{"events":[{"admin_name":"string","device_id":"3bafab7b-4400-4bcf-'
            '8e6e-09f954699940","id":"488f6eca-6276-4993-bfeb-d3cbbbba6f08","me'
            'ssage":"string","org_id":"a40f5d1f-d889-42e9-94ea-b9b33585fc6b","s'
            'ite_id":"72771e6a-6f5e-4de4-a5b9-1266c4197811","src_ip":"string","'
            'timestamp":0}],"topic":"audits"}', WebhookAudits.from_dictionary)

        # Perform the API call through the SDK function
        result = self.controller.audits(body)

        # Test response code
        assert self.response_catcher.response.status_code == 200

        # Test headers
        expected_headers = {}
        expected_headers['content-type'] = 'application/json'

        assert ComparisonHelper.match_headers(expected_headers, self.response_catcher.response.headers)


    # Webhook sample for `client_join` topic
    #
    #**Note**: The server host will be your own server FQDN where the Mist Cloud is sending the webhook messages
    #
    def test_client_join(self):
        # Parameters for the API call
        body = APIHelper.json_deserialize('{"events":[{"ap":"string","ap_name":"string","band":"string","bssi'
            'd":"string","connect":0,"connect_float":0,"mac":"string","org_id":'
            '"a40f5d1f-d889-42e9-94ea-b9b33585fc6b","rssi":0,"site_id":"72771e6'
            'a-6f5e-4de4-a5b9-1266c4197811","site_name":"string","ssid":"string'
            '","timestamp":0,"version":0,"wlan_id":"5028e92b-fc59-4056-91d1-ea4'
            'b4ca1617a"}],"topic":"client-join"}', WebhookClientJoin.from_dictionary)

        # Perform the API call through the SDK function
        result = self.controller.client_join(body)

        # Test response code
        assert self.response_catcher.response.status_code == 200

        # Test headers
        expected_headers = {}
        expected_headers['content-type'] = 'application/json'

        assert ComparisonHelper.match_headers(expected_headers, self.response_catcher.response.headers)


    # Webhook sample for `client_sessions` topic
    #
    #**Note**: The server host will be your own server FQDN where the Mist Cloud is sending the webhook messages
    #
    def test_client_sessions(self):
        # Parameters for the API call
        body = APIHelper.json_deserialize('{"events":[{"ap":"string","ap_name":"string","band":"string","bssi'
            'd":"string","client_family":"string","client_manufacture":"string"'
            ',"client_model":"string","client_os":"string","connect":0,"connect'
            '_float":0,"disconnect":0,"disconnect_float":0,"duration":0,"mac":"'
            'string","next_ap":"string","org_id":"a40f5d1f-d889-42e9-94ea-b9b33'
            '585fc6b","rssi":0,"site_id":"72771e6a-6f5e-4de4-a5b9-1266c4197811"'
            ',"site_name":"string","ssid":"string","termination_reason":0,"time'
            'stamp":0,"version":0,"wlan_id":"5028e92b-fc59-4056-91d1-ea4b4ca161'
            '7a"}],"topic":"client-sessions"}', WebhookClientSessions.from_dictionary)

        # Perform the API call through the SDK function
        result = self.controller.client_sessions(body)

        # Test response code
        assert self.response_catcher.response.status_code == 200

        # Test headers
        expected_headers = {}
        expected_headers['content-type'] = 'application/json'

        assert ComparisonHelper.match_headers(expected_headers, self.response_catcher.response.headers)


    # Webhook sample for `device_events` topic
    #
    #**Note**: The server host will be your own server FQDN where the Mist Cloud is sending the webhook messages
    #
    def test_device_events(self):
        # Parameters for the API call
        body = APIHelper.json_deserialize('{"events":[{"ap":"string","ap_name":"string","audit_id":"78c04fa6-'
            'cfb4-46a0-9aa5-3681ba4f3897","device_name":"string","device_type":'
            '"ap","ev_type":"notice","mac":"string","org_id":"a40f5d1f-d889-42e'
            '9-94ea-b9b33585fc6b","reason":"string","site_id":"72771e6a-6f5e-4d'
            'e4-a5b9-1266c4197811","site_name":"string","text":"string","timest'
            'amp":0,"type":"string"}],"topic":"device-events"}', WebhookDeviceEvents.from_dictionary)

        # Perform the API call through the SDK function
        result = self.controller.device_events(body)

        # Test response code
        assert self.response_catcher.response.status_code == 200

        # Test headers
        expected_headers = {}
        expected_headers['content-type'] = 'application/json'

        assert ComparisonHelper.match_headers(expected_headers, self.response_catcher.response.headers)


    # Webhook sample for `device_updowns` topic
    #
    #**Note**: The server host will be your own server FQDN where the Mist Cloud is sending the webhook messages
    #
    def test_device_up_down(self):
        # Parameters for the API call
        body = APIHelper.json_deserialize('{"events":[{"ap":"string","ap_name":"string","for_site":true,"org_'
            'id":"a40f5d1f-d889-42e9-94ea-b9b33585fc6b","site_id":"72771e6a-6f5'
            'e-4de4-a5b9-1266c4197811","site_name":"string","timestamp":0,"type'
            '":"string"}],"topic":"device-updowns"}', WebhookDeviceUpdowns.from_dictionary)

        # Perform the API call through the SDK function
        result = self.controller.device_up_down(body)

        # Test response code
        assert self.response_catcher.response.status_code == 200

        # Test headers
        expected_headers = {}
        expected_headers['content-type'] = 'application/json'

        assert ComparisonHelper.match_headers(expected_headers, self.response_catcher.response.headers)


    # Webhook sample for `discovered-raw-rssi` topic
    #
    #**Note**: The server host will be your own server FQDN where the Mist Cloud is sending the webhook messages
    #
    def test_discovered_raw_rssi(self):
        # Parameters for the API call
        body = APIHelper.json_deserialize('{"events":[{"ap_loc":[0],"beam":0,"device_id":"3bafab7b-4400-4bcf-'
            '8e6e-09f954699940","ibeacon_major":0,"ibeacon_minor":0,"ibeacon_uu'
            'id":"1f89bc00-d0af-481b-82fe-a6629259a39f","is_asset":true,"mac":"'
            'string","map_id":"09d2b626-2e4e-45ef-a3c4-e6aeb6c83db1","mfg_compa'
            'ny_id":"string","mfg_data":"string","org_id":"a40f5d1f-d889-42e9-9'
            '4ea-b9b33585fc6b","rssi":0,"service_packets":[{"service_data":"str'
            'ing","service_uuid":"7138cc00-c611-4dec-a05e-5c4b1cae13c0"}],"site'
            '_id":"72771e6a-6f5e-4de4-a5b9-1266c4197811","timestamp":0}],"topic'
            '":"string"}', WebhookDiscoveredRawRssi.from_dictionary)

        # Perform the API call through the SDK function
        result = self.controller.discovered_raw_rssi(body)

        # Test response code
        assert self.response_catcher.response.status_code == 200

        # Test headers
        expected_headers = {}
        expected_headers['content-type'] = 'application/json'

        assert ComparisonHelper.match_headers(expected_headers, self.response_catcher.response.headers)


    # Webhook sample for `location` topic
    #
    #**Note**: The server host will be your own server FQDN where the Mist Cloud is sending the webhook messages
    #
    def test_location(self):
        # Parameters for the API call
        body = APIHelper.json_deserialize('{"events":[{"battery_voltage":0,"eddystone_uid_instance":"string",'
            '"eddystone_uid_namespace":"string","eddystone_url_url":"string","i'
            'beacon_major":0,"ibeacon_minor":0,"ibeacon_uuid":"1f89bc00-d0af-48'
            '1b-82fe-a6629259a39f","id":"487f6eca-6276-4993-bfeb-e3cbbbba6f08",'
            '"mac":"string","map_id":"09d2b626-2e4e-45ef-a3c4-e6aeb6c83db1","mf'
            'g_company_id":0,"mfg_data":"string","name":"string","site_id":"727'
            '71e6a-6f5e-4de4-a5b9-1266c4197811","timestamp":0,"type":"string","'
            'x":0,"y":0}],"topic":"location"}', WebhookLocation.from_dictionary)

        # Perform the API call through the SDK function
        result = self.controller.location(body)

        # Test response code
        assert self.response_catcher.response.status_code == 200

        # Test headers
        expected_headers = {}
        expected_headers['content-type'] = 'application/json'

        assert ComparisonHelper.match_headers(expected_headers, self.response_catcher.response.headers)


    # Webhook sample for `occupancy_alerts` topic
    #
    #**Note**: The server host will be your own server FQDN where the Mist Cloud is sending the webhook messages
    #
    def test_occupancy_alerts(self):
        # Parameters for the API call
        body = APIHelper.json_deserialize('{"events":[{"alert_events":[{"current_occupancy":0,"map_id":"09d2b'
            '626-2e4e-45ef-a3c4-e6aeb6c83db1","occupancy_limit":0,"org_id":"a40'
            'f5d1f-d889-42e9-94ea-b9b33585fc6b","timestamp":0,"type":"COMPLIANC'
            'E-VIOLATION","zone_id":"4495020a-236f-46e0-9453-e3f9cc6476f4","zon'
            'e_name":"string"}],"for_site":true,"site_id":"72771e6a-6f5e-4de4-a'
            '5b9-1266c4197811","site_name":"string"}],"topic":"occupancy-alerts'
            '"}', WebhookOccupancyAlerts.from_dictionary)

        # Perform the API call through the SDK function
        result = self.controller.occupancy_alerts(body)

        # Test response code
        assert self.response_catcher.response.status_code == 200

        # Test headers
        expected_headers = {}
        expected_headers['content-type'] = 'application/json'

        assert ComparisonHelper.match_headers(expected_headers, self.response_catcher.response.headers)


    # Webhook sample for `ping` topic
    #
    #**Note**: The server host will be your own server FQDN where the Mist Cloud is sending the webhook messages
    #
    def test_ping(self):
        # Parameters for the API call
        body = APIHelper.json_deserialize('{"events":[{"id":"487f6eca-6276-4993-bfeb-f3cbbbba6f08","name":"st'
            'ring","site_id":"72771e6a-6f5e-4de4-a5b9-1266c4197811","timestamp"'
            ':0}],"topic":"ping"}', WebhookPing.from_dictionary)

        # Perform the API call through the SDK function
        result = self.controller.ping(body)

        # Test response code
        assert self.response_catcher.response.status_code == 200

        # Test headers
        expected_headers = {}
        expected_headers['content-type'] = 'application/json'

        assert ComparisonHelper.match_headers(expected_headers, self.response_catcher.response.headers)


    # Webhook sample for `sdkclient_scan_data` topic
    #
    #**Note**: The server host will be your own server FQDN where the Mist Cloud is sending the webhook messages
    #
    def test_sdkclient_scan_data(self):
        # Parameters for the API call
        body = APIHelper.json_deserialize('{"events":[{"connection_ap":"5c5b352f587e","connection_band":"2.4"'
            ',"connection_bssid":"5c5b352b51b4","connection_channel":11,"connec'
            'tion_rssi":-87,"last_seen":1592333828,"mac":"70ef0071535f","scan_d'
            'ata":[{"ap":"5c5b352f587e","band":"2.4","bssid":"5c5b352b51b4","ch'
            'annel":11,"rssi":-87,"ssid":"mist-wifi","timestamp":1592333828},{"'
            'ap":"5c5b352f587e","band":"5","bssid":"5c5b352b51b8","channel":36,'
            '"rssi":-75,"ssid":"mist-wifi","timestamp":1592333828}],"site_id":"'
            'd761985e-49b1-4506-88e9-e0368a05c301"}],"topic":"sdkclient-scan-da'
            'ta"}', WebhookSdkclientScanData.from_dictionary)

        # Perform the API call through the SDK function
        result = self.controller.sdkclient_scan_data(body)

        # Test response code
        assert self.response_catcher.response.status_code == 200

        # Test headers
        expected_headers = {}
        expected_headers['content-type'] = 'application/json'

        assert ComparisonHelper.match_headers(expected_headers, self.response_catcher.response.headers)


    # Webhook sample for `zone` topic
    #
    #**Note**: The server host will be your own server FQDN where the Mist Cloud is sending the webhook messages
    #
    def test_zone(self):
        # Parameters for the API call
        body = APIHelper.json_deserialize('{"events":[{"asset_id":"b4695157-0d1d-4da0-8f9e-5c53149389e4","id"'
            ':"485f6eca-6276-4993-bfeb-54cbbbba6f08","mac":"string","map_id":"0'
            '9d2b626-2e4e-45ef-a3c4-e6aeb6c83db1","name":"string","site_id":"72'
            '771e6a-6f5e-4de4-a5b9-1266c4197811","timestamp":0,"trigger":"enter'
            '","type":"string","zone_id":"4495020a-236f-46e0-9453-e3f9cc6476f4"'
            '}],"topic":"zone"}', WebhookZone.from_dictionary)

        # Perform the API call through the SDK function
        result = self.controller.zone(body)

        # Test response code
        assert self.response_catcher.response.status_code == 200

        # Test headers
        expected_headers = {}
        expected_headers['content-type'] = 'application/json'

        assert ComparisonHelper.match_headers(expected_headers, self.response_catcher.response.headers)

