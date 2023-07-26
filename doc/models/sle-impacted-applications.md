
# Sle Impacted Applications

## Structure

`SleImpactedApplications`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `apps` | [`List of Apps1`](../../doc/models/apps-1.md) | Optional | - |
| `classifier` | `string` | Optional | - |
| `end` | `int` | Optional | - |
| `failure` | `string` | Optional | - |
| `limit` | `string` | Optional | - |
| `metric` | `string` | Optional | - |
| `page` | `int` | Optional | - |
| `start` | `int` | Optional | - |
| `total_count` | `int` | Optional | - |

## Example (as JSON)

```json
{
  "apps": [
    {
      "app": "app2",
      "degraded": 212,
      "duration": 62,
      "name": "name4",
      "threshold": 174
    },
    {
      "app": "app3",
      "degraded": 213,
      "duration": 63,
      "name": "name5",
      "threshold": 175
    }
  ],
  "classifier": "classifier4",
  "end": 254,
  "failure": "failure6",
  "limit": "limit4"
}
```

