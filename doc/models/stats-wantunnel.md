
# Stats Wantunnel

## Structure

`StatsWantunnel`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `auth_algo` | `string` | Optional | authentication algorithm |
| `encrypt_algo` | `string` | Optional | encryption algorithm |
| `ike_version` | `string` | Optional | ike version |
| `ip` | `string` | Optional | ip address |
| `last_event` | `string` | Optional | reason of why the tunnel is down |
| `mac` | `string` | Optional | router mac address |
| `node` | `string` | Optional | node0/node1 |
| `org_id` | `string` | Optional | - |
| `peer_host` | `string` | Optional | peer host |
| `peer_ip` | `string` | Optional | peer ip address |
| `protocol` | [`Protocol8Enum`](../../doc/models/protocol-8-enum.md) | Optional | - |
| `rx_bytes` | `int` | Optional | - |
| `rx_pkts` | `int` | Optional | - |
| `site_id` | `string` | Optional | - |
| `tunnel_name` | `string` | Optional | Mist Tunnel Name |
| `tx_bytes` | `int` | Optional | - |
| `tx_pkts` | `int` | Optional | - |
| `up` | `bool` | Optional | - |
| `uptime` | `int` | Optional | duration from first (or last) SA was established |

## Example (as JSON)

```json
{
  "auth_algo": "auth_algo2",
  "encrypt_algo": "encrypt_algo6",
  "ike_version": "ike_version4",
  "ip": "ip4",
  "last_event": "last_event4"
}
```

