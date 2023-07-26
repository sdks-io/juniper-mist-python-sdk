
# Sle Histogram

## Structure

`SleHistogram`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `data` | [`List of Datum`](../../doc/models/datum.md) | Required | **Constraints**: *Minimum Items*: `1`, *Unique Items Required* |
| `end` | `float` | Required | - |
| `metric` | `string` | Required | **Constraints**: *Minimum Length*: `1` |
| `start` | `float` | Required | - |
| `x_label` | `string` | Required | **Constraints**: *Minimum Length*: `1` |
| `y_label` | `string` | Required | **Constraints**: *Minimum Length*: `1` |

## Example (as JSON)

```json
{
  "data": [
    {
      "range": [
        57.08
      ],
      "value": 145.67
    }
  ],
  "end": 12.78,
  "metric": "metric8",
  "start": 224.84,
  "x_label": "x_label4",
  "y_label": "y_label8"
}
```

