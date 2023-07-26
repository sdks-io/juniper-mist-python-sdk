
# Upgrade Status

## Structure

`UpgradeStatus`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `status` | [`Status7Enum`](../../doc/models/status-7-enum.md) | Required | - |
| `status_id` | `int` | Required | the internal status id |
| `timestamp` | `float` | Required | timestamp |

## Example (as JSON)

```json
{
  "status": "error",
  "status_id": 72,
  "timestamp": 128.82
}
```

