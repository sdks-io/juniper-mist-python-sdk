# Sites Insights

```python
sites_insights_controller = client.sites_insights
```

## Class Name

`SitesInsightsController`

## Methods

* [Get Site Insight Metrics for Client](../../doc/controllers/sites-insights.md#get-site-insight-metrics-for-client)
* [Get Site Insight Metrics for Device](../../doc/controllers/sites-insights.md#get-site-insight-metrics-for-device)
* [List Site Rogue a Ps](../../doc/controllers/sites-insights.md#list-site-rogue-a-ps)
* [List Site Rogue Clients](../../doc/controllers/sites-insights.md#list-site-rogue-clients)
* [Get Site Insight Metrics](../../doc/controllers/sites-insights.md#get-site-insight-metrics)


# Get Site Insight Metrics for Client

Get Client Insight Metrics
See metrics possibilities at /api/v1/const/insight_metrics

```python
def get_site_insight_metrics_for_client(self,
                                       site_id,
                                       client_mac,
                                       metric,
                                       page=1,
                                       limit=100,
                                       start=0,
                                       end=0,
                                       duration='1d',
                                       interval=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `client_mac` | `string` | Template, Required | **Constraints**: *Pattern*: `^[0-9a-fA-F]{12}$` |
| `metric` | `string` | Template, Required | see /api/v1/const/insight_metrics for available metrics |
| `page` | `int` | Query, Optional | **Default**: `1`<br>**Constraints**: `>= 1` |
| `limit` | `int` | Query, Optional | **Default**: `100`<br>**Constraints**: `>= 0` |
| `start` | `int` | Query, Optional | **Default**: `0`<br>**Constraints**: `>= 0` |
| `end` | `int` | Query, Optional | **Default**: `0`<br>**Constraints**: `>= 0` |
| `duration` | `string` | Query, Optional | For historical stats and/or logs where time range is needed, you can specify the time range in a few different ways:<br><br>* ?start=1430000000&end=1430864000	specify the start / end<br>* ?end=1430864000&duration=1d	specify end time and duration<br>* ?duration=1d	specify duration, end will be now() in seconds<br>**Default**: `'1d'` |
| `interval` | `string` | Query, Optional | Aggregation works by giving a time range plus interval (e.g. 1d, 1h, 10m) where aggregation function would be applied to. |

## Response Type

[`InsightMetric`](../../doc/models/insight-metric.md)

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

client_mac = '0000000000ab'

metric = 'metric8'

page = 1

limit = 100

start = 0

end = 0

duration = '10m'

interval = '10m'

result = sites_insights_controller.get_site_insight_metrics_for_client(
    site_id,
    client_mac,
    metric,
    page,
    limit,
    start,
    end,
    duration,
    interval
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "end": 0,
  "interval": 0,
  "results": [
    {}
  ],
  "start": 0
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesInsightsClientMetric401ErrorException`](../../doc/models/api-v1-sites-insights-client-metric-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesInsightsClientMetric403ErrorException`](../../doc/models/api-v1-sites-insights-client-metric-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesInsightsClientMetric404ErrorException`](../../doc/models/api-v1-sites-insights-client-metric-404-error-exception.md) |


# Get Site Insight Metrics for Device

Get AP Insight Metrics
See metrics possibilities at /api/v1/const/insight_metrics

```python
def get_site_insight_metrics_for_device(self,
                                       site_id,
                                       metric,
                                       device_mac,
                                       page=1,
                                       limit=100,
                                       start=0,
                                       end=0,
                                       duration='1d',
                                       interval=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `metric` | `string` | Template, Required | see /api/v1/const/insight_metrics for available metrics |
| `device_mac` | `string` | Template, Required | **Constraints**: *Pattern*: `^[0-9a-fA-F]{12}$` |
| `page` | `int` | Query, Optional | **Default**: `1`<br>**Constraints**: `>= 1` |
| `limit` | `int` | Query, Optional | **Default**: `100`<br>**Constraints**: `>= 0` |
| `start` | `int` | Query, Optional | **Default**: `0`<br>**Constraints**: `>= 0` |
| `end` | `int` | Query, Optional | **Default**: `0`<br>**Constraints**: `>= 0` |
| `duration` | `string` | Query, Optional | For historical stats and/or logs where time range is needed, you can specify the time range in a few different ways:<br><br>* ?start=1430000000&end=1430864000	specify the start / end<br>* ?end=1430864000&duration=1d	specify end time and duration<br>* ?duration=1d	specify duration, end will be now() in seconds<br>**Default**: `'1d'` |
| `interval` | `string` | Query, Optional | Aggregation works by giving a time range plus interval (e.g. 1d, 1h, 10m) where aggregation function would be applied to. |

## Response Type

[`DeviceMetric`](../../doc/models/device-metric.md)

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

metric = 'metric8'

device_mac = '0000000000ab'

page = 1

limit = 100

start = 0

end = 0

duration = '10m'

interval = '10m'

result = sites_insights_controller.get_site_insight_metrics_for_device(
    site_id,
    metric,
    device_mac,
    page,
    limit,
    start,
    end,
    duration,
    interval
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "end": 1604347200,
  "interval": 3600,
  "limit": 168,
  "page": 1,
  "results": [
    10,
    11,
    12,
    12,
    10,
    9,
    9,
    9,
    10,
    10,
    11,
    11,
    11,
    11,
    11,
    11,
    11,
    10,
    11,
    11,
    10,
    11,
    11,
    10
  ],
  "rt": [
    "2020-11-01T20:00:00Z",
    "2020-11-01T21:00:00Z",
    "2020-11-01T22:00:00Z",
    "2020-11-01T23:00:00Z",
    "2020-11-02T00:00:00Z",
    "2020-11-02T01:00:00Z",
    "2020-11-02T02:00:00Z",
    "2020-11-02T03:00:00Z",
    "2020-11-02T04:00:00Z",
    "2020-11-02T05:00:00Z",
    "2020-11-02T06:00:00Z",
    "2020-11-02T07:00:00Z",
    "2020-11-02T08:00:00Z",
    "2020-11-02T09:00:00Z",
    "2020-11-02T10:00:00Z",
    "2020-11-02T11:00:00Z",
    "2020-11-02T12:00:00Z",
    "2020-11-02T13:00:00Z",
    "2020-11-02T14:00:00Z",
    "2020-11-02T15:00:00Z",
    "2020-11-02T16:00:00Z",
    "2020-11-02T17:00:00Z",
    "2020-11-02T18:00:00Z",
    "2020-11-02T19:00:00Z"
  ],
  "start": 1604260800
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesInsightsDeviceMetric401ErrorException`](../../doc/models/api-v1-sites-insights-device-metric-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesInsightsDeviceMetric403ErrorException`](../../doc/models/api-v1-sites-insights-device-metric-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesInsightsDeviceMetric404ErrorException`](../../doc/models/api-v1-sites-insights-device-metric-404-error-exception.md) |


# List Site Rogue a Ps

Get List of Site Rogue/Neighbor APs

```python
def list_site_rogue_a_ps(self,
                        site_id,
                        mtype=None,
                        limit=100,
                        start=0,
                        end=0,
                        duration='1d',
                        interval=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `mtype` | [`Type57Enum`](../../doc/models/type-57-enum.md) | Query, Optional | - |
| `limit` | `int` | Query, Optional | **Default**: `100`<br>**Constraints**: `>= 0` |
| `start` | `int` | Query, Optional | **Default**: `0`<br>**Constraints**: `>= 0` |
| `end` | `int` | Query, Optional | **Default**: `0`<br>**Constraints**: `>= 0` |
| `duration` | `string` | Query, Optional | For historical stats and/or logs where time range is needed, you can specify the time range in a few different ways:<br><br>* ?start=1430000000&end=1430864000	specify the start / end<br>* ?end=1430864000&duration=1d	specify end time and duration<br>* ?duration=1d	specify duration, end will be now() in seconds<br>**Default**: `'1d'` |
| `interval` | `string` | Query, Optional | Aggregation works by giving a time range plus interval (e.g. 1d, 1h, 10m) where aggregation function would be applied to. |

## Response Type

[`InsightRogue`](../../doc/models/insight-rogue.md)

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

limit = 100

start = 0

end = 0

duration = '10m'

interval = '10m'

result = sites_insights_controller.list_site_rogue_a_ps(
    site_id,
    limit,
    start,
    end,
    duration,
    interval
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "end": 1428954000,
  "limit": 100,
  "next": "/api/v1/sites/a3eda150-ab3f-11e4-aa18-13e21dd250cc/rogues?start=1498482000&end=1498485600&limit=10&interval=1h&type=others",
  "results": [
    {
      "ap_mac": "5c5b350e021c",
      "avg_rssi": -72,
      "bssid": "d8-97-ba-76-b5-aa",
      "channel": "11",
      "num_aps": 4,
      "ssid": "xfinitywifi",
      "times_heard": 8
    }
  ],
  "start": 1428939600
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesInsightsRogues401ErrorException`](../../doc/models/api-v1-sites-insights-rogues-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesInsightsRogues403ErrorException`](../../doc/models/api-v1-sites-insights-rogues-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesInsightsRogues404ErrorException`](../../doc/models/api-v1-sites-insights-rogues-404-error-exception.md) |


# List Site Rogue Clients

Get List of Site Rogue Clients

```python
def list_site_rogue_clients(self,
                           site_id,
                           limit=100,
                           start=0,
                           end=0,
                           duration='1d',
                           interval=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `limit` | `int` | Query, Optional | **Default**: `100`<br>**Constraints**: `>= 0` |
| `start` | `int` | Query, Optional | **Default**: `0`<br>**Constraints**: `>= 0` |
| `end` | `int` | Query, Optional | **Default**: `0`<br>**Constraints**: `>= 0` |
| `duration` | `string` | Query, Optional | For historical stats and/or logs where time range is needed, you can specify the time range in a few different ways:<br><br>* ?start=1430000000&end=1430864000	specify the start / end<br>* ?end=1430864000&duration=1d	specify end time and duration<br>* ?duration=1d	specify duration, end will be now() in seconds<br>**Default**: `'1d'` |
| `interval` | `string` | Query, Optional | Aggregation works by giving a time range plus interval (e.g. 1d, 1h, 10m) where aggregation function would be applied to. |

## Response Type

[`InsightRogueClients`](../../doc/models/insight-rogue-clients.md)

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

limit = 100

start = 0

end = 0

duration = '10m'

interval = '10m'

result = sites_insights_controller.list_site_rogue_clients(
    site_id,
    limit,
    start,
    end,
    duration,
    interval
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "end": 1428954000,
  "limit": 100,
  "next": "/api/v1/sites/a3eda150-ab3f-11e4-aa18-13e21dd250cc/rogues/clients?start=1498482000&end=1498485600&limit=10&interval=1h",
  "results": [
    {
      "annotation": "whitelist",
      "ap_mac": "5c-5b-35-0e-02-1c",
      "avg_rssi": -63.9,
      "band": "5",
      "bssid": "d8-97-ba-76-b5-aa",
      "client_mac": "34-f8-32-13-57-c2",
      "num_aps": 2
    }
  ],
  "start": 1428939600
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesInsightsRoguesClients401ErrorException`](../../doc/models/api-v1-sites-insights-rogues-clients-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesInsightsRoguesClients403ErrorException`](../../doc/models/api-v1-sites-insights-rogues-clients-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesInsightsRoguesClients404ErrorException`](../../doc/models/api-v1-sites-insights-rogues-clients-404-error-exception.md) |


# Get Site Insight Metrics

Get Site Insight Metrics
See metrics possibilities at /api/v1/const/insight_metrics

```python
def get_site_insight_metrics(self,
                            site_id,
                            metric,
                            page=1,
                            limit=100,
                            start=0,
                            end=0,
                            duration='1d',
                            interval=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `metric` | `string` | Template, Required | see /api/v1/const/insight_metrics for available metrics |
| `page` | `int` | Query, Optional | **Default**: `1`<br>**Constraints**: `>= 1` |
| `limit` | `int` | Query, Optional | **Default**: `100`<br>**Constraints**: `>= 0` |
| `start` | `int` | Query, Optional | **Default**: `0`<br>**Constraints**: `>= 0` |
| `end` | `int` | Query, Optional | **Default**: `0`<br>**Constraints**: `>= 0` |
| `duration` | `string` | Query, Optional | For historical stats and/or logs where time range is needed, you can specify the time range in a few different ways:<br><br>* ?start=1430000000&end=1430864000	specify the start / end<br>* ?end=1430864000&duration=1d	specify end time and duration<br>* ?duration=1d	specify duration, end will be now() in seconds<br>**Default**: `'1d'` |
| `interval` | `string` | Query, Optional | Aggregation works by giving a time range plus interval (e.g. 1d, 1h, 10m) where aggregation function would be applied to. |

## Response Type

[`InsightMetric`](../../doc/models/insight-metric.md)

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

metric = 'metric8'

page = 1

limit = 100

start = 0

end = 0

duration = '10m'

interval = '10m'

result = sites_insights_controller.get_site_insight_metrics(
    site_id,
    metric,
    page,
    limit,
    start,
    end,
    duration,
    interval
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "end": 0,
  "interval": 0,
  "results": [
    {}
  ],
  "start": 0
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesInsights401ErrorException`](../../doc/models/api-v1-sites-insights-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesInsights403ErrorException`](../../doc/models/api-v1-sites-insights-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesInsights404ErrorException`](../../doc/models/api-v1-sites-insights-404-error-exception.md) |

