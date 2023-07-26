
# Assets Waits

ble asset wait time right now

## Structure

`AssetsWaits`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `avg` | `float` | Optional | average wait time in seconds |
| `max` | `float` | Optional | longest wait time in seconds |
| `min` | `float` | Optional | shortest wait time in seconds |
| `p_95` | `float` | Optional | 95th percentile of all the wait time(s) |

## Example (as JSON)

```json
{
  "avg": 178.62,
  "max": 9.3,
  "min": 82.72,
  "p95": 111.2
}
```

