
# Call Stats Array

## Structure

`CallStatsArray`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `end` | `float` | Optional | - |
| `limit` | `int` | Optional | - |
| `next` | `string` | Optional | - |
| `results` | [`List of StatsCall`](../../doc/models/stats-call.md) | Optional | - |
| `start` | `float` | Optional | - |
| `total` | `int` | Optional | - |

## Example (as JSON)

```json
{
  "end": 12.78,
  "limit": 172,
  "next": "next2",
  "results": [
    {
      "app": "app9",
      "audio_quality": 149,
      "end_time": 13,
      "mac": "mac7",
      "meeting_id": "meeting_id9"
    }
  ],
  "start": 224.84
}
```

