
# Junos Ip Config

Junos IP Config

## Structure

`JunosIpConfig`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `dns` | `List of string` | Optional | - |
| `dns_suffix` | `List of string` | Optional | - |
| `gateway` | `string` | Optional | - |
| `ip` | `string` | Optional | - |
| `netmask` | `string` | Optional | used only if `subnet` is not specified in `networks` |
| `network` | `string` | Optional | the network where this mgmt IP reside, this will be used as default network for outbound-ssh, dns, ntp, dns, tacplus, radius, syslog, snmp |
| `mtype` | [`Type11Enum`](../../doc/models/type-11-enum.md) | Optional | **Default**: `'dynamic'` |
| `use_mgmt_vrf` | `bool` | Optional | for host-out traffic (NTP/TACPLUS/RADIUS/SYSLOG/SNMP)<br>**Default**: `False` |

## Example (as JSON)

```json
{
  "type": "dynamic",
  "use_mgmt_vrf": false,
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

