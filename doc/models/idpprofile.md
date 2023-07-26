
# Idpprofile

## Structure

`Idpprofile`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `base_profile` | [`BaseProfileEnum`](../../doc/models/base-profile-enum.md) | Optional | - |
| `created_time` | `int` | Optional | - |
| `id` | `uuid\|string` | Optional | - |
| `modified_time` | `int` | Optional | - |
| `name` | `string` | Optional | - |
| `overwrites` | [`List of Overwrite`](../../doc/models/overwrite.md) | Optional | - |

## Example (as JSON)

```json
{
  "base_profile": "strict",
  "id": "874ca978-d736-4d4b-bc90-a49a29eec133",
  "name": "relaxed",
  "created_time": 118,
  "modified_time": 98
}
```

