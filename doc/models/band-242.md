
# Band 242

radio stat of 2.4G radio

## Structure

`Band242`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `bandwidth` | [`Bandwidth2Enum`](../../doc/models/bandwidth-2-enum.md) | Optional | current channel bandwidth |
| `channel` | `int` | Optional | current channel the radio is running on |
| `dynamic_chaining_enalbed` | `bool` | Optional | Use dynamic chaining for downlink |
| `mac` | `string` | Optional | radio (base) mac, it can have 16 bssids (e.g. 5c5b350001a0-5c5b350001af) |
| `num_clients` | `int` | Optional | number of clients |
| `power` | `int` | Optional | transmit power (in dBm) |
| `rx_bytes` | `float` | Optional | - |
| `rx_pkts` | `float` | Optional | - |
| `tx_bytes` | `float` | Optional | - |
| `tx_pkts` | `float` | Optional | - |
| `util_all` | `int` | Optional | all utilization in percentage |
| `util_non_wifi` | `int` | Optional | reception of “No Packets” utilization in percentage, received frames with invalid PLCPs and CRS glitches as noise |
| `util_rx_in_bss` | `int` | Optional | reception of “In BSS” utilization in percentage, only frames that are received from AP/STAs within the BSS |
| `util_rx_other_bss` | `int` | Optional | reception of “Other BSS” utilization in percentage, all frames received from AP/STAs that are outside the BSS |
| `util_tx` | `int` | Optional | transmission utilization in percentage |
| `util_unknown_wifi` | `int` | Optional | reception of “No Category” utilization in percentage, all 802.11 frames that are corrupted at the receiver |

## Example (as JSON)

```json
{
  "bandwidth": 20,
  "channel": 120,
  "dynamic_chaining_enalbed": false,
  "mac": "mac4",
  "num_clients": 150
}
```

