
# Network

Networks are usually subnets that have cross-site significance. `networks`in Org Settings will got merged into `networks`in Site Setting. For gateways, they can be used to define Service Routes.

## Structure

`Network`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `created_time` | `float` | Optional | - |
| `disallow_mist_services` | `bool` | Optional | whether to disallow Mist Devices in the network<br>**Default**: `False` |
| `gateway` | `string` | Optional | - |
| `hosts` | [`dict`](../../doc/models/hosts.md) | Optional | - |
| `id` | `uuid\|string` | Optional | - |
| `internal_access` | [`InternalAccess`](../../doc/models/internal-access.md) | Optional | - |
| `internet_access` | [`InternetAccess`](../../doc/models/internet-access.md) | Optional | whether this network has direct internet access |
| `isolation` | `bool` | Optional | whether to allow clients in the network to talk to each other |
| `modified_time` | `float` | Optional | - |
| `name` | `string` | Optional | - |
| `org_id` | `uuid\|string` | Optional | - |
| `subnet` | `string` | Optional | - |
| `tenants` | [`dict`](../../doc/models/tenants.md) | Optional | - |
| `vlan_id` | `int` | Optional | - |
| `vpn_access` | [`dict`](../../doc/models/vpn-access.md) | Optional | whether this network can be accessed from vpn |

## Example (as JSON)

```json
{
  "disallow_mist_services": false,
  "gateway": "192.168.70.1",
  "subnet": "192.168.70.0/24",
  "created_time": 198.3,
  "hosts": {
    "key0": {
      "external_ips": "external_ips9",
      "ips": "ips7"
    }
  },
  "id": "00001770-0000-0000-0000-000000000000"
}
```

