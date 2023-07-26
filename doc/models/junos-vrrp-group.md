
# Junos Vrrp Group

Junos VRRP group

## Structure

`JunosVrrpGroup`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `auth_key` | `string` | Optional | if `auth_type`==`md5` |
| `auth_password` | `string` | Optional | if `auth_type`==`simple` |
| `auth_type` | [`AuthType1Enum`](../../doc/models/auth-type-1-enum.md) | Optional | **Default**: `'md5'` |
| `networks` | [`dict`](../../doc/models/networks-2.md) | Optional | The property key is the network name |

## Example (as JSON)

```json
{
  "auth_type": "md5",
  "auth_key": "auth_key8",
  "auth_password": "auth_password6",
  "networks": {
    "key0": {
      "ip": "ip6"
    },
    "key1": {
      "ip": "ip7"
    },
    "key2": {
      "ip": "ip8"
    }
  }
}
```

