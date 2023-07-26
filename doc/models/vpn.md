
# Vpn

## Structure

`Vpn`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `created_time` | `int` | Optional | - |
| `id` | `uuid\|string` | Optional | - |
| `modified_time` | `int` | Optional | - |
| `name` | `string` | Required | **Constraints**: *Minimum Length*: `1` |
| `org_id` | `uuid\|string` | Optional | - |
| `paths` | [`dict`](../../doc/models/paths-1.md) | Required | - |

## Example (as JSON)

```json
{
  "created_time": 118,
  "id": "00001770-0000-0000-0000-000000000000",
  "modified_time": 98,
  "name": "name0",
  "org_id": "00000ec8-0000-0000-0000-000000000000",
  "paths": {
    "key0": {
      "bfd_profile": "broadband",
      "ip": "ip1"
    }
  }
}
```

