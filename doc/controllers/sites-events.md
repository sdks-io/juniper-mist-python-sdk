# Sites Events

```python
sites_events_controller = client.sites_events
```

## Class Name

`SitesEventsController`

## Methods

* [Get Site Roaming Events](../../doc/controllers/sites-events.md#get-site-roaming-events)
* [Get Site Interference Events](../../doc/controllers/sites-events.md#get-site-interference-events)
* [Count Site System Events](../../doc/controllers/sites-events.md#count-site-system-events)
* [Search Site System Events](../../doc/controllers/sites-events.md#search-site-system-events)


# Get Site Roaming Events

Get Roaming Events data

```python
def get_site_roaming_events(self,
                           site_id,
                           mtype=None,
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
| `mtype` | [`Type55Enum`](../../doc/models/type-55-enum.md) | Query, Optional | event type |
| `page` | `int` | Query, Optional | **Default**: `1`<br>**Constraints**: `>= 1` |
| `limit` | `int` | Query, Optional | **Default**: `100`<br>**Constraints**: `>= 0` |
| `start` | `int` | Query, Optional | **Default**: `0`<br>**Constraints**: `>= 0` |
| `end` | `int` | Query, Optional | **Default**: `0`<br>**Constraints**: `>= 0` |
| `duration` | `string` | Query, Optional | For historical stats and/or logs where time range is needed, you can specify the time range in a few different ways:<br><br>* ?start=1430000000&end=1430864000	specify the start / end<br>* ?end=1430864000&duration=1d	specify end time and duration<br>* ?duration=1d	specify duration, end will be now() in seconds<br>**Default**: `'1d'` |

## Response Type

[`EventsFastroam`](../../doc/models/events-fastroam.md)

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

page = 1

limit = 100

start = 0

end = 0

duration = '10m'

result = sites_events_controller.get_site_roaming_events(
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
  "end": 1501023379,
  "limit": 2,
  "next": "/api/v1/sites/dca0a44b-324c-11e6-a776-0243ad110007/events/fast_roam?type=success&start=1428939600&end=1428949600&limit=200&token=AAAAEgAIAAVVJh4hF8AAAARzc2lkAH%2F%2F%2F%2F0%3D",
  "results": [
    {
      "ap_mac": "5c5b350e040b",
      "client_mac": "dc2b2a3fb13d",
      "fromap": "5c5b350e0569",
      "latency": 0.1874195,
      "ssid": "marvis_test",
      "subtype": "CLIENT_AUTHENTICATED_11R",
      "timestamp": 1501000002283782
    }
  ],
  "start": 1500940800
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesEventsFastRoam401ErrorException`](../../doc/models/api-v1-sites-events-fast-roam-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesEventsFastRoam403ErrorException`](../../doc/models/api-v1-sites-events-fast-roam-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesEventsFastRoam404ErrorException`](../../doc/models/api-v1-sites-events-fast-roam-404-error-exception.md) |


# Get Site Interference Events

Get Interference Events

```python
def get_site_interference_events(self,
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

[`EventsInterference`](../../doc/models/events-interference.md)

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

page = 1

limit = 100

start = 0

end = 0

duration = '10m'

result = sites_events_controller.get_site_interference_events(
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
  "end": 1428954000,
  "limit": 100,
  "page": 1,
  "results": [
    {
      "ap_id": "00000000-0000-0000-1000-5c5b359e4fe0",
      "band": 5,
      "channel_util": 0.03,
      "channels": [
        1,
        2,
        5
      ],
      "rssi": -64,
      "source": "Microwave Oven",
      "timestamp": 1428939600
    }
  ],
  "start": 1428939600,
  "total": 135
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesEventsInterference401ErrorException`](../../doc/models/api-v1-sites-events-interference-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesEventsInterference403ErrorException`](../../doc/models/api-v1-sites-events-interference-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesEventsInterference404ErrorException`](../../doc/models/api-v1-sites-events-interference-404-error-exception.md) |


# Count Site System Events

Count System Events

```python
def count_site_system_events(self,
                            site_id,
                            distinct='type',
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
| `distinct` | [`Distinct11Enum`](../../doc/models/distinct-11-enum.md) | Query, Optional | **Default**: `'type'` |
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

distinct = Distinct11Enum.ENUM_TYPE

page = 1

limit = 100

start = 0

end = 0

duration = '10m'

result = sites_events_controller.count_site_system_events(
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
| 401 | Unauthorized | [`ApiV1SitesEventsSystemCount401ErrorException`](../../doc/models/api-v1-sites-events-system-count-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesEventsSystemCount403ErrorException`](../../doc/models/api-v1-sites-events-system-count-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesEventsSystemCount404ErrorException`](../../doc/models/api-v1-sites-events-system-count-404-error-exception.md) |


# Search Site System Events

Search System Events

```python
def search_site_system_events(self,
                             site_id,
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
| `mtype` | `string` | Query, Optional | - |
| `limit` | `int` | Query, Optional | **Default**: `100`<br>**Constraints**: `>= 0` |
| `start` | `int` | Query, Optional | **Default**: `0`<br>**Constraints**: `>= 0` |
| `end` | `int` | Query, Optional | **Default**: `0`<br>**Constraints**: `>= 0` |
| `duration` | `string` | Query, Optional | For historical stats and/or logs where time range is needed, you can specify the time range in a few different ways:<br><br>* ?start=1430000000&end=1430864000	specify the start / end<br>* ?end=1430864000&duration=1d	specify end time and duration<br>* ?duration=1d	specify duration, end will be now() in seconds<br>**Default**: `'1d'` |

## Response Type

[`DevicesEventsSearch`](../../doc/models/devices-events-search.md)

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

limit = 100

start = 0

end = 0

duration = '10m'

result = sites_events_controller.search_site_system_events(
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
  "end": 0,
  "limit": 0,
  "next": "string",
  "results": [
    {
      "ap": "5c5b351e13b5",
      "apfw": "5c5b351e13b5",
      "model": "BT11-WW",
      "org_id": "4ac1dcf4-9d8b-7211-65c4-057819f0862a",
      "site_id": "4ac1dcf4-9d8b-7211-65c4-057819f0862b",
      "text": "Succeeding DNS query from 172.29.101.134 to 172.29.101.7 for \"portal.mistsys.com\" on vlan 1, id 60224",
      "timestamp": 1547235620.89,
      "type": "CLIENT_DNS_OK"
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
| 401 | Unauthorized | [`ApiV1SitesEventsSystemSearch401ErrorException`](../../doc/models/api-v1-sites-events-system-search-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesEventsSystemSearch403ErrorException`](../../doc/models/api-v1-sites-events-system-search-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesEventsSystemSearch404ErrorException`](../../doc/models/api-v1-sites-events-system-search-404-error-exception.md) |

