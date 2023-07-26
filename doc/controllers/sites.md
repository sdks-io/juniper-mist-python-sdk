# Sites

A site represents a project, a deployment. For MSP, it can be as small as a coffee shop or a five-star 600-room hotel. A site contains a set of Maps, Wlans, Policies, Zones.

```python
sites_controller = client.sites
```

## Class Name

`SitesController`

## Methods

* [Delete Site](../../doc/controllers/sites.md#delete-site)
* [Get Site Info](../../doc/controllers/sites.md#get-site-info)
* [Update Site Info](../../doc/controllers/sites.md#update-site-info)


# Delete Site

Delete Site

```python
def delete_site(self,
               site_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |

## Response Type

`object`

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

result = sites_controller.delete_site(site_id)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1Sites401ErrorException`](../../doc/models/api-v1-sites-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1Sites403ErrorException`](../../doc/models/api-v1-sites-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1Sites404ErrorException`](../../doc/models/api-v1-sites-404-error-exception.md) |


# Get Site Info

Get Site Info

```python
def get_site_info(self,
                 site_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |

## Response Type

[`Site`](../../doc/models/site.md)

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

result = sites_controller.get_site_info(site_id)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "address": "1601 S. Deanza Blvd., Cupertino, CA, 95014",
  "alarmtemplate_id": "684dfc5c-fe77-2290-eb1d-ef3d677fe168",
  "apporttemplate_id": "string",
  "aptemplate_id": "16bdf952-ade2-4491-80b0-85ce506c760b",
  "country_code": "US",
  "created_time": 0,
  "gatewaytemplate_id": "6f9b2e75-9b2f-b5ae-81e3-e14c76f1a90f",
  "id": "497f6eca-6276-5005-bfeb-53cbbbba6f17",
  "latlng": {
    "lat": 37.295833,
    "lng": -122.032946
  },
  "modified_time": 0,
  "name": "Mist Office",
  "networktemplate_id": "12ae9bd2-e0ab-107b-72e8-a7a005565ec2",
  "notes": "string",
  "org_id": "a40f5d1f-d889-42e9-94ea-b9b33585fc6b",
  "rftemplate_id": "bb8a9017-1e36-5d6c-6f2b-551abe8a76a2",
  "secpolicy_id": "3bcd0beb-5d0a-4cbd-92c1-14aea91e98ef",
  "sitegroup_ids": [
    "497f6eca-6276-5006-bfeb-53cbbbba6f18"
  ],
  "timezone": "America/Los_Angeles"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1Sites401ErrorException`](../../doc/models/api-v1-sites-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1Sites403ErrorException`](../../doc/models/api-v1-sites-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1Sites404ErrorException`](../../doc/models/api-v1-sites-404-error-exception.md) |


# Update Site Info

Update Site Info

```python
def update_site_info(self,
                    site_id,
                    body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `body` | [`Site`](../../doc/models/site.md) | Body, Optional | Request Body |

## Response Type

[`Site`](../../doc/models/site.md)

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

body = Site(
    name='string',
    address='string',
    alarmtemplate_id='b069b358-4c97-5319-1f8c-7c5ca64d6ab1',
    country_code='string',
    latlng=Latlng1(
        lat=0,
        lng=0
    ),
    networktemplate_id='b069b358-4c97-5319-1f8c-7c5ca64d6ab1',
    notes='string',
    rftemplate_id='b069b358-4c97-5319-1f8c-7c5ca64d6ab1',
    secpolicy_id='b069b358-4c97-5319-1f8c-7c5ca64d6ab1',
    sitegroup_ids=[
        'b069b358-4c97-5319-1f8c-7c5ca64d6ab1'
    ],
    timezone='string'
)

result = sites_controller.update_site_info(
    site_id,
    body
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "address": "1601 S. Deanza Blvd., Cupertino, CA, 95014",
  "alarmtemplate_id": "684dfc5c-fe77-2290-eb1d-ef3d677fe168",
  "apporttemplate_id": "string",
  "aptemplate_id": "16bdf952-ade2-4491-80b0-85ce506c760b",
  "country_code": "US",
  "created_time": 0,
  "gatewaytemplate_id": "6f9b2e75-9b2f-b5ae-81e3-e14c76f1a90f",
  "id": "497f6eca-6276-5005-bfeb-53cbbbba6f17",
  "latlng": {
    "lat": 37.295833,
    "lng": -122.032946
  },
  "modified_time": 0,
  "name": "Mist Office",
  "networktemplate_id": "12ae9bd2-e0ab-107b-72e8-a7a005565ec2",
  "notes": "string",
  "org_id": "a40f5d1f-d889-42e9-94ea-b9b33585fc6b",
  "rftemplate_id": "bb8a9017-1e36-5d6c-6f2b-551abe8a76a2",
  "secpolicy_id": "3bcd0beb-5d0a-4cbd-92c1-14aea91e98ef",
  "sitegroup_ids": [
    "497f6eca-6276-5006-bfeb-53cbbbba6f18"
  ],
  "timezone": "America/Los_Angeles"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1Sites401ErrorException`](../../doc/models/api-v1-sites-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1Sites403ErrorException`](../../doc/models/api-v1-sites-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1Sites404ErrorException`](../../doc/models/api-v1-sites-404-error-exception.md) |

