
# Ipsec

## Structure

`Ipsec`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `dns_servers` | `List of string` | Optional | - |
| `dns_suffix` | `List of string` | Optional | - |
| `enabled` | `bool` | Optional | - |
| `extra_routes` | [`List of ExtraRoutes4`](../../doc/models/extra-routes-4.md) | Optional | - |
| `split_tunnel` | `bool` | Optional | - |
| `use_mxedge` | `bool` | Optional | - |

## Example (as JSON)

```json
{
  "dns_servers": [
    "dns_servers0"
  ],
  "dns_suffix": [
    "dns_suffix7"
  ],
  "enabled": false,
  "extra_routes": [
    {
      "dest": "dest3",
      "next_hop": "next_hop3"
    },
    {
      "dest": "dest4",
      "next_hop": "next_hop4"
    }
  ],
  "split_tunnel": false
}
```

