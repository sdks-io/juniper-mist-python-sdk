# Sites Stats

```python
sites_stats_controller = client.sites_stats
```

## Class Name

`SitesStatsController`

## Methods

* [Get Site Stats](../../doc/controllers/sites-stats.md#get-site-stats)
* [List Site Assets Stats](../../doc/controllers/sites-stats.md#list-site-assets-stats)
* [Get Site Asset Stats](../../doc/controllers/sites-stats.md#get-site-asset-stats)
* [List Site Beacons Stats](../../doc/controllers/sites-stats.md#list-site-beacons-stats)
* [List Site Wireless Clients Stats](../../doc/controllers/sites-stats.md#list-site-wireless-clients-stats)
* [Get Site Wireless Client Stats](../../doc/controllers/sites-stats.md#get-site-wireless-client-stats)
* [List Site Discovered Assets](../../doc/controllers/sites-stats.md#list-site-discovered-assets)
* [Search Site Discovered Switches Metrics](../../doc/controllers/sites-stats.md#search-site-discovered-switches-metrics)
* [Count Site Discovered Switches](../../doc/controllers/sites-stats.md#count-site-discovered-switches)
* [Get Site Discovered Switches Metrics](../../doc/controllers/sites-stats.md#get-site-discovered-switches-metrics)
* [Search Site Discovered Switches](../../doc/controllers/sites-stats.md#search-site-discovered-switches)
* [Get Site Gateway Metrics](../../doc/controllers/sites-stats.md#get-site-gateway-metrics)
* [Get Site Wireless Clients Stats by Map](../../doc/controllers/sites-stats.md#get-site-wireless-clients-stats-by-map)
* [Get Site Discovered Asset by Map](../../doc/controllers/sites-stats.md#get-site-discovered-asset-by-map)
* [Get Site Sdk Stats by Map](../../doc/controllers/sites-stats.md#get-site-sdk-stats-by-map)
* [List Site Unconnected Client Stats](../../doc/controllers/sites-stats.md#list-site-unconnected-client-stats)
* [Get Site Sdk Stats](../../doc/controllers/sites-stats.md#get-site-sdk-stats)
* [Get Site Wx Rules Usage](../../doc/controllers/sites-stats.md#get-site-wx-rules-usage)
* [List Site Zones Stats](../../doc/controllers/sites-stats.md#list-site-zones-stats)
* [Get Site Zone Stats](../../doc/controllers/sites-stats.md#get-site-zone-stats)


# Get Site Stats

Get Site Stats

```python
def get_site_stats(self,
                  site_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |

## Response Type

[`StatsSite`](../../doc/models/stats-site.md)

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

result = sites_stats_controller.get_site_stats(site_id)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "address": "string",
  "alarmtemplate_id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
  "country_code": "string",
  "created_time": 0,
  "id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
  "lat": 0,
  "latlng": {
    "lat": 0,
    "lng": 0
  },
  "lng": 0,
  "modified_time": 0,
  "msp_id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
  "name": "string",
  "networktemplate_id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
  "num_ap": 0,
  "num_ap_connected": 0,
  "num_clients": 0,
  "num_devices": 0,
  "num_devices_connected": 0,
  "num_gateway": 0,
  "num_gateway_connected": 0,
  "num_switch": 0,
  "num_switch_connected": 0,
  "org_id": "a40f5d1f-d889-42e9-94ea-b9b33585fc6b",
  "rftemplate_id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
  "sitegroup_ids": [
    "6f4bf402-45f9-2a56-6c8b-7f83d3bc98e9"
  ],
  "timezone": "string",
  "tzoffset": 0
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesStats401ErrorException`](../../doc/models/api-v1-sites-stats-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesStats403ErrorException`](../../doc/models/api-v1-sites-stats-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesStats404ErrorException`](../../doc/models/api-v1-sites-stats-404-error-exception.md) |


# List Site Assets Stats

Get List of Site Assets Stats

```python
def list_site_assets_stats(self,
                          site_id,
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
| `page` | `int` | Query, Optional | **Default**: `1`<br>**Constraints**: `>= 1` |
| `limit` | `int` | Query, Optional | **Default**: `100`<br>**Constraints**: `>= 0` |
| `start` | `int` | Query, Optional | **Default**: `0`<br>**Constraints**: `>= 0` |
| `end` | `int` | Query, Optional | **Default**: `0`<br>**Constraints**: `>= 0` |
| `duration` | `string` | Query, Optional | For historical stats and/or logs where time range is needed, you can specify the time range in a few different ways:<br><br>* ?start=1430000000&end=1430864000	specify the start / end<br>* ?end=1430864000&duration=1d	specify end time and duration<br>* ?duration=1d	specify duration, end will be now() in seconds<br>**Default**: `'1d'` |

## Response Type

[`List of StatsAsset`](../../doc/models/stats-asset.md)

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

page = 1

limit = 100

start = 0

end = 0

duration = '10m'

result = sites_stats_controller.list_site_assets_stats(
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
[
  {
    "battery_voltage": 0,
    "eddystone_uid_instance": "string",
    "eddystone_uid_namespace": "string",
    "eddystone_url_url": "string",
    "ibeacon_major": 0,
    "ibeacon_minor": 0,
    "ibeacon_uuid": "1f89bc00-d0af-481b-82fe-a6629259a39f",
    "last_seen": 0,
    "mac": "string",
    "map_id": "09d2b626-2e4e-45ef-a3c4-e6aeb6c83db1",
    "name": "string",
    "rssizones": [
      {
        "id": "478f6eca-6276-4993-bfeb-5bcbbbba6f08",
        "since": 0
      }
    ],
    "x": 0,
    "y": 0,
    "zones": [
      {
        "id": "477f6eca-6276-4993-bfeb-5ccbbbba6f08",
        "since": 0
      }
    ]
  }
]
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesStatsAssets401ErrorException`](../../doc/models/api-v1-sites-stats-assets-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesStatsAssets403ErrorException`](../../doc/models/api-v1-sites-stats-assets-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesStatsAssets404ErrorException`](../../doc/models/api-v1-sites-stats-assets-404-error-exception.md) |


# Get Site Asset Stats

Get Site Asset Details

```python
def get_site_asset_stats(self,
                        site_id,
                        start=0,
                        end=0,
                        duration='1d')
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `start` | `int` | Query, Optional | **Default**: `0`<br>**Constraints**: `>= 0` |
| `end` | `int` | Query, Optional | **Default**: `0`<br>**Constraints**: `>= 0` |
| `duration` | `string` | Query, Optional | For historical stats and/or logs where time range is needed, you can specify the time range in a few different ways:<br><br>* ?start=1430000000&end=1430864000	specify the start / end<br>* ?end=1430864000&duration=1d	specify end time and duration<br>* ?duration=1d	specify duration, end will be now() in seconds<br>**Default**: `'1d'` |

## Response Type

[`StatsAsset`](../../doc/models/stats-asset.md)

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

start = 0

end = 0

duration = '10m'

result = sites_stats_controller.get_site_asset_stats(
    site_id,
    start,
    end,
    duration
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "battery_voltage": 0,
  "eddystone_uid_instance": "string",
  "eddystone_uid_namespace": "string",
  "eddystone_url_url": "string",
  "ibeacon_major": 0,
  "ibeacon_minor": 0,
  "ibeacon_uuid": "1f89bc00-d0af-481b-82fe-a6629259a39f",
  "last_seen": 0,
  "mac": "string",
  "map_id": "09d2b626-2e4e-45ef-a3c4-e6aeb6c83db1",
  "name": "string",
  "rssizones": [
    {
      "id": "480f6eca-6276-4993-bfeb-59cbbbba6f08",
      "since": 0
    }
  ],
  "x": 0,
  "y": 0,
  "zones": [
    {
      "id": "479f6eca-6276-4993-bfeb-5acbbbba6f08",
      "since": 0
    }
  ]
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesStatsAssetsAssetId401ErrorException`](../../doc/models/api-v1-sites-stats-assets-asset-id-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesStatsAssetsAssetId403ErrorException`](../../doc/models/api-v1-sites-stats-assets-asset-id-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesStatsAssetsAssetId404ErrorException`](../../doc/models/api-v1-sites-stats-assets-asset-id-404-error-exception.md) |


# List Site Beacons Stats

Get List of Site Beacons Stats

```python
def list_site_beacons_stats(self,
                           site_id,
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
| `page` | `int` | Query, Optional | **Default**: `1`<br>**Constraints**: `>= 1` |
| `limit` | `int` | Query, Optional | **Default**: `100`<br>**Constraints**: `>= 0` |
| `start` | `int` | Query, Optional | **Default**: `0`<br>**Constraints**: `>= 0` |
| `end` | `int` | Query, Optional | **Default**: `0`<br>**Constraints**: `>= 0` |
| `duration` | `string` | Query, Optional | For historical stats and/or logs where time range is needed, you can specify the time range in a few different ways:<br><br>* ?start=1430000000&end=1430864000	specify the start / end<br>* ?end=1430864000&duration=1d	specify end time and duration<br>* ?duration=1d	specify duration, end will be now() in seconds<br>**Default**: `'1d'` |

## Response Type

[`List of StatsBeacon`](../../doc/models/stats-beacon.md)

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

page = 1

limit = 100

start = 0

end = 0

duration = '10m'

result = sites_stats_controller.list_site_beacons_stats(
    site_id,
    page,
    limit,
    start,
    end,
    duration
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesStatsBeacons401ErrorException`](../../doc/models/api-v1-sites-stats-beacons-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesStatsBeacons403ErrorException`](../../doc/models/api-v1-sites-stats-beacons-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesStatsBeacons404ErrorException`](../../doc/models/api-v1-sites-stats-beacons-404-error-exception.md) |


# List Site Wireless Clients Stats

Get List of Site All Clients Stats Details

```python
def list_site_wireless_clients_stats(self,
                                    site_id,
                                    wired=False)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `wired` | `bool` | Query, Optional | **Default**: `False` |

## Response Type

`List of mixed`

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

wired = False

result = sites_stats_controller.list_site_wireless_clients_stats(
    site_id,
    wired
)
print(result)
```

## Example Response

```
[
  {
    "_id": "003ee1bec926",
    "_ttl": 277,
    "ap_id": "00000000-0000-0000-1000-d420b085fdff",
    "auth_state": "authorizedForCompleteAccess",
    "eth_port": "eth1",
    "last_seen": 1645060912.0751352,
    "mac": "e45f01319a43",
    "rx_bytes": 0,
    "rx_pkts": 0,
    "site_id": "1916d52a-4a90-11e5-8b45-1258369c38a9",
    "tx_bytes": 0,
    "tx_pkts": 0,
    "uptime": 8723766,
    "vlan_id": 70
  }
]
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesStatsClients401ErrorException`](../../doc/models/api-v1-sites-stats-clients-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesStatsClients403ErrorException`](../../doc/models/api-v1-sites-stats-clients-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesStatsClients404ErrorException`](../../doc/models/api-v1-sites-stats-clients-404-error-exception.md) |


# Get Site Wireless Client Stats

Get Site Client Stats Details

```python
def get_site_wireless_client_stats(self,
                                  site_id,
                                  client_mac,
                                  wired=False)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `client_mac` | `string` | Template, Required | **Constraints**: *Pattern*: `^[0-9a-fA-F]{12}$` |
| `wired` | `bool` | Query, Optional | **Default**: `False` |

## Response Type

`mixed`

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

client_mac = '0000000000ab'

wired = False

result = sites_stats_controller.get_site_wireless_client_stats(
    site_id,
    client_mac,
    wired
)
print(result)
```

## Example Response

```
{
  "_id": "003ee1bec926",
  "_ttl": 277,
  "ap_id": "00000000-0000-0000-1000-d420b085fdff",
  "auth_state": "authorizedForCompleteAccess",
  "eth_port": "eth1",
  "last_seen": 1645060912.0751352,
  "mac": "e45f01319a43",
  "rx_bytes": 0,
  "rx_pkts": 0,
  "site_id": "1916d52a-4a90-11e5-8b45-1258369c38a9",
  "tx_bytes": 0,
  "tx_pkts": 0,
  "uptime": 8723766,
  "vlan_id": 70
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesStatsClients401ErrorException`](../../doc/models/api-v1-sites-stats-clients-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesStatsClients403ErrorException`](../../doc/models/api-v1-sites-stats-clients-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesStatsClients404ErrorException`](../../doc/models/api-v1-sites-stats-clients-404-error-exception.md) |


# List Site Discovered Assets

Get List of Site Discovered BLE Assets that doesn’t match any of the Asset / Assetfilters

```python
def list_site_discovered_assets(self,
                               site_id,
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
| `page` | `int` | Query, Optional | **Default**: `1`<br>**Constraints**: `>= 1` |
| `limit` | `int` | Query, Optional | **Default**: `100`<br>**Constraints**: `>= 0` |
| `start` | `int` | Query, Optional | **Default**: `0`<br>**Constraints**: `>= 0` |
| `end` | `int` | Query, Optional | **Default**: `0`<br>**Constraints**: `>= 0` |
| `duration` | `string` | Query, Optional | For historical stats and/or logs where time range is needed, you can specify the time range in a few different ways:<br><br>* ?start=1430000000&end=1430864000	specify the start / end<br>* ?end=1430864000&duration=1d	specify end time and duration<br>* ?duration=1d	specify duration, end will be now() in seconds<br>**Default**: `'1d'` |

## Response Type

[`List of Asset`](../../doc/models/asset.md)

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

page = 1

limit = 100

start = 0

end = 0

duration = '10m'

result = sites_stats_controller.list_site_discovered_assets(
    site_id,
    page,
    limit,
    start,
    end,
    duration
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesStatsDiscoveredAssets401ErrorException`](../../doc/models/api-v1-sites-stats-discovered-assets-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesStatsDiscoveredAssets403ErrorException`](../../doc/models/api-v1-sites-stats-discovered-assets-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesStatsDiscoveredAssets404ErrorException`](../../doc/models/api-v1-sites-stats-discovered-assets-404-error-exception.md) |


# Search Site Discovered Switches Metrics

Search Discovered Switch Metrics

```python
def search_site_discovered_switches_metrics(self,
                                           site_id,
                                           scope='site',
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
| `scope` | [`Scope17Enum`](../../doc/models/scope-17-enum.md) | Query, Optional | metric scope, optional<br>**Default**: `'site'` |
| `mtype` | [`Type62Enum`](../../doc/models/type-62-enum.md) | Query, Optional | metric type, inactive_wired_vlans/switch_ap_affinity/poe_compliance/version_compliance, optional |
| `limit` | `int` | Query, Optional | **Default**: `100`<br>**Constraints**: `>= 0` |
| `start` | `int` | Query, Optional | **Default**: `0`<br>**Constraints**: `>= 0` |
| `end` | `int` | Query, Optional | **Default**: `0`<br>**Constraints**: `>= 0` |
| `duration` | `string` | Query, Optional | For historical stats and/or logs where time range is needed, you can specify the time range in a few different ways:<br><br>* ?start=1430000000&end=1430864000	specify the start / end<br>* ?end=1430864000&duration=1d	specify end time and duration<br>* ?duration=1d	specify duration, end will be now() in seconds<br>**Default**: `'1d'` |

## Response Type

[`ApiV1SitesStatsDiscoveredSwitchMetricsSearchResponse`](../../doc/models/api-v1-sites-stats-discovered-switch-metrics-search-response.md)

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

scope = Scope17Enum.SITE

limit = 100

start = 0

end = 0

duration = '10m'

result = sites_stats_controller.search_site_discovered_switches_metrics(
    site_id,
    scope,
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
  "end": 1675193686.0191767,
  "limit": 1,
  "next": "/api/v1/sites/f5fcbee5-fbca-45b3-8bf1-1619ede87879/stats/discovered_switch_metrics/search?end=1675193686.0191767&limit=1&search_after=%5B1675193400000%5D&start=1675107286.0191767",
  "results": [
    {
      "details": {},
      "org_id": "203d3d02-dbc0-4c1b-9f41-76896a3330f4",
      "scope": "site",
      "score": 100,
      "site_id": "f5fcbee5-fbca-45b3-8bf1-1619ede87879",
      "timestamp": 1675193400,
      "type": "inactive_wired_vlans"
    }
  ],
  "start": 1675107286.0191767,
  "total": 3
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesStatsDiscoveredSwitchMetricsSearch401ErrorException`](../../doc/models/api-v1-sites-stats-discovered-switch-metrics-search-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesStatsDiscoveredSwitchMetricsSearch403ErrorException`](../../doc/models/api-v1-sites-stats-discovered-switch-metrics-search-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesStatsDiscoveredSwitchMetricsSearch404ErrorException`](../../doc/models/api-v1-sites-stats-discovered-switch-metrics-search-404-error-exception.md) |


# Count Site Discovered Switches

Count Discovered Switches

```python
def count_site_discovered_switches(self,
                                  site_id,
                                  distinct='system_name',
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
| `distinct` | [`Distinct18Enum`](../../doc/models/distinct-18-enum.md) | Query, Optional | **Default**: `'system_name'` |
| `page` | `int` | Query, Optional | **Default**: `1`<br>**Constraints**: `>= 1` |
| `limit` | `int` | Query, Optional | **Default**: `100`<br>**Constraints**: `>= 0` |
| `start` | `int` | Query, Optional | **Default**: `0`<br>**Constraints**: `>= 0` |
| `end` | `int` | Query, Optional | **Default**: `0`<br>**Constraints**: `>= 0` |
| `duration` | `string` | Query, Optional | For historical stats and/or logs where time range is needed, you can specify the time range in a few different ways:<br><br>* ?start=1430000000&end=1430864000	specify the start / end<br>* ?end=1430864000&duration=1d	specify end time and duration<br>* ?duration=1d	specify duration, end will be now() in seconds<br>**Default**: `'1d'` |

## Response Type

[`ApiV1SitesStatsDiscoveredSwitchesCountResponse`](../../doc/models/api-v1-sites-stats-discovered-switches-count-response.md)

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

distinct = Distinct18Enum.SYSTEM_NAME

page = 1

limit = 100

start = 0

end = 0

duration = '10m'

result = sites_stats_controller.count_site_discovered_switches(
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
  "distinct": "system_name",
  "end": 1604496202.3555834,
  "limit": 1000,
  "percentage": 100,
  "results": [
    {
      "count": 1,
      "system_name": "test-ex"
    },
    {
      "count": 1,
      "system_name": "sw-jn-01"
    }
  ],
  "start": 1604409802.3555677,
  "total": 2
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesStatsDiscoveredSwitchesCount401ErrorException`](../../doc/models/api-v1-sites-stats-discovered-switches-count-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesStatsDiscoveredSwitchesCount403ErrorException`](../../doc/models/api-v1-sites-stats-discovered-switches-count-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesStatsDiscoveredSwitchesCount404ErrorException`](../../doc/models/api-v1-sites-stats-discovered-switches-count-404-error-exception.md) |


# Get Site Discovered Switches Metrics

Discovered switches related metrics, lists related switch system names & details if not compliant

```python
def get_site_discovered_switches_metrics(self,
                                        site_id,
                                        threshold=None,
                                        system_name=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `threshold` | `string` | Query, Optional | configurable # ap per switch threshold, default 12 |
| `system_name` | `string` | Query, Optional | system name for switch level metrics, optional |

## Response Type

[`ApiV1SitesStatsDiscoveredSwitchesMetricsResponse`](../../doc/models/api-v1-sites-stats-discovered-switches-metrics-response.md)

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

result = sites_stats_controller.get_site_discovered_switches_metrics(site_id)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "inactive_wired_vlans": {
    "details": {},
    "score": 100
  },
  "poe_compliance": {
    "details": {
      "total_aps": 63,
      "total_power": 981500
    },
    "score": 100
  },
  "switch_ap_affinity": {
    "details": {
      "system_name": [
        "mist-lab-ex2300c",
        "switch1"
      ],
      "threshold": 12
    },
    "score": 33.3333
  },
  "version_compliance": {
    "details": {
      "major_versions": [
        {
          "major_count": 2,
          "model": "EX2300-C-12P",
          "system_names": [
            "switch1",
            "mist-lab-ex2300c"
          ]
        },
        {
          "major_count": 1,
          "model": "EX4300-48P",
          "system_names": []
        }
      ],
      "total_switch_count": 5
    },
    "score": 75
  }
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesStatsDiscoveredSwitchesMetrics401ErrorException`](../../doc/models/api-v1-sites-stats-discovered-switches-metrics-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesStatsDiscoveredSwitchesMetrics403ErrorException`](../../doc/models/api-v1-sites-stats-discovered-switches-metrics-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesStatsDiscoveredSwitchesMetrics404ErrorException`](../../doc/models/api-v1-sites-stats-discovered-switches-metrics-404-error-exception.md) |


# Search Site Discovered Switches

Search Discovered Switches

```python
def search_site_discovered_switches(self,
                                   site_id,
                                   adopted=None,
                                   system_name=None,
                                   hostname=None,
                                   vendor=None,
                                   model=None,
                                   version=None,
                                   limit=100,
                                   start=0,
                                   end=0,
                                   duration='1d')
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `adopted` | `bool` | Query, Optional | - |
| `system_name` | `string` | Query, Optional | - |
| `hostname` | `string` | Query, Optional | - |
| `vendor` | `string` | Query, Optional | - |
| `model` | `string` | Query, Optional | - |
| `version` | `string` | Query, Optional | - |
| `limit` | `int` | Query, Optional | **Default**: `100`<br>**Constraints**: `>= 0` |
| `start` | `int` | Query, Optional | **Default**: `0`<br>**Constraints**: `>= 0` |
| `end` | `int` | Query, Optional | **Default**: `0`<br>**Constraints**: `>= 0` |
| `duration` | `string` | Query, Optional | For historical stats and/or logs where time range is needed, you can specify the time range in a few different ways:<br><br>* ?start=1430000000&end=1430864000	specify the start / end<br>* ?end=1430864000&duration=1d	specify end time and duration<br>* ?duration=1d	specify duration, end will be now() in seconds<br>**Default**: `'1d'` |

## Response Type

[`ApiV1SitesStatsDiscoveredSwitchesSearchResponse`](../../doc/models/api-v1-sites-stats-discovered-switches-search-response.md)

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

limit = 100

start = 0

end = 0

duration = '10m'

result = sites_stats_controller.search_site_discovered_switches(
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
  "end": 1604496474.8978634,
  "limit": 1000,
  "results": [
    {
      "aps": [
        {
          "hostname": "ap41nearlab",
          "inactive_wired_vlans": [],
          "mac": "5c5b352e2001",
          "poe_status": true,
          "when": "2019-06-13T19:53:16.870+0000"
        }
      ],
      "mgmt_addr": "10.1.1.1",
      "model": "EX2300-C-12P",
      "org_id": "6748cfa6-4e12-11e6-9188-0242ac110007",
      "site_id": "67970e46-4e12-11e6-9188-0242ac110007",
      "system_desc": "Juniper Networks, Inc. ex2300-c-12p Ethernet Switch, kernel JUNOS 18.2R2.6, Build date: 2018-12-07 13:19:04 UTC Copyright (c) 1996-2018 Juniper Networks, Inc.",
      "system_name": "mist-lab-ex2300c",
      "timestamp": 1560457177.037,
      "vendor": "Juniper Networks",
      "version": "18.2R2.6"
    }
  ],
  "start": 1604410074.8978484,
  "total": 1
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesStatsDiscoveredSwitchesSearch401ErrorException`](../../doc/models/api-v1-sites-stats-discovered-switches-search-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesStatsDiscoveredSwitchesSearch403ErrorException`](../../doc/models/api-v1-sites-stats-discovered-switches-search-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesStatsDiscoveredSwitchesSearch404ErrorException`](../../doc/models/api-v1-sites-stats-discovered-switches-search-404-error-exception.md) |


# Get Site Gateway Metrics

Get Site Gateway Metrics

```python
def get_site_gateway_metrics(self,
                            site_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |

## Response Type

[`ApiV1SitesStatsGatewaysMetricsResponse`](../../doc/models/api-v1-sites-stats-gateways-metrics-response.md)

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

result = sites_stats_controller.get_site_gateway_metrics(site_id)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "config_success": 99.9,
  "version_compliance": {
    "major_version": {
      "SRX320": {
        "major_count": 0,
        "major_version": "19.4R2-S1.2"
      }
    },
    "score": 99.9,
    "type": "gateway"
  }
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesStatsGatewaysMetrics401ErrorException`](../../doc/models/api-v1-sites-stats-gateways-metrics-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesStatsGatewaysMetrics403ErrorException`](../../doc/models/api-v1-sites-stats-gateways-metrics-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesStatsGatewaysMetrics404ErrorException`](../../doc/models/api-v1-sites-stats-gateways-metrics-404-error-exception.md) |


# Get Site Wireless Clients Stats by Map

Get Site Clients Stats By Map

```python
def get_site_wireless_clients_stats_by_map(self,
                                          site_id,
                                          map_id,
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
| `map_id` | `uuid\|string` | Template, Required | - |
| `page` | `int` | Query, Optional | **Default**: `1`<br>**Constraints**: `>= 1` |
| `limit` | `int` | Query, Optional | **Default**: `100`<br>**Constraints**: `>= 0` |
| `start` | `int` | Query, Optional | **Default**: `0`<br>**Constraints**: `>= 0` |
| `end` | `int` | Query, Optional | **Default**: `0`<br>**Constraints**: `>= 0` |
| `duration` | `string` | Query, Optional | For historical stats and/or logs where time range is needed, you can specify the time range in a few different ways:<br><br>* ?start=1430000000&end=1430864000	specify the start / end<br>* ?end=1430864000&duration=1d	specify end time and duration<br>* ?duration=1d	specify duration, end will be now() in seconds<br>**Default**: `'1d'` |

## Response Type

[`List of StatsClient`](../../doc/models/stats-client.md)

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

map_id = '000000ab-00ab-00ab-00ab-0000000000ab'

page = 1

limit = 100

start = 0

end = 0

duration = '10m'

result = sites_stats_controller.get_site_wireless_clients_stats_by_map(
    site_id,
    map_id,
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
[
  {
    "_ttl": 0,
    "accuracy": 0,
    "airespace_ifname": "string",
    "airwatch": {
      "authorized": true
    },
    "ap_id": "325b588d-147b-4fa4-bb40-83383f83c77e",
    "ap_mac": "string",
    "band": "24",
    "channel": 0,
    "dual_band": true,
    "family": "string",
    "guest": {
      "authorized": false,
      "authorized_expiring_time": 0,
      "authorized_time": 0,
      "company": "string",
      "email": "string",
      "field1": "string",
      "name": "string"
    },
    "hostname": "string",
    "idle_time": 0,
    "ip": "192.168.0.1",
    "ip6": "2001:0db8:85a3:0000:0000:8a2e:0370:7334",
    "is_guest": false,
    "key_mgmt": "string",
    "last_seen": 0,
    "mac": "string",
    "manufacture": "string",
    "map_id": "09d2b626-2e4e-45ef-a3c4-e6aeb6c83db1",
    "model": "string",
    "num_locating_aps": 0,
    "os": "string",
    "power_saving": true,
    "proto": "a",
    "psk_id": "4cb94c10-4e99-46b0-8261-4c71d0b2cb9d",
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
    "vlan_id": 0,
    "wlan_id": "5028e92b-fc59-4056-91d1-ea4b4ca1617a",
    "x": 0,
    "y": 0
  }
]
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesStatsMapsClients401ErrorException`](../../doc/models/api-v1-sites-stats-maps-clients-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesStatsMapsClients403ErrorException`](../../doc/models/api-v1-sites-stats-maps-clients-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesStatsMapsClients404ErrorException`](../../doc/models/api-v1-sites-stats-maps-clients-404-error-exception.md) |


# Get Site Discovered Asset by Map

Get a list of BLE beacons that we discovered (whether they’re defined as assets or not)

```python
def get_site_discovered_asset_by_map(self,
                                    site_id,
                                    map_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `map_id` | `uuid\|string` | Template, Required | - |

## Response Type

[`List of StatsAsset`](../../doc/models/stats-asset.md)

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

map_id = '000000ab-00ab-00ab-00ab-0000000000ab'

result = sites_stats_controller.get_site_discovered_asset_by_map(
    site_id,
    map_id
)
print(result)
```

## Example Response *(as JSON)*

```json
[
  {
    "device_name": "[TV] UN65JU670D",
    "duration": 120,
    "eddystone_uid_instance": "5c5b35000001",
    "eddystone_uid_namespace": "2818e3868dec25629ede",
    "eddystone_url_url": "https://www.abc.com",
    "ibeacon_major": 13,
    "ibeacon_minor": 138,
    "ibeacon_uuid": "f3f17139-704a-f03a-2786-0400279e37c3",
    "last_seen": 1428939600,
    "mac": "6fa474be7ae5",
    "manufacture": "Apple",
    "mfg_company_id": 935,
    "mfg_data": "648520a1020000",
    "x": 60,
    "y": 80
  }
]
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesStatsMapsDiscoveredAssets401ErrorException`](../../doc/models/api-v1-sites-stats-maps-discovered-assets-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesStatsMapsDiscoveredAssets403ErrorException`](../../doc/models/api-v1-sites-stats-maps-discovered-assets-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesStatsMapsDiscoveredAssets404ErrorException`](../../doc/models/api-v1-sites-stats-maps-discovered-assets-404-error-exception.md) |


# Get Site Sdk Stats by Map

Get SdkClient Stats By Map

```python
def get_site_sdk_stats_by_map(self,
                             site_id,
                             map_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `map_id` | `uuid\|string` | Template, Required | - |

## Response Type

[`List of StatsSdkclient`](../../doc/models/stats-sdkclient.md)

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

map_id = '000000ab-00ab-00ab-00ab-0000000000ab'

result = sites_stats_controller.get_site_sdk_stats_by_map(
    site_id,
    map_id
)
print(result)
```

## Example Response *(as JSON)*

```json
[
  {
    "id": "de87bf9d-183f-e383-cc68-6ba43947d403",
    "last_seen": 1428939600,
    "map_id": "845a23bf-bed9-e43c-4c86-6fa474be7ae5",
    "name": "John's iPhone",
    "network_connection": {
      "mac": "c3-b6-e5-af-41-15",
      "rssi": -75,
      "signal_level": 3,
      "type": "WiFi"
    },
    "uuid": "ada72f8f-1643-e5c6-94db-f2a5636f1a64",
    "x": 60,
    "y": 80
  }
]
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesStatsMapsSdkclients401ErrorException`](../../doc/models/api-v1-sites-stats-maps-sdkclients-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesStatsMapsSdkclients403ErrorException`](../../doc/models/api-v1-sites-stats-maps-sdkclients-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesStatsMapsSdkclients404ErrorException`](../../doc/models/api-v1-sites-stats-maps-sdkclients-404-error-exception.md) |


# List Site Unconnected Client Stats

Get List of Site Unconnected Client Location

```python
def list_site_unconnected_client_stats(self,
                                      site_id,
                                      map_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `map_id` | `uuid\|string` | Template, Required | - |

## Response Type

[`List of StatsUnconnectedClients`](../../doc/models/stats-unconnected-clients.md)

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

map_id = '000000ab-00ab-00ab-00ab-0000000000ab'

result = sites_stats_controller.list_site_unconnected_client_stats(
    site_id,
    map_id
)
print(result)
```

## Example Response *(as JSON)*

```json
[
  {
    "ap_mac": "5c5b350e0410",
    "last_seen": 1428939600,
    "mac": "5684dae9ac8b",
    "manufacture": "Apple",
    "map_id": "ea77be98-ab51-4ff8-a863-ac3c8e1b1c3a",
    "rssi": -75,
    "x": 60,
    "y": 80
  }
]
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesStatsMapsUnconnectedClients401ErrorException`](../../doc/models/api-v1-sites-stats-maps-unconnected-clients-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesStatsMapsUnconnectedClients403ErrorException`](../../doc/models/api-v1-sites-stats-maps-unconnected-clients-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesStatsMapsUnconnectedClients404ErrorException`](../../doc/models/api-v1-sites-stats-maps-unconnected-clients-404-error-exception.md) |


# Get Site Sdk Stats

Get Detail Stats of a SdkClient

```python
def get_site_sdk_stats(self,
                      site_id,
                      sdkclient_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `sdkclient_id` | `uuid\|string` | Template, Required | - |

## Response Type

[`StatsSdkclientDetails`](../../doc/models/stats-sdkclient-details.md)

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

sdkclient_id = '000000ab-00ab-00ab-00ab-0000000000ab'

result = sites_stats_controller.get_site_sdk_stats(
    site_id,
    sdkclient_id
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "id": "de87bf9d-183f-e383-cc68-6ba43947d403",
  "last_seen": 1428939600,
  "map_id": "845a23bf-bed9-e43c-4c86-6fa474be7ae5",
  "name": "John's iPhone",
  "network_connection": {
    "mac": "c3-b6-e5-af-41-15",
    "rssi": -75,
    "signal_level": 3,
    "type": "WiFi"
  },
  "uuid": "ada72f8f-1643-e5c6-94db-f2a5636f1a64",
  "vbeacons": [
    {
      "id": "d379d29d-24b4-96c5-5dd4-6f2a2dc5aaeb",
      "since": 1428939300
    }
  ],
  "x": 60,
  "y": 80,
  "zones": [
    {
      "id": "8ac84899-32db-6327-334c-9b6d58544cfe",
      "since": 1428939600
    }
  ]
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesStatsSdkclients401ErrorException`](../../doc/models/api-v1-sites-stats-sdkclients-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesStatsSdkclients403ErrorException`](../../doc/models/api-v1-sites-stats-sdkclients-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesStatsSdkclients404ErrorException`](../../doc/models/api-v1-sites-stats-sdkclients-404-error-exception.md) |


# Get Site Wx Rules Usage

Get Wxlan Rule usage

```python
def get_site_wx_rules_usage(self,
                           site_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |

## Response Type

[`List of StatsWxrule`](../../doc/models/stats-wxrule.md)

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

result = sites_stats_controller.get_site_wx_rules_usage(site_id)
print(result)
```

## Example Response *(as JSON)*

```json
[
  {
    "action": "allow",
    "client_mac": [
      "3bbbf819bb6f",
      "bd96cbc4910f"
    ],
    "dst_allow_wxtags": [
      "fff34466-eec0-3756-6765-381c728a6037",
      "eee2c7b0-d1d0-5a30-f349-e35fa43dc3b3"
    ],
    "dst_deny_wxtags": [
      "aaa34466-eec0-3756-6765-381c728a6037",
      "bbb2c7b0-d1d0-5a30-f349-e35fa43dc3b3"
    ],
    "dst_wxtags": [
      "d4134466-eec0-3756-6765-381c728a6037",
      "1a42c7b0-d1d0-5a30-f349-e35fa43dc3b3"
    ],
    "name": "Guest",
    "order": 1,
    "src_wxtags": [
      "8bfc2490-d726-3587-038d-cb2e71bd2330",
      "3aa8e73f-9f46-d827-8d6a-567bb7e67fc9"
    ],
    "usage": {
      "00000000-0000-0000-0000-000000000000": {
        "num_flows": 30
      },
      "1a42c7b0-d1d0-5a30-f349-e35fa43dc3b3": {
        "num_flows": 60
      },
      "d4134466-eec0-3756-6765-381c728a6037": {
        "num_flows": 60
      }
    }
  }
]
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesStatsWxrules401ErrorException`](../../doc/models/api-v1-sites-stats-wxrules-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesStatsWxrules403ErrorException`](../../doc/models/api-v1-sites-stats-wxrules-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesStatsWxrules404ErrorException`](../../doc/models/api-v1-sites-stats-wxrules-404-error-exception.md) |


# List Site Zones Stats

Get List of Site Zones Stats

```python
def list_site_zones_stats(self,
                         site_id,
                         map_id=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `map_id` | `string` | Query, Optional | - |

## Response Type

[`List of StatsZone`](../../doc/models/stats-zone.md)

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

map_id = '00000000-0000-0000-0000-000000000000'

result = sites_stats_controller.list_site_zones_stats(
    site_id,
    map_id
)
print(result)
```

## Example Response *(as JSON)*

```json
[
  {
    "assets_waits": {
      "avg": 0,
      "max": 0,
      "min": 0,
      "p95": 0
    },
    "clients_waits": {
      "avg": 1200,
      "max": 3610,
      "min": 600,
      "p95": 2800
    },
    "created_time": 1616625211,
    "id": "123470c7-5d9d-424a-8475-8b344c621234",
    "map_id": "123449d4-d12f-4feb-b40f-5be0e2ae1234",
    "modified_time": 1616625211,
    "name": "Zone A",
    "num_assets": 0,
    "num_clients": 80,
    "num_sdkclients": 10,
    "occupancy_limit": 4,
    "org_id": "1234c1a0-6ef6-11e6-8bbf-02e208b21234",
    "sdkclients_waits": {
      "avg": 1200,
      "max": 3610,
      "min": 600,
      "p95": 2800
    },
    "site_id": "123448e6-6ef6-11e6-8bbf-02e208b21234",
    "vertices": [
      {
        "x": 732,
        "y": 1821
      },
      {
        "x": 732.5,
        "y": 1731
      },
      {
        "x": 837.5,
        "y": 1731.5
      },
      {
        "x": 839,
        "y": 1821
      }
    ],
    "vertices_m": [
      {
        "x": 24.1983341951072,
        "y": 60.198314985369144
      },
      {
        "x": 24.21486311190714,
        "y": 57.22310996138056
      },
      {
        "x": 27.685935639893827,
        "y": 57.23963887818049
      },
      {
        "x": 27.73552239029364,
        "y": 60.198314985369144
      }
    ]
  }
]
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesStatsZones401ErrorException`](../../doc/models/api-v1-sites-stats-zones-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesStatsZones403ErrorException`](../../doc/models/api-v1-sites-stats-zones-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesStatsZones404ErrorException`](../../doc/models/api-v1-sites-stats-zones-404-error-exception.md) |


# Get Site Zone Stats

Get Detail Zone Stats

```python
def get_site_zone_stats(self,
                       site_id,
                       zone_type,
                       zone_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `zone_type` | [`ZoneTypeEnum`](../../doc/models/zone-type-enum.md) | Template, Required | - |
| `zone_id` | `uuid\|string` | Template, Required | - |

## Response Type

[`StatsZoneDetails`](../../doc/models/stats-zone-details.md)

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

zone_type = ZoneTypeEnum.ZONES

zone_id = '000000ab-00ab-00ab-00ab-0000000000ab'

result = sites_stats_controller.get_site_zone_stats(
    site_id,
    zone_type,
    zone_id
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "client_waits": {
    "avg": 1200,
    "max": 3610,
    "min": 600,
    "p95": 2800
  },
  "clients": [
    "5684dae9ac8b"
  ],
  "id": "8ac84899-32db-6327-334c-9b6d58544cfe",
  "map_id": "63eda950-c6da-11e4-a628-60f81dd250cc",
  "name": "Board Room",
  "num_clients": 80,
  "num_sdkclients": 0,
  "sdkclients": [
    "7e2b463d-c91c-ff7d-f3c0-6eccc6949ff8"
  ]
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesStatsZoneId401ErrorException`](../../doc/models/api-v1-sites-stats-zone-id-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesStatsZoneId403ErrorException`](../../doc/models/api-v1-sites-stats-zone-id-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesStatsZoneId404ErrorException`](../../doc/models/api-v1-sites-stats-zone-id-404-error-exception.md) |

