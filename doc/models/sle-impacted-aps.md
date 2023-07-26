
# Sle Impacted Aps

## Structure

`SleImpactedAps`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `aps` | [`List of Aps1`](../../doc/models/aps-1.md) | Required | **Constraints**: *Minimum Items*: `1`, *Unique Items Required* |
| `classifier` | `string` | Required | - |
| `end` | `float` | Required | - |
| `failure` | `string` | Required | - |
| `limit` | `float` | Required | - |
| `metric` | `string` | Required | **Constraints**: *Minimum Length*: `1` |
| `page` | `float` | Required | - |
| `start` | `float` | Required | - |
| `total_count` | `float` | Required | - |

## Example (as JSON)

```json
{
  "aps": [
    {
      "ap_mac": "ap_mac3",
      "degraded": 123.41,
      "duration": 252.47,
      "name": "name1",
      "total": 104.59
    }
  ],
  "classifier": "classifier4",
  "end": 12.78,
  "failure": "failure6",
  "limit": 237.24,
  "metric": "metric8",
  "page": 110.38,
  "start": 224.84,
  "total_count": 82.96
}
```

