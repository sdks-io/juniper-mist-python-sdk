
# Capture

## Structure

`Capture`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `ap_mac` | `string` | Optional | filter by ap_mac |
| `client_mac` | `string` | Optional | client mac, required if `type`==`client`; optional otherwise |
| `duration` | `int` | Optional | duration of the capture, in seconds<br>**Default**: `600`<br>**Constraints**: `>= 0`, `<= 86400` |
| `includes_mcast` | `bool` | Optional | - |
| `max_pkt_len` | `int` | Optional | max_len of each packet to capture<br>**Default**: `128`<br>**Constraints**: `>= 128`, `<= 2048` |
| `num_packets` | `int` | Optional | number of packets to capture, 0 for unlimited, default is 1024 for client-capture<br>**Default**: `1024`<br>**Constraints**: `>= 0` |
| `ssid` | `string` | Optional | optional filter by ssid |
| `mtype` | [`Type7Enum`](../../doc/models/type-7-enum.md) | Optional | client<br>**Default**: `'client'` |
| `format` | [`FormatEnum`](../../doc/models/format-enum.md) | Optional | pcap format<br>**Default**: `'pcap'` |
| `tcpdump_expression` | `string` | Optional | tcpdump expression |
| `band` | [`Band1Enum`](../../doc/models/band-1-enum.md) | Optional | only used for radiotap<br>**Default**: `'24'` |
| `wlan_id` | `uuid\|string` | Optional | WLAN ID |
| `radiotap_tcpdump_expression` | `string` | Optional | tcpdump expression for radiotap interface (802.11 + radio headers) |
| `wired_tcpdump_expression` | `string` | Optional | tcpdump expression for wired |
| `wireless_tcpdump_expression` | `string` | Optional | tcpdump expression for radiotap interface (802.11) |
| `gateways` | [`dict`](../../doc/models/gateways.md) | Optional | List of SSRs. Property key is the SSR MAC |
| `aps` | [`dict`](../../doc/models/aps.md) | Optional | - |
| `channel` | `string` | Optional | specify the channel value where scan PCAP has to be started |
| `width` | `string` | Optional | specify the bandwidth value with respect to the channel. |
| `switches` | [`dict`](../../doc/models/switches.md) | Optional | Property key is the switch mac |

## Example (as JSON)

```json
{
  "duration": 600,
  "max_pkt_len": 1500,
  "num_packets": 1024,
  "type": "client",
  "format": "pcap",
  "band": "24",
  "ap_mac": "ap_mac2",
  "client_mac": "client_mac8",
  "includes_mcast": false
}
```

