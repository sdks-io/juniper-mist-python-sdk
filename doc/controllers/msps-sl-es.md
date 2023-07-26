# Msps SL Es

```python
msps_sl_es_controller = client.msps_sl_es
```

## Class Name

`MspsSLEsController`


# Get Msp Sle

Get MSP SLEs (all/worst Orgs ...)

```python
def get_msp_sle(self,
               msp_id,
               metric,
               sle=None,
               duration='1d',
               interval=None,
               start=0,
               end=0)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `msp_id` | `uuid\|string` | Template, Required | - |
| `metric` | `string` | Template, Required | see /api/v1/const/insight_metrics for available metrics |
| `sle` | `string` | Query, Optional | see /api/v1/const/insight_metrics for more details |
| `duration` | `string` | Query, Optional | For historical stats and/or logs where time range is needed, you can specify the time range in a few different ways:<br><br>* ?start=1430000000&end=1430864000	specify the start / end<br>* ?end=1430864000&duration=1d	specify end time and duration<br>* ?duration=1d	specify duration, end will be now() in seconds<br>**Default**: `'1d'` |
| `interval` | `string` | Query, Optional | Aggregation works by giving a time range plus interval (e.g. 1d, 1h, 10m) where aggregation function would be applied to. |
| `start` | `int` | Query, Optional | **Default**: `0`<br>**Constraints**: `>= 0` |
| `end` | `int` | Query, Optional | **Default**: `0`<br>**Constraints**: `>= 0` |

## Response Type

[`ApiV1MspsInsightsResponse`](../../doc/models/api-v1-msps-insights-response.md)

## Example Usage

```python
msp_id = '000000ab-00ab-00ab-00ab-0000000000ab'

metric = 'metric8'

duration = '10m'

interval = '10m'

start = 0

end = 0

result = msps_sl_es_controller.get_msp_sle(
    msp_id,
    metric,
    duration,
    interval,
    start,
    end
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "end": 1643706000,
  "interval": 3600,
  "limit": 100,
  "results": [
    {
      "ap-availability": 0.9919400860511628,
      "ap-health": 0.967607512909879,
      "capacity": 0.7484652273070254,
      "coverage": 0.91217567374857,
      "num_aps": 13,
      "num_clients": 12,
      "org_id": "978c48e6-6ef6-11e6-8bbf-02e208b2d34f",
      "roaming": 0.991735537682683,
      "roaming-exp": 0.991735537682683,
      "successful-connect": 0.46052632135780236,
      "throughput": 0.6775702123846302,
      "time-to-connect": 0.9349112447196916
    },
    {
      "ap-availability": 0.9990384613092129,
      "ap-health": 0.48201754375507955,
      "capacity": 0.9702673450306101,
      "coverage": 0.8335392334930375,
      "num_aps": 1,
      "num_clients": 6,
      "org_id": "49ff76e0-a283-4e7d-b38d-041f1e9aff3c",
      "roaming": 1,
      "roaming-exp": 1,
      "successful-connect": 1,
      "throughput": 0,
      "time-to-connect": 1
    },
    {
      "ap-availability": 1,
      "ap-health": 0.982456140612301,
      "capacity": 1,
      "coverage": 0.9276041182442488,
      "num_aps": 2,
      "num_clients": 3,
      "org_id": "9b9b48f1-15a4-459e-86cc-9cbec9005983",
      "roaming": 1,
      "roaming-exp": 1,
      "successful-connect": 1,
      "throughput": 1,
      "time-to-connect": 0.8125
    },
    {
      "ap-availability": 0.9981132070973234,
      "ap-health": 0.9991228068084047,
      "capacity": 1,
      "coverage": 1,
      "num_aps": 1,
      "num_clients": 0,
      "org_id": "eb0e1671-7a6b-472b-94c3-c187dafe5274",
      "roaming": 1,
      "roaming-exp": 1,
      "successful-connect": 1,
      "throughput": 0,
      "time-to-connect": 0.5
    }
  ],
  "start": 1643670000
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1MspsInsights401ErrorException`](../../doc/models/api-v1-msps-insights-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1MspsInsights403ErrorException`](../../doc/models/api-v1-msps-insights-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1MspsInsights404ErrorException`](../../doc/models/api-v1-msps-insights-404-error-exception.md) |

