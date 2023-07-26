
# Anomaly

Anomaly

## Structure

`Anomaly`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `events` | `List of object` | Required | - |
| `since` | `float` | Optional | - |
| `sle_baseline` | `float` | Required | - |
| `sle_deviation` | `float` | Required | - |
| `timestamp` | `float` | Required | - |

## Example (as JSON)

```json
{
  "events": [
    {
      "key1": "val1",
      "key2": "val2"
    }
  ],
  "since": 1.6,
  "sle_baseline": 233.08,
  "sle_deviation": 108.46,
  "timestamp": 128.82
}
```

