
# Auto Preemption

schedule to preempt ap’s which are not connected to preferred peer

## Structure

`AutoPreemption`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `day_of_week` | [`DayOfWeekEnum`](../../doc/models/day-of-week-enum.md) | Optional | - |
| `enabled` | `bool` | Optional | whether auto preemption should happen<br>**Default**: `False` |
| `time_of_day` | `string` | Optional | any / HH:MM (24-hour format)<br>**Default**: `'any'` |

## Example (as JSON)

```json
{
  "enabled": false,
  "time_of_day": "any",
  "day_of_week": "any"
}
```

