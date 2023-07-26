
# Org Site Sle Wifi Response

## Structure

`OrgSiteSleWifiResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `end` | `float` | Required | - |
| `interval` | `int` | Required | - |
| `limit` | `int` | Required | - |
| `page` | `int` | Required | - |
| `results` | [`List of Result1`](../../doc/models/result-1.md) | Required | **Constraints**: *Minimum Items*: `1`, *Unique Items Required* |
| `start` | `float` | Required | - |
| `total` | `int` | Required | - |

## Example (as JSON)

```json
{
  "end": 12.78,
  "interval": 92,
  "limit": 172,
  "page": 30,
  "results": [
    {
      "ap-availability": 138.67,
      "ap-health": 170.91,
      "capacity": 172.45,
      "coverage": 62.53,
      "num_aps": 56.89,
      "site_id": "00002183-0000-0000-0000-000000000000"
    }
  ],
  "start": 224.84,
  "total": 10
}
```

