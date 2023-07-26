
# Json 2

## Structure

`Json2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `transform` | [`Transform`](../../doc/models/transform.md) | Optional | If `transform` is provided, all the locations of the objects on the map (AP, Zone, Vbeacon, Beacon) will be transformed as well (relative to the new Map) |

## Example (as JSON)

```json
{
  "transform": {
    "rotate": 141.94,
    "scale": 195.12,
    "x": 28.38,
    "y": 102.9
  }
}
```

