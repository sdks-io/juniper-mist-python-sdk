
# Device Metric

## Structure

`DeviceMetric`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `end` | `int` | Required | - |
| `interval` | `int` | Required | - |
| `results` | `List of object` | Required | - |
| `rt` | `List of string` | Optional | - |
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
  "rt": [
    "rt6"
  ],
  "start": 212
}
```

