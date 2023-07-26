
# Insight Rogue

## Structure

`InsightRogue`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `end` | `int` | Required | - |
| `limit` | `int` | Required | - |
| `next` | `string` | Optional | link to next set of results. If more results aren’t present, next is null. |
| `results` | [`List of Result19`](../../doc/models/result-19.md) | Required | **Constraints**: *Minimum Items*: `0`, *Unique Items Required* |
| `start` | `int` | Required | - |

## Example (as JSON)

```json
{
  "end": 254,
  "limit": 172,
  "results": [
    {
      "ap_mac": "ap_mac5",
      "avg_rssi": 236.57,
      "bssid": "bssid3",
      "channel": "channel1",
      "delta_x": 91.47,
      "delta_y": 243.39,
      "num_aps": 57,
      "seen_on_lan": true,
      "ssid": "ssid9",
      "times_heard": 193
    }
  ],
  "start": 212,
  "next": "next2"
}
```

