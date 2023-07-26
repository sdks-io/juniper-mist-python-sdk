
# Events Interference

## Structure

`EventsInterference`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `end` | `int` | Required | - |
| `limit` | `int` | Required | - |
| `page` | `int` | Required | - |
| `results` | [`List of Result17`](../../doc/models/result-17.md) | Required | **Constraints**: *Minimum Items*: `1`, *Unique Items Required* |
| `start` | `int` | Required | - |
| `total` | `int` | Required | - |

## Example (as JSON)

```json
{
  "end": 254,
  "limit": 172,
  "page": 30,
  "results": [
    {
      "ap_id": "000001ef-0000-0000-0000-000000000000",
      "band": 91,
      "channel_util": 159.53,
      "channels": [
        158,
        159
      ],
      "rssi": 62.95,
      "source": "source1",
      "timestamp": 63.09
    }
  ],
  "start": 212,
  "total": 10
}
```

