
# Org Site Sle Wired Response

## Structure

`OrgSiteSleWiredResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `end` | `float` | Required | - |
| `interval` | `int` | Required | - |
| `limit` | `int` | Required | - |
| `page` | `int` | Required | - |
| `results` | [`List of Result2`](../../doc/models/result-2.md) | Required | **Constraints**: *Minimum Items*: `1`, *Unique Items Required* |
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
      "num_clients": 3.23,
      "num_switches": 2.13,
      "site_id": "00002183-0000-0000-0000-000000000000",
      "switch-health": 153.01,
      "switch-stc": 124.05,
      "switch-throughput": 91.91
    }
  ],
  "start": 224.84,
  "total": 10
}
```

