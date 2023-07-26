
# Junos Oob Ip Config

Junos out-of-band (vme/em0/fxp0) IP config

## Structure

`JunosOobIpConfig`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `dns` | `List of string` | Optional | - |
| `dns_suffix` | `List of string` | Optional | - |
| `gateway` | `string` | Optional | - |
| `ip` | `string` | Optional | - |
| `netmask` | `string` | Optional | used only if `subnet` is not specified in `networks` |
| `network` | `string` | Optional | optional, the network to be used for mgmt |
| `node_1` | [`Node1`](../../doc/models/node-1.md) | Optional | for HA Cluster, node1 can have different IP Config |
| `mtype` | [`Type11Enum`](../../doc/models/type-11-enum.md) | Optional | **Default**: `'dynamic'` |
| `use_mgmt_vrf` | `bool` | Optional | if supported on the platform. If enabled, DNS will be using this routing-instance, too<br>**Default**: `True` |
| `use_mgmt_vrf_for_host_out` | `bool` | Optional | whether to use `mgmt_junos` for host-out traffic (NTP/TACPLUS/RADIUS/SYSLOG/SNMP), if alternative service is desired<br>**Default**: `False` |
| `vlan_id` | `int` | Optional | - |

## Example (as JSON)

```json
{
  "type": "dynamic",
  "use_mgmt_vrf": true,
  "use_mgmt_vrf_for_host_out": false,
  "dns": [
    "dns1"
  ],
  "dns_suffix": [
    "dns_suffix7"
  ],
  "gateway": "gateway0",
  "ip": "ip4",
  "netmask": "netmask0"
}
```

