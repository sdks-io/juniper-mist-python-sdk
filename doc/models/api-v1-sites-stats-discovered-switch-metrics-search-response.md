
# Api V1 Sites Stats Discovered Switch Metrics Search Response

## Structure

`ApiV1SitesStatsDiscoveredSwitchMetricsSearchResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `end` | `float` | Required | - |
| `limit` | `int` | Required | - |
| `next` | `string` | Optional | - |
| `results` | [`List of Result24`](../../doc/models/result-24.md) | Required | - |
| `start` | `float` | Required | - |
| `total` | `int` | Required | - |

## Example (as JSON)

```json
{
  "end": 12.78,
  "limit": 172,
  "results": [
    {
      "details": {
        "key1": "val1",
        "key2": "val2"
      },
      "org_id": "org_id9",
      "scope": "scope9",
      "score": 65,
      "site_id": "site_id9"
    }
  ],
  "start": 224.84,
  "total": 10,
  "next": "next2"
}
```

