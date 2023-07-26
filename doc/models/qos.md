
# Qos

## Structure

`Qos`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `mclass` | [`ClassEnum`](../../doc/models/class-enum.md) | Optional | **Default**: `'best_effort'` |
| `overwrite` | `bool` | Optional | whether to overwrite QoS<br>**Default**: `False` |

## Example (as JSON)

```json
{
  "class": "best_effort",
  "overwrite": false
}
```

