# Sites Maps

```python
sites_maps_controller = client.sites_maps
```

## Class Name

`SitesMapsController`

## Methods

* [List Site Maps](../../doc/controllers/sites-maps.md#list-site-maps)
* [Create Site Map](../../doc/controllers/sites-maps.md#create-site-map)
* [Import Site Maps](../../doc/controllers/sites-maps.md#import-site-maps)
* [Delete Site Map](../../doc/controllers/sites-maps.md#delete-site-map)
* [Get Site Map](../../doc/controllers/sites-maps.md#get-site-map)
* [Update Site Map](../../doc/controllers/sites-maps.md#update-site-map)
* [Delete Site Map Image](../../doc/controllers/sites-maps.md#delete-site-map-image)
* [Add Site Map Image](../../doc/controllers/sites-maps.md#add-site-map-image)
* [Replace Site Map Image](../../doc/controllers/sites-maps.md#replace-site-map-image)
* [Bulk Assign Site Aps to Map](../../doc/controllers/sites-maps.md#bulk-assign-site-aps-to-map)
* [Import Site Wayfindings](../../doc/controllers/sites-maps.md#import-site-wayfindings)


# List Site Maps

Get List of Site Maps

```python
def list_site_maps(self,
                  site_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |

## Response Type

[`List of Map`](../../doc/models/map.md)

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

result = sites_maps_controller.list_site_maps(site_id)
print(result)
```

## Example Response *(as JSON)*

```json
[
  {
    "created_time": 0,
    "flags": {},
    "height": 0,
    "height_m": 0,
    "id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
    "latlng_br": {
      "lat": "string",
      "lng": "string"
    },
    "latlng_tl": {
      "lat": "string",
      "lng": "string"
    },
    "locked": true,
    "modified_time": 0,
    "name": "string",
    "occupancy_limit": 0,
    "org_id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
    "orientation": 0,
    "origin_x": 0,
    "origin_y": 0,
    "ppm": 0,
    "site_id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
    "sitesurvey_path": [
      {
        "coordinate": "string",
        "id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
        "name": "string",
        "nodes": [
          {
            "edges": {
              "N2": "string"
            },
            "name": "string",
            "position": {
              "x": 0,
              "y": 0
            }
          }
        ]
      }
    ],
    "thumbnail_url": "string",
    "type": "image",
    "url": "string",
    "view": "roadmap",
    "wall_path": {
      "coordinate": "string",
      "nodes": [
        {
          "edges": {
            "N2": "string"
          },
          "name": "string",
          "position": {
            "x": 0,
            "y": 0
          }
        }
      ]
    },
    "wayfinding": {
      "micello": {
        "account_key": "string",
        "default_level_id": 0,
        "map_id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1"
      },
      "snap_to_path": true
    },
    "wayfinding_path": {
      "coordinate": "string",
      "nodes": [
        {
          "edges": {
            "N2": "string"
          },
          "name": "string",
          "position": {
            "x": 0,
            "y": 0
          }
        }
      ]
    },
    "width": 0,
    "width_m": 0
  }
]
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesMaps401ErrorException`](../../doc/models/api-v1-sites-maps-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesMaps403ErrorException`](../../doc/models/api-v1-sites-maps-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesMaps404ErrorException`](../../doc/models/api-v1-sites-maps-404-error-exception.md) |


# Create Site Map

Create Site Map

```python
def create_site_map(self,
                   site_id,
                   body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `body` | [`Map`](../../doc/models/map.md) | Body, Optional | Request Body |

## Response Type

[`Map`](../../doc/models/map.md)

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

body = Map(
    flags={},
    height=0,
    height_m=0,
    latlng_br=LatlngBr(
        lat='string',
        lng='string'
    ),
    latlng_tl=LatlngTl(
        lat='string',
        lng='string'
    ),
    locked=True,
    name='string',
    occupancy_limit=0,
    orientation=0,
    origin_x=0,
    origin_y=0,
    ppm=0,
    sitesurvey_path=[
        SitesurveyPath(
            coordinate='string',
            id='b069b358-4c97-5319-1f8c-7c5ca64d6ab1',
            name='string',
            nodes=[
                MapNode(
                    name='string',
                    edges={
                        "N2": 'string'
                    },
                    position=Position(
                        x=0,
                        y=0
                    )
                )
            ]
        )
    ],
    thumbnail_url='string',
    mtype=Type30Enum.IMAGE,
    url='string',
    view=ViewEnum.ROADMAP,
    wall_path=WallPath(
        coordinate='string',
        nodes=[
            MapNode(
                name='string',
                edges={
                    "N2": 'string'
                },
                position=Position(
                    x=0,
                    y=0
                )
            )
        ]
    ),
    wayfinding=Wayfinding(
        micello=Micello(
            account_key='string',
            default_level_id=0,
            map_id='b069b358-4c97-5319-1f8c-7c5ca64d6ab1'
        ),
        snap_to_path=True
    ),
    wayfinding_path=WayfindingPath(
        coordinate='string',
        nodes=[
            MapNode(
                name='string',
                edges={
                    "N2": 'string'
                },
                position=Position(
                    x=0,
                    y=0
                )
            )
        ]
    ),
    width=0,
    width_m=0
)

result = sites_maps_controller.create_site_map(
    site_id,
    body
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesMaps401ErrorException`](../../doc/models/api-v1-sites-maps-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesMaps403ErrorException`](../../doc/models/api-v1-sites-maps-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesMaps404ErrorException`](../../doc/models/api-v1-sites-maps-404-error-exception.md) |


# Import Site Maps

Import data from files is a multipart POST which has an file, an optional json, and an optional csv, to create floorplan, assign matching inventory to specific site, place ap if name or mac matches.

# Note

This endpoint (at the site level), the AP must be already assigned to the site to be placed on the floorplan. If you want to place APs from the Org inventory, it is required to use the endpoint at the Org level [importOrgMaps](#operation/importOrgMaps)

# CSV File Format

```csv
Vendor AP name,Mist AP Mac
US Office AP-2,5c:5b:35:00:00:02
US Office AP-3,5c5b35000002
```

```python
def import_site_maps(self,
                    site_id,
                    auto_deviceprofile_assignment=None,
                    csv=None,
                    file=None,
                    json=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `auto_deviceprofile_assignment` | `bool` | Form, Optional | whether to auto assign device to deviceprofile by name |
| `csv` | `string` | Form, Optional | csv file for ap name mapping, optional |
| `file` | `string` | Form, Optional | ekahau or ibwave file |
| `json` | [`Json`](../../doc/models/json.md) | Form, Optional | - |

## Response Type

[`ApiV1SitesMapsImportResponse`](../../doc/models/api-v1-sites-maps-import-response.md)

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

json = Json(
    vendor_name=VendorNameEnum.IBWAVE,
    import_all_floorplans=False,
    import_height=False,
    import_orientation=False
)

result = sites_maps_controller.import_site_maps(
    site_id,
    json
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "aps": [
    {
      "action": "ignored",
      "floorplan_id": "cbdb7f0b-3be0-4872-88f9-58790b509c23-j68kows8",
      "height": 3,
      "mac": "5c5b35000001",
      "orientation": 45
    },
    {
      "action": "placed",
      "height": 3,
      "mac": "5c5b35000001",
      "map_id": "845a23bf-bed9-e43c-4c86-6fa474be7ae5",
      "orientation": 45
    }
  ],
  "floorplans": [
    {
      "action": "ignored",
      "id": "cbdb7f0b-3be0-4872-88f9-58790b509c23-j68kows8",
      "map_id": "845a23bf-bed9-e43c-4c86-6fa474be7ae5",
      "name": "map1",
      "reason": "no aps placed"
    }
  ],
  "site_id": "4ac1dcf4-9d8b-7211-65c4-057819f0862b",
  "summary": {
    "num_ap_assigned": 1,
    "num_inv_assigned": 1,
    "num_map_assigned": 1
  }
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesMapsImport401ErrorException`](../../doc/models/api-v1-sites-maps-import-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesMapsImport403ErrorException`](../../doc/models/api-v1-sites-maps-import-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesMapsImport404ErrorException`](../../doc/models/api-v1-sites-maps-import-404-error-exception.md) |


# Delete Site Map

Delete Site Map

```python
def delete_site_map(self,
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

result = sites_maps_controller.delete_site_map(
    site_id,
    map_id
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesMaps401ErrorException`](../../doc/models/api-v1-sites-maps-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesMaps403ErrorException`](../../doc/models/api-v1-sites-maps-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesMaps404ErrorException`](../../doc/models/api-v1-sites-maps-404-error-exception.md) |


# Get Site Map

Get Site Map Details

```python
def get_site_map(self,
                site_id,
                map_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `map_id` | `uuid\|string` | Template, Required | - |

## Response Type

[`Map`](../../doc/models/map.md)

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

map_id = '000000ab-00ab-00ab-00ab-0000000000ab'

result = sites_maps_controller.get_site_map(
    site_id,
    map_id
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesMaps401ErrorException`](../../doc/models/api-v1-sites-maps-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesMaps403ErrorException`](../../doc/models/api-v1-sites-maps-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesMaps404ErrorException`](../../doc/models/api-v1-sites-maps-404-error-exception.md) |


# Update Site Map

Update Site Map

```python
def update_site_map(self,
                   site_id,
                   map_id,
                   body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `map_id` | `uuid\|string` | Template, Required | - |
| `body` | [`Map`](../../doc/models/map.md) | Body, Optional | Request Body |

## Response Type

[`Map`](../../doc/models/map.md)

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

map_id = '000000ab-00ab-00ab-00ab-0000000000ab'

body = Map(
    flags={},
    height=0,
    height_m=0,
    latlng_br=LatlngBr(
        lat='string',
        lng='string'
    ),
    latlng_tl=LatlngTl(
        lat='string',
        lng='string'
    ),
    locked=True,
    name='string',
    occupancy_limit=0,
    orientation=0,
    origin_x=0,
    origin_y=0,
    ppm=0,
    sitesurvey_path=[
        SitesurveyPath(
            coordinate='string',
            id='b069b358-4c97-5319-1f8c-7c5ca64d6ab1',
            name='string',
            nodes=[
                MapNode(
                    name='string',
                    edges={
                        "N2": 'string'
                    },
                    position=Position(
                        x=0,
                        y=0
                    )
                )
            ]
        )
    ],
    thumbnail_url='string',
    mtype=Type30Enum.IMAGE,
    url='string',
    view=ViewEnum.ROADMAP,
    wall_path=WallPath(
        coordinate='string',
        nodes=[
            MapNode(
                name='string',
                edges={
                    "N2": 'string'
                },
                position=Position(
                    x=0,
                    y=0
                )
            )
        ]
    ),
    wayfinding=Wayfinding(
        micello=Micello(
            account_key='string',
            default_level_id=0,
            map_id='b069b358-4c97-5319-1f8c-7c5ca64d6ab1'
        ),
        snap_to_path=True
    ),
    wayfinding_path=WayfindingPath(
        coordinate='string',
        nodes=[
            MapNode(
                name='string',
                edges={
                    "N2": 'string'
                },
                position=Position(
                    x=0,
                    y=0
                )
            )
        ]
    ),
    width=0,
    width_m=0
)

result = sites_maps_controller.update_site_map(
    site_id,
    map_id,
    body
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesMaps401ErrorException`](../../doc/models/api-v1-sites-maps-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesMaps403ErrorException`](../../doc/models/api-v1-sites-maps-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesMaps404ErrorException`](../../doc/models/api-v1-sites-maps-404-error-exception.md) |


# Delete Site Map Image

Delete Site Map Image

```python
def delete_site_map_image(self,
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

result = sites_maps_controller.delete_site_map_image(
    site_id,
    map_id
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesMapsImage401ErrorException`](../../doc/models/api-v1-sites-maps-image-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesMapsImage403ErrorException`](../../doc/models/api-v1-sites-maps-image-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesMapsImage404ErrorException`](../../doc/models/api-v1-sites-maps-image-404-error-exception.md) |


# Add Site Map Image

Add image map is a multipart POST which has an file (Image) and an optional json parameter

```python
def add_site_map_image(self,
                      site_id,
                      map_id,
                      file=None,
                      json=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `map_id` | `uuid\|string` | Template, Required | - |
| `file` | `string` | Form, Optional | binary file |
| `json` | `string` | Form, Optional | JSON string describing your upload |

## Response Type

`object`

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

map_id = '000000ab-00ab-00ab-00ab-0000000000ab'

result = sites_maps_controller.add_site_map_image(
    site_id,
    map_id
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesMapsImage401ErrorException`](../../doc/models/api-v1-sites-maps-image-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesMapsImage403ErrorException`](../../doc/models/api-v1-sites-maps-image-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesMapsImage404ErrorException`](../../doc/models/api-v1-sites-maps-image-404-error-exception.md) |


# Replace Site Map Image

Replace Map Image

This works like an PUT where the image will be replaced. If transform is provided, all the locations of the objects on the map (AP, Zone, Vbeacon, Beacon) will be transformed as well (relative to the new Map)

```python
def replace_site_map_image(self,
                          site_id,
                          map_id,
                          file,
                          json=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `map_id` | `uuid\|string` | Template, Required | - |
| `file` | `string` | Form, Required | **Constraints**: *Minimum Length*: `1` |
| `json` | [`Json2`](../../doc/models/json-2.md) | Form, Optional | - |

## Response Type

`object`

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

map_id = '000000ab-00ab-00ab-00ab-0000000000ab'

file = 'file0'

result = sites_maps_controller.replace_site_map_image(
    site_id,
    map_id,
    file
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesMapsReplace401ErrorException`](../../doc/models/api-v1-sites-maps-replace-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesMapsReplace403ErrorException`](../../doc/models/api-v1-sites-maps-replace-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesMapsReplace404ErrorException`](../../doc/models/api-v1-sites-maps-replace-404-error-exception.md) |


# Bulk Assign Site Aps to Map

This API can be used to assign a list of AP Macs associated with site_id to the specified map_id. Note that map_id must be associated with corresponding site_id. This API obeys the following rules

1. if AP is unassigned to any Map, it gets associated with map_id
2. Any moved APs are returned in the response
3. If the AP is considered a locked AP, no action will be taken

```python
def bulk_assign_site_aps_to_map(self,
                               site_id,
                               map_id,
                               body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `map_id` | `uuid\|string` | Template, Required | - |
| `body` | [`ApiV1SitesMapsSetMapRequest`](../../doc/models/api-v1-sites-maps-set-map-request.md) | Body, Optional | - |

## Response Type

[`ApiV1SitesMapsSetMapResponse`](../../doc/models/api-v1-sites-maps-set-map-response.md)

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

map_id = '000000ab-00ab-00ab-00ab-0000000000ab'

body = ApiV1SitesMapsSetMapRequest(
    device_ids=[
        '5c5b35000001',
        '5c5b35584a6f'
    ]
)

result = sites_maps_controller.bulk_assign_site_aps_to_map(
    site_id,
    map_id,
    body
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "locked": [
    "5c5b35584a6f"
  ],
  "moved": [
    "5c5b35000001"
  ]
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesMapsSetMap401ErrorException`](../../doc/models/api-v1-sites-maps-set-map-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesMapsSetMap403ErrorException`](../../doc/models/api-v1-sites-maps-set-map-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesMapsSetMap404ErrorException`](../../doc/models/api-v1-sites-maps-set-map-404-error-exception.md) |


# Import Site Wayfindings

This imports the vendor map meta data into the Map JSON. This is required by the SDK and App in order to access/render the vendor Map properly.

```python
def import_site_wayfindings(self,
                           site_id,
                           map_id,
                           body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `map_id` | `uuid\|string` | Template, Required | - |
| `body` | `object` | Body, Optional | Request Body |

## Response Type

`object`

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

map_id = '000000ab-00ab-00ab-00ab-0000000000ab'

body = {"client_id":"199d6770-0f6f-407a-9bd5-fc33c7840194","client_secret":"/9Nog3yDzcYj0bY91XJZQLCt+m9DXaIVhx+Ghk3ddd","customer_id":123,"endpoint_url":"https://api.jibestream.com","map_id":"b069b358-4c97-5319-1f8c-7c5ca64d6ab1","mmpp":223,"ppm":4,"vendor_name":"jibestream","venue_id":123}

result = sites_maps_controller.import_site_wayfindings(
    site_id,
    map_id,
    body
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesMapsWayfindingImport401ErrorException`](../../doc/models/api-v1-sites-maps-wayfinding-import-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesMapsWayfindingImport403ErrorException`](../../doc/models/api-v1-sites-maps-wayfinding-import-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesMapsWayfindingImport404ErrorException`](../../doc/models/api-v1-sites-maps-wayfinding-import-404-error-exception.md) |

