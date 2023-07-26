# Sites Skyatp

```python
sites_skyatp_controller = client.sites_skyatp
```

## Class Name

`SitesSkyatpController`

## Methods

* [Count Site Skyatp Events](../../doc/controllers/sites-skyatp.md#count-site-skyatp-events)
* [Search Site Skyatp Events](../../doc/controllers/sites-skyatp.md#search-site-skyatp-events)


# Count Site Skyatp Events

Count by Distinct Attributes of Skyatp Events (WIP)

```python
def count_site_skyatp_events(self,
                            site_id,
                            distinct='type',
                            mtype=None,
                            mac=None,
                            device_mac=None,
                            threat_level=None,
                            ip_address=None,
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
| `distinct` | [`Distinct15Enum`](../../doc/models/distinct-15-enum.md) | Query, Optional | **Default**: `'type'` |
| `mtype` | `string` | Query, Optional | event type, e.g. cc, fs, mw |
| `mac` | `string` | Query, Optional | client MAC |
| `device_mac` | `string` | Query, Optional | device MAC |
| `threat_level` | `int` | Query, Optional | threat level |
| `ip_address` | `string` | Query, Optional | - |
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

distinct = Distinct15Enum.ENUM_TYPE

ip_address = '192.168.1.1'

page = 1

limit = 100

start = 0

end = 0

duration = '10m'

result = sites_skyatp_controller.count_site_skyatp_events(
    site_id,
    distinct,
    ip_address,
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
| 401 | Unauthorized | [`ApiV1SitesSkyatpEventsCount401ErrorException`](../../doc/models/api-v1-sites-skyatp-events-count-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesSkyatpEventsCount403ErrorException`](../../doc/models/api-v1-sites-skyatp-events-count-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesSkyatpEventsCount404ErrorException`](../../doc/models/api-v1-sites-skyatp-events-count-404-error-exception.md) |


# Search Site Skyatp Events

Search Skyatp Events (WIP)

```python
def search_site_skyatp_events(self,
                             site_id,
                             mtype=None,
                             mac=None,
                             device_mac=None,
                             threat_level=None,
                             ip_address=None,
                             limit=100,
                             start=0,
                             end=0,
                             duration='1d')
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `mtype` | `string` | Query, Optional | event type, e.g. cc, fs, mw |
| `mac` | `string` | Query, Optional | client MAC |
| `device_mac` | `string` | Query, Optional | device MAC |
| `threat_level` | `int` | Query, Optional | threat level |
| `ip_address` | `string` | Query, Optional | - |
| `limit` | `int` | Query, Optional | **Default**: `100`<br>**Constraints**: `>= 0` |
| `start` | `int` | Query, Optional | **Default**: `0`<br>**Constraints**: `>= 0` |
| `end` | `int` | Query, Optional | **Default**: `0`<br>**Constraints**: `>= 0` |
| `duration` | `string` | Query, Optional | For historical stats and/or logs where time range is needed, you can specify the time range in a few different ways:<br><br>* ?start=1430000000&end=1430864000	specify the start / end<br>* ?end=1430864000&duration=1d	specify end time and duration<br>* ?duration=1d	specify duration, end will be now() in seconds<br>**Default**: `'1d'` |

## Response Type

[`ApiV1SitesSkyatpEventsSearchResponse`](../../doc/models/api-v1-sites-skyatp-events-search-response.md)

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

ip_address = '192.168.1.1'

limit = 100

start = 0

end = 0

duration = '10m'

result = sites_skyatp_controller.search_site_skyatp_events(
    site_id,
    ip_address,
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
  "end": 1513176951,
  "limit": 10,
  "results": [
    {
      "device_mac": "658279bb1fa4",
      "ip": "172.16.0.11",
      "mac": "b019c66c8348",
      "org_id": "3139f2c2-fac6-11e5-8156-0242ac110006",
      "site_id": "70e0f468-fc13-11e5-85ad-0242ac110008",
      "threat_level": 7,
      "timestamp": 1592524478,
      "type": "cc"
    }
  ],
  "start": 1512572151,
  "total": 1
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesSkyatpEventsSearch401ErrorException`](../../doc/models/api-v1-sites-skyatp-events-search-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesSkyatpEventsSearch403ErrorException`](../../doc/models/api-v1-sites-skyatp-events-search-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesSkyatpEventsSearch404ErrorException`](../../doc/models/api-v1-sites-skyatp-events-search-404-error-exception.md) |

