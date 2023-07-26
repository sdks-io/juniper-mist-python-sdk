
# Org Auto Rules

auto_rules in org settings

## Structure

`OrgAutoRules`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `expression` | `string` | Optional | "[0:3]"            // "abcdef" -> "abc"<br>"split(.)[1]"      // "a.b.c" -> "b"<br>"split(-)[1][0:3]" // "a1234-b5678-c90" -> "b56" |
| `model` | `string` | Optional | - |
| `prefix` | `string` | Optional | - |
| `src` | [`Src1Enum`](../../doc/models/src-1-enum.md) | Required | - |
| `subnet` | `string` | Optional | - |
| `suffix` | `string` | Optional | - |
| `value` | `string` | Optional | - |

## Example (as JSON)

```json
{
  "expression": "split(.)[1]",
  "prefix": "XX-",
  "src": "model",
  "suffix": "-YY",
  "model": "model2",
  "subnet": "subnet8"
}
```

