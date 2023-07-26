
# Internet Access

whether this network has direct internet access

## Structure

`InternetAccess`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `create_simple_service_policy` | `bool` | Optional | **Default**: `False` |
| `destination_nat` | [`dict`](../../doc/models/destination-nat.md) | Optional | The property key may be an IP/Port (i.e. "63.16.0.3:443"), or a port (i.e. ":2222") |
| `enabled` | `bool` | Optional | - |
| `restricted` | `bool` | Optional | by default, all access is allowed, to only allow certain traffic, make `restricted`=`true` and define service_policies<br>**Default**: `False` |
| `static_nat` | [`dict`](../../doc/models/static-nat.md) | Optional | The property key may be an IP Address (i.e. "63.16.0.1), or a CIDR (i.e. "63.16.0.32/30") |

## Example (as JSON)

```json
{
  "create_simple_service_policy": false,
  "restricted": false,
  "destination_nat": {
    "key0": {
      "internal_ip": "internal_ip7",
      "name": "name1",
      "port": 99
    }
  },
  "enabled": false,
  "static_nat": {
    "key0": {
      "internal_ip": "internal_ip2",
      "name": "name2"
    },
    "key1": {
      "internal_ip": "internal_ip1",
      "name": "name3"
    },
    "key2": {
      "internal_ip": "internal_ip0",
      "name": "name4"
    }
  }
}
```

