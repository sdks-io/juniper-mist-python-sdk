
# Anomaly Metrics

## Structure

`AnomalyMetrics`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `end` | `int` | Required | - |
| `limit` | `int` | Required | - |
| `page` | `int` | Required | - |
| `results` | [`List of Anomaly`](../../doc/models/anomaly.md) | Required | **Constraints**: *Minimum Items*: `1`, *Unique Items Required* |
| `start` | `int` | Required | - |

## Example (as JSON)

```json
{
  "end": 254,
  "limit": 172,
  "page": 30,
  "results": [
    {
      "events": [
        {
          "key1": "val1",
          "key2": "val2"
        }
      ],
      "since": 67.33,
      "sle_baseline": 42.81,
      "sle_deviation": 42.73,
      "timestamp": 63.09
    }
  ],
  "start": 212
}
```

