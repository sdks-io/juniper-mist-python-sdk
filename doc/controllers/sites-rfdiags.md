# Sites Rfdiags

```python
sites_rfdiags_controller = client.sites_rfdiags
```

## Class Name

`SitesRfdiagsController`

## Methods

* [Get Site Site Rfdiag Recording](../../doc/controllers/sites-rfdiags.md#get-site-site-rfdiag-recording)
* [Start Site Recording](../../doc/controllers/sites-rfdiags.md#start-site-recording)
* [Delete Site Rfdiag Recording](../../doc/controllers/sites-rfdiags.md#delete-site-rfdiag-recording)
* [Get Site Rfdiag Recording](../../doc/controllers/sites-rfdiags.md#get-site-rfdiag-recording)
* [Update Site Rfdiag Recording](../../doc/controllers/sites-rfdiags.md#update-site-rfdiag-recording)
* [Download Site Rfdiag Recording](../../doc/controllers/sites-rfdiags.md#download-site-rfdiag-recording)
* [Stop Site Rfdiag Recording](../../doc/controllers/sites-rfdiags.md#stop-site-rfdiag-recording)


# Get Site Site Rfdiag Recording

List RF Glass Recording

```python
def get_site_site_rfdiag_recording(self,
                                  site_id,
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
| `page` | `int` | Query, Optional | **Default**: `1`<br>**Constraints**: `>= 1` |
| `limit` | `int` | Query, Optional | **Default**: `100`<br>**Constraints**: `>= 0` |
| `start` | `int` | Query, Optional | **Default**: `0`<br>**Constraints**: `>= 0` |
| `end` | `int` | Query, Optional | **Default**: `0`<br>**Constraints**: `>= 0` |
| `duration` | `string` | Query, Optional | For historical stats and/or logs where time range is needed, you can specify the time range in a few different ways:<br><br>* ?start=1430000000&end=1430864000	specify the start / end<br>* ?end=1430864000&duration=1d	specify end time and duration<br>* ?duration=1d	specify duration, end will be now() in seconds<br>**Default**: `'1d'` |

## Response Type

[`List of RfdiagResponse`](../../doc/models/rfdiag-response.md)

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

page = 1

limit = 100

start = 0

end = 0

duration = '10m'

result = sites_rfdiags_controller.get_site_site_rfdiag_recording(
    site_id,
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
[
  [
    {
      "asset_id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
      "asset_name": "string",
      "client_name": "string",
      "duration": 0,
      "end_time": 0,
      "frame_count": 0,
      "id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
      "mac": "string",
      "map_id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
      "name": "string",
      "next": "string",
      "raw_events": "string",
      "ready": true,
      "sdkclient_id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
      "sdkclient_name": "string",
      "sdkclient_uuid": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
      "start_time": 0,
      "type": "sdkclient",
      "url": "string"
    }
  ]
]
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesRfdiags401ErrorException`](../../doc/models/api-v1-sites-rfdiags-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesRfdiags403ErrorException`](../../doc/models/api-v1-sites-rfdiags-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesRfdiags404ErrorException`](../../doc/models/api-v1-sites-rfdiags-404-error-exception.md) |


# Start Site Recording

Start RF Glass Recording

```python
def start_site_recording(self,
                        site_id,
                        body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `body` | [`Rfdiag`](../../doc/models/rfdiag.md) | Body, Optional | Request Body |

## Response Type

[`List of RfdiagResponse`](../../doc/models/rfdiag-response.md)

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

body = Rfdiag(
    name='name6',
    mtype=Type36Enum.CLIENT,
    duration=180
)

result = sites_rfdiags_controller.start_site_recording(
    site_id,
    body
)
print(result)
```

## Example Response *(as JSON)*

```json
[
  {
    "asset_id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
    "asset_name": "string",
    "client_name": "string",
    "duration": 0,
    "end_time": 0,
    "frame_count": 0,
    "id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
    "mac": "string",
    "map_id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
    "name": "string",
    "next": "string",
    "raw_events": "string",
    "ready": true,
    "sdkclient_id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
    "sdkclient_name": "string",
    "sdkclient_uuid": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
    "start_time": 0,
    "type": "sdkclient",
    "url": "string"
  }
]
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesRfdiags401ErrorException`](../../doc/models/api-v1-sites-rfdiags-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesRfdiags403ErrorException`](../../doc/models/api-v1-sites-rfdiags-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesRfdiags404ErrorException`](../../doc/models/api-v1-sites-rfdiags-404-error-exception.md) |


# Delete Site Rfdiag Recording

Delete Recording

```python
def delete_site_rfdiag_recording(self,
                                site_id,
                                rfdiag_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `rfdiag_id` | `uuid\|string` | Template, Required | - |

## Response Type

`object`

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

rfdiag_id = '000000ab-00ab-00ab-00ab-0000000000ab'

result = sites_rfdiags_controller.delete_site_rfdiag_recording(
    site_id,
    rfdiag_id
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesRfdiags401ErrorException`](../../doc/models/api-v1-sites-rfdiags-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesRfdiags403ErrorException`](../../doc/models/api-v1-sites-rfdiags-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesRfdiags404ErrorException`](../../doc/models/api-v1-sites-rfdiags-404-error-exception.md) |


# Get Site Rfdiag Recording

Get RF Diage Recording Details

```python
def get_site_rfdiag_recording(self,
                             site_id,
                             rfdiag_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `rfdiag_id` | `uuid\|string` | Template, Required | - |

## Response Type

[`List of RfdiagResponse`](../../doc/models/rfdiag-response.md)

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

rfdiag_id = '000000ab-00ab-00ab-00ab-0000000000ab'

result = sites_rfdiags_controller.get_site_rfdiag_recording(
    site_id,
    rfdiag_id
)
print(result)
```

## Example Response *(as JSON)*

```json
[
  {
    "asset_id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
    "asset_name": "string",
    "client_name": "string",
    "duration": 0,
    "end_time": 0,
    "frame_count": 0,
    "id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
    "mac": "string",
    "map_id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
    "name": "string",
    "next": "string",
    "raw_events": "string",
    "ready": true,
    "sdkclient_id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
    "sdkclient_name": "string",
    "sdkclient_uuid": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
    "start_time": 0,
    "type": "sdkclient",
    "url": "string"
  }
]
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesRfdiags401ErrorException`](../../doc/models/api-v1-sites-rfdiags-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesRfdiags403ErrorException`](../../doc/models/api-v1-sites-rfdiags-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesRfdiags404ErrorException`](../../doc/models/api-v1-sites-rfdiags-404-error-exception.md) |


# Update Site Rfdiag Recording

Update Recording

```python
def update_site_rfdiag_recording(self,
                                site_id,
                                rfdiag_id,
                                body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `rfdiag_id` | `uuid\|string` | Template, Required | - |
| `body` | [`Rfdiag`](../../doc/models/rfdiag.md) | Body, Optional | Request Body |

## Response Type

[`List of RfdiagResponse`](../../doc/models/rfdiag-response.md)

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

rfdiag_id = '000000ab-00ab-00ab-00ab-0000000000ab'

body = Rfdiag(
    name='name6',
    mtype=Type36Enum.CLIENT,
    duration=180
)

result = sites_rfdiags_controller.update_site_rfdiag_recording(
    site_id,
    rfdiag_id,
    body
)
print(result)
```

## Example Response *(as JSON)*

```json
[
  {
    "asset_id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
    "asset_name": "string",
    "client_name": "string",
    "duration": 0,
    "end_time": 0,
    "frame_count": 0,
    "id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
    "mac": "string",
    "map_id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
    "name": "string",
    "next": "string",
    "raw_events": "string",
    "ready": true,
    "sdkclient_id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
    "sdkclient_name": "string",
    "sdkclient_uuid": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
    "start_time": 0,
    "type": "sdkclient",
    "url": "string"
  }
]
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesRfdiags401ErrorException`](../../doc/models/api-v1-sites-rfdiags-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesRfdiags403ErrorException`](../../doc/models/api-v1-sites-rfdiags-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesRfdiags404ErrorException`](../../doc/models/api-v1-sites-rfdiags-404-error-exception.md) |


# Download Site Rfdiag Recording

Download Recording
Download raw_events blob

```python
def download_site_rfdiag_recording(self,
                                  site_id,
                                  rfdiag_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `rfdiag_id` | `uuid\|string` | Template, Required | - |

## Response Type

`string`

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

rfdiag_id = '000000ab-00ab-00ab-00ab-0000000000ab'

result = sites_rfdiags_controller.download_site_rfdiag_recording(
    site_id,
    rfdiag_id
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesRfdiagsDownload401ErrorException`](../../doc/models/api-v1-sites-rfdiags-download-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesRfdiagsDownload403ErrorException`](../../doc/models/api-v1-sites-rfdiags-download-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesRfdiagsDownload404ErrorException`](../../doc/models/api-v1-sites-rfdiags-download-404-error-exception.md) |


# Stop Site Rfdiag Recording

If the recording session is active for the given rfdiag_id, it will finish the recording. duration and end_time will be updated to reflect the correct values.

```python
def stop_site_rfdiag_recording(self,
                              site_id,
                              rfdiag_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `rfdiag_id` | `uuid\|string` | Template, Required | - |

## Response Type

`object`

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

rfdiag_id = '000000ab-00ab-00ab-00ab-0000000000ab'

result = sites_rfdiags_controller.stop_site_rfdiag_recording(
    site_id,
    rfdiag_id
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesRfdiagsStop401ErrorException`](../../doc/models/api-v1-sites-rfdiags-stop-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesRfdiagsStop403ErrorException`](../../doc/models/api-v1-sites-rfdiags-stop-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesRfdiagsStop404ErrorException`](../../doc/models/api-v1-sites-rfdiags-stop-404-error-exception.md) |

