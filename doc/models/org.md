
# Org

An organization usualy represents a customer - which has inventories, licenses. An Organization can contain multiple sites. A site usually represents a deployment at the same location (a campus, an office).

## Structure

`Org`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `alarmtemplate_id` | `uuid\|string` | Optional | - |
| `allow_mist` | `bool` | Optional | **Default**: `True` |
| `created_time` | `float` | Optional | - |
| `id` | `uuid\|string` | Optional | - |
| `modified_time` | `float` | Optional | - |
| `msp_id` | `uuid\|string` | Optional | - |
| `name` | `string` | Required | - |
| `orggroup_ids` | `List of uuid\|string` | Optional | - |
| `session_expiry` | `float` | Optional | **Default**: `1440` |

## Example (as JSON)

```json
{
  "allow_mist": true,
  "name": "name0",
  "session_expiry": 1440,
  "alarmtemplate_id": "00001a0e-0000-0000-0000-000000000000",
  "created_time": 198.3,
  "id": "00001770-0000-0000-0000-000000000000",
  "modified_time": 136.66
}
```

