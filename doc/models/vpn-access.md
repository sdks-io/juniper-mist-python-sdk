
# Vpn Access

## Structure

`VpnAccess`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `affinity` | [`AffinityEnum`](../../doc/models/affinity-enum.md) | Optional | DRAFT - when used in path preference, whether we should prefer the same hub or by path<br>**Default**: `'hub'` |
| `allow_ping` | `bool` | Optional | whether to allow ping from vpn into this routed network |
| `destination_nat` | [`dict`](../../doc/models/destination-nat-1.md) | Optional | Property key is the external IP / port (e.g. "172.16.0.5/30" or "172.16.0.3:8443") |
| `nat_pool` | `string` | Optional | if `routed`==`false` (usually at Spoke), but some hosts needs to be reachable from Hub, a subnet is required to create and advertise the route to Hub |
| `no_readvertise_to_lan_bgp` | `bool` | Optional | toward LAN-side BGP peers<br>**Default**: `False` |
| `no_readvertise_to_overlay` | `bool` | Optional | toward overlay<br>how HUB should deal with routes it received from Spokes |
| `routed` | `bool` | Optional | whether this network is routable |
| `source_nat` | [`SourceNat`](../../doc/models/source-nat.md) | Optional | if `routed`==`false` (usually at Spoke), but some hosts needs to be reachable from Hub |
| `static_nat` | [`dict`](../../doc/models/static-nat.md) | Optional | The property key may be an IP Address (i.e. "172.16.0.1"), and IP Address and Port (i.e. "172.16.0.1:8443") or a CIDR (i.e. "172.16.0.12/20") |
| `summarized_subnet` | `string` | Optional | toward overlay<br>how HUB should deal with routes it received from Spokes |
| `summarized_subnet_to_lan_bgp` | `string` | Optional | toward LAN-side BGP peers |

## Example (as JSON)

```json
{
  "affinity": "hub",
  "nat_pool": "172.16.0.0/26",
  "no_readvertise_to_lan_bgp": false,
  "summarized_subnet": "172.16.0.0/16",
  "summarized_subnet_to_lan_bgp": "172.16.0.0/16",
  "allow_ping": false,
  "destination_nat": {
    "key0": {
      "name": "name1",
      "port": 99,
      "to": "to5"
    }
  }
}
```

