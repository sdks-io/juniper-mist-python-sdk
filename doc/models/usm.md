
# Usm

## Structure

`Usm`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `engine_id` | `string` | Optional | required only if `engine_type`==`remote_engine` |
| `engine_type` | [`EngineTypeEnum`](../../doc/models/engine-type-enum.md) | Optional | - |
| `users` | [`List of User`](../../doc/models/user.md) | Optional | - |

## Example (as JSON)

```json
{
  "engine-id": "00:00:00:0b:00:00:70:10:6f:08:b6:3f",
  "engine_type": "remote_engine",
  "users": [
    {
      "authentication_password": "authentication_password7",
      "authentication_type": "authentication-sha512",
      "encryption_password": "encryption_password1",
      "encryption_type": "privacy-none",
      "name": "name3"
    },
    {
      "authentication_password": "authentication_password8",
      "authentication_type": "authentication-none",
      "encryption_password": "encryption_password2",
      "encryption_type": "privacy-aes128",
      "name": "name4"
    }
  ]
}
```

