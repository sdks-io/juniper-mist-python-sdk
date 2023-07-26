
# Rules 2

## Structure

`Rules2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `equals` | `string` | Optional | - |
| `equals_any` | `List of string` | Optional | use `equals_any` to match any item in a list |
| `expression` | `string` | Optional | "[0:3]":"abcdef" -> "abc"<br>"split(.)[1]": "a.b.c" -> "b"<br>"split(-)[1][0:3]: "a1234-b5678-c90" -> "b56" |
| `src` | [`SrcEnum`](../../doc/models/src-enum.md) | Required | - |
| `usage` | `string` | Optional | `port_usage` name |

## Example (as JSON)

```json
{
  "equals": "equals0",
  "equals_any": [
    "equals_any1",
    "equals_any2",
    "equals_any3"
  ],
  "expression": "expression2",
  "src": "lldp_manufacturer_name",
  "usage": "usage8"
}
```

