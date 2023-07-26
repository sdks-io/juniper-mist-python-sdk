
# Apitoken

API Token

## Structure

`Apitoken`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `created_by` | `string` | Optional | for Org token only. email of the token creator / null if creator is deleted |
| `created_time` | `int` | Optional | - |
| `id` | `uuid\|string` | Optional | - |
| `key` | `string` | Optional | - |
| `last_used` | `int` | Optional | - |
| `name` | `string` | Optional | name of the token |
| `org_id` | `uuid\|string` | Optional | - |
| `privileges` | [`List of Privileges`](../../doc/models/privileges.md) | Optional | list of privileges the token has on the orgs/sites<br>**Constraints**: *Minimum Items*: `1`, *Unique Items Required* |

## Example (as JSON)

```json
{
  "created_by": "created_by2",
  "created_time": 118,
  "id": "00001770-0000-0000-0000-000000000000",
  "key": "key0",
  "last_used": 82
}
```

