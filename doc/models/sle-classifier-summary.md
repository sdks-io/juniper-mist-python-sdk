
# Sle Classifier Summary

## Structure

`SleClassifierSummary`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `classifier` | [`Classifier`](../../doc/models/classifier.md) | Required | - |
| `end` | `float` | Required | - |
| `failures` | `List of object` | Required | - |
| `impact` | [`Impact1`](../../doc/models/impact-1.md) | Required | - |
| `metric` | `string` | Required | **Constraints**: *Minimum Length*: `1` |
| `start` | `float` | Required | - |

## Example (as JSON)

```json
{
  "classifier": {
    "impact": {
      "num_aps": 71.48,
      "num_users": 183.6
    },
    "interval": 24.52,
    "name": "name4",
    "samples": {
      "degraded": [
        39.25,
        39.26
      ],
      "duration": [
        104.84
      ],
      "total": [
        46.65,
        46.66,
        46.67
      ]
    },
    "x_label": "x_label0",
    "y_label": "y_label2"
  },
  "end": 12.78,
  "failures": [
    {
      "key1": "val1",
      "key2": "val2"
    },
    {
      "key1": "val1",
      "key2": "val2"
    },
    {
      "key1": "val1",
      "key2": "val2"
    }
  ],
  "impact": {
    "num_aps": 250.52,
    "num_users": 4.56,
    "total_aps": 243.84,
    "total_users": 4.14
  },
  "metric": "metric8",
  "start": 224.84
}
```

