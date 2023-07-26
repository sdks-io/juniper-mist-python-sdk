
# Api V1 Sites Maps Auto Placement Response

## Structure

`ApiV1SitesMapsAutoPlacementResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `end_time` | `float` | Optional | time when autoplacement completed or was manually stopped |
| `estimated_time_left` | `float` | Optional | estimate of the time to completion |
| `start_time` | `float` | Optional | time when autoplacement process was last queued for this map |
| `status` | [`Status8Enum`](../../doc/models/status-8-enum.md) | Optional | the status of autoplacement for a given map |

## Example (as JSON)

```json
{
  "end_time": 221.12,
  "estimated_time_left": 241.76,
  "start_time": 195.76,
  "status": "pending"
}
```

