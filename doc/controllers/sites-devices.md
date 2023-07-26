# Sites Devices

```python
sites_devices_controller = client.sites_devices
```

## Class Name

`SitesDevicesController`

## Methods

* [List Site Devices](../../doc/controllers/sites-devices.md#list-site-devices)
* [Count Site Device Config History](../../doc/controllers/sites-devices.md#count-site-device-config-history)
* [Search Site Device Config History](../../doc/controllers/sites-devices.md#search-site-device-config-history)
* [Count Site Devices](../../doc/controllers/sites-devices.md#count-site-devices)
* [Count Site Device Events](../../doc/controllers/sites-devices.md#count-site-device-events)
* [Search Site Devices Events](../../doc/controllers/sites-devices.md#search-site-devices-events)
* [Export Site Devices](../../doc/controllers/sites-devices.md#export-site-devices)
* [Import Site Devices](../../doc/controllers/sites-devices.md#import-site-devices)
* [Count Site Device Last Config](../../doc/controllers/sites-devices.md#count-site-device-last-config)
* [Search Site Device Last Configs](../../doc/controllers/sites-devices.md#search-site-device-last-configs)
* [Multi Restart Site Devices](../../doc/controllers/sites-devices.md#multi-restart-site-devices)
* [Search Site Devices](../../doc/controllers/sites-devices.md#search-site-devices)
* [Delete Site Device](../../doc/controllers/sites-devices.md#delete-site-device)
* [Get Site Device](../../doc/controllers/sites-devices.md#get-site-device)
* [Update Site Device](../../doc/controllers/sites-devices.md#update-site-device)
* [Get Site Device Config Cmd](../../doc/controllers/sites-devices.md#get-site-device-config-cmd)
* [Delete Site Device Image](../../doc/controllers/sites-devices.md#delete-site-device-image)
* [Add Site Device Image](../../doc/controllers/sites-devices.md#add-site-device-image)
* [Get Site Device Ztp Password](../../doc/controllers/sites-devices.md#get-site-device-ztp-password)
* [Restart Site Device](../../doc/controllers/sites-devices.md#restart-site-device)
* [Upload Site Device Support File](../../doc/controllers/sites-devices.md#upload-site-device-support-file)


# List Site Devices

Get list of devices on the site.

```python
def list_site_devices(self,
                     site_id,
                     mtype='ap',
                     name=None,
                     page=1,
                     limit=100)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `mtype` | [`Type47Enum`](../../doc/models/type-47-enum.md) | Query, Optional | device type<br>**Default**: `'ap'` |
| `name` | `string` | Query, Optional | - |
| `page` | `int` | Query, Optional | **Default**: `1`<br>**Constraints**: `>= 1` |
| `limit` | `int` | Query, Optional | **Default**: `100`<br>**Constraints**: `>= 0` |

## Response Type

[`List of DevicesArray`](../../doc/models/devices-array.md)

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

mtype = Type47Enum.AP

page = 1

limit = 100

result = sites_devices_controller.list_site_devices(
    site_id,
    mtype,
    page,
    limit
)
print(result)
```

## Example Response *(as JSON)*

```json
[
  {
    "aeroscout": {
      "enabled": true,
      "host": "string"
    },
    "ble_config": {
      "beacon_enabled": true,
      "beacon_rate": 0,
      "beacon_rate_mode": "string",
      "beam_disabled": [
        0
      ],
      "eddystone_uid_adv_power": -100,
      "eddystone_uid_beams": "string",
      "eddystone_uid_enabled": true,
      "eddystone_uid_freq_msec": 0,
      "eddystone_uid_instance": "string",
      "eddystone_uid_namespace": "string",
      "eddystone_url_adv_power": 0,
      "eddystone_url_beams": "string",
      "eddystone_url_enabled": true,
      "eddystone_url_freq_msec": 0,
      "eddystone_url_url": "string",
      "ibeacon_adv_power": -100,
      "ibeacon_beams": "string",
      "ibeacon_enabled": true,
      "ibeacon_freq_msec": 0,
      "ibeacon_major": 0,
      "ibeacon_minor": 0,
      "ibeacon_uuid": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
      "power": 0,
      "power_mode": "string"
    },
    "created_time": 0,
    "deviceprofile_id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
    "disable_eth1": true,
    "disable_eth2": true,
    "disable_eth3": true,
    "disable_module": true,
    "height": 0,
    "id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
    "image1_url": "string",
    "iot_config": {
      "A1": {
        "enabled": true,
        "name": "string",
        "output": true,
        "pullup": "internal",
        "value": true
      },
      "A2": {
        "enabled": true,
        "name": "string",
        "output": true,
        "pullup": "internal",
        "value": true
      },
      "A3": {
        "enabled": true,
        "name": "string",
        "output": true,
        "pullup": "internal",
        "value": true
      },
      "A4": {
        "enabled": true,
        "name": "string",
        "output": true,
        "pullup": "internal",
        "value": true
      },
      "DI1": {
        "enabled": true,
        "name": "string",
        "pullup": "internal",
        "value": true
      },
      "DI2": {
        "enabled": true,
        "name": "string",
        "pullup": "internal",
        "value": true
      },
      "DO": {
        "enabled": true,
        "name": "string",
        "output": true,
        "pullup": "internal",
        "value": true
      }
    },
    "ip_config": {
      "dns": [
        "string"
      ],
      "dns_suffix": [
        "string"
      ],
      "gateway": "string",
      "gateway6": "string",
      "ip": "string",
      "ip6": "string",
      "mtu": 0,
      "netmask": "string",
      "netmask6": "string",
      "type": "static",
      "type6": "string",
      "vlan_id": 1
    },
    "led": {
      "brightness": 0,
      "enabled": true
    },
    "map_id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
    "mesh": {
      "enabled": true,
      "group": 0,
      "role": "base"
    },
    "modified_time": 0,
    "name": "string",
    "notes": "string",
    "ntp_servers": [
      "string"
    ],
    "org_id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
    "orientation": 0,
    "orientation_overwrite": true,
    "poe_passthrough": true,
    "pwr_config": {
      "base": 0
    },
    "radio_config": {
      "ant_gain_24": 0,
      "ant_gain_5": 0,
      "band_24": {
        "allow_rrm_disable": true,
        "antenna_mode": "default",
        "bandwidth": 0,
        "channel": 0,
        "disabled": true,
        "power": 0,
        "power_max": 0,
        "power_min": 0,
        "preamble": "auto",
        "usage": "string"
      },
      "band_24_usage": "24",
      "band_5": {
        "allow_rrm_disable": true,
        "antenna_mode": "default",
        "bandwidth": 0,
        "channel": 0,
        "disabled": true,
        "power": 0,
        "power_max": 0,
        "power_min": 0,
        "preamble": "auto",
        "usage": "string"
      },
      "band_5_on_24_radio": {
        "allow_rrm_disable": true,
        "antenna_mode": "default",
        "bandwidth": 0,
        "channel": 0,
        "disabled": true,
        "power": 0,
        "power_max": 0,
        "power_min": 0,
        "preamble": "auto",
        "usage": "string"
      },
      "scanning_enabled": true
    },
    "site_id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
    "switch_config": {
      "enabled": true,
      "eth0": {
        "port_vlan_id": 1,
        "vlan_ids": [
          0
        ]
      },
      "eth1": {
        "port_vlan_id": 1,
        "vlan_ids": [
          0
        ]
      },
      "eth2": {
        "port_vlan_id": 1,
        "vlan_ids": [
          0
        ]
      },
      "eth3": {
        "port_vlan_id": 1,
        "vlan_ids": [
          0
        ]
      },
      "module": {
        "port_vlan_id": 1,
        "vlan_ids": [
          0
        ]
      },
      "wds": {
        "port_vlan_id": 1,
        "vlan_ids": [
          0
        ]
      }
    },
    "usb_config": {
      "cacert": "string",
      "channel": 0,
      "enabled": true,
      "host": "string",
      "port": 0,
      "type": "string",
      "verify_cert": true
    },
    "vars": {},
    "x": 0,
    "y": 0
  }
]
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesDevices401ErrorException`](../../doc/models/api-v1-sites-devices-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesDevices403ErrorException`](../../doc/models/api-v1-sites-devices-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesDevices404ErrorException`](../../doc/models/api-v1-sites-devices-404-error-exception.md) |


# Count Site Device Config History

Counts the number of entries in device config history for distinct field with given filters

```python
def count_site_device_config_history(self,
                                    site_id,
                                    distinct=None,
                                    mac=None,
                                    page=1,
                                    limit=100,
                                    start=0,
                                    end=0,
                                    duration='1d')
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `distinct` | `string` | Query, Optional | - |
| `mac` | `string` | Query, Optional | - |
| `page` | `int` | Query, Optional | **Default**: `1`<br>**Constraints**: `>= 1` |
| `limit` | `int` | Query, Optional | **Default**: `100`<br>**Constraints**: `>= 0` |
| `start` | `int` | Query, Optional | **Default**: `0`<br>**Constraints**: `>= 0` |
| `end` | `int` | Query, Optional | **Default**: `0`<br>**Constraints**: `>= 0` |
| `duration` | `string` | Query, Optional | For historical stats and/or logs where time range is needed, you can specify the time range in a few different ways:<br><br>* ?start=1430000000&end=1430864000	specify the start / end<br>* ?end=1430864000&duration=1d	specify end time and duration<br>* ?duration=1d	specify duration, end will be now() in seconds<br>**Default**: `'1d'` |

## Response Type

[`Count`](../../doc/models/count.md)

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

page = 1

limit = 100

start = 0

end = 0

duration = '10m'

result = sites_devices_controller.count_site_device_config_history(
    site_id,
    page,
    limit,
    start,
    end,
    duration
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "distinct": "string",
  "end": 0,
  "limit": 0,
  "percentage": 0,
  "results": [
    {
      "count": 0,
      "property": "string"
    }
  ],
  "start": 0,
  "total": 0
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesDevicesConfigHistoryCount401ErrorException`](../../doc/models/api-v1-sites-devices-config-history-count-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesDevicesConfigHistoryCount403ErrorException`](../../doc/models/api-v1-sites-devices-config-history-count-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesDevicesConfigHistoryCount404ErrorException`](../../doc/models/api-v1-sites-devices-config-history-count-404-error-exception.md) |


# Search Site Device Config History

Search for entries in device config history

```python
def search_site_device_config_history(self,
                                     site_id,
                                     device_type='ap',
                                     mac=None,
                                     limit=100,
                                     start=0,
                                     end=0,
                                     duration='1d')
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `device_type` | [`DeviceType2Enum`](../../doc/models/device-type-2-enum.md) | Query, Optional | **Default**: `'ap'` |
| `mac` | `string` | Query, Optional | Device MAC Address |
| `limit` | `int` | Query, Optional | **Default**: `100`<br>**Constraints**: `>= 0` |
| `start` | `int` | Query, Optional | **Default**: `0`<br>**Constraints**: `>= 0` |
| `end` | `int` | Query, Optional | **Default**: `0`<br>**Constraints**: `>= 0` |
| `duration` | `string` | Query, Optional | For historical stats and/or logs where time range is needed, you can specify the time range in a few different ways:<br><br>* ?start=1430000000&end=1430864000	specify the start / end<br>* ?end=1430864000&duration=1d	specify end time and duration<br>* ?duration=1d	specify duration, end will be now() in seconds<br>**Default**: `'1d'` |

## Response Type

[`ConfigsHistorySearch`](../../doc/models/configs-history-search.md)

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

device_type = DeviceType2Enum.AP

limit = 100

start = 0

end = 0

duration = '10m'

result = sites_devices_controller.search_site_device_config_history(
    site_id,
    device_type,
    limit,
    start,
    end,
    duration
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "end": 1531862583,
  "limit": 10,
  "results": [
    {
      "channel_24": 11,
      "channel_5": 100,
      "radio_macs": [
        "5c5b352e000a",
        "5c5b352e000b",
        "5c5b352e000c"
      ],
      "radios": [
        {
          "band": "24",
          "channel": 11
        },
        {
          "band": "5",
          "channel": 100
        }
      ],
      "secpolicy_violated": false,
      "ssids": [
        "test24",
        "test5"
      ],
      "ssids_24": [
        "test24"
      ],
      "ssids_5": [
        "test5"
      ],
      "timestamp": 1531855856.643369,
      "version": "apfw-0.2.14754-cersei-75c8",
      "wlans": [
        {
          "auth": "psk",
          "bands": [
            "24"
          ],
          "id": "be22bba7-8e22-e1cf-5185-b880816fe2cf",
          "ssid": "test24",
          "vlan_ids": [
            "1"
          ]
        },
        {
          "auth": "psk",
          "bands": [
            "5"
          ],
          "id": "f8c18724-4118-3487-811a-f98964988604",
          "ssid": "test5",
          "vlan_ids": [
            "1"
          ]
        }
      ]
    }
  ],
  "start": 1531776183,
  "total": 1
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesDevicesConfigHistorySearch401ErrorException`](../../doc/models/api-v1-sites-devices-config-history-search-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesDevicesConfigHistorySearch403ErrorException`](../../doc/models/api-v1-sites-devices-config-history-search-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesDevicesConfigHistorySearch404ErrorException`](../../doc/models/api-v1-sites-devices-config-history-search-404-error-exception.md) |


# Count Site Devices

Counts the number of entries in ap events history for distinct field with given filters

```python
def count_site_devices(self,
                      site_id,
                      distinct='model',
                      hostname=None,
                      model=None,
                      mac=None,
                      version=None,
                      mxtunnel_status=None,
                      mxedge_id=None,
                      lldp_system_name=None,
                      lldp_system_desc=None,
                      lldp_port_id=None,
                      lldp_mgmt_addr=None,
                      map_id=None,
                      page=1,
                      limit=100,
                      start=0,
                      end=0,
                      duration='1d')
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `distinct` | [`Distinct8Enum`](../../doc/models/distinct-8-enum.md) | Query, Optional | **Default**: `'model'` |
| `hostname` | `string` | Query, Optional | - |
| `model` | `string` | Query, Optional | - |
| `mac` | `string` | Query, Optional | - |
| `version` | `string` | Query, Optional | - |
| `mxtunnel_status` | `string` | Query, Optional | - |
| `mxedge_id` | `string` | Query, Optional | - |
| `lldp_system_name` | `string` | Query, Optional | - |
| `lldp_system_desc` | `string` | Query, Optional | - |
| `lldp_port_id` | `string` | Query, Optional | - |
| `lldp_mgmt_addr` | `string` | Query, Optional | - |
| `map_id` | `string` | Query, Optional | - |
| `page` | `int` | Query, Optional | **Default**: `1`<br>**Constraints**: `>= 1` |
| `limit` | `int` | Query, Optional | **Default**: `100`<br>**Constraints**: `>= 0` |
| `start` | `int` | Query, Optional | **Default**: `0`<br>**Constraints**: `>= 0` |
| `end` | `int` | Query, Optional | **Default**: `0`<br>**Constraints**: `>= 0` |
| `duration` | `string` | Query, Optional | For historical stats and/or logs where time range is needed, you can specify the time range in a few different ways:<br><br>* ?start=1430000000&end=1430864000	specify the start / end<br>* ?end=1430864000&duration=1d	specify end time and duration<br>* ?duration=1d	specify duration, end will be now() in seconds<br>**Default**: `'1d'` |

## Response Type

[`ApiV1SitesDevicesCountResponse`](../../doc/models/api-v1-sites-devices-count-response.md)

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

distinct = Distinct8Enum.MODEL

page = 1

limit = 100

start = 0

end = 0

duration = '10m'

result = sites_devices_controller.count_site_devices(
    site_id,
    distinct,
    page,
    limit,
    start,
    end,
    duration
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "distinct": "model",
  "end": 1604304258.674506,
  "limit": 10,
  "percentage": 100,
  "results": [
    {
      "count": 1,
      "model": "AP41"
    },
    {
      "count": 1,
      "model": "AP43"
    }
  ],
  "start": 1604217858.6744902,
  "total": 2
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesDevicesCount401ErrorException`](../../doc/models/api-v1-sites-devices-count-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesDevicesCount403ErrorException`](../../doc/models/api-v1-sites-devices-count-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesDevicesCount404ErrorException`](../../doc/models/api-v1-sites-devices-count-404-error-exception.md) |


# Count Site Device Events

Counts the number of entries in ap events history for distinct field with given filters

```python
def count_site_device_events(self,
                            site_id,
                            distinct='model',
                            model=None,
                            mtype=None,
                            type_code=None,
                            page=1,
                            limit=100,
                            start=0,
                            end=0,
                            duration='1d')
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `distinct` | [`Distinct9Enum`](../../doc/models/distinct-9-enum.md) | Query, Optional | **Default**: `'model'` |
| `model` | `string` | Query, Optional | - |
| `mtype` | `string` | Query, Optional | - |
| `type_code` | `string` | Query, Optional | - |
| `page` | `int` | Query, Optional | **Default**: `1`<br>**Constraints**: `>= 1` |
| `limit` | `int` | Query, Optional | **Default**: `100`<br>**Constraints**: `>= 0` |
| `start` | `int` | Query, Optional | **Default**: `0`<br>**Constraints**: `>= 0` |
| `end` | `int` | Query, Optional | **Default**: `0`<br>**Constraints**: `>= 0` |
| `duration` | `string` | Query, Optional | For historical stats and/or logs where time range is needed, you can specify the time range in a few different ways:<br><br>* ?start=1430000000&end=1430864000	specify the start / end<br>* ?end=1430864000&duration=1d	specify end time and duration<br>* ?duration=1d	specify duration, end will be now() in seconds<br>**Default**: `'1d'` |

## Response Type

[`ApiV1SitesDevicesEventsCountResponse`](../../doc/models/api-v1-sites-devices-events-count-response.md)

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

distinct = Distinct9Enum.MODEL

page = 1

limit = 100

start = 0

end = 0

duration = '10m'

result = sites_devices_controller.count_site_device_events(
    site_id,
    distinct,
    page,
    limit,
    start,
    end,
    duration
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "distinct": "type",
  "end": 1531862583,
  "limit": 10,
  "percentage": 100,
  "results": [
    {
      "count": 10,
      "type": "AP_CONNECT_STATUS"
    },
    {
      "count": 4,
      "type": "AP_CONFIGURED"
    }
  ],
  "start": 1531776183,
  "total": 2
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesDevicesEventsCount401ErrorException`](../../doc/models/api-v1-sites-devices-events-count-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesDevicesEventsCount403ErrorException`](../../doc/models/api-v1-sites-devices-events-count-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesDevicesEventsCount404ErrorException`](../../doc/models/api-v1-sites-devices-events-count-404-error-exception.md) |


# Search Site Devices Events

Search Devices Events

```python
def search_site_devices_events(self,
                              site_id,
                              device_type=None,
                              mac=None,
                              model=None,
                              text=None,
                              timestamp=None,
                              mtype=None,
                              limit=100,
                              start=0,
                              end=0,
                              duration='1d')
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `device_type` | [`DeviceType2Enum`](../../doc/models/device-type-2-enum.md) | Query, Optional | - |
| `mac` | `string` | Query, Optional | device mac |
| `model` | `string` | Query, Optional | device model |
| `text` | `string` | Query, Optional | event message |
| `timestamp` | `string` | Query, Optional | event time |
| `mtype` | `string` | Query, Optional | see [Event Types Definition](/#operation/listDeviceEventsDefinitions) |
| `limit` | `int` | Query, Optional | **Default**: `100`<br>**Constraints**: `>= 0` |
| `start` | `int` | Query, Optional | **Default**: `0`<br>**Constraints**: `>= 0` |
| `end` | `int` | Query, Optional | **Default**: `0`<br>**Constraints**: `>= 0` |
| `duration` | `string` | Query, Optional | For historical stats and/or logs where time range is needed, you can specify the time range in a few different ways:<br><br>* ?start=1430000000&end=1430864000	specify the start / end<br>* ?end=1430864000&duration=1d	specify end time and duration<br>* ?duration=1d	specify duration, end will be now() in seconds<br>**Default**: `'1d'` |

## Response Type

[`ApiV1SitesDevicesEventsSearchResponse`](../../doc/models/api-v1-sites-devices-events-search-response.md)

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

limit = 100

start = 0

end = 0

duration = '10m'

result = sites_devices_controller.search_site_devices_events(
    site_id,
    limit,
    start,
    end,
    duration
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "end": 1531862583,
  "limit": 2,
  "next": "/api/v1/sites/8aaba0aa-09cc-44bd-9709-33b98040550c/devices/events/search?ap=5c5b350e0001&end=1531855849.000&limit=2&start=1531776183.0",
  "results": [
    {
      "last_reboot_time": 1531854327,
      "text": "Success",
      "timestamp": 1531855849.226722,
      "type": "AP_CONNECT_STATUS",
      "type_code": 2002
    },
    {
      "timestamp": 1531854326,
      "type": "AP_CONFIGURED"
    }
  ],
  "start": 1531776183,
  "total": 14
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesDevicesEventsSearch401ErrorException`](../../doc/models/api-v1-sites-devices-events-search-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesDevicesEventsSearch403ErrorException`](../../doc/models/api-v1-sites-devices-events-search-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesDevicesEventsSearch404ErrorException`](../../doc/models/api-v1-sites-devices-events-search-404-error-exception.md) |


# Export Site Devices

To download the exported device information

```python
def export_site_devices(self,
                       site_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |

## Response Type

`string`

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

result = sites_devices_controller.export_site_devices(site_id)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesDevicesExport401ErrorException`](../../doc/models/api-v1-sites-devices-export-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesDevicesExport403ErrorException`](../../doc/models/api-v1-sites-devices-export-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesDevicesExport404ErrorException`](../../doc/models/api-v1-sites-devices-export-404-error-exception.md) |


# Import Site Devices

Import Information for Multiple Devices

CSV format:

```csv
mac,name,map_id,x,y,height,orientation,labels,band_24.power,band_24.bandwidth,band_24.channel,band_24.disabled,band_5.power,band_5.bandwidth,band_5.channel,band_5.disabled,band_6.power,band_6.bandwidth,band_6.channel,band_6.disabled
5c5b53010101,"AP 1",845a23bf-bed9-e43c-4c86-6fa474be7ae5,30,10,2.3,45,"guest, campus, vip",1,20,0,false,0,40,0,false,17,80,0,false
```

```python
def import_site_devices(self,
                       site_id,
                       body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `body` | [`List of DeviceAp`](../../doc/models/device-ap.md) | Body, Optional | - |

## Response Type

[`List of DevicesArray`](../../doc/models/devices-array.md)

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

body = [
    DeviceAp(
        aeroscout=ApAeroscout(
            enabled=False,
            host='string',
            locate_connected=True
        ),
        ble_config=ApBle(
            beacon_enabled=True,
            beacon_rate=0,
            beacon_rate_mode=BeaconRateModeEnum.DEFAULT,
            beam_disabled=[
                0
            ],
            eddystone_uid_adv_power=-100,
            eddystone_uid_beams='string',
            eddystone_uid_enabled=True,
            eddystone_uid_freq_msec=0,
            eddystone_uid_instance='string',
            eddystone_uid_namespace='string',
            eddystone_url_adv_power=0,
            eddystone_url_beams='string',
            eddystone_url_enabled=True,
            eddystone_url_freq_msec=0,
            eddystone_url_url='string',
            ibeacon_adv_power=-100,
            ibeacon_beams='string',
            ibeacon_enabled=False,
            ibeacon_freq_msec=0,
            ibeacon_major=0,
            ibeacon_minor=0,
            ibeacon_uuid='1f89bc00-d0af-481b-82fe-a6629259a39f',
            power=9,
            power_mode='string'
        ),
        created_time=0,
        deviceprofile_id='366a0f23-8d77-404c-8908-b2e629ba0782',
        disable_eth_1=False,
        disable_eth_2=False,
        disable_eth_3=False,
        disable_module=False,
        for_site=True,
        height=0,
        id='484f6eca-6276-4993-bfeb-55cbbbba6f08',
        image_1_url='string',
        image_2_url='string',
        image_3_url='string',
        iot_config=ApIot(
            a_1=ApIotOutput(
                enabled=False,
                name='string',
                output=True,
                pullup=PullupEnum.INTERNAL,
                value=0
            ),
            a_2=ApIotOutput(
                enabled=False,
                name='string',
                output=True,
                pullup=PullupEnum.INTERNAL,
                value=0
            ),
            a_3=ApIotOutput(
                enabled=False,
                name='string',
                output=True,
                pullup=PullupEnum.INTERNAL,
                value=0
            ),
            a_4=ApIotOutput(
                enabled=False,
                name='string',
                output=True,
                pullup=PullupEnum.INTERNAL,
                value=0
            ),
            di_1=ApIotInput(
                enabled=False,
                name='string',
                pullup=PullupEnum.INTERNAL
            ),
            di_2=ApIotInput(
                enabled=False,
                name='string',
                pullup=PullupEnum.INTERNAL
            ),
            do=ApIotOutput(
                enabled=False,
                name='string',
                output=True,
                pullup=PullupEnum.INTERNAL,
                value=0
            )
        ),
        ip_config=ApIp(
            dns=[
                'string'
            ],
            dns_suffix=[
                'string'
            ],
            gateway='192.168.0.1',
            gateway_6='2001:0db8:85a3:0000:0000:8a2e:0370:7334',
            ip='192.168.0.1',
            ip_6='2001:0db8:85a3:0000:0000:8a2e:0370:7334',
            mtu=0,
            netmask='192.168.0.1',
            netmask_6='2001:0db8:85a3:0000:0000:8a2e:0370:7334',
            mtype=Type2Enum.STATIC,
            type_6=Type6Enum.STATIC,
            vlan_id=1
        ),
        led=ApLed(
            brightness=0,
            enabled=True
        ),
        locked=True,
        map_id='09d2b626-2e4e-45ef-a3c4-e6aeb6c83db1',
        mesh=ApMesh(
            enabled=False,
            group=0,
            role=Role1Enum.BASE
        ),
        modified_time=0,
        name='string',
        notes='string',
        ntp_servers=[
            'string'
        ],
        org_id='a40f5d1f-d889-42e9-94ea-b9b33585fc6b',
        orientation=0,
        poe_passthrough=False,
        port_config={
            "property1": ApPortConfig(
                disabled=True,
                dynamic_vlan=DynamicVlan(
                    default_vlan_id=0,
                    enabled=True,
                    mtype='string',
                    vlans={
                        "property1": 'string',
                        "property2": 'string'
                    }
                ),
                enable_mac_auth=True,
                forwarding=ForwardingEnum.ALL,
                mx_tunnel_id='5f5cac07-0805-46ea-aafd-5c5729042729',
                mxtunnel_name='string',
                port_auth=PortAuthEnum.NONE,
                port_vlan_id=0,
                radius_config=JunosRadiusConfig(
                    acct_interim_interval=0,
                    acct_servers=[
                        AcctServer(
                            host='string',
                            port=1813,
                            secret='string',
                            keywrap_enabled=True,
                            keywrap_format='string',
                            keywrap_kek='string',
                            keywrap_mack='string'
                        )
                    ],
                    auth_servers=[
                        AuthServer(
                            host='string',
                            port=1812,
                            secret='string',
                            keywrap_enabled=True,
                            keywrap_format='string',
                            keywrap_kek='string',
                            keywrap_mack='string'
                        )
                    ],
                    auth_servers_retries=3,
                    auth_servers_timeout=5,
                    coa_enabled=False,
                    coa_port=3799,
                    network='string',
                    source_ip='string'
                ),
                radsec=Radsec(
                    enabled=True,
                    idle_timeout=0,
                    server_name='string',
                    servers=[
                        Server(
                            host='string',
                            port=0
                        )
                    ],
                    use_mxedge=True
                ),
                vlan_id=0,
                vland_ids=[
                    0
                ],
                wxtunnel_id='string',
                wxtunnel_remote_id='string'
            ),
            "property2": ApPortConfig(
                disabled=True,
                dynamic_vlan=DynamicVlan(
                    default_vlan_id=0,
                    enabled=True,
                    mtype='string',
                    vlans={
                        "property1": 'string',
                        "property2": 'string'
                    }
                ),
                enable_mac_auth=True,
                forwarding=ForwardingEnum.ALL,
                mx_tunnel_id='5f5cac07-0805-46ea-aafd-5c5729042729',
                mxtunnel_name='string',
                port_auth=PortAuthEnum.NONE,
                port_vlan_id=0,
                radius_config=JunosRadiusConfig(
                    acct_interim_interval=0,
                    acct_servers=[
                        AcctServer(
                            host='string',
                            port=1813,
                            secret='string',
                            keywrap_enabled=True,
                            keywrap_format='string',
                            keywrap_kek='string',
                            keywrap_mack='string'
                        )
                    ],
                    auth_servers=[
                        AuthServer(
                            host='string',
                            port=1812,
                            secret='string',
                            keywrap_enabled=True,
                            keywrap_format='string',
                            keywrap_kek='string',
                            keywrap_mack='string'
                        )
                    ],
                    auth_servers_retries=3,
                    auth_servers_timeout=5,
                    coa_enabled=False,
                    coa_port=3799,
                    network='string',
                    source_ip='string'
                ),
                radsec=Radsec(
                    enabled=True,
                    idle_timeout=0,
                    server_name='string',
                    servers=[
                        Server(
                            host='string',
                            port=0
                        )
                    ],
                    use_mxedge=True
                ),
                vlan_id=0,
                vland_ids=[
                    0
                ],
                wxtunnel_id='string',
                wxtunnel_remote_id='string'
            )
        },
        pwr_config=PwrConfig(
            base=0
        ),
        radio_config=ApRadio(
            ant_gain_24=0,
            ant_gain_5=0,
            ant_gain_6=0,
            band_24=ApRadioBand(
                allow_rrm_disable=True,
                ant_gain=0,
                antenna_mode=AntennaModeEnum.DEFAULT,
                bandwidth=BandwidthEnum.ENUM_20,
                channel=0,
                channels=[
                    0
                ],
                disabled=True,
                power=0,
                power_max=0,
                power_min=0,
                preamble=PreambleEnum.SHORT,
                usage=UsageEnum.ENUM_24
            ),
            band_24_usage=Band24UsageEnum.ENUM_24,
            band_5=ApRadioBand(
                allow_rrm_disable=True,
                ant_gain=0,
                antenna_mode=AntennaModeEnum.DEFAULT,
                bandwidth=BandwidthEnum.ENUM_20,
                channel=0,
                channels=[
                    0
                ],
                disabled=True,
                power=0,
                power_max=0,
                power_min=0,
                preamble=PreambleEnum.SHORT,
                usage=UsageEnum.ENUM_24
            ),
            band_5_on_24_radio=ApRadioBand(
                allow_rrm_disable=True,
                ant_gain=0,
                antenna_mode=AntennaModeEnum.DEFAULT,
                bandwidth=BandwidthEnum.ENUM_20,
                channel=0,
                channels=[
                    0
                ],
                disabled=True,
                power=0,
                power_max=0,
                power_min=0,
                preamble=PreambleEnum.SHORT,
                usage=UsageEnum.ENUM_24
            ),
            band_6=ApRadioBand(
                allow_rrm_disable=True,
                ant_gain=0,
                antenna_mode=AntennaModeEnum.DEFAULT,
                bandwidth=BandwidthEnum.ENUM_20,
                channel=0,
                channels=[
                    0
                ],
                disabled=True,
                power=0,
                power_max=0,
                power_min=0,
                preamble=PreambleEnum.SHORT,
                usage=UsageEnum.ENUM_24
            ),
            scanning_enabled=True
        ),
        site_id='72771e6a-6f5e-4de4-a5b9-1266c4197811',
        usb_config=ApUsb(
            cacert='string',
            channel=0,
            enabled=True,
            host='string',
            port=0,
            mtype=Type3Enum.IMAGOTAG,
            verify_cert=True
        ),
        vars={},
        x=0,
        y=0
    )
]

result = sites_devices_controller.import_site_devices(
    site_id,
    body
)
print(result)
```

## Example Response *(as JSON)*

```json
[
  {
    "aeroscout": {
      "enabled": true,
      "host": "string"
    },
    "ble_config": {
      "beacon_enabled": true,
      "beacon_rate": 0,
      "beacon_rate_mode": "string",
      "beam_disabled": [
        0
      ],
      "eddystone_uid_adv_power": -100,
      "eddystone_uid_beams": "string",
      "eddystone_uid_enabled": true,
      "eddystone_uid_freq_msec": 0,
      "eddystone_uid_instance": "string",
      "eddystone_uid_namespace": "string",
      "eddystone_url_adv_power": 0,
      "eddystone_url_beams": "string",
      "eddystone_url_enabled": true,
      "eddystone_url_freq_msec": 0,
      "eddystone_url_url": "string",
      "ibeacon_adv_power": -100,
      "ibeacon_beams": "string",
      "ibeacon_enabled": true,
      "ibeacon_freq_msec": 0,
      "ibeacon_major": 0,
      "ibeacon_minor": 0,
      "ibeacon_uuid": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
      "power": 0,
      "power_mode": "string"
    },
    "created_time": 0,
    "deviceprofile_id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
    "disable_eth1": true,
    "disable_eth2": true,
    "disable_eth3": true,
    "disable_module": true,
    "height": 0,
    "id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
    "image1_url": "string",
    "iot_config": {
      "A1": {
        "enabled": true,
        "name": "string",
        "output": true,
        "pullup": "internal",
        "value": true
      },
      "A2": {
        "enabled": true,
        "name": "string",
        "output": true,
        "pullup": "internal",
        "value": true
      },
      "A3": {
        "enabled": true,
        "name": "string",
        "output": true,
        "pullup": "internal",
        "value": true
      },
      "A4": {
        "enabled": true,
        "name": "string",
        "output": true,
        "pullup": "internal",
        "value": true
      },
      "DI1": {
        "enabled": true,
        "name": "string",
        "pullup": "internal",
        "value": true
      },
      "DI2": {
        "enabled": true,
        "name": "string",
        "pullup": "internal",
        "value": true
      },
      "DO": {
        "enabled": true,
        "name": "string",
        "output": true,
        "pullup": "internal",
        "value": true
      }
    },
    "ip_config": {
      "dns": [
        "string"
      ],
      "dns_suffix": [
        "string"
      ],
      "gateway": "string",
      "gateway6": "string",
      "ip": "string",
      "ip6": "string",
      "mtu": 0,
      "netmask": "string",
      "netmask6": "string",
      "type": "static",
      "type6": "string",
      "vlan_id": 1
    },
    "led": {
      "brightness": 0,
      "enabled": true
    },
    "map_id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
    "mesh": {
      "enabled": true,
      "group": 0,
      "role": "base"
    },
    "modified_time": 0,
    "name": "string",
    "notes": "string",
    "ntp_servers": [
      "string"
    ],
    "org_id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
    "orientation": 0,
    "orientation_overwrite": true,
    "poe_passthrough": true,
    "pwr_config": {
      "base": 0
    },
    "radio_config": {
      "ant_gain_24": 0,
      "ant_gain_5": 0,
      "band_24": {
        "allow_rrm_disable": true,
        "antenna_mode": "default",
        "bandwidth": 0,
        "channel": 0,
        "disabled": true,
        "power": 0,
        "power_max": 0,
        "power_min": 0,
        "preamble": "auto",
        "usage": "string"
      },
      "band_24_usage": "24",
      "band_5": {
        "allow_rrm_disable": true,
        "antenna_mode": "default",
        "bandwidth": 0,
        "channel": 0,
        "disabled": true,
        "power": 0,
        "power_max": 0,
        "power_min": 0,
        "preamble": "auto",
        "usage": "string"
      },
      "band_5_on_24_radio": {
        "allow_rrm_disable": true,
        "antenna_mode": "default",
        "bandwidth": 0,
        "channel": 0,
        "disabled": true,
        "power": 0,
        "power_max": 0,
        "power_min": 0,
        "preamble": "auto",
        "usage": "string"
      },
      "scanning_enabled": true
    },
    "site_id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
    "switch_config": {
      "enabled": true,
      "eth0": {
        "port_vlan_id": 1,
        "vlan_ids": [
          0
        ]
      },
      "eth1": {
        "port_vlan_id": 1,
        "vlan_ids": [
          0
        ]
      },
      "eth2": {
        "port_vlan_id": 1,
        "vlan_ids": [
          0
        ]
      },
      "eth3": {
        "port_vlan_id": 1,
        "vlan_ids": [
          0
        ]
      },
      "module": {
        "port_vlan_id": 1,
        "vlan_ids": [
          0
        ]
      },
      "wds": {
        "port_vlan_id": 1,
        "vlan_ids": [
          0
        ]
      }
    },
    "usb_config": {
      "cacert": "string",
      "channel": 0,
      "enabled": true,
      "host": "string",
      "port": 0,
      "type": "string",
      "verify_cert": true
    },
    "vars": {},
    "x": 0,
    "y": 0
  }
]
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesDevicesImport401ErrorException`](../../doc/models/api-v1-sites-devices-import-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesDevicesImport403ErrorException`](../../doc/models/api-v1-sites-devices-import-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesDevicesImport404ErrorException`](../../doc/models/api-v1-sites-devices-import-404-error-exception.md) |


# Count Site Device Last Config

Counts the number of entries in device config history for distinct field with given filters

```python
def count_site_device_last_config(self,
                                 site_id,
                                 distinct='mac',
                                 page=1,
                                 limit=100,
                                 start=0,
                                 end=0,
                                 duration='1d')
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `distinct` | [`Distinct10Enum`](../../doc/models/distinct-10-enum.md) | Query, Optional | **Default**: `'mac'` |
| `page` | `int` | Query, Optional | **Default**: `1`<br>**Constraints**: `>= 1` |
| `limit` | `int` | Query, Optional | **Default**: `100`<br>**Constraints**: `>= 0` |
| `start` | `int` | Query, Optional | **Default**: `0`<br>**Constraints**: `>= 0` |
| `end` | `int` | Query, Optional | **Default**: `0`<br>**Constraints**: `>= 0` |
| `duration` | `string` | Query, Optional | For historical stats and/or logs where time range is needed, you can specify the time range in a few different ways:<br><br>* ?start=1430000000&end=1430864000	specify the start / end<br>* ?end=1430864000&duration=1d	specify end time and duration<br>* ?duration=1d	specify duration, end will be now() in seconds<br>**Default**: `'1d'` |

## Response Type

[`ApiV1SitesDevicesLastConfigCountResponse`](../../doc/models/api-v1-sites-devices-last-config-count-response.md)

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

distinct = Distinct10Enum.MAC

page = 1

limit = 100

start = 0

end = 0

duration = '10m'

result = sites_devices_controller.count_site_device_last_config(
    site_id,
    distinct,
    page,
    limit,
    start,
    end,
    duration
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "distinct": "ap",
  "end": 1604310805,
  "limit": 10,
  "percentage": 100,
  "results": [
    {
      "ap": "5c5b35000000",
      "count": 1
    },
    {
      "ap": "5c5b35000001",
      "count": 1
    }
  ],
  "start": 1604307205,
  "total": 2
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesDevicesLastConfigCount401ErrorException`](../../doc/models/api-v1-sites-devices-last-config-count-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesDevicesLastConfigCount403ErrorException`](../../doc/models/api-v1-sites-devices-last-config-count-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesDevicesLastConfigCount404ErrorException`](../../doc/models/api-v1-sites-devices-last-config-count-404-error-exception.md) |


# Search Site Device Last Configs

Search Device Last Configs

```python
def search_site_device_last_configs(self,
                                   site_id,
                                   device_type='ap',
                                   mac=None,
                                   version=None,
                                   name=None,
                                   limit=100,
                                   start=0,
                                   end=0,
                                   duration='1d')
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `device_type` | [`DeviceType2Enum`](../../doc/models/device-type-2-enum.md) | Query, Optional | **Default**: `'ap'` |
| `mac` | `string` | Query, Optional | - |
| `version` | `string` | Query, Optional | - |
| `name` | `string` | Query, Optional | - |
| `limit` | `int` | Query, Optional | **Default**: `100`<br>**Constraints**: `>= 0` |
| `start` | `int` | Query, Optional | **Default**: `0`<br>**Constraints**: `>= 0` |
| `end` | `int` | Query, Optional | **Default**: `0`<br>**Constraints**: `>= 0` |
| `duration` | `string` | Query, Optional | For historical stats and/or logs where time range is needed, you can specify the time range in a few different ways:<br><br>* ?start=1430000000&end=1430864000	specify the start / end<br>* ?end=1430864000&duration=1d	specify end time and duration<br>* ?duration=1d	specify duration, end will be now() in seconds<br>**Default**: `'1d'` |

## Response Type

[`ConfigsHistorySearch`](../../doc/models/configs-history-search.md)

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

device_type = DeviceType2Enum.AP

limit = 100

start = 0

end = 0

duration = '10m'

result = sites_devices_controller.search_site_device_last_configs(
    site_id,
    device_type,
    limit,
    start,
    end,
    duration
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "end": 1531862583,
  "limit": 10,
  "results": [
    {
      "channel_24": 11,
      "channel_5": 100,
      "radio_macs": [
        "5c5b352e000a",
        "5c5b352e000b",
        "5c5b352e000c"
      ],
      "radios": [
        {
          "band": "24",
          "channel": 11
        },
        {
          "band": "5",
          "channel": 100
        }
      ],
      "secpolicy_violated": false,
      "ssids": [
        "test24",
        "test5"
      ],
      "ssids_24": [
        "test24"
      ],
      "ssids_5": [
        "test5"
      ],
      "timestamp": 1531855856.643369,
      "version": "apfw-0.2.14754-cersei-75c8",
      "wlans": [
        {
          "auth": "psk",
          "bands": [
            "24"
          ],
          "id": "be22bba7-8e22-e1cf-5185-b880816fe2cf",
          "ssid": "test24",
          "vlan_ids": [
            "1"
          ]
        },
        {
          "auth": "psk",
          "bands": [
            "5"
          ],
          "id": "f8c18724-4118-3487-811a-f98964988604",
          "ssid": "test5",
          "vlan_ids": [
            "1"
          ]
        }
      ]
    }
  ],
  "start": 1531776183,
  "total": 1
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesDevicesLastConfigSearch401ErrorException`](../../doc/models/api-v1-sites-devices-last-config-search-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesDevicesLastConfigSearch403ErrorException`](../../doc/models/api-v1-sites-devices-last-config-search-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesDevicesLastConfigSearch404ErrorException`](../../doc/models/api-v1-sites-devices-last-config-search-404-error-exception.md) |


# Multi Restart Site Devices

Note that only the devices that are connected will be restarted.

```python
def multi_restart_site_devices(self,
                              site_id,
                              body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `body` | [`ApiV1SitesDevicesRestartRequest`](../../doc/models/api-v1-sites-devices-restart-request.md) | Body, Optional | Request Body |

## Response Type

`object`

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

body = ApiV1SitesDevicesRestartRequest(
    device_ids=[
        '00000000-0000-0000-1000-5c5b35584a6f',
        '00000000-0000-0000-1000-5c5b350ea3b3'
    ]
)

result = sites_devices_controller.multi_restart_site_devices(
    site_id,
    body
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesDevicesRestart401ErrorException`](../../doc/models/api-v1-sites-devices-restart-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesDevicesRestart403ErrorException`](../../doc/models/api-v1-sites-devices-restart-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesDevicesRestart404ErrorException`](../../doc/models/api-v1-sites-devices-restart-404-error-exception.md) |


# Search Site Devices

Search Device

```python
def search_site_devices(self,
                       site_id,
                       hostname=None,
                       mtype='ap',
                       model=None,
                       mac=None,
                       version=None,
                       power_constrained=None,
                       ip_address=None,
                       mxtunnel_status=None,
                       mxedge_id=None,
                       lldp_system_name=None,
                       lldp_system_desc=None,
                       lldp_port_id=None,
                       lldp_mgmt_addr=None,
                       band_24_channel=None,
                       band_5_channel=None,
                       band_6_channel=None,
                       band_24_bandwith=None,
                       band_5_bandwith=None,
                       band_6_bandwith=None,
                       eth_0_port_speed=None,
                       sort='timestamp',
                       desc_sort=None,
                       stats=False,
                       limit=100,
                       start=0,
                       end=0,
                       duration='1d')
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `hostname` | `string` | Query, Optional | partial / full hostname |
| `mtype` | [`Type16Enum`](../../doc/models/type-16-enum.md) | Query, Optional | device type<br>**Default**: `'ap'` |
| `model` | `string` | Query, Optional | device model |
| `mac` | `string` | Query, Optional | device MAC |
| `version` | `string` | Query, Optional | version |
| `power_constrained` | `bool` | Query, Optional | power_constrained |
| `ip_address` | `string` | Query, Optional | - |
| `mxtunnel_status` | [`MxtunnelStatusEnum`](../../doc/models/mxtunnel-status-enum.md) | Query, Optional | MxTunnel status, up / down |
| `mxedge_id` | `uuid\|string` | Query, Optional | Mist Edge id, if AP is connecting to a Mist Edge |
| `lldp_system_name` | `string` | Query, Optional | LLDP system name |
| `lldp_system_desc` | `string` | Query, Optional | LLDP system description |
| `lldp_port_id` | `string` | Query, Optional | LLDP port id |
| `lldp_mgmt_addr` | `string` | Query, Optional | LLDP management ip address |
| `band_24_channel` | `int` | Query, Optional | Channel of band_24 |
| `band_5_channel` | `int` | Query, Optional | Channel of band_5 |
| `band_6_channel` | `int` | Query, Optional | Channel of band_6 |
| `band_24_bandwith` | `int` | Query, Optional | Bandwidth of band_24 |
| `band_5_bandwith` | `int` | Query, Optional | Bandwidth of band_5 |
| `band_6_bandwith` | `int` | Query, Optional | Bandwidth of band_6 |
| `eth_0_port_speed` | `int` | Query, Optional | Port speed of eth0 |
| `sort` | [`Sort1Enum`](../../doc/models/sort-1-enum.md) | Query, Optional | sort options<br>**Default**: `'timestamp'` |
| `desc_sort` | [`DescSortEnum`](../../doc/models/desc-sort-enum.md) | Query, Optional | sort options in reverse order |
| `stats` | `bool` | Query, Optional | whether to return device stats<br>**Default**: `False` |
| `limit` | `int` | Query, Optional | **Default**: `100`<br>**Constraints**: `>= 0` |
| `start` | `int` | Query, Optional | **Default**: `0`<br>**Constraints**: `>= 0` |
| `end` | `int` | Query, Optional | **Default**: `0`<br>**Constraints**: `>= 0` |
| `duration` | `string` | Query, Optional | For historical stats and/or logs where time range is needed, you can specify the time range in a few different ways:<br><br>* ?start=1430000000&end=1430864000	specify the start / end<br>* ?end=1430864000&duration=1d	specify end time and duration<br>* ?duration=1d	specify duration, end will be now() in seconds<br>**Default**: `'1d'` |

## Response Type

[`DevicesSearch`](../../doc/models/devices-search.md)

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

mtype = Type16Enum.AP

ip_address = '192.168.1.1'

sort = Sort1Enum.TIMESTAMP

stats = False

limit = 100

start = 0

end = 0

duration = '10m'

result = sites_devices_controller.search_site_devices(
    site_id,
    mtype,
    ip_address,
    sort,
    stats,
    limit,
    start,
    end,
    duration
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "end": 0,
  "limit": 0,
  "next": "string",
  "results": [
    {
      "hostname": [
        "AP41-STB-3E5299-WH-2001",
        "AP41-STB-3E5299-WH-50",
        "AP41-STB-3E5299",
        "5c5b353e5299"
      ],
      "ip": "10.2.16.205",
      "lldp_mgmt_addr": "10.2.10.139",
      "lldp_port_desc": "GigabitEthernet1/0/1",
      "lldp_port_id": "Gi1/0/1",
      "lldp_system_desc": "Cisco IOS Software, C2960S Software (C2960S-UNIVERSALK9-M), Version 15.2(1)E1, RELEASE SOFTWARE (fc2)\nTechnical Support: http://www.cisco.com/techsupport\nCopyright (c) 1986-2013 by Cisco Systems, Inc.\nCompiled Fri 22-Nov-13 07:10 by prod_rel_team",
      "lldp_system_name": "ME-DC-1-ACC-SW",
      "mac": "5c5b353e5299",
      "model": "AP41",
      "mxedge_id": "00000000-0000-0000-1000-43a81f238391",
      "mxtunnel_status": "down",
      "org_id": "6748cfa6-4e12-11e6-9188-0242ac110007",
      "site_id": "a8178443-ecb5-461c-b854-f16627619ab3",
      "sku": "AP41-US",
      "timestamp": 1596588619.007,
      "uptime": 85280,
      "version": "0.7.20216"
    }
  ],
  "start": 0,
  "total": 0
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesDevicesSearch401ErrorException`](../../doc/models/api-v1-sites-devices-search-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesDevicesSearch403ErrorException`](../../doc/models/api-v1-sites-devices-search-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesDevicesSearch404ErrorException`](../../doc/models/api-v1-sites-devices-search-404-error-exception.md) |


# Delete Site Device

Delete Site Device

```python
def delete_site_device(self,
                      site_id,
                      device_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `device_id` | `uuid\|string` | Template, Required | - |

## Response Type

`object`

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

device_id = '000000ab-00ab-00ab-00ab-0000000000ab'

result = sites_devices_controller.delete_site_device(
    site_id,
    device_id
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesDevices401ErrorException`](../../doc/models/api-v1-sites-devices-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesDevices403ErrorException`](../../doc/models/api-v1-sites-devices-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesDevices404ErrorException`](../../doc/models/api-v1-sites-devices-404-error-exception.md) |


# Get Site Device

Get Device Configuration

```python
def get_site_device(self,
                   site_id,
                   device_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `device_id` | `uuid\|string` | Template, Required | - |

## Response Type

`mixed`

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

device_id = '000000ab-00ab-00ab-00ab-0000000000ab'

result = sites_devices_controller.get_site_device(
    site_id,
    device_id
)
print(result)
```

## Example Response

```
{
  "aeroscout": {
    "enabled": false,
    "host": "string",
    "locate_connected": true
  },
  "ble_config": {
    "beacon_enabled": true,
    "beacon_rate": 0,
    "beacon_rate_mode": "default",
    "beam_disabled": [
      0
    ],
    "eddystone_uid_adv_power": -100,
    "eddystone_uid_beams": "string",
    "eddystone_uid_enabled": true,
    "eddystone_uid_freq_msec": 0,
    "eddystone_uid_instance": "string",
    "eddystone_uid_namespace": "string",
    "eddystone_url_adv_power": 0,
    "eddystone_url_beams": "string",
    "eddystone_url_enabled": true,
    "eddystone_url_freq_msec": 0,
    "eddystone_url_url": "string",
    "ibeacon_adv_power": -100,
    "ibeacon_beams": "string",
    "ibeacon_enabled": false,
    "ibeacon_freq_msec": 0,
    "ibeacon_major": 0,
    "ibeacon_minor": 0,
    "ibeacon_uuid": "1f89bc00-d0af-481b-82fe-a6629259a39f",
    "power": 9,
    "power_mode": "string"
  },
  "created_time": 0,
  "deviceprofile_id": "366a0f23-8d77-404c-8908-b2e629ba0782",
  "disable_eth1": false,
  "disable_eth2": false,
  "disable_eth3": false,
  "disable_module": false,
  "for_site": true,
  "height": 0,
  "id": "474f6eca-6276-4993-bfeb-5fcbbbba6f08",
  "image1_url": "string",
  "image2_url": "string",
  "image3_url": "string",
  "iot_config": {
    "A1": {
      "enabled": false,
      "name": "string",
      "output": true,
      "pullup": "internal",
      "value": 0
    },
    "A2": {
      "enabled": false,
      "name": "string",
      "output": true,
      "pullup": "internal",
      "value": 0
    },
    "A3": {
      "enabled": false,
      "name": "string",
      "output": true,
      "pullup": "internal",
      "value": 0
    },
    "A4": {
      "enabled": false,
      "name": "string",
      "output": true,
      "pullup": "internal",
      "value": 0
    },
    "DI1": {
      "enabled": false,
      "name": "string",
      "pullup": "internal"
    },
    "DI2": {
      "enabled": false,
      "name": "string",
      "pullup": "internal"
    },
    "DO": {
      "enabled": false,
      "name": "string",
      "output": true,
      "pullup": "internal",
      "value": 0
    }
  },
  "ip_config": {
    "dns": [
      "string"
    ],
    "dns_suffix": [
      "string"
    ],
    "gateway": "192.168.0.1",
    "gateway6": "2001:0db8:85a3:0000:0000:8a2e:0370:7334",
    "ip": "192.168.0.1",
    "ip6": "2001:0db8:85a3:0000:0000:8a2e:0370:7334",
    "mtu": 0,
    "netmask": "192.168.0.1",
    "netmask6": "2001:0db8:85a3:0000:0000:8a2e:0370:7334",
    "type": "static",
    "type6": "static",
    "vlan_id": 1
  },
  "led": {
    "brightness": 0,
    "enabled": true
  },
  "map_id": "09d2b626-2e4e-45ef-a3c4-e6aeb6c83db1",
  "mesh": {
    "enabled": false,
    "group": 0,
    "role": "base"
  },
  "modified_time": 0,
  "name": "string",
  "notes": "string",
  "ntp_servers": [
    "string"
  ],
  "org_id": "a40f5d1f-d889-42e9-94ea-b9b33585fc6b",
  "orientation": 0,
  "orientation_overwrite": true,
  "poe_passthrough": false,
  "port_config": {
    "property1": {
      "disabled": true,
      "dynamic_vlan": {
        "default_vlan_id": 0,
        "enabled": true,
        "type": "string",
        "vlans": {
          "property1": "string",
          "property2": "string"
        }
      },
      "enable_mac_auth": true,
      "forwarding": "all",
      "mx_tunnel_id": "5f5cac07-0805-46ea-aafd-5c5729042729",
      "mxtunnel_name": "string",
      "port_auth": "none",
      "port_vlan_id": 0,
      "radius_config": {
        "acct_interim_interval": 0,
        "acct_servers": [
          {
            "host": "string",
            "port": 1813,
            "secret": "string"
          }
        ],
        "auth_servers": [
          {
            "host": "string",
            "port": 1812,
            "secret": "string"
          }
        ],
        "auth_servers_retries": 3,
        "auth_servers_timeout": 5,
        "coa_enabled": false,
        "coa_port": 3799,
        "network": "string",
        "source_ip": "string"
      },
      "radsec": {
        "enabled": true,
        "idle_timeout": 0,
        "server_name": "string",
        "servers": [
          {
            "host": "string",
            "port": 0
          }
        ],
        "use_mxedge": true
      },
      "vlan_id": 0,
      "vland_ids": [
        0
      ],
      "wxtunnel_id": "string",
      "wxtunnel_remote_id": "string"
    },
    "property2": {
      "disabled": true,
      "dynamic_vlan": {
        "default_vlan_id": 0,
        "enabled": true,
        "type": "string",
        "vlans": {
          "property1": "string",
          "property2": "string"
        }
      },
      "enable_mac_auth": true,
      "forwarding": "all",
      "mx_tunnel_id": "5f5cac07-0805-46ea-aafd-5c5729042729",
      "mxtunnel_name": "string",
      "port_auth": "none",
      "port_vlan_id": 0,
      "radius_config": {
        "acct_interim_interval": 0,
        "acct_servers": [
          {
            "host": "string",
            "port": 1813,
            "secret": "string"
          }
        ],
        "auth_servers": [
          {
            "host": "string",
            "port": 1812,
            "secret": "string"
          }
        ],
        "auth_servers_retries": 3,
        "auth_servers_timeout": 5,
        "coa_enabled": false,
        "coa_port": 3799,
        "network": "string",
        "source_ip": "string"
      },
      "radsec": {
        "enabled": true,
        "idle_timeout": 0,
        "server_name": "string",
        "servers": [
          {
            "host": "string",
            "port": 0
          }
        ],
        "use_mxedge": true
      },
      "vlan_id": 0,
      "vland_ids": [
        0
      ],
      "wxtunnel_id": "string",
      "wxtunnel_remote_id": "string"
    }
  },
  "pwr_config": {
    "base": 0
  },
  "radio_config": {
    "ant_gain_24": 0,
    "ant_gain_5": 0,
    "ant_gain_6": 0,
    "band_24": {
      "allow_rrm_disable": true,
      "ant_gain": 0,
      "antenna_mode": "default",
      "bandwidth": 20,
      "channel": 0,
      "channels": [
        0
      ],
      "disabled": true,
      "power": 0,
      "power_max": 0,
      "power_min": 0,
      "preamble": "short",
      "usage": "24"
    },
    "band_24_usage": "24",
    "band_5": {
      "allow_rrm_disable": true,
      "ant_gain": 0,
      "antenna_mode": "default",
      "bandwidth": 20,
      "channel": 0,
      "channels": [
        0
      ],
      "disabled": true,
      "power": 0,
      "power_max": 0,
      "power_min": 0,
      "preamble": "short",
      "usage": "24"
    },
    "band_5_on_24_radio": {
      "allow_rrm_disable": true,
      "ant_gain": 0,
      "antenna_mode": "default",
      "bandwidth": 20,
      "channel": 0,
      "channels": [
        0
      ],
      "disabled": true,
      "power": 0,
      "power_max": 0,
      "power_min": 0,
      "preamble": "short",
      "usage": "24"
    },
    "band_6": {
      "allow_rrm_disable": true,
      "ant_gain": 0,
      "antenna_mode": "default",
      "bandwidth": 20,
      "channel": 0,
      "channels": [
        0
      ],
      "disabled": true,
      "power": 0,
      "power_max": 0,
      "power_min": 0,
      "preamble": "short",
      "usage": "24"
    },
    "scanning_enabled": true
  },
  "site_id": "72771e6a-6f5e-4de4-a5b9-1266c4197811",
  "switch_config": {
    "enabled": false,
    "eth0": {
      "enable_vlan": true,
      "port_vlan_id": 0,
      "vlan_ids": [
        0
      ]
    },
    "eth1": {
      "enable_vlan": true,
      "port_vlan_id": 0,
      "vlan_ids": [
        0
      ]
    },
    "eth2": {
      "enable_vlan": true,
      "port_vlan_id": 0,
      "vlan_ids": [
        0
      ]
    },
    "eth3": {
      "enable_vlan": true,
      "port_vlan_id": 0,
      "vlan_ids": [
        0
      ]
    },
    "module": {
      "enable_vlan": true,
      "port_vlan_id": 0,
      "vlan_ids": [
        0
      ]
    },
    "wds": {
      "enable_vlan": true,
      "port_vlan_id": 0,
      "vlan_ids": [
        0
      ]
    }
  },
  "usb_config": {
    "cacert": "string",
    "channel": 0,
    "enabled": true,
    "host": "string",
    "port": 0,
    "type": "imagotag",
    "verify_cert": true
  },
  "vars": {},
  "x": 0,
  "y": 0
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesDevices401ErrorException`](../../doc/models/api-v1-sites-devices-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesDevices403ErrorException`](../../doc/models/api-v1-sites-devices-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesDevices404ErrorException`](../../doc/models/api-v1-sites-devices-404-error-exception.md) |


# Update Site Device

Update Device Configuration

```python
def update_site_device(self,
                      site_id,
                      device_id,
                      body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `device_id` | `uuid\|string` | Template, Required | - |
| `body` | `object` | Body, Optional | Request Body |

## Response Type

`mixed`

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

device_id = '000000ab-00ab-00ab-00ab-0000000000ab'

body = jsonpickle.decode('{"aeroscout":{"enabled":true,"host":"string"},"ble_config":{"beacon_enabled":true,"beacon_rate":0,"beacon_rate_mode":"default","beam_disabled":[0],"eddystone_uid_adv_power":-100,"eddystone_uid_beams":"string","eddystone_uid_enabled":true,"eddystone_uid_freq_msec":0,"eddystone_uid_instance":"string","eddystone_uid_namespace":"string","eddystone_url_adv_power":0,"eddystone_url_beams":"string","eddystone_url_enabled":true,"eddystone_url_freq_msec":0,"eddystone_url_url":"string","ibeacon_adv_power":-100,"ibeacon_beams":"string","ibeacon_enabled":true,"ibeacon_freq_msec":0,"ibeacon_major":0,"ibeacon_minor":0,"ibeacon_uuid":"b069b358-4c97-5319-1f8c-7c5ca64d6ab1","power":1,"power_mode":"string"},"deviceprofile_id":"b069b358-4c97-5319-1f8c-7c5ca64d6ab1","disable_eth1":true,"disable_eth2":true,"disable_eth3":true,"disable_module":true,"height":0,"image1_url":"string","iot_config":{"A1":{"enabled":true,"name":"string","output":false,"pullup":"internal"},"A2":{"enabled":true,"name":"string","output":false,"pullup":"internal"},"A3":{"enabled":true,"name":"string","output":false,"pullup":"internal"},"A4":{"enabled":true,"name":"string","output":false,"pullup":"internal"},"DI1":{"enabled":true,"name":"string","pullup":"internal"},"DI2":{"enabled":true,"name":"string","pullup":"internal"},"DO":{"enabled":true,"name":"string","output":true,"pullup":"internal","value":1}},"ip_config":{"dns":["string"],"dns_suffix":["string"],"gateway":"192.168.0.1","gateway6":"2001:0db8:85a3:0000:0000:8a2e:0370:7334","ip":"192.168.0.1","ip6":"2001:0db8:85a3:0000:0000:8a2e:0370:7334","mtu":0,"netmask":"192.168.0.1","netmask6":"2001:0db8:85a3:0000:0000:8a2e:0370:7334","type":"static","type6":"static","vlan_id":1},"led":{"brightness":0,"enabled":true},"map_id":"b069b358-4c97-5319-1f8c-7c5ca64d6ab1","mesh":{"enabled":true,"group":0,"role":"base"},"name":"string","notes":"string","ntp_servers":["string"],"orientation":0,"orientation_overwrite":true,"poe_passthrough":true,"port_config":{"property1":{"disabled":true,"dynamic_vlan":{"default_vlan_id":1,"enabled":true,"type":"string","vlans":{"property1":"string","property2":"string"}},"enable_mac_auth":true,"forwarding":"all","mx_tunnel_id":"b069b358-4c97-5319-1f8c-7c5ca64d6ab1","mxtunnel_name":"string","port_auth":"none","port_vlan_id":1,"radius_config":{"acct_interim_interval":0,"acct_servers":[{"host":"string","port":0,"secret":"string"}],"auth_servers":[{"host":"string","port":0,"secret":"string"}],"auth_servers_retries":0,"auth_servers_timeout":0},"radsec":{"enabled":true,"server_name":"string","servers":[{"host":"string","port":0}],"use_mxedge":true},"vland_ids":[0],"wxtunnel_id":"string","wxtunnel_remote_id":"string"},"property2":{"disabled":true,"dynamic_vlan":{"default_vlan_id":1,"enabled":true,"type":"string","vlans":{"property1":"string","property2":"string"}},"enable_mac_auth":true,"forwarding":"all","mx_tunnel_id":"420f6eca-6276-5993-bfeb-53cbbbba6f01","mxtunnel_name":"string","port_auth":"none","port_vlan_id":1,"radius_config":{"acct_interim_interval":0,"acct_servers":[{"host":"string","port":0,"secret":"string"}],"auth_servers":[{"host":"string","port":0,"secret":"string"}],"auth_servers_retries":0,"auth_servers_timeout":0},"radsec":{"enabled":true,"server_name":"string","servers":[{"host":"string","port":0}],"use_mxedge":true},"vland_ids":[0],"wxtunnel_id":"string","wxtunnel_remote_id":"string"}},"pwr_config":{"base":0},"radio_config":{"ant_gain_24":0,"ant_gain_5":0,"band_24":{"allow_rrm_disable":true,"antenna_mode":"default","bandwidth":20,"channel":0,"disabled":true,"power":0,"power_max":0,"power_min":0,"preamble":"auto","usage":"24"},"band_24_usage":"24","band_5":{"allow_rrm_disable":true,"antenna_mode":"default","bandwidth":20,"channel":0,"disabled":true,"power":0,"power_max":0,"power_min":0,"preamble":"auto","usage":"24"},"band_5_on_24_radio":{"allow_rrm_disable":true,"antenna_mode":"default","bandwidth":20,"channel":0,"disabled":true,"power":0,"power_max":0,"power_min":0,"preamble":"auto","usage":"24"},"scanning_enabled":true},"switch_config":{"enabled":true,"eth0":{"port_vlan_id":1,"vlan_ids":[0]},"eth1":{"port_vlan_id":1,"vlan_ids":[0]},"eth2":{"port_vlan_id":1,"vlan_ids":[0]},"eth3":{"port_vlan_id":1,"vlan_ids":[0]},"module":{"port_vlan_id":1,"vlan_ids":[0]},"wds":{"port_vlan_id":1,"vlan_ids":[0]}},"usb_config":{"cacert":"string","channel":0,"enabled":true,"host":"string","port":0,"type":"imagotag","verify_cert":true},"vars":{},"x":0,"y":0}')

result = sites_devices_controller.update_site_device(
    site_id,
    device_id,
    body
)
print(result)
```

## Example Response

```
{
  "aeroscout": {
    "enabled": false,
    "host": "string",
    "locate_connected": true
  },
  "ble_config": {
    "beacon_enabled": true,
    "beacon_rate": 0,
    "beacon_rate_mode": "default",
    "beam_disabled": [
      0
    ],
    "eddystone_uid_adv_power": -100,
    "eddystone_uid_beams": "string",
    "eddystone_uid_enabled": true,
    "eddystone_uid_freq_msec": 0,
    "eddystone_uid_instance": "string",
    "eddystone_uid_namespace": "string",
    "eddystone_url_adv_power": 0,
    "eddystone_url_beams": "string",
    "eddystone_url_enabled": true,
    "eddystone_url_freq_msec": 0,
    "eddystone_url_url": "string",
    "ibeacon_adv_power": -100,
    "ibeacon_beams": "string",
    "ibeacon_enabled": false,
    "ibeacon_freq_msec": 0,
    "ibeacon_major": 0,
    "ibeacon_minor": 0,
    "ibeacon_uuid": "1f89bc00-d0af-481b-82fe-a6629259a39f",
    "power": 9,
    "power_mode": "string"
  },
  "created_time": 0,
  "deviceprofile_id": "366a0f23-8d77-404c-8908-b2e629ba0782",
  "disable_eth1": false,
  "disable_eth2": false,
  "disable_eth3": false,
  "disable_module": false,
  "for_site": true,
  "height": 0,
  "id": "474f6eca-6276-4993-bfeb-5fcbbbba6f08",
  "image1_url": "string",
  "image2_url": "string",
  "image3_url": "string",
  "iot_config": {
    "A1": {
      "enabled": false,
      "name": "string",
      "output": true,
      "pullup": "internal",
      "value": 0
    },
    "A2": {
      "enabled": false,
      "name": "string",
      "output": true,
      "pullup": "internal",
      "value": 0
    },
    "A3": {
      "enabled": false,
      "name": "string",
      "output": true,
      "pullup": "internal",
      "value": 0
    },
    "A4": {
      "enabled": false,
      "name": "string",
      "output": true,
      "pullup": "internal",
      "value": 0
    },
    "DI1": {
      "enabled": false,
      "name": "string",
      "pullup": "internal"
    },
    "DI2": {
      "enabled": false,
      "name": "string",
      "pullup": "internal"
    },
    "DO": {
      "enabled": false,
      "name": "string",
      "output": true,
      "pullup": "internal",
      "value": 0
    }
  },
  "ip_config": {
    "dns": [
      "string"
    ],
    "dns_suffix": [
      "string"
    ],
    "gateway": "192.168.0.1",
    "gateway6": "2001:0db8:85a3:0000:0000:8a2e:0370:7334",
    "ip": "192.168.0.1",
    "ip6": "2001:0db8:85a3:0000:0000:8a2e:0370:7334",
    "mtu": 0,
    "netmask": "192.168.0.1",
    "netmask6": "2001:0db8:85a3:0000:0000:8a2e:0370:7334",
    "type": "static",
    "type6": "static",
    "vlan_id": 1
  },
  "led": {
    "brightness": 0,
    "enabled": true
  },
  "map_id": "09d2b626-2e4e-45ef-a3c4-e6aeb6c83db1",
  "mesh": {
    "enabled": false,
    "group": 0,
    "role": "base"
  },
  "modified_time": 0,
  "name": "string",
  "notes": "string",
  "ntp_servers": [
    "string"
  ],
  "org_id": "a40f5d1f-d889-42e9-94ea-b9b33585fc6b",
  "orientation": 0,
  "orientation_overwrite": true,
  "poe_passthrough": false,
  "port_config": {
    "property1": {
      "disabled": true,
      "dynamic_vlan": {
        "default_vlan_id": 0,
        "enabled": true,
        "type": "string",
        "vlans": {
          "property1": "string",
          "property2": "string"
        }
      },
      "enable_mac_auth": true,
      "forwarding": "all",
      "mx_tunnel_id": "5f5cac07-0805-46ea-aafd-5c5729042729",
      "mxtunnel_name": "string",
      "port_auth": "none",
      "port_vlan_id": 0,
      "radius_config": {
        "acct_interim_interval": 0,
        "acct_servers": [
          {
            "host": "string",
            "port": 1813,
            "secret": "string"
          }
        ],
        "auth_servers": [
          {
            "host": "string",
            "port": 1812,
            "secret": "string"
          }
        ],
        "auth_servers_retries": 3,
        "auth_servers_timeout": 5,
        "coa_enabled": false,
        "coa_port": 3799,
        "network": "string",
        "source_ip": "string"
      },
      "radsec": {
        "enabled": true,
        "idle_timeout": 0,
        "server_name": "string",
        "servers": [
          {
            "host": "string",
            "port": 0
          }
        ],
        "use_mxedge": true
      },
      "vlan_id": 0,
      "vland_ids": [
        0
      ],
      "wxtunnel_id": "string",
      "wxtunnel_remote_id": "string"
    },
    "property2": {
      "disabled": true,
      "dynamic_vlan": {
        "default_vlan_id": 0,
        "enabled": true,
        "type": "string",
        "vlans": {
          "property1": "string",
          "property2": "string"
        }
      },
      "enable_mac_auth": true,
      "forwarding": "all",
      "mx_tunnel_id": "5f5cac07-0805-46ea-aafd-5c5729042729",
      "mxtunnel_name": "string",
      "port_auth": "none",
      "port_vlan_id": 0,
      "radius_config": {
        "acct_interim_interval": 0,
        "acct_servers": [
          {
            "host": "string",
            "port": 1813,
            "secret": "string"
          }
        ],
        "auth_servers": [
          {
            "host": "string",
            "port": 1812,
            "secret": "string"
          }
        ],
        "auth_servers_retries": 3,
        "auth_servers_timeout": 5,
        "coa_enabled": false,
        "coa_port": 3799,
        "network": "string",
        "source_ip": "string"
      },
      "radsec": {
        "enabled": true,
        "idle_timeout": 0,
        "server_name": "string",
        "servers": [
          {
            "host": "string",
            "port": 0
          }
        ],
        "use_mxedge": true
      },
      "vlan_id": 0,
      "vland_ids": [
        0
      ],
      "wxtunnel_id": "string",
      "wxtunnel_remote_id": "string"
    }
  },
  "pwr_config": {
    "base": 0
  },
  "radio_config": {
    "ant_gain_24": 0,
    "ant_gain_5": 0,
    "ant_gain_6": 0,
    "band_24": {
      "allow_rrm_disable": true,
      "ant_gain": 0,
      "antenna_mode": "default",
      "bandwidth": 20,
      "channel": 0,
      "channels": [
        0
      ],
      "disabled": true,
      "power": 0,
      "power_max": 0,
      "power_min": 0,
      "preamble": "short",
      "usage": "24"
    },
    "band_24_usage": "24",
    "band_5": {
      "allow_rrm_disable": true,
      "ant_gain": 0,
      "antenna_mode": "default",
      "bandwidth": 20,
      "channel": 0,
      "channels": [
        0
      ],
      "disabled": true,
      "power": 0,
      "power_max": 0,
      "power_min": 0,
      "preamble": "short",
      "usage": "24"
    },
    "band_5_on_24_radio": {
      "allow_rrm_disable": true,
      "ant_gain": 0,
      "antenna_mode": "default",
      "bandwidth": 20,
      "channel": 0,
      "channels": [
        0
      ],
      "disabled": true,
      "power": 0,
      "power_max": 0,
      "power_min": 0,
      "preamble": "short",
      "usage": "24"
    },
    "band_6": {
      "allow_rrm_disable": true,
      "ant_gain": 0,
      "antenna_mode": "default",
      "bandwidth": 20,
      "channel": 0,
      "channels": [
        0
      ],
      "disabled": true,
      "power": 0,
      "power_max": 0,
      "power_min": 0,
      "preamble": "short",
      "usage": "24"
    },
    "scanning_enabled": true
  },
  "site_id": "72771e6a-6f5e-4de4-a5b9-1266c4197811",
  "switch_config": {
    "enabled": false,
    "eth0": {
      "enable_vlan": true,
      "port_vlan_id": 0,
      "vlan_ids": [
        0
      ]
    },
    "eth1": {
      "enable_vlan": true,
      "port_vlan_id": 0,
      "vlan_ids": [
        0
      ]
    },
    "eth2": {
      "enable_vlan": true,
      "port_vlan_id": 0,
      "vlan_ids": [
        0
      ]
    },
    "eth3": {
      "enable_vlan": true,
      "port_vlan_id": 0,
      "vlan_ids": [
        0
      ]
    },
    "module": {
      "enable_vlan": true,
      "port_vlan_id": 0,
      "vlan_ids": [
        0
      ]
    },
    "wds": {
      "enable_vlan": true,
      "port_vlan_id": 0,
      "vlan_ids": [
        0
      ]
    }
  },
  "usb_config": {
    "cacert": "string",
    "channel": 0,
    "enabled": true,
    "host": "string",
    "port": 0,
    "type": "imagotag",
    "verify_cert": true
  },
  "vars": {},
  "x": 0,
  "y": 0
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesDevices401ErrorException`](../../doc/models/api-v1-sites-devices-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesDevices403ErrorException`](../../doc/models/api-v1-sites-devices-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesDevices404ErrorException`](../../doc/models/api-v1-sites-devices-404-error-exception.md) |


# Get Site Device Config Cmd

Get Config CLI Commands
For a brown-field switch deployment where we adopted the switch through Adoption Command, we do not wipe out / overwrite the existing config automatically. Instead, we generate CLI commands that we would have generated. The user can inspect, modify, and incorporate this into their existing config manually.

Once they feel comfortable about the config we generate, they can enable allow_mist_config where we will take full control of their config like a claimed switch

```python
def get_site_device_config_cmd(self,
                              site_id,
                              device_id,
                              sort='false')
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `device_id` | `uuid\|string` | Template, Required | - |
| `sort` | [`Sort2Enum`](../../doc/models/sort-2-enum.md) | Query, Optional | Make output cmds sorted (for better readability) or not.<br>**Default**: `'false'` |

## Response Type

[`DeviceConfigCmd`](../../doc/models/device-config-cmd.md)

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

device_id = '000000ab-00ab-00ab-00ab-0000000000ab'

sort = Sort2Enum.FALSE

result = sites_devices_controller.get_site_device_config_cmd(
    site_id,
    device_id,
    sort
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "cli": [
    "set system hostname corp-a135"
  ]
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesDevicesConfigCmd401ErrorException`](../../doc/models/api-v1-sites-devices-config-cmd-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesDevicesConfigCmd403ErrorException`](../../doc/models/api-v1-sites-devices-config-cmd-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesDevicesConfigCmd404ErrorException`](../../doc/models/api-v1-sites-devices-config-cmd-404-error-exception.md) |


# Delete Site Device Image

Delete image from a device

```python
def delete_site_device_image(self,
                            site_id,
                            device_id,
                            image_number)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `device_id` | `uuid\|string` | Template, Required | - |
| `image_number` | `int` | Template, Required | - |

## Response Type

`object`

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

device_id = '000000ab-00ab-00ab-00ab-0000000000ab'

image_number = 110

result = sites_devices_controller.delete_site_device_image(
    site_id,
    device_id,
    image_number
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesDevicesImageImageNumber401ErrorException`](../../doc/models/api-v1-sites-devices-image-image-number-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesDevicesImageImageNumber403ErrorException`](../../doc/models/api-v1-sites-devices-image-image-number-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesDevicesImageImageNumber404ErrorException`](../../doc/models/api-v1-sites-devices-image-image-number-404-error-exception.md) |


# Add Site Device Image

Attach up to 3 images to a device

```python
def add_site_device_image(self,
                         site_id,
                         device_id,
                         image_number,
                         file=None,
                         json=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `device_id` | `uuid\|string` | Template, Required | - |
| `image_number` | `int` | Template, Required | - |
| `file` | `string` | Form, Optional | binary file |
| `json` | `string` | Form, Optional | JSON string describing your upload |

## Response Type

`object`

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

device_id = '000000ab-00ab-00ab-00ab-0000000000ab'

image_number = 110

result = sites_devices_controller.add_site_device_image(
    site_id,
    device_id,
    image_number
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesDevicesImageImageNumber401ErrorException`](../../doc/models/api-v1-sites-devices-image-image-number-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesDevicesImageImageNumber403ErrorException`](../../doc/models/api-v1-sites-devices-image-image-number-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesDevicesImageImageNumber404ErrorException`](../../doc/models/api-v1-sites-devices-image-image-number-404-error-exception.md) |


# Get Site Device Ztp Password

In the case where soemthing happens during/after ZTP, the root-password is modified (required for ZTP to set up outbound-ssh) but the user-defined password config has not be configured. This API can be used to retrieve the temporary password.

```python
def get_site_device_ztp_password(self,
                                site_id,
                                device_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `device_id` | `uuid\|string` | Template, Required | - |

## Response Type

[`ApiV1SitesDevicesRequestZtpPasswordResponse`](../../doc/models/api-v1-sites-devices-request-ztp-password-response.md)

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

device_id = '000000ab-00ab-00ab-00ab-0000000000ab'

result = sites_devices_controller.get_site_device_ztp_password(
    site_id,
    device_id
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "root_password": "ef8070ef8f924edb592e1819ed64b31172ab8de9d5cde75d3f46acd9506202ab9b1cbb97e381c5aa11037f17e5ed7b4b609461cd813d944670549d410ef82f2e"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesDevicesRequestZtpPassword401ErrorException`](../../doc/models/api-v1-sites-devices-request-ztp-password-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesDevicesRequestZtpPassword403ErrorException`](../../doc/models/api-v1-sites-devices-request-ztp-password-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesDevicesRequestZtpPassword404ErrorException`](../../doc/models/api-v1-sites-devices-request-ztp-password-404-error-exception.md) |


# Restart Site Device

Restart / Reboot a device

```python
def restart_site_device(self,
                       site_id,
                       device_id,
                       body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `device_id` | `uuid\|string` | Template, Required | - |
| `body` | [`ApiV1SitesDevicesRestartRequest1`](../../doc/models/api-v1-sites-devices-restart-request-1.md) | Body, Optional | - |

## Response Type

`object`

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

device_id = '000000ab-00ab-00ab-00ab-0000000000ab'

result = sites_devices_controller.restart_site_device(
    site_id,
    device_id
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesDevicesRestart401ErrorException`](../../doc/models/api-v1-sites-devices-restart-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesDevicesRestart403ErrorException`](../../doc/models/api-v1-sites-devices-restart-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesDevicesRestart404ErrorException`](../../doc/models/api-v1-sites-devices-restart-404-error-exception.md) |


# Upload Site Device Support File

Support / Upload device support files

#### Info Param

**Parameter**|**Description**
:-------------: |:-------------: |:-------------:
process|Upload 1 file with output of show system processes extensive
outbound-ssh|Upload 1 file that concatenates all /var/log/outbound-ssh.log* files
messages|Upload 1 to 10 /var/log/messages* files
core-dumps|Upload all core dump files, if any
full|string|Upload 1 file with output of request support information, 1 file that concatenates all /var/log/outbound-ssh.log files, all core dump files, the 3 most recent /var/log/messages files, and Mist agent logs (for Junos devices running the Mist agent)
var-logs|Upload all non-empty files in the /var/log/ directory
jma-logs|Upload Mist agent logs (for Junos devices running the Mist agent only)

```python
def upload_site_device_support_file(self,
                                   site_id,
                                   device_id,
                                   body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `device_id` | `uuid\|string` | Template, Required | - |
| `body` | [`ApiV1SitesDevicesSupportRequest`](../../doc/models/api-v1-sites-devices-support-request.md) | Body, Optional | Request Body |

## Response Type

`object`

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

device_id = '000000ab-00ab-00ab-00ab-0000000000ab'

body = ApiV1SitesDevicesSupportRequest(
    info=InfoEnum.FULL
)

result = sites_devices_controller.upload_site_device_support_file(
    site_id,
    device_id,
    body
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Device not online | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesDevicesSupport401ErrorException`](../../doc/models/api-v1-sites-devices-support-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesDevicesSupport403ErrorException`](../../doc/models/api-v1-sites-devices-support-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesDevicesSupport404ErrorException`](../../doc/models/api-v1-sites-devices-support-404-error-exception.md) |

