# Constants

```python
constants_controller = client.constants
```

## Class Name

`ConstantsController`

## Methods

* [List Alarm Definitions](../../doc/controllers/constants.md#list-alarm-definitions)
* [List Ap Channels](../../doc/controllers/constants.md#list-ap-channels)
* [List Ap Led Definition](../../doc/controllers/constants.md#list-ap-led-definition)
* [List Applications](../../doc/controllers/constants.md#list-applications)
* [List Call Events Definitions](../../doc/controllers/constants.md#list-call-events-definitions)
* [List Client Events Definitions](../../doc/controllers/constants.md#list-client-events-definitions)
* [List Country Codes](../../doc/controllers/constants.md#list-country-codes)
* [Get Gataway Default Config](../../doc/controllers/constants.md#get-gataway-default-config)
* [List Device Events Definitions](../../doc/controllers/constants.md#list-device-events-definitions)
* [List Device Models](../../doc/controllers/constants.md#list-device-models)
* [List Insight Metrics](../../doc/controllers/constants.md#list-insight-metrics)
* [List Site Languages](../../doc/controllers/constants.md#list-site-languages)
* [Get License Types](../../doc/controllers/constants.md#get-license-types)
* [List Mx Edge Events Definitions](../../doc/controllers/constants.md#list-mx-edge-events-definitions)
* [List Mx Edge Models](../../doc/controllers/constants.md#list-mx-edge-models)
* [List Other Device Events Definitions](../../doc/controllers/constants.md#list-other-device-events-definitions)
* [List Traffic Types](../../doc/controllers/constants.md#list-traffic-types)


# List Alarm Definitions

Get List of brief definitions of all the supported alarm types.  The example field contains an example payload as you would recieve in the alarm webhook output.

```python
def list_alarm_definitions(self)
```

## Response Type

[`List of ApiV1ConstAlarmDefsResponse`](../../doc/models/api-v1-const-alarm-defs-response.md)

## Example Usage

```python
result = constants_controller.list_alarm_definitions()
print(result)
```

## Example Response *(as JSON)*

```json
[
  {
    "display": "Device offline",
    "example": {
      "aps": [
        "d420b02000fa"
      ],
      "count": 1,
      "group": "infrastructure",
      "hostnames": [
        "Vendor_AP2"
      ],
      "id": "f70c308f-7007-4866-9ecd-0d01842979ea",
      "last_seen": 1629753888,
      "org_id": "09dac91f-6e73-4100-89f7-698e0fafbb1b",
      "severity": "warn",
      "site_id": "dcfb31a1-d615-4361-8c95-b9dde05aa704",
      "timestamp": 1629753888,
      "type": "device_down"
    },
    "fields": [
      "aps",
      "hostnames"
    ],
    "group": "infrastructure",
    "key": "device_down",
    "severity": "warn"
  }
]
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1ConstAlarmDefs401ErrorException`](../../doc/models/api-v1-const-alarm-defs-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1ConstAlarmDefs403ErrorException`](../../doc/models/api-v1-const-alarm-defs-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1ConstAlarmDefs404ErrorException`](../../doc/models/api-v1-const-alarm-defs-404-error-exception.md) |


# List Ap Channels

Get List of List of Available channels per country code

```python
def list_ap_channels(self,
                    country_code=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `country_code` | `string` | Query, Optional | country code, in two-character<br>**Constraints**: *Pattern*: `^[a-zA-Z]{2}$` |

## Response Type

[`ApiV1ConstApChannelsResponse`](../../doc/models/api-v1-const-ap-channels-response.md)

## Example Usage

```python
country_code = 'US'

result = constants_controller.list_ap_channels(
    country_code
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "band24_channels": {
    "20": [
      1,
      2,
      3,
      4,
      5,
      6,
      7,
      8,
      9,
      10,
      11
    ],
    "40": [
      1,
      2,
      3,
      4,
      5,
      6,
      7,
      8,
      9,
      10,
      11
    ]
  },
  "band24_enabled": true,
  "band5_channels": {
    "20": [
      36,
      40,
      44,
      48,
      52,
      56,
      60,
      64,
      100,
      104,
      108,
      112,
      116,
      132,
      136,
      140,
      149,
      153,
      157,
      161,
      165
    ],
    "40": [
      36,
      40,
      44,
      48,
      52,
      56,
      60,
      64,
      100,
      104,
      108,
      112,
      132,
      136,
      149,
      153,
      157,
      161
    ],
    "80": [
      36,
      40,
      44,
      48,
      52,
      56,
      60,
      64,
      100,
      104,
      108,
      112,
      132,
      136,
      149,
      153,
      157,
      161
    ],
    "dfs": [
      52,
      56,
      60,
      64,
      100,
      104,
      108,
      112,
      116,
      132,
      136,
      140
    ]
  },
  "band5_enabled": true,
  "code": 840,
  "dfs_ok": true,
  "key": "US",
  "name": "United States"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1ConstApChannels401ErrorException`](../../doc/models/api-v1-const-ap-channels-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1ConstApChannels403ErrorException`](../../doc/models/api-v1-const-ap-channels-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1ConstApChannels404ErrorException`](../../doc/models/api-v1-const-ap-channels-404-error-exception.md) |


# List Ap Led Definition

Get List of AP LED definition

```python
def list_ap_led_definition(self)
```

## Response Type

[`List of ApiV1ConstApLedStatusResponse`](../../doc/models/api-v1-const-ap-led-status-response.md)

## Example Usage

```python
result = constants_controller.list_ap_led_definition()
print(result)
```

## Example Response *(as JSON)*

```json
[
  {
    "code": "02",
    "description": "Has no link (Seen using power injectors, but not connected to a switch)",
    "key": "NO_ETHERNET_LINK",
    "name": "No ethernet link"
  }
]
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1ConstApLedStatus401ErrorException`](../../doc/models/api-v1-const-ap-led-status-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1ConstApLedStatus403ErrorException`](../../doc/models/api-v1-const-ap-led-status-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1ConstApLedStatus404ErrorException`](../../doc/models/api-v1-const-ap-led-status-404-error-exception.md) |


# List Applications

Get List of a list of applications that Juniper-Mist APs recognize

```python
def list_applications(self)
```

## Response Type

[`List of ConstApplication`](../../doc/models/const-application.md)

## Example Usage

```python
result = constants_controller.list_applications()
print(result)
```

## Example Response *(as JSON)*

```json
[
  {
    "app_id": true,
    "group": "Emails",
    "key": "all-email",
    "name": "All Emails"
  },
  {
    "app_id": true,
    "category": "Collaboration",
    "group": "Emails",
    "key": "gmail",
    "name": "Gmail",
    "ssr_app_id": true
  },
  {
    "app_id": true,
    "category": "Collaboration",
    "group": "Emails",
    "key": "yahoo-mail",
    "name": "Yahoo Mail",
    "ssr_app_id": true
  },
  {
    "app_id": true,
    "app_image_url": "",
    "app_probe": true,
    "category": "FileSharing",
    "group": "File Sharing",
    "key": "dropbox",
    "name": "Dropbox",
    "ssr_app_id": true
  },
  {
    "app_id": true,
    "group": "Online Backup",
    "key": "icloud-backup",
    "name": "iCloud backup"
  },
  {
    "app_id": true,
    "category": "FileSharing",
    "group": "Peer 2 Peer",
    "key": "bit-torrent",
    "name": "BitTorrent",
    "ssr_app_id": true
  },
  {
    "app_id": true,
    "group": "Social",
    "key": "all-social",
    "name": "All Socials"
  },
  {
    "app_id": true,
    "app_image_url": "",
    "app_probe": true,
    "category": "SocialMedia",
    "group": "Social",
    "key": "facebook",
    "name": "Facebook",
    "ssr_app_id": true
  }
]
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1ConstApplications401ErrorException`](../../doc/models/api-v1-const-applications-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1ConstApplications403ErrorException`](../../doc/models/api-v1-const-applications-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1ConstApplications404ErrorException`](../../doc/models/api-v1-const-applications-404-error-exception.md) |


# List Call Events Definitions

Get List of Call Event Definitions

```python
def list_call_events_definitions(self)
```

## Response Type

[`List of ApiV1ConstCallEventsResponse`](../../doc/models/api-v1-const-call-events-response.md)

## Example Usage

```python
result = constants_controller.list_call_events_definitions()
print(result)
```

## Example Response *(as JSON)*

```json
[
  {
    "description": "Client joined the call",
    "display": "Client joined the call",
    "example": {
      "app": "zoom",
      "meeting_id": "87609329850",
      "org_id": "2818e386-8dec-2562-9ede-5b8a0fbbdc71",
      "site_id": "1916d52a-4a90-11e5-8b45-1258369c38a9",
      "timestamp": 1674777600,
      "type": "CLIENTS_JOINED_CALL",
      "wcid": "82c70a73-e2e1-42f9-6da0-97db44b7b9ad"
    },
    "key": "CLIENT_JOINED_CALL"
  },
  {
    "description": "Client got abruptly disconnected from the call",
    "display": "Client disconnected abruptly from the call",
    "example": {
      "app": "zoom",
      "meeting_id": "87609329850",
      "org_id": "2818e386-8dec-2562-9ede-5b8a0fbbdc71",
      "reason": "Network connection error.",
      "site_id": "1916d52a-4a90-11e5-8b45-1258369c38a9",
      "timestamp": 1674777600,
      "type": "CLIENT_DISCONNECTED_FROM_CALL",
      "wcid": "82c70a73-e2e1-42f9-6da0-97db44b7b9ad"
    },
    "key": "CLIENT_DISCONNECTED_FROM_CALL"
  },
  {
    "description": "Client left the call",
    "display": "Client left the call",
    "example": {
      "app": "zoom",
      "meeting_id": "87609329850",
      "org_id": "2818e386-8dec-2562-9ede-5b8a0fbbdc71",
      "site_id": "1916d52a-4a90-11e5-8b45-1258369c38a9",
      "timestamp": 1674777600,
      "type": "CLIENT_LEFT_CALL",
      "wcid": "82c70a73-e2e1-42f9-6da0-97db44b7b9ad"
    },
    "key": "CLIENT_LEFT_CALL"
  },
  {
    "description": "Zoom/Teams CPU usage is high",
    "display": "High CPU Observed",
    "example": {
      "app": "zoom",
      "org_id": "2818e386-8dec-2562-9ede-5b8a0fbbdc71",
      "timestamp": 1674777600,
      "type": "HIGH_CPU_OBSERVED"
    },
    "key": "HIGH_CPU_OBSERVED"
  }
]
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1ConstCallEvents401ErrorException`](../../doc/models/api-v1-const-call-events-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1ConstCallEvents403ErrorException`](../../doc/models/api-v1-const-call-events-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1ConstCallEvents404ErrorException`](../../doc/models/api-v1-const-call-events-404-error-exception.md) |


# List Client Events Definitions

Get List of List of available Client Events

```python
def list_client_events_definitions(self)
```

## Response Type

[`List of ApiV1ConstClientEventsResponse`](../../doc/models/api-v1-const-client-events-response.md)

## Example Usage

```python
result = constants_controller.list_client_events_definitions()
print(result)
```

## Example Response *(as JSON)*

```json
[
  {
    "display": "DHCP Success",
    "key": "CLIENT_IP_ASSIGNED"
  }
]
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1ConstClientEvents401ErrorException`](../../doc/models/api-v1-const-client-events-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1ConstClientEvents403ErrorException`](../../doc/models/api-v1-const-client-events-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1ConstClientEvents404ErrorException`](../../doc/models/api-v1-const-client-events-404-error-exception.md) |


# List Country Codes

Get List of List of available Country Codes

```python
def list_country_codes(self)
```

## Response Type

[`List of ApiV1ConstCountriesResponse`](../../doc/models/api-v1-const-countries-response.md)

## Example Usage

```python
result = constants_controller.list_country_codes()
print(result)
```

## Example Response *(as JSON)*

```json
[
  {
    "alpha2": "US",
    "certified": true,
    "name": "United States",
    "numeric": 840
  },
  {
    "alpha2": "JP",
    "certified": true,
    "name": "Japan",
    "numeric": 392
  }
]
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1ConstCountries401ErrorException`](../../doc/models/api-v1-const-countries-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1ConstCountries403ErrorException`](../../doc/models/api-v1-const-countries-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1ConstCountries404ErrorException`](../../doc/models/api-v1-const-countries-404-error-exception.md) |


# Get Gataway Default Config

Generate Default Gateway Config

```python
def get_gataway_default_config(self,
                              model=None,
                              ha=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `model` | `string` | Query, Optional | model the default gateway config is intended (as the default LAN/WAN port can differ) |
| `ha` | `string` | Query, Optional | whether the config is intended for HA |

## Response Type

`object`

## Example Usage

```python
result = constants_controller.get_gataway_default_config()
print(result)
```

## Example Response

```
{
  "dhcpd_config": {
    "lan": {
      "ip_end": "192.168.1.254",
      "ip_start": "192.168.1.2"
    }
  },
  "ip_configs": {
    "lan": {
      "ip": "192.168.1.1",
      "type": "static"
    }
  },
  "networks": {
    "lan": {
      "name": "lan",
      "subnet": "192.168.1.0/24",
      "vlan_id": 1
    }
  },
  "path_preferences": {
    "wan": {
      "paths": [
        {
          "name": "wan",
          "type": "wan"
        }
      ]
    }
  },
  "port_config": {
    "cl-1/0/0": {
      "ip_config": {
        "type": "dhcp"
      },
      "name": "lte",
      "usage": "wan",
      "wan_type": "lte"
    },
    "ge-0/0/0,ge-0/0/7": {
      "ip_config": {
        "type": "dhcp"
      },
      "name": "wan",
      "usage": "wan"
    },
    "ge-0/0/1-6": {
      "port_network": "lan",
      "usage": "lan"
    }
  },
  "service_policies": [
    {
      "action": "allow",
      "name": "Internet",
      "path_preference": "wan",
      "services": [
        "any"
      ],
      "tenants": [
        "lan"
      ]
    }
  ]
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1ConstDefaultGatewayConfig401ErrorException`](../../doc/models/api-v1-const-default-gateway-config-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1ConstDefaultGatewayConfig403ErrorException`](../../doc/models/api-v1-const-default-gateway-config-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1ConstDefaultGatewayConfig404ErrorException`](../../doc/models/api-v1-const-default-gateway-config-404-error-exception.md) |


# List Device Events Definitions

Get list of available Device Events

```python
def list_device_events_definitions(self)
```

## Response Type

[`List of ApiV1ConstDeviceEventsResponse`](../../doc/models/api-v1-const-device-events-response.md)

## Example Usage

```python
result = constants_controller.list_device_events_definitions()
print(result)
```

## Example Response *(as JSON)*

```json
[
  {
    "description": "AP was assigned to a site",
    "display": "AP Assigned",
    "example": {
      "ap": "5c5b35000001",
      "audit_id": "e9a88814-fa81-5bdc-34b0-84e8735420e5",
      "org_id": "2818e386-8dec-2562-9ede-5b8a0fbbdc71",
      "site_id": "4ac1dcf4-9d8b-7211-65c4-057819f0862b",
      "timestamp": 1552408871,
      "type": "AP_ASSIGNED"
    },
    "key": "AP_ASSIGNED"
  }
]
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1ConstDeviceEvents401ErrorException`](../../doc/models/api-v1-const-device-events-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1ConstDeviceEvents403ErrorException`](../../doc/models/api-v1-const-device-events-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1ConstDeviceEvents404ErrorException`](../../doc/models/api-v1-const-device-events-404-error-exception.md) |


# List Device Models

Get list of AP device models for the Mist Site

```python
def list_device_models(self)
```

## Response Type

[`List of ConstDeviceModel`](../../doc/models/const-device-model.md)

## Example Usage

```python
result = constants_controller.list_device_models()
print(result)
```

## Example Response *(as JSON)*

```json
[
  {
    "alias": "string",
    "ap_type": "string",
    "band24": {
      "max_clients": 0,
      "max_power": 0,
      "min_power": 0
    },
    "band5": {
      "max_clients": 0,
      "max_power": 0,
      "min_power": 0
    },
    "band6": {
      "max_clients": 0,
      "max_power": 0,
      "min_power": 0
    },
    "ce_dfs_ok": true,
    "cisco_pace": true,
    "defaults": {
      "_ports": "string",
      "property1": "string",
      "property2": "string"
    },
    "description": "string",
    "disallowed_channels": {
      "property1": {
        "property1": [
          0
        ],
        "property2": [
          0
        ]
      },
      "property2": {
        "property1": [
          0
        ],
        "property2": [
          0
        ]
      }
    },
    "display": "string",
    "evolved_os": false,
    "evpn_ri_type": "string",
    "experimental": false,
    "extio": {
      "property1": {
        "default_dir": "IN",
        "input": true,
        "output": true
      },
      "property2": {
        "default_dir": "IN",
        "input": true,
        "output": true
      }
    },
    "fans_pluggable": true,
    "fcc_dfs_ok": true,
    "ha_node0_fpc": 0,
    "ha_node1_fpc": 0,
    "has_11ax": true,
    "has_bgp": false,
    "has_compass": true,
    "has_ets": false,
    "has_evpn": false,
    "has_ext_ant": true,
    "has_extio": true,
    "has_fxp0": true,
    "has_ha_control": false,
    "has_ha_data": false,
    "has_height": true,
    "has_irb": false,
    "has_module_port": true,
    "has_poe_out": true,
    "has_scanning_radio": true,
    "has_selectable_radio": true,
    "has_snapshot": true,
    "has_usb": true,
    "has_vble": true,
    "has_vc": true,
    "has_wifi_band24": true,
    "has_wifi_band5": true,
    "has_wifi_band6": true,
    "irb_disabled_by_default": false,
    "max_poe_out": 0,
    "max_wlans": 0,
    "model": "string",
    "modular": false,
    "no_shaping_rate": false,
    "number_fans": 0,
    "oc_device": false,
    "oob_interface": "string",
    "other_dfs_ok": true,
    "outdoor": true,
    "packet_action_drop_only": false,
    "pic": {
      "property1": "string",
      "property2": "string"
    },
    "ports": {
      "display": "string",
      "pci_address": "string",
      "speed": 0
    },
    "radios": {
      "property1": "string",
      "property2": "string"
    },
    "shared_scanning_radio": true,
    "sub_required": "string",
    "t128_device": false,
    "type": "gateway",
    "unmanaged": true,
    "vble": {
      "beacon_rate": 0,
      "beams": 0,
      "power": 0
    }
  }
]
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1ConstDeviceModels401ErrorException`](../../doc/models/api-v1-const-device-models-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1ConstDeviceModels403ErrorException`](../../doc/models/api-v1-const-device-models-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1ConstDeviceModels404ErrorException`](../../doc/models/api-v1-const-device-models-404-error-exception.md) |


# List Insight Metrics

List Insight Metrics

```python
def list_insight_metrics(self)
```

## Response Type

[`dict`](../../doc/models/api-v1-const-insight-metrics-response.md)

## Example Usage

```python
result = constants_controller.list_insight_metrics()
print(result)
```

## Example Response *(as JSON)*

```json
{
  "bytes": {
    "description": "aggregated bytes over time",
    "example": [
      185,
      197,
      250
    ],
    "intervals": {
      "10m": {
        "interval": 600,
        "max_age": 86400
      },
      "1h": {
        "interval": 3600,
        "max_age": 1209600
      }
    },
    "report_durations": {
      "1d": {
        "duration": 86400,
        "interval": 3600
      },
      "1w": {
        "duration": 604800,
        "interval": 3600
      }
    },
    "report_scopes": [
      "site",
      "org"
    ],
    "scopes": [
      "site",
      "ap",
      "client"
    ],
    "type": "timeseries",
    "unit": "byte"
  },
  "num_clients": {
    "description": "number of client over time",
    "example": [
      18,
      null,
      15
    ],
    "intervals": {
      "10m": {
        "interval": 600,
        "max_age": 86400
      },
      "1h": {
        "interval": 3600,
        "max_age": 1209600
      }
    },
    "report_durations": {
      "1d": {
        "duration": 86400,
        "interval": 3600
      },
      "1w": {
        "duration": 604800,
        "interval": 3600
      }
    },
    "report_scopes": [
      "site",
      "org"
    ],
    "scopes": [
      "site",
      "ap",
      "device"
    ],
    "type": "timeseries",
    "unit": ""
  }
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1ConstInsightMetrics401ErrorException`](../../doc/models/api-v1-const-insight-metrics-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1ConstInsightMetrics403ErrorException`](../../doc/models/api-v1-const-insight-metrics-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1ConstInsightMetrics404ErrorException`](../../doc/models/api-v1-const-insight-metrics-404-error-exception.md) |


# List Site Languages

Get List of Languages

```python
def list_site_languages(self)
```

## Response Type

[`List of ApiV1ConstLanguagesResponse`](../../doc/models/api-v1-const-languages-response.md)

## Example Usage

```python
result = constants_controller.list_site_languages()
print(result)
```

## Example Response *(as JSON)*

```json
[
  {
    "display": "English (US)",
    "display_native": "English (US)",
    "key": "en-US"
  },
  {
    "display": "Chinese Traditional (Taiwan)",
    "display_native": "中文（台灣）",
    "key": "zh-TW"
  }
]
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1ConstLanguages401ErrorException`](../../doc/models/api-v1-const-languages-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1ConstLanguages403ErrorException`](../../doc/models/api-v1-const-languages-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1ConstLanguages404ErrorException`](../../doc/models/api-v1-const-languages-404-error-exception.md) |


# Get License Types

Get License Types

```python
def get_license_types(self)
```

## Response Type

[`List of ApiV1ConstLicenseTypesResponse`](../../doc/models/api-v1-const-license-types-response.md)

## Example Usage

```python
result = constants_controller.get_license_types()
print(result)
```

## Example Response *(as JSON)*

```json
[
  {
    "description": "Asset Visibility",
    "key": "sub_ast",
    "name": "SUB-AST"
  },
  {
    "description": "IoT Assurance",
    "key": "sub_clnt",
    "name": "SUB-CLNT"
  },
  {
    "description": "vBLE Engagement",
    "key": "sub_eng",
    "name": "SUB-ENG"
  },
  {
    "description": "Wired Assurance 12",
    "includes": [
      "sub_ex12a",
      "sub_ex12p"
    ],
    "key": "sub_ex12",
    "name": "SUB-EX12"
  },
  {
    "description": "Wired Assurance 12 Advanced",
    "key": "sub_ex12a",
    "name": "SUB-EX12A"
  },
  {
    "description": "Wired Assurance 12 Premium",
    "key": "sub_ex12p",
    "name": "SUB-EX12P"
  },
  {
    "description": "Wired Assurance 24",
    "includes": [
      "sub_ex24a",
      "sub_ex24p"
    ],
    "key": "sub_ex24",
    "name": "SUB-EX24"
  },
  {
    "description": "Wired Assurance 24 Advanced",
    "key": "sub_ex24a",
    "name": "SUB-EX24A"
  },
  {
    "description": "Wired Assurance 24 Premium",
    "key": "sub_ex24p",
    "name": "SUB-EX24P"
  },
  {
    "description": "Wired Assurance 48",
    "includes": [
      "sub_ex48a",
      "sub_ex48p"
    ],
    "key": "sub_ex48",
    "name": "SUB-EX48"
  },
  {
    "description": "Wired Assurance 48 Advanced",
    "key": "sub_ex48a",
    "name": "SUB-EX48A"
  },
  {
    "description": "Wired Assurance 48 Premium",
    "key": "sub_ex48p",
    "name": "SUB-EX48P"
  },
  {
    "description": "WiFi Management and Assurance",
    "key": "sub_man",
    "name": "SUB-MAN"
  },
  {
    "description": "Mist Edge",
    "key": "sub_me",
    "name": "SUB-ME"
  },
  {
    "description": "Premium Analytics",
    "key": "sub_pma",
    "name": "SUB-PMA"
  },
  {
    "description": "Marvis for Wired Network",
    "includes": [
      "sub_svna4"
    ],
    "key": "sub_svna",
    "name": "SUB-SVNA"
  },
  {
    "description": "Marvis for Wired/EX and QFX Class 4 devices",
    "key": "sub_svna4",
    "name": "SUB-SVNA4"
  },
  {
    "description": "Wired Assurance for Class 4",
    "includes": [
      "sub_sw4a",
      "sub_sw4p"
    ],
    "key": "sub_sw4",
    "name": "SUB-SW4"
  },
  {
    "description": "Wired Assurance for Class 4 Advanced",
    "key": "sub_sw4a",
    "name": "SUB-SW4A"
  },
  {
    "description": "Wired Assurance for Class 4 Premium",
    "key": "sub_sw4p",
    "name": "SUB-SW4P"
  },
  {
    "description": "Marvis for Wireless",
    "key": "sub_vna",
    "name": "SUB-VNA"
  },
  {
    "description": "WAN Assurance",
    "key": "sub_wan",
    "name": "SUB-WAN"
  },
  {
    "description": "WAN Assurance for Class 1",
    "key": "sub_wan1",
    "name": "SUB-WAN1"
  },
  {
    "description": "WAN Assurance for Class 2",
    "key": "sub_wan2",
    "name": "SUB-WAN2"
  },
  {
    "description": "WAN Assurance for Class 3",
    "key": "sub_wan3",
    "name": "SUB-WAN3"
  },
  {
    "description": "WAN Assurance for Class 4",
    "key": "sub_wan4",
    "name": "SUB-WAN4"
  },
  {
    "description": "WAN Assurance for Class 5",
    "key": "sub_wan5",
    "name": "SUB-WAN5"
  },
  {
    "description": "WAN Assurance for Class 6",
    "key": "sub_wan6",
    "name": "SUB-WAN6"
  },
  {
    "description": "Marvis for WAN",
    "includes": [
      "sub_wvna1",
      "sub_wvna2",
      "sub_wvna3",
      "sub_wvna4",
      "sub_wvna5",
      "sub_wvna6"
    ],
    "key": "sub_wvna",
    "name": "SUB-WVNA"
  },
  {
    "description": "Marvis for WAN for SRX Class 1 devices",
    "key": "sub_wvna1",
    "name": "SUB-WVNA1"
  },
  {
    "description": "Marvis for WAN for SRX Class 2 devices",
    "key": "sub_wvna2",
    "name": "SUB-WVNA2"
  },
  {
    "description": "Marvis for WAN for SRX Class 3 devices",
    "key": "sub_wvna3",
    "name": "SUB-WVNA3"
  },
  {
    "description": "Marvis for WAN for SRX Class 4 devices",
    "key": "sub_wvna4",
    "name": "SUB-WVNA4"
  },
  {
    "description": "Marvis for WAN for SRX Class 5 devices",
    "key": "sub_wvna5",
    "name": "SUB-WVNA5"
  },
  {
    "description": "Marvis for WAN for SRX Class 6 devices",
    "key": "sub_wvna6",
    "name": "SUB-WVNA6"
  }
]
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1ConstLicenseTypes401ErrorException`](../../doc/models/api-v1-const-license-types-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1ConstLicenseTypes403ErrorException`](../../doc/models/api-v1-const-license-types-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1ConstLicenseTypes404ErrorException`](../../doc/models/api-v1-const-license-types-404-error-exception.md) |


# List Mx Edge Events Definitions

Get List of available MX Edge Events

```python
def list_mx_edge_events_definitions(self)
```

## Response Type

[`List of ApiV1ConstMxedgeEventsResponse`](../../doc/models/api-v1-const-mxedge-events-response.md)

## Example Usage

```python
result = constants_controller.list_mx_edge_events_definitions()
print(result)
```

## Example Response *(as JSON)*

```json
[
  {
    "description": "Config change on ME was triggered as a result of change made by user",
    "display": "ME Config changed by user",
    "example": {
      "audit_id": "e9a88814-fa81-5bdc-34b0-84e8735420e5",
      "mxcluster_id": "ed4665ed-c9ad-4835-8ca5-dda642765ad3",
      "mxedge_id": "387804a7-3474-85ce-15a2-f9a9684c9c90",
      "org_id": "2818e386-8dec-2562-9ede-5b8a0fbbdc71",
      "service": "mxagent",
      "site_id": "4ac1dcf4-9d8b-7211-65c4-057819f0862b",
      "timestamp": 1552408871,
      "type": "ME_CONFIG_CHANGED_BY_USER"
    },
    "key": "ME_CONFIG_CHANGED_BY_USER"
  }
]
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1ConstMxedgeEvents401ErrorException`](../../doc/models/api-v1-const-mxedge-events-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1ConstMxedgeEvents403ErrorException`](../../doc/models/api-v1-const-mxedge-events-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1ConstMxedgeEvents404ErrorException`](../../doc/models/api-v1-const-mxedge-events-404-error-exception.md) |


# List Mx Edge Models

Get List of available Mx Edge models

```python
def list_mx_edge_models(self)
```

## Response Type

[`List of ApiV1ConstMxedgeModelsResponse`](../../doc/models/api-v1-const-mxedge-models-response.md)

## Example Usage

```python
result = constants_controller.list_mx_edge_models()
print(result)
```

## Example Response *(as JSON)*

```json
[
  {
    "custom_ports": true,
    "display": "string",
    "model": "string",
    "ports": {
      "0": {
        "display": "string",
        "speed": 0
      },
      "1": {
        "display": "string",
        "speed": 0
      },
      "2": {
        "display": "string",
        "speed": 0
      },
      "3": {
        "display": "string",
        "speed": 0
      }
    }
  }
]
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1ConstMxedgeModels401ErrorException`](../../doc/models/api-v1-const-mxedge-models-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1ConstMxedgeModels403ErrorException`](../../doc/models/api-v1-const-mxedge-models-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1ConstMxedgeModels404ErrorException`](../../doc/models/api-v1-const-mxedge-models-404-error-exception.md) |


# List Other Device Events Definitions

Supported Events Type

```python
def list_other_device_events_definitions(self)
```

## Response Type

[`List of ApiV1ConstOtherDeviceEventsResponse`](../../doc/models/api-v1-const-other-device-events-response.md)

## Example Usage

```python
result = constants_controller.list_other_device_events_definitions()
print(result)
```

## Example Response *(as JSON)*

```json
[
  {
    "display": "Connected to NCM",
    "example": {
      "device_mac": "5c5b351e13b5",
      "mac": "0030447771c0",
      "org_id": "c080ce4d-4e35-4373-bdc4-08df15d257f5",
      "site_id": "1df889ad-9111-4c0e-a00b-8a008b83eb68",
      "text": "Connected to NCM",
      "timestamp": 1675827825.765,
      "type": "CELLULAR_EDGE_CONNECTED_TO_NCM",
      "vendor": "cradlepoint"
    },
    "key": "CELLULAR_EDGE_CONNECTED_TO_NCM"
  },
  {
    "display": "Disconnected from NCM",
    "example": {
      "device_mac": "5c5b351e13b5",
      "mac": "0030447771c0",
      "org_id": "c080ce4d-4e35-4373-bdc4-08df15d257f5",
      "site_id": "1df889ad-9111-4c0e-a00b-8a008b83eb68",
      "text": "Disconnected from NCM",
      "timestamp": 1675827825.765,
      "type": "CELLULAR_EDGE_DISCONNECTED_FROM_NCM",
      "vendor": "cradlepoint"
    },
    "key": "CELLULAR_EDGE_DISCONNECTED_FROM_NCM"
  }
]
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1ConstOtherDeviceEvents401ErrorException`](../../doc/models/api-v1-const-other-device-events-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1ConstOtherDeviceEvents403ErrorException`](../../doc/models/api-v1-const-other-device-events-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1ConstOtherDeviceEvents404ErrorException`](../../doc/models/api-v1-const-other-device-events-404-error-exception.md) |


# List Traffic Types

Get List of identified traffic

```python
def list_traffic_types(self)
```

## Response Type

[`List of ApiV1ConstTrafficTypesResponse`](../../doc/models/api-v1-const-traffic-types-response.md)

## Example Usage

```python
result = constants_controller.list_traffic_types()
print(result)
```

## Example Response *(as JSON)*

```json
[
  {
    "dscp": 0,
    "failover_policy": "string",
    "name": "string",
    "traffic_class": "string"
  }
]
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1ConstTrafficTypes401ErrorException`](../../doc/models/api-v1-const-traffic-types-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1ConstTrafficTypes403ErrorException`](../../doc/models/api-v1-const-traffic-types-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1ConstTrafficTypes404ErrorException`](../../doc/models/api-v1-const-traffic-types-404-error-exception.md) |

