
# Node 1

for HA Cluster, node1 can have different IP Config

## Structure

`Node1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `ip` | `string` | Optional | - |
| `netmask` | `string` | Optional | used only if `subnet` is not specified in `networks` |
| `network` | `string` | Optional | optional, the network to be used for mgmt |
| `mtype` | [`Type11Enum`](../../doc/models/type-11-enum.md) | Optional | **Default**: `'dynamic'` |
| `use_mgmt_vrf` | `bool` | Optional | if supported on the platform. If enabled, DNS will be using this routing-instance, too<br>**Default**: `False` |
| `use_mgmt_vrf_for_host_out` | `bool` | Optional | whether to use `mgmt_junos` for host-out traffic (NTP/TACPLUS/RADIUS/SYSLOG/SNMP), if alternative service is desired<br>**Default**: `False` |
| `vlan_id` | `int` | Optional | optional, if different from parent |

## Example (as JSON)

```json
{
  "type": "dynamic",
  "use_mgmt_vrf": false,
  "use_mgmt_vrf_for_host_out": false,
  "ip": "ip4",
  "netmask": "netmask0",
  "network": "network4"
}
```

