# Installer

In a typical enterprise, a separate group of people, Installers, are responsible for install new devices. May it be a new installation (e.g. new stores), a replacement installation (e.g. replacing Cisco APs with Mist APs), or addition (e.g. adding new APs for better coverage). Instead of granting them Admin/Write privilege, it's more desirable to grant them minimum privileges to do the initial provisioning so they cannot read sensible information (e.g. PSK of a WLAN), or change configs of running APs.
At a high level, Installer APs try to achieve the following:

1. identifying a device by MAC (that’s what they see)
2. they can only touch configurations of the devices they’re installing
3. allow the following configurations: * name * site assignment * device  profile assignment * map and location (x/y) assignment * claim (if not already in the inventory) * replace existing device with the device being installed

* Grace Period *
  Grace period provides a dynamic way to limit what devices / sites   installer can work on. Generally installers work on recent deployments -  bringing up new sites, add newly claimed devices to new / existing sites. They  make mistakes, too, and may need to further tweak some of the parameters.   Default grace period is 7 days and can be set from 1 day to 365 days.

```python
installer_controller = client.installer
```

## Class Name

`InstallerController`

## Methods

* [List Installer Alarm Templates](../../doc/controllers/installer.md#list-installer-alarm-templates)
* [List Installer Device Profiles](../../doc/controllers/installer.md#list-installer-device-profiles)
* [List Installer List of Renctly Claimed Devices](../../doc/controllers/installer.md#list-installer-list-of-renctly-claimed-devices)
* [Claim Installer Devices](../../doc/controllers/installer.md#claim-installer-devices)
* [Unassign Installer Recently Claimed Device](../../doc/controllers/installer.md#unassign-installer-recently-claimed-device)
* [Provision Installer Devices](../../doc/controllers/installer.md#provision-installer-devices)
* [Start Installer Locate Device](../../doc/controllers/installer.md#start-installer-locate-device)
* [Stop Installer Locate Device](../../doc/controllers/installer.md#stop-installer-locate-device)
* [Delete Installer Device Image](../../doc/controllers/installer.md#delete-installer-device-image)
* [Add Installer Device Image](../../doc/controllers/installer.md#add-installer-device-image)
* [List Installer Rf Templates Names](../../doc/controllers/installer.md#list-installer-rf-templates-names)
* [List Installer Sec Policies](../../doc/controllers/installer.md#list-installer-sec-policies)
* [List Installer Site Groups](../../doc/controllers/installer.md#list-installer-site-groups)
* [List Installer Sites](../../doc/controllers/installer.md#list-installer-sites)
* [Create or Update Installer Sites](../../doc/controllers/installer.md#create-or-update-installer-sites)
* [List Installer Maps](../../doc/controllers/installer.md#list-installer-maps)
* [Import Installer Map](../../doc/controllers/installer.md#import-installer-map)
* [Delete Installer Map](../../doc/controllers/installer.md#delete-installer-map)
* [Create Installer Map](../../doc/controllers/installer.md#create-installer-map)
* [Update Installer Map](../../doc/controllers/installer.md#update-installer-map)
* [Optimize Installer Rrm](../../doc/controllers/installer.md#optimize-installer-rrm)


# List Installer Alarm Templates

Get List of alarm templates

```python
def list_installer_alarm_templates(self,
                                  org_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `org_id` | `uuid\|string` | Template, Required | - |

## Response Type

[`List of ApiV1InstallerOrgsAlarmtemplatesResponse`](../../doc/models/api-v1-installer-orgs-alarmtemplates-response.md)

## Example Usage

```python
org_id = '000000ab-00ab-00ab-00ab-0000000000ab'

result = installer_controller.list_installer_alarm_templates(org_id)
print(result)
```

## Example Response *(as JSON)*

```json
[
  {
    "id": "684dfc5c-fe77-2290-eb1d-ef3d677fe168",
    "name": "AlarmTemplate 1"
  }
]
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1InstallerOrgsAlarmtemplates401ErrorException`](../../doc/models/api-v1-installer-orgs-alarmtemplates-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1InstallerOrgsAlarmtemplates403ErrorException`](../../doc/models/api-v1-installer-orgs-alarmtemplates-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1InstallerOrgsAlarmtemplates404ErrorException`](../../doc/models/api-v1-installer-orgs-alarmtemplates-404-error-exception.md) |


# List Installer Device Profiles

Get List of Device Profiles

```python
def list_installer_device_profiles(self,
                                  org_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `org_id` | `uuid\|string` | Template, Required | - |

## Response Type

[`List of ApiV1InstallerOrgsDeviceprofilesResponse`](../../doc/models/api-v1-installer-orgs-deviceprofiles-response.md)

## Example Usage

```python
org_id = '000000ab-00ab-00ab-00ab-0000000000ab'

result = installer_controller.list_installer_device_profiles(org_id)
print(result)
```

## Example Response *(as JSON)*

```json
[
  {
    "id": "6f4bf402-45f9-2a56-6c8b-7f83d3bc98e9",
    "name": "DeviceProfile 1"
  }
]
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1InstallerOrgsDeviceprofiles401ErrorException`](../../doc/models/api-v1-installer-orgs-deviceprofiles-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1InstallerOrgsDeviceprofiles403ErrorException`](../../doc/models/api-v1-installer-orgs-deviceprofiles-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1InstallerOrgsDeviceprofiles404ErrorException`](../../doc/models/api-v1-installer-orgs-deviceprofiles-404-error-exception.md) |


# List Installer List of Renctly Claimed Devices

Get List of recently claimed devices

```python
def list_installer_list_of_renctly_claimed_devices(self,
                                                  org_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `org_id` | `uuid\|string` | Template, Required | - |

## Response Type

[`List of ApiV1InstallerOrgsDevicesResponse`](../../doc/models/api-v1-installer-orgs-devices-response.md)

## Example Usage

```python
org_id = '000000ab-00ab-00ab-00ab-0000000000ab'

result = installer_controller.list_installer_list_of_renctly_claimed_devices(org_id)
print(result)
```

## Example Response *(as JSON)*

```json
[
  {
    "connected": true,
    "mac": "5c5b35000018",
    "model": "AP41",
    "serial": "FXLH2015150025"
  },
  {
    "connected": false,
    "deviceprofile_name": "SJ1",
    "name": "hallway",
    "site_name": "SJ1"
  },
  {
    "connected": true,
    "height": 2.7,
    "map_id": "845a23bf-bed9-e43c-4c86-6fa474be7ae5",
    "orientation": 90,
    "x": 150,
    "y": 300
  }
]
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1InstallerOrgsDevices401ErrorException`](../../doc/models/api-v1-installer-orgs-devices-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1InstallerOrgsDevices403ErrorException`](../../doc/models/api-v1-installer-orgs-devices-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1InstallerOrgsDevices404ErrorException`](../../doc/models/api-v1-installer-orgs-devices-404-error-exception.md) |


# Claim Installer Devices

This mirrors `POST /api/v1/orgs/{org_id}/inventory` (see Inventory API)

```python
def claim_installer_devices(self,
                           org_id,
                           body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `org_id` | `uuid\|string` | Template, Required | - |
| `body` | `List of string` | Body, Optional | Request Body |

## Response Type

[`ApiV1InstallerOrgsDevicesResponse1`](../../doc/models/api-v1-installer-orgs-devices-response-1.md)

## Example Usage

```python
org_id = '000000ab-00ab-00ab-00ab-0000000000ab'

body = [
    '6JG8E-PTFV2-A9Z2N',
    'DVH4V-SNMSZ-PDXBR'
]

result = installer_controller.claim_installer_devices(
    org_id,
    body
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "added": [
    "6JG8E-PTFV2-A9Z2N"
  ],
  "duplicated": [
    "DVH4V-SNMSZ-PDXBR"
  ],
  "error": [
    "PO1025335ohoh"
  ],
  "inventory_added": [
    {
      "mac": "5c5b35000018",
      "magic": "6JG8EPTFV2A9Z2N",
      "model": "AP41",
      "serial": "FXLH2015150025",
      "type": "ap"
    }
  ],
  "inventory_duplicated": [
    {
      "mac": "5c5b35000012",
      "magic": "DVH4VSNMSZPDXBR",
      "model": "AP41",
      "serial": "FXLH2015150027",
      "type": "ap"
    }
  ]
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request if none of the entries are valid | `APIException` |
| 401 | Unauthorized | [`ApiV1InstallerOrgsDevices401ErrorException`](../../doc/models/api-v1-installer-orgs-devices-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1InstallerOrgsDevices403ErrorException`](../../doc/models/api-v1-installer-orgs-devices-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1InstallerOrgsDevices404ErrorException`](../../doc/models/api-v1-installer-orgs-devices-404-error-exception.md) |


# Unassign Installer Recently Claimed Device

Unassign recently claimed devices

```python
def unassign_installer_recently_claimed_device(self,
                                              org_id,
                                              device_mac)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `org_id` | `uuid\|string` | Template, Required | - |
| `device_mac` | `string` | Template, Required | **Constraints**: *Pattern*: `^[0-9a-fA-F]{12}$` |

## Response Type

`object`

## Example Usage

```python
org_id = '000000ab-00ab-00ab-00ab-0000000000ab'

device_mac = '0000000000ab'

result = installer_controller.unassign_installer_recently_claimed_device(
    org_id,
    device_mac
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1InstallerOrgsDevices401ErrorException`](../../doc/models/api-v1-installer-orgs-devices-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1InstallerOrgsDevices403ErrorException`](../../doc/models/api-v1-installer-orgs-devices-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1InstallerOrgsDevices404ErrorException`](../../doc/models/api-v1-installer-orgs-devices-404-error-exception.md) |


# Provision Installer Devices

Provision or Replace a device

If replacing_mac is in the request payload, other attributes are ignored, we attempt to replace existing device (with mac replacing_mac) with the inventory device being configured. The replacement device must be in the inventory but not assigned, and the replacing_mac device must be assigned to a site, and satisfy grace period requirements. The Device replaced will become unassigned.

```python
def provision_installer_devices(self,
                               org_id,
                               device_mac,
                               body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `org_id` | `uuid\|string` | Template, Required | - |
| `device_mac` | `string` | Template, Required | **Constraints**: *Pattern*: `^[0-9a-fA-F]{12}$` |
| `body` | [`InstallerDevices`](../../doc/models/installer-devices.md) | Body, Optional | Request Body |

## Response Type

`object`

## Example Usage

```python
org_id = '000000ab-00ab-00ab-00ab-0000000000ab'

device_mac = '0000000000ab'

body = InstallerDevices(
    name='string',
    deviceprofile_name='string',
    for_site=True,
    height=0,
    map_id='09d2b626-2e4e-45ef-a3c4-e6aeb6c83db1',
    orientation=0,
    site_id='72771e6a-6f5e-4de4-a5b9-1266c4197811',
    site_name='string',
    x=0,
    y=0
)

result = installer_controller.provision_installer_devices(
    org_id,
    device_mac,
    body
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request | [`ApiV1InstallerOrgsDevices400ErrorException`](../../doc/models/api-v1-installer-orgs-devices-400-error-exception.md) |
| 401 | Unauthorized | [`ApiV1InstallerOrgsDevices401ErrorException`](../../doc/models/api-v1-installer-orgs-devices-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1InstallerOrgsDevices403ErrorException`](../../doc/models/api-v1-installer-orgs-devices-403-error-exception.md) |
| 404 | Not Found | [`ApiV1InstallerOrgsDevices404ErrorException`](../../doc/models/api-v1-installer-orgs-devices-404-error-exception.md) |


# Start Installer Locate Device

Locate a Device by blinking it’s LED, it’s a persisted state that has to be stopped by calling Stop Locating API

```python
def start_installer_locate_device(self,
                                 org_id,
                                 device_mac,
                                 body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `org_id` | `uuid\|string` | Template, Required | - |
| `device_mac` | `string` | Template, Required | **Constraints**: *Pattern*: `^[0-9a-fA-F]{12}$` |
| `body` | `object` | Body, Optional | - |

## Response Type

`object`

## Example Usage

```python
org_id = '000000ab-00ab-00ab-00ab-0000000000ab'

device_mac = '0000000000ab'

result = installer_controller.start_installer_locate_device(
    org_id,
    device_mac
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1InstallerOrgsDevicesLocate401ErrorException`](../../doc/models/api-v1-installer-orgs-devices-locate-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1InstallerOrgsDevicesLocate403ErrorException`](../../doc/models/api-v1-installer-orgs-devices-locate-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1InstallerOrgsDevicesLocate404ErrorException`](../../doc/models/api-v1-installer-orgs-devices-locate-404-error-exception.md) |


# Stop Installer Locate Device

Stop it

```python
def stop_installer_locate_device(self,
                                org_id,
                                device_mac)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `org_id` | `uuid\|string` | Template, Required | - |
| `device_mac` | `string` | Template, Required | **Constraints**: *Pattern*: `^[0-9a-fA-F]{12}$` |

## Response Type

`object`

## Example Usage

```python
org_id = '000000ab-00ab-00ab-00ab-0000000000ab'

device_mac = '0000000000ab'

result = installer_controller.stop_installer_locate_device(
    org_id,
    device_mac
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1InstallerOrgsDevicesUnlocate401ErrorException`](../../doc/models/api-v1-installer-orgs-devices-unlocate-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1InstallerOrgsDevicesUnlocate403ErrorException`](../../doc/models/api-v1-installer-orgs-devices-unlocate-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1InstallerOrgsDevicesUnlocate404ErrorException`](../../doc/models/api-v1-installer-orgs-devices-unlocate-404-error-exception.md) |


# Delete Installer Device Image

delete image

```python
def delete_installer_device_image(self,
                                 org_id,
                                 image_name,
                                 device_mac)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `org_id` | `uuid\|string` | Template, Required | - |
| `image_name` | `string` | Template, Required | - |
| `device_mac` | `string` | Template, Required | **Constraints**: *Pattern*: `^[0-9a-fA-F]{12}$` |

## Response Type

`object`

## Example Usage

```python
org_id = '000000ab-00ab-00ab-00ab-0000000000ab'

image_name = 'image_name6'

device_mac = '0000000000ab'

result = installer_controller.delete_installer_device_image(
    org_id,
    image_name,
    device_mac
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1InstallerOrgsDevicesImageName401ErrorException`](../../doc/models/api-v1-installer-orgs-devices-image-name-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1InstallerOrgsDevicesImageName403ErrorException`](../../doc/models/api-v1-installer-orgs-devices-image-name-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1InstallerOrgsDevicesImageName404ErrorException`](../../doc/models/api-v1-installer-orgs-devices-image-name-404-error-exception.md) |


# Add Installer Device Image

Add image

```python
def add_installer_device_image(self,
                              org_id,
                              image_name,
                              device_mac,
                              file=None,
                              json=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `org_id` | `uuid\|string` | Template, Required | - |
| `image_name` | `string` | Template, Required | - |
| `device_mac` | `string` | Template, Required | **Constraints**: *Pattern*: `^[0-9a-fA-F]{12}$` |
| `file` | `string` | Form, Optional | binary file |
| `json` | `string` | Form, Optional | JSON string describing your upload |

## Response Type

`object`

## Example Usage

```python
org_id = '000000ab-00ab-00ab-00ab-0000000000ab'

image_name = 'image_name6'

device_mac = '0000000000ab'

result = installer_controller.add_installer_device_image(
    org_id,
    image_name,
    device_mac
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1InstallerOrgsDevicesImageName401ErrorException`](../../doc/models/api-v1-installer-orgs-devices-image-name-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1InstallerOrgsDevicesImageName403ErrorException`](../../doc/models/api-v1-installer-orgs-devices-image-name-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1InstallerOrgsDevicesImageName404ErrorException`](../../doc/models/api-v1-installer-orgs-devices-image-name-404-error-exception.md) |


# List Installer Rf Templates Names

Get List of RF Templates

```python
def list_installer_rf_templates_names(self,
                                     org_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `org_id` | `uuid\|string` | Template, Required | - |

## Response Type

[`List of ApiV1InstallerOrgsRftemplatesResponse`](../../doc/models/api-v1-installer-orgs-rftemplates-response.md)

## Example Usage

```python
org_id = '000000ab-00ab-00ab-00ab-0000000000ab'

result = installer_controller.list_installer_rf_templates_names(org_id)
print(result)
```

## Example Response *(as JSON)*

```json
[
  {
    "id": "bb8a9017-1e36-5d6c-6f2b-551abe8a76a2",
    "name": "RFTemplate 1"
  }
]
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1InstallerOrgsRftemplates401ErrorException`](../../doc/models/api-v1-installer-orgs-rftemplates-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1InstallerOrgsRftemplates403ErrorException`](../../doc/models/api-v1-installer-orgs-rftemplates-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1InstallerOrgsRftemplates404ErrorException`](../../doc/models/api-v1-installer-orgs-rftemplates-404-error-exception.md) |


# List Installer Sec Policies

Get List of Secuity Policies

```python
def list_installer_sec_policies(self,
                               org_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `org_id` | `uuid\|string` | Template, Required | - |

## Response Type

[`List of ApiV1InstallerOrgsSecpoliciesResponse`](../../doc/models/api-v1-installer-orgs-secpolicies-response.md)

## Example Usage

```python
org_id = '000000ab-00ab-00ab-00ab-0000000000ab'

result = installer_controller.list_installer_sec_policies(org_id)
print(result)
```

## Example Response *(as JSON)*

```json
[
  {
    "id": "3bcd0beb-5d0a-4cbd-92c1-14aea91e98ef",
    "name": "SecuPolicy 1"
  }
]
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1InstallerOrgsSecpolicies401ErrorException`](../../doc/models/api-v1-installer-orgs-secpolicies-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1InstallerOrgsSecpolicies403ErrorException`](../../doc/models/api-v1-installer-orgs-secpolicies-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1InstallerOrgsSecpolicies404ErrorException`](../../doc/models/api-v1-installer-orgs-secpolicies-404-error-exception.md) |


# List Installer Site Groups

Get List of Site Groups

```python
def list_installer_site_groups(self,
                              org_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `org_id` | `uuid\|string` | Template, Required | - |

## Response Type

[`List of ApiV1InstallerOrgsSitegroupsResponse`](../../doc/models/api-v1-installer-orgs-sitegroups-response.md)

## Example Usage

```python
org_id = '000000ab-00ab-00ab-00ab-0000000000ab'

result = installer_controller.list_installer_site_groups(org_id)
print(result)
```

## Example Response *(as JSON)*

```json
[
  {
    "id": "581328b6-e382-f54e-c9dc-999983183a34",
    "name": "SiteGroup 1"
  }
]
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1InstallerOrgsSitegroups401ErrorException`](../../doc/models/api-v1-installer-orgs-sitegroups-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1InstallerOrgsSitegroups403ErrorException`](../../doc/models/api-v1-installer-orgs-sitegroups-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1InstallerOrgsSitegroups404ErrorException`](../../doc/models/api-v1-installer-orgs-sitegroups-404-error-exception.md) |


# List Installer Sites

Get List of Sites

```python
def list_installer_sites(self,
                        org_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `org_id` | `uuid\|string` | Template, Required | - |

## Response Type

[`List of ApiV1InstallerOrgsSitesResponse`](../../doc/models/api-v1-installer-orgs-sites-response.md)

## Example Usage

```python
org_id = '000000ab-00ab-00ab-00ab-0000000000ab'

result = installer_controller.list_installer_sites(org_id)
print(result)
```

## Example Response *(as JSON)*

```json
[
  {
    "address": "1601 S. Deanza Blvd., Cupertino, CA, 95014",
    "country_code": "US",
    "id": "4ac1dcf4-9d8b-7211-65c4-057819f0862b",
    "latlng": {
      "lat": 37.295833,
      "lng": -122.032946
    },
    "name": "Mist Office",
    "timezone": "America/Los_Angeles"
  }
]
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1InstallerOrgsSites401ErrorException`](../../doc/models/api-v1-installer-orgs-sites-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1InstallerOrgsSites403ErrorException`](../../doc/models/api-v1-installer-orgs-sites-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1InstallerOrgsSites404ErrorException`](../../doc/models/api-v1-installer-orgs-sites-404-error-exception.md) |


# Create or Update Installer Sites

Often the Installers are asked to assign Devices to Sites. The Sites can either be pre-created or created/modified by the Installer. If this is an update, the same grace period also applies.

```python
def create_or_update_installer_sites(self,
                                    org_id,
                                    site_name,
                                    body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `org_id` | `uuid\|string` | Template, Required | - |
| `site_name` | `string` | Template, Required | - |
| `body` | [`Site`](../../doc/models/site.md) | Body, Optional | Request Body |

## Response Type

`object`

## Example Usage

```python
org_id = '000000ab-00ab-00ab-00ab-0000000000ab'

site_name = 'site_name8'

body = Site(
    name='string',
    address='1601 S. Deanza Blvd., Cupertino, CA, 95014',
    country_code='US',
    latlng=Latlng1(
        lat=37.295833,
        lng=-122.032946
    ),
    timezone='America/Los_Angeles'
)

result = installer_controller.create_or_update_installer_sites(
    org_id,
    site_name,
    body
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1InstallerOrgsSites401ErrorException`](../../doc/models/api-v1-installer-orgs-sites-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1InstallerOrgsSites403ErrorException`](../../doc/models/api-v1-installer-orgs-sites-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1InstallerOrgsSites404ErrorException`](../../doc/models/api-v1-installer-orgs-sites-404-error-exception.md) |


# List Installer Maps

Get List of Maps

```python
def list_installer_maps(self,
                       org_id,
                       site_name)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `org_id` | `uuid\|string` | Template, Required | - |
| `site_name` | `string` | Template, Required | - |

## Response Type

[`List of Map`](../../doc/models/map.md)

## Example Usage

```python
org_id = '000000ab-00ab-00ab-00ab-0000000000ab'

site_name = 'site_name8'

result = installer_controller.list_installer_maps(
    org_id,
    site_name
)
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
| 401 | Unauthorized | [`ApiV1InstallerOrgsSitesMaps401ErrorException`](../../doc/models/api-v1-installer-orgs-sites-maps-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1InstallerOrgsSitesMaps403ErrorException`](../../doc/models/api-v1-installer-orgs-sites-maps-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1InstallerOrgsSitesMaps404ErrorException`](../../doc/models/api-v1-installer-orgs-sites-maps-404-error-exception.md) |


# Import Installer Map

Import data from files is a multipart POST which has an file, an optional json, and an optional csv, to create floorplan, assign & place ap if name or mac matches

```python
def import_installer_map(self,
                        org_id,
                        site_name,
                        csv=None,
                        file=None,
                        json=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `org_id` | `uuid\|string` | Template, Required | - |
| `site_name` | `string` | Template, Required | - |
| `csv` | `string` | Form, Optional | - |
| `file` | `string` | Form, Optional | - |
| `json` | [`Json`](../../doc/models/json.md) | Form, Optional | - |

## Response Type

[`MapImport`](../../doc/models/map-import.md)

## Example Usage

```python
org_id = '000000ab-00ab-00ab-00ab-0000000000ab'

site_name = 'site_name8'

json = Json(
    vendor_name=VendorNameEnum.IBWAVE,
    import_all_floorplans=False,
    import_height=False,
    import_orientation=False
)

result = installer_controller.import_installer_map(
    org_id,
    site_name,
    json
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "aps": [
    {
      "action": "assigned-placed",
      "floorplan_id": "6f4bf402-45f9-2a56-6c8b-7f83d3bc98e9",
      "height": 3,
      "mac": "5c5b35000001",
      "map_id": "845a23bf-bed9-e43c-4c86-6fa474be7ae5",
      "orientation": 45
    }
  ],
  "floorplans": [
    {
      "action": "imported",
      "id": "cbdb7f0b-3be0-4872-88f9-58790b509c23",
      "map_id": "845a23bf-bed9-e43c-4c86-6fa474be7ae5",
      "name": "map1"
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
| 401 | Unauthorized | [`ApiV1InstallerOrgsSitesMapsImport401ErrorException`](../../doc/models/api-v1-installer-orgs-sites-maps-import-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1InstallerOrgsSitesMapsImport403ErrorException`](../../doc/models/api-v1-installer-orgs-sites-maps-import-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1InstallerOrgsSitesMapsImport404ErrorException`](../../doc/models/api-v1-installer-orgs-sites-maps-import-404-error-exception.md) |


# Delete Installer Map

Delete Map

```python
def delete_installer_map(self,
                        org_id,
                        site_name,
                        map_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `org_id` | `uuid\|string` | Template, Required | - |
| `site_name` | `string` | Template, Required | - |
| `map_id` | `uuid\|string` | Template, Required | - |

## Response Type

`object`

## Example Usage

```python
org_id = '000000ab-00ab-00ab-00ab-0000000000ab'

site_name = 'site_name8'

map_id = '000000ab-00ab-00ab-00ab-0000000000ab'

result = installer_controller.delete_installer_map(
    org_id,
    site_name,
    map_id
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1InstallerOrgsSitesMapsMapId401ErrorException`](../../doc/models/api-v1-installer-orgs-sites-maps-map-id-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1InstallerOrgsSitesMapsMapId403ErrorException`](../../doc/models/api-v1-installer-orgs-sites-maps-map-id-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1InstallerOrgsSitesMapsMapId404ErrorException`](../../doc/models/api-v1-installer-orgs-sites-maps-map-id-404-error-exception.md) |


# Create Installer Map

Create a MAP

```python
def create_installer_map(self,
                        org_id,
                        site_name,
                        map_id,
                        body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `org_id` | `uuid\|string` | Template, Required | - |
| `site_name` | `string` | Template, Required | - |
| `map_id` | `uuid\|string` | Template, Required | - |
| `body` | [`Map`](../../doc/models/map.md) | Body, Optional | Request Body |

## Response Type

[`Map`](../../doc/models/map.md)

## Example Usage

```python
org_id = '000000ab-00ab-00ab-00ab-0000000000ab'

site_name = 'site_name8'

map_id = '000000ab-00ab-00ab-00ab-0000000000ab'

body = Map(
    flags={},
    height=0,
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
    width=0
)

result = installer_controller.create_installer_map(
    org_id,
    site_name,
    map_id,
    body
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1InstallerOrgsSitesMapsMapId401ErrorException`](../../doc/models/api-v1-installer-orgs-sites-maps-map-id-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1InstallerOrgsSitesMapsMapId403ErrorException`](../../doc/models/api-v1-installer-orgs-sites-maps-map-id-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1InstallerOrgsSitesMapsMapId404ErrorException`](../../doc/models/api-v1-installer-orgs-sites-maps-map-id-404-error-exception.md) |


# Update Installer Map

Update map

```python
def update_installer_map(self,
                        org_id,
                        site_name,
                        map_id,
                        body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `org_id` | `uuid\|string` | Template, Required | - |
| `site_name` | `string` | Template, Required | - |
| `map_id` | `uuid\|string` | Template, Required | - |
| `body` | [`Map`](../../doc/models/map.md) | Body, Optional | Request Body |

## Response Type

[`Map`](../../doc/models/map.md)

## Example Usage

```python
org_id = '000000ab-00ab-00ab-00ab-0000000000ab'

site_name = 'site_name8'

map_id = '000000ab-00ab-00ab-00ab-0000000000ab'

body = Map(
    locked=False,
    orientation=0,
    mtype=Type30Enum.IMAGE,
    use_auto_orientation=False,
    use_auto_placement=False
)

result = installer_controller.update_installer_map(
    org_id,
    site_name,
    map_id,
    body
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1InstallerOrgsSitesMapsMapId401ErrorException`](../../doc/models/api-v1-installer-orgs-sites-maps-map-id-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1InstallerOrgsSitesMapsMapId403ErrorException`](../../doc/models/api-v1-installer-orgs-sites-maps-map-id-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1InstallerOrgsSitesMapsMapId404ErrorException`](../../doc/models/api-v1-installer-orgs-sites-maps-map-id-404-error-exception.md) |


# Optimize Installer Rrm

After installation is considered complete (APs are placed on maps, all powered up), you can trigger an optimize operation where RRM will kick in (and maybe other things in the future) before it’s automatically scheduled.

```python
def optimize_installer_rrm(self,
                          site_name)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_name` | `string` | Template, Required | - |

## Response Type

`object`

## Example Usage

```python
site_name = 'site_name8'

result = installer_controller.optimize_installer_rrm(site_name)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1InstallerSitesOptimize401ErrorException`](../../doc/models/api-v1-installer-sites-optimize-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1InstallerSitesOptimize403ErrorException`](../../doc/models/api-v1-installer-sites-optimize-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1InstallerSitesOptimize404ErrorException`](../../doc/models/api-v1-installer-sites-optimize-404-error-exception.md) |

