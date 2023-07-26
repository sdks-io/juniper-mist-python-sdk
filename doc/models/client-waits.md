
# Client Waits

client wait time right now

## Structure

`ClientWaits`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `avg` | `int` | Required | average wait time in seconds |
| `max` | `int` | Required | longest wait time in seconds |
| `min` | `int` | Required | shortest wait time in seconds |
| `p_95` | `int` | Required | 95th percentile of all the wait time(s) |

## Example (as JSON)

```json
{
  "avg": 198,
  "max": 162,
  "min": 80,
  "p95": 112
}
```

