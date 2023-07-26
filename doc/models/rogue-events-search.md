
# Rogue Events Search

## Structure

`RogueEventsSearch`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `end` | `int` | Required | - |
| `limit` | `int` | Required | - |
| `next` | `string` | Optional | - |
| `results` | [`List of EventsRogue`](../../doc/models/events-rogue.md) | Required | **Constraints**: *Minimum Items*: `1`, *Unique Items Required* |
| `start` | `int` | Required | - |
| `total` | `int` | Required | - |

## Example (as JSON)

```json
{
  "end": 254,
  "limit": 172,
  "results": [
    {
      "ap": "ap1",
      "bssid": "bssid3",
      "channel": 203,
      "rssi": 151,
      "ssid": "ssid9",
      "timestamp": 63.09
    }
  ],
  "start": 212,
  "total": 10,
  "next": "next2"
}
```

