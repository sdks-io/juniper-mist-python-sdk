
# Stats Bgp

## Structure

`StatsBgp`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `evpn_overlay` | `bool` | Optional | if this is created for evpn overlay |
| `for_overlay` | `bool` | Optional | if this is created for overlay |
| `local_as` | `int` | Optional | AS |
| `mac` | `string` | Optional | router mac address |
| `neighbor` | `string` | Optional | - |
| `neighbor_as` | `int` | Optional | - |
| `neighbor_mac` | `string` | Optional | if it's another device in the same org |
| `node` | `string` | Optional | node0/node1 |
| `org_id` | `string` | Optional | router org ID |
| `rx_pkts` | `int` | Optional | - |
| `rx_routes` | `int` | Optional | number of received routes |
| `site_id` | `string` | Optional | router site ID |
| `state` | [`StateEnum`](../../doc/models/state-enum.md) | Optional | - |
| `timestamp` | `float` | Optional | - |
| `tx_pkts` | `int` | Optional | - |
| `tx_routes` | `int` | Optional | - |
| `up` | `bool` | Optional | - |
| `uptime` | `int` | Optional | - |
| `vrf_name` | `string` | Optional | - |

## Example (as JSON)

```json
{
  "evpn_overlay": false,
  "for_overlay": false,
  "local_as": 184,
  "mac": "mac4",
  "neighbor": "neighbor0"
}
```

