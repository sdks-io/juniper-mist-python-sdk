
# Rrm Events

## Structure

`RrmEvents`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `end` | `int` | Required | - |
| `limit` | `int` | Required | - |
| `next` | `string` | Optional | the link to query next set of results. value is null if no next page exists. |
| `results` | [`List of Result23`](../../doc/models/result-23.md) | Required | **Constraints**: *Minimum Items*: `1`, *Unique Items Required* |
| `start` | `int` | Required | - |

## Example (as JSON)

```json
{
  "end": 254,
  "limit": 172,
  "results": [
    {
      "ap_id": "000001ef-0000-0000-0000-000000000000",
      "band": "6",
      "bandwidth": 40,
      "channel": 203,
      "event": "neighbor-ap-recovered",
      "power": 143,
      "pre_bandwidth": 0,
      "pre_channel": 247,
      "pre_power": 157.93,
      "pre_usage": "pre_usage9",
      "timestamp": 63.09,
      "usage": "usage1"
    }
  ],
  "start": 212,
  "next": "next2"
}
```

