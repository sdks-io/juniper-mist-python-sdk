# Sites SL Es

```python
sites_sl_es_controller = client.sites_sl_es
```

## Class Name

`SitesSLEsController`

## Methods

* [Get Site Sle Classifier Details](../../doc/controllers/sites-sl-es.md#get-site-sle-classifier-details)
* [Get Site Sle Metric Classifiers](../../doc/controllers/sites-sl-es.md#get-site-sle-metric-classifiers)
* [Get Site Sle Histogram](../../doc/controllers/sites-sl-es.md#get-site-sle-histogram)
* [Get Site Sle Impact Summary](../../doc/controllers/sites-sl-es.md#get-site-sle-impact-summary)
* [Get Site Sle Impacted Applications](../../doc/controllers/sites-sl-es.md#get-site-sle-impacted-applications)
* [Get Site Sle Impacted Aps](../../doc/controllers/sites-sl-es.md#get-site-sle-impacted-aps)
* [Get Site Sle Impacted Chassis](../../doc/controllers/sites-sl-es.md#get-site-sle-impacted-chassis)
* [Get Site Sle Impacted Wired Clients](../../doc/controllers/sites-sl-es.md#get-site-sle-impacted-wired-clients)
* [Get Site Sle Impacted Gateways](../../doc/controllers/sites-sl-es.md#get-site-sle-impacted-gateways)
* [Get Site Sle Impacted Interfaces](../../doc/controllers/sites-sl-es.md#get-site-sle-impacted-interfaces)
* [Get Site Sle Impacted Switches](../../doc/controllers/sites-sl-es.md#get-site-sle-impacted-switches)
* [Get Site Sle Impacted Wireless Clients](../../doc/controllers/sites-sl-es.md#get-site-sle-impacted-wireless-clients)
* [Get Site Sle Summary](../../doc/controllers/sites-sl-es.md#get-site-sle-summary)
* [Get Site Sle Threshold](../../doc/controllers/sites-sl-es.md#get-site-sle-threshold)
* [Replace Site Sle Threshold](../../doc/controllers/sites-sl-es.md#replace-site-sle-threshold)
* [Update Site Sle Threshold](../../doc/controllers/sites-sl-es.md#update-site-sle-threshold)
* [Get Site Sles Metrics](../../doc/controllers/sites-sl-es.md#get-site-sles-metrics)


# Get Site Sle Classifier Details

Get SLE classifier details

```python
def get_site_sle_classifier_details(self,
                                   site_id,
                                   scope,
                                   scope_id,
                                   metric,
                                   classifier,
                                   start=0,
                                   end=0,
                                   duration='1d')
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `scope` | [`Scope2Enum`](../../doc/models/scope-2-enum.md) | Template, Required | - |
| `scope_id` | `string` | Template, Required | * site_id if `scope`==`site`<br>* device_id if `scope`==`ap`, `scope`==`switch` or `scope`==`gateway`<br>* mac if `scope`==`client` |
| `metric` | `string` | Template, Required | values from /api/v1/sites/{site_id}/sle/{scope}/{scope_id}/metrics |
| `classifier` | `string` | Template, Required | - |
| `start` | `int` | Query, Optional | **Default**: `0`<br>**Constraints**: `>= 0` |
| `end` | `int` | Query, Optional | **Default**: `0`<br>**Constraints**: `>= 0` |
| `duration` | `string` | Query, Optional | For historical stats and/or logs where time range is needed, you can specify the time range in a few different ways:<br><br>* ?start=1430000000&end=1430864000	specify the start / end<br>* ?end=1430864000&duration=1d	specify end time and duration<br>* ?duration=1d	specify duration, end will be now() in seconds<br>**Default**: `'1d'` |

## Response Type

[`SleClassifierSummary`](../../doc/models/sle-classifier-summary.md)

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

scope = Scope2Enum.SWITCH

scope_id = 'scope_id0'

metric = 'metric8'

classifier = 'classifier4'

start = 0

end = 0

duration = '10m'

result = sites_sl_es_controller.get_site_sle_classifier_details(
    site_id,
    scope,
    scope_id,
    metric,
    classifier,
    start,
    end,
    duration
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "classifier": {
    "impact": {
      "num_aps": 2,
      "num_users": 17
    },
    "interval": 3600,
    "name": "wifi-interference",
    "samples": {
      "degraded": [
        0,
        0,
        210.03334,
        3.1333334,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        102.5,
        108.03333,
        0,
        0,
        201.9,
        566.48334,
        135.63333,
        0
      ],
      "duration": [
        0,
        0,
        210.03334,
        3.1333334,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        102.5,
        108.03333,
        0,
        0,
        201.9,
        566.48334,
        135.63333,
        0
      ],
      "total": [
        1302.3,
        1289.0167,
        1396.3167,
        1423.6666,
        1439.2167,
        1414.7,
        1361.0834,
        1371.5834,
        1372.0667,
        1339.1,
        1374.3667,
        1369.9,
        1352.4833,
        1382.8,
        1426.7167,
        1425.6333,
        1403.9333,
        1420.75,
        1416.8334,
        1437.3334,
        1425.1,
        1485.3667,
        1426.4333,
        444.13333
      ]
    },
    "x_label": "seconds",
    "y_label": "user-minutes"
  },
  "end": 1627312871,
  "failures": [],
  "impact": {
    "num_aps": 2,
    "num_users": 21,
    "total_aps": 3,
    "total_users": 26
  },
  "metric": "capacity",
  "start": 1627226471
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesSleScopeIdMetricMetricClassifierClassifierSummary401ErrorException`](../../doc/models/api-v1-sites-sle-scope-id-metric-metric-classifier-classifier-summary-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesSleScopeIdMetricMetricClassifierClassifierSummary403ErrorException`](../../doc/models/api-v1-sites-sle-scope-id-metric-metric-classifier-classifier-summary-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesSleScopeIdMetricMetricClassifierClassifierSummary404ErrorException`](../../doc/models/api-v1-sites-sle-scope-id-metric-metric-classifier-classifier-summary-404-error-exception.md) |


# Get Site Sle Metric Classifiers

Get the list of classifiers for a specific metric

```python
def get_site_sle_metric_classifiers(self,
                                   site_id,
                                   scope,
                                   scope_id,
                                   metric)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `scope` | [`Scope2Enum`](../../doc/models/scope-2-enum.md) | Template, Required | - |
| `scope_id` | `string` | Template, Required | * site_id if `scope`==`site`<br>* device_id if `scope`==`ap`, `scope`==`switch` or `scope`==`gateway`<br>* mac if `scope`==`client` |
| `metric` | `string` | Template, Required | values from /api/v1/sites/{site_id}/sle/{scope}/{scope_id}/metrics |

## Response Type

`List of string`

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

scope = Scope2Enum.SWITCH

scope_id = 'scope_id0'

metric = 'metric8'

result = sites_sl_es_controller.get_site_sle_metric_classifiers(
    site_id,
    scope,
    scope_id,
    metric
)
print(result)
```

## Example Response

```
[
  "asymmetry-uplink",
  "weak-signal",
  "asymmetry-downlink"
]
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesSleScopeIdMetricMetricClassifiers401ErrorException`](../../doc/models/api-v1-sites-sle-scope-id-metric-metric-classifiers-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesSleScopeIdMetricMetricClassifiers403ErrorException`](../../doc/models/api-v1-sites-sle-scope-id-metric-metric-classifiers-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesSleScopeIdMetricMetricClassifiers404ErrorException`](../../doc/models/api-v1-sites-sle-scope-id-metric-metric-classifiers-404-error-exception.md) |


# Get Site Sle Histogram

Get the histogram for the SLE metric

```python
def get_site_sle_histogram(self,
                          site_id,
                          scope,
                          scope_id,
                          metric,
                          start=0,
                          end=0,
                          duration='1d')
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `scope` | [`Scope2Enum`](../../doc/models/scope-2-enum.md) | Template, Required | - |
| `scope_id` | `string` | Template, Required | * site_id if `scope`==`site`<br>* device_id if `scope`==`ap`, `scope`==`switch` or `scope`==`gateway`<br>* mac if `scope`==`client` |
| `metric` | `string` | Template, Required | values from /api/v1/sites/{site_id}/sle/{scope}/{scope_id}/metrics |
| `start` | `int` | Query, Optional | **Default**: `0`<br>**Constraints**: `>= 0` |
| `end` | `int` | Query, Optional | **Default**: `0`<br>**Constraints**: `>= 0` |
| `duration` | `string` | Query, Optional | For historical stats and/or logs where time range is needed, you can specify the time range in a few different ways:<br><br>* ?start=1430000000&end=1430864000	specify the start / end<br>* ?end=1430864000&duration=1d	specify end time and duration<br>* ?duration=1d	specify duration, end will be now() in seconds<br>**Default**: `'1d'` |

## Response Type

[`SleHistogram`](../../doc/models/sle-histogram.md)

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

scope = Scope2Enum.SWITCH

scope_id = 'scope_id0'

metric = 'metric8'

start = 0

end = 0

duration = '10m'

result = sites_sl_es_controller.get_site_sle_histogram(
    site_id,
    scope,
    scope_id,
    metric,
    start,
    end,
    duration
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "data": [
    {
      "range": [
        null,
        0
      ],
      "value": 0
    },
    {
      "range": [
        0,
        10
      ],
      "value": 0
    },
    {
      "range": [
        10,
        20
      ],
      "value": 5105
    },
    {
      "range": [
        20,
        30
      ],
      "value": 10616
    },
    {
      "range": [
        30,
        40
      ],
      "value": 40051
    },
    {
      "range": [
        40,
        50
      ],
      "value": 141201
    },
    {
      "range": [
        50,
        60
      ],
      "value": 949823
    },
    {
      "range": [
        60,
        70
      ],
      "value": 686308
    },
    {
      "range": [
        70,
        80
      ],
      "value": 177670
    },
    {
      "range": [
        80,
        90
      ],
      "value": 689
    },
    {
      "range": [
        90,
        100
      ],
      "value": 0
    },
    {
      "range": [
        100,
        null
      ],
      "value": 0
    }
  ],
  "end": 1627055181,
  "metric": "capacity",
  "start": 1626968781,
  "x_label": "available-bandwidth(%)",
  "y_label": "seconds"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesSleScopeIdMetricMetricHistogram401ErrorException`](../../doc/models/api-v1-sites-sle-scope-id-metric-metric-histogram-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesSleScopeIdMetricMetricHistogram403ErrorException`](../../doc/models/api-v1-sites-sle-scope-id-metric-metric-histogram-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesSleScopeIdMetricMetricHistogram404ErrorException`](../../doc/models/api-v1-sites-sle-scope-id-metric-metric-histogram-404-error-exception.md) |


# Get Site Sle Impact Summary

Get impact summary counts optionally filtered by classifier and failure type

* Wireless SLE Fields: `wlan`, `device_type`, `device_os` ,`band`, `ap`, `server`, `mxedge`
* Wired SLE Fields: `switch`, `client`, `vlan`, `interface`, `chassis`
* WAN SLE Fields: `gateway`, `client`, `interface`, `chassis`, `peer_path`, `gateway_zones`

```python
def get_site_sle_impact_summary(self,
                               site_id,
                               scope,
                               scope_id,
                               metric,
                               start=0,
                               end=0,
                               duration='1d',
                               fields=None,
                               classifier=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `scope` | [`Scope2Enum`](../../doc/models/scope-2-enum.md) | Template, Required | - |
| `scope_id` | `string` | Template, Required | * site_id if `scope`==`site`<br>* device_id if `scope`==`ap`, `scope`==`switch` or `scope`==`gateway`<br>* mac if `scope`==`client` |
| `metric` | `string` | Template, Required | values from /api/v1/sites/{site_id}/sle/{scope}/{scope_id}/metrics |
| `start` | `int` | Query, Optional | **Default**: `0`<br>**Constraints**: `>= 0` |
| `end` | `int` | Query, Optional | **Default**: `0`<br>**Constraints**: `>= 0` |
| `duration` | `string` | Query, Optional | For historical stats and/or logs where time range is needed, you can specify the time range in a few different ways:<br><br>* ?start=1430000000&end=1430864000	specify the start / end<br>* ?end=1430864000&duration=1d	specify end time and duration<br>* ?duration=1d	specify duration, end will be now() in seconds<br>**Default**: `'1d'` |
| `fields` | [`FieldsEnum`](../../doc/models/fields-enum.md) | Query, Optional | - |
| `classifier` | `string` | Query, Optional | - |

## Response Type

[`SleImpactSummary`](../../doc/models/sle-impact-summary.md)

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

scope = Scope2Enum.SWITCH

scope_id = 'scope_id0'

metric = 'metric8'

start = 0

end = 0

duration = '10m'

result = sites_sl_es_controller.get_site_sle_impact_summary(
    site_id,
    scope,
    scope_id,
    metric,
    start,
    end,
    duration
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "ap": [
    {
      "ap_mac": "5c5b3550bd2e",
      "degraded": 1486,
      "duration": 0,
      "name": "ap43-off.lab",
      "total": 27406
    },
    {
      "ap_mac": "d420b083e17a",
      "degraded": 3,
      "duration": 0,
      "name": "ap33-ent.lab",
      "total": 1193
    }
  ],
  "band": [
    {
      "band": "24",
      "degraded": 1410,
      "duration": 0,
      "name": "24",
      "total": 28536
    },
    {
      "band": "5",
      "degraded": 78,
      "duration": 0,
      "name": "5",
      "total": 4679
    }
  ],
  "classifier": "",
  "device_os": [
    {
      "degraded": 1329,
      "device_os": "",
      "duration": 0,
      "name": "unknown",
      "total": 27165
    },
    {
      "degraded": 81,
      "device_os": "Linux",
      "duration": 0,
      "name": "Linux",
      "total": 1437
    },
    {
      "degraded": 36,
      "device_os": "Android 11",
      "duration": 0,
      "name": "Android 11",
      "total": 761
    },
    {
      "degraded": 39,
      "device_os": "14.6",
      "duration": 0,
      "name": "14.6",
      "total": 2413
    },
    {
      "degraded": 2,
      "device_os": "Catalina",
      "duration": 0,
      "name": "Catalina",
      "total": 1438
    }
  ],
  "device_type": [
    {
      "degraded": 1410,
      "device_type": "",
      "duration": 0,
      "name": "unknown",
      "total": 28603
    },
    {
      "degraded": 2,
      "device_type": "iPhone",
      "duration": 0,
      "name": "iPhone",
      "total": 1263
    },
    {
      "degraded": 36,
      "device_type": "OnePlus",
      "duration": 0,
      "name": "OnePlus",
      "total": 761
    },
    {
      "degraded": 37,
      "device_type": "iPad",
      "duration": 0,
      "name": "iPad",
      "total": 1150
    },
    {
      "degraded": 2,
      "device_type": "Mac",
      "duration": 0,
      "name": "Mac",
      "total": 1438
    }
  ],
  "end": 1627312734,
  "failure": "",
  "metric": "capacity",
  "start": 1627226334,
  "wlan": [
    {
      "degraded": 37,
      "duration": 0,
      "name": "MlN.ADM",
      "total": 1150,
      "wlan_id": "ba3f85fc-ba48-4d8f-ad89-152e5c42db18"
    },
    {
      "degraded": 1410,
      "duration": 0,
      "name": "MlN",
      "total": 28603,
      "wlan_id": "649a2336-b1e0-47bd-961c-f637dbe50e7b"
    },
    {
      "degraded": 41,
      "duration": 0,
      "name": "MlN.1X",
      "total": 3462,
      "wlan_id": "a937da77-fe3c-4784-86c4-f2134d7b1483"
    }
  ]
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesSleScopeIdMetricMetricImpactSummary401ErrorException`](../../doc/models/api-v1-sites-sle-scope-id-metric-metric-impact-summary-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesSleScopeIdMetricMetricImpactSummary403ErrorException`](../../doc/models/api-v1-sites-sle-scope-id-metric-metric-impact-summary-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesSleScopeIdMetricMetricImpactSummary404ErrorException`](../../doc/models/api-v1-sites-sle-scope-id-metric-metric-impact-summary-404-error-exception.md) |


# Get Site Sle Impacted Applications

For WAN SLEs. Get list of impacted interfaces optionally filtered by classifier and failure type

```python
def get_site_sle_impacted_applications(self,
                                      site_id,
                                      scope,
                                      scope_id,
                                      metric,
                                      start=0,
                                      end=0,
                                      duration='1d',
                                      classifier=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `scope` | [`Scope6Enum`](../../doc/models/scope-6-enum.md) | Template, Required | - |
| `scope_id` | `uuid\|string` | Template, Required | - |
| `metric` | `string` | Template, Required | values from /api/v1/sites/{site_id}/sle/{scope}/{scope_id}/metrics |
| `start` | `int` | Query, Optional | **Default**: `0`<br>**Constraints**: `>= 0` |
| `end` | `int` | Query, Optional | **Default**: `0`<br>**Constraints**: `>= 0` |
| `duration` | `string` | Query, Optional | For historical stats and/or logs where time range is needed, you can specify the time range in a few different ways:<br><br>* ?start=1430000000&end=1430864000	specify the start / end<br>* ?end=1430864000&duration=1d	specify end time and duration<br>* ?duration=1d	specify duration, end will be now() in seconds<br>**Default**: `'1d'` |
| `classifier` | `string` | Query, Optional | - |

## Response Type

[`SleImpactedApplications`](../../doc/models/sle-impacted-applications.md)

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

scope = Scope6Enum.GATEWAY

scope_id = '000008e8-0000-0000-0000-000000000000'

metric = 'metric8'

start = 0

end = 0

duration = '10m'

result = sites_sl_es_controller.get_site_sle_impacted_applications(
    site_id,
    scope,
    scope_id,
    metric,
    start,
    end,
    duration
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "apps": [
    {
      "app": "ZOOM",
      "degraded": 371103,
      "duration": 0,
      "name": "ZOOM",
      "threshold": 173,
      "total": 1771274
    }
  ],
  "classifier": "",
  "end": 1668760746,
  "failure": "",
  "limit": "1000",
  "metric": "application-health",
  "page": 1,
  "start": 1668121200,
  "total_count": 1
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesSleScopeIdMetricMetricImpactedApplications401ErrorException`](../../doc/models/api-v1-sites-sle-scope-id-metric-metric-impacted-applications-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesSleScopeIdMetricMetricImpactedApplications403ErrorException`](../../doc/models/api-v1-sites-sle-scope-id-metric-metric-impacted-applications-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesSleScopeIdMetricMetricImpactedApplications404ErrorException`](../../doc/models/api-v1-sites-sle-scope-id-metric-metric-impacted-applications-404-error-exception.md) |


# Get Site Sle Impacted Aps

For Wireless SLEs. Get list of impacted APs optionally filtered by classifier and failure type

```python
def get_site_sle_impacted_aps(self,
                             site_id,
                             scope,
                             scope_id,
                             metric,
                             start=0,
                             end=0,
                             duration='1d',
                             classifier=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `scope` | [`Scope7Enum`](../../doc/models/scope-7-enum.md) | Template, Required | - |
| `scope_id` | `uuid\|string` | Template, Required | - |
| `metric` | `string` | Template, Required | values from /api/v1/sites/{site_id}/sle/{scope}/{scope_id}/metrics |
| `start` | `int` | Query, Optional | **Default**: `0`<br>**Constraints**: `>= 0` |
| `end` | `int` | Query, Optional | **Default**: `0`<br>**Constraints**: `>= 0` |
| `duration` | `string` | Query, Optional | For historical stats and/or logs where time range is needed, you can specify the time range in a few different ways:<br><br>* ?start=1430000000&end=1430864000	specify the start / end<br>* ?end=1430864000&duration=1d	specify end time and duration<br>* ?duration=1d	specify duration, end will be now() in seconds<br>**Default**: `'1d'` |
| `classifier` | `string` | Query, Optional | - |

## Response Type

[`SleImpactedAps`](../../doc/models/sle-impacted-aps.md)

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

scope = Scope7Enum.SITE

scope_id = '000008e8-0000-0000-0000-000000000000'

metric = 'metric8'

start = 0

end = 0

duration = '10m'

result = sites_sl_es_controller.get_site_sle_impacted_aps(
    site_id,
    scope,
    scope_id,
    metric,
    start,
    end,
    duration
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "aps": [
    {
      "ap_mac": "5c5b35500000",
      "degraded": 1486,
      "duration": 0,
      "name": "ap43.lab",
      "total": 27377
    },
    {
      "ap_mac": "d420b0830000",
      "degraded": 3,
      "duration": 0,
      "name": "ap33.lab",
      "total": 1189
    }
  ],
  "classifier": "",
  "end": 1627313016,
  "failure": "",
  "limit": 1000,
  "metric": "capacity",
  "page": 1,
  "start": 1627226616,
  "total_count": 2
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesSleScopeIdMetricMetricImpactedAps401ErrorException`](../../doc/models/api-v1-sites-sle-scope-id-metric-metric-impacted-aps-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesSleScopeIdMetricMetricImpactedAps403ErrorException`](../../doc/models/api-v1-sites-sle-scope-id-metric-metric-impacted-aps-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesSleScopeIdMetricMetricImpactedAps404ErrorException`](../../doc/models/api-v1-sites-sle-scope-id-metric-metric-impacted-aps-404-error-exception.md) |


# Get Site Sle Impacted Chassis

For Wired and WAN SLEs. Get list of impacted interfaces optionally filtered by classifier and failure type

```python
def get_site_sle_impacted_chassis(self,
                                 site_id,
                                 scope,
                                 scope_id,
                                 metric,
                                 start=0,
                                 end=0,
                                 duration='1d',
                                 classifier=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `scope` | [`Scope6Enum`](../../doc/models/scope-6-enum.md) | Template, Required | - |
| `scope_id` | `uuid\|string` | Template, Required | - |
| `metric` | `string` | Template, Required | values from /api/v1/sites/{site_id}/sle/{scope}/{scope_id}/metrics |
| `start` | `int` | Query, Optional | **Default**: `0`<br>**Constraints**: `>= 0` |
| `end` | `int` | Query, Optional | **Default**: `0`<br>**Constraints**: `>= 0` |
| `duration` | `string` | Query, Optional | For historical stats and/or logs where time range is needed, you can specify the time range in a few different ways:<br><br>* ?start=1430000000&end=1430864000	specify the start / end<br>* ?end=1430864000&duration=1d	specify end time and duration<br>* ?duration=1d	specify duration, end will be now() in seconds<br>**Default**: `'1d'` |
| `classifier` | `string` | Query, Optional | - |

## Response Type

[`SleImpactedChassis`](../../doc/models/sle-impacted-chassis.md)

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

scope = Scope6Enum.GATEWAY

scope_id = '000008e8-0000-0000-0000-000000000000'

metric = 'metric8'

start = 0

end = 0

duration = '10m'

result = sites_sl_es_controller.get_site_sle_impacted_chassis(
    site_id,
    scope,
    scope_id,
    metric,
    start,
    end,
    duration
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "chassis": [
    {
      "chassis": "1",
      "degraded": 12.283334,
      "duration": 13655.167,
      "role": "master",
      "switch_mac": "d0dd49012345",
      "switch_name": "test-chassis",
      "total": 13655.167
    }
  ],
  "classifier": "",
  "end": 1668760643,
  "failure": "",
  "limit": 1000,
  "metric": "switch-health",
  "page": 1,
  "start": 1668121200,
  "total_count": 1
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesSleScopeIdMetricMetricImpactedChassis401ErrorException`](../../doc/models/api-v1-sites-sle-scope-id-metric-metric-impacted-chassis-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesSleScopeIdMetricMetricImpactedChassis403ErrorException`](../../doc/models/api-v1-sites-sle-scope-id-metric-metric-impacted-chassis-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesSleScopeIdMetricMetricImpactedChassis404ErrorException`](../../doc/models/api-v1-sites-sle-scope-id-metric-metric-impacted-chassis-404-error-exception.md) |


# Get Site Sle Impacted Wired Clients

For Wired SLEs. Get list of impacted interfaces optionally filtered by classifier and failure type

```python
def get_site_sle_impacted_wired_clients(self,
                                       site_id,
                                       scope,
                                       scope_id,
                                       metric,
                                       start=0,
                                       end=0,
                                       duration='1d',
                                       classifier=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `scope` | [`Scope6Enum`](../../doc/models/scope-6-enum.md) | Template, Required | - |
| `scope_id` | `uuid\|string` | Template, Required | - |
| `metric` | `string` | Template, Required | values from /api/v1/sites/{site_id}/sle/{scope}/{scope_id}/metrics |
| `start` | `int` | Query, Optional | **Default**: `0`<br>**Constraints**: `>= 0` |
| `end` | `int` | Query, Optional | **Default**: `0`<br>**Constraints**: `>= 0` |
| `duration` | `string` | Query, Optional | For historical stats and/or logs where time range is needed, you can specify the time range in a few different ways:<br><br>* ?start=1430000000&end=1430864000	specify the start / end<br>* ?end=1430864000&duration=1d	specify end time and duration<br>* ?duration=1d	specify duration, end will be now() in seconds<br>**Default**: `'1d'` |
| `classifier` | `string` | Query, Optional | - |

## Response Type

[`SleImpactedClients`](../../doc/models/sle-impacted-clients.md)

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

scope = Scope6Enum.GATEWAY

scope_id = '000008e8-0000-0000-0000-000000000000'

metric = 'metric8'

start = 0

end = 0

duration = '10m'

result = sites_sl_es_controller.get_site_sle_impacted_wired_clients(
    site_id,
    scope,
    scope_id,
    metric,
    start,
    end,
    duration
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "classifier": "",
  "clients": [
    {
      "degraded": 40,
      "duration": 11014,
      "mac": "001122334455",
      "name": "test-device",
      "switches": [
        {
          "interfaces": [
            "ge-0/0/6"
          ],
          "switch_mac": "2c2131001122",
          "switch_name": "test-ex"
        }
      ],
      "total": 11014
    }
  ],
  "end": 1668760198,
  "failure": "",
  "limit": 1000,
  "metric": "switch-throughput",
  "page": 1,
  "start": 1668726000,
  "total_count": 1
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesSleScopeIdMetricMetricImpactedClients401ErrorException`](../../doc/models/api-v1-sites-sle-scope-id-metric-metric-impacted-clients-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesSleScopeIdMetricMetricImpactedClients403ErrorException`](../../doc/models/api-v1-sites-sle-scope-id-metric-metric-impacted-clients-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesSleScopeIdMetricMetricImpactedClients404ErrorException`](../../doc/models/api-v1-sites-sle-scope-id-metric-metric-impacted-clients-404-error-exception.md) |


# Get Site Sle Impacted Gateways

For WAN SLEs. Get list of impacted interfaces optionally filtered by classifier and failure type

```python
def get_site_sle_impacted_gateways(self,
                                  site_id,
                                  scope,
                                  scope_id,
                                  metric,
                                  start=0,
                                  end=0,
                                  duration='1d',
                                  classifier=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `scope` | [`Scope7Enum`](../../doc/models/scope-7-enum.md) | Template, Required | - |
| `scope_id` | `uuid\|string` | Template, Required | - |
| `metric` | `string` | Template, Required | values from /api/v1/sites/{site_id}/sle/{scope}/{scope_id}/metrics |
| `start` | `int` | Query, Optional | **Default**: `0`<br>**Constraints**: `>= 0` |
| `end` | `int` | Query, Optional | **Default**: `0`<br>**Constraints**: `>= 0` |
| `duration` | `string` | Query, Optional | For historical stats and/or logs where time range is needed, you can specify the time range in a few different ways:<br><br>* ?start=1430000000&end=1430864000	specify the start / end<br>* ?end=1430864000&duration=1d	specify end time and duration<br>* ?duration=1d	specify duration, end will be now() in seconds<br>**Default**: `'1d'` |
| `classifier` | `string` | Query, Optional | - |

## Response Type

[`SleImpactedGateways`](../../doc/models/sle-impacted-gateways.md)

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

scope = Scope7Enum.SITE

scope_id = '000008e8-0000-0000-0000-000000000000'

metric = 'metric8'

start = 0

end = 0

duration = '10m'

result = sites_sl_es_controller.get_site_sle_impacted_gateways(
    site_id,
    scope,
    scope_id,
    metric,
    start,
    end,
    duration
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "classifier": "",
  "end": 1668760746,
  "failure": "",
  "gateways": [
    {
      "degraded": 758573.1,
      "duration": 2770997,
      "gateway_mac": "fc3342001122",
      "gateway_model": "SRX320",
      "gateway_version": "20.4R1.12",
      "name": "test-SRX",
      "total": 2770997
    }
  ],
  "limit": 1000,
  "metric": "application-health",
  "page": 1,
  "start": 1668121200,
  "total_count": 1
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesSleScopeIdMetricMetricImpactedGateways401ErrorException`](../../doc/models/api-v1-sites-sle-scope-id-metric-metric-impacted-gateways-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesSleScopeIdMetricMetricImpactedGateways403ErrorException`](../../doc/models/api-v1-sites-sle-scope-id-metric-metric-impacted-gateways-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesSleScopeIdMetricMetricImpactedGateways404ErrorException`](../../doc/models/api-v1-sites-sle-scope-id-metric-metric-impacted-gateways-404-error-exception.md) |


# Get Site Sle Impacted Interfaces

For Wired and WAN SLEs. Get list of impacted interfaces optionally filtered by classifier and failure type

```python
def get_site_sle_impacted_interfaces(self,
                                    site_id,
                                    scope,
                                    scope_id,
                                    metric,
                                    start=0,
                                    end=0,
                                    duration='1d',
                                    classifier=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `scope` | [`Scope6Enum`](../../doc/models/scope-6-enum.md) | Template, Required | - |
| `scope_id` | `uuid\|string` | Template, Required | - |
| `metric` | `string` | Template, Required | values from /api/v1/sites/{site_id}/sle/{scope}/{scope_id}/metrics |
| `start` | `int` | Query, Optional | **Default**: `0`<br>**Constraints**: `>= 0` |
| `end` | `int` | Query, Optional | **Default**: `0`<br>**Constraints**: `>= 0` |
| `duration` | `string` | Query, Optional | For historical stats and/or logs where time range is needed, you can specify the time range in a few different ways:<br><br>* ?start=1430000000&end=1430864000	specify the start / end<br>* ?end=1430864000&duration=1d	specify end time and duration<br>* ?duration=1d	specify duration, end will be now() in seconds<br>**Default**: `'1d'` |
| `classifier` | `string` | Query, Optional | - |

## Response Type

[`SleImpactedInterfaces`](../../doc/models/sle-impacted-interfaces.md)

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

scope = Scope6Enum.GATEWAY

scope_id = '000008e8-0000-0000-0000-000000000000'

metric = 'metric8'

start = 0

end = 0

duration = '10m'

result = sites_sl_es_controller.get_site_sle_impacted_interfaces(
    site_id,
    scope,
    scope_id,
    metric,
    start,
    end,
    duration
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "classifier": "",
  "end": 1668760198,
  "failure": "",
  "interfaces": [
    {
      "degraded": 11.583333,
      "duration": 765.4667,
      "interface_name": "ge-0/0/10",
      "switch_mac": "2c2131001122",
      "switch_name": "test-ex",
      "total": 765.4667
    },
    {
      "degraded": 191.08333,
      "duration": 13775.35,
      "interface_name": "xe-0/1/0",
      "switch_mac": "2c2131001122",
      "switch_name": "test-ex",
      "total": 13775.35
    }
  ],
  "limit": 1000,
  "metric": "switch-throughput",
  "page": 1,
  "start": 1668726000,
  "total_count": 5
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesSleScopeIdMetricMetricImpactedInterfaces401ErrorException`](../../doc/models/api-v1-sites-sle-scope-id-metric-metric-impacted-interfaces-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesSleScopeIdMetricMetricImpactedInterfaces403ErrorException`](../../doc/models/api-v1-sites-sle-scope-id-metric-metric-impacted-interfaces-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesSleScopeIdMetricMetricImpactedInterfaces404ErrorException`](../../doc/models/api-v1-sites-sle-scope-id-metric-metric-impacted-interfaces-404-error-exception.md) |


# Get Site Sle Impacted Switches

For Wired SLEs. Get list of impacted switches optionally filtered by classifier and failure type

```python
def get_site_sle_impacted_switches(self,
                                  site_id,
                                  scope,
                                  scope_id,
                                  metric,
                                  start=0,
                                  end=0,
                                  duration='1d',
                                  classifier=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `scope` | [`Scope7Enum`](../../doc/models/scope-7-enum.md) | Template, Required | - |
| `scope_id` | `uuid\|string` | Template, Required | - |
| `metric` | `string` | Template, Required | values from /api/v1/sites/{site_id}/sle/{scope}/{scope_id}/metrics |
| `start` | `int` | Query, Optional | **Default**: `0`<br>**Constraints**: `>= 0` |
| `end` | `int` | Query, Optional | **Default**: `0`<br>**Constraints**: `>= 0` |
| `duration` | `string` | Query, Optional | For historical stats and/or logs where time range is needed, you can specify the time range in a few different ways:<br><br>* ?start=1430000000&end=1430864000	specify the start / end<br>* ?end=1430864000&duration=1d	specify end time and duration<br>* ?duration=1d	specify duration, end will be now() in seconds<br>**Default**: `'1d'` |
| `classifier` | `string` | Query, Optional | - |

## Response Type

[`SleImpactedSwitches`](../../doc/models/sle-impacted-switches.md)

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

scope = Scope7Enum.SITE

scope_id = '000008e8-0000-0000-0000-000000000000'

metric = 'metric8'

start = 0

end = 0

duration = '10m'

result = sites_sl_es_controller.get_site_sle_impacted_switches(
    site_id,
    scope,
    scope_id,
    metric,
    start,
    end,
    duration
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "classifier": "",
  "end": 1668760198,
  "failure": "",
  "limit": 1000,
  "metric": "switch-throughput",
  "page": 1,
  "start": 1668726000,
  "switches": [
    {
      "degraded": 109.88333,
      "duration": 5753.75,
      "interface": [
        "ge-0/0/11",
        "xe-0/1/0"
      ],
      "name": "test-ex",
      "switch_mac": "2c2131001122",
      "switch_model": "EX2300-C-12P",
      "switch_version": "20.4R3-S3.4",
      "total": 5753.75
    }
  ],
  "total_count": 1
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesSleScopeIdMetricMetricImpactedSwitches401ErrorException`](../../doc/models/api-v1-sites-sle-scope-id-metric-metric-impacted-switches-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesSleScopeIdMetricMetricImpactedSwitches403ErrorException`](../../doc/models/api-v1-sites-sle-scope-id-metric-metric-impacted-switches-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesSleScopeIdMetricMetricImpactedSwitches404ErrorException`](../../doc/models/api-v1-sites-sle-scope-id-metric-metric-impacted-switches-404-error-exception.md) |


# Get Site Sle Impacted Wireless Clients

For Wireless SLEs. Get list of impacted wireless users optionally filtered by classifier and failure type

```python
def get_site_sle_impacted_wireless_clients(self,
                                          site_id,
                                          scope,
                                          scope_id,
                                          metric,
                                          start=0,
                                          end=0,
                                          duration='1d',
                                          classifier=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `scope` | [`Scope13Enum`](../../doc/models/scope-13-enum.md) | Template, Required | - |
| `scope_id` | `uuid\|string` | Template, Required | - |
| `metric` | `string` | Template, Required | values from /api/v1/sites/{site_id}/sle/{scope}/{scope_id}/metrics |
| `start` | `int` | Query, Optional | **Default**: `0`<br>**Constraints**: `>= 0` |
| `end` | `int` | Query, Optional | **Default**: `0`<br>**Constraints**: `>= 0` |
| `duration` | `string` | Query, Optional | For historical stats and/or logs where time range is needed, you can specify the time range in a few different ways:<br><br>* ?start=1430000000&end=1430864000	specify the start / end<br>* ?end=1430864000&duration=1d	specify end time and duration<br>* ?duration=1d	specify duration, end will be now() in seconds<br>**Default**: `'1d'` |
| `classifier` | `string` | Query, Optional | - |

## Response Type

[`SleImpactedUsers`](../../doc/models/sle-impacted-users.md)

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

scope = Scope13Enum.SITE

scope_id = '000008e8-0000-0000-0000-000000000000'

metric = 'metric8'

start = 0

end = 0

duration = '10m'

result = sites_sl_es_controller.get_site_sle_impacted_wireless_clients(
    site_id,
    scope,
    scope_id,
    metric,
    start,
    end,
    duration
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "classifier": "",
  "end": 1627313103,
  "failure": "",
  "limit": 1000,
  "metric": "capacity",
  "page": 1,
  "start": 1627226703,
  "total_count": 21,
  "users": [
    {
      "ap_mac": "d420b0830000",
      "ap_name": "ap33.lab",
      "degraded": 2,
      "device_os": "14.6",
      "device_type": "iPhone",
      "duration": 1270,
      "mac": "dc080f360000",
      "name": "aPhone-20973",
      "ssid": "lab.1X",
      "total": 1270,
      "wlan_id": "a937da77-0000-0000-0000-f2134d7b1483"
    },
    {
      "ap_mac": "5c5b35500000",
      "ap_name": "ap43.lab",
      "degraded": 36,
      "device_os": "Android 11",
      "device_type": "OnePlus",
      "duration": 767,
      "mac": "4c4feedc0000",
      "name": "OnePlus-8",
      "ssid": "lab.1X",
      "total": 767,
      "wlan_id": "a937da77-0000-0000-0000-f2134d7b1483"
    },
    {
      "ap_mac": "5c5b35500000",
      "ap_name": "ap43.lab",
      "degraded": 2,
      "device_os": "Catalina",
      "device_type": "Mac",
      "duration": 1405,
      "mac": "a483e7390000",
      "name": "tmunzer-mbp",
      "ssid": "lab.1X",
      "total": 1405,
      "wlan_id": "a937da77-0000-0000-0000-f2134d7b1483"
    },
    {
      "ap_mac": "5c5b35500000",
      "ap_name": "ap43.lab",
      "degraded": 81,
      "device_os": "Linux",
      "device_type": "unknown",
      "duration": 1403,
      "mac": "5caafd0d0000",
      "name": "SonosZP",
      "ssid": "lab",
      "total": 1403,
      "wlan_id": "649a2336-0000-0000-0000-f637dbe50e7b"
    }
  ]
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesSleScopeIdMetricMetricImpactedUsers401ErrorException`](../../doc/models/api-v1-sites-sle-scope-id-metric-metric-impacted-users-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesSleScopeIdMetricMetricImpactedUsers403ErrorException`](../../doc/models/api-v1-sites-sle-scope-id-metric-metric-impacted-users-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesSleScopeIdMetricMetricImpactedUsers404ErrorException`](../../doc/models/api-v1-sites-sle-scope-id-metric-metric-impacted-users-404-error-exception.md) |


# Get Site Sle Summary

Get the summary for the SLE metric

```python
def get_site_sle_summary(self,
                        site_id,
                        scope,
                        scope_id,
                        metric,
                        start=0,
                        end=0,
                        duration='1d')
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `scope` | [`Scope2Enum`](../../doc/models/scope-2-enum.md) | Template, Required | - |
| `scope_id` | `string` | Template, Required | * site_id if `scope`==`site`<br>* device_id if `scope`==`ap`, `scope`==`switch` or `scope`==`gateway`<br>* mac if `scope`==`client` |
| `metric` | `string` | Template, Required | values from /api/v1/sites/{site_id}/sle/{scope}/{scope_id}/metrics |
| `start` | `int` | Query, Optional | **Default**: `0`<br>**Constraints**: `>= 0` |
| `end` | `int` | Query, Optional | **Default**: `0`<br>**Constraints**: `>= 0` |
| `duration` | `string` | Query, Optional | For historical stats and/or logs where time range is needed, you can specify the time range in a few different ways:<br><br>* ?start=1430000000&end=1430864000	specify the start / end<br>* ?end=1430864000&duration=1d	specify end time and duration<br>* ?duration=1d	specify duration, end will be now() in seconds<br>**Default**: `'1d'` |

## Response Type

[`SleSummary`](../../doc/models/sle-summary.md)

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

scope = Scope2Enum.SWITCH

scope_id = 'scope_id0'

metric = 'metric8'

start = 0

end = 0

duration = '10m'

result = sites_sl_es_controller.get_site_sle_summary(
    site_id,
    scope,
    scope_id,
    metric,
    start,
    end,
    duration
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "classifiers": [
    {
      "impact": {
        "num_aps": 1,
        "num_users": 4,
        "total_aps": 3,
        "total_users": 26
      },
      "interval": 3600,
      "name": "client-count",
      "samples": {
        "degraded": [
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          5.8,
          0,
          0,
          0,
          4.65,
          0,
          7.55,
          47.55,
          13.266666
        ],
        "duration": [
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          5.8,
          0,
          0,
          0,
          4.65,
          0,
          7.55,
          47.55,
          13.266666
        ],
        "total": [
          1302.3,
          1289.0167,
          1396.3167,
          1423.6666,
          1439.2167,
          1414.7,
          1361.0834,
          1371.5834,
          1372.0667,
          1339.1,
          1374.3667,
          1369.9,
          1352.4833,
          1382.8,
          1426.7167,
          1425.6333,
          1403.9333,
          1420.75,
          1416.8334,
          1437.3334,
          1425.1,
          1485.3667,
          1426.4333,
          289.83334
        ]
      },
      "x_label": "seconds",
      "y_label": "user-minutes"
    },
    {
      "impact": {
        "num_aps": 2,
        "num_users": 17,
        "total_aps": 3,
        "total_users": 26
      },
      "interval": 3600,
      "name": "wifi-interference",
      "samples": {
        "degraded": [
          0,
          0,
          210.03334,
          3.1333334,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          102.5,
          108.03333,
          0,
          0,
          201.9,
          566.48334,
          135.63333,
          0
        ],
        "duration": [
          0,
          0,
          210.03334,
          3.1333334,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          102.5,
          108.03333,
          0,
          0,
          201.9,
          566.48334,
          135.63333,
          0
        ],
        "total": [
          1302.3,
          1289.0167,
          1396.3167,
          1423.6666,
          1439.2167,
          1414.7,
          1361.0834,
          1371.5834,
          1372.0667,
          1339.1,
          1374.3667,
          1369.9,
          1352.4833,
          1382.8,
          1426.7167,
          1425.6333,
          1403.9333,
          1420.75,
          1416.8334,
          1437.3334,
          1425.1,
          1485.3667,
          1426.4333,
          289.83334
        ]
      },
      "x_label": "seconds",
      "y_label": "user-minutes"
    },
    {
      "impact": {
        "num_aps": 0,
        "num_users": 0,
        "total_aps": 3,
        "total_users": 26
      },
      "interval": 3600,
      "name": "client-usage",
      "samples": {
        "degraded": [
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0
        ],
        "duration": [
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0
        ],
        "total": [
          1302.3,
          1289.0167,
          1396.3167,
          1423.6666,
          1439.2167,
          1414.7,
          1361.0834,
          1371.5834,
          1372.0667,
          1339.1,
          1374.3667,
          1369.9,
          1352.4833,
          1382.8,
          1426.7167,
          1425.6333,
          1403.9333,
          1420.75,
          1416.8334,
          1437.3334,
          1425.1,
          1485.3667,
          1426.4333,
          289.83334
        ]
      },
      "x_label": "seconds",
      "y_label": "user-minutes"
    },
    {
      "impact": {
        "num_aps": 1,
        "num_users": 17,
        "total_aps": 3,
        "total_users": 26
      },
      "interval": 3600,
      "name": "non-wifi-interference",
      "samples": {
        "degraded": [
          0,
          0,
          0,
          0,
          16.65,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          31.15,
          17.616667,
          17.85,
          0,
          0,
          0,
          0
        ],
        "duration": [
          0,
          0,
          0,
          0,
          16.65,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          31.15,
          17.616667,
          17.85,
          0,
          0,
          0,
          0
        ],
        "total": [
          1302.3,
          1289.0167,
          1396.3167,
          1423.6666,
          1439.2167,
          1414.7,
          1361.0834,
          1371.5834,
          1372.0667,
          1339.1,
          1374.3667,
          1369.9,
          1352.4833,
          1382.8,
          1426.7167,
          1425.6333,
          1403.9333,
          1420.75,
          1416.8334,
          1437.3334,
          1425.1,
          1485.3667,
          1426.4333,
          289.83334
        ]
      },
      "x_label": "seconds",
      "y_label": "user-minutes"
    }
  ],
  "end": 1627312606,
  "events": [],
  "impact": {
    "num_aps": 2,
    "num_users": 21,
    "total_aps": 3,
    "total_users": 26
  },
  "sle": {
    "interval": 3600,
    "name": "capacity",
    "samples": {
      "degraded": [
        0,
        0,
        210.03334,
        3.1333334,
        16.65,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        5.8,
        102.5,
        139.18333,
        17.616667,
        22.5,
        201.9,
        574.0333,
        183.18333,
        13.266666
      ],
      "total": [
        1302.3,
        1289.0167,
        1396.3167,
        1423.6666,
        1439.2167,
        1414.7,
        1361.0834,
        1371.5834,
        1372.0667,
        1339.1,
        1374.3667,
        1369.9,
        1352.4833,
        1382.8,
        1426.7167,
        1425.6333,
        1403.9333,
        1420.75,
        1416.8334,
        1437.3334,
        1425.1,
        1485.3667,
        1426.4333,
        289.83334
      ],
      "value": [
        0.6764934,
        0.6783766,
        0.641645,
        0.6934629,
        0.68676674,
        0.6834809,
        0.6961604,
        0.6979584,
        0.7033722,
        0.70410794,
        0.7025278,
        0.70305353,
        0.70292175,
        0.7009334,
        0.69344264,
        0.68596864,
        0.5952168,
        0.62183666,
        0.68161446,
        0.65352744,
        0.6183489,
        0.54178274,
        0.6044712,
        0.66845906
      ]
    },
    "x_label": "seconds",
    "y_label": "%"
  },
  "start": 1627226206
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesSleScopeIdMetricMetricSummary401ErrorException`](../../doc/models/api-v1-sites-sle-scope-id-metric-metric-summary-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesSleScopeIdMetricMetricSummary403ErrorException`](../../doc/models/api-v1-sites-sle-scope-id-metric-metric-summary-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesSleScopeIdMetricMetricSummary404ErrorException`](../../doc/models/api-v1-sites-sle-scope-id-metric-metric-summary-404-error-exception.md) |


# Get Site Sle Threshold

Get the SLE threshold

```python
def get_site_sle_threshold(self,
                          site_id,
                          scope,
                          scope_id,
                          metric)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `scope` | [`Scope2Enum`](../../doc/models/scope-2-enum.md) | Template, Required | - |
| `scope_id` | `string` | Template, Required | * site_id if `scope`==`site`<br>* device_id if `scope`==`ap`, `scope`==`switch` or `scope`==`gateway`<br>* mac if `scope`==`client` |
| `metric` | `string` | Template, Required | values from /api/v1/sites/{site_id}/sle/{scope}/{scope_id}/metrics |

## Response Type

[`SleThreshold`](../../doc/models/sle-threshold.md)

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

scope = Scope2Enum.SWITCH

scope_id = 'scope_id0'

metric = 'metric8'

result = sites_sl_es_controller.get_site_sle_threshold(
    site_id,
    scope,
    scope_id,
    metric
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "default": -72,
  "direction": "left",
  "maximum": -60,
  "metric": "coverage",
  "minimum": -90,
  "threshold": "-66",
  "units": "dBm"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesSleScopeIdMetricMetricThreshold401ErrorException`](../../doc/models/api-v1-sites-sle-scope-id-metric-metric-threshold-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesSleScopeIdMetricMetricThreshold403ErrorException`](../../doc/models/api-v1-sites-sle-scope-id-metric-metric-threshold-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesSleScopeIdMetricMetricThreshold404ErrorException`](../../doc/models/api-v1-sites-sle-scope-id-metric-metric-threshold-404-error-exception.md) |


# Replace Site Sle Threshold

Replace the SLE threshold

```python
def replace_site_sle_threshold(self,
                              site_id,
                              scope,
                              scope_id,
                              metric,
                              body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `scope` | [`Scope2Enum`](../../doc/models/scope-2-enum.md) | Template, Required | - |
| `scope_id` | `string` | Template, Required | * site_id if `scope`==`site`<br>* device_id if `scope`==`ap`, `scope`==`switch` or `scope`==`gateway`<br>* mac if `scope`==`client` |
| `metric` | `string` | Template, Required | values from /api/v1/sites/{site_id}/sle/{scope}/{scope_id}/metrics |
| `body` | [`SleThreshold`](../../doc/models/sle-threshold.md) | Body, Optional | - |

## Response Type

[`SleThreshold`](../../doc/models/sle-threshold.md)

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

scope = Scope2Enum.SWITCH

scope_id = 'scope_id0'

metric = 'metric8'

body = SleThreshold(
    maximum=-60,
    minimum=-90
)

result = sites_sl_es_controller.replace_site_sle_threshold(
    site_id,
    scope,
    scope_id,
    metric,
    body
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "default": -72,
  "direction": "left",
  "maximum": -60,
  "metric": "coverage",
  "minimum": -90,
  "threshold": "-66",
  "units": "dBm"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesSleScopeIdMetricMetricThreshold401ErrorException`](../../doc/models/api-v1-sites-sle-scope-id-metric-metric-threshold-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesSleScopeIdMetricMetricThreshold403ErrorException`](../../doc/models/api-v1-sites-sle-scope-id-metric-metric-threshold-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesSleScopeIdMetricMetricThreshold404ErrorException`](../../doc/models/api-v1-sites-sle-scope-id-metric-metric-threshold-404-error-exception.md) |


# Update Site Sle Threshold

Update the SLE threshold

```python
def update_site_sle_threshold(self,
                             site_id,
                             scope,
                             scope_id,
                             metric,
                             body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `scope` | [`Scope2Enum`](../../doc/models/scope-2-enum.md) | Template, Required | - |
| `scope_id` | `string` | Template, Required | * site_id if `scope`==`site`<br>* device_id if `scope`==`ap`, `scope`==`switch` or `scope`==`gateway`<br>* mac if `scope`==`client` |
| `metric` | `string` | Template, Required | values from /api/v1/sites/{site_id}/sle/{scope}/{scope_id}/metrics |
| `body` | [`SleThreshold`](../../doc/models/sle-threshold.md) | Body, Optional | - |

## Response Type

[`SleThreshold`](../../doc/models/sle-threshold.md)

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

scope = Scope2Enum.SWITCH

scope_id = 'scope_id0'

metric = 'metric8'

body = SleThreshold(
    maximum=-60,
    minimum=-90
)

result = sites_sl_es_controller.update_site_sle_threshold(
    site_id,
    scope,
    scope_id,
    metric,
    body
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "default": -72,
  "direction": "left",
  "maximum": -60,
  "metric": "coverage",
  "minimum": -90,
  "threshold": "-66",
  "units": "dBm"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesSleScopeIdMetricMetricThreshold401ErrorException`](../../doc/models/api-v1-sites-sle-scope-id-metric-metric-threshold-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesSleScopeIdMetricMetricThreshold403ErrorException`](../../doc/models/api-v1-sites-sle-scope-id-metric-metric-threshold-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesSleScopeIdMetricMetricThreshold404ErrorException`](../../doc/models/api-v1-sites-sle-scope-id-metric-metric-threshold-404-error-exception.md) |


# Get Site Sles Metrics

Get the list of metrics for the given scope

```python
def get_site_sles_metrics(self,
                         site_id,
                         scope,
                         scope_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `scope` | [`Scope2Enum`](../../doc/models/scope-2-enum.md) | Template, Required | - |
| `scope_id` | `string` | Template, Required | * site_id if `scope`==`site`<br>* device_id if `scope`==`ap`, `scope`==`switch` or `scope`==`gateway`<br>* mac if `scope`==`client` |

## Response Type

[`ApiV1SitesSleScopeIdMetricsResponse`](../../doc/models/api-v1-sites-sle-scope-id-metrics-response.md)

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

scope = Scope2Enum.SWITCH

scope_id = 'scope_id0'

result = sites_sl_es_controller.get_site_sles_metrics(
    site_id,
    scope,
    scope_id
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "enabled": [
    "coverage",
    "capacity",
    "time-to-connect",
    "failed-to-connect",
    "roaming",
    "roaming-v2",
    "throughput",
    "switch-health",
    "switch-throughput",
    "switch-stc",
    "gateway-health",
    "application-health",
    "wan-link-health",
    "ap-availability"
  ],
  "supported": [
    "coverage",
    "capacity",
    "time-to-connect",
    "failed-to-connect",
    "roaming",
    "roaming-v2",
    "location-jitter",
    "location-latency",
    "throughput",
    "location-dropped-requests",
    "switch-health",
    "switch-throughput",
    "switch-stc",
    "gateway-health",
    "application-health",
    "wan-link-health",
    "ap-availability",
    "location-sdk-connect-time",
    "location-ble-hung"
  ]
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesSleScopeIdMetrics401ErrorException`](../../doc/models/api-v1-sites-sle-scope-id-metrics-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesSleScopeIdMetrics403ErrorException`](../../doc/models/api-v1-sites-sle-scope-id-metrics-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesSleScopeIdMetrics404ErrorException`](../../doc/models/api-v1-sites-sle-scope-id-metrics-404-error-exception.md) |

