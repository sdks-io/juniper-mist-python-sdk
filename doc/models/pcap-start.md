
# Pcap Start

## Structure

`PcapStart`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `ap_count` | `int` | Optional | - |
| `aps` | `List of string` | Optional | - |
| `client_mac` | `string` | Optional | - |
| `duration` | `float` | Optional | - |
| `enabled` | `bool` | Optional | - |
| `expiry` | `float` | Optional | - |
| `format` | `string` | Optional | - |
| `id` | `uuid\|string` | Required | - |
| `include_mcast` | `bool` | Optional | - |
| `invalid_aps` | `object` | Optional | - |
| `max_pkt_len` | `int` | Optional | - |
| `num_packets` | `int` | Optional | - |
| `org_id` | `uuid\|string` | Required | - |
| `raw` | `bool` | Optional | - |
| `site_id` | `uuid\|string` | Required | - |
| `ssid` | `string` | Optional | - |
| `tcpdump_parser_expression` | `string` | Optional | - |
| `timestamp` | `float` | Required | - |
| `mtype` | `string` | Required | - |

## Example (as JSON)

```json
{
  "ap_count": 124,
  "aps": [
    "aps1",
    "aps2"
  ],
  "client_mac": "client_mac8",
  "duration": 228.96,
  "enabled": false,
  "id": "00001770-0000-0000-0000-000000000000",
  "org_id": "00000ec8-0000-0000-0000-000000000000",
  "site_id": "000007d6-0000-0000-0000-000000000000",
  "timestamp": 128.82,
  "type": "type0"
}
```

