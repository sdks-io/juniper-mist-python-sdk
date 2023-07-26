
# Ap Iot Input

IoT Input AP settings

## Structure

`ApIotInput`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `enabled` | `bool` | Optional | whether to enable a pin<br>**Default**: `False` |
| `name` | `string` | Optional | optional; descriptive pin name |
| `pullup` | [`PullupEnum`](../../doc/models/pullup-enum.md) | Optional | the type of pull-up the pin uses (internal, external, none), default none |

## Example (as JSON)

```json
{
  "enabled": false,
  "name": "name0",
  "pullup": "internal"
}
```

