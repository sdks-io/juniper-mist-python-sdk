
# Dsl Config

if `wan_type`==`dsl`

## Structure

`DslConfig`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `ppoe_auth` | [`PpoeAuthEnum`](../../doc/models/ppoe-auth-enum.md) | Optional | **Default**: `'none'` |
| `ppoe_password` | `string` | Optional | - |
| `ppoe_username` | `string` | Optional | - |

## Example (as JSON)

```json
{
  "ppoe_auth": "none",
  "ppoe_password": "ppoe_password4",
  "ppoe_username": "ppoe_username4"
}
```

