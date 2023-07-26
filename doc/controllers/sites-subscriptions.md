# Sites Subscriptions

```python
sites_subscriptions_controller = client.sites_subscriptions
```

## Class Name

`SitesSubscriptionsController`

## Methods

* [Unsubscribe Site Alarms](../../doc/controllers/sites-subscriptions.md#unsubscribe-site-alarms)
* [Subscribe Site Alarms](../../doc/controllers/sites-subscriptions.md#subscribe-site-alarms)


# Unsubscribe Site Alarms

Unsubscribe to Site Alarms

```python
def unsubscribe_site_alarms(self,
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

result = sites_subscriptions_controller.unsubscribe_site_alarms(site_id)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesSubscriptions401ErrorException`](../../doc/models/api-v1-sites-subscriptions-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesSubscriptions403ErrorException`](../../doc/models/api-v1-sites-subscriptions-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesSubscriptions404ErrorException`](../../doc/models/api-v1-sites-subscriptions-404-error-exception.md) |


# Subscribe Site Alarms

Subscribe to Site Alarms

```python
def subscribe_site_alarms(self,
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

result = sites_subscriptions_controller.subscribe_site_alarms(site_id)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesSubscriptions401ErrorException`](../../doc/models/api-v1-sites-subscriptions-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesSubscriptions403ErrorException`](../../doc/models/api-v1-sites-subscriptions-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesSubscriptions404ErrorException`](../../doc/models/api-v1-sites-subscriptions-404-error-exception.md) |

