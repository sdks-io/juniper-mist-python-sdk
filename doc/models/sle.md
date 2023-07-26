
# Sle

## Structure

`Sle`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `interval` | `float` | Required | - |
| `name` | `string` | Required | **Constraints**: *Minimum Length*: `1` |
| `samples` | [`Samples2`](../../doc/models/samples-2.md) | Required | - |
| `x_label` | `string` | Required | **Constraints**: *Minimum Length*: `1` |
| `y_label` | `string` | Required | **Constraints**: *Minimum Length*: `1` |

## Example (as JSON)

```json
{
  "interval": 154.52,
  "name": "name0",
  "samples": {
    "degraded": [
      183.49
    ],
    "total": [
      158.41
    ],
    "value": [
      26.92,
      26.93,
      26.94
    ]
  },
  "x_label": "x_label4",
  "y_label": "y_label8"
}
```

