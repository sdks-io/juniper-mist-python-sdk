
# Ml Events

## Structure

`MlEvents`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `end` | `int` | Required | - |
| `interval` | `int` | Required | - |
| `start` | `int` | Required | - |
| `updates` | [`List of Update`](../../doc/models/update.md) | Required | **Constraints**: *Minimum Items*: `1`, *Unique Items Required* |

## Example (as JSON)

```json
{
  "end": 254,
  "interval": 92,
  "start": 212,
  "updates": [
    {
      "client_type": "client_type6",
      "completed": 60.84,
      "int": 195.56,
      "level": 10.26,
      "ple": 191.32,
      "timestamp": 251.18
    }
  ]
}
```

