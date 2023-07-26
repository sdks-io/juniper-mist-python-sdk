# Sites Assets

```python
sites_assets_controller = client.sites_assets
```

## Class Name

`SitesAssetsController`

## Methods

* [List Site Assets](../../doc/controllers/sites-assets.md#list-site-assets)
* [Create Site Asset](../../doc/controllers/sites-assets.md#create-site-asset)
* [Import Site Assets](../../doc/controllers/sites-assets.md#import-site-assets)
* [Delete Site Asset](../../doc/controllers/sites-assets.md#delete-site-asset)
* [Get Site Asset](../../doc/controllers/sites-assets.md#get-site-asset)
* [Update Site Asset](../../doc/controllers/sites-assets.md#update-site-asset)
* [Count Site Assets](../../doc/controllers/sites-assets.md#count-site-assets)
* [Search Site Assets](../../doc/controllers/sites-assets.md#search-site-assets)
* [Get Site Assets of Interest](../../doc/controllers/sites-assets.md#get-site-assets-of-interest)


# List Site Assets

Get List of Site Assets

```python
def list_site_assets(self,
                    site_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |

## Response Type

[`List of Asset`](../../doc/models/asset.md)

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

result = sites_assets_controller.list_site_assets(site_id)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesAssets401ErrorException`](../../doc/models/api-v1-sites-assets-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesAssets403ErrorException`](../../doc/models/api-v1-sites-assets-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesAssets404ErrorException`](../../doc/models/api-v1-sites-assets-404-error-exception.md) |


# Create Site Asset

Create Site Asset

```python
def create_site_asset(self,
                     site_id,
                     body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `body` | [`Asset`](../../doc/models/asset.md) | Body, Optional | Request Body |

## Response Type

[`Asset`](../../doc/models/asset.md)

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

result = sites_assets_controller.create_site_asset(site_id)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "created_time": 0,
  "id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
  "mac": "string",
  "map_id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
  "modified_time": 0,
  "name": "string",
  "org_id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
  "site_id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
  "tag_id": "6f4bf402-45f9-2a56-6c8b-7f83d3bc98e9"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesAssets401ErrorException`](../../doc/models/api-v1-sites-assets-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesAssets403ErrorException`](../../doc/models/api-v1-sites-assets-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesAssets404ErrorException`](../../doc/models/api-v1-sites-assets-404-error-exception.md) |


# Import Site Assets

Impert Site Assets.

It can be done via a CSV file or a JSON payload.

## CSV File Format

```csv
name,mac
"asset_name",5c5b53010101
```

```python
def import_site_assets(self,
                      site_id,
                      upsert='False',
                      file=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `upsert` | [`UpsertEnum`](../../doc/models/upsert-enum.md) | Query, Optional | API will replace the assets with same mac if provided `upsert`==`True`, otherwise will report in errors in response.<br>**Default**: `'False'` |
| `file` | `string` | Form, Optional | CSV file |

## Response Type

`object`

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

upsert = UpsertEnum.ENUM_FALSE

result = sites_assets_controller.import_site_assets(
    site_id,
    upsert
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesAssetsImport401ErrorException`](../../doc/models/api-v1-sites-assets-import-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesAssetsImport403ErrorException`](../../doc/models/api-v1-sites-assets-import-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesAssetsImport404ErrorException`](../../doc/models/api-v1-sites-assets-import-404-error-exception.md) |


# Delete Site Asset

Delete Site Asset

```python
def delete_site_asset(self,
                     site_id,
                     asset_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `asset_id` | `uuid\|string` | Template, Required | - |

## Response Type

`object`

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

asset_id = '000000ab-00ab-00ab-00ab-0000000000ab'

result = sites_assets_controller.delete_site_asset(
    site_id,
    asset_id
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesAssets401ErrorException`](../../doc/models/api-v1-sites-assets-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesAssets403ErrorException`](../../doc/models/api-v1-sites-assets-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesAssets404ErrorException`](../../doc/models/api-v1-sites-assets-404-error-exception.md) |


# Get Site Asset

Get Site Asset Details

```python
def get_site_asset(self,
                  site_id,
                  asset_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `asset_id` | `uuid\|string` | Template, Required | - |

## Response Type

[`Asset`](../../doc/models/asset.md)

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

asset_id = '000000ab-00ab-00ab-00ab-0000000000ab'

result = sites_assets_controller.get_site_asset(
    site_id,
    asset_id
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "created_time": 0,
  "id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
  "mac": "string",
  "map_id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
  "modified_time": 0,
  "name": "string",
  "org_id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
  "site_id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
  "tag_id": "6f4bf402-45f9-2a56-6c8b-7f83d3bc98e9"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesAssets401ErrorException`](../../doc/models/api-v1-sites-assets-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesAssets403ErrorException`](../../doc/models/api-v1-sites-assets-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesAssets404ErrorException`](../../doc/models/api-v1-sites-assets-404-error-exception.md) |


# Update Site Asset

Update Site Asset

```python
def update_site_asset(self,
                     site_id,
                     asset_id,
                     body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `asset_id` | `uuid\|string` | Template, Required | - |
| `body` | [`Asset`](../../doc/models/asset.md) | Body, Optional | Request Body |

## Response Type

[`Asset`](../../doc/models/asset.md)

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

asset_id = '000000ab-00ab-00ab-00ab-0000000000ab'

result = sites_assets_controller.update_site_asset(
    site_id,
    asset_id
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "created_time": 0,
  "id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
  "mac": "string",
  "map_id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
  "modified_time": 0,
  "name": "string",
  "org_id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
  "site_id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
  "tag_id": "6f4bf402-45f9-2a56-6c8b-7f83d3bc98e9"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesAssets401ErrorException`](../../doc/models/api-v1-sites-assets-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesAssets403ErrorException`](../../doc/models/api-v1-sites-assets-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesAssets404ErrorException`](../../doc/models/api-v1-sites-assets-404-error-exception.md) |


# Count Site Assets

Count Asset by distinct field

```python
def count_site_assets(self,
                     site_id,
                     distinct='map_id')
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `distinct` | [`Distinct17Enum`](../../doc/models/distinct-17-enum.md) | Query, Optional | **Default**: `'map_id'` |

## Response Type

[`Count`](../../doc/models/count.md)

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

distinct = Distinct17Enum.MAP_ID

result = sites_assets_controller.count_site_assets(
    site_id,
    distinct
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "distinct": "string",
  "end": 0,
  "limit": 0,
  "percentage": 0,
  "results": [
    {
      "count": 0,
      "property": "string"
    }
  ],
  "start": 0,
  "total": 0
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesStatsAssetsCount401ErrorException`](../../doc/models/api-v1-sites-stats-assets-count-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesStatsAssetsCount403ErrorException`](../../doc/models/api-v1-sites-stats-assets-count-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesStatsAssetsCount404ErrorException`](../../doc/models/api-v1-sites-stats-assets-count-404-error-exception.md) |


# Search Site Assets

Assets Search

```python
def search_site_assets(self,
                      site_id,
                      mac=None,
                      map_id=None,
                      ibeacon_uuid=None,
                      ibeacon_major=None,
                      ibeacon_minor=None,
                      eddystone_uid_namespace=None,
                      eddystone_uid_instance=None,
                      eddystone_url=None,
                      device_name=None,
                      by=None,
                      name=None,
                      ap_mac=None,
                      beam=None,
                      rssi=None,
                      limit=100,
                      start=0,
                      end=0,
                      duration='1d')
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `mac` | `string` | Query, Optional | - |
| `map_id` | `uuid\|string` | Query, Optional | - |
| `ibeacon_uuid` | `uuid\|string` | Query, Optional | - |
| `ibeacon_major` | `int` | Query, Optional | - |
| `ibeacon_minor` | `int` | Query, Optional | - |
| `eddystone_uid_namespace` | `string` | Query, Optional | - |
| `eddystone_uid_instance` | `string` | Query, Optional | - |
| `eddystone_url` | `string` | Query, Optional | - |
| `device_name` | `string` | Query, Optional | - |
| `by` | `string` | Query, Optional | - |
| `name` | `string` | Query, Optional | - |
| `ap_mac` | `string` | Query, Optional | - |
| `beam` | `string` | Query, Optional | - |
| `rssi` | `string` | Query, Optional | - |
| `limit` | `int` | Query, Optional | **Default**: `100`<br>**Constraints**: `>= 0` |
| `start` | `int` | Query, Optional | **Default**: `0`<br>**Constraints**: `>= 0` |
| `end` | `int` | Query, Optional | **Default**: `0`<br>**Constraints**: `>= 0` |
| `duration` | `string` | Query, Optional | For historical stats and/or logs where time range is needed, you can specify the time range in a few different ways:<br><br>* ?start=1430000000&end=1430864000	specify the start / end<br>* ?end=1430864000&duration=1d	specify end time and duration<br>* ?duration=1d	specify duration, end will be now() in seconds<br>**Default**: `'1d'` |

## Response Type

[`AssetsArrayStatsSearch`](../../doc/models/assets-array-stats-search.md)

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

limit = 100

start = 0

end = 0

duration = '10m'

result = sites_assets_controller.search_site_assets(
    site_id,
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
  "end": 0,
  "limit": 0,
  "next": "string",
  "results": [
    {
      "battery_voltage": 0,
      "eddystone_uid_instance": "string",
      "eddystone_uid_namespace": "string",
      "eddystone_url_url": "string",
      "ibeacon_major": 0,
      "ibeacon_minor": 0,
      "ibeacon_uuid": "1f89bc00-d0af-481b-82fe-a6629259a39f",
      "last_seen": 0,
      "mac": "string",
      "map_id": "09d2b626-2e4e-45ef-a3c4-e6aeb6c83db1",
      "name": "string",
      "rssizones": [
        {
          "id": "476f6eca-6276-4993-bfeb-5dcbbbba6f08",
          "since": 0
        }
      ],
      "x": 0,
      "y": 0,
      "zones": [
        {
          "id": "475f6eca-6276-4993-bfeb-5ecbbbba6f08",
          "since": 0
        }
      ]
    }
  ],
  "start": 0,
  "total": 0
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesStatsAssetsSearch401ErrorException`](../../doc/models/api-v1-sites-stats-assets-search-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesStatsAssetsSearch403ErrorException`](../../doc/models/api-v1-sites-stats-assets-search-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesStatsAssetsSearch404ErrorException`](../../doc/models/api-v1-sites-stats-assets-search-404-error-exception.md) |


# Get Site Assets of Interest

Get a list of BLE beacons that matches Asset or AssetFilter

```python
def get_site_assets_of_interest(self,
                               site_id,
                               duration='1d',
                               start=0,
                               end=0,
                               page=1,
                               limit=100)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `duration` | `string` | Query, Optional | For historical stats and/or logs where time range is needed, you can specify the time range in a few different ways:<br><br>* ?start=1430000000&end=1430864000	specify the start / end<br>* ?end=1430864000&duration=1d	specify end time and duration<br>* ?duration=1d	specify duration, end will be now() in seconds<br>**Default**: `'1d'` |
| `start` | `int` | Query, Optional | **Default**: `0`<br>**Constraints**: `>= 0` |
| `end` | `int` | Query, Optional | **Default**: `0`<br>**Constraints**: `>= 0` |
| `page` | `int` | Query, Optional | **Default**: `1`<br>**Constraints**: `>= 1` |
| `limit` | `int` | Query, Optional | **Default**: `100`<br>**Constraints**: `>= 0` |

## Response Type

[`List of AssetOfInterest`](../../doc/models/asset-of-interest.md)

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

duration = '10m'

start = 0

end = 0

page = 1

limit = 100

result = sites_assets_controller.get_site_assets_of_interest(
    site_id,
    duration,
    start,
    end,
    page,
    limit
)
print(result)
```

## Example Response *(as JSON)*

```json
[
  {
    "_checkpoint_prep": 0,
    "_checkpoint_preparer": 0,
    "_checkpoint_scan": 0,
    "_id": "string",
    "_timestamp": 0,
    "_ttl": 0,
    "ap_mac": "string",
    "beam": 0,
    "by": "string",
    "curr_site": "string",
    "device_name": "string",
    "id": "string",
    "last_seen": 0,
    "mac": "string",
    "manufacture": "string",
    "map_id": "string",
    "name": "string",
    "rssi": 0
  }
]
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesStatsFilteredAssets401ErrorException`](../../doc/models/api-v1-sites-stats-filtered-assets-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesStatsFilteredAssets403ErrorException`](../../doc/models/api-v1-sites-stats-filtered-assets-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesStatsFilteredAssets404ErrorException`](../../doc/models/api-v1-sites-stats-filtered-assets-404-error-exception.md) |

