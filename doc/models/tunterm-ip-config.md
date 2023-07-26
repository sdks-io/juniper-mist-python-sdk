
# Tunterm Ip Config

ip configuration of the Mist Tunnel interface

## Structure

`TuntermIpConfig`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `gateway` | `string` | Required | - |
| `ip` | `string` | Required | untagged VLAN |
| `netmask` | `string` | Required | - |

## Example (as JSON)

```json
{
  "gateway": "10.2.1.254",
  "ip": "10.2.1.1",
  "netmask": "255.255.255.0"
}
```

