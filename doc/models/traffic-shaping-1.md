
# Traffic Shaping 1

## Structure

`TrafficShaping1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `class_percentage` | `List of int` | Optional | percentages for differet class of traffic: high / medium / low / best-effort<br>sum must be equal to 100 |
| `enabled` | `bool` | Optional | - |
| `max_tx_kbps` | `int` | Optional | - |

## Example (as JSON)

```json
{
  "class_percentage": [
    241,
    242,
    243
  ],
  "enabled": false,
  "max_tx_kbps": 54
}
```

