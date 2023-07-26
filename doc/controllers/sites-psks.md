# Sites Psks

```python
sites_psks_controller = client.sites_psks
```

## Class Name

`SitesPsksController`

## Methods

* [List Site Psks](../../doc/controllers/sites-psks.md#list-site-psks)
* [Create Site Psk](../../doc/controllers/sites-psks.md#create-site-psk)
* [Update Site Psks](../../doc/controllers/sites-psks.md#update-site-psks)
* [Import Site Psks](../../doc/controllers/sites-psks.md#import-site-psks)
* [Delete Site Psk](../../doc/controllers/sites-psks.md#delete-site-psk)
* [Get Site Psk](../../doc/controllers/sites-psks.md#get-site-psk)
* [Update Site Psk](../../doc/controllers/sites-psks.md#update-site-psk)


# List Site Psks

Get List of Site PSKs

```python
def list_site_psks(self,
                  site_id,
                  ssid=None,
                  role=None,
                  name=None,
                  page=1,
                  limit=100)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `ssid` | `string` | Query, Optional | - |
| `role` | `string` | Query, Optional | - |
| `name` | `string` | Query, Optional | - |
| `page` | `int` | Query, Optional | **Default**: `1`<br>**Constraints**: `>= 1` |
| `limit` | `int` | Query, Optional | **Default**: `100`<br>**Constraints**: `>= 0` |

## Response Type

[`List of Psk`](../../doc/models/psk.md)

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

page = 1

limit = 100

result = sites_psks_controller.list_site_psks(
    site_id,
    page,
    limit
)
print(result)
```

## Example Response *(as JSON)*

```json
[
  {
    "created_time": 0,
    "id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
    "mac": "string",
    "modified_time": 0,
    "name": "string",
    "org_id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
    "passphrase": "stringst",
    "site_id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
    "ssid": "string",
    "usage": "multi",
    "vlan_id": 1
  }
]
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesPsks401ErrorException`](../../doc/models/api-v1-sites-psks-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesPsks403ErrorException`](../../doc/models/api-v1-sites-psks-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesPsks404ErrorException`](../../doc/models/api-v1-sites-psks-404-error-exception.md) |


# Create Site Psk

Create Site PSK

```python
def create_site_psk(self,
                   site_id,
                   body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `body` | [`Psk`](../../doc/models/psk.md) | Body, Optional | Request Body |

## Response Type

[`Psk`](../../doc/models/psk.md)

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

body = Psk(
    name='string',
    passphrase='stringst',
    ssid='string',
    mac='string',
    usage=Usage2Enum.MULTI,
    vlan_id=1
)

result = sites_psks_controller.create_site_psk(
    site_id,
    body
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesPsks401ErrorException`](../../doc/models/api-v1-sites-psks-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesPsks403ErrorException`](../../doc/models/api-v1-sites-psks-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesPsks404ErrorException`](../../doc/models/api-v1-sites-psks-404-error-exception.md) |


# Update Site Psks

Update multi PSKs

```python
def update_site_psks(self,
                    site_id,
                    body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `body` | [`List of Psk`](../../doc/models/psk.md) | Body, Optional | - |

## Response Type

[`List of Psk`](../../doc/models/psk.md)

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

body = [
    Psk(
        name='common123',
        passphrase='foryoureyesonly2',
        ssid='warehouse',
        id='2f64a022-9422-4fa3-92aa-ff6559a9f7f9'
    ),
    Psk(
        name='common12',
        passphrase='foryoureyesonly1',
        ssid='warehouse',
        id='110c59ae-d7b2-40f9-9bf2-82367370e55a',
        role='teacher',
        usage=Usage2Enum.SINGLE
    )
]

result = sites_psks_controller.update_site_psks(
    site_id,
    body
)
print(result)
```

## Example Response *(as JSON)*

```json
[
  {
    "created_time": 0,
    "id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
    "mac": "string",
    "modified_time": 0,
    "name": "string",
    "org_id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
    "passphrase": "stringst",
    "site_id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
    "ssid": "string",
    "usage": "multi",
    "vlan_id": 1
  }
]
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesPsks401ErrorException`](../../doc/models/api-v1-sites-psks-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesPsks403ErrorException`](../../doc/models/api-v1-sites-psks-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesPsks404ErrorException`](../../doc/models/api-v1-sites-psks-404-error-exception.md) |


# Import Site Psks

Import PSK from CSV file or JSON

## CSV File Format

```csv
PSK Import CSV File Format:
name,ssid,passphrase,usage,vlan_id,mac
Common,warehouse,foryoureyesonly,single,35,a31425f31278
Justin,reception,visible,multi,1002
```

```python
def import_site_psks(self,
                    site_id,
                    file=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `file` | `string` | Form, Optional | - |

## Response Type

[`List of Psk`](../../doc/models/psk.md)

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

result = sites_psks_controller.import_site_psks(site_id)
print(result)
```

## Example Response *(as JSON)*

```json
[
  {
    "created_time": 0,
    "id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
    "mac": "string",
    "modified_time": 0,
    "name": "string",
    "org_id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
    "passphrase": "stringst",
    "site_id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
    "ssid": "string",
    "usage": "multi",
    "vlan_id": 1
  }
]
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesPsksImport401ErrorException`](../../doc/models/api-v1-sites-psks-import-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesPsksImport403ErrorException`](../../doc/models/api-v1-sites-psks-import-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesPsksImport404ErrorException`](../../doc/models/api-v1-sites-psks-import-404-error-exception.md) |


# Delete Site Psk

Delete Site PSK

```python
def delete_site_psk(self,
                   site_id,
                   psk_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `psk_id` | `uuid\|string` | Template, Required | PSK ID |

## Response Type

`object`

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

psk_id = '000000ab-00ab-00ab-00ab-0000000000ab'

result = sites_psks_controller.delete_site_psk(
    site_id,
    psk_id
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesPsks401ErrorException`](../../doc/models/api-v1-sites-psks-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesPsks403ErrorException`](../../doc/models/api-v1-sites-psks-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesPsks404ErrorException`](../../doc/models/api-v1-sites-psks-404-error-exception.md) |


# Get Site Psk

Get Site PSK Details

```python
def get_site_psk(self,
                site_id,
                psk_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `psk_id` | `uuid\|string` | Template, Required | PSK ID |

## Response Type

[`Psk`](../../doc/models/psk.md)

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

psk_id = '000000ab-00ab-00ab-00ab-0000000000ab'

result = sites_psks_controller.get_site_psk(
    site_id,
    psk_id
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesPsks401ErrorException`](../../doc/models/api-v1-sites-psks-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesPsks403ErrorException`](../../doc/models/api-v1-sites-psks-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesPsks404ErrorException`](../../doc/models/api-v1-sites-psks-404-error-exception.md) |


# Update Site Psk

Update Site PSK

```python
def update_site_psk(self,
                   site_id,
                   psk_id,
                   body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `psk_id` | `uuid\|string` | Template, Required | PSK ID |
| `body` | [`Psk`](../../doc/models/psk.md) | Body, Optional | Request Body |

## Response Type

[`Psk`](../../doc/models/psk.md)

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

psk_id = '000000ab-00ab-00ab-00ab-0000000000ab'

body = Psk(
    name='string',
    passphrase='stringst',
    ssid='string',
    mac='string',
    usage=Usage2Enum.MULTI,
    vlan_id=1
)

result = sites_psks_controller.update_site_psk(
    site_id,
    psk_id,
    body
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesPsks401ErrorException`](../../doc/models/api-v1-sites-psks-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesPsks403ErrorException`](../../doc/models/api-v1-sites-psks-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesPsks404ErrorException`](../../doc/models/api-v1-sites-psks-404-error-exception.md) |

