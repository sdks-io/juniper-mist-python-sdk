
# Rrm Consideration

## Structure

`RrmConsideration`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `results` | [`List of Result22`](../../doc/models/result-22.md) | Required | **Constraints**: *Minimum Items*: `1`, *Unique Items Required* |

## Example (as JSON)

```json
{
  "results": [
    {
      "channel": 203,
      "noise": 110.07,
      "other_rssi": 223.63,
      "other_ssid": "other_ssid3",
      "util_score": 11.05,
      "util_score_non_wifi": 140.61,
      "util_score_other": 42.67
    }
  ]
}
```

