
# Api V1 Register Request

## Structure

`ApiV1RegisterRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_only` | `bool` | Optional | skip creating initial setup if true<br>**Default**: `False` |
| `allow_mist` | `bool` | Optional | whether to allow Mist to look at this org<br>**Default**: `False` |
| `email` | `string` | Required | - |
| `first_name` | `string` | Required | - |
| `invite_code` | `string` | Optional | required initially |
| `last_name` | `string` | Required | - |
| `org_name` | `string` | Required | - |
| `password` | `string` | Required | - |
| `recaptcha` | `string` | Required | - |
| `referer_invite_token` | `string` | Optional | the invite token to apply after account creation |
| `return_to` | `string` | Optional | the url the user should be redirected back to |

## Example (as JSON)

```json
{
  "account_only": false,
  "allow_mist": false,
  "email": "email6",
  "first_name": "first_name0",
  "last_name": "last_name8",
  "org_name": "org_name0",
  "password": "password4",
  "recaptcha": "recaptcha4",
  "invite_code": "invite_code8",
  "referer_invite_token": "referer_invite_token4",
  "return_to": "return_to6"
}
```

