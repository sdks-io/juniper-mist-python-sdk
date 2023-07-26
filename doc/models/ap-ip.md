
# Ap Ip

IP AP settings

## Structure

`ApIp`

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

## Example (as JSON)

```json
{
  "vlan_id": 1,
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

