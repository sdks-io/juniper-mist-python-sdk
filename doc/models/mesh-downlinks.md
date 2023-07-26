
# Mesh Downlinks

the property key is the mesh downlink id

## Structure

`MeshDownlinks`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `band` | `string` | Optional | - |
| `channel` | `int` | Optional | - |
| `idle_time` | `int` | Optional | - |
| `last_seen` | `int` | Optional | - |
| `proto` | `string` | Optional | - |
| `rssi` | `int` | Optional | - |
| `rx_bps` | `int` | Optional | - |
| `rx_bytes` | `int` | Optional | - |
| `rx_packets` | `int` | Optional | - |
| `rx_rate` | `int` | Optional | - |
| `rx_retries` | `int` | Optional | - |
| `site_id` | `uuid\|string` | Optional | - |
| `snr` | `int` | Optional | - |
| `tx_bps` | `int` | Optional | - |
| `tx_bytes` | `int` | Optional | - |
| `tx_packets` | `int` | Optional | - |
| `tx_rate` | `int` | Optional | - |
| `tx_retries` | `int` | Optional | - |

## Example (as JSON)

```json
{
  "band": "band2",
  "channel": 120,
  "idle_time": 20,
  "last_seen": 42,
  "proto": "proto6"
}
```

