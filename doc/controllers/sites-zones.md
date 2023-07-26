# Sites Zones

```python
sites_zones_controller = client.sites_zones
```

## Class Name

`SitesZonesController`

## Methods

* [List Site Zones](../../doc/controllers/sites-zones.md#list-site-zones)
* [Create Site Zone](../../doc/controllers/sites-zones.md#create-site-zone)
* [Delete Site Zone](../../doc/controllers/sites-zones.md#delete-site-zone)
* [Get Site Zone](../../doc/controllers/sites-zones.md#get-site-zone)
* [Update Site Zone](../../doc/controllers/sites-zones.md#update-site-zone)
* [Count Site Zone Sessions](../../doc/controllers/sites-zones.md#count-site-zone-sessions)
* [Search Site Zone Sessions](../../doc/controllers/sites-zones.md#search-site-zone-sessions)


# List Site Zones

Get List of Site Zones

```python
def list_site_zones(self,
                   site_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |

## Response Type

[`List of Zone`](../../doc/models/zone.md)

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

result = sites_zones_controller.list_site_zones(site_id)
print(result)
```

## Example Response *(as JSON)*

```json
[
  {
    "created_time": 0,
    "id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
    "map_id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
    "modified_time": 0,
    "name": "string",
    "org_id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
    "site_id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
    "vertices": [
      {
        "x": 0,
        "y": 0
      }
    ]
  }
]
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesZones401ErrorException`](../../doc/models/api-v1-sites-zones-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesZones403ErrorException`](../../doc/models/api-v1-sites-zones-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesZones404ErrorException`](../../doc/models/api-v1-sites-zones-404-error-exception.md) |


# Create Site Zone

Create Site Zone

```python
def create_site_zone(self,
                    site_id,
                    body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `body` | [`Zone`](../../doc/models/zone.md) | Body, Optional | Request Body |

## Response Type

[`Zone`](../../doc/models/zone.md)

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

body = Zone(
    map_id='b069b358-4c97-5319-1f8c-7c5ca64d6ab1',
    name='string',
    vertices=[
        Vertex(
            x=0,
            y=0
        )
    ]
)

result = sites_zones_controller.create_site_zone(
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
  "map_id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
  "modified_time": 0,
  "name": "string",
  "org_id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
  "site_id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
  "vertices": [
    {
      "x": 0,
      "y": 0
    }
  ]
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesZones401ErrorException`](../../doc/models/api-v1-sites-zones-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesZones403ErrorException`](../../doc/models/api-v1-sites-zones-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesZones404ErrorException`](../../doc/models/api-v1-sites-zones-404-error-exception.md) |


# Delete Site Zone

Delete Site Zone

```python
def delete_site_zone(self,
                    site_id,
                    zone_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `zone_id` | `uuid\|string` | Template, Required | - |

## Response Type

`object`

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

zone_id = '000000ab-00ab-00ab-00ab-0000000000ab'

result = sites_zones_controller.delete_site_zone(
    site_id,
    zone_id
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesZones401ErrorException`](../../doc/models/api-v1-sites-zones-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesZones403ErrorException`](../../doc/models/api-v1-sites-zones-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesZones404ErrorException`](../../doc/models/api-v1-sites-zones-404-error-exception.md) |


# Get Site Zone

Get Site Zone Details

```python
def get_site_zone(self,
                 site_id,
                 zone_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `zone_id` | `uuid\|string` | Template, Required | - |

## Response Type

[`Zone`](../../doc/models/zone.md)

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

zone_id = '000000ab-00ab-00ab-00ab-0000000000ab'

result = sites_zones_controller.get_site_zone(
    site_id,
    zone_id
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "created_time": 0,
  "id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
  "map_id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
  "modified_time": 0,
  "name": "string",
  "org_id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
  "site_id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
  "vertices": [
    {
      "x": 0,
      "y": 0
    }
  ]
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesZones401ErrorException`](../../doc/models/api-v1-sites-zones-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesZones403ErrorException`](../../doc/models/api-v1-sites-zones-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesZones404ErrorException`](../../doc/models/api-v1-sites-zones-404-error-exception.md) |


# Update Site Zone

Update Site Zone

```python
def update_site_zone(self,
                    site_id,
                    zone_id,
                    body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `zone_id` | `uuid\|string` | Template, Required | - |
| `body` | [`Zone`](../../doc/models/zone.md) | Body, Optional | Request Body |

## Response Type

[`Zone`](../../doc/models/zone.md)

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

zone_id = '000000ab-00ab-00ab-00ab-0000000000ab'

body = Zone(
    map_id='b069b358-4c97-5319-1f8c-7c5ca64d6ab1',
    name='string',
    vertices=[
        Vertex(
            x=0,
            y=0
        )
    ]
)

result = sites_zones_controller.update_site_zone(
    site_id,
    zone_id,
    body
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "created_time": 0,
  "id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
  "map_id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
  "modified_time": 0,
  "name": "string",
  "org_id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
  "site_id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
  "vertices": [
    {
      "x": 0,
      "y": 0
    }
  ]
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesZones401ErrorException`](../../doc/models/api-v1-sites-zones-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesZones403ErrorException`](../../doc/models/api-v1-sites-zones-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesZones404ErrorException`](../../doc/models/api-v1-sites-zones-404-error-exception.md) |


# Count Site Zone Sessions

Count Site Zone Sessions

```python
def count_site_zone_sessions(self,
                            site_id,
                            zone_type,
                            distinct='scope_id',
                            user_type='client',
                            user=None,
                            scope_id=None,
                            scope='site',
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
| `zone_type` | [`ZoneTypeEnum`](../../doc/models/zone-type-enum.md) | Template, Required | - |
| `distinct` | [`Distinct24Enum`](../../doc/models/distinct-24-enum.md) | Query, Optional | **Default**: `'scope_id'` |
| `user_type` | [`UserTypeEnum`](../../doc/models/user-type-enum.md) | Query, Optional | user type<br>**Default**: `'client'` |
| `user` | `string` | Query, Optional | client MAC / Asset MAC / SDK UUID |
| `scope_id` | `string` | Query, Optional | if `scope`==`map`/`zone`/`rssizone`, the scope id |
| `scope` | [`Scope19Enum`](../../doc/models/scope-19-enum.md) | Query, Optional | scope<br>**Default**: `'site'` |
| `page` | `int` | Query, Optional | **Default**: `1`<br>**Constraints**: `>= 1` |
| `limit` | `int` | Query, Optional | **Default**: `100`<br>**Constraints**: `>= 0` |
| `start` | `int` | Query, Optional | **Default**: `0`<br>**Constraints**: `>= 0` |
| `end` | `int` | Query, Optional | **Default**: `0`<br>**Constraints**: `>= 0` |
| `duration` | `string` | Query, Optional | For historical stats and/or logs where time range is needed, you can specify the time range in a few different ways:<br><br>* ?start=1430000000&end=1430864000	specify the start / end<br>* ?end=1430864000&duration=1d	specify end time and duration<br>* ?duration=1d	specify duration, end will be now() in seconds<br>**Default**: `'1d'` |

## Response Type

[`ApiV1SitesCountResponse`](../../doc/models/api-v1-sites-count-response.md)

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

zone_type = ZoneTypeEnum.ZONES

distinct = Distinct24Enum.SCOPE_ID

user_type = UserTypeEnum.CLIENT

scope = Scope19Enum.SITE

page = 1

limit = 100

start = 0

end = 0

duration = '10m'

result = sites_zones_controller.count_site_zone_sessions(
    site_id,
    zone_type,
    distinct,
    user_type,
    scope,
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
  "end": 1531862583,
  "results": [
    {
      "count": 18,
      "scope_id": "f0c38357-9370-4506-84f9-0f94a63faddd"
    },
    {
      "count": 7,
      "scope_id": "a002eb82-6d08-4556-b8c5-2f2547a7c7f8"
    },
    {
      "count": 5,
      "scope_id": "85fbba9e-4e12-11e6-9188-0242ac110007"
    }
  ],
  "start": 1531776183,
  "total": 3
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesCount401ErrorException`](../../doc/models/api-v1-sites-count-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesCount403ErrorException`](../../doc/models/api-v1-sites-count-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesCount404ErrorException`](../../doc/models/api-v1-sites-count-404-error-exception.md) |


# Search Site Zone Sessions

Search Zone Sessions

```python
def search_site_zone_sessions(self,
                             site_id,
                             zone_type,
                             user_type='client',
                             user=None,
                             scope_id=None,
                             scope='site',
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
| `zone_type` | [`ZoneTypeEnum`](../../doc/models/zone-type-enum.md) | Template, Required | - |
| `user_type` | [`UserTypeEnum`](../../doc/models/user-type-enum.md) | Query, Optional | user type, client (default) / sdkclient / asset<br>**Default**: `'client'` |
| `user` | `string` | Query, Optional | client MAC / Asset MAC / SDK UUID |
| `scope_id` | `string` | Query, Optional | if `scope`==`map`/`zone`/`rssizone`, the scope id |
| `scope` | [`Scope19Enum`](../../doc/models/scope-19-enum.md) | Query, Optional | scope<br>**Default**: `'site'` |
| `page` | `int` | Query, Optional | **Default**: `1`<br>**Constraints**: `>= 1` |
| `limit` | `int` | Query, Optional | **Default**: `100`<br>**Constraints**: `>= 0` |
| `start` | `int` | Query, Optional | **Default**: `0`<br>**Constraints**: `>= 0` |
| `end` | `int` | Query, Optional | **Default**: `0`<br>**Constraints**: `>= 0` |
| `duration` | `string` | Query, Optional | For historical stats and/or logs where time range is needed, you can specify the time range in a few different ways:<br><br>* ?start=1430000000&end=1430864000	specify the start / end<br>* ?end=1430864000&duration=1d	specify end time and duration<br>* ?duration=1d	specify duration, end will be now() in seconds<br>**Default**: `'1d'` |

## Response Type

[`ApiV1SitesVisitsSearchResponse`](../../doc/models/api-v1-sites-visits-search-response.md)

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

zone_type = ZoneTypeEnum.ZONES

user_type = UserTypeEnum.CLIENT

scope = Scope19Enum.SITE

page = 1

limit = 100

start = 0

end = 0

duration = '10m'

result = sites_zones_controller.search_site_zone_sessions(
    site_id,
    zone_type,
    user_type,
    scope,
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
  "end": 1541705289.769911,
  "limit": 2,
  "next": "/api/v1/sites/67970e46-4e12-11e6-9188-0242ac110007/zones/visits/search?limit=2&end=1541705247.000&scope_id=85fbba9e-4e12-11e6-9188-0242ac110007&user_type=asset&start=1541618889.77",
  "results": [
    {
      "enter": 1541705254,
      "scope": "map",
      "timestamp": 1541705254,
      "user": "c4b301c81166"
    },
    {
      "enter": 1541705247,
      "scope": "map",
      "timestamp": 1541705247,
      "user": "c57bbb6a1277"
    }
  ],
  "start": 1541618889.769886,
  "total": 5892
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesVisitsSearch401ErrorException`](../../doc/models/api-v1-sites-visits-search-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesVisitsSearch403ErrorException`](../../doc/models/api-v1-sites-visits-search-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesVisitsSearch404ErrorException`](../../doc/models/api-v1-sites-visits-search-404-error-exception.md) |

