# Sites Rogues

```python
sites_rogues_controller = client.sites_rogues
```

## Class Name

`SitesRoguesController`

## Methods

* [Count Site Rogue Events](../../doc/controllers/sites-rogues.md#count-site-rogue-events)
* [Search Site Rogue Events](../../doc/controllers/sites-rogues.md#search-site-rogue-events)
* [Get Site Rogue AP](../../doc/controllers/sites-rogues.md#get-site-rogue-ap)
* [Deauth Site Wireless Clients Connected to a Rogue](../../doc/controllers/sites-rogues.md#deauth-site-wireless-clients-connected-to-a-rogue)


# Count Site Rogue Events

Count Rogue Events

```python
def count_site_rogue_events(self,
                           site_id,
                           distinct='bssid',
                           mtype=None,
                           ssid=None,
                           bssid=None,
                           ap_mac=None,
                           channel=None,
                           seen_on_lan=None,
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
| `distinct` | [`Distinct14Enum`](../../doc/models/distinct-14-enum.md) | Query, Optional | **Default**: `'bssid'` |
| `mtype` | [`Type57Enum`](../../doc/models/type-57-enum.md) | Query, Optional | - |
| `ssid` | `string` | Query, Optional | ssid of the network detected as threat |
| `bssid` | `string` | Query, Optional | bssid of the network detected as threat |
| `ap_mac` | `string` | Query, Optional | mac of the device that had strongest signal strength for ssid/bssid pair |
| `channel` | `string` | Query, Optional | channel over which ap_mac heard ssid/bssid pair |
| `seen_on_lan` | `bool` | Query, Optional | whether the reporting AP see a wireless client (on LAN) connecting to it |
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

distinct = Distinct14Enum.BSSID

page = 1

limit = 100

start = 0

end = 0

duration = '10m'

result = sites_rogues_controller.count_site_rogue_events(
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
| 401 | Unauthorized | [`ApiV1SitesRoguesEventsCount401ErrorException`](../../doc/models/api-v1-sites-rogues-events-count-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesRoguesEventsCount403ErrorException`](../../doc/models/api-v1-sites-rogues-events-count-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesRoguesEventsCount404ErrorException`](../../doc/models/api-v1-sites-rogues-events-count-404-error-exception.md) |


# Search Site Rogue Events

Search Rogue Events

```python
def search_site_rogue_events(self,
                            site_id,
                            mtype=None,
                            ssid=None,
                            bssid=None,
                            ap_mac=None,
                            channel=None,
                            seen_on_lan=None,
                            limit=100,
                            start=0,
                            end=0,
                            duration='1d')
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `mtype` | [`Type57Enum`](../../doc/models/type-57-enum.md) | Query, Optional | - |
| `ssid` | `string` | Query, Optional | ssid of the network detected as threat |
| `bssid` | `string` | Query, Optional | bssid of the network detected as threat |
| `ap_mac` | `string` | Query, Optional | mac of the device that had strongest signal strength for ssid/bssid pair |
| `channel` | `int` | Query, Optional | channel over which ap_mac heard ssid/bssid pair |
| `seen_on_lan` | `bool` | Query, Optional | whether the reporting AP see a wireless client (on LAN) connecting to it |
| `limit` | `int` | Query, Optional | **Default**: `100`<br>**Constraints**: `>= 0` |
| `start` | `int` | Query, Optional | **Default**: `0`<br>**Constraints**: `>= 0` |
| `end` | `int` | Query, Optional | **Default**: `0`<br>**Constraints**: `>= 0` |
| `duration` | `string` | Query, Optional | For historical stats and/or logs where time range is needed, you can specify the time range in a few different ways:<br><br>* ?start=1430000000&end=1430864000	specify the start / end<br>* ?end=1430864000&duration=1d	specify end time and duration<br>* ?duration=1d	specify duration, end will be now() in seconds<br>**Default**: `'1d'` |

## Response Type

[`RogueEventsSearch`](../../doc/models/rogue-events-search.md)

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

limit = 100

start = 0

end = 0

duration = '10m'

result = sites_rogues_controller.search_site_rogue_events(
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
  "end": 1538074800,
  "limit": 10,
  "results": [
    {
      "ap": "5c5b350e10030",
      "bssid": "38ff363c8c4c",
      "channel": 136,
      "rssi": -54,
      "ssid": "MyHomeNetwork",
      "timestamp": 1538074612
    },
    {
      "ap": "5c5b350e10030",
      "bssid": "60d02c2394cc",
      "channel": 11,
      "rssi": -59,
      "ssid": "Home-Office",
      "timestamp": 1538074612
    }
  ],
  "start": 1538071200,
  "total": 2
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesRoguesEventsSearch401ErrorException`](../../doc/models/api-v1-sites-rogues-events-search-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesRoguesEventsSearch403ErrorException`](../../doc/models/api-v1-sites-rogues-events-search-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesRoguesEventsSearch404ErrorException`](../../doc/models/api-v1-sites-rogues-events-search-404-error-exception.md) |


# Get Site Rogue AP

Get Rogue AP Details

```python
def get_site_rogue_ap(self,
                     site_id,
                     rogue_bssid)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `rogue_bssid` | `string` | Template, Required | **Constraints**: *Pattern*: `^[0-9a-fA-F]{12}$` |

## Response Type

[`ApiV1SitesRoguesResponse`](../../doc/models/api-v1-sites-rogues-response.md)

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

rogue_bssid = '0000000000ab'

result = sites_rogues_controller.get_site_rogue_ap(
    site_id,
    rogue_bssid
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "manufacture": "Intel Corporate",
  "seen_as_client": true
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesRogues401ErrorException`](../../doc/models/api-v1-sites-rogues-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesRogues403ErrorException`](../../doc/models/api-v1-sites-rogues-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesRogues404ErrorException`](../../doc/models/api-v1-sites-rogues-404-error-exception.md) |


# Deauth Site Wireless Clients Connected to a Rogue

Send Deauth frame to clients connected to a Rogue AP

```python
def deauth_site_wireless_clients_connected_to_a_rogue(self,
                                                     site_id,
                                                     rogue_bssid)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `rogue_bssid` | `string` | Template, Required | **Constraints**: *Pattern*: `^[0-9a-fA-F]{12}$` |

## Response Type

`object`

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

rogue_bssid = '0000000000ab'

result = sites_rogues_controller.deauth_site_wireless_clients_connected_to_a_rogue(
    site_id,
    rogue_bssid
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesRoguesDeauthClients401ErrorException`](../../doc/models/api-v1-sites-rogues-deauth-clients-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesRoguesDeauthClients403ErrorException`](../../doc/models/api-v1-sites-rogues-deauth-clients-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesRoguesDeauthClients404ErrorException`](../../doc/models/api-v1-sites-rogues-deauth-clients-404-error-exception.md) |

