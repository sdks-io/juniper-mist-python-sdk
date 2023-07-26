
# Insight Metric

## Structure

`InsightMetric`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `end` | `int` | Required | - |
| `interval` | `int` | Required | - |
| `results` | `List of object` | Required | results depends on the `metric`<br>**Constraints**: *Minimum Items*: `1`, *Unique Items Required* |
| `start` | `int` | Required | - |

## Example (as JSON)

```json
{
  "end": 254,
  "interval": 92,
  "results": [
    {
      "key1": "val1",
      "key2": "val2"
    }
  ],
  "start": 212
}
```

