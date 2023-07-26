# Sites Webhooks

```python
sites_webhooks_controller = client.sites_webhooks
```

## Class Name

`SitesWebhooksController`

## Methods

* [List Site Webhooks](../../doc/controllers/sites-webhooks.md#list-site-webhooks)
* [Create Site Webhook](../../doc/controllers/sites-webhooks.md#create-site-webhook)
* [Delete Site Webhook](../../doc/controllers/sites-webhooks.md#delete-site-webhook)
* [Get Site Webhook](../../doc/controllers/sites-webhooks.md#get-site-webhook)
* [Update Site Webhook](../../doc/controllers/sites-webhooks.md#update-site-webhook)
* [Search Site Webhooks Deliveries](../../doc/controllers/sites-webhooks.md#search-site-webhooks-deliveries)
* [Ping Site Webhook](../../doc/controllers/sites-webhooks.md#ping-site-webhook)


# List Site Webhooks

Get List of Site Webhooks

```python
def list_site_webhooks(self,
                      site_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |

## Response Type

[`List of Webhook`](../../doc/models/webhook.md)

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

result = sites_webhooks_controller.list_site_webhooks(site_id)
print(result)
```

## Example Response *(as JSON)*

```json
[
  {
    "created_time": 0,
    "enabled": true,
    "headers": {},
    "id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
    "modified_time": 0,
    "name": "string",
    "org_id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
    "secret": "string",
    "site_id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
    "splunk_token": "string",
    "topics": [
      "location"
    ],
    "type": "http-post",
    "url": "string",
    "verify_cert": true
  }
]
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesWebhooks401ErrorException`](../../doc/models/api-v1-sites-webhooks-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesWebhooks403ErrorException`](../../doc/models/api-v1-sites-webhooks-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesWebhooks404ErrorException`](../../doc/models/api-v1-sites-webhooks-404-error-exception.md) |


# Create Site Webhook

Webhook defines a webhook, modeled after [github’s model](https://developer.github.com/webhooks/).

There is two types of webhooks:

* webhooks ([examples](https://www.postman.com/juniper-mist/workspace/mist-systems-s-public-workspace/folder/224925-be01e694-7253-4195-8563-78e2a745e114))
* raw data webhooks ([examples](https://www.postman.com/juniper-mist/workspace/mist-systems-s-public-workspace/folder/224925-e2d5d5f8-4bdb-4efc-93e4-90f4b33d0b2b))

##### Webhooks

Webhooks can be configured at the org level (subset of topics only) and at the site level. It is possible to have multiple topics in the same webhook configuration and/or to have multiple webhooks configured at the same time.

##### Client Raw Data Webhooks

Raw data webhooks are a special subset of webhooks that provide insight into raw data packets emitted by a client, identified by their advertising MAC address (assets, discovered ble, connected wifi, unconnected wifi). The data that client raw data webhooks encompasses are reporting AP information, RSSI Data, and any special packets/telemetry packets that the client may emit. Note that client raw webhooks are the raw data coming from the client and do not contain the X,Y location data of the client. In order to get the location data for a client please see our location webhooks. Clients can be identified uniquely across these client raw data topics and location webhook topic using MAC address as the Unique identifier (client identifier).

###### Client Raw Data Webhooks Topics

Topics that correspond to client raw data for different client types.

* `asset-raw-rssi` - Raw data from packets emitted by named and filtered assets
* `discovered-raw-rssi` - Raw data from packets emitted by passive BLE devices
* `wifi-conn-raw` - Raw data from packets emitted by connected devices
* `wifi-unconn-raw` - Raw data from packets emitted by unconnected devices (passive)

###### Rules for configuring client raw data webhooks

1. Only one instance of a webhook object containing a client raw data webhook topic is allowed. (a site level entry will override an org level entry for the client raw data webhook topic in question)
2. Only one client raw data webhook topic is allowed per `http-post` message to webhooks api

```python
def create_site_webhook(self,
                       site_id,
                       body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `body` | [`Webhook`](../../doc/models/webhook.md) | Body, Optional | Request Body |

## Response Type

[`Webhook`](../../doc/models/webhook.md)

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

body = Webhook(
    enabled=True,
    headers={},
    name='string',
    secret='string',
    splunk_token='string',
    topics=[
        TopicEnum.LOCATION
    ],
    mtype=Type41Enum.HTTPPOST,
    url='string',
    verify_cert=True
)

result = sites_webhooks_controller.create_site_webhook(
    site_id,
    body
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "created_time": 0,
  "enabled": true,
  "headers": {},
  "id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
  "modified_time": 0,
  "name": "string",
  "org_id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
  "secret": "string",
  "site_id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
  "splunk_token": "string",
  "topics": [
    "location"
  ],
  "type": "http-post",
  "url": "string",
  "verify_cert": true
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad request | [`ApiV1SitesWebhooks400ErrorException`](../../doc/models/api-v1-sites-webhooks-400-error-exception.md) |
| 401 | Unauthorized | [`ApiV1SitesWebhooks401ErrorException`](../../doc/models/api-v1-sites-webhooks-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesWebhooks403ErrorException`](../../doc/models/api-v1-sites-webhooks-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesWebhooks404ErrorException`](../../doc/models/api-v1-sites-webhooks-404-error-exception.md) |


# Delete Site Webhook

Delete Site Webhook

```python
def delete_site_webhook(self,
                       site_id,
                       webhook_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `webhook_id` | `uuid\|string` | Template, Required | - |

## Response Type

`object`

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

webhook_id = '000000ab-00ab-00ab-00ab-0000000000ab'

result = sites_webhooks_controller.delete_site_webhook(
    site_id,
    webhook_id
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesWebhooks401ErrorException`](../../doc/models/api-v1-sites-webhooks-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesWebhooks403ErrorException`](../../doc/models/api-v1-sites-webhooks-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesWebhooks404ErrorException`](../../doc/models/api-v1-sites-webhooks-404-error-exception.md) |


# Get Site Webhook

Get Site Webhook Details

```python
def get_site_webhook(self,
                    site_id,
                    webhook_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `webhook_id` | `uuid\|string` | Template, Required | - |

## Response Type

[`Webhook`](../../doc/models/webhook.md)

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

webhook_id = '000000ab-00ab-00ab-00ab-0000000000ab'

result = sites_webhooks_controller.get_site_webhook(
    site_id,
    webhook_id
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "created_time": 0,
  "enabled": true,
  "headers": {},
  "id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
  "modified_time": 0,
  "name": "string",
  "org_id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
  "secret": "string",
  "site_id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
  "splunk_token": "string",
  "topics": [
    "location"
  ],
  "type": "http-post",
  "url": "string",
  "verify_cert": true
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesWebhooks401ErrorException`](../../doc/models/api-v1-sites-webhooks-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesWebhooks403ErrorException`](../../doc/models/api-v1-sites-webhooks-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesWebhooks404ErrorException`](../../doc/models/api-v1-sites-webhooks-404-error-exception.md) |


# Update Site Webhook

Update Site Webhook

```python
def update_site_webhook(self,
                       site_id,
                       webhook_id,
                       body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `webhook_id` | `uuid\|string` | Template, Required | - |
| `body` | [`Webhook`](../../doc/models/webhook.md) | Body, Optional | Request Body |

## Response Type

[`Webhook`](../../doc/models/webhook.md)

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

webhook_id = '000000ab-00ab-00ab-00ab-0000000000ab'

body = Webhook(
    enabled=True,
    headers={},
    name='string',
    secret='string',
    splunk_token='string',
    topics=[
        TopicEnum.LOCATION
    ],
    mtype=Type41Enum.HTTPPOST,
    url='string',
    verify_cert=True
)

result = sites_webhooks_controller.update_site_webhook(
    site_id,
    webhook_id,
    body
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "created_time": 0,
  "enabled": true,
  "headers": {},
  "id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
  "modified_time": 0,
  "name": "string",
  "org_id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
  "secret": "string",
  "site_id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
  "splunk_token": "string",
  "topics": [
    "location"
  ],
  "type": "http-post",
  "url": "string",
  "verify_cert": true
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesWebhooks401ErrorException`](../../doc/models/api-v1-sites-webhooks-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesWebhooks403ErrorException`](../../doc/models/api-v1-sites-webhooks-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesWebhooks404ErrorException`](../../doc/models/api-v1-sites-webhooks-404-error-exception.md) |


# Search Site Webhooks Deliveries

Search webhooks deliveries

To get a list of webhook deliveries in error, use the query parameter `?error=*`

```python
def search_site_webhooks_deliveries(self,
                                   site_id,
                                   webhook_id,
                                   status_code=None,
                                   error=None,
                                   topic=None,
                                   start=0,
                                   end=0,
                                   duration='1d',
                                   limit=100)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `webhook_id` | `uuid\|string` | Template, Required | - |
| `status_code` | `int` | Query, Optional | - |
| `error` | `string` | Query, Optional | - |
| `topic` | [`Topic2Enum`](../../doc/models/topic-2-enum.md) | Query, Optional | webhook topic |
| `start` | `int` | Query, Optional | **Default**: `0`<br>**Constraints**: `>= 0` |
| `end` | `int` | Query, Optional | **Default**: `0`<br>**Constraints**: `>= 0` |
| `duration` | `string` | Query, Optional | For historical stats and/or logs where time range is needed, you can specify the time range in a few different ways:<br><br>* ?start=1430000000&end=1430864000	specify the start / end<br>* ?end=1430864000&duration=1d	specify end time and duration<br>* ?duration=1d	specify duration, end will be now() in seconds<br>**Default**: `'1d'` |
| `limit` | `int` | Query, Optional | **Default**: `100`<br>**Constraints**: `>= 0` |

## Response Type

[`WebhookDeliverySearch`](../../doc/models/webhook-delivery-search.md)

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

webhook_id = '000000ab-00ab-00ab-00ab-0000000000ab'

start = 0

end = 0

duration = '10m'

limit = 100

result = sites_webhooks_controller.search_site_webhooks_deliveries(
    site_id,
    webhook_id,
    start,
    end,
    duration,
    limit
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "end": 1688035193,
  "limit": 10,
  "results": [
    {
      "error": "string",
      "id": "55b0f02f-ebf6-4ad2-8b10-200508a97581",
      "org_id": "fc7e2967-e7ef-41e6-b007-1217713de05a",
      "req_headers": "{\"Content-Type\":[\"application/json\"],\"User-Agent\":[\"Mist-webhook\"]}",
      "req_payload": "{\"topic\":\"audits\",\"events\":[{\"admin_name\":\"John Doe john.doe@juniper.net\",\"after\":\"{\\\"radio_config\\\": {\\\"band_24\\\": {\\\"disabled\\\": false, \\\"allow_rrm_disable\\\": false, \\\"power_min\\\": null, \\\"power_max\\\": null, \\\"power\\\": 10, \\\"preamble\\\": \\\"short\\\", \\\"channels\\\": [1, 10], \\\"bandwidth\\\": 20}}}\",\"before\":\"{\\\"radio_config\\\": {\\\"band_24\\\": {\\\"disabled\\\": false, \\\"allow_rrm_disable\\\": false, \\\"power_min\\\": 8, \\\"power_max\\\": 18, \\\"power\\\": null, \\\"preamble\\\": \\\"long\\\", \\\"channels\\\": [1, 10], \\\"bandwidth\\\": 20}}}\",\"id\":\"737909a2-04ff-4aeb-b9da-cc924e74a4dd\",\"message\":\"Update Site Settings\",\"org_id\":\"fc7e2967-e7ef-41e6-b007-1217713de05a\",\"site_id\":\"256c3a35-9cb7-436e-bc6d-314972645d95\",\"site_name\":\"Test Site\",\"src_ip\":\"1.2.3.4\",\"timestamp\":1685956576.923601,\"user_agent\":\"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36\"}]}",
      "req_url": "http://example.com",
      "resp_body": "Ok",
      "resp_headers": "string",
      "site_id": "256c3a35-9cb7-436e-bc6d-314972645d95",
      "status_code": 200,
      "timestamp": 1687962508.583656,
      "topic": "audits",
      "webhook_id": "7a11b901-f719-4c91-8aef-deb8699a6364"
    }
  ],
  "start": 1687948793,
  "total": 0
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesWebhooksEventsSearch401ErrorException`](../../doc/models/api-v1-sites-webhooks-events-search-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesWebhooksEventsSearch403ErrorException`](../../doc/models/api-v1-sites-webhooks-events-search-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesWebhooksEventsSearch404ErrorException`](../../doc/models/api-v1-sites-webhooks-events-search-404-error-exception.md) |


# Ping Site Webhook

send a Ping event to the webhook

```python
def ping_site_webhook(self,
                     site_id,
                     webhook_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `webhook_id` | `uuid\|string` | Template, Required | - |

## Response Type

`object`

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

webhook_id = '000000ab-00ab-00ab-00ab-0000000000ab'

result = sites_webhooks_controller.ping_site_webhook(
    site_id,
    webhook_id
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesWebhooksPing401ErrorException`](../../doc/models/api-v1-sites-webhooks-ping-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesWebhooksPing403ErrorException`](../../doc/models/api-v1-sites-webhooks-ping-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesWebhooksPing404ErrorException`](../../doc/models/api-v1-sites-webhooks-ping-404-error-exception.md) |

