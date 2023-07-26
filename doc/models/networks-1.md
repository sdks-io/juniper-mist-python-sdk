
# Networks 1

## Structure

`Networks1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `auth_keys` | `dict` | Optional | if `auth_type`==`md5`. The property key is the key number |
| `auth_password` | `string` | Optional | if `auth_type`==`password`, the password, max length is 8 |
| `auth_type` | [`AuthTypeEnum`](../../doc/models/auth-type-enum.md) | Optional | auth type<br>**Default**: `'none'` |
| `bfd_minimum_interval` | `int` | Optional | **Constraints**: `>= 1`, `<= 255000` |
| `dead_interval` | `int` | Optional | **Constraints**: `>= 1`, `<= 65535` |
| `hello_interval` | `int` | Optional | **Constraints**: `>= 1`, `<= 255` |
| `interface_type` | [`InterfaceTypeEnum`](../../doc/models/interface-type-enum.md) | Optional | interface type (nbma = non-broadcast multi-access)<br>**Default**: `'nbma'` |
| `metric` | `int` | Optional | **Constraints**: `>= 1`, `<= 65535` |
| `passive` | `bool` | Optional | whether to send OSPF-Hello<br>**Default**: `False` |

## Example (as JSON)

```json
{
  "auth_type": "none",
  "bfd_minimum_interval": 500,
  "interface_type": "nbma",
  "metric": 10000,
  "passive": false,
  "auth_keys": {
    "key0": "auth_keys6",
    "key1": "auth_keys7"
  },
  "auth_password": "auth_password6",
  "dead_interval": 250
}
```

