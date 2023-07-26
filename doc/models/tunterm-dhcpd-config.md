
# Tunterm Dhcpd Config

DHCP server/relay configuration of Mist Tunneled VLANs. The property key is the VLAN ID

## Structure

`TuntermDhcpdConfig`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `enabled` | `bool` | Optional | **Default**: `False` |
| `servers` | `List of string` | Optional | - |
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

