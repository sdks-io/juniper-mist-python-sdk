
# Wayfinding Path

a JSON blob for wayfinding (using Dijkstra’s algorithm)

## Structure

`WayfindingPath`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `coordinate` | `string` | Optional | - |
| `nodes` | [`List of MapNode`](../../doc/models/map-node.md) | Optional | **Constraints**: *Minimum Items*: `0` |

## Example (as JSON)

```json
{
  "coordinate": "coordinate2",
  "nodes": [
    {
      "edges": {
        "key0": "edges2",
        "key1": "edges1",
        "key2": "edges0"
      },
      "name": "name4",
      "position": {
        "x": 136.06,
        "y": 11.34
      }
    },
    {
      "edges": {
        "key0": "edges3",
        "key1": "edges2"
      },
      "name": "name5",
      "position": {
        "x": 136.07,
        "y": 11.35
      }
    },
    {
      "edges": {
        "key0": "edges4"
      },
      "name": "name6",
      "position": {
        "x": 136.08,
        "y": 11.36
      }
    }
  ]
}
```

