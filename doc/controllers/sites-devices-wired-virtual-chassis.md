# Sites Devices-Wired Virtual Chassis

```python
sites_devices_wired_virtual_chassis_controller = client.sites_devices_wired_virtual_chassis
```

## Class Name

`SitesDevicesWiredVirtualChassisController`

## Methods

* [Delete Site Virtual Chassis](../../doc/controllers/sites-devices-wired-virtual-chassis.md#delete-site-virtual-chassis)
* [Get Site Device Virtual Chassis](../../doc/controllers/sites-devices-wired-virtual-chassis.md#get-site-device-virtual-chassis)
* [Create Site Virtual Chassis](../../doc/controllers/sites-devices-wired-virtual-chassis.md#create-site-virtual-chassis)
* [Update Site Virtual Chassis Member](../../doc/controllers/sites-devices-wired-virtual-chassis.md#update-site-virtual-chassis-member)
* [Set Site Vc Port](../../doc/controllers/sites-devices-wired-virtual-chassis.md#set-site-vc-port)


# Delete Site Virtual Chassis

When all the member switches of VC are removed and only member ID 0 is left, the cloud would detect this situation and automatically changes the single switch to non-VC role.

For some unexpected cases that the VC is gone and disconncted, the API below could be used to change the state of VC’s switches to be standalone. After it is executed, all the switches will be shown as standalone switches under Inventory.

```python
def delete_site_virtual_chassis(self,
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

result = sites_devices_wired_virtual_chassis_controller.delete_site_virtual_chassis(
    site_id,
    device_id
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesDevicesVc401ErrorException`](../../doc/models/api-v1-sites-devices-vc-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesDevicesVc403ErrorException`](../../doc/models/api-v1-sites-devices-vc-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesDevicesVc404ErrorException`](../../doc/models/api-v1-sites-devices-vc-404-error-exception.md) |


# Get Site Device Virtual Chassis

Get VC Status

The API returns a combined view of the VC status which includes topology and stats_

```python
def get_site_device_virtual_chassis(self,
                                   site_id,
                                   device_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `device_id` | `uuid\|string` | Template, Required | - |

## Response Type

[`Vc`](../../doc/models/vc.md)

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

device_id = '000000ab-00ab-00ab-00ab-0000000000ab'

result = sites_devices_wired_virtual_chassis_controller.get_site_device_virtual_chassis(
    site_id,
    device_id
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "id": {
    "members": [
      {
        "mac": "string",
        "member": 0,
        "vc_ports": [
          "string"
        ],
        "vc_role": "master"
      }
    ],
    "op": "add"
  }
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesDevicesVc401ErrorException`](../../doc/models/api-v1-sites-devices-vc-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesDevicesVc403ErrorException`](../../doc/models/api-v1-sites-devices-vc-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesDevicesVc404ErrorException`](../../doc/models/api-v1-sites-devices-vc-404-error-exception.md) |


# Create Site Virtual Chassis

For models (e.g. EX3400 and up) having dedicated VC ports, it is easier to form a VC by just connecting cables with the dedicated VC ports. Cloud will detect the new VC and update the inventory.

In case that the user would like to choose the dedicated switch as a VC master. Or for EX2300-C-12P and EX2300-C-12T which doesn’t have dedicated VC ports, below are procedures to automate the VC creation:

1. Power on the switch that is choosen as the VC master first. And the powering on the other member switches.
2. Claim or adopt all these switches under the same organization’s Inventory
3. Assign these switches into the same Site
4. Invoke vc command on the switch choosen to be the VC master. For EX2300-C-12P, VC ports will be created automatically.
5. Connect the cables to the VC ports for these switches
6. Wait for the VC to be formed. The Org’s inventory will be updated for the new VC.

```python
def create_site_virtual_chassis(self,
                               site_id,
                               device_id,
                               body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `device_id` | `uuid\|string` | Template, Required | - |
| `body` | [`DeviceSwitchVc`](../../doc/models/device-switch-vc.md) | Body, Optional | Request Body |

## Response Type

[`Vc`](../../doc/models/vc.md)

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

device_id = '000000ab-00ab-00ab-00ab-0000000000ab'

body = DeviceSwitchVc(
    members=[
        Member1(
            mac='aff827549235',
            vc_ports=[
                'xe-0/1/0'
            ]
        ),
        Member1(
            mac='8396cd006c8c',
            vc_ports=[
                'xe-0/1/0',
                'xe-0/1/1'
            ]
        ),
        Member1(
            mac='8396cd00888c',
            vc_ports=[
                'xe-0/1/0'
            ]
        )
    ]
)

result = sites_devices_wired_virtual_chassis_controller.create_site_virtual_chassis(
    site_id,
    device_id,
    body
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "id": {
    "members": [
      {
        "mac": "string",
        "member": 0,
        "vc_ports": [
          "string"
        ],
        "vc_role": "master"
      }
    ],
    "op": "add"
  }
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesDevicesVc401ErrorException`](../../doc/models/api-v1-sites-devices-vc-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesDevicesVc403ErrorException`](../../doc/models/api-v1-sites-devices-vc-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesDevicesVc404ErrorException`](../../doc/models/api-v1-sites-devices-vc-404-error-exception.md) |


# Update Site Virtual Chassis Member

The VC creation and adding member switch API will update the device’s virtual chassis config which is applied after VC is formed to create JUNOS pre-provisioned virtual chassis configuration.

## Change to use preprovisioned VC

To switch the VC to use preprovisioned VC, enable preprovisioned in virtual_chassis config. Both vc_role master and backup will be matched to routing-engine role in Junos preprovisioned VC config.

In this config, fpc0 has to be the same as the mac of device_id. Use renumber if you want to replace fpc0 which involves device_id change.

Notice: to configure preprovisioned VC, every member of the VC must be in the inventory.

## Add new members

For models (e.g. EX4300 and up) having dedicated VC ports, it is easier to add new member switches into a VC by just connecting cables with the dedicated VC ports. Cloud will detect the new members and update the inventory.

For EX2300 VC, adding new members requires to follow the procedures below:

1. Powering on the new member switches and ensuring cables are not connected to any VC ports.
2. Claim or adopt all new member switches under the VC’s organization Inventory
3. Assign all new member switches to the same Site as the VC
4. Invoke vc command to add switches to the VC.
5. Connect the cables to the VC ports for these switches
6. After a while, the Org’s Inventory shows this new switches has been added into the VC.

## Removing member switch

To remove a member switch from the VC, following the procedures below:

1. Ensuring the VC is connected to the cloud first
2. Unplug the cable from the VC port of the switch
3. Waiting for the VC state (vc_state) of this switch is changed to not-present
4. Invoke update_vc with remove to remove this switch from the VC
5. The Org’s Inventory shows the switch is removed.

Please notice that member ID 0 (fpc0) cannot be removed. When a VC has two switches left, unpluging the cable may result in the situation that fpc0 becomes a line card (LC). When this situation is happened, please re-plug in the cable, wait for both switches becoming present (show virtual-chassis) and then removing the cable again.

## Renumber a member switch

When a member switch doesn’t work properly and needed to be replaced, the renumber API could be used. The following two types of renumber are supported:

1. Replace a non-fpc0 member switch
2. Replace fpc0. When fpc0 is relaced, PAPI device config and JUNOS config will be both updated.

For renumber to work, the following procedures are needed:

1. Ensuring the VC is connected to the cloud and the state of the member switch to be replaced must be non present.
2. Adding the new member switch to the VC
3. Waiting for the VC state (vc_state) of this VC to be updated to API server
4. Invoke vc with renumber to replace the new member switch from fpc X to

```python
def update_site_virtual_chassis_member(self,
                                      site_id,
                                      device_id,
                                      body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `device_id` | `uuid\|string` | Template, Required | - |
| `body` | [`DeviceSwitchVc`](../../doc/models/device-switch-vc.md) | Body, Optional | Request Body |

## Response Type

[`Vc`](../../doc/models/vc.md)

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

device_id = '000000ab-00ab-00ab-00ab-0000000000ab'

body = DeviceSwitchVc(
    members=[
        Member1(
            mac='aff827549235',
            member=0,
            vc_ports=[
                'xe-0/1/1'
            ]
        ),
        Member1(
            mac='aff827549235',
            member=2,
            vc_ports=[
                'xe-0/1/1'
            ]
        ),
        Member1(
            mac='8396cd00777c',
            vc_ports=[
                'xe-0/1/0'
            ]
        ),
        Member1(
            mac='8396cd00888c',
            vc_ports=[
                'xe-0/1/0'
            ]
        )
    ],
    op=OpEnum.ADD
)

result = sites_devices_wired_virtual_chassis_controller.update_site_virtual_chassis_member(
    site_id,
    device_id,
    body
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "id": {
    "members": [
      {
        "mac": "string",
        "member": 0,
        "vc_ports": [
          "string"
        ],
        "vc_role": "master"
      }
    ],
    "op": "add"
  }
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesDevicesVc401ErrorException`](../../doc/models/api-v1-sites-devices-vc-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesDevicesVc403ErrorException`](../../doc/models/api-v1-sites-devices-vc-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesDevicesVc404ErrorException`](../../doc/models/api-v1-sites-devices-vc-404-error-exception.md) |


# Set Site Vc Port

Set VC port

```python
def set_site_vc_port(self,
                    site_id,
                    device_id,
                    body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `uuid\|string` | Template, Required | - |
| `device_id` | `uuid\|string` | Template, Required | - |
| `body` | [`ApiV1SitesDevicesVcVcPortRequest`](../../doc/models/api-v1-sites-devices-vc-vc-port-request.md) | Body, Optional | - |

## Response Type

`object`

## Example Usage

```python
site_id = '000000ab-00ab-00ab-00ab-0000000000ab'

device_id = '000000ab-00ab-00ab-00ab-0000000000ab'

body = ApiV1SitesDevicesVcVcPortRequest(
    members=[
        Member2(
            member=0,
            vc_ports=[
                'xe-0/1/1'
            ]
        ),
        Member2(
            member=2,
            vc_ports=[
                'xe-0/1/1'
            ]
        )
    ],
    op=Op5Enum.DELETE
)

result = sites_devices_wired_virtual_chassis_controller.set_site_vc_port(
    site_id,
    device_id,
    body
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesDevicesVcVcPort401ErrorException`](../../doc/models/api-v1-sites-devices-vc-vc-port-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesDevicesVcVcPort403ErrorException`](../../doc/models/api-v1-sites-devices-vc-vc-port-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesDevicesVcVcPort404ErrorException`](../../doc/models/api-v1-sites-devices-vc-vc-port-404-error-exception.md) |

