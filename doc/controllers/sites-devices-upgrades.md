# Sites Devices Upgrades

```python
sites_devices_upgrades_controller = client.sites_devices_upgrades
```

## Class Name

`SitesDevicesUpgradesController`

## Methods

* [List Site Devices Upgrade](../../doc/controllers/sites-devices-upgrades.md#list-site-devices-upgrade)
* [Multi Upgrade Site Devices](../../doc/controllers/sites-devices-upgrades.md#multi-upgrade-site-devices)
* [Get Site Upgrade](../../doc/controllers/sites-devices-upgrades.md#get-site-upgrade)
* [Cancel Site Device Upgrade](../../doc/controllers/sites-devices-upgrades.md#cancel-site-device-upgrade)
* [List Site Available Device Versions](../../doc/controllers/sites-devices-upgrades.md#list-site-available-device-versions)
* [Upgrade Site Device](../../doc/controllers/sites-devices-upgrades.md#upgrade-site-device)
* [Get Site Ssr Upgrade](../../doc/controllers/sites-devices-upgrades.md#get-site-ssr-upgrade)
* [Upgrade Site Ssr](../../doc/controllers/sites-devices-upgrades.md#upgrade-site-ssr)


# List Site Devices Upgrade

Get all upgrades for site

```python
def list_site_devices_upgrade(self,
                             site_id,
                             status=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `status` | [`Status6Enum`](../../doc/models/status-6-enum.md) | Query, Optional | - |

## Response Type

[`List of DeviceUpgradeResponse`](../../doc/models/device-upgrade-response.md)

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

result = sites_devices_upgrades_controller.list_site_devices_upgrade(site_id)
print(result)
```

## Example Response *(as JSON)*

```json
[
  {
    "counts": {
      "download_requested": 0,
      "downloaded": 0,
      "failed": 0,
      "reboot_in_progress": 0,
      "rebooted": 0,
      "skipped": 0,
      "total": 0
    },
    "enable_p2p": true,
    "force": true,
    "id": "472f6eca-6276-4993-bfeb-53cbbbba6f28",
    "start_time": 0,
    "status": "created",
    "strategy": "big_bang",
    "target_version": "string"
  }
]
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesDevicesUpgrade401ErrorException`](../../doc/models/api-v1-sites-devices-upgrade-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesDevicesUpgrade403ErrorException`](../../doc/models/api-v1-sites-devices-upgrade-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesDevicesUpgrade404ErrorException`](../../doc/models/api-v1-sites-devices-upgrade-404-error-exception.md) |


# Multi Upgrade Site Devices

Upgrade Multiple Device

**Note**: this call doesn’t guarantee the devices to be upgraded right away (they may be offline)

```python
def multi_upgrade_site_devices(self,
                              site_id,
                              body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `body` | [`DeviceUpgrade`](../../doc/models/device-upgrade.md) | Body, Optional | Request Body |

## Response Type

[`DeviceUpgradeResponse`](../../doc/models/device-upgrade-response.md)

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

body = DeviceUpgrade(
    canary_phases=[
        1,
        10,
        50,
        100
    ],
    device_ids=[
        'string'
    ],
    enable_p_2_p=True,
    force=False,
    max_failure_percentage=5,
    max_failures=[
        0
    ],
    models=[
        'string'
    ],
    start_time=0,
    strategy=StrategyEnum.BIG_BANG,
    version='stable'
)

result = sites_devices_upgrades_controller.multi_upgrade_site_devices(
    site_id,
    body
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "counts": {
    "downloaded": 0,
    "failed": 0,
    "reboot_in_progress": 0,
    "rebooted": 0,
    "total": 0
  },
  "enable_p2p": true,
  "force": true,
  "id": "473f6eca-6276-4993-bfeb-53cbbbba6f18",
  "start_time": 0,
  "status": "created",
  "strategy": "big_bang",
  "target_version": "string"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesDevicesUpgrade401ErrorException`](../../doc/models/api-v1-sites-devices-upgrade-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesDevicesUpgrade403ErrorException`](../../doc/models/api-v1-sites-devices-upgrade-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesDevicesUpgrade404ErrorException`](../../doc/models/api-v1-sites-devices-upgrade-404-error-exception.md) |


# Get Site Upgrade

Get Site Device Upgrade

```python
def get_site_upgrade(self,
                    site_id,
                    upgrade_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `upgrade_id` | `uuid\|string` | Template, Required | - |

## Response Type

[`DeviceUpgradeResponse`](../../doc/models/device-upgrade-response.md)

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

upgrade_id = '000000ab-00ab-00ab-00ab-0000000000ab'

result = sites_devices_upgrades_controller.get_site_upgrade(
    site_id,
    upgrade_id
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "counts": {
    "downloaded": 0,
    "failed": 0,
    "reboot_in_progress": 0,
    "rebooted": 0,
    "total": 0
  },
  "enable_p2p": true,
  "force": true,
  "id": "473f6eca-6276-4993-bfeb-53cbbbba6f18",
  "start_time": 0,
  "status": "created",
  "strategy": "big_bang",
  "target_version": "string"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesDevicesUpgrade401ErrorException`](../../doc/models/api-v1-sites-devices-upgrade-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesDevicesUpgrade403ErrorException`](../../doc/models/api-v1-sites-devices-upgrade-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesDevicesUpgrade404ErrorException`](../../doc/models/api-v1-sites-devices-upgrade-404-error-exception.md) |


# Cancel Site Device Upgrade

Best effort to cancel an upgrade. Devices which are already upgraded wont be touched

```python
def cancel_site_device_upgrade(self,
                              site_id,
                              upgrade_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `upgrade_id` | `uuid\|string` | Template, Required | - |

## Response Type

`object`

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

upgrade_id = '000000ab-00ab-00ab-00ab-0000000000ab'

result = sites_devices_upgrades_controller.cancel_site_device_upgrade(
    site_id,
    upgrade_id
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesDevicesUpgradeCancel401ErrorException`](../../doc/models/api-v1-sites-devices-upgrade-cancel-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesDevicesUpgradeCancel403ErrorException`](../../doc/models/api-v1-sites-devices-upgrade-cancel-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesDevicesUpgradeCancel404ErrorException`](../../doc/models/api-v1-sites-devices-upgrade-cancel-404-error-exception.md) |


# List Site Available Device Versions

Get List of Available Device Versions

```python
def list_site_available_device_versions(self,
                                       site_id,
                                       mtype='ap',
                                       model=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `mtype` | [`Type16Enum`](../../doc/models/type-16-enum.md) | Query, Optional | fetch version for device type (E.g. switch)<br>**Default**: `'ap'` |
| `model` | `string` | Query, Optional | fetch version for device model, use/combine with `type` as needed (for switch and gateway devices) |

## Response Type

[`List of DeviceVersion`](../../doc/models/device-version.md)

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

mtype = Type16Enum.AP

result = sites_devices_upgrades_controller.list_site_available_device_versions(
    site_id,
    mtype
)
print(result)
```

## Example Response *(as JSON)*

```json
[
  {
    "model": "AP41",
    "tag": "stable",
    "version": "v0.1.543"
  },
  {
    "model": "AP21",
    "version": "v0.1.545"
  }
]
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesDevicesVersions401ErrorException`](../../doc/models/api-v1-sites-devices-versions-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesDevicesVersions403ErrorException`](../../doc/models/api-v1-sites-devices-versions-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesDevicesVersions404ErrorException`](../../doc/models/api-v1-sites-devices-versions-404-error-exception.md) |


# Upgrade Site Device

Device Upgrade

```python
def upgrade_site_device(self,
                       site_id,
                       device_id,
                       body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `device_id` | `uuid\|string` | Template, Required | - |
| `body` | [`ApiV1SitesDevicesUpgradeRequest`](../../doc/models/api-v1-sites-devices-upgrade-request.md) | Body, Optional | - |

## Response Type

[`UpgradeStatus`](../../doc/models/upgrade-status.md)

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

device_id = '000000ab-00ab-00ab-00ab-0000000000ab'

body = ApiV1SitesDevicesUpgradeRequest(
    version='3.1.5'
)

result = sites_devices_upgrades_controller.upgrade_site_device(
    site_id,
    device_id,
    body
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "status": "inprogress",
  "status_id": 5,
  "timestamp": 1428949501
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesDevicesUpgrade401ErrorException`](../../doc/models/api-v1-sites-devices-upgrade-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesDevicesUpgrade403ErrorException`](../../doc/models/api-v1-sites-devices-upgrade-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesDevicesUpgrade404ErrorException`](../../doc/models/api-v1-sites-devices-upgrade-404-error-exception.md) |


# Get Site Ssr Upgrade

Get Specific Site SSR Upgrade

```python
def get_site_ssr_upgrade(self,
                        site_id,
                        upgrade_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `upgrade_id` | `uuid\|string` | Template, Required | - |

## Response Type

[`ApiV1SitesSsrUpgradeResponse`](../../doc/models/api-v1-sites-ssr-upgrade-response.md)

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

upgrade_id = '000000ab-00ab-00ab-00ab-0000000000ab'

result = sites_devices_upgrades_controller.get_site_ssr_upgrade(
    site_id,
    upgrade_id
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "channel": "stable",
  "device_type": "gateway",
  "id": "5cbcee0a-c620-4bb4-a25e-15000934e9d8",
  "status": "upgrading",
  "targets": {
    "failed": [],
    "queued": [],
    "success": [],
    "upgrading": [
      "8e525f1d-4178-4ae1-a988-2b0176855e55"
    ]
  },
  "versions": {}
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesSsrUpgrade401ErrorException`](../../doc/models/api-v1-sites-ssr-upgrade-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesSsrUpgrade403ErrorException`](../../doc/models/api-v1-sites-ssr-upgrade-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesSsrUpgrade404ErrorException`](../../doc/models/api-v1-sites-ssr-upgrade-404-error-exception.md) |


# Upgrade Site Ssr

Upgrade Site SSR device

```python
def upgrade_site_ssr(self,
                    site_id,
                    device_id,
                    body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `device_id` | `uuid\|string` | Template, Required | - |
| `body` | [`ApiV1SitesSsrUpgradeRequest`](../../doc/models/api-v1-sites-ssr-upgrade-request.md) | Body, Optional | - |

## Response Type

[`SsrUpgradeResponse`](../../doc/models/ssr-upgrade-response.md)

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

device_id = '000000ab-00ab-00ab-00ab-0000000000ab'

body = ApiV1SitesSsrUpgradeRequest(
    version='5.3.1-170-93',
    channel=ChannelEnum.STABLE
)

result = sites_devices_upgrades_controller.upgrade_site_ssr(
    site_id,
    device_id,
    body
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "channel": "stable",
  "counts": {
    "failed": 0,
    "queued": 1,
    "success": 0,
    "upgrading": 1
  },
  "device_type": "gateway",
  "id": "ceef2c8a-e2e6-447a-8b27-cb4f3ec1adae",
  "status": "upgrading",
  "strategy": "serial",
  "versions": {}
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesSsrUpgrade401ErrorException`](../../doc/models/api-v1-sites-ssr-upgrade-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesSsrUpgrade403ErrorException`](../../doc/models/api-v1-sites-ssr-upgrade-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesSsrUpgrade404ErrorException`](../../doc/models/api-v1-sites-ssr-upgrade-404-error-exception.md) |

