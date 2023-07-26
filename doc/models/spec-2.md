
# Spec 2

## Structure

`Spec2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `port_range` | `string` | Optional | matched dst port, "0" means any<br>**Default**: `'0'` |
| `protocol` | `string` | Optional | tcp / udp / icmp / gre / any / ":protocol_number", `protocol_number` is between 1-254<br>**Default**: `'any'` |
| `subnets` | `List of string` | Optional | matched dst subnet |

## Example (as JSON)

```json
{
  "port_range": "0",
  "protocol": "any",
  "subnets": [
    "subnets7",
    "subnets8",
    "subnets9"
  ]
}
```

