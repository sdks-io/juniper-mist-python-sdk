
# Paths

## Structure

`Paths`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `cost` | `int` | Optional | - |
| `gateway_ip` | `string` | Optional | if `type`==`local`, if a different gateway is desired |
| `internet_access` | `bool` | Optional | when `type`==`vpn`, if this vpn path can be used for internet<br>**Default**: `False` |
| `name` | `string` | Optional | - |
| `networks` | `List of string` | Optional | if `type`==`local` |
| `target_ips` | `List of string` | Optional | if `type`==`local`, if destination IP is to be replaced |
| `mtype` | [`Type19Enum`](../../doc/models/type-19-enum.md) | Optional | - |

## Example (as JSON)

```json
{
  "internet_access": false,
  "cost": 156,
  "gateway_ip": "gateway_ip6",
  "name": "name0",
  "networks": [
    "networks2",
    "networks3",
    "networks4"
  ]
}
```

