
# Aps 3

## Structure

`Aps3`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `action` | [`Action8Enum`](../../doc/models/action-8-enum.md) | Optional | **Constraints**: *Minimum Length*: `1` |
| `floorplan_id` | `string` | Optional | **Constraints**: *Minimum Length*: `1` |
| `height` | `float` | Optional | - |
| `mac` | `string` | Required | **Constraints**: *Minimum Length*: `1` |
| `map_id` | `string` | Optional | **Constraints**: *Minimum Length*: `1` |
| `orientation` | `float` | Optional | - |
| `reason` | `string` | Optional | **Constraints**: *Minimum Length*: `1` |

## Example (as JSON)

```json
{
  "action": "named-placed",
  "floorplan_id": "floorplan_id4",
  "height": 18.96,
  "mac": "mac4",
  "map_id": "map_id4",
  "orientation": 117.0
}
```

