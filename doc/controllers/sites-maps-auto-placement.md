# Sites Maps Auto-Placement

```python
sites_maps_auto_placement_controller = client.sites_maps_auto_placement
```

## Class Name

`SitesMapsAutoPlacementController`

## Methods

* [Delete Site Ap Autoplacement](../../doc/controllers/sites-maps-auto-placement.md#delete-site-ap-autoplacement)
* [Get Site Ap Auto Placement](../../doc/controllers/sites-maps-auto-placement.md#get-site-ap-auto-placement)
* [Run Site Ap Autoplacement](../../doc/controllers/sites-maps-auto-placement.md#run-site-ap-autoplacement)
* [Clear Site Ap Autoplacement](../../doc/controllers/sites-maps-auto-placement.md#clear-site-ap-autoplacement)
* [Confirm Site Ap Localization Data](../../doc/controllers/sites-maps-auto-placement.md#confirm-site-ap-localization-data)


# Delete Site Ap Autoplacement

This API is called to force stop auto placement for a given map

```python
def delete_site_ap_autoplacement(self,
                                site_id,
                                map_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `map_id` | `uuid\|string` | Template, Required | - |

## Response Type

`void`

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

map_id = '000000ab-00ab-00ab-00ab-0000000000ab'

result = sites_maps_auto_placement_controller.delete_site_ap_autoplacement(
    site_id,
    map_id
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Autoplacement was not triggered | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesMapsAutoPlacement401ErrorException`](../../doc/models/api-v1-sites-maps-auto-placement-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesMapsAutoPlacement403ErrorException`](../../doc/models/api-v1-sites-maps-auto-placement-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesMapsAutoPlacement404ErrorException`](../../doc/models/api-v1-sites-maps-auto-placement-404-error-exception.md) |


# Get Site Ap Auto Placement

This API is called to view the current status of auto placement for a given map.

```python
def get_site_ap_auto_placement(self,
                              site_id,
                              map_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `map_id` | `uuid\|string` | Template, Required | - |

## Response Type

[`ApiV1SitesMapsAutoPlacementResponse`](../../doc/models/api-v1-sites-maps-auto-placement-response.md)

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

map_id = '000000ab-00ab-00ab-00ab-0000000000ab'

result = sites_maps_auto_placement_controller.get_site_ap_auto_placement(
    site_id,
    map_id
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "end_time": 1678900362,
  "start_time": 1678900062,
  "status": "done"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesMapsAutoPlacement401ErrorException`](../../doc/models/api-v1-sites-maps-auto-placement-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesMapsAutoPlacement403ErrorException`](../../doc/models/api-v1-sites-maps-auto-placement-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesMapsAutoPlacement404ErrorException`](../../doc/models/api-v1-sites-maps-auto-placement-404-error-exception.md) |


# Run Site Ap Autoplacement

This API is called to trigger a map for auto placement. For auto placement feature to work, RTT-FTM data need to be collected from the APs on the map. This scan is disruptive and therefore the user must be notified of service disrution during the functioning of auto placement Repeated POST to this endpoint while a map is still running will be rejected.

List of devices to provide suggestions for is an optional parameter that can be given to this API. This will provide autoplacement suggestions only for the devices specified. If no list of devices is provided, all APs asociated with that map are considered by default

```python
def run_site_ap_autoplacement(self,
                             site_id,
                             map_id,
                             body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `map_id` | `uuid\|string` | Template, Required | - |
| `body` | [`ApiV1SitesMapsAutoPlacementRequest`](../../doc/models/api-v1-sites-maps-auto-placement-request.md) | Body, Optional | - |

## Response Type

`void`

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

map_id = '000000ab-00ab-00ab-00ab-0000000000ab'

body = ApiV1SitesMapsAutoPlacementRequest(
    force_collection=False
)

result = sites_maps_auto_placement_controller.run_site_ap_autoplacement(
    site_id,
    map_id,
    body
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | * Map has less than 3 APs associated with it to perform auto placement<br>* Auto AP Placement is already in progress for this Map<br>* Autoplacement data does not exist or has gone stale | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesMapsAutoPlacement401ErrorException`](../../doc/models/api-v1-sites-maps-auto-placement-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesMapsAutoPlacement403ErrorException`](../../doc/models/api-v1-sites-maps-auto-placement-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesMapsAutoPlacement404ErrorException`](../../doc/models/api-v1-sites-maps-auto-placement-404-error-exception.md) |


# Clear Site Ap Autoplacement

This API is used to destroy the cached autoplacement locations of a map or subset of APs on a map.

```python
def clear_site_ap_autoplacement(self,
                               site_id,
                               map_id,
                               body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `map_id` | `uuid\|string` | Template, Required | - |
| `body` | [`ApiV1SitesMapsClearAutoplacementRequest`](../../doc/models/api-v1-sites-maps-clear-autoplacement-request.md) | Body, Optional | - |

## Response Type

`object`

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

map_id = '000000ab-00ab-00ab-00ab-0000000000ab'

result = sites_maps_auto_placement_controller.clear_site_ap_autoplacement(
    site_id,
    map_id
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesMapsClearAutoplacement401ErrorException`](../../doc/models/api-v1-sites-maps-clear-autoplacement-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesMapsClearAutoplacement403ErrorException`](../../doc/models/api-v1-sites-maps-clear-autoplacement-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesMapsClearAutoplacement404ErrorException`](../../doc/models/api-v1-sites-maps-clear-autoplacement-404-error-exception.md) |


# Confirm Site Ap Localization Data

This API is used to accept or reject the cached autoplacement and auto orientation values of a map or subset of APs on a map. A rejected AP will retain its current X,Y and orientation until accpeted.

```python
def confirm_site_ap_localization_data(self,
                                     site_id,
                                     map_id,
                                     body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `string` | Template, Required | - |
| `map_id` | `string` | Template, Required | - |
| `body` | [`ApiV1SitesMapsUseAutoApValuesRequest`](../../doc/models/api-v1-sites-maps-use-auto-ap-values-request.md) | Body, Optional | - |

## Response Type

`void`

## Example Usage

```python
site_id = 'site_id6'

map_id = 'map_id4'

body = ApiV1SitesMapsUseAutoApValuesRequest(
    accept=False,
    device_macs=[
        'string'
    ],
    mfor=ForEnum.PLACEMENT
)

result = sites_maps_auto_placement_controller.confirm_site_ap_localization_data(
    site_id,
    map_id,
    body
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Invalid localization service expected: placement or orientation | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesMapsUseAutoApValues401ErrorException`](../../doc/models/api-v1-sites-maps-use-auto-ap-values-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesMapsUseAutoApValues403ErrorException`](../../doc/models/api-v1-sites-maps-use-auto-ap-values-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesMapsUseAutoApValues404ErrorException`](../../doc/models/api-v1-sites-maps-use-auto-ap-values-404-error-exception.md) |

