
# Bgp Stats Array Search

## Structure

`BgpStatsArraySearch`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `end` | `float` | Optional | - |
| `limit` | `int` | Optional | - |
| `results` | [`List of StatsBgp`](../../doc/models/stats-bgp.md) | Optional | - |
| `start` | `float` | Optional | - |
| `total` | `int` | Optional | - |

## Example (as JSON)

```json
{
  "end": 12.78,
  "limit": 172,
  "results": [
    {
      "evpn_overlay": true,
      "for_overlay": true,
      "local_as": 101,
      "mac": "mac7",
      "neighbor": "neighbor3"
    }
  ],
  "start": 224.84,
  "total": 10
}
```

