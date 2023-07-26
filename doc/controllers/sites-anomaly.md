# Sites Anomaly

```python
sites_anomaly_controller = client.sites_anomaly
```

## Class Name

`SitesAnomalyController`

## Methods

* [Get Site Anomaly Events for Client](../../doc/controllers/sites-anomaly.md#get-site-anomaly-events-for-client)
* [Get Site Anomaly Eventsfor Device](../../doc/controllers/sites-anomaly.md#get-site-anomaly-eventsfor-device)
* [Get Site Anomaly Events](../../doc/controllers/sites-anomaly.md#get-site-anomaly-events)


# Get Site Anomaly Events for Client

Get Client Anomaly Events

```python
def get_site_anomaly_events_for_client(self,
                                      site_id,
                                      client_mac,
                                      metric)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `client_mac` | `string` | Template, Required | **Constraints**: *Pattern*: `^[0-9a-fA-F]{12}$` |
| `metric` | `string` | Template, Required | see /api/v1/const/insight_metrics for available metrics |

## Response Type

[`AnomalyMetrics`](../../doc/models/anomaly-metrics.md)

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

client_mac = '0000000000ab'

metric = 'metric8'

result = sites_anomaly_controller.get_site_anomaly_events_for_client(
    site_id,
    client_mac,
    metric
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesAnomalyClientMetric401ErrorException`](../../doc/models/api-v1-sites-anomaly-client-metric-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesAnomalyClientMetric403ErrorException`](../../doc/models/api-v1-sites-anomaly-client-metric-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesAnomalyClientMetric404ErrorException`](../../doc/models/api-v1-sites-anomaly-client-metric-404-error-exception.md) |


# Get Site Anomaly Eventsfor Device

Get Device Anomaly Events

```python
def get_site_anomaly_eventsfor_device(self,
                                     site_id,
                                     metric,
                                     device_mac)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `metric` | `string` | Template, Required | see /api/v1/const/insight_metrics for available metrics |
| `device_mac` | `string` | Template, Required | **Constraints**: *Pattern*: `^[0-9a-fA-F]{12}$` |

## Response Type

[`AnomalyMetrics`](../../doc/models/anomaly-metrics.md)

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

metric = 'metric8'

device_mac = '0000000000ab'

result = sites_anomaly_controller.get_site_anomaly_eventsfor_device(
    site_id,
    metric,
    device_mac
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesAnomalyDeviceMetric401ErrorException`](../../doc/models/api-v1-sites-anomaly-device-metric-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesAnomalyDeviceMetric403ErrorException`](../../doc/models/api-v1-sites-anomaly-device-metric-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesAnomalyDeviceMetric404ErrorException`](../../doc/models/api-v1-sites-anomaly-device-metric-404-error-exception.md) |


# Get Site Anomaly Events

Get Site Anomaly Events

```python
def get_site_anomaly_events(self,
                           site_id,
                           metric)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `metric` | `string` | Template, Required | see /api/v1/const/insight_metrics for available metrics |

## Response Type

[`AnomalyMetrics`](../../doc/models/anomaly-metrics.md)

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

metric = 'metric8'

result = sites_anomaly_controller.get_site_anomaly_events(
    site_id,
    metric
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesAnomaly401ErrorException`](../../doc/models/api-v1-sites-anomaly-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesAnomaly403ErrorException`](../../doc/models/api-v1-sites-anomaly-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesAnomaly404ErrorException`](../../doc/models/api-v1-sites-anomaly-404-error-exception.md) |

