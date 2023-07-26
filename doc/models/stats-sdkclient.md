
# Stats Sdkclient

SDK Client statistics

## Structure

`StatsSdkclient`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `uuid\|string` | Required | - |
| `last_seen` | `float` | Required | last seen timestamp |
| `map_id` | `uuid\|string` | Optional | map_id of the sdk client (if known), or null |
| `name` | `string` | Optional | name of the sdk client (if provided) |
| `network_connection` | [`NetworkConnection`](../../doc/models/network-connection.md) | Required | various network connection info for the SDK client (if known, else omitted), with RSSI in dBm, and signal level as |
| `uuid` | `uuid\|string` | Required | uuid of the sdk client |
| `x` | `float` | Optional | x (in pixels) of user location on the map (if known) |
| `y` | `float` | Optional | y (in pixels) of user location on the map (if known) |

## Example (as JSON)

```json
{
  "id": "00001770-0000-0000-0000-000000000000",
  "last_seen": 33.7,
  "map_id": "000006bc-0000-0000-0000-000000000000",
  "name": "name0",
  "network_connection": {
    "mac": "mac2",
    "rssi": 235.8,
    "signal_level": 47.82,
    "type": "type2"
  },
  "uuid": "00000f7e-0000-0000-0000-000000000000",
  "x": 222.14,
  "y": 165.14
}
```

