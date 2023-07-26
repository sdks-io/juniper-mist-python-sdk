
# Mxcluster Nac

## Structure

`MxclusterNac`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `acct_server_port` | `int` | Optional | **Default**: `1813` |
| `auth_server_port` | `int` | Optional | **Default**: `1812` |
| `client_ips` | [`dict`](../../doc/models/client-ips.md) | Optional | - |
| `enabled` | `bool` | Optional | - |
| `secret` | `string` | Optional | - |

## Example (as JSON)

```json
{
  "acct_server_port": 1813,
  "auth_server_port": 1812,
  "secret": "testing123",
  "client_ips": {
    "key0": {
      "secret": "secret5",
      "site_id": "00002431-0000-0000-0000-000000000000",
      "vendor": "aruba"
    },
    "key1": {
      "secret": "secret4",
      "site_id": "00002432-0000-0000-0000-000000000000",
      "vendor": "paloalto"
    },
    "key2": {
      "secret": "secret3",
      "site_id": "00002433-0000-0000-0000-000000000000",
      "vendor": "cisco-aironet"
    }
  },
  "enabled": false
}
```

