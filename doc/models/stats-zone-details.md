
# Stats Zone Details

Zone details statistics

## Structure

`StatsZoneDetails`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `assets` | `List of string` | Optional | list of ble assets currently in the zone and when they entered |
| `client_waits` | [`ClientWaits`](../../doc/models/client-waits.md) | Required | client wait time right now |
| `clients` | `List of string` | Optional | list of clients currently in the zone and when they entered |
| `id` | `uuid\|string` | Required | id of the zone |
| `map_id` | `uuid\|string` | Required | map_id of the zone |
| `name` | `string` | Required | name of the zone |
| `num_clients` | `int` | Required | - |
| `num_sdkclients` | `int` | Required | sdkclient wait time right now |
| `sdkclients` | `List of string` | Optional | list of sdkclients currently in the zone and when they entered |

## Example (as JSON)

```json
{
  "assets": [
    "assets4",
    "assets5",
    "assets6"
  ],
  "client_waits": {
    "avg": 174,
    "max": 70,
    "min": 152,
    "p95": 120
  },
  "clients": [
    "clients4"
  ],
  "id": "00001770-0000-0000-0000-000000000000",
  "map_id": "000006bc-0000-0000-0000-000000000000",
  "name": "name0",
  "num_clients": 150,
  "num_sdkclients": 246,
  "sdkclients": [
    "sdkclients4",
    "sdkclients5"
  ]
}
```

