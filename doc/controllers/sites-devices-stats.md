# Sites Devices Stats

```python
sites_devices_stats_controller = client.sites_devices_stats
```

## Class Name

`SitesDevicesStatsController`

## Methods

* [Count Site Bgp Stats](../../doc/controllers/sites-devices-stats.md#count-site-bgp-stats)
* [Search Site Bgp Stats](../../doc/controllers/sites-devices-stats.md#search-site-bgp-stats)
* [List Site Devices Stats](../../doc/controllers/sites-devices-stats.md#list-site-devices-stats)
* [Get Site Device Stats](../../doc/controllers/sites-devices-stats.md#get-site-device-stats)
* [Get Site All Clients Stats by Device](../../doc/controllers/sites-devices-stats.md#get-site-all-clients-stats-by-device)
* [List Site Mx Edges Stats](../../doc/controllers/sites-devices-stats.md#list-site-mx-edges-stats)
* [Get Site Mx Edge Stats](../../doc/controllers/sites-devices-stats.md#get-site-mx-edge-stats)
* [Count Site Sw or Gw Ports](../../doc/controllers/sites-devices-stats.md#count-site-sw-or-gw-ports)
* [Search Site Sw or Gw Ports](../../doc/controllers/sites-devices-stats.md#search-site-sw-or-gw-ports)
* [Count Site Switch Ports](../../doc/controllers/sites-devices-stats.md#count-site-switch-ports)
* [Search Site Switch Ports](../../doc/controllers/sites-devices-stats.md#search-site-switch-ports)


# Count Site Bgp Stats

Count BGP Stats

```python
def count_site_bgp_stats(self,
                        site_id,
                        state=None,
                        distinct=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `state` | `string` | Query, Optional | - |
| `distinct` | `string` | Query, Optional | - |

## Response Type

[`Count`](../../doc/models/count.md)

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

result = sites_devices_stats_controller.count_site_bgp_stats(site_id)
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
| 401 | Unauthorized | [`ApiV1SitesStatsBgpPeersCount401ErrorException`](../../doc/models/api-v1-sites-stats-bgp-peers-count-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesStatsBgpPeersCount403ErrorException`](../../doc/models/api-v1-sites-stats-bgp-peers-count-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesStatsBgpPeersCount404ErrorException`](../../doc/models/api-v1-sites-stats-bgp-peers-count-404-error-exception.md) |


# Search Site Bgp Stats

Search BGP Stats

```python
def search_site_bgp_stats(self,
                         site_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |

## Response Type

[`BgpStatsArraySearch`](../../doc/models/bgp-stats-array-search.md)

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

result = sites_devices_stats_controller.search_site_bgp_stats(site_id)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "end": 1619518989.4989712,
  "limit": 10,
  "results": [
    {
      "as": 65000,
      "mac": "020001c04668",
      "neighbor": "15.8.3.5",
      "neighbor_mac": "c15353123096",
      "org_id": "0c160b7f-1027-4cd1-923b-744534c4b070",
      "rx_pkts": 63366,
      "rx_routes": 60,
      "site_id": "725a8d34-a126-4f2c-b990-d1219421cb75",
      "state": "established",
      "tx_pkts": 1735,
      "uptime": 31355,
      "vrf_name": "default"
    }
  ],
  "start": 1619518689.4989705,
  "total": 1
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesStatsBgpPeersSearch401ErrorException`](../../doc/models/api-v1-sites-stats-bgp-peers-search-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesStatsBgpPeersSearch403ErrorException`](../../doc/models/api-v1-sites-stats-bgp-peers-search-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesStatsBgpPeersSearch404ErrorException`](../../doc/models/api-v1-sites-stats-bgp-peers-search-404-error-exception.md) |


# List Site Devices Stats

Get List of Site Devices Stats

```python
def list_site_devices_stats(self,
                           site_id,
                           mtype='ap',
                           status='all',
                           page=1,
                           limit=100)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `mtype` | [`Type47Enum`](../../doc/models/type-47-enum.md) | Query, Optional | **Default**: `'ap'` |
| `status` | [`Status9Enum`](../../doc/models/status-9-enum.md) | Query, Optional | **Default**: `'all'` |
| `page` | `int` | Query, Optional | **Default**: `1`<br>**Constraints**: `>= 1` |
| `limit` | `int` | Query, Optional | **Default**: `100`<br>**Constraints**: `>= 0` |

## Response Type

[`List of DevicesArrayStatsSite`](../../doc/models/devices-array-stats-site.md)

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

mtype = Type47Enum.AP

status = Status9Enum.ALL

page = 1

limit = 100

result = sites_devices_stats_controller.list_site_devices_stats(
    site_id,
    mtype,
    status,
    page,
    limit
)
print(result)
```

## Example Response *(as JSON)*

```json
[
  {
    "ble_config": {
      "beacon_rate": 3,
      "beacon_rate_model": "custom",
      "beam_disabled": [
        1,
        3,
        6
      ],
      "power": 10,
      "power_mode": "custom"
    },
    "ble_stat": {
      "beacon_rate": 3,
      "eddystone_uid_enabled": false,
      "eddystone_uid_freq_msec": 200,
      "eddystone_uid_instance": "5c5b35000001",
      "eddystone_uid_namespace": "2818e3868dec25629ede",
      "eddystone_url_enabled": true,
      "eddystone_url_freq_msec": 100,
      "eddystone_url_url": "https://www.abc.com",
      "ibeacon_enabled": true,
      "ibeacon_major": 13,
      "ibeacon_minor": 138,
      "ibeacon_uuid": "f3f17139-704a-f03a-2786-0400279e37c3",
      "major": 12345,
      "minors": [
        201,
        202,
        203,
        204,
        205,
        206,
        207,
        208
      ],
      "power": 10,
      "rx_bytes": 135,
      "rx_pkts": 135,
      "tx_bytes": 5231513353,
      "tx_pkts": 135135135,
      "tx_resets": 0,
      "uuid": "ada72f8f-1643-e5c6-94db-f2a5636f1a64"
    },
    "cert_expiry": 1534534392,
    "ext_ip": "73.92.124.103",
    "fwupdate": {
      "progress": 10,
      "status": "inprogress",
      "status_id": 5,
      "timestamp": 1428949501
    },
    "iot_stat": {
      "DI2": {
        "value": 0
      }
    },
    "ip": "10.2.9.159",
    "ip_config": {
      "dns": [
        "8.8.8.8",
        "4.4.4.4"
      ],
      "dns_suffix": [
        ".mist.local",
        ".mist.com"
      ],
      "gateway": "10.2.1.254",
      "ip": "10.2.1.1",
      "netmask": "255.255.255.0",
      "type": "static"
    },
    "ip_stat": {
      "dns": [
        "8.8.8.8",
        "4.4.4.4"
      ],
      "dns_suffix": [
        ".mist.local",
        ".mist.com"
      ],
      "gateway": "10.2.1.254",
      "gateway6": "2607:f8b0:4005:808::1",
      "ip": "10.2.1.1",
      "ip6": "2607:f8b0:4005:808::2004",
      "ips": {
        "vlan1": "10.2.1.1/24,2607:f8b0:4005:808::1/32",
        "vlan193": "10.73.1.31/16",
        "vlan3157": "10.72.11.14/24"
      },
      "netmask": "255.255.255.0",
      "netmask6": "/32"
    },
    "l2tp_stat": {
      "7dae216d-7c98-a51b-e068-dd7d477b7216": {
        "sessions": [
          {
            "local_sid": 31,
            "remote_id": "vpn1",
            "remote_sid": 13,
            "state": "established"
          }
        ],
        "state": "established_with_sessions",
        "uptime": 135,
        "wxtunnel_id": "7dae216d-7c98-a51b-e068-dd7d477b7216"
      }
    },
    "last_seen": 1470417522,
    "last_trouble": {
      "code": "03",
      "timestamp": 1428949501
    },
    "led": {
      "brightness": 255,
      "enabled": true
    },
    "lldp_stat": {
      "chassis_id": "63:68:61:73:73:69",
      "lldp_med_supported": false,
      "mgmt_addr": "10.1.5.2",
      "port_desc": "2/26",
      "power_allocated": 15500,
      "power_draw": 15000,
      "power_request_count": 3,
      "power_requested": 25500,
      "system_desc": "HP J9729A 2920-48G-POE+ Switch",
      "system_name": "TC2-OWL-Stack-01"
    },
    "locating": false,
    "mac": "5c5b35000010",
    "map_id": "63eda950-c6da-11e4-a628-60f81dd250cc",
    "mesh_downlinks": {
      "00000000-0000-0000-1000-5c5b356be59f": {
        "band": "24",
        "channel": 7,
        "idle_time": 3,
        "last_seen": 1470417522,
        "proto": "a",
        "rssi": -65,
        "rx_bps": 12,
        "rx_bytes": 217416,
        "rx_packets": 2337,
        "rx_rate": 65,
        "rx_retries": 5,
        "snr": 31,
        "tx_bps": 6,
        "tx_bytes": 175132,
        "tx_packets": 1566,
        "tx_rate": 65,
        "tx_retries": 500
      }
    },
    "mesh_uplink": {
      "band": "24",
      "channel": 7,
      "idle_time": 3,
      "last_seen": 1470417522,
      "proto": "a",
      "rssi": -65,
      "rx_bps": 12,
      "rx_bytes": 217416,
      "rx_packets": 2337,
      "rx_rate": 65,
      "rx_retries": 5,
      "snr": 31,
      "tx_bps": 6,
      "tx_bytes": 175132,
      "tx_packets": 1566,
      "tx_rate": 65,
      "tx_retries": 500,
      "uplink_ap_id": "00000000-0000-0000-1000-5c5b35000010"
    },
    "model": "AP200",
    "name": "conference room",
    "num_clients": 10,
    "port_stat": {
      "eth0": {
        "full_duplex": true,
        "rx_bytes": 2056,
        "rx_errors": 0,
        "rx_pkts": 670,
        "speed": 1000,
        "tx_bytes": 2056,
        "tx_pkts": 670,
        "up": true
      },
      "eth1": {
        "up": false
      },
      "module": {
        "up": false
      }
    },
    "power_budget": -12000,
    "power_src": "PoE 802.3af",
    "radio_config": {
      "band_24": {
        "bandwidth": 20,
        "channel": 0,
        "dynamic_chaining_enabled": false,
        "power": 0,
        "rx_chain": 4,
        "tx_chain": 4
      },
      "band_5": {
        "bandwidth": 40,
        "channel": 0,
        "dynamic_chaining_enabled": false,
        "power": 0,
        "rx_chain": 4,
        "tx_chain": 1
      },
      "scanning_enabled": true
    },
    "radio_stat": {
      "band_24": {
        "bandwidth": 20,
        "channel": 6,
        "mac": "5c5b350004a0",
        "num_clients": 6,
        "power": 19,
        "rx_bytes": 8504737800,
        "rx_pkts": 57731964,
        "tx_bytes": 211166512114,
        "tx_pkts": 812058566
      },
      "band_5": {
        "bandwidth": 80,
        "channel": 44,
        "mac": "5c5b350004b0",
        "num_clients": 4,
        "power": 15,
        "rx_bytes": 10366616,
        "rx_pkts": 38603,
        "tx_bytes": 50877568,
        "tx_pkts": 145496
      }
    },
    "rx_bps": 60003,
    "rx_bytes": 8515104416,
    "rx_pkts": 57770567,
    "serial": "FXLH2015170017",
    "status": "connected",
    "tx_bps": 634301,
    "tx_bytes": 211217389682,
    "tx_pkts": 812204062,
    "type": "ap",
    "uptime": 13500,
    "usb_stat": {
      "channel": 3,
      "connected": true,
      "last_activity": 1586873254,
      "type": "imagotag",
      "up": true
    },
    "version": "1.0.0",
    "x": 53.5,
    "y": 173.1
  }
]
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesStatsDevices401ErrorException`](../../doc/models/api-v1-sites-stats-devices-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesStatsDevices403ErrorException`](../../doc/models/api-v1-sites-stats-devices-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesStatsDevices404ErrorException`](../../doc/models/api-v1-sites-stats-devices-404-error-exception.md) |


# Get Site Device Stats

Get Site Device Stats Details

```python
def get_site_device_stats(self,
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

result = sites_devices_stats_controller.get_site_device_stats(
    site_id,
    device_id
)
print(result)
```

## Example Response

```
{
  "ble_config": {
    "beacon_rate": 3,
    "beacon_rate_model": "custom",
    "beam_disabled": [
      1,
      3,
      6
    ],
    "power": 10,
    "power_mode": "custom"
  },
  "ble_stat": {
    "beacon_rate": 3,
    "eddystone_uid_enabled": false,
    "eddystone_uid_freq_msec": 200,
    "eddystone_uid_instance": "5c5b35000001",
    "eddystone_uid_namespace": "2818e3868dec25629ede",
    "eddystone_url_enabled": true,
    "eddystone_url_freq_msec": 100,
    "eddystone_url_url": "https://www.abc.com",
    "ibeacon_enabled": true,
    "ibeacon_major": 13,
    "ibeacon_minor": 138,
    "ibeacon_uuid": "f3f17139-704a-f03a-2786-0400279e37c3",
    "major": 12345,
    "minors": [
      201,
      202,
      203,
      204,
      205,
      206,
      207,
      208
    ],
    "power": 10,
    "rx_bytes": 135,
    "rx_pkts": 135,
    "tx_bytes": 5231513353,
    "tx_pkts": 135135135,
    "tx_resets": 0,
    "uuid": "ada72f8f-1643-e5c6-94db-f2a5636f1a64"
  },
  "cert_expiry": 1534534392,
  "ext_ip": "73.92.124.103",
  "fwupdate": {
    "progress": 10,
    "status": "inprogress",
    "status_id": 5,
    "timestamp": 1428949501
  },
  "iot_stat": {
    "DI2": {
      "value": 0
    }
  },
  "ip": "10.2.9.159",
  "ip_config": {
    "dns": [
      "8.8.8.8",
      "4.4.4.4"
    ],
    "dns_suffix": [
      ".mist.local",
      ".mist.com"
    ],
    "gateway": "10.2.1.254",
    "ip": "10.2.1.1",
    "netmask": "255.255.255.0",
    "type": "static"
  },
  "ip_stat": {
    "dns": [
      "8.8.8.8",
      "4.4.4.4"
    ],
    "dns_suffix": [
      ".mist.local",
      ".mist.com"
    ],
    "gateway": "10.2.1.254",
    "gateway6": "2607:f8b0:4005:808::1",
    "ip": "10.2.1.1",
    "ip6": "2607:f8b0:4005:808::2004",
    "ips": {
      "vlan1": "10.2.1.1/24,2607:f8b0:4005:808::1/32",
      "vlan193": "10.73.1.31/16",
      "vlan3157": "10.72.11.14/24"
    },
    "netmask": "255.255.255.0",
    "netmask6": "/32"
  },
  "l2tp_stat": {
    "7dae216d-7c98-a51b-e068-dd7d477b7216": {
      "sessions": [
        {
          "local_sid": 31,
          "remote_id": "vpn1",
          "remote_sid": 13,
          "state": "established"
        }
      ],
      "state": "established_with_sessions",
      "uptime": 135,
      "wxtunnel_id": "7dae216d-7c98-a51b-e068-dd7d477b7216"
    }
  },
  "last_seen": 1470417522,
  "last_trouble": {
    "code": "03",
    "timestamp": 1428949501
  },
  "led": {
    "brightness": 255,
    "enabled": true
  },
  "lldp_stat": {
    "chassis_id": "63:68:61:73:73:69",
    "lldp_med_supported": false,
    "mgmt_addr": "10.1.5.2",
    "port_desc": "2/26",
    "power_allocated": 15500,
    "power_draw": 15000,
    "power_request_count": 3,
    "power_requested": 25500,
    "system_desc": "HP J9729A 2920-48G-POE+ Switch",
    "system_name": "TC2-OWL-Stack-01"
  },
  "locating": false,
  "mac": "5c5b35000010",
  "map_id": "63eda950-c6da-11e4-a628-60f81dd250cc",
  "mesh_downlinks": {
    "00000000-0000-0000-1000-5c5b356be59f": {
      "band": "24",
      "channel": 7,
      "idle_time": 3,
      "last_seen": 1470417522,
      "proto": "a",
      "rssi": -65,
      "rx_bps": 12,
      "rx_bytes": 217416,
      "rx_packets": 2337,
      "rx_rate": 65,
      "rx_retries": 5,
      "snr": 31,
      "tx_bps": 6,
      "tx_bytes": 175132,
      "tx_packets": 1566,
      "tx_rate": 65,
      "tx_retries": 500
    }
  },
  "mesh_uplink": {
    "band": "24",
    "channel": 7,
    "idle_time": 3,
    "last_seen": 1470417522,
    "proto": "a",
    "rssi": -65,
    "rx_bps": 12,
    "rx_bytes": 217416,
    "rx_packets": 2337,
    "rx_rate": 65,
    "rx_retries": 5,
    "snr": 31,
    "tx_bps": 6,
    "tx_bytes": 175132,
    "tx_packets": 1566,
    "tx_rate": 65,
    "tx_retries": 500,
    "uplink_ap_id": "00000000-0000-0000-1000-5c5b35000010"
  },
  "model": "AP200",
  "name": "conference room",
  "num_clients": 10,
  "port_stat": {
    "eth0": {
      "full_duplex": true,
      "rx_bytes": 2056,
      "rx_errors": 0,
      "rx_pkts": 670,
      "speed": 1000,
      "tx_bytes": 2056,
      "tx_pkts": 670,
      "up": true
    },
    "eth1": {
      "up": false
    },
    "module": {
      "up": false
    }
  },
  "power_budget": -12000,
  "power_src": "PoE 802.3af",
  "radio_config": {
    "band_24": {
      "bandwidth": 20,
      "channel": 0,
      "dynamic_chaining_enabled": false,
      "power": 0,
      "rx_chain": 4,
      "tx_chain": 4
    },
    "band_5": {
      "bandwidth": 40,
      "channel": 0,
      "dynamic_chaining_enabled": false,
      "power": 0,
      "rx_chain": 4,
      "tx_chain": 1
    },
    "scanning_enabled": true
  },
  "radio_stat": {
    "band_24": {
      "bandwidth": 20,
      "channel": 6,
      "mac": "5c5b350004a0",
      "num_clients": 6,
      "power": 19,
      "rx_bytes": 8504737800,
      "rx_pkts": 57731964,
      "tx_bytes": 211166512114,
      "tx_pkts": 812058566
    },
    "band_5": {
      "bandwidth": 80,
      "channel": 44,
      "mac": "5c5b350004b0",
      "num_clients": 4,
      "power": 15,
      "rx_bytes": 10366616,
      "rx_pkts": 38603,
      "tx_bytes": 50877568,
      "tx_pkts": 145496
    }
  },
  "rx_bps": 60003,
  "rx_bytes": 8515104416,
  "rx_pkts": 57770567,
  "serial": "FXLH2015170017",
  "status": "connected",
  "tx_bps": 634301,
  "tx_bytes": 211217389682,
  "tx_pkts": 812204062,
  "type": "ap",
  "uptime": 13500,
  "usb_stat": {
    "channel": 3,
    "connected": true,
    "last_activity": 1586873254,
    "type": "imagotag",
    "up": true
  },
  "version": "1.0.0",
  "x": 53.5,
  "y": 173.1
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesStatsDevices401ErrorException`](../../doc/models/api-v1-sites-stats-devices-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesStatsDevices403ErrorException`](../../doc/models/api-v1-sites-stats-devices-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesStatsDevices404ErrorException`](../../doc/models/api-v1-sites-stats-devices-404-error-exception.md) |


# Get Site All Clients Stats by Device

Get wireless client stat by Device

```python
def get_site_all_clients_stats_by_device(self,
                                        site_id,
                                        device_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `device_id` | `uuid\|string` | Template, Required | - |

## Response Type

[`List of StatsClient`](../../doc/models/stats-client.md)

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

device_id = '000000ab-00ab-00ab-00ab-0000000000ab'

result = sites_devices_stats_controller.get_site_all_clients_stats_by_device(
    site_id,
    device_id
)
print(result)
```

## Example Response *(as JSON)*

```json
[
  {
    "_ttl": 0,
    "accuracy": 0,
    "airespace_ifname": "string",
    "airwatch": {
      "authorized": true
    },
    "ap_id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
    "ap_mac": "string",
    "band": "24",
    "channel": 0,
    "dual_band": true,
    "family": "string",
    "guest": {
      "authorized": true,
      "authorized_expiring_time": 0,
      "authorized_time": 0,
      "company": "string",
      "email": "string",
      "field1": "string",
      "name": "string"
    },
    "hostname": "string",
    "id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
    "idle_time": 0,
    "ip": "192.168.1.2",
    "is_guest": true,
    "key_mgmt": "string",
    "last_seen": 0,
    "mac": "string",
    "manufacture": "string",
    "map_id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
    "model": "string",
    "name": "string",
    "num_locating_aps": 0,
    "os": "string",
    "power_saving": true,
    "proto": "ac",
    "psk_id": "6f4bf402-45f9-2a56-6c8b-7f83d3bc98e9",
    "rssi": 0,
    "rx_bps": 0,
    "rx_bytes": 0,
    "rx_packets": 0,
    "rx_rate": 0,
    "rx_retries": 0,
    "snr": 0,
    "ssid": "string",
    "tx_bps": 0,
    "tx_bytes": 0,
    "tx_packets": 0,
    "tx_rate": 0,
    "tx_retries": 0,
    "type": "string",
    "uptime": 0,
    "username": "string",
    "vlan_id": 1,
    "wlan_id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
    "x": 0,
    "y": 0
  }
]
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesStatsDevicesClients401ErrorException`](../../doc/models/api-v1-sites-stats-devices-clients-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesStatsDevicesClients403ErrorException`](../../doc/models/api-v1-sites-stats-devices-clients-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesStatsDevicesClients404ErrorException`](../../doc/models/api-v1-sites-stats-devices-clients-404-error-exception.md) |


# List Site Mx Edges Stats

Get List of Site MxEdges Stats

```python
def list_site_mx_edges_stats(self,
                            site_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |

## Response Type

[`List of StatsMxedge`](../../doc/models/stats-mxedge.md)

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

result = sites_devices_stats_controller.list_site_mx_edges_stats(site_id)
print(result)
```

## Example Response *(as JSON)*

```json
[
  {
    "cpu_stat": {
      "cpus": {
        "property1": {
          "idle": 0,
          "interrupt": 0,
          "system": 0,
          "usage": 0,
          "user": 0
        },
        "property2": {
          "idle": 0,
          "interrupt": 0,
          "system": 0,
          "usage": 0,
          "user": 0
        }
      },
      "idle": 0,
      "interrupt": 0,
      "system": 0,
      "usage": 0,
      "user": 0
    },
    "created_time": 0,
    "for_site": true,
    "id": "493f6eca-6276-4993-bfeb-83cbbbba6f08",
    "ip_stat": {
      "ip": "string",
      "ips": {
        "property1": "string",
        "property2": "string"
      }
    },
    "lag_stat": {},
    "last_seen": 0,
    "mac": "string",
    "memory_stat": {
      "active": 0,
      "available": 0,
      "buffers": 0,
      "cached": 0,
      "free": 0,
      "inactive": 0,
      "swap_cached": 0,
      "swap_free": 0,
      "swap_total": 0,
      "total": 0,
      "usage": 0
    },
    "model": "string",
    "modified_time": 0,
    "mxagent_registered": true,
    "mxcluster_id": "de779d5f-583c-4a9c-b212-6105ad1a78b6",
    "name": "string",
    "num_tunnels": 0,
    "org_id": "a40f5d1f-d889-42e9-94ea-b9b33585fc6b",
    "port_stat": {
      "property1": {
        "full_duplex": true,
        "mac": "string",
        "rx_bytes": 0,
        "rx_errors": 0,
        "rx_pkts": 0,
        "speed": 0,
        "state": "string",
        "tx_bytes": 0,
        "tx_errors": 0,
        "tx_pkts": 0,
        "up": true
      },
      "property2": {
        "full_duplex": true,
        "mac": "string",
        "rx_bytes": 0,
        "rx_errors": 0,
        "rx_pkts": 0,
        "speed": 0,
        "state": "string",
        "tx_bytes": 0,
        "tx_errors": 0,
        "tx_pkts": 0,
        "up": true
      }
    },
    "sensor_stat": {},
    "service_stat": {
      "mxagent": {
        "ext_ip": "string",
        "last_seen": 0,
        "package_state": "string",
        "package_version": "string",
        "running_state": "string",
        "uptime": 0
      },
      "tunterm": {
        "ext_ip": "string",
        "last_seen": 0,
        "package_state": "string",
        "package_version": "string",
        "running_state": "string",
        "uptime": 0
      }
    },
    "services": [
      {}
    ],
    "site_id": "72771e6a-6f5e-4de4-a5b9-1266c4197811",
    "status": "string",
    "tunterm_id": "811edbcf-b497-4977-b6d1-40d54cf871a5",
    "tunterm_ip_config": {
      "gateway": "string",
      "ip": "string",
      "netmask": "string"
    },
    "tunterm_port_config": {
      "downstream_ports": [
        {}
      ],
      "separate_upstream_downstream": true,
      "upstream_ports": [
        {}
      ]
    },
    "tunterm_registered": true,
    "tunterm_stat": {
      "monitoring_failed": true
    },
    "uptime": 0,
    "virtualization_type": "string"
  }
]
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesStatsMxedges401ErrorException`](../../doc/models/api-v1-sites-stats-mxedges-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesStatsMxedges403ErrorException`](../../doc/models/api-v1-sites-stats-mxedges-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesStatsMxedges404ErrorException`](../../doc/models/api-v1-sites-stats-mxedges-404-error-exception.md) |


# Get Site Mx Edge Stats

Get One Site MxEdge Stats

```python
def get_site_mx_edge_stats(self,
                          site_id,
                          mxedge_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `mxedge_id` | `uuid\|string` | Template, Required | - |

## Response Type

[`StatsMxedge`](../../doc/models/stats-mxedge.md)

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

mxedge_id = '000000ab-00ab-00ab-00ab-0000000000ab'

result = sites_devices_stats_controller.get_site_mx_edge_stats(
    site_id,
    mxedge_id
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "cpu_stat": {
    "cpus": {
      "property1": {
        "idle": 0,
        "interrupt": 0,
        "system": 0,
        "usage": 0,
        "user": 0
      },
      "property2": {
        "idle": 0,
        "interrupt": 0,
        "system": 0,
        "usage": 0,
        "user": 0
      }
    },
    "idle": 0,
    "interrupt": 0,
    "system": 0,
    "usage": 0,
    "user": 0
  },
  "created_time": 0,
  "for_site": true,
  "id": "492f6eca-6276-4993-bfeb-93cbbbba6f08",
  "ip_stat": {
    "ip": "string",
    "ips": {
      "property1": "string",
      "property2": "string"
    }
  },
  "lag_stat": {},
  "last_seen": 0,
  "mac": "string",
  "memory_stat": {
    "active": 0,
    "available": 0,
    "buffers": 0,
    "cached": 0,
    "free": 0,
    "inactive": 0,
    "swap_cached": 0,
    "swap_free": 0,
    "swap_total": 0,
    "total": 0,
    "usage": 0
  },
  "model": "string",
  "modified_time": 0,
  "mxagent_registered": true,
  "mxcluster_id": "de779d5f-583c-4a9c-b212-6105ad1a78b6",
  "name": "string",
  "num_tunnels": 0,
  "org_id": "a40f5d1f-d889-42e9-94ea-b9b33585fc6b",
  "port_stat": {
    "property1": {
      "full_duplex": true,
      "mac": "string",
      "rx_bytes": 0,
      "rx_errors": 0,
      "rx_pkts": 0,
      "speed": 0,
      "state": "string",
      "tx_bytes": 0,
      "tx_errors": 0,
      "tx_pkts": 0,
      "up": true
    },
    "property2": {
      "full_duplex": true,
      "mac": "string",
      "rx_bytes": 0,
      "rx_errors": 0,
      "rx_pkts": 0,
      "speed": 0,
      "state": "string",
      "tx_bytes": 0,
      "tx_errors": 0,
      "tx_pkts": 0,
      "up": true
    }
  },
  "sensor_stat": {},
  "service_stat": {
    "mxagent": {
      "ext_ip": "string",
      "last_seen": 0,
      "package_state": "string",
      "package_version": "string",
      "running_state": "string",
      "uptime": 0
    },
    "tunterm": {
      "ext_ip": "string",
      "last_seen": 0,
      "package_state": "string",
      "package_version": "string",
      "running_state": "string",
      "uptime": 0
    }
  },
  "services": [
    {}
  ],
  "site_id": "72771e6a-6f5e-4de4-a5b9-1266c4197811",
  "status": "string",
  "tunterm_id": "811edbcf-b497-4977-b6d1-40d54cf871a5",
  "tunterm_ip_config": {
    "gateway": "string",
    "ip": "string",
    "netmask": "string"
  },
  "tunterm_port_config": {
    "downstream_ports": [
      {}
    ],
    "separate_upstream_downstream": true,
    "upstream_ports": [
      {}
    ]
  },
  "tunterm_registered": true,
  "tunterm_stat": {
    "monitoring_failed": true
  },
  "uptime": 0,
  "virtualization_type": "string"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesStatsMxedges401ErrorException`](../../doc/models/api-v1-sites-stats-mxedges-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesStatsMxedges403ErrorException`](../../doc/models/api-v1-sites-stats-mxedges-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesStatsMxedges404ErrorException`](../../doc/models/api-v1-sites-stats-mxedges-404-error-exception.md) |


# Count Site Sw or Gw Ports

Count by Distinct Attributes of Switch/Gateway Ports

```python
def count_site_sw_or_gw_ports(self,
                             site_id,
                             distinct='mac',
                             full_duplex=None,
                             mac=None,
                             neighbor_mac=None,
                             neighbor_port_desc=None,
                             neighbor_system_name=None,
                             poe_disabled=None,
                             poe_mode=None,
                             poe_on=None,
                             port_id=None,
                             port_mac=None,
                             power_draw=None,
                             tx_pkts=None,
                             rx_pkts=None,
                             rx_bytes=None,
                             tx_bps=None,
                             rx_bps=None,
                             tx_mcast_pkts=None,
                             tx_bcast_pkts=None,
                             rx_mcast_pkts=None,
                             rx_bcast_pkts=None,
                             speed=None,
                             stp_state=None,
                             stp_role=None,
                             auth_state=None,
                             up=None,
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
| `distinct` | [`Distinct19Enum`](../../doc/models/distinct-19-enum.md) | Query, Optional | port_id, port_mac, full_duplex, mac, neighbor_macneighbor_port_desc, neighbor_system_name, poe_disabled, poe_mode, poe_on, speed, up<br>**Default**: `'mac'` |
| `full_duplex` | `bool` | Query, Optional | indicates full or half duplex |
| `mac` | `string` | Query, Optional | device identifier |
| `neighbor_mac` | `string` | Query, Optional | Chassis identifier of the chassis type listed |
| `neighbor_port_desc` | `string` | Query, Optional | Description supplied by the system on the interface E.g. “GigabitEthernet2/0/39” |
| `neighbor_system_name` | `string` | Query, Optional | Name supplied by the system on the interface E.g. neighbor system name E.g. “Kumar-Acc-SW.mist.local” |
| `poe_disabled` | `bool` | Query, Optional | is the POE configured not be disabled. |
| `poe_mode` | `string` | Query, Optional | poe mode depending on class E.g. “802.3at” |
| `poe_on` | `bool` | Query, Optional | is the device attached to POE |
| `port_id` | `string` | Query, Optional | interface name |
| `port_mac` | `string` | Query, Optional | interface mac address |
| `power_draw` | `float` | Query, Optional | Amount of power being used by the interface at the time the command is executed. Unit in watts. |
| `tx_pkts` | `int` | Query, Optional | Output packets |
| `rx_pkts` | `int` | Query, Optional | Input packets |
| `rx_bytes` | `int` | Query, Optional | Input bytes |
| `tx_bps` | `int` | Query, Optional | Output rate |
| `rx_bps` | `int` | Query, Optional | Input rate |
| `tx_mcast_pkts` | `int` | Query, Optional | Multicast output packets |
| `tx_bcast_pkts` | `int` | Query, Optional | Broadcast output packets |
| `rx_mcast_pkts` | `int` | Query, Optional | Multicast input packets |
| `rx_bcast_pkts` | `int` | Query, Optional | Broadcast input packets |
| `speed` | `int` | Query, Optional | port speed |
| `stp_state` | [`StpStateEnum`](../../doc/models/stp-state-enum.md) | Query, Optional | if `up`==`true` |
| `stp_role` | [`StpRoleEnum`](../../doc/models/stp-role-enum.md) | Query, Optional | if `up`==`true` |
| `auth_state` | [`AuthStateEnum`](../../doc/models/auth-state-enum.md) | Query, Optional | if `up`==`true` && has Authenticator role |
| `up` | `bool` | Query, Optional | indicates if interface is up |
| `page` | `int` | Query, Optional | **Default**: `1`<br>**Constraints**: `>= 1` |
| `limit` | `int` | Query, Optional | **Default**: `100`<br>**Constraints**: `>= 0` |
| `start` | `int` | Query, Optional | **Default**: `0`<br>**Constraints**: `>= 0` |
| `end` | `int` | Query, Optional | **Default**: `0`<br>**Constraints**: `>= 0` |
| `duration` | `string` | Query, Optional | For historical stats and/or logs where time range is needed, you can specify the time range in a few different ways:<br><br>* ?start=1430000000&end=1430864000	specify the start / end<br>* ?end=1430864000&duration=1d	specify end time and duration<br>* ?duration=1d	specify duration, end will be now() in seconds<br>**Default**: `'1d'` |

## Response Type

[`ApiV1SitesStatsPortsCountResponse`](../../doc/models/api-v1-sites-stats-ports-count-response.md)

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

distinct = Distinct19Enum.MAC

page = 1

limit = 100

start = 0

end = 0

duration = '10m'

result = sites_devices_stats_controller.count_site_sw_or_gw_ports(
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
  "distinct": "mac",
  "end": 1513177200,
  "limit": 100,
  "results": [
    {
      "count": 217,
      "mac": "112233445566"
    },
    {
      "count": 35,
      "mac": "001122334455"
    }
  ],
  "start": 1511967600,
  "total": 20
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesStatsPortsCount401ErrorException`](../../doc/models/api-v1-sites-stats-ports-count-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesStatsPortsCount403ErrorException`](../../doc/models/api-v1-sites-stats-ports-count-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesStatsPortsCount404ErrorException`](../../doc/models/api-v1-sites-stats-ports-count-404-error-exception.md) |


# Search Site Sw or Gw Ports

Search Switch / Gateway Ports

```python
def search_site_sw_or_gw_ports(self,
                              site_id,
                              full_duplex=None,
                              mac=None,
                              mtype=None,
                              neighbor_mac=None,
                              neighbor_port_desc=None,
                              neighbor_system_name=None,
                              poe_disabled=None,
                              poe_mode=None,
                              poe_on=None,
                              port_id=None,
                              port_mac=None,
                              power_draw=None,
                              tx_pkts=None,
                              rx_pkts=None,
                              rx_bytes=None,
                              tx_bps=None,
                              rx_bps=None,
                              tx_errors=None,
                              rx_errors=None,
                              tx_mcast_pkts=None,
                              tx_bcast_pkts=None,
                              rx_mcast_pkts=None,
                              rx_bcast_pkts=None,
                              speed=None,
                              mac_limit=None,
                              mac_count=None,
                              up=None,
                              active=None,
                              jitter=None,
                              loss=None,
                              latency=None,
                              stp_state=None,
                              stp_role=None,
                              xcvr_part_number=None,
                              auth_state=None,
                              lte_imsi=None,
                              lte_iccid=None,
                              lte_imei=None,
                              limit=100,
                              start=0,
                              end=0,
                              duration='1d')
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `full_duplex` | `bool` | Query, Optional | indicates full or half duplex |
| `mac` | `string` | Query, Optional | device identifier |
| `mtype` | [`Type63Enum`](../../doc/models/type-63-enum.md) | Query, Optional | device type |
| `neighbor_mac` | `string` | Query, Optional | Chassis identifier of the chassis type listed |
| `neighbor_port_desc` | `string` | Query, Optional | Description supplied by the system on the interface E.g. “GigabitEthernet2/0/39” |
| `neighbor_system_name` | `string` | Query, Optional | Name supplied by the system on the interface E.g. neighbor system name E.g. “Kumar-Acc-SW.mist.local” |
| `poe_disabled` | `bool` | Query, Optional | is the POE configured not be disabled. |
| `poe_mode` | `string` | Query, Optional | poe mode depending on class E.g. “802.3at” |
| `poe_on` | `bool` | Query, Optional | is the device attached to POE |
| `port_id` | `string` | Query, Optional | interface name |
| `port_mac` | `string` | Query, Optional | interface mac address |
| `power_draw` | `float` | Query, Optional | Amount of power being used by the interface at the time the command is executed. Unit in watts. |
| `tx_pkts` | `int` | Query, Optional | Output packets |
| `rx_pkts` | `int` | Query, Optional | Input packets |
| `rx_bytes` | `int` | Query, Optional | Input bytes |
| `tx_bps` | `int` | Query, Optional | Output rate |
| `rx_bps` | `int` | Query, Optional | Input rate |
| `tx_errors` | `int` | Query, Optional | Output errors |
| `rx_errors` | `int` | Query, Optional | Input errors |
| `tx_mcast_pkts` | `int` | Query, Optional | Multicast output packets |
| `tx_bcast_pkts` | `int` | Query, Optional | Broadcast output packets |
| `rx_mcast_pkts` | `int` | Query, Optional | Multicast input packets |
| `rx_bcast_pkts` | `int` | Query, Optional | Broadcast input packets |
| `speed` | `int` | Query, Optional | port speed |
| `mac_limit` | `int` | Query, Optional | Limit on number of dynamically learned macs |
| `mac_count` | `int` | Query, Optional | Number of mac addresses in the forwarding table |
| `up` | `bool` | Query, Optional | indicates if interface is up |
| `active` | `bool` | Query, Optional | indicates if interface is active/inactive |
| `jitter` | `float` | Query, Optional | Last sampled jitter of the interface |
| `loss` | `float` | Query, Optional | Last sampled loss of the interface |
| `latency` | `float` | Query, Optional | Last sampled latency of the interface |
| `stp_state` | [`StpStateEnum`](../../doc/models/stp-state-enum.md) | Query, Optional | if `up`==`true` |
| `stp_role` | [`StpRoleEnum`](../../doc/models/stp-role-enum.md) | Query, Optional | if `up`==`true` |
| `xcvr_part_number` | `string` | Query, Optional | Optic Slot Partnumber, Check for null/empty |
| `auth_state` | [`AuthStateEnum`](../../doc/models/auth-state-enum.md) | Query, Optional | if `up`==`true` && has Authenticator role |
| `lte_imsi` | `string` | Query, Optional | LTE IMSI value, Check for null/empty |
| `lte_iccid` | `string` | Query, Optional | LTE ICCID value, Check for null/empty |
| `lte_imei` | `string` | Query, Optional | LTE IMEI value, Check for null/empty |
| `limit` | `int` | Query, Optional | **Default**: `100`<br>**Constraints**: `>= 0` |
| `start` | `int` | Query, Optional | **Default**: `0`<br>**Constraints**: `>= 0` |
| `end` | `int` | Query, Optional | **Default**: `0`<br>**Constraints**: `>= 0` |
| `duration` | `string` | Query, Optional | For historical stats and/or logs where time range is needed, you can specify the time range in a few different ways:<br><br>* ?start=1430000000&end=1430864000	specify the start / end<br>* ?end=1430864000&duration=1d	specify end time and duration<br>* ?duration=1d	specify duration, end will be now() in seconds<br>**Default**: `'1d'` |

## Response Type

[`ApiV1SitesStatsPortsSearchResponse`](../../doc/models/api-v1-sites-stats-ports-search-response.md)

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

limit = 100

start = 0

end = 0

duration = '10m'

result = sites_devices_stats_controller.search_site_sw_or_gw_ports(
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
  "end": 1513177200,
  "limit": 10,
  "results": [
    {
      "mac": "5c4527a96580",
      "neighbor_mac": "64d814353400",
      "neighbor_port_desc": "GigabitEthernet1/0/21",
      "neighbor_system_name": "CORP-D-SW-2",
      "org_id": "c168ddee-c14c-11e5-8e81-1258369c38a9",
      "poe_disabled": true,
      "port_id": "me0",
      "port_mac": "5c4527a96580",
      "rx_bytes": 4563443626,
      "rx_pkts": 30360265,
      "site_id": "c1698122-c14c-11e5-8e81-1258369c38a9",
      "speed": 1000,
      "tx_bytes": 11299516780,
      "tx_pkts": 14610886,
      "up": true
    },
    {
      "full_duplex": true,
      "mac": "0c8126c6ff6c",
      "neighbor_mac": "5c5b350eb361",
      "neighbor_port_desc": "ETH0",
      "neighbor_system_name": "kevinsap",
      "org_id": "c168ddee-c14c-11e5-8e81-1258369c38a9",
      "poe_mode": "802.3at",
      "poe_on": true,
      "port_id": "ge-0/0/0",
      "port_mac": "0c8126c6ff6f",
      "power_draw": 5.4,
      "rx_bps": 1176,
      "rx_bytes": 2628451,
      "rx_pkts": 11829,
      "site_id": "c1698122-c14c-11e5-8e81-1258369c38a9",
      "speed": 1000,
      "tx_bps": 14264,
      "tx_bytes": 96810192,
      "tx_pkts": 492176,
      "up": true
    }
  ],
  "start": 1511967600,
  "total": 100
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesStatsPortsSearch401ErrorException`](../../doc/models/api-v1-sites-stats-ports-search-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesStatsPortsSearch403ErrorException`](../../doc/models/api-v1-sites-stats-ports-search-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesStatsPortsSearch404ErrorException`](../../doc/models/api-v1-sites-stats-ports-search-404-error-exception.md) |


# Count Site Switch Ports

Count by Distinct Attributes of Switch/Gateway Ports

```python
def count_site_switch_ports(self,
                           site_id,
                           distinct='mac',
                           full_duplex=None,
                           mac=None,
                           neighbor_mac=None,
                           neighbor_port_desc=None,
                           neighbor_system_name=None,
                           poe_disabled=None,
                           poe_mode=None,
                           poe_on=None,
                           port_id=None,
                           port_mac=None,
                           power_draw=None,
                           tx_pkts=None,
                           rx_pkts=None,
                           rx_bytes=None,
                           tx_bps=None,
                           rx_bps=None,
                           tx_mcast_pkts=None,
                           tx_bcast_pkts=None,
                           rx_mcast_pkts=None,
                           rx_bcast_pkts=None,
                           speed=None,
                           stp_state=None,
                           stp_role=None,
                           auth_state=None,
                           up=None,
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
| `distinct` | [`Distinct19Enum`](../../doc/models/distinct-19-enum.md) | Query, Optional | port_id, port_mac, full_duplex, mac, neighbor_macneighbor_port_desc, neighbor_system_name, poe_disabled, poe_mode, poe_on, speed, up<br>**Default**: `'mac'` |
| `full_duplex` | `bool` | Query, Optional | indicates full or half duplex |
| `mac` | `string` | Query, Optional | device identifier |
| `neighbor_mac` | `string` | Query, Optional | Chassis identifier of the chassis type listed |
| `neighbor_port_desc` | `string` | Query, Optional | Description supplied by the system on the interface E.g. “GigabitEthernet2/0/39” |
| `neighbor_system_name` | `string` | Query, Optional | Name supplied by the system on the interface E.g. neighbor system name E.g. “Kumar-Acc-SW.mist.local” |
| `poe_disabled` | `bool` | Query, Optional | is the POE configured not be disabled. |
| `poe_mode` | `string` | Query, Optional | poe mode depending on class E.g. “802.3at” |
| `poe_on` | `bool` | Query, Optional | is the device attached to POE |
| `port_id` | `string` | Query, Optional | interface name |
| `port_mac` | `string` | Query, Optional | interface mac address |
| `power_draw` | `float` | Query, Optional | Amount of power being used by the interface at the time the command is executed. Unit in watts. |
| `tx_pkts` | `int` | Query, Optional | Output packets |
| `rx_pkts` | `int` | Query, Optional | Input packets |
| `rx_bytes` | `int` | Query, Optional | Input bytes |
| `tx_bps` | `int` | Query, Optional | Output rate |
| `rx_bps` | `int` | Query, Optional | Input rate |
| `tx_mcast_pkts` | `int` | Query, Optional | Multicast output packets |
| `tx_bcast_pkts` | `int` | Query, Optional | Broadcast output packets |
| `rx_mcast_pkts` | `int` | Query, Optional | Multicast input packets |
| `rx_bcast_pkts` | `int` | Query, Optional | Broadcast input packets |
| `speed` | `int` | Query, Optional | port speed |
| `stp_state` | [`StpStateEnum`](../../doc/models/stp-state-enum.md) | Query, Optional | if `up`==`true` |
| `stp_role` | [`StpRoleEnum`](../../doc/models/stp-role-enum.md) | Query, Optional | if `up`==`true` |
| `auth_state` | [`AuthStateEnum`](../../doc/models/auth-state-enum.md) | Query, Optional | if `up`==`true` |
| `up` | `bool` | Query, Optional | indicates if interface is up |
| `page` | `int` | Query, Optional | **Default**: `1`<br>**Constraints**: `>= 1` |
| `limit` | `int` | Query, Optional | **Default**: `100`<br>**Constraints**: `>= 0` |
| `start` | `int` | Query, Optional | **Default**: `0`<br>**Constraints**: `>= 0` |
| `end` | `int` | Query, Optional | **Default**: `0`<br>**Constraints**: `>= 0` |
| `duration` | `string` | Query, Optional | For historical stats and/or logs where time range is needed, you can specify the time range in a few different ways:<br><br>* ?start=1430000000&end=1430864000	specify the start / end<br>* ?end=1430864000&duration=1d	specify end time and duration<br>* ?duration=1d	specify duration, end will be now() in seconds<br>**Default**: `'1d'` |

## Response Type

[`ApiV1SitesStatsSwitchPortsCountResponse`](../../doc/models/api-v1-sites-stats-switch-ports-count-response.md)

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

distinct = Distinct19Enum.MAC

page = 1

limit = 100

start = 0

end = 0

duration = '10m'

result = sites_devices_stats_controller.count_site_switch_ports(
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
  "distinct": "mac",
  "end": 1513177200,
  "limit": 100,
  "results": [
    {
      "count": 217,
      "mac": "112233445566"
    },
    {
      "count": 35,
      "mac": "001122334455"
    }
  ],
  "start": 1511967600,
  "total": 20
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesStatsSwitchPortsCount401ErrorException`](../../doc/models/api-v1-sites-stats-switch-ports-count-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesStatsSwitchPortsCount403ErrorException`](../../doc/models/api-v1-sites-stats-switch-ports-count-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesStatsSwitchPortsCount404ErrorException`](../../doc/models/api-v1-sites-stats-switch-ports-count-404-error-exception.md) |


# Search Site Switch Ports

Search Switch / Gateway Ports

```python
def search_site_switch_ports(self,
                            site_id,
                            full_duplex=None,
                            mac=None,
                            neighbor_mac=None,
                            neighbor_port_desc=None,
                            neighbor_system_name=None,
                            poe_disabled=None,
                            poe_mode=None,
                            poe_on=None,
                            port_id=None,
                            port_mac=None,
                            power_draw=None,
                            tx_pkts=None,
                            rx_pkts=None,
                            rx_bytes=None,
                            tx_bps=None,
                            rx_bps=None,
                            tx_mcast_pkts=None,
                            tx_bcast_pkts=None,
                            rx_mcast_pkts=None,
                            rx_bcast_pkts=None,
                            speed=None,
                            stp_state=None,
                            stp_role=None,
                            auth_state=None,
                            up=None,
                            limit=100,
                            start=0,
                            end=0,
                            duration='1d')
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `full_duplex` | `bool` | Query, Optional | indicates full or half duplex |
| `mac` | `string` | Query, Optional | device identifier |
| `neighbor_mac` | `string` | Query, Optional | Chassis identifier of the chassis type listed |
| `neighbor_port_desc` | `string` | Query, Optional | Description supplied by the system on the interface E.g. “GigabitEthernet2/0/39” |
| `neighbor_system_name` | `string` | Query, Optional | Name supplied by the system on the interface E.g. neighbor system name E.g. “Kumar-Acc-SW.mist.local” |
| `poe_disabled` | `bool` | Query, Optional | is the POE configured not be disabled. |
| `poe_mode` | `string` | Query, Optional | poe mode depending on class E.g. “802.3at” |
| `poe_on` | `bool` | Query, Optional | is the device attached to POE |
| `port_id` | `string` | Query, Optional | interface name |
| `port_mac` | `string` | Query, Optional | interface mac address |
| `power_draw` | `float` | Query, Optional | Amount of power being used by the interface at the time the command is executed. Unit in watts. |
| `tx_pkts` | `int` | Query, Optional | Output packets |
| `rx_pkts` | `int` | Query, Optional | Input packets |
| `rx_bytes` | `int` | Query, Optional | Input bytes |
| `tx_bps` | `int` | Query, Optional | Output rate |
| `rx_bps` | `int` | Query, Optional | Input rate |
| `tx_mcast_pkts` | `int` | Query, Optional | Multicast output packets |
| `tx_bcast_pkts` | `int` | Query, Optional | Broadcast output packets |
| `rx_mcast_pkts` | `int` | Query, Optional | Multicast input packets |
| `rx_bcast_pkts` | `int` | Query, Optional | Broadcast input packets |
| `speed` | `int` | Query, Optional | port speed |
| `stp_state` | [`StpStateEnum`](../../doc/models/stp-state-enum.md) | Query, Optional | if `up`==`true` |
| `stp_role` | [`StpRoleEnum`](../../doc/models/stp-role-enum.md) | Query, Optional | if `up`==`true` |
| `auth_state` | [`AuthStateEnum`](../../doc/models/auth-state-enum.md) | Query, Optional | if `up`==`true` && has Authenticator role |
| `up` | `bool` | Query, Optional | indicates if interface is up |
| `limit` | `int` | Query, Optional | **Default**: `100`<br>**Constraints**: `>= 0` |
| `start` | `int` | Query, Optional | **Default**: `0`<br>**Constraints**: `>= 0` |
| `end` | `int` | Query, Optional | **Default**: `0`<br>**Constraints**: `>= 0` |
| `duration` | `string` | Query, Optional | For historical stats and/or logs where time range is needed, you can specify the time range in a few different ways:<br><br>* ?start=1430000000&end=1430864000	specify the start / end<br>* ?end=1430864000&duration=1d	specify end time and duration<br>* ?duration=1d	specify duration, end will be now() in seconds<br>**Default**: `'1d'` |

## Response Type

[`ApiV1SitesStatsSwitchPortsSearchResponse`](../../doc/models/api-v1-sites-stats-switch-ports-search-response.md)

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

limit = 100

start = 0

end = 0

duration = '10m'

result = sites_devices_stats_controller.search_site_switch_ports(
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
  "end": 1513177200,
  "limit": 10,
  "results": [
    {
      "mac": "5c4527a96580",
      "neighbor_mac": "64d814353400",
      "neighbor_port_desc": "GigabitEthernet1/0/21",
      "neighbor_system_name": "CORP-D-SW-2",
      "org_id": "c168ddee-c14c-11e5-8e81-1258369c38a9",
      "poe_disabled": true,
      "port_id": "me0",
      "port_mac": "5c4527a96580",
      "rx_bytes": 4563443626,
      "rx_pkts": 30360265,
      "site_id": "c1698122-c14c-11e5-8e81-1258369c38a9",
      "speed": 1000,
      "tx_bytes": 11299516780,
      "tx_pkts": 14610886,
      "up": true
    },
    {
      "full_duplex": true,
      "mac": "0c8126c6ff6c",
      "neighbor_mac": "5c5b350eb361",
      "neighbor_port_desc": "ETH0",
      "neighbor_system_name": "kevinsap",
      "org_id": "c168ddee-c14c-11e5-8e81-1258369c38a9",
      "poe_mode": "802.3at",
      "poe_on": true,
      "port_id": "ge-0/0/0",
      "port_mac": "0c8126c6ff6f",
      "power_draw": 5.4,
      "rx_bps": 1176,
      "rx_bytes": 2628451,
      "rx_pkts": 11829,
      "site_id": "c1698122-c14c-11e5-8e81-1258369c38a9",
      "speed": 1000,
      "tx_bps": 14264,
      "tx_bytes": 96810192,
      "tx_pkts": 492176,
      "up": true
    }
  ],
  "start": 1511967600,
  "total": 100
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesStatsSwitchPortsSearch401ErrorException`](../../doc/models/api-v1-sites-stats-switch-ports-search-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesStatsSwitchPortsSearch403ErrorException`](../../doc/models/api-v1-sites-stats-switch-ports-search-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesStatsSwitchPortsSearch404ErrorException`](../../doc/models/api-v1-sites-stats-switch-ports-search-404-error-exception.md) |

