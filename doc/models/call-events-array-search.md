
# Call Events Array Search

## Structure

`CallEventsArraySearch`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `end` | `int` | Optional | - |
| `limit` | `int` | Optional | - |
| `results` | [`List of EventCall`](../../doc/models/event-call.md) | Optional | - |
| `start` | `int` | Optional | - |
| `total` | `int` | Optional | - |

## Example (as JSON)

```json
{
  "end": 254,
  "limit": 172,
  "results": [
    {
      "app": "app9",
      "audio_quality": "audio_quality5",
      "meeting_id": "meeting_id9",
      "org_id": "org_id9",
      "reason": "reason1"
    }
  ],
  "start": 212,
  "total": 10
}
```

