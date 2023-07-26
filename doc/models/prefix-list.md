
# Prefix List

## Structure

`PrefixList`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `context_prefix` | `string` | Optional | only required if `type`==`context_prefix` |
| `notify_view` | `string` | Optional | refer to view name |
| `read_view` | `string` | Optional | refer to view name |
| `security_level` | [`SecurityLevelEnum`](../../doc/models/security-level-enum.md) | Optional | - |
| `security_model` | [`SecurityModel1Enum`](../../doc/models/security-model-1-enum.md) | Optional | - |
| `mtype` | [`Type27Enum`](../../doc/models/type-27-enum.md) | Optional | - |
| `write_view` | `string` | Optional | refer to view name |

## Example (as JSON)

```json
{
  "context_prefix": "iil",
  "notify_view": "all",
  "read_view": "all",
  "write_view": "all",
  "security_level": "privacy",
  "security_model": "v1"
}
```

