
# Oob Ip Config

ip configuration of the Mist Edge out-of-band management interface

## Structure

`OobIpConfig`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `dns` | `List of string` | Optional | if `type`=`static` |
| `gateway` | `string` | Optional | if `type`=`static` |
| `gateway_6` | `string` | Optional | - |
| `ip` | `string` | Optional | if `type`=`static` |
| `ip_6` | `string` | Optional | - |
| `netmask` | `string` | Optional | if `type`=`static` |
| `netmask_6` | `string` | Optional | - |
| `mtype` | [`Type6Enum`](../../doc/models/type-6-enum.md) | Optional | **Default**: `'dhcp'` |
| `type_6` | [`Type6Enum`](../../doc/models/type-6-enum.md) | Optional | - |

## Example (as JSON)

```json
{
  "dns": [
    "8.8.8.8",
    "4.4.4.4",
    "2001:4860:4860::8888"
  ],
  "gateway": "10.2.1.254",
  "gateway6": "2601:1700:43c0:dc0::1",
  "ip": "10.2.1.2",
  "ip6": "2601:1700:43c0:dc0:20c:29ff:fea7:93bc",
  "netmask": "255.255.255.0",
  "netmask6": "/64",
  "type": "static",
  "type6": "static"
}
```

