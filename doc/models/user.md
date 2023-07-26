
# User

## Structure

`User`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `authentication_password` | `string` | Optional | Not required if `authentication_type`==`authentication-none`<br>include alphabetic, numeric, and special characters, but it cannot include control characters.<br>**Constraints**: *Minimum Length*: `7` |
| `authentication_type` | [`AuthenticationTypeEnum`](../../doc/models/authentication-type-enum.md) | Optional | sha224, sha256, sha384, sha512 are supported in 21.1 and newer release |
| `encryption_password` | `string` | Optional | Not required if `encryption_type`==`privacy-none`<br>include alphabetic, numeric, and special characters, but it cannot include control characters<br>**Constraints**: *Minimum Length*: `8` |
| `encryption_type` | [`EncryptionTypeEnum`](../../doc/models/encryption-type-enum.md) | Optional | - |
| `name` | `string` | Optional | - |

## Example (as JSON)

```json
{
  "authentication_password": "authentication_password4",
  "authentication_type": "authentication-sha512",
  "encryption_password": "encryption_password8",
  "encryption_type": "privacy-3des",
  "name": "name0"
}
```

