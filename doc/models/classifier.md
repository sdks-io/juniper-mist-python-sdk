
# Classifier

## Structure

`Classifier`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `impact` | [`Impact`](../../doc/models/impact.md) | Required | - |
| `interval` | `float` | Required | - |
| `name` | `string` | Required | **Constraints**: *Minimum Length*: `1` |
| `samples` | [`Samples`](../../doc/models/samples.md) | Required | - |
| `x_label` | `string` | Required | **Constraints**: *Minimum Length*: `1` |
| `y_label` | `string` | Required | **Constraints**: *Minimum Length*: `1` |

## Example (as JSON)

```json
{
  "impact": {
    "num_aps": 250.52,
    "num_users": 4.56
  },
  "interval": 154.52,
  "name": "name0",
  "samples": {
    "degraded": [
      183.49
    ],
    "duration": [
      249.08,
      249.09,
      249.1
    ],
    "total": [
      158.41
    ]
  },
  "x_label": "x_label4",
  "y_label": "y_label8"
}
```

