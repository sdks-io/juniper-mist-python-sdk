# Sitesv Beacons

```python
sitesv_beacons_controller = client.sitesv_beacons
```

## Class Name

`SitesvBeaconsController`

## Methods

* [List Site V Beacons](../../doc/controllers/sitesv-beacons.md#list-site-v-beacons)
* [Create Site V Beacon](../../doc/controllers/sitesv-beacons.md#create-site-v-beacon)
* [Delete Site V Beacon](../../doc/controllers/sitesv-beacons.md#delete-site-v-beacon)
* [Get Site V Beacon](../../doc/controllers/sitesv-beacons.md#get-site-v-beacon)
* [Update Site V Beacon](../../doc/controllers/sitesv-beacons.md#update-site-v-beacon)


# List Site V Beacons

Get List of Site Virtual Beacons

```python
def list_site_v_beacons(self,
                       site_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |

## Response Type

[`List of Vbeacon`](../../doc/models/vbeacon.md)

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

result = sites_v_beacons_controller.list_site_v_beacons(site_id)
print(result)
```

## Example Response *(as JSON)*

```json
[
  {
    "created_time": 0,
    "id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
    "major": 0,
    "map_id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
    "message": "string",
    "minor": 0,
    "modified_time": 0,
    "name": "string",
    "org_id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
    "power": 4,
    "power_mode": "default",
    "site_id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
    "url": "string",
    "uuid": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
    "wayfinding_nodename": "string",
    "x": 0,
    "y": 0
  }
]
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesVbeacons401ErrorException`](../../doc/models/api-v1-sites-vbeacons-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesVbeacons403ErrorException`](../../doc/models/api-v1-sites-vbeacons-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesVbeacons404ErrorException`](../../doc/models/api-v1-sites-vbeacons-404-error-exception.md) |


# Create Site V Beacon

Create Virtual Beacon

```python
def create_site_v_beacon(self,
                        site_id,
                        body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `body` | [`Vbeacon`](../../doc/models/vbeacon.md) | Body, Optional | Request Body |

## Response Type

[`Vbeacon`](../../doc/models/vbeacon.md)

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

body = Vbeacon(
    major=0,
    map_id='b069b358-4c97-5319-1f8c-7c5ca64d6ab1',
    message='string',
    minor=0,
    name='string',
    power=4,
    power_mode=PowerModeEnum.DEFAULT,
    url='string',
    uuid='6f4bf402-45f9-2a56-6c8b-7f83d3bc98e9',
    wayfinding_nodename='string',
    x=0,
    y=0
)

result = sites_v_beacons_controller.create_site_v_beacon(
    site_id,
    body
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "created_time": 0,
  "id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
  "major": 0,
  "map_id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
  "message": "string",
  "minor": 0,
  "modified_time": 0,
  "name": "string",
  "org_id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
  "power": 4,
  "power_mode": "default",
  "site_id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
  "url": "string",
  "uuid": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
  "wayfinding_nodename": "string",
  "x": 0,
  "y": 0
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesVbeacons401ErrorException`](../../doc/models/api-v1-sites-vbeacons-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesVbeacons403ErrorException`](../../doc/models/api-v1-sites-vbeacons-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesVbeacons404ErrorException`](../../doc/models/api-v1-sites-vbeacons-404-error-exception.md) |


# Delete Site V Beacon

Delete Site Virtual Beacon

```python
def delete_site_v_beacon(self,
                        site_id,
                        vbeacon_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `vbeacon_id` | `uuid\|string` | Template, Required | - |

## Response Type

`object`

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

vbeacon_id = '000000ab-00ab-00ab-00ab-0000000000ab'

result = sites_v_beacons_controller.delete_site_v_beacon(
    site_id,
    vbeacon_id
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesVbeacons401ErrorException`](../../doc/models/api-v1-sites-vbeacons-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesVbeacons403ErrorException`](../../doc/models/api-v1-sites-vbeacons-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesVbeacons404ErrorException`](../../doc/models/api-v1-sites-vbeacons-404-error-exception.md) |


# Get Site V Beacon

Get Site Virtual Beacon Details

```python
def get_site_v_beacon(self,
                     site_id,
                     vbeacon_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `vbeacon_id` | `uuid\|string` | Template, Required | - |

## Response Type

[`Vbeacon`](../../doc/models/vbeacon.md)

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

vbeacon_id = '000000ab-00ab-00ab-00ab-0000000000ab'

result = sites_v_beacons_controller.get_site_v_beacon(
    site_id,
    vbeacon_id
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "created_time": 0,
  "id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
  "major": 0,
  "map_id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
  "message": "string",
  "minor": 0,
  "modified_time": 0,
  "name": "string",
  "org_id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
  "power": 4,
  "power_mode": "default",
  "site_id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
  "url": "string",
  "uuid": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
  "wayfinding_nodename": "string",
  "x": 0,
  "y": 0
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesVbeacons401ErrorException`](../../doc/models/api-v1-sites-vbeacons-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesVbeacons403ErrorException`](../../doc/models/api-v1-sites-vbeacons-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesVbeacons404ErrorException`](../../doc/models/api-v1-sites-vbeacons-404-error-exception.md) |


# Update Site V Beacon

Update Site Virtual Beacon

```python
def update_site_v_beacon(self,
                        site_id,
                        vbeacon_id,
                        body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `vbeacon_id` | `uuid\|string` | Template, Required | - |
| `body` | [`Vbeacon`](../../doc/models/vbeacon.md) | Body, Optional | Request Body |

## Response Type

[`Vbeacon`](../../doc/models/vbeacon.md)

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

vbeacon_id = '000000ab-00ab-00ab-00ab-0000000000ab'

body = Vbeacon(
    major=0,
    map_id='b069b358-4c97-5319-1f8c-7c5ca64d6ab1',
    message='string',
    minor=0,
    name='string',
    power=4,
    power_mode=PowerModeEnum.DEFAULT,
    url='string',
    uuid='6f4bf402-45f9-2a56-6c8b-7f83d3bc98e9',
    wayfinding_nodename='string',
    x=0,
    y=0
)

result = sites_v_beacons_controller.update_site_v_beacon(
    site_id,
    vbeacon_id,
    body
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "created_time": 0,
  "id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
  "major": 0,
  "map_id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
  "message": "string",
  "minor": 0,
  "modified_time": 0,
  "name": "string",
  "org_id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
  "power": 4,
  "power_mode": "default",
  "site_id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
  "url": "string",
  "uuid": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
  "wayfinding_nodename": "string",
  "x": 0,
  "y": 0
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesVbeacons401ErrorException`](../../doc/models/api-v1-sites-vbeacons-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesVbeacons403ErrorException`](../../doc/models/api-v1-sites-vbeacons-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesVbeacons404ErrorException`](../../doc/models/api-v1-sites-vbeacons-404-error-exception.md) |

