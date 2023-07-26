# Sites Wx Tags

```python
sites_wx_tags_controller = client.sites_wx_tags
```

## Class Name

`SitesWxTagsController`

## Methods

* [List Site Wx Tags](../../doc/controllers/sites-wx-tags.md#list-site-wx-tags)
* [Create Site Wx Tag](../../doc/controllers/sites-wx-tags.md#create-site-wx-tag)
* [Get Site Application List](../../doc/controllers/sites-wx-tags.md#get-site-application-list)
* [Delete Site Wx Tag](../../doc/controllers/sites-wx-tags.md#delete-site-wx-tag)
* [Get Site Wx Tag](../../doc/controllers/sites-wx-tags.md#get-site-wx-tag)
* [Update Site Wx Tag](../../doc/controllers/sites-wx-tags.md#update-site-wx-tag)
* [Get Site Current Matching Clients of a Wx Tag](../../doc/controllers/sites-wx-tags.md#get-site-current-matching-clients-of-a-wx-tag)


# List Site Wx Tags

Get List of Site WxTags

```python
def list_site_wx_tags(self,
                     site_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |

## Response Type

[`List of WxlanTag`](../../doc/models/wxlan-tag.md)

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

result = sites_wx_tags_controller.list_site_wx_tags(site_id)
print(result)
```

## Example Response *(as JSON)*

```json
[
  {
    "created_time": 0,
    "id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
    "last_ips": [
      "string"
    ],
    "mac": "string",
    "match": "wlan_id",
    "modified_time": 0,
    "name": "string",
    "op": "in",
    "org_id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
    "resource_mac": "string",
    "services": [
      "string"
    ],
    "site_id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
    "specs": [
      {
        "port_range": "string",
        "protocol": "tcp",
        "subnet": [
          "string"
        ]
      }
    ],
    "subnet": "string",
    "type": "match",
    "values": [
      "string"
    ]
  }
]
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesWxtags401ErrorException`](../../doc/models/api-v1-sites-wxtags-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesWxtags403ErrorException`](../../doc/models/api-v1-sites-wxtags-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesWxtags404ErrorException`](../../doc/models/api-v1-sites-wxtags-404-error-exception.md) |


# Create Site Wx Tag

Create Site WxTag

```python
def create_site_wx_tag(self,
                      site_id,
                      body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `body` | [`WxlanTag`](../../doc/models/wxlan-tag.md) | Body, Optional | Request Body |

## Response Type

[`WxlanTag`](../../doc/models/wxlan-tag.md)

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

body = WxlanTag(
    name='string',
    mtype=Type43Enum.MATCH,
    last_ips=[
        'string'
    ],
    mac='string',
    match=Match1Enum.WLAN_ID,
    op=Op1Enum.ENUM_IN,
    resource_mac='string',
    services=[
        'string'
    ],
    specs=[
        Spec2(
            port_range='string',
            protocol='tcp'
        )
    ],
    subnet='string',
    values=[
        'string'
    ]
)

result = sites_wx_tags_controller.create_site_wx_tag(
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
  "last_ips": [
    "string"
  ],
  "mac": "string",
  "match": "wlan_id",
  "modified_time": 0,
  "name": "string",
  "op": "in",
  "org_id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
  "resource_mac": "string",
  "services": [
    "string"
  ],
  "site_id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
  "specs": [
    {
      "port_range": "string",
      "protocol": "tcp",
      "subnet": [
        "string"
      ]
    }
  ],
  "subnet": "string",
  "type": "match",
  "values": [
    "string"
  ]
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesWxtags401ErrorException`](../../doc/models/api-v1-sites-wxtags-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesWxtags403ErrorException`](../../doc/models/api-v1-sites-wxtags-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesWxtags404ErrorException`](../../doc/models/api-v1-sites-wxtags-404-error-exception.md) |


# Get Site Application List

Get Application List

```python
def get_site_application_list(self,
                             site_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |

## Response Type

[`List of ApiV1SitesWxtagsAppsResponse`](../../doc/models/api-v1-sites-wxtags-apps-response.md)

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

result = sites_wx_tags_controller.get_site_application_list(site_id)
print(result)
```

## Example Response *(as JSON)*

```json
[
  {
    "group": "Emails",
    "key": "gmail",
    "name": "Gmail - web/app"
  }
]
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesWxtagsApps401ErrorException`](../../doc/models/api-v1-sites-wxtags-apps-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesWxtagsApps403ErrorException`](../../doc/models/api-v1-sites-wxtags-apps-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesWxtagsApps404ErrorException`](../../doc/models/api-v1-sites-wxtags-apps-404-error-exception.md) |


# Delete Site Wx Tag

Delete Site WxTag

```python
def delete_site_wx_tag(self,
                      site_id,
                      wxtag_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `wxtag_id` | `uuid\|string` | Template, Required | - |

## Response Type

`object`

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

wxtag_id = '000000ab-00ab-00ab-00ab-0000000000ab'

result = sites_wx_tags_controller.delete_site_wx_tag(
    site_id,
    wxtag_id
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesWxtags401ErrorException`](../../doc/models/api-v1-sites-wxtags-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesWxtags403ErrorException`](../../doc/models/api-v1-sites-wxtags-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesWxtags404ErrorException`](../../doc/models/api-v1-sites-wxtags-404-error-exception.md) |


# Get Site Wx Tag

Get Site WxTag Details

```python
def get_site_wx_tag(self,
                   site_id,
                   wxtag_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `wxtag_id` | `uuid\|string` | Template, Required | - |

## Response Type

[`WxlanTag`](../../doc/models/wxlan-tag.md)

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

wxtag_id = '000000ab-00ab-00ab-00ab-0000000000ab'

result = sites_wx_tags_controller.get_site_wx_tag(
    site_id,
    wxtag_id
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "created_time": 0,
  "id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
  "last_ips": [
    "string"
  ],
  "mac": "string",
  "match": "wlan_id",
  "modified_time": 0,
  "name": "string",
  "op": "in",
  "org_id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
  "resource_mac": "string",
  "services": [
    "string"
  ],
  "site_id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
  "specs": [
    {
      "port_range": "string",
      "protocol": "tcp",
      "subnet": [
        "string"
      ]
    }
  ],
  "subnet": "string",
  "type": "match",
  "values": [
    "string"
  ]
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesWxtags401ErrorException`](../../doc/models/api-v1-sites-wxtags-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesWxtags403ErrorException`](../../doc/models/api-v1-sites-wxtags-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesWxtags404ErrorException`](../../doc/models/api-v1-sites-wxtags-404-error-exception.md) |


# Update Site Wx Tag

Update Site WxTag

```python
def update_site_wx_tag(self,
                      site_id,
                      wxtag_id,
                      body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `wxtag_id` | `uuid\|string` | Template, Required | - |
| `body` | [`WxlanTag`](../../doc/models/wxlan-tag.md) | Body, Optional | Request Body |

## Response Type

[`WxlanTag`](../../doc/models/wxlan-tag.md)

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

wxtag_id = '000000ab-00ab-00ab-00ab-0000000000ab'

body = WxlanTag(
    name='string',
    mtype=Type43Enum.MATCH,
    last_ips=[
        'string'
    ],
    mac='string',
    match=Match1Enum.WLAN_ID,
    op=Op1Enum.ENUM_IN,
    resource_mac='string',
    services=[
        'string'
    ],
    specs=[
        Spec2(
            port_range='string',
            protocol='tcp'
        )
    ],
    subnet='string',
    values=[
        'string'
    ]
)

result = sites_wx_tags_controller.update_site_wx_tag(
    site_id,
    wxtag_id,
    body
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "created_time": 0,
  "id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
  "last_ips": [
    "string"
  ],
  "mac": "string",
  "match": "wlan_id",
  "modified_time": 0,
  "name": "string",
  "op": "in",
  "org_id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
  "resource_mac": "string",
  "services": [
    "string"
  ],
  "site_id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
  "specs": [
    {
      "port_range": "string",
      "protocol": "tcp",
      "subnet": [
        "string"
      ]
    }
  ],
  "subnet": "string",
  "type": "match",
  "values": [
    "string"
  ]
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesWxtags401ErrorException`](../../doc/models/api-v1-sites-wxtags-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesWxtags403ErrorException`](../../doc/models/api-v1-sites-wxtags-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesWxtags404ErrorException`](../../doc/models/api-v1-sites-wxtags-404-error-exception.md) |


# Get Site Current Matching Clients of a Wx Tag

Get Current Matching Clients of a WXLAN Tag

```python
def get_site_current_matching_clients_of_a_wx_tag(self,
                                                 site_id,
                                                 wxtag_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `wxtag_id` | `uuid\|string` | Template, Required | - |

## Response Type

[`List of ApiV1SitesWxtagsClientsResponse`](../../doc/models/api-v1-sites-wxtags-clients-response.md)

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

wxtag_id = '000000ab-00ab-00ab-00ab-0000000000ab'

result = sites_wx_tags_controller.get_site_current_matching_clients_of_a_wx_tag(
    site_id,
    wxtag_id
)
print(result)
```

## Example Response *(as JSON)*

```json
[
  {
    "mac": "5684dae9ac8b",
    "since": 1428939600
  }
]
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesWxtagsClients401ErrorException`](../../doc/models/api-v1-sites-wxtags-clients-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesWxtagsClients403ErrorException`](../../doc/models/api-v1-sites-wxtags-clients-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesWxtagsClients404ErrorException`](../../doc/models/api-v1-sites-wxtags-clients-404-error-exception.md) |

