# Sites Maps Auto-Orientation

```python
sites_maps_auto_orientation_controller = client.sites_maps_auto_orientation
```

## Class Name

`SitesMapsAutoOrientationController`

## Methods

* [Delete Site Ap Auto Orientation](../../doc/controllers/sites-maps-auto-orientation.md#delete-site-ap-auto-orientation)
* [Start Site Ap Auto Orientation](../../doc/controllers/sites-maps-auto-orientation.md#start-site-ap-auto-orientation)
* [Clear Site Ap Auto Orient](../../doc/controllers/sites-maps-auto-orientation.md#clear-site-ap-auto-orient)


# Delete Site Ap Auto Orientation

This API is called to force stop auto placement for a given map

```python
def delete_site_ap_auto_orientation(self,
                                   map_id,
                                   site_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `map_id` | `uuid\|string` | Template, Required | - |
| `site_id` | `uuid\|string` | Template, Required | - |

## Response Type

`object`

## Example Usage

```python
map_id = '000000ab-00ab-00ab-00ab-0000000000ab'

site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

result = sites_maps_auto_orientation_controller.delete_site_ap_auto_orientation(
    map_id,
    site_id
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Autoplacement was not triggered | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesMapsAutoOrient401ErrorException`](../../doc/models/api-v1-sites-maps-auto-orient-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesMapsAutoOrient403ErrorException`](../../doc/models/api-v1-sites-maps-auto-orient-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesMapsAutoOrient404ErrorException`](../../doc/models/api-v1-sites-maps-auto-orient-404-error-exception.md) |


# Start Site Ap Auto Orientation

This API is used to trigger a map for Auto orientation

```python
def start_site_ap_auto_orientation(self,
                                  map_id,
                                  site_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `map_id` | `uuid\|string` | Template, Required | - |
| `site_id` | `uuid\|string` | Template, Required | - |

## Response Type

[`ApiV1SitesMapsAutoOrientResponse`](../../doc/models/api-v1-sites-maps-auto-orient-response.md)

## Example Usage

```python
map_id = '000000ab-00ab-00ab-00ab-0000000000ab'

site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

result = sites_maps_auto_orientation_controller.start_site_ap_auto_orientation(
    map_id,
    site_id
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "state": "Not Started",
  "time_queued": 1675414259
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesMapsAutoOrient401ErrorException`](../../doc/models/api-v1-sites-maps-auto-orient-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesMapsAutoOrient403ErrorException`](../../doc/models/api-v1-sites-maps-auto-orient-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesMapsAutoOrient404ErrorException`](../../doc/models/api-v1-sites-maps-auto-orient-404-error-exception.md) |


# Clear Site Ap Auto Orient

This API is used to destroy the autoorientations of a map or subset of APs on a map.

```python
def clear_site_ap_auto_orient(self,
                             site_id,
                             map_id,
                             body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `map_id` | `uuid\|string` | Template, Required | - |
| `body` | [`ApiV1SitesMapsClearAutoOrientRequest`](../../doc/models/api-v1-sites-maps-clear-auto-orient-request.md) | Body, Optional | - |

## Response Type

`object`

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

map_id = '000000ab-00ab-00ab-00ab-0000000000ab'

result = sites_maps_auto_orientation_controller.clear_site_ap_auto_orient(
    site_id,
    map_id
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesMapsClearAutoOrient401ErrorException`](../../doc/models/api-v1-sites-maps-clear-auto-orient-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesMapsClearAutoOrient403ErrorException`](../../doc/models/api-v1-sites-maps-clear-auto-orient-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesMapsClearAutoOrient404ErrorException`](../../doc/models/api-v1-sites-maps-clear-auto-orient-404-error-exception.md) |

