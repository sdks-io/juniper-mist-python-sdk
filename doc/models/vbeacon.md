
# Vbeacon

vBeacon

## Structure

`Vbeacon`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `created_time` | `float` | Optional | - |
| `for_site` | `bool` | Optional | - |
| `id` | `uuid\|string` | Optional | - |
| `major` | `int` | Optional | bluetooth tag major |
| `map_id` | `uuid\|string` | Optional | map where the device belongs to |
| `message` | `string` | Optional | a message that can be displayed when the sdkclient gets near the vbeacon |
| `minor` | `int` | Optional | bluetooth tag minor |
| `modified_time` | `float` | Optional | - |
| `name` | `string` | Optional | name / label of the device |
| `org_id` | `uuid\|string` | Optional | - |
| `power` | `int` | Optional | required if `power_mode`==`custom`, -30 - 100, in dBm. For default power_mode, power = 4 dBm.<br>**Default**: `4`<br>**Constraints**: `>= -30`, `<= 100` |
| `power_mode` | [`PowerModeEnum`](../../doc/models/power-mode-enum.md) | Optional | default / custom<br>**Default**: `'default'` |
| `site_id` | `uuid\|string` | Optional | - |
| `url` | `string` | Optional | URL to show, optional |
| `uuid` | `uuid\|string` | Optional | bluetooth tag UUID |
| `wayfinding_nodename` | `string` | Optional | the name to be used in wayfinding_path or wayfinding_grid blob |
| `x` | `float` | Optional | x in pixel |
| `y` | `float` | Optional | y in pixel |

## Example (as JSON)

```json
{
  "power": 4,
  "power_mode": "default",
  "created_time": 198.3,
  "for_site": false,
  "id": "00001770-0000-0000-0000-000000000000",
  "major": 226,
  "map_id": "000006bc-0000-0000-0000-000000000000"
}
```

