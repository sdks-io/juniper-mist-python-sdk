
# Beacon

Beacon

## Structure

`Beacon`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `created_time` | `float` | Optional | - |
| `eddystone_instance` | `string` | Optional | Eddystone-UID instance (6 bytes) in hexstring format |
| `eddystone_namespace` | `string` | Optional | Eddystone-UID namespace (10 bytes) in hexstring format |
| `eddystone_url` | `string` | Optional | Eddystone-URL url |
| `for_site` | `bool` | Optional | - |
| `ibeacon_major` | `int` | Optional | bluetooth tag major |
| `ibeacon_minor` | `int` | Optional | bluetooth tag minor |
| `ibeacon_uuid` | `uuid\|string` | Optional | bluetooth tag UUID |
| `id` | `uuid\|string` | Optional | - |
| `mac` | `string` | Optional | optiona, MAC of the beacon, currently used only to identify battery voltage |
| `map_id` | `uuid\|string` | Optional | map where the device belongs to |
| `modified_time` | `float` | Optional | - |
| `name` | `string` | Optional | name / label of the device |
| `org_id` | `uuid\|string` | Optional | - |
| `power` | `int` | Optional | in dBm<br>**Default**: `-12`<br>**Constraints**: `>= -12`, `<= 100` |
| `site_id` | `uuid\|string` | Optional | - |
| `mtype` | [`Type4Enum`](../../doc/models/type-4-enum.md) | Optional | **Default**: `'eddystone-uid'` |
| `x` | `float` | Optional | x in pixel |
| `y` | `float` | Optional | y in pixel |

## Example (as JSON)

```json
{
  "power": -12,
  "type": "eddystone-uid",
  "created_time": 198.3,
  "eddystone_instance": "eddystone_instance8",
  "eddystone_namespace": "eddystone_namespace4",
  "eddystone_url": "eddystone_url2",
  "for_site": false
}
```

