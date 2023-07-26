# Sites Synthetic Tests

```python
sites_synthetic_tests_controller = client.sites_synthetic_tests
```

## Class Name

`SitesSyntheticTestsController`

## Methods

* [Start Site Switch Radius Synthetic Test](../../doc/controllers/sites-synthetic-tests.md#start-site-switch-radius-synthetic-test)
* [Start Site Device Synthetic Test](../../doc/controllers/sites-synthetic-tests.md#start-site-device-synthetic-test)
* [Get Site Synthetic Test Status](../../doc/controllers/sites-synthetic-tests.md#get-site-synthetic-test-status)
* [Trigger Site Synthetic Test](../../doc/controllers/sites-synthetic-tests.md#trigger-site-synthetic-test)


# Start Site Switch Radius Synthetic Test

Ping test from the AP to confirm ‘reachability’ of the Radius server. Utilize Juniper EX switch(to which an AP is connected to) radius test capabilities to get details on the Radius Server ‘availability’.

```python
def start_site_switch_radius_synthetic_test(self,
                                           site_id,
                                           device_id,
                                           body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `device_id` | `uuid\|string` | Template, Required | - |
| `body` | [`ApiV1SitesDevicesCheckRadiusServerRequest`](../../doc/models/api-v1-sites-devices-check-radius-server-request.md) | Body, Optional | - |

## Response Type

[`Session1`](../../doc/models/session-1.md)

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

device_id = '000000ab-00ab-00ab-00ab-0000000000ab'

body = ApiV1SitesDevicesCheckRadiusServerRequest(
    password='string',
    user='string',
    profile='dot1x'
)

result = sites_synthetic_tests_controller.start_site_switch_radius_synthetic_test(
    site_id,
    device_id,
    body
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "session": "session_id"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesDevicesCheckRadiusServer401ErrorException`](../../doc/models/api-v1-sites-devices-check-radius-server-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesDevicesCheckRadiusServer403ErrorException`](../../doc/models/api-v1-sites-devices-check-radius-server-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesDevicesCheckRadiusServer404ErrorException`](../../doc/models/api-v1-sites-devices-check-radius-server-404-error-exception.md) |


# Start Site Device Synthetic Test

Device Synthetic Test

```python
def start_site_device_synthetic_test(self,
                                    site_id,
                                    device_id,
                                    body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `device_id` | `uuid\|string` | Template, Required | - |
| `body` | [`ApiV1SitesDevicesSyntheticTestRequest`](../../doc/models/api-v1-sites-devices-synthetic-test-request.md) | Body, Optional | - |

## Response Type

`void`

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

device_id = '000000ab-00ab-00ab-00ab-0000000000ab'

result = sites_synthetic_tests_controller.start_site_device_synthetic_test(
    site_id,
    device_id
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Device not online / Device not supported / Already in progress | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesDevicesSyntheticTest401ErrorException`](../../doc/models/api-v1-sites-devices-synthetic-test-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesDevicesSyntheticTest403ErrorException`](../../doc/models/api-v1-sites-devices-synthetic-test-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesDevicesSyntheticTest404ErrorException`](../../doc/models/api-v1-sites-devices-synthetic-test-404-error-exception.md) |


# Get Site Synthetic Test Status

Get Synthetic Testing Status

```python
def get_site_synthetic_test_status(self,
                                  site_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |

## Response Type

[`ApiV1SitesSyntheticTestResponse`](../../doc/models/api-v1-sites-synthetic-test-response.md)

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

result = sites_synthetic_tests_controller.get_site_synthetic_test_status(site_id)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesSyntheticTest401ErrorException`](../../doc/models/api-v1-sites-synthetic-test-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesSyntheticTest403ErrorException`](../../doc/models/api-v1-sites-synthetic-test-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesSyntheticTest404ErrorException`](../../doc/models/api-v1-sites-synthetic-test-404-error-exception.md) |


# Trigger Site Synthetic Test

Trigger Synthetic Testing

```python
def trigger_site_synthetic_test(self,
                               site_id,
                               body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `body` | [`ApiV1SitesSyntheticTestRequest`](../../doc/models/api-v1-sites-synthetic-test-request.md) | Body, Optional | - |

## Response Type

[`ApiV1SitesSyntheticTestResponse1`](../../doc/models/api-v1-sites-synthetic-test-response-1.md)

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

body = ApiV1SitesSyntheticTestRequest(
    email='john@abc.com'
)

result = sites_synthetic_tests_controller.trigger_site_synthetic_test(
    site_id,
    body
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "email": "john@abc.com",
  "id": "68b329da-9893-e340-99c7-d8ad5cb9c940"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesSyntheticTest401ErrorException`](../../doc/models/api-v1-sites-synthetic-test-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesSyntheticTest403ErrorException`](../../doc/models/api-v1-sites-synthetic-test-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesSyntheticTest404ErrorException`](../../doc/models/api-v1-sites-synthetic-test-404-error-exception.md) |

