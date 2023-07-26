
# Dns Server Rewrite

for radius_group-based DNS server (rewrite DNS request depending on the Group RADIUS server returns)

## Structure

`DnsServerRewrite`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `enabled` | `bool` | Optional | - |
| `radius_groups` | `object` | Optional | map between radius_group and the desired DNS server (IPv4 only) |

## Example (as JSON)

```json
{
  "enabled": false,
  "radius_groups": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

