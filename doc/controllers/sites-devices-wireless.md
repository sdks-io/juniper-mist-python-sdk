# Sites Devices-Wireless

```python
sites_devices_wireless_controller = client.sites_devices_wireless
```

## Class Name

`SitesDevicesWirelessController`

## Methods

* [Get Site Device Radio Channels](../../doc/controllers/sites-devices-wireless.md#get-site-device-radio-channels)
* [Reprovision Site All Aps](../../doc/controllers/sites-devices-wireless.md#reprovision-site-all-aps)
* [Reset Site All Aps to Use Rrm](../../doc/controllers/sites-devices-wireless.md#reset-site-all-aps-to-use-rrm)
* [Zeroize Site Fips All Aps](../../doc/controllers/sites-devices-wireless.md#zeroize-site-fips-all-aps)
* [Get Site Device Iot Port](../../doc/controllers/sites-devices-wireless.md#get-site-device-iot-port)
* [Set Site Device Iot Port](../../doc/controllers/sites-devices-wireless.md#set-site-device-iot-port)
* [Start Site Locate Device](../../doc/controllers/sites-devices-wireless.md#start-site-locate-device)
* [Stop Site Locate Device](../../doc/controllers/sites-devices-wireless.md#stop-site-locate-device)


# Get Site Device Radio Channels

Get a list of allowed channels (per channel width)

```python
def get_site_device_radio_channels(self,
                                  site_id,
                                  country_code=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `country_code` | `string` | Query, Optional | country code for the site (for AP config generation), in [two-character](http://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) |

## Response Type

[`DeviceRadioChannels`](../../doc/models/device-radio-channels.md)

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

country_code = 'US'

result = sites_devices_wireless_controller.get_site_device_radio_channels(
    site_id,
    country_code
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "band24_40mhz_allowed": false,
  "band24_channels": {
    "20": [
      1,
      2,
      3,
      4,
      5,
      6,
      7,
      8,
      9,
      10,
      11
    ],
    "40": [
      1,
      2,
      3,
      4,
      5,
      6,
      7,
      8,
      9,
      10,
      11
    ]
  },
  "band24_enabled": true,
  "band5_channels": {
    "20": [
      36,
      40,
      44,
      48,
      52,
      56,
      60,
      64,
      100,
      104,
      108,
      112,
      116,
      120,
      124,
      128,
      132,
      136,
      140,
      144,
      149,
      153,
      157,
      161,
      165
    ],
    "40": [
      36,
      40,
      44,
      48,
      52,
      56,
      60,
      64,
      100,
      104,
      108,
      112,
      116,
      120,
      124,
      128,
      132,
      136,
      140,
      144,
      149,
      153,
      157,
      161
    ],
    "80": [
      36,
      40,
      44,
      48,
      52,
      56,
      60,
      64,
      100,
      104,
      108,
      112,
      116,
      120,
      124,
      128,
      132,
      136,
      140,
      144,
      149,
      153,
      157,
      161
    ],
    "dfs": [
      52,
      56,
      60,
      64,
      100,
      104,
      108,
      112,
      116,
      120,
      124,
      128,
      132,
      136,
      140,
      144
    ],
    "outdoor": [
      36,
      40,
      44,
      48,
      52,
      56,
      60,
      64,
      100,
      104,
      108,
      112,
      116,
      120,
      124,
      128,
      132,
      136,
      140,
      144,
      149,
      153,
      157,
      161,
      165
    ]
  },
  "band5_enabled": true,
  "certified": true,
  "code": 840,
  "dfs_ok": true,
  "key": "US",
  "name": "United States",
  "uses": "US_FCC"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesDevicesApChannels401ErrorException`](../../doc/models/api-v1-sites-devices-ap-channels-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesDevicesApChannels403ErrorException`](../../doc/models/api-v1-sites-devices-ap-channels-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesDevicesApChannels404ErrorException`](../../doc/models/api-v1-sites-devices-ap-channels-404-error-exception.md) |


# Reprovision Site All Aps

To force all APs to reprovision itself again.

```python
def reprovision_site_all_aps(self,
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

result = sites_devices_wireless_controller.reprovision_site_all_aps(site_id)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesDevicesReprovision401ErrorException`](../../doc/models/api-v1-sites-devices-reprovision-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesDevicesReprovision403ErrorException`](../../doc/models/api-v1-sites-devices-reprovision-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesDevicesReprovision404ErrorException`](../../doc/models/api-v1-sites-devices-reprovision-404-error-exception.md) |


# Reset Site All Aps to Use Rrm

Reset all APs in the Site to use RRM

```python
def reset_site_all_aps_to_use_rrm(self,
                                 site_id,
                                 body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `body` | [`ApiV1SitesDevicesResetRadioConfigRequest`](../../doc/models/api-v1-sites-devices-reset-radio-config-request.md) | Body, Optional | Request Body |

## Response Type

`object`

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

body = ApiV1SitesDevicesResetRadioConfigRequest(
    bands=[
        '24',
        '5',
        '6'
    ],
    force=False
)

result = sites_devices_wireless_controller.reset_site_all_aps_to_use_rrm(
    site_id,
    body
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesDevicesResetRadioConfig401ErrorException`](../../doc/models/api-v1-sites-devices-reset-radio-config-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesDevicesResetRadioConfig403ErrorException`](../../doc/models/api-v1-sites-devices-reset-radio-config-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesDevicesResetRadioConfig404ErrorException`](../../doc/models/api-v1-sites-devices-reset-radio-config-404-error-exception.md) |


# Zeroize Site Fips All Aps

Zeroize all FIPS APs in the Site

```python
def zeroize_site_fips_all_aps(self,
                             site_id,
                             body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `body` | [`ApiV1SitesDevicesZeriozeRequest`](../../doc/models/api-v1-sites-devices-zerioze-request.md) | Body, Optional | Request Body |

## Response Type

`object`

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

body = ApiV1SitesDevicesZeriozeRequest(
    password='NUKETHESITE'
)

result = sites_devices_wireless_controller.zeroize_site_fips_all_aps(
    site_id,
    body
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesDevicesZerioze401ErrorException`](../../doc/models/api-v1-sites-devices-zerioze-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesDevicesZerioze403ErrorException`](../../doc/models/api-v1-sites-devices-zerioze-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesDevicesZerioze404ErrorException`](../../doc/models/api-v1-sites-devices-zerioze-404-error-exception.md) |


# Get Site Device Iot Port

Returns the current state of each enabled IoT pin configured as an output.

```python
def get_site_device_iot_port(self,
                            site_id,
                            device_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `device_id` | `uuid\|string` | Template, Required | - |

## Response Type

`dict`

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

device_id = '000000ab-00ab-00ab-00ab-0000000000ab'

result = sites_devices_wireless_controller.get_site_device_iot_port(
    site_id,
    device_id
)
print(result)
```

## Example Response

```
{
  "A1": 1,
  "DO": 0
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesDevicesIot401ErrorException`](../../doc/models/api-v1-sites-devices-iot-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesDevicesIot403ErrorException`](../../doc/models/api-v1-sites-devices-iot-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesDevicesIot404ErrorException`](../../doc/models/api-v1-sites-devices-iot-404-error-exception.md) |


# Set Site Device Iot Port

**Note**: For each IoT pin referenced:

* The pin must be enabled using the Device `iot_config` API
* The pin must support the output direction

```python
def set_site_device_iot_port(self,
                            site_id,
                            device_id,
                            body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `device_id` | `uuid\|string` | Template, Required | - |
| `body` | `dict` | Body, Optional | Request Body |

## Response Type

`dict`

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

device_id = '000000ab-00ab-00ab-00ab-0000000000ab'

body = {
    "A1": 1,
    "DO": 0
}

result = sites_devices_wireless_controller.set_site_device_iot_port(
    site_id,
    device_id,
    body
)
print(result)
```

## Example Response

```
{
  "A1": 1,
  "DO": 0
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesDevicesIot401ErrorException`](../../doc/models/api-v1-sites-devices-iot-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesDevicesIot403ErrorException`](../../doc/models/api-v1-sites-devices-iot-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesDevicesIot404ErrorException`](../../doc/models/api-v1-sites-devices-iot-404-error-exception.md) |


# Start Site Locate Device

Locate a Device by blinking it’s LED, it’s a persisted state that has to be stopped by calling Stop Locating API

```python
def start_site_locate_device(self,
                            site_id,
                            device_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `device_id` | `uuid\|string` | Template, Required | - |

## Response Type

`object`

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

device_id = '000000ab-00ab-00ab-00ab-0000000000ab'

result = sites_devices_wireless_controller.start_site_locate_device(
    site_id,
    device_id
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesDevicesLocate401ErrorException`](../../doc/models/api-v1-sites-devices-locate-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesDevicesLocate403ErrorException`](../../doc/models/api-v1-sites-devices-locate-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesDevicesLocate404ErrorException`](../../doc/models/api-v1-sites-devices-locate-404-error-exception.md) |


# Stop Site Locate Device

Stop Locate a Device

```python
def stop_site_locate_device(self,
                           site_id,
                           device_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `device_id` | `uuid\|string` | Template, Required | - |

## Response Type

`object`

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

device_id = '000000ab-00ab-00ab-00ab-0000000000ab'

result = sites_devices_wireless_controller.stop_site_locate_device(
    site_id,
    device_id
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesDevicesUnlocate401ErrorException`](../../doc/models/api-v1-sites-devices-unlocate-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesDevicesUnlocate403ErrorException`](../../doc/models/api-v1-sites-devices-unlocate-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesDevicesUnlocate404ErrorException`](../../doc/models/api-v1-sites-devices-unlocate-404-error-exception.md) |

