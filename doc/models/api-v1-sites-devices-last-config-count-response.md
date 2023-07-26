
# Api V1 Sites Devices Last Config Count Response

## Structure

`ApiV1SitesDevicesLastConfigCountResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `distinct` | `string` | Required | - |
| `end` | `int` | Required | - |
| `limit` | `int` | Required | - |
| `percentage` | `int` | Required | - |
| `results` | [`List of Result14`](../../doc/models/result-14.md) | Required | **Constraints**: *Minimum Items*: `1`, *Unique Items Required* |
| `start` | `int` | Required | - |
| `total` | `int` | Required | - |

## Example (as JSON)

```json
{
  "distinct": "distinct6",
  "end": 254,
  "limit": 172,
  "percentage": 162,
  "results": [
    {
      "ap": "ap1",
      "count": 143
    }
  ],
  "start": 212,
  "total": 10
}
```

