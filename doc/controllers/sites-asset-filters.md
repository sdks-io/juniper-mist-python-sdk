# Sites Asset Filters

```python
sites_asset_filters_controller = client.sites_asset_filters
```

## Class Name

`SitesAssetFiltersController`

## Methods

* [List Site Asset Filters](../../doc/controllers/sites-asset-filters.md#list-site-asset-filters)
* [Create Site Asset Filters](../../doc/controllers/sites-asset-filters.md#create-site-asset-filters)
* [Delete Site Asset Filter](../../doc/controllers/sites-asset-filters.md#delete-site-asset-filter)
* [Get Site Asset Filter](../../doc/controllers/sites-asset-filters.md#get-site-asset-filter)
* [Update Site Asset Filter](../../doc/controllers/sites-asset-filters.md#update-site-asset-filter)


# List Site Asset Filters

Get List of Site Asset Filters

```python
def list_site_asset_filters(self,
                           site_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |

## Response Type

[`List of AssetFilter`](../../doc/models/asset-filter.md)

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

result = sites_asset_filters_controller.list_site_asset_filters(site_id)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesAssetfilters401ErrorException`](../../doc/models/api-v1-sites-assetfilters-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesAssetfilters403ErrorException`](../../doc/models/api-v1-sites-assetfilters-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesAssetfilters404ErrorException`](../../doc/models/api-v1-sites-assetfilters-404-error-exception.md) |


# Create Site Asset Filters

Create Site Asset Filter

```python
def create_site_asset_filters(self,
                             site_id,
                             body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `body` | [`AssetFilter`](../../doc/models/asset-filter.md) | Body, Optional | Request Body |

## Response Type

[`AssetFilter`](../../doc/models/asset-filter.md)

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

body = AssetFilter(
    name='Visitor Tags',
    eddystone_uid_namespace='2818e3868dec25629ede',
    eddystone_url='https://www.abc.com',
    ibeacon_major=13,
    ibeacon_uuid='f3f17139-704a-f03a-2786-0400279e37c3',
    mfg_company_id=935,
    service_uuid='0000fe6a-0000-1000-8000-0030459b3cfb'
)

result = sites_asset_filters_controller.create_site_asset_filters(
    site_id,
    body
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "created_time": 0,
  "disasbled": true,
  "eddystone_uid_namespace": "string",
  "eddystone_url": "string",
  "for_site": true,
  "ibeacon_major": 0,
  "ibeacon_uuid": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
  "id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
  "mfg_company_id": 0,
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
| 401 | Unauthorized | [`ApiV1SitesAssetfilters401ErrorException`](../../doc/models/api-v1-sites-assetfilters-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesAssetfilters403ErrorException`](../../doc/models/api-v1-sites-assetfilters-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesAssetfilters404ErrorException`](../../doc/models/api-v1-sites-assetfilters-404-error-exception.md) |


# Delete Site Asset Filter

Deletes an existing BLE asset filter for the given site.

```python
def delete_site_asset_filter(self,
                            site_id,
                            assetfilter_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `assetfilter_id` | `uuid\|string` | Template, Required | - |

## Response Type

`object`

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

assetfilter_id = '000000ab-00ab-00ab-00ab-0000000000ab'

result = sites_asset_filters_controller.delete_site_asset_filter(
    site_id,
    assetfilter_id
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesAssetfilters401ErrorException`](../../doc/models/api-v1-sites-assetfilters-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesAssetfilters403ErrorException`](../../doc/models/api-v1-sites-assetfilters-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesAssetfilters404ErrorException`](../../doc/models/api-v1-sites-assetfilters-404-error-exception.md) |


# Get Site Asset Filter

Get Site Asset Filter Details

```python
def get_site_asset_filter(self,
                         site_id,
                         assetfilter_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `assetfilter_id` | `uuid\|string` | Template, Required | - |

## Response Type

[`AssetFilter`](../../doc/models/asset-filter.md)

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

assetfilter_id = '000000ab-00ab-00ab-00ab-0000000000ab'

result = sites_asset_filters_controller.get_site_asset_filter(
    site_id,
    assetfilter_id
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "created_time": 0,
  "disasbled": true,
  "eddystone_uid_namespace": "string",
  "eddystone_url": "string",
  "for_site": true,
  "ibeacon_major": 0,
  "ibeacon_uuid": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
  "id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
  "mfg_company_id": 0,
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
| 401 | Unauthorized | [`ApiV1SitesAssetfilters401ErrorException`](../../doc/models/api-v1-sites-assetfilters-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesAssetfilters403ErrorException`](../../doc/models/api-v1-sites-assetfilters-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesAssetfilters404ErrorException`](../../doc/models/api-v1-sites-assetfilters-404-error-exception.md) |


# Update Site Asset Filter

Updates an existing BLE asset filter for the given site.

```python
def update_site_asset_filter(self,
                            site_id,
                            assetfilter_id,
                            body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `assetfilter_id` | `uuid\|string` | Template, Required | - |
| `body` | [`AssetFilter`](../../doc/models/asset-filter.md) | Body, Optional | Request Body |

## Response Type

[`AssetFilter`](../../doc/models/asset-filter.md)

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

assetfilter_id = '000000ab-00ab-00ab-00ab-0000000000ab'

body = AssetFilter(
    name='Visitor Tags',
    eddystone_uid_namespace='2818e3868dec25629ede',
    eddystone_url='https://www.abc.com',
    ibeacon_major=13,
    ibeacon_uuid='f3f17139-704a-f03a-2786-0400279e37c3',
    mfg_company_id=935,
    service_uuid='0000fe6a-0000-1000-8000-0030459b3cfb'
)

result = sites_asset_filters_controller.update_site_asset_filter(
    site_id,
    assetfilter_id,
    body
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "created_time": 0,
  "disasbled": true,
  "eddystone_uid_namespace": "string",
  "eddystone_url": "string",
  "for_site": true,
  "ibeacon_major": 0,
  "ibeacon_uuid": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
  "id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
  "mfg_company_id": 0,
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
| 401 | Unauthorized | [`ApiV1SitesAssetfilters401ErrorException`](../../doc/models/api-v1-sites-assetfilters-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesAssetfilters403ErrorException`](../../doc/models/api-v1-sites-assetfilters-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesAssetfilters404ErrorException`](../../doc/models/api-v1-sites-assetfilters-404-error-exception.md) |

