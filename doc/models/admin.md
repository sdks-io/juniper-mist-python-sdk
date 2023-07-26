
# Admin

Admin

## Structure

`Admin`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `admin_id` | `uuid\|string` | Optional | - |
| `email` | `string` | Required | - |
| `enable_two_factor` | `bool` | Optional | - |
| `first_name` | `string` | Required | for an invite, this is the original first name used |
| `hours` | `int` | Optional | how long the invite should be valid<br>**Default**: `24`<br>**Constraints**: `>= 1`, `<= 168` |
| `last_name` | `string` | Required | for an invite, this is the original last name used |
| `oauth_google` | `bool` | Optional | - |
| `phone` | `string` | Optional | phone number (numbers only, including country code) |
| `phone_2` | `string` | Optional | secondary phone number (numbers only, including country code) |
| `privileges` | [`List of Privileges`](../../doc/models/privileges.md) | Optional | list of privileges the admin has on the MSP / Orgs / OrgGroups<br>**Constraints**: *Minimum Items*: `1`, *Unique Items Required* |
| `session_expiry` | `int` | Optional | - |
| `tags` | `List of string` | Optional | - |
| `two_factor_verified` | `bool` | Optional | two factor status |
| `via_sso` | `string` | Optional | an admin alogin via_sso is more restircted. (password and email cannot be changed) |

## Example (as JSON)

```json
{
  "email": "email6",
  "first_name": "first_name0",
  "hours": 24,
  "last_name": "last_name8",
  "admin_id": "00001ada-0000-0000-0000-000000000000",
  "enable_two_factor": false,
  "oauth_google": false,
  "phone": "phone0"
}
```

