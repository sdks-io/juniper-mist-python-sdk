
# Api V1 Sites Stats Discovered Switches Count Response

## Structure

`ApiV1SitesStatsDiscoveredSwitchesCountResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `distinct` | `string` | Required | - |
| `end` | `float` | Required | - |
| `limit` | `int` | Required | - |
| `percentage` | `int` | Required | - |
| `results` | [`List of Result25`](../../doc/models/result-25.md) | Required | **Constraints**: *Minimum Items*: `1`, *Unique Items Required* |
| `start` | `float` | Required | - |
| `total` | `int` | Required | - |

## Example (as JSON)

```json
{
  "distinct": "distinct6",
  "end": 12.78,
  "limit": 172,
  "percentage": 162,
  "results": [
    {
      "count": 143,
      "system_name": "system_name3"
    }
  ],
  "start": 224.84,
  "total": 10
}
```

