# Sites RRM

```python
sites_rrm_controller = client.sites_rrm
```

## Class Name

`SitesRRMController`

## Methods

* [Get Site Current Channel Planning](../../doc/controllers/sites-rrm.md#get-site-current-channel-planning)
* [Get Site Current Rrm Considerations for an Ap on a Specific Band](../../doc/controllers/sites-rrm.md#get-site-current-rrm-considerations-for-an-ap-on-a-specific-band)
* [Get Site Rrm Events](../../doc/controllers/sites-rrm.md#get-site-rrm-events)
* [Optimize Site Rrm](../../doc/controllers/sites-rrm.md#optimize-site-rrm)


# Get Site Current Channel Planning

Get Current Channel Planning

```python
def get_site_current_channel_planning(self,
                                     site_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |

## Response Type

[`Rrm`](../../doc/models/rrm.md)

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

result = sites_rrm_controller.get_site_current_channel_planning(site_id)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "band_24": {},
  "band_24_metric": {
    "avg_aps_per_channel": 0,
    "channel_distribution_uniformity": 0,
    "cochannel_neighbors": 0,
    "density": 0,
    "naps_by_channel": {},
    "naps_by_power": {},
    "neighbors": 0,
    "noise": 0
  },
  "band_5": {},
  "band_5_metric": {
    "avg_aps_per_channel": 0,
    "channel_distribution_uniformity": 0,
    "cochannel_neighbors": 0,
    "density": 0,
    "naps_by_channel": {},
    "naps_by_power": {},
    "neighbors": 0,
    "noise": 0
  },
  "rftemplate": {
    "band_24": {
      "allow_rrm_disable": true,
      "antenna_mode": "default",
      "bandwidth": 20,
      "channel": 0,
      "disabled": true,
      "power": 0,
      "power_max": 0,
      "power_min": 0,
      "preamble": "auto",
      "usage": "24"
    },
    "band_5": {
      "allow_rrm_disable": true,
      "antenna_mode": "default",
      "bandwidth": 20,
      "channel": 0,
      "disabled": true,
      "power": 0,
      "power_max": 0,
      "power_min": 0,
      "preamble": "auto",
      "usage": "24"
    },
    "country_code": "string",
    "created_time": 0,
    "id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
    "model_specific": {
      "property1": {
        "band_24": {
          "allow_rrm_disable": true,
          "antenna_mode": "default",
          "bandwidth": 20,
          "channel": 0,
          "disabled": true,
          "power": 0,
          "power_max": 0,
          "power_min": 0,
          "preamble": "auto",
          "usage": "24"
        },
        "band_5": {
          "allow_rrm_disable": true,
          "antenna_mode": "default",
          "bandwidth": 20,
          "channel": 0,
          "disabled": true,
          "power": 0,
          "power_max": 0,
          "power_min": 0,
          "preamble": "auto",
          "usage": "24"
        }
      },
      "property2": {
        "band_24": {
          "allow_rrm_disable": true,
          "antenna_mode": "default",
          "bandwidth": 20,
          "channel": 0,
          "disabled": true,
          "power": 0,
          "power_max": 0,
          "power_min": 0,
          "preamble": "auto",
          "usage": "24"
        },
        "band_5": {
          "allow_rrm_disable": true,
          "antenna_mode": "default",
          "bandwidth": 20,
          "channel": 0,
          "disabled": true,
          "power": 0,
          "power_max": 0,
          "power_min": 0,
          "preamble": "auto",
          "usage": "24"
        }
      }
    },
    "modified_time": 0,
    "name": "string",
    "org_id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
    "site_id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1"
  },
  "rftemplate_id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
  "rftemplate_name": "string",
  "status": "updating",
  "timestamp": 0
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesRrmCurrent401ErrorException`](../../doc/models/api-v1-sites-rrm-current-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesRrmCurrent403ErrorException`](../../doc/models/api-v1-sites-rrm-current-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesRrmCurrent404ErrorException`](../../doc/models/api-v1-sites-rrm-current-404-error-exception.md) |


# Get Site Current Rrm Considerations for an Ap on a Specific Band

Get Current RRM Considerations for an AP on a Specific Band

```python
def get_site_current_rrm_considerations_for_an_ap_on_a_specific_band(self,
                                                                    site_id,
                                                                    device_id,
                                                                    band)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `device_id` | `uuid\|string` | Template, Required | - |
| `band` | [`Band8Enum`](../../doc/models/band-8-enum.md) | Template, Required | radio band |

## Response Type

[`RrmConsideration`](../../doc/models/rrm-consideration.md)

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

device_id = '000000ab-00ab-00ab-00ab-0000000000ab'

band = Band8Enum.ENUM_6

result = sites_rrm_controller.get_site_current_rrm_considerations_for_an_ap_on_a_specific_band(
    site_id,
    device_id,
    band
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "results": [
    {
      "channel": 36,
      "noise": -78,
      "non_wifi": 0.08,
      "other_rssi": -66,
      "other_ssid": "Rivendell5G",
      "rssi": -48,
      "util_score": 0.1,
      "util_score_non_wifi": 0.01,
      "util_score_other": 0.05,
      "wifi": 0.13
    }
  ]
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesRrmCurrentDevicesBandBand401ErrorException`](../../doc/models/api-v1-sites-rrm-current-devices-band-band-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesRrmCurrentDevicesBandBand403ErrorException`](../../doc/models/api-v1-sites-rrm-current-devices-band-band-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesRrmCurrentDevicesBandBand404ErrorException`](../../doc/models/api-v1-sites-rrm-current-devices-band-band-404-error-exception.md) |


# Get Site Rrm Events

Get Site RRM Events

```python
def get_site_rrm_events(self,
                       site_id,
                       band,
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
| `band` | [`Band8Enum`](../../doc/models/band-8-enum.md) | Query, Required | - |
| `page` | `int` | Query, Optional | **Default**: `1`<br>**Constraints**: `>= 1` |
| `limit` | `int` | Query, Optional | **Default**: `100`<br>**Constraints**: `>= 0` |
| `start` | `int` | Query, Optional | **Default**: `0`<br>**Constraints**: `>= 0` |
| `end` | `int` | Query, Optional | **Default**: `0`<br>**Constraints**: `>= 0` |
| `duration` | `string` | Query, Optional | For historical stats and/or logs where time range is needed, you can specify the time range in a few different ways:<br><br>* ?start=1430000000&end=1430864000	specify the start / end<br>* ?end=1430864000&duration=1d	specify end time and duration<br>* ?duration=1d	specify duration, end will be now() in seconds<br>**Default**: `'1d'` |

## Response Type

[`RrmEvents`](../../doc/models/rrm-events.md)

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

band = Band8Enum.ENUM_6

page = 1

limit = 100

start = 0

end = 0

duration = '10m'

result = sites_rrm_controller.get_site_rrm_events(
    site_id,
    band,
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
  "next": "/api/v1/sites/dca0a44b-324c-11e6-a776-0243ad110007/events/rrm?start=1428939600&end=1428949600&limit=200&token=001a0010000000120010000005005880ec18000004776c616e007fffffeb067ab8e29c1d659b6a7c8cf698bf81490003",
  "results": [
    {
      "ap_id": "00000000-0000-0000-1000-5c5b359e4fe0",
      "band": "24",
      "bandwidth": 20,
      "channel": 6,
      "event": "scheduled-site-rrm",
      "power": 5,
      "pre_bandwidth": 20,
      "pre_channel": 1,
      "pre_power": 11,
      "pre_usage": "24",
      "timestamp": 1428939600,
      "usage": "24"
    }
  ],
  "start": 1428939600
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesRrmEvents401ErrorException`](../../doc/models/api-v1-sites-rrm-events-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesRrmEvents403ErrorException`](../../doc/models/api-v1-sites-rrm-events-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesRrmEvents404ErrorException`](../../doc/models/api-v1-sites-rrm-events-404-error-exception.md) |


# Optimize Site Rrm

Optimize Site RRM

```python
def optimize_site_rrm(self,
                     site_id,
                     body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `body` | [`ApiV1SitesRrmOptimizeRequest`](../../doc/models/api-v1-sites-rrm-optimize-request.md) | Body, Optional | Request Body |

## Response Type

`object`

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

body = ApiV1SitesRrmOptimizeRequest(
    bands=[
        '24',
        '5',
        '6'
    ]
)

result = sites_rrm_controller.optimize_site_rrm(
    site_id,
    body
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesRrmOptimize401ErrorException`](../../doc/models/api-v1-sites-rrm-optimize-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesRrmOptimize403ErrorException`](../../doc/models/api-v1-sites-rrm-optimize-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesRrmOptimize404ErrorException`](../../doc/models/api-v1-sites-rrm-optimize-404-error-exception.md) |

