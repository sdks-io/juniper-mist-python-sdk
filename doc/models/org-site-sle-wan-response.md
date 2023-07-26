
# Org Site Sle Wan Response

## Structure

`OrgSiteSleWanResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `end` | `float` | Required | - |
| `interval` | `int` | Required | - |
| `limit` | `int` | Required | - |
| `page` | `int` | Required | - |
| `results` | [`List of Result`](../../doc/models/result.md) | Required | **Constraints**: *Minimum Items*: `1`, *Unique Items Required* |
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
      "application-health": 40.11,
      "gateway-health": 51.47,
      "num_clients": 3.23,
      "num_gateways": 147.87,
      "site_id": "00002183-0000-0000-0000-000000000000",
      "wan-link-health": 69.09
    }
  ],
  "start": 224.84,
  "total": 10
}
```

