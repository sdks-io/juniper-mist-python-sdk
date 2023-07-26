
# Stats Zone

Zone statistics

## Structure

`StatsZone`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `assets_waits` | [`AssetsWaits`](../../doc/models/assets-waits.md) | Optional | ble asset wait time right now |
| `clients_waits` | [`ClientsWaits`](../../doc/models/clients-waits.md) | Optional | client wait time right now |
| `created_time` | `int` | Optional | - |
| `id` | `uuid\|string` | Required | id of the zone |
| `map_id` | `uuid\|string` | Required | map_id of the zone |
| `modified_time` | `int` | Optional | - |
| `name` | `string` | Required | name of the zone |
| `num_assets` | `int` | Optional | number of assets |
| `num_clients` | `int` | Optional | number of wifi clients (unconnected + connected) |
| `num_sdkclients` | `int` | Optional | number of sdk clients |
| `occupancy_limit` | `int` | Optional | - |
| `org_id` | `string` | Optional | - |
| `sdkclients_waits` | [`SdkclientsWaits`](../../doc/models/sdkclients-waits.md) | Optional | sdkclient wait time right now |
| `site_id` | `string` | Optional | - |

## Example (as JSON)

```json
{
  "assets_waits": {
    "avg": 81.08,
    "max": 149.16,
    "min": 75.74,
    "p95": 47.26
  },
  "clients_waits": {
    "avg": 73.04,
    "max": 141.12,
    "min": 188.3,
    "p95": 39.22
  },
  "created_time": 118,
  "id": "00001770-0000-0000-0000-000000000000",
  "map_id": "000006bc-0000-0000-0000-000000000000",
  "modified_time": 98,
  "name": "name0",
  "num_assets": 140
}
```

