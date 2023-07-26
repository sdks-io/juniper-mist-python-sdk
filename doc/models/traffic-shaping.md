
# Traffic Shaping

## Structure

`TrafficShaping`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `class_percentages` | `List of int` | Optional | percentages for differet class of traffic: high / medium / low / best-effort<br>sum must be equal to 100 |
| `enabled` | `bool` | Optional | **Default**: `False` |

## Example (as JSON)

```json
{
  "enabled": false,
  "class_percentages": [
    251
  ]
}
```

