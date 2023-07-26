
# Wan Clients Search

## Structure

`WanClientsSearch`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `end` | `int` | Optional | - |
| `limit` | `int` | Optional | - |
| `results` | [`StatsClientsWan`](../../doc/models/stats-clients-wan.md) | Optional | - |
| `start` | `int` | Optional | - |
| `total` | `int` | Optional | - |

## Example (as JSON)

```json
{
  "end": 254,
  "limit": 172,
  "results": {
    "When": "When8",
    "hostname": [
      "hostname6",
      "hostname7",
      "hostname8"
    ],
    "ip": [
      "ip7",
      "ip8"
    ],
    "last_hostname": "last_hostname8",
    "last_ip": "last_ip6"
  },
  "start": 212,
  "total": 10
}
```

