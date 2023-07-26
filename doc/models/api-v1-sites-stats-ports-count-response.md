
# Api V1 Sites Stats Ports Count Response

## Structure

`ApiV1SitesStatsPortsCountResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `distinct` | `string` | Required | - |
| `end` | `int` | Required | - |
| `limit` | `int` | Required | - |
| `results` | [`List of Result27`](../../doc/models/result-27.md) | Required | **Constraints**: *Minimum Items*: `1`, *Unique Items Required* |
| `start` | `int` | Required | - |
| `total` | `int` | Required | - |

## Example (as JSON)

```json
{
  "distinct": "distinct6",
  "end": 254,
  "limit": 172,
  "results": [
    {
      "count": 143,
      "mac": "mac7"
    }
  ],
  "start": 212,
  "total": 10
}
```

