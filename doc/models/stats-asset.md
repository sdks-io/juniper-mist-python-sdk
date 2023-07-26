
# Stats Asset

Asset statistics

## Structure

`StatsAsset`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `battery_voltage` | `float` | Optional | battery voltage, in mV |
| `eddystone_uid_instance` | `string` | Optional | - |
| `eddystone_uid_namespace` | `string` | Optional | - |
| `eddystone_url_url` | `string` | Optional | - |
| `ibeacon_major` | `int` | Optional | - |
| `ibeacon_minor` | `int` | Optional | - |
| `ibeacon_uuid` | `uuid\|string` | Optional | - |
| `last_seen` | `float` | Optional | last seen timestamp |
| `mac` | `string` | Required | bluetooth MAC |
| `map_id` | `uuid\|string` | Optional | map where the device belongs to |
| `name` | `string` | Optional | name / label of the device |
| `rssizones` | [`List of Rssizone1`](../../doc/models/rssizone-1.md) | Optional | only send this for individual asset stat |
| `x` | `float` | Optional | x in pixel |
| `y` | `float` | Optional | y in pixel |
| `zones` | [`List of Zone4`](../../doc/models/zone-4.md) | Optional | only send this for individual asset stat |

## Example (as JSON)

```json
{
  "battery_voltage": 214.26,
  "eddystone_uid_instance": "eddystone_uid_instance4",
  "eddystone_uid_namespace": "eddystone_uid_namespace4",
  "eddystone_url_url": "eddystone_url_url4",
  "ibeacon_major": 222,
  "mac": "mac4"
}
```

