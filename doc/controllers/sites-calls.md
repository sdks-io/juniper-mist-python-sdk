# Sites Calls

```python
sites_calls_controller = client.sites_calls
```

## Class Name

`SitesCallsController`

## Methods

* [Count Site Call Events](../../doc/controllers/sites-calls.md#count-site-call-events)
* [Search Site Call Events](../../doc/controllers/sites-calls.md#search-site-call-events)
* [Count Site Calls](../../doc/controllers/sites-calls.md#count-site-calls)
* [Search Site Calls](../../doc/controllers/sites-calls.md#search-site-calls)


# Count Site Call Events

Count Site Call Events

```python
def count_site_call_events(self,
                          site_id,
                          distinct=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `distinct` | [`Distinct4Enum`](../../doc/models/distinct-4-enum.md) | Query, Optional | - |

## Response Type

[`Count`](../../doc/models/count.md)

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

result = sites_calls_controller.count_site_call_events(site_id)
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
| 401 | Unauthorized | [`ApiV1SitesCallEventsCount401ErrorException`](../../doc/models/api-v1-sites-call-events-count-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesCallEventsCount403ErrorException`](../../doc/models/api-v1-sites-call-events-count-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesCallEventsCount404ErrorException`](../../doc/models/api-v1-sites-call-events-count-404-error-exception.md) |


# Search Site Call Events

Search Site Call Events

```python
def search_site_call_events(self,
                           site_id,
                           mtype=None,
                           ap=None,
                           mac=None,
                           app=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `mtype` | `string` | Query, Optional | Event Type. See [listCallEventsDefinitions](/#operation/listCallEventsDefinitions) |
| `ap` | `string` | Query, Optional | - |
| `mac` | `string` | Query, Optional | - |
| `app` | `string` | Query, Optional | - |

## Response Type

[`CallEventsArraySearch`](../../doc/models/call-events-array-search.md)

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

result = sites_calls_controller.search_site_call_events(site_id)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "end": 1674819324,
  "limit": 10,
  "results": [
    {
      "app": "zoom",
      "audio_quality": "good",
      "meeting_id": "87609329850",
      "org_id": "2818e386-8dec-2562-9ede-5b8a0fbbdc71",
      "reason": "Host ended the meeting.",
      "screen_share_quality": "good",
      "site_id": "1916d52a-4a90-11e5-8b45-1258369c38a9",
      "timestamp": 1674199827,
      "type": "CLIENT_LEFT_CALL",
      "video_quality": "good",
      "wcid": "82c70a73-e2e1-42f9-6da0-97db44b7b9ad"
    },
    {
      "app": "zoom",
      "meeting_id": "87609329850",
      "org_id": "2818e386-8dec-2562-9ede-5b8a0fbbdc71",
      "reason": "Network connection error.",
      "site_id": "1916d52a-4a90-11e5-8b45-1258369c38a9",
      "timestamp": 1674199827,
      "type": "CLIENT_DISCONNECTED_FROM_CALL",
      "wcid": "82c70a73-e2e1-42f9-6da0-97db44b7b9ad"
    },
    {
      "app": "zoom",
      "meeting_id": "87609329850",
      "org_id": "2818e386-8dec-2562-9ede-5b8a0fbbdc71",
      "site_id": "1916d52a-4a90-11e5-8b45-1258369c38a9",
      "timestamp": 1674199827,
      "type": "CLIENTS_JOINED_CALL",
      "wcid": "82c70a73-e2e1-42f9-6da0-97db44b7b9ad"
    }
  ],
  "start": 1674153000,
  "total": 3
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesCallEventsSearch401ErrorException`](../../doc/models/api-v1-sites-call-events-search-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesCallEventsSearch403ErrorException`](../../doc/models/api-v1-sites-call-events-search-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesCallEventsSearch404ErrorException`](../../doc/models/api-v1-sites-call-events-search-404-error-exception.md) |


# Count Site Calls

Count by Distinct Attributes of Calls

```python
def count_site_calls(self,
                    site_id,
                    distrinct='mac',
                    rating=None,
                    app=None,
                    start=None,
                    end=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `distrinct` | [`DistrinctEnum`](../../doc/models/distrinct-enum.md) | Query, Optional | **Default**: `'mac'` |
| `rating` | `int` | Query, Optional | feedback rating (e.g. "rating=1" or "rating=1,2")<br>**Constraints**: `>= 1`, `<= 5` |
| `app` | `string` | Query, Optional | - |
| `start` | `string` | Query, Optional | - |
| `end` | `string` | Query, Optional | - |

## Response Type

[`Count`](../../doc/models/count.md)

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

distrinct = DistrinctEnum.MAC

result = sites_calls_controller.count_site_calls(
    site_id,
    distrinct
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
| 401 | Unauthorized | [`ApiV1SitesStatsCallsCount401ErrorException`](../../doc/models/api-v1-sites-stats-calls-count-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesStatsCallsCount403ErrorException`](../../doc/models/api-v1-sites-stats-calls-count-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesStatsCallsCount404ErrorException`](../../doc/models/api-v1-sites-stats-calls-count-404-error-exception.md) |


# Search Site Calls

Search Calls

```python
def search_site_calls(self,
                     site_id,
                     mac=None,
                     app=None,
                     limit=100,
                     start=0,
                     end=0,
                     duration='1d')
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `mac` | `string` | Query, Optional | device identifier |
| `app` | `string` | Query, Optional | Third party app name |
| `limit` | `int` | Query, Optional | **Default**: `100`<br>**Constraints**: `>= 0` |
| `start` | `int` | Query, Optional | **Default**: `0`<br>**Constraints**: `>= 0` |
| `end` | `int` | Query, Optional | **Default**: `0`<br>**Constraints**: `>= 0` |
| `duration` | `string` | Query, Optional | For historical stats and/or logs where time range is needed, you can specify the time range in a few different ways:<br><br>* ?start=1430000000&end=1430864000	specify the start / end<br>* ?end=1430864000&duration=1d	specify end time and duration<br>* ?duration=1d	specify duration, end will be now() in seconds<br>**Default**: `'1d'` |

## Response Type

[`CallStatsArray`](../../doc/models/call-stats-array.md)

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

app = 'zoom'

limit = 100

start = 0

end = 0

duration = '10m'

result = sites_calls_controller.search_site_calls(
    site_id,
    app,
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
| 401 | Unauthorized | [`ApiV1SitesStatsCallsSearch401ErrorException`](../../doc/models/api-v1-sites-stats-calls-search-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesStatsCallsSearch403ErrorException`](../../doc/models/api-v1-sites-stats-calls-search-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesStatsCallsSearch404ErrorException`](../../doc/models/api-v1-sites-stats-calls-search-404-error-exception.md) |

