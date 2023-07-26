
# Target Parameter

## Structure

`TargetParameter`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `message_processing_model` | [`MessageProcessingModelEnum`](../../doc/models/message-processing-model-enum.md) | Optional | - |
| `name` | `string` | Optional | - |
| `notify_filter` | `string` | Optional | refer to profile-name in notify-filter |
| `security_level` | [`SecurityLevelEnum`](../../doc/models/security-level-enum.md) | Optional | - |
| `security_model` | [`SecurityModelEnum`](../../doc/models/security-model-enum.md) | Optional | - |
| `security_name` | `string` | Optional | refer to security_name in usm |

## Example (as JSON)

```json
{
  "security_name": "m01620",
  "message_processing_model": "v1",
  "name": "name0",
  "notify_filter": "notify_filter8",
  "security_level": "privacy",
  "security_model": "v2c"
}
```

