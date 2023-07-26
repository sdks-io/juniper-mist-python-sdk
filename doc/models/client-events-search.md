
# Client Events Search

## Structure

`ClientEventsSearch`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `end` | `int` | Required | - |
| `limit` | `int` | Required | - |
| `next` | `string` | Optional | - |
| `results` | [`List of EventsClient`](../../doc/models/events-client.md) | Required | **Constraints**: *Minimum Items*: `1`, *Unique Items Required* |
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
      "band": "5",
      "bssid": "bssid3",
      "channel": 203,
      "proto": "n",
      "ssid": "ssid9",
      "text": "text7",
      "timestamp": 63.09
    }
  ],
  "start": 212,
  "total": 10,
  "next": "next2"
}
```

