
# Wan Client Events Search

## Structure

`WanClientEventsSearch`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `end` | `int` | Optional | - |
| `limit` | `int` | Optional | - |
| `results` | [`EventsClientWan`](../../doc/models/events-client-wan.md) | Optional | - |
| `start` | `int` | Optional | - |
| `total` | `int` | Optional | - |

## Example (as JSON)

```json
{
  "end": 254,
  "limit": 172,
  "results": {
    "When": "When8",
    "ev_type": "ev_type4",
    "metadata": {
      "key1": "val1",
      "key2": "val2"
    },
    "org_id": "00002492-0000-0000-0000-000000000000",
    "random_mac": false
  },
  "start": 212,
  "total": 10
}
```

