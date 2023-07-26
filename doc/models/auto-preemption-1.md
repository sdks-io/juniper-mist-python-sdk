
# Auto Preemption 1

## Structure

`AutoPreemption1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `day_of_week` | [`DayOfWeekEnum`](../../doc/models/day-of-week-enum.md) | Optional | - |
| `enabled` | `bool` | Optional | whether auto preemption should happen |
| `time_of_day` | `string` | Optional | any / HH:MM (24-hour format). Preemption will happen within 15 mins of this time |

## Example (as JSON)

```json
{
  "day_of_week": "any",
  "enabled": false,
  "time_of_day": "time_of_day6"
}
```

