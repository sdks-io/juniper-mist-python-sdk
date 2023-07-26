
# Junos Ip Config Gateway

Junos IP Config

## Structure

`JunosIpConfigGateway`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `dns` | `List of string` | Optional | except for out-of-band interface (vme/em0/fxp0) |
| `dns_suffix` | `List of string` | Optional | except for out-of-band interface (vme/em0/fxp0) |
| `gateway` | `string` | Optional | except for out-of-band interface (vme/em0/fxp0) |
| `ip` | `string` | Optional | - |
| `netmask` | `string` | Optional | used only if `subnet` is not specified in `networks` |
| `network` | `string` | Optional | optional, the network to be used for mgmt |
| `poser_password` | `string` | Optional | if `type`==`pppoe` |
| `ppoe_username` | `string` | Optional | if `type`==`pppoe` |
| `pppoe_auth` | [`PppoeAuthEnum`](../../doc/models/pppoe-auth-enum.md) | Optional | if `type`==`pppoe`<br>**Default**: `'none'` |
| `mtype` | [`Type14Enum`](../../doc/models/type-14-enum.md) | Optional | **Default**: `'dhcp'` |

## Example (as JSON)

```json
{
  "pppoe_auth": "none",
  "type": "dhcp",
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

