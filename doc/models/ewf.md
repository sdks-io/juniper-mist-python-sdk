
# Ewf

## Structure

`Ewf`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `alert_only` | `bool` | Optional | - |
| `block_message` | `string` | Optional | - |
| `enabled` | `bool` | Optional | **Default**: `False` |
| `profille` | [`ProfilleEnum`](../../doc/models/profille-enum.md) | Optional | **Default**: `'strict'` |

## Example (as JSON)

```json
{
  "block_message": "Access to this URL Category has been blocked",
  "enabled": false,
  "profille": "strict",
  "alert_only": false
}
```

