
# Ap Ip 1

IP AP settings

## Structure

`ApIp1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `dns` | `List of string` | Optional | if `type`==`static` |
| `dns_suffix` | `List of string` | Optional | required if `type`==`static` |
| `gateway` | `string` | Optional | required if `type`==`static` |
| `gateway_6` | `string` | Optional | - |
| `ip` | `string` | Optional | required if `type`==`static` |
| `ip_6` | `string` | Optional | - |
| `mtu` | `int` | Optional | - |
| `netmask` | `string` | Optional | required if `type`==`static` |
| `netmask_6` | `string` | Optional | - |
| `mtype` | [`Type2Enum`](../../doc/models/type-2-enum.md) | Optional | static / dhcp (default) |
| `type_6` | [`Type6Enum`](../../doc/models/type-6-enum.md) | Optional | - |
| `vlan_id` | `int` | Optional | management vlan id, default is 1 (untagged)<br>**Default**: `1` |
| `network` | `string` | Optional | the network where this mgmt IP reside, this will be used as default network for outbound-ssh, dns, ntp, dns, tacplus, radius, syslog, snmp |
| `use_mgmt_vrf` | `bool` | Optional | for host-out traffic (NTP/TACPLUS/RADIUS/SYSLOG/SNMP)<br>**Default**: `False` |

## Example (as JSON)

```json
{
  "vlan_id": 1,
  "use_mgmt_vrf": false,
  "dns": [
    "dns1"
  ],
  "dns_suffix": [
    "dns_suffix7"
  ],
  "gateway": "gateway0",
  "gateway6": "gateway66",
  "ip": "ip4"
}
```

