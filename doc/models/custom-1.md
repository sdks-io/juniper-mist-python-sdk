
# Custom 1

## Structure

`Custom1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `port_range` | `string` | Optional | matched dst port, `0` means any<br>**Constraints**: *Minimum Length*: `0`, *Maximum Length*: `6553` |
| `protocol` | [`ProtocolEnum`](../../doc/models/protocol-enum.md) | Optional | **Default**: `'any'` |
| `subnets` | `List of string` | Optional | - |

## Example (as JSON)

```json
{
  "protocol": "any",
  "port_range": "port_range0",
  "subnets": [
    "subnets7",
    "subnets8",
    "subnets9"
  ]
}
```

