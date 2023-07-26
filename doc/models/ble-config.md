
# Ble Config

## Structure

`BleConfig`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `beacon_rate` | `int` | Optional | - |
| `beacon_rate_model` | `string` | Optional | - |
| `beam_disabled` | `List of int` | Optional | - |
| `power` | `int` | Optional | - |
| `power_mode` | `string` | Optional | - |

## Example (as JSON)

```json
{
  "beacon_rate": 94,
  "beacon_rate_model": "beacon_rate_model4",
  "beam_disabled": [
    97,
    98
  ],
  "power": 60,
  "power_mode": "power_mode0"
}
```

