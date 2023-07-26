
# Sle Summary

## Structure

`SleSummary`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `classifiers` | [`List of Classifier1`](../../doc/models/classifier-1.md) | Required | **Constraints**: *Minimum Items*: `1`, *Unique Items Required* |
| `end` | `float` | Required | - |
| `events` | `List of object` | Required | - |
| `impact` | [`Impact1`](../../doc/models/impact-1.md) | Required | - |
| `sle` | [`Sle`](../../doc/models/sle.md) | Required | - |
| `start` | `float` | Required | - |

## Example (as JSON)

```json
{
  "classifiers": [
    {
      "impact": {
        "num_aps": 192.61,
        "num_users": 62.47,
        "total_aps": 45.75,
        "total_users": 202.23
      },
      "interval": 159.39,
      "name": "name1",
      "samples": {
        "degraded": [
          174.12
        ],
        "duration": [
          239.71,
          239.72,
          239.73
        ],
        "total": [
          88.22
        ]
      },
      "x_label": "x_label3",
      "y_label": "y_label9"
    }
  ],
  "end": 12.78,
  "events": [
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
  "sle": {
    "interval": 227.76,
    "name": "name8",
    "samples": {
      "degraded": [
        242.49,
        242.5
      ],
      "total": [
        28.49,
        28.5
      ],
      "value": [
        85.92
      ]
    },
    "x_label": "x_label4",
    "y_label": "y_label6"
  },
  "start": 224.84
}
```

