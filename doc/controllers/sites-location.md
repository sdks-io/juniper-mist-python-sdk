# Sites Location

```python
sites_location_controller = client.sites_location
```

## Class Name

`SitesLocationController`

## Methods

* [Get Site Beam Coverage Overview](../../doc/controllers/sites-location.md#get-site-beam-coverage-overview)
* [Get Site Machine Learning Current Stat](../../doc/controllers/sites-location.md#get-site-machine-learning-current-stat)
* [Get Site Default Plf for Models](../../doc/controllers/sites-location.md#get-site-default-plf-for-models)
* [Clear Site Ml Overwrite for Device](../../doc/controllers/sites-location.md#clear-site-ml-overwrite-for-device)
* [Overwrite Site Ml for Device](../../doc/controllers/sites-location.md#overwrite-site-ml-for-device)
* [Clear Site Ml Overwrite for Map](../../doc/controllers/sites-location.md#clear-site-ml-overwrite-for-map)
* [Overwrite Site Ml for Map](../../doc/controllers/sites-location.md#overwrite-site-ml-for-map)
* [Reset Site Ml Stats by Map](../../doc/controllers/sites-location.md#reset-site-ml-stats-by-map)
* [Get Site Machine Learning Events](../../doc/controllers/sites-location.md#get-site-machine-learning-events)


# Get Site Beam Coverage Overview

Get Beam Coverage Overview

```python
def get_site_beam_coverage_overview(self,
                                   site_id,
                                   map_id=None,
                                   mtype='sdkclient',
                                   duration='1h',
                                   resolution='default',
                                   client_type=None,
                                   start=0,
                                   end=0)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `map_id` | `string` | Query, Optional | map_id (filter by map_id) |
| `mtype` | [`Type58Enum`](../../doc/models/type-58-enum.md) | Query, Optional | **Default**: `'sdkclient'` |
| `duration` | [`DurationEnum`](../../doc/models/duration-enum.md) | Query, Optional | where the start time will be calculated (with end time is now)<br>**Default**: `'1h'` |
| `resolution` | [`ResolutionEnum`](../../doc/models/resolution-enum.md) | Query, Optional | **Default**: `'default'` |
| `client_type` | `string` | Query, Optional | client_type (as filter. optional) |
| `start` | `int` | Query, Optional | **Default**: `0`<br>**Constraints**: `>= 0` |
| `end` | `int` | Query, Optional | **Default**: `0`<br>**Constraints**: `>= 0` |

## Response Type

[`ApiV1SitesLocationCoverageResponse`](../../doc/models/api-v1-sites-location-coverage-response.md)

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

map_id = '00000000-0000-0000-0000-000000000000'

mtype = Type58Enum.SDKCLIENT

duration = DurationEnum.ENUM_1H

resolution = ResolutionEnum.DEFAULT

start = 0

end = 0

result = sites_location_controller.get_site_beam_coverage_overview(
    site_id,
    map_id,
    mtype,
    duration,
    resolution,
    start,
    end
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "beams_means": [
    [
      1,
      3,
      3.2
    ],
    [
      6,
      10,
      6.5
    ]
  ],
  "end": 1428954000,
  "gridsize": 1,
  "result_def": [
    "x",
    "y",
    "beams_mean",
    "beacons_mean",
    "max_rssi",
    "avg_rssi"
  ],
  "results": [
    [
      1,
      3,
      3.2,
      18.5,
      -68,
      -70
    ],
    [
      6,
      10,
      6.5,
      30,
      1,
      -72.5,
      -75
    ]
  ],
  "start": 1428939600
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesLocationCoverage401ErrorException`](../../doc/models/api-v1-sites-location-coverage-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesLocationCoverage403ErrorException`](../../doc/models/api-v1-sites-location-coverage-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesLocationCoverage404ErrorException`](../../doc/models/api-v1-sites-location-coverage-404-error-exception.md) |


# Get Site Machine Learning Current Stat

Get Machine Learning Current Stat
For each VBLE AP, it has ML model parameters (e.g. Path-loss-estimate, Intercept) as well as completion indicators (Level and PercentageComplete). For the completeness, ML takes N sample to finish its first level and use N*0.25 samples to complete each successive level. When a device is moved, the completeness will be reset as it has to re-learn.

```python
def get_site_machine_learning_current_stat(self,
                                          site_id,
                                          map_id=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `map_id` | `string` | Query, Optional | map_id (as filter, optional) |

## Response Type

`List of object`

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

map_id = '00000000-0000-0000-0000-000000000000'

result = sites_location_controller.get_site_machine_learning_current_stat(
    site_id,
    map_id
)
print(result)
```

## Example Response

```
[
  {
    "current": {
      "Android": {
        "completed": 36,
        "int": -6,
        "level": 3,
        "ple": -3,
        "quality": "4",
        "src": "device",
        "timestamp": 1442854794
      },
      "iOS": {
        "completed": 16,
        "int": -6,
        "level": 6,
        "ple": -3,
        "quality": "2",
        "src": "default",
        "timestamp": 1442854704
      },
      "iPod": {
        "int": -10,
        "overwrite": true,
        "ple": -5,
        "src": "overwrite"
      }
    },
    "device_id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1"
  },
  {
    "beacon_id": "7913f032-aab4-c3ae-e83e-5a2756ef4d40",
    "current": {
      "iOS": {
        "completed": 16,
        "int": -6,
        "level": 6,
        "ple": -3,
        "quality": "last",
        "src": "device",
        "timestamp": 1442854704
      }
    }
  }
]
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesLocationMlCurrent401ErrorException`](../../doc/models/api-v1-sites-location-ml-current-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesLocationMlCurrent403ErrorException`](../../doc/models/api-v1-sites-location-ml-current-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesLocationMlCurrent404ErrorException`](../../doc/models/api-v1-sites-location-ml-current-404-error-exception.md) |


# Get Site Default Plf for Models

Get Default PLF for Models

```python
def get_site_default_plf_for_models(self,
                                   site_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |

## Response Type

`List of object`

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

result = sites_location_controller.get_site_default_plf_for_models(site_id)
print(result)
```

## Example Response

```
[
  {
    "current": {
      "Android": {
        "completed": 36,
        "int": -6,
        "level": 3,
        "ple": -3,
        "quality": "4",
        "src": "device",
        "timestamp": 1442854794
      },
      "iOS": {
        "completed": 16,
        "int": -6,
        "level": 6,
        "ple": -3,
        "quality": "2",
        "src": "default",
        "timestamp": 1442854704
      },
      "iPod": {
        "int": -10,
        "overwrite": true,
        "ple": -5,
        "src": "overwrite"
      }
    },
    "device_id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1"
  },
  {
    "beacon_id": "7913f032-aab4-c3ae-e83e-5a2756ef4d40",
    "current": {
      "iOS": {
        "completed": 16,
        "int": -6,
        "level": 6,
        "ple": -3,
        "quality": "last",
        "src": "device",
        "timestamp": 1442854704
      }
    }
  }
]
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesLocationMlDefaults401ErrorException`](../../doc/models/api-v1-sites-location-ml-defaults-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesLocationMlDefaults403ErrorException`](../../doc/models/api-v1-sites-location-ml-defaults-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesLocationMlDefaults404ErrorException`](../../doc/models/api-v1-sites-location-ml-defaults-404-error-exception.md) |


# Clear Site Ml Overwrite for Device

Clear ML Overwrite for Device

```python
def clear_site_ml_overwrite_for_device(self,
                                      site_id,
                                      device_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `device_id` | `uuid\|string` | Template, Required | - |

## Response Type

`object`

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

device_id = '000000ab-00ab-00ab-00ab-0000000000ab'

result = sites_location_controller.clear_site_ml_overwrite_for_device(
    site_id,
    device_id
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesLocationMlDevice401ErrorException`](../../doc/models/api-v1-sites-location-ml-device-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesLocationMlDevice403ErrorException`](../../doc/models/api-v1-sites-location-ml-device-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesLocationMlDevice404ErrorException`](../../doc/models/api-v1-sites-location-ml-device-404-error-exception.md) |


# Overwrite Site Ml for Device

Overwrite ML For Device

```python
def overwrite_site_ml_for_device(self,
                                site_id,
                                device_id,
                                body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `device_id` | `uuid\|string` | Template, Required | - |
| `body` | [`dict`](../../doc/models/model-ml.md) | Body, Optional | Request Body |

## Response Type

`List of object`

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

device_id = '000000ab-00ab-00ab-00ab-0000000000ab'

body = {
    "iOS": ModelMl(
        int=6,
        ple=-3
    ),
    "iPod": ModelMl(
        int=-10,
        ple=-5
    )
}

result = sites_location_controller.overwrite_site_ml_for_device(
    site_id,
    device_id,
    body
)
print(result)
```

## Example Response

```
[
  {
    "current": {
      "Android": {
        "completed": 36,
        "int": -6,
        "level": 3,
        "ple": -3,
        "quality": "4",
        "src": "device",
        "timestamp": 1442854794
      },
      "iOS": {
        "completed": 16,
        "int": -6,
        "level": 6,
        "ple": -3,
        "quality": "2",
        "src": "default",
        "timestamp": 1442854704
      },
      "iPod": {
        "int": -10,
        "overwrite": true,
        "ple": -5,
        "src": "overwrite"
      }
    },
    "device_id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1"
  },
  {
    "beacon_id": "7913f032-aab4-c3ae-e83e-5a2756ef4d40",
    "current": {
      "iOS": {
        "completed": 16,
        "int": -6,
        "level": 6,
        "ple": -3,
        "quality": "last",
        "src": "device",
        "timestamp": 1442854704
      }
    }
  }
]
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesLocationMlDevice401ErrorException`](../../doc/models/api-v1-sites-location-ml-device-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesLocationMlDevice403ErrorException`](../../doc/models/api-v1-sites-location-ml-device-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesLocationMlDevice404ErrorException`](../../doc/models/api-v1-sites-location-ml-device-404-error-exception.md) |


# Clear Site Ml Overwrite for Map

Clear ML Overwrite for Map

```python
def clear_site_ml_overwrite_for_map(self,
                                   site_id,
                                   map_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `map_id` | `uuid\|string` | Template, Required | - |

## Response Type

`object`

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

map_id = '000000ab-00ab-00ab-00ab-0000000000ab'

result = sites_location_controller.clear_site_ml_overwrite_for_map(
    site_id,
    map_id
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesLocationMlMap401ErrorException`](../../doc/models/api-v1-sites-location-ml-map-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesLocationMlMap403ErrorException`](../../doc/models/api-v1-sites-location-ml-map-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesLocationMlMap404ErrorException`](../../doc/models/api-v1-sites-location-ml-map-404-error-exception.md) |


# Overwrite Site Ml for Map

Overwrite ML For Map

```python
def overwrite_site_ml_for_map(self,
                             site_id,
                             map_id,
                             body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `map_id` | `uuid\|string` | Template, Required | - |
| `body` | [`dict`](../../doc/models/model-ml.md) | Body, Optional | Request Body |

## Response Type

`List of object`

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

map_id = '000000ab-00ab-00ab-00ab-0000000000ab'

body = {
    "iOS": ModelMl(
        int=6,
        ple=-3
    ),
    "iPod": ModelMl(
        int=-10,
        ple=-5
    )
}

result = sites_location_controller.overwrite_site_ml_for_map(
    site_id,
    map_id,
    body
)
print(result)
```

## Example Response

```
[
  {
    "current": {
      "Android": {
        "completed": 36,
        "int": -6,
        "level": 3,
        "ple": -3,
        "quality": "4",
        "src": "device",
        "timestamp": 1442854794
      },
      "iOS": {
        "completed": 16,
        "int": -6,
        "level": 6,
        "ple": -3,
        "quality": "2",
        "src": "default",
        "timestamp": 1442854704
      },
      "iPod": {
        "int": -10,
        "overwrite": true,
        "ple": -5,
        "src": "overwrite"
      }
    },
    "device_id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1"
  },
  {
    "beacon_id": "7913f032-aab4-c3ae-e83e-5a2756ef4d40",
    "current": {
      "iOS": {
        "completed": 16,
        "int": -6,
        "level": 6,
        "ple": -3,
        "quality": "last",
        "src": "device",
        "timestamp": 1442854704
      }
    }
  }
]
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesLocationMlMap401ErrorException`](../../doc/models/api-v1-sites-location-ml-map-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesLocationMlMap403ErrorException`](../../doc/models/api-v1-sites-location-ml-map-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesLocationMlMap404ErrorException`](../../doc/models/api-v1-sites-location-ml-map-404-error-exception.md) |


# Reset Site Ml Stats by Map

Reset ML Stats by Map

```python
def reset_site_ml_stats_by_map(self,
                              site_id,
                              map_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `map_id` | `uuid\|string` | Template, Required | - |

## Response Type

`object`

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

map_id = '000000ab-00ab-00ab-00ab-0000000000ab'

result = sites_location_controller.reset_site_ml_stats_by_map(
    site_id,
    map_id
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesLocationMlResetMap401ErrorException`](../../doc/models/api-v1-sites-location-ml-reset-map-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesLocationMlResetMap403ErrorException`](../../doc/models/api-v1-sites-location-ml-reset-map-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesLocationMlResetMap404ErrorException`](../../doc/models/api-v1-sites-location-ml-reset-map-404-error-exception.md) |


# Get Site Machine Learning Events

Get Machine Learning Events

```python
def get_site_machine_learning_events(self,
                                    site_id,
                                    device_id=None,
                                    map_ip=None,
                                    client_type=None,
                                    duration=None,
                                    start=0,
                                    end=0,
                                    interval=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `device_id` | `string` | Query, Optional | device_id (as filter, optional) |
| `map_ip` | `string` | Query, Optional | map_id (as filter, optional) |
| `client_type` | `string` | Query, Optional | client_type (as filter, optional) |
| `duration` | `string` | Query, Optional | instead of start, you can use 1d, 30m, 5h, where the start will be calculated |
| `start` | `int` | Query, Optional | **Default**: `0`<br>**Constraints**: `>= 0` |
| `end` | `int` | Query, Optional | **Default**: `0`<br>**Constraints**: `>= 0` |
| `interval` | `string` | Query, Optional | - |

## Response Type

[`MlEvents`](../../doc/models/ml-events.md)

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

device_id = '00000000-0000-0000-0000-000000000000'

start = 0

end = 0

result = sites_location_controller.get_site_machine_learning_events(
    site_id,
    device_id,
    start,
    end
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "end": 1428954000,
  "interval": 600,
  "start": 1428939600,
  "updates": [
    {
      "client_type": "iOS",
      "completed": 6,
      "int": -6,
      "level": 0,
      "ple": -3,
      "timestamp": 1442854794
    },
    {
      "client_type": "iOS",
      "completed": 4,
      "int": -4,
      "level": 0,
      "ple": -2,
      "timestamp": 1442854796
    },
    {
      "client_type": "iOS",
      "completed": 2,
      "int": -2,
      "level": 0,
      "ple": -1,
      "timestamp": 1442854798
    }
  ]
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesLocationMlUpdates401ErrorException`](../../doc/models/api-v1-sites-location-ml-updates-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesLocationMlUpdates403ErrorException`](../../doc/models/api-v1-sites-location-ml-updates-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesLocationMlUpdates404ErrorException`](../../doc/models/api-v1-sites-location-ml-updates-404-error-exception.md) |

