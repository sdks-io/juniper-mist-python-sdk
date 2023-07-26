
# Spec

## Structure

`Spec`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `port_range` | `int` | Optional | matched dst port, "0" means any<br>**Default**: `0` |
| `protocol` | `string` | Optional | `tcp` / `udp` / `icmp` / `gre` / `any` / `:protocol_number`. `protocol_number` is between 1-254<br>**Default**: `'any'` |

## Example (as JSON)

```json
{
  "port_range": 0,
  "protocol": "any"
}
```

