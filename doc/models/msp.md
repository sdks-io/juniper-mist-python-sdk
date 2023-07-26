
# Msp

## Structure

`Msp`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `allow_mist` | `bool` | Optional | - |
| `created_time` | `int` | Optional | - |
| `id` | `uuid\|string` | Optional | - |
| `logo_url` | `string` | Optional | For advanced tier (uMSPs) only |
| `name` | `string` | Optional | - |
| `tier` | [`TierEnum`](../../doc/models/tier-enum.md) | Optional | **Default**: `'base'` |
| `url` | `string` | Optional | For advanced tier (uMSPs) only |

## Example (as JSON)

```json
{
  "tier": "base",
  "allow_mist": false,
  "created_time": 118,
  "id": "00001770-0000-0000-0000-000000000000",
  "logo_url": "logo_url0",
  "name": "name0"
}
```

