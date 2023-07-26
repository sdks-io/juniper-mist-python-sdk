
# Sle Impacted Chassis

## Structure

`SleImpactedChassis`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `chassis` | [`List of Chassi`](../../doc/models/chassi.md) | Optional | - |
| `classifier` | `string` | Optional | - |
| `end` | `int` | Optional | - |
| `failure` | `string` | Optional | - |
| `limit` | `int` | Optional | - |
| `metric` | `string` | Optional | - |
| `page` | `int` | Optional | - |
| `start` | `int` | Optional | - |
| `total_count` | `int` | Optional | - |

## Example (as JSON)

```json
{
  "chassis": [
    {
      "chassis": "chassis8",
      "degraded": 135.68,
      "duration": 8.74,
      "role": "role8",
      "switch_mac": "switch_mac6"
    },
    {
      "chassis": "chassis7",
      "degraded": 135.69,
      "duration": 8.75,
      "role": "role7",
      "switch_mac": "switch_mac7"
    }
  ],
  "classifier": "classifier4",
  "end": 254,
  "failure": "failure6",
  "limit": 172
}
```

