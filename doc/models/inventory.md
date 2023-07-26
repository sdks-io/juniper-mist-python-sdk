
# Inventory

## Structure

`Inventory`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `adopted` | `bool` | Optional | only if `type`==`switch` or `type`==`gateway`<br>whether the switch/gateway is adopted |
| `connected` | `bool` | Optional | whether the device is connected |
| `created_time` | `int` | Optional | inventory created time, in epoch |
| `deviceprofile_id` | `string` | Optional | deviceprofile id if assigned, null if not assigned |
| `hostname` | `string` | Optional | hostname reported by the device |
| `hw_rev` | `string` | Optional | device hardware revision number |
| `id` | `string` | Optional | device id |
| `jsi` | `bool` | Optional | - |
| `mac` | `string` | Optional | device MAC address |
| `magic` | `string` | Optional | device claim code |
| `model` | `string` | Optional | device model |
| `modified_time` | `int` | Optional | inventory last modified time, in epoch |
| `name` | `string` | Optional | device name if configured |
| `org_id` | `string` | Optional | org id |
| `serial` | `string` | Optional | device serial |
| `site_id` | `string` | Optional | site id if assigned, null if not assigned |
| `sku` | `string` | Optional | device stock keeping unit |
| `mtype` | [`Type23Enum`](../../doc/models/type-23-enum.md) | Optional | device type |

## Example (as JSON)

```json
{
  "adopted": false,
  "connected": false,
  "created_time": 118,
  "deviceprofile_id": "deviceprofile_id0",
  "hostname": "hostname4"
}
```

