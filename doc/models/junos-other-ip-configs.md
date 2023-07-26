
# Junos Other Ip Configs

optional, if it's required to have switch's L3 presense on a network/vlan

## Structure

`JunosOtherIpConfigs`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `evpn_anycast` | `bool` | Optional | for EVPN, if anycast is desired<br>**Default**: `False` |
| `ip` | `string` | Optional | required if `type`==`static` |
| `netmask` | `string` | Optional | optional, `subnet` from `network` definition will be used if defined |
| `mtype` | [`Type6Enum`](../../doc/models/type-6-enum.md) | Optional | **Default**: `'dhcp'` |

## Example (as JSON)

```json
{
  "evpn_anycast": false,
  "type": "dhcp",
  "ip": "ip4",
  "netmask": "netmask0"
}
```

