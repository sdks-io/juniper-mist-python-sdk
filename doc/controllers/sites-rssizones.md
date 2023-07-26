# Sites Rssizones

```python
sites_rssizones_controller = client.sites_rssizones
```

## Class Name

`SitesRssizonesController`

## Methods

* [List Site Rssi Zones](../../doc/controllers/sites-rssizones.md#list-site-rssi-zones)
* [Create Site Rssi Zone](../../doc/controllers/sites-rssizones.md#create-site-rssi-zone)
* [Delete Site Rssi Zone](../../doc/controllers/sites-rssizones.md#delete-site-rssi-zone)
* [Get Site Rssi Zone](../../doc/controllers/sites-rssizones.md#get-site-rssi-zone)
* [Update Site Rssi Zone](../../doc/controllers/sites-rssizones.md#update-site-rssi-zone)


# List Site Rssi Zones

Get List of Site RSSI Zone (RSSI-based)

```python
def list_site_rssi_zones(self,
                        site_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |

## Response Type

[`List of Rssizone`](../../doc/models/rssizone.md)

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

result = sites_rssizones_controller.list_site_rssi_zones(site_id)
print(result)
```

## Example Response *(as JSON)*

```json
[
  {
    "created_time": 0,
    "devices": [
      {
        "device_id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
        "rssi": 0
      }
    ],
    "id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
    "modified_time": 0,
    "name": "string",
    "org_id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1"
  }
]
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesRssizones401ErrorException`](../../doc/models/api-v1-sites-rssizones-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesRssizones403ErrorException`](../../doc/models/api-v1-sites-rssizones-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesRssizones404ErrorException`](../../doc/models/api-v1-sites-rssizones-404-error-exception.md) |


# Create Site Rssi Zone

Create RSSI Zone

```python
def create_site_rssi_zone(self,
                         site_id,
                         body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `body` | [`Rssizone`](../../doc/models/rssizone.md) | Body, Optional | Request Body |

## Response Type

[`Rssizone`](../../doc/models/rssizone.md)

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

body = Rssizone(
    devices=[
        Device(
            device_id='b069b358-4c97-5319-1f8c-7c5ca64d6ab1',
            rssi=0
        )
    ],
    name='string'
)

result = sites_rssizones_controller.create_site_rssi_zone(
    site_id,
    body
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "created_time": 0,
  "devices": [
    {
      "device_id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
      "rssi": 0
    }
  ],
  "id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
  "modified_time": 0,
  "name": "string",
  "org_id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesRssizones401ErrorException`](../../doc/models/api-v1-sites-rssizones-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesRssizones403ErrorException`](../../doc/models/api-v1-sites-rssizones-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesRssizones404ErrorException`](../../doc/models/api-v1-sites-rssizones-404-error-exception.md) |


# Delete Site Rssi Zone

Delete Site RSSI Zone

```python
def delete_site_rssi_zone(self,
                         site_id,
                         rssizone_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `rssizone_id` | `uuid\|string` | Template, Required | - |

## Response Type

`object`

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

rssizone_id = '000000ab-00ab-00ab-00ab-0000000000ab'

result = sites_rssizones_controller.delete_site_rssi_zone(
    site_id,
    rssizone_id
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesRssizones401ErrorException`](../../doc/models/api-v1-sites-rssizones-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesRssizones403ErrorException`](../../doc/models/api-v1-sites-rssizones-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesRssizones404ErrorException`](../../doc/models/api-v1-sites-rssizones-404-error-exception.md) |


# Get Site Rssi Zone

Get Site RSSI Zone details

```python
def get_site_rssi_zone(self,
                      site_id,
                      rssizone_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `rssizone_id` | `uuid\|string` | Template, Required | - |

## Response Type

[`List of Rssizone`](../../doc/models/rssizone.md)

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

rssizone_id = '000000ab-00ab-00ab-00ab-0000000000ab'

result = sites_rssizones_controller.get_site_rssi_zone(
    site_id,
    rssizone_id
)
print(result)
```

## Example Response *(as JSON)*

```json
[
  {
    "created_time": 0,
    "devices": [
      {
        "device_id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
        "rssi": 0
      }
    ],
    "id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
    "modified_time": 0,
    "name": "string",
    "org_id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
    "site_id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1"
  }
]
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesRssizones401ErrorException`](../../doc/models/api-v1-sites-rssizones-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesRssizones403ErrorException`](../../doc/models/api-v1-sites-rssizones-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesRssizones404ErrorException`](../../doc/models/api-v1-sites-rssizones-404-error-exception.md) |


# Update Site Rssi Zone

Update Site RSSI Zone

```python
def update_site_rssi_zone(self,
                         site_id,
                         rssizone_id,
                         body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `rssizone_id` | `uuid\|string` | Template, Required | - |
| `body` | [`Rssizone`](../../doc/models/rssizone.md) | Body, Optional | Request Body |

## Response Type

[`Rssizone`](../../doc/models/rssizone.md)

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

rssizone_id = '000000ab-00ab-00ab-00ab-0000000000ab'

body = Rssizone(
    devices=[
        Device(
            device_id='b069b358-4c97-5319-1f8c-7c5ca64d6ab1',
            rssi=0
        )
    ],
    name='string'
)

result = sites_rssizones_controller.update_site_rssi_zone(
    site_id,
    rssizone_id,
    body
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "created_time": 0,
  "devices": [
    {
      "device_id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
      "rssi": 0
    }
  ],
  "id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
  "modified_time": 0,
  "name": "string",
  "org_id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
  "site_id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesRssizones401ErrorException`](../../doc/models/api-v1-sites-rssizones-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesRssizones403ErrorException`](../../doc/models/api-v1-sites-rssizones-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesRssizones404ErrorException`](../../doc/models/api-v1-sites-rssizones-404-error-exception.md) |

