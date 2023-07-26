
# Stats Beacon

## Structure

`StatsBeacon`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `battery_voltage` | `float` | Optional | battery voltage, in mV |
| `eddystone_instance` | `string` | Optional | - |
| `eddystone_namespace` | `string` | Optional | - |
| `last_seen` | `float` | Required | - |
| `mac` | `string` | Required | - |
| `map_id` | `uuid\|string` | Required | - |
| `name` | `string` | Required | - |
| `power` | `int` | Required | - |
| `mtype` | `string` | Required | - |
| `x` | `float` | Required | - |
| `y` | `float` | Required | - |

## Example (as JSON)

```json
{
  "battery_voltage": 214.26,
  "eddystone_instance": "eddystone_instance8",
  "eddystone_namespace": "eddystone_namespace4",
  "last_seen": 33.7,
  "mac": "mac4",
  "map_id": "000006bc-0000-0000-0000-000000000000",
  "name": "name0",
  "power": 60,
  "type": "type0",
  "x": 222.14,
  "y": 165.14
}
```

