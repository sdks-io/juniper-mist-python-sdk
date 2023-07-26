
# Aps 2

## Structure

`Aps2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `action` | [`Action8Enum`](../../doc/models/action-8-enum.md) | Required | - |
| `floorplan_id` | `uuid\|string` | Required | - |
| `height` | `float` | Optional | - |
| `mac` | `string` | Required | - |
| `map_id` | `uuid\|string` | Required | - |
| `orientation` | `float` | Required | - |
| `reason` | `string` | Optional | - |

## Example (as JSON)

```json
{
  "action": "named-placed",
  "floorplan_id": "00001954-0000-0000-0000-000000000000",
  "height": 18.96,
  "mac": "mac4",
  "map_id": "000006bc-0000-0000-0000-000000000000",
  "orientation": 117.0,
  "reason": "reason4"
}
```

