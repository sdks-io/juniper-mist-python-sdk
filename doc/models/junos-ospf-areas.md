
# Junos Ospf Areas

Junos OSPF areas

## Structure

`JunosOspfAreas`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `include_loopback` | `bool` | Optional | **Default**: `False` |
| `networks` | [`dict`](../../doc/models/networks-1.md) | Optional | networks to participate in an OSPF area. The property key is the network name |
| `mtype` | [`Type25Enum`](../../doc/models/type-25-enum.md) | Optional | OSPF type, default (default) / stub / nssa<br>**Default**: `'default'` |

## Example (as JSON)

```json
{
  "include_loopback": false,
  "type": "default",
  "networks": {
    "key0": {
      "auth_keys": {
        "key0": "auth_keys8",
        "key1": "auth_keys9"
      },
      "auth_password": "auth_password8",
      "auth_type": "md5",
      "bfd_minimum_interval": 32,
      "dead_interval": 180
    },
    "key1": {
      "auth_keys": {
        "key0": "auth_keys9",
        "key1": "auth_keys0",
        "key2": "auth_keys1"
      },
      "auth_password": "auth_password9",
      "auth_type": "none",
      "bfd_minimum_interval": 31,
      "dead_interval": 181
    },
    "key2": {
      "auth_keys": {
        "key0": "auth_keys0"
      },
      "auth_password": "auth_password0",
      "auth_type": "password",
      "bfd_minimum_interval": 30,
      "dead_interval": 182
    }
  }
}
```

