
# Tunterm Dhcpd Config 1

global and per-VLAN. The property key is the VLAN ID

## Structure

`TuntermDhcpdConfig1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `enabled` | `bool` | Optional | **Default**: `False` |
| `servers` | `List of string` | Optional | list of DHCP servers; required if `type`==`relay` |
| `mtype` | [`Type31Enum`](../../doc/models/type-31-enum.md) | Optional | **Default**: `'relay'` |

## Example (as JSON)

```json
{
  "enabled": false,
  "type": "relay",
  "servers": [
    "servers3",
    "servers4"
  ]
}
```

