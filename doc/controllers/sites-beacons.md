# Sites Beacons

```python
sites_beacons_controller = client.sites_beacons
```

## Class Name

`SitesBeaconsController`

## Methods

* [List Site Beacons](../../doc/controllers/sites-beacons.md#list-site-beacons)
* [Create Site Beacon](../../doc/controllers/sites-beacons.md#create-site-beacon)
* [Delete Site Beacons](../../doc/controllers/sites-beacons.md#delete-site-beacons)
* [Get Site Beacon](../../doc/controllers/sites-beacons.md#get-site-beacon)
* [Update Site Beacons](../../doc/controllers/sites-beacons.md#update-site-beacons)


# List Site Beacons

Get List of Site Beacons

```python
def list_site_beacons(self,
                     site_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |

## Response Type

[`List of Beacon`](../../doc/models/beacon.md)

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

result = sites_beacons_controller.list_site_beacons(site_id)
print(result)
```

## Example Response *(as JSON)*

```json
[
  {
    "created_time": 0,
    "eddystone_instance": "string",
    "eddystone_namespace": "string",
    "eddystone_url": "string",
    "ibeacon_major": 0,
    "ibeacon_minor": 0,
    "ibeacon_uuid": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
    "id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
    "mac": "string",
    "map_id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
    "modified_time": 0,
    "name": "string",
    "org_id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
    "power": 0,
    "site_id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
    "type": "eddystone-uid",
    "x": 0,
    "y": 0
  }
]
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesBeacons401ErrorException`](../../doc/models/api-v1-sites-beacons-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesBeacons403ErrorException`](../../doc/models/api-v1-sites-beacons-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesBeacons404ErrorException`](../../doc/models/api-v1-sites-beacons-404-error-exception.md) |


# Create Site Beacon

Create Site Beacon

```python
def create_site_beacon(self,
                      site_id,
                      body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `body` | [`Beacon`](../../doc/models/beacon.md) | Body, Optional | Request Body |

## Response Type

[`Beacon`](../../doc/models/beacon.md)

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

body = Beacon(
    eddystone_instance='string',
    eddystone_namespace='string',
    eddystone_url='string',
    ibeacon_major=0,
    ibeacon_minor=0,
    ibeacon_uuid='b069b358-4c97-5319-1f8c-7c5ca64d6ab1',
    mac='string',
    map_id='b069b358-4c97-5319-1f8c-7c5ca64d6ab1',
    name='string',
    power=0,
    mtype=Type4Enum.EDDYSTONEUID,
    x=0,
    y=0
)

result = sites_beacons_controller.create_site_beacon(
    site_id,
    body
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "created_time": 0,
  "eddystone_instance": "string",
  "eddystone_namespace": "string",
  "eddystone_url": "string",
  "ibeacon_major": 0,
  "ibeacon_minor": 0,
  "ibeacon_uuid": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
  "id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
  "mac": "string",
  "map_id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
  "modified_time": 0,
  "name": "string",
  "org_id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
  "power": 0,
  "site_id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
  "type": "eddystone-uid",
  "x": 0,
  "y": 0
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesBeacons401ErrorException`](../../doc/models/api-v1-sites-beacons-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesBeacons403ErrorException`](../../doc/models/api-v1-sites-beacons-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesBeacons404ErrorException`](../../doc/models/api-v1-sites-beacons-404-error-exception.md) |


# Delete Site Beacons

Delete Site Beacon

```python
def delete_site_beacons(self,
                       site_id,
                       beacon_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `beacon_id` | `uuid\|string` | Template, Required | - |

## Response Type

`object`

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

beacon_id = '000000ab-00ab-00ab-00ab-0000000000ab'

result = sites_beacons_controller.delete_site_beacons(
    site_id,
    beacon_id
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesBeacons401ErrorException`](../../doc/models/api-v1-sites-beacons-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesBeacons403ErrorException`](../../doc/models/api-v1-sites-beacons-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesBeacons404ErrorException`](../../doc/models/api-v1-sites-beacons-404-error-exception.md) |


# Get Site Beacon

Get Site Beacon Details

```python
def get_site_beacon(self,
                   site_id,
                   beacon_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `beacon_id` | `uuid\|string` | Template, Required | - |

## Response Type

[`Beacon`](../../doc/models/beacon.md)

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

beacon_id = '000000ab-00ab-00ab-00ab-0000000000ab'

result = sites_beacons_controller.get_site_beacon(
    site_id,
    beacon_id
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "created_time": 0,
  "eddystone_instance": "string",
  "eddystone_namespace": "string",
  "eddystone_url": "string",
  "ibeacon_major": 0,
  "ibeacon_minor": 0,
  "ibeacon_uuid": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
  "id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
  "mac": "string",
  "map_id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
  "modified_time": 0,
  "name": "string",
  "org_id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
  "power": 0,
  "site_id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
  "type": "eddystone-uid",
  "x": 0,
  "y": 0
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesBeacons401ErrorException`](../../doc/models/api-v1-sites-beacons-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesBeacons403ErrorException`](../../doc/models/api-v1-sites-beacons-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesBeacons404ErrorException`](../../doc/models/api-v1-sites-beacons-404-error-exception.md) |


# Update Site Beacons

Update Site Beacon

```python
def update_site_beacons(self,
                       site_id,
                       beacon_id,
                       body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `beacon_id` | `uuid\|string` | Template, Required | - |
| `body` | [`Beacon`](../../doc/models/beacon.md) | Body, Optional | Request Body |

## Response Type

[`Beacon`](../../doc/models/beacon.md)

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

beacon_id = '000000ab-00ab-00ab-00ab-0000000000ab'

body = Beacon(
    eddystone_instance='string',
    eddystone_namespace='string',
    eddystone_url='string',
    ibeacon_major=0,
    ibeacon_minor=0,
    ibeacon_uuid='b069b358-4c97-5319-1f8c-7c5ca64d6ab1',
    mac='string',
    map_id='b069b358-4c97-5319-1f8c-7c5ca64d6ab1',
    name='string',
    power=0,
    mtype=Type4Enum.EDDYSTONEUID,
    x=0,
    y=0
)

result = sites_beacons_controller.update_site_beacons(
    site_id,
    beacon_id,
    body
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "created_time": 0,
  "eddystone_instance": "string",
  "eddystone_namespace": "string",
  "eddystone_url": "string",
  "ibeacon_major": 0,
  "ibeacon_minor": 0,
  "ibeacon_uuid": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
  "id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
  "mac": "string",
  "map_id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
  "modified_time": 0,
  "name": "string",
  "org_id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
  "power": 0,
  "site_id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
  "type": "eddystone-uid",
  "x": 0,
  "y": 0
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesBeacons401ErrorException`](../../doc/models/api-v1-sites-beacons-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesBeacons403ErrorException`](../../doc/models/api-v1-sites-beacons-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesBeacons404ErrorException`](../../doc/models/api-v1-sites-beacons-404-error-exception.md) |

