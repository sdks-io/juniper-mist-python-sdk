
# Service Policy

## Structure

`ServicePolicy`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `action` | [`Action1Enum`](../../doc/models/action-1-enum.md) | Required | **Default**: `'allow'`<br>**Constraints**: *Minimum Length*: `1` |
| `created_time` | `float` | Optional | - |
| `id` | `string` | Optional | - |
| `modified_time` | `float` | Optional | - |
| `name` | `string` | Required | - |
| `org_id` | `string` | Optional | - |
| `services` | `List of string` | Required | - |
| `tenants` | `List of string` | Required | - |

## Example (as JSON)

```json
{
  "action": "allow",
  "name": "name0",
  "services": [
    "services0",
    "services1"
  ],
  "tenants": [
    "tenants1",
    "tenants2"
  ],
  "created_time": 198.3,
  "id": "id0",
  "modified_time": 136.66,
  "org_id": "org_id4"
}
```

