
# Installer Devices

## Structure

`InstallerDevices`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `deviceprofile_name` | `string` | Optional | - |
| `for_site` | `bool` | Optional | - |
| `height` | `float` | Optional | - |
| `map_id` | `uuid\|string` | Optional | - |
| `name` | `string` | Required | - |
| `orientation` | `float` | Optional | - |
| `replacing_mac` | `string` | Optional | Onlif this is to replace an existing device |
| `role` | `string` | Optional | optional role for switch / gateway |
| `site_id` | `uuid\|string` | Optional | - |
| `site_name` | `string` | Optional | - |
| `x` | `float` | Optional | - |
| `y` | `float` | Optional | - |

## Example (as JSON)

```json
{
  "deviceprofile_name": "deviceprofile_name6",
  "for_site": false,
  "height": 18.96,
  "map_id": "000006bc-0000-0000-0000-000000000000",
  "name": "name0",
  "orientation": 117.0
}
```

