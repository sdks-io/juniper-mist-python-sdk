
# Stats Unconnected Clients

Unconnected clients statistics

## Structure

`StatsUnconnectedClients`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `ap_mac` | `string` | Required | mac address of the AP that heard the client |
| `last_seen` | `float` | Required | last seen timestamp |
| `mac` | `string` | Required | mac address of the (unconnected) client |
| `manufacture` | `string` | Required | device manufacture, through fingerprinting or OUI |
| `map_id` | `uuid\|string` | Optional | map_id of the client (if known), or null |
| `rssi` | `int` | Required | client RSSI observered by the AP that heard the client (in dBm) |
| `x` | `int` | Optional | x (in pixels) of user location on the map (if known) |
| `y` | `int` | Required | y (in pixels) of user location on the map (if known) |

## Example (as JSON)

```json
{
  "ap_mac": "ap_mac2",
  "last_seen": 33.7,
  "mac": "mac4",
  "manufacture": "manufacture4",
  "map_id": "000006bc-0000-0000-0000-000000000000",
  "rssi": 22,
  "x": 198,
  "y": 130
}
```

