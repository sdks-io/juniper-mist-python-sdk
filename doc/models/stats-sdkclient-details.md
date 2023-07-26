
# Stats Sdkclient Details

SDK Client Details statistics

## Structure

`StatsSdkclientDetails`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `uuid\|string` | Required | - |
| `last_seen` | `float` | Required | last seen timestamp |
| `map_id` | `uuid\|string` | Optional | map_id of the sdk client (if known), or null |
| `name` | `string` | Optional | name of the sdk client (if provided) |
| `network_connection` | [`NetworkConnection`](../../doc/models/network-connection.md) | Optional | various network connection info for the SDK client (if known, else omitted), with RSSI in dBm, and signal level as |
| `uuid` | `uuid\|string` | Required | uuid of the sdk client |
| `vbeacons` | [`List of Vbeacon1`](../../doc/models/vbeacon-1.md) | Optional | list of beacon_id’s of the sdk client is in and since when (if known)<br>**Constraints**: *Minimum Items*: `1`, *Unique Items Required* |
| `x` | `float` | Optional | x (in pixels) of user location on the map (if known) |
| `y` | `float` | Optional | y (in pixels) of user location on the map (if known) |
| `zones` | [`List of Zone2`](../../doc/models/zone-2.md) | Optional | list of zone_id’s of the sdk client is in and since when (if known)<br>**Constraints**: *Minimum Items*: `1`, *Unique Items Required* |

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
  "vbeacons": [
    {
      "id": "00000690-0000-0000-0000-000000000000",
      "since": 58.4
    },
    {
      "id": "00000691-0000-0000-0000-000000000000",
      "since": 58.41
    },
    {
      "id": "00000692-0000-0000-0000-000000000000",
      "since": 58.42
    }
  ],
  "x": 222.14
}
```

