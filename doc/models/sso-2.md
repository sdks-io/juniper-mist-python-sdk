
# Sso 2

if `auth`==`sso`

## Structure

`Sso2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `allowed_roles` | `List of string` | Optional | // allowed roles for accessing psk portal, if none, any role is permitted |
| `idp_cert` | `string` | Optional | - |
| `idp_sign_algo` | `string` | Optional | - |
| `idp_sso_url` | `string` | Optional | - |
| `issuer` | `string` | Optional | - |
| `nameid_format` | `string` | Optional | - |
| `role_mapping` | `dict` | Optional | Property key is the role name, property value is the SSO Attribute |
| `use_sso_role_for_psk_role` | `bool` | Optional | if enabled, the `role` above will be ignored |

## Example (as JSON)

```json
{
  "allowed_roles": [
    "allowed_roles9",
    "allowed_roles0"
  ],
  "idp_cert": "idp_cert6",
  "idp_sign_algo": "idp_sign_algo6",
  "idp_sso_url": "idp_sso_url0",
  "issuer": "issuer0"
}
```

