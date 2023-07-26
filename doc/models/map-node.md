
# Map Node

Nodes on maps

## Structure

`MapNode`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `edges` | `dict` | Optional | - |
| `name` | `string` | Required | - |
| `position` | [`Position`](../../doc/models/position.md) | Optional | - |

## Example (as JSON)

```json
{
  "edges": {
    "key0": "edges2",
    "key1": "edges3",
    "key2": "edges4"
  },
  "name": "name0",
  "position": {
    "x": 224.72,
    "y": 100.0
  }
}
```

