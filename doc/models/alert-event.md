
# Alert Event

## Structure

`AlertEvent`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `current_occupancy` | `int` | Required | - |
| `map_id` | `uuid\|string` | Required | - |
| `occupancy_limit` | `int` | Required | - |
| `org_id` | `uuid\|string` | Required | - |
| `timestamp` | `float` | Required | - |
| `mtype` | [`Type42Enum`](../../doc/models/type-42-enum.md) | Required | event type (COMPLIANCE-VIOLATION / COMPLIANCE-OK) |
| `zone_id` | `uuid\|string` | Required | - |
| `zone_name` | `string` | Required | - |

## Example (as JSON)

```json
{
  "current_occupancy": 88,
  "map_id": "000006bc-0000-0000-0000-000000000000",
  "occupancy_limit": 236,
  "org_id": "00000ec8-0000-0000-0000-000000000000",
  "timestamp": 128.82,
  "type": "COMPLIANCE-VIOLATION",
  "zone_id": "000019ec-0000-0000-0000-000000000000",
  "zone_name": "zone_name0"
}
```

