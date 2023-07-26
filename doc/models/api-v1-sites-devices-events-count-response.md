
# Api V1 Sites Devices Events Count Response

## Structure

`ApiV1SitesDevicesEventsCountResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `distinct` | `string` | Required | - |
| `end` | `int` | Required | - |
| `limit` | `int` | Required | - |
| `percentage` | `int` | Required | - |
| `results` | [`List of Result13`](../../doc/models/result-13.md) | Required | **Constraints**: *Minimum Items*: `1`, *Unique Items Required* |
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
      "count": 143,
      "type": "type7"
    }
  ],
  "start": 212,
  "total": 10
}
```

