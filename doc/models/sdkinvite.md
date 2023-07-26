
# Sdkinvite

SDK invite

## Structure

`Sdkinvite`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `created_time` | `float` | Optional | - |
| `enabled` | `bool` | Optional | **Default**: `True` |
| `expire_time` | `int` | Optional | - |
| `id` | `uuid\|string` | Optional | - |
| `modified_time` | `float` | Optional | - |
| `name` | `string` | Required | name, will show up in mobile |
| `org_id` | `uuid\|string` | Optional | - |
| `quota` | `int` | Optional | number of time this invite can be used |
| `quota_limited` | `bool` | Optional | whether quota limiting is enabled<br>**Default**: `False` |
| `site_id` | `uuid\|string` | Optional | - |

## Example (as JSON)

```json
{
  "enabled": true,
  "name": "name0",
  "quota_limited": false,
  "created_time": 198.3,
  "expire_time": 72,
  "id": "00001770-0000-0000-0000-000000000000",
  "modified_time": 136.66
}
```

