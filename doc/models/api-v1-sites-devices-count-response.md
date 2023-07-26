
# Api V1 Sites Devices Count Response

## Structure

`ApiV1SitesDevicesCountResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `distinct` | `string` | Required | - |
| `end` | `float` | Required | - |
| `limit` | `int` | Required | - |
| `percentage` | `int` | Required | - |
| `results` | [`List of Result12`](../../doc/models/result-12.md) | Required | **Constraints**: *Minimum Items*: `1`, *Unique Items Required* |
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
      "model": "model9"
    }
  ],
  "start": 224.84,
  "total": 10
}
```

