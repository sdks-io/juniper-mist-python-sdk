
# Pcap Status

## Structure

`PcapStatus`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `ap_mac` | `string` | Optional | - |
| `aps` | `List of string` | Optional | List of target APs to capture packets |
| `client_mac` | `string` | Optional | - |
| `duration` | `int` | Optional | - |
| `failed` | `List of string` | Optional | List of APs where configuration attempt failed |
| `gateways` | `List of string` | Optional | List of target Gateways to capture packets if a gateway capture type is specified |
| `id` | `uuid\|string` | Required | unique id for the capture |
| `includes_mcast` | `bool` | Optional | - |
| `max_num_packets` | `int` | Optional | max number of packets configured by user |
| `max_pkt_len` | `int` | Optional | - |
| `num_packets` | `int` | Optional | total number of packets captured by all AP, not applicable for type [client, new_assoc] |
| `ok` | `List of string` | Optional | List of target APs successfully configured to capture packets |
| `radiotap_tcpdump_expression` | `string` | Optional | when `type`==`radiotap`, radiotap_tcpdump_expression expression provided by the user |
| `scan_tcpdump_expression` | `string` | Optional | when `type`==`scan`, scan_tcpdump_expression provided by the user |
| `ssid` | `string` | Optional | - |
| `started_time` | `int` | Optional | - |
| `tcpdump_expression` | `string` | Optional | tcpdump expression provided by the user (common) |
| `mtype` | [`Type59Enum`](../../doc/models/type-59-enum.md) | Required | - |
| `wired_tcpdump_expression` | `string` | Optional | when `type`==`wired`, wired_tcpdump_expression provided by the user |
| `wireless_tcpdump_expression` | `string` | Optional | when `type`==`‘wireless’`, wireless_tcpdump_expression provided by the user |

## Example (as JSON)

```json
{
  "client_mac": "60a10a773412",
  "duration": 300,
  "id": "00001770-0000-0000-0000-000000000000",
  "max_num_packets": 1000,
  "max_pkt_len": 128,
  "started_time": 1435080709,
  "type": "client",
  "ap_mac": "ap_mac2",
  "aps": [
    "aps1",
    "aps2"
  ],
  "failed": [
    "failed6",
    "failed7"
  ]
}
```

