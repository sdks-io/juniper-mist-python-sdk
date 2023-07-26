
# Ap Iot Output

IoT output AP settings

## Structure

`ApIotOutput`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `enabled` | `bool` | Optional | whether to enable a pin<br>**Default**: `False` |
| `name` | `string` | Optional | optional; descriptive pin name |
| `output` | `bool` | Optional | whether the pin is configured as an output. DO and A1-A4 can be repurposed by changing |
| `pullup` | [`PullupEnum`](../../doc/models/pullup-enum.md) | Optional | the type of pull-up the pin uses (internal, external, none), default none |
| `value` | `int` | Optional | output pin signal level, default 0 |

## Example (as JSON)

```json
{
  "enabled": false,
  "name": "name0",
  "output": false,
  "pullup": "internal",
  "value": 64
}
```

