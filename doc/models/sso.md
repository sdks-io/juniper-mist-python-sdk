
# Sso

SSO

## Structure

`Sso`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `created_time` | `float` | Optional | - |
| `custom_logout_url` | `string` | Optional | optional, a URL we will redirect the user after user logout from Mist (for some IdP which supports a custom logout URL that is different from SP-initiated SLO process) |
| `default_role` | `string` | Optional | default role to assign if there’s no match. By default, an assertion is treated as invalid when there’s no role matched |
| `domain` | `string` | Optional | - |
| `id` | `uuid\|string` | Optional | - |
| `idp_cert` | `string` | Optional | if `idp_type`==`saml`. IDP Cert (used to verify the signed response) |
| `idp_sign_algo` | `string` | Optional | if `idp_type`==`saml`. Signing algorithm for SAML Assertion |
| `idp_sso_url` | `string` | Optional | IDP Single-Sign-On URL |
| `idp_type` | [`IdpTypeEnum`](../../doc/models/idp-type-enum.md) | Optional | **Default**: `'saml'` |
| `ignore_unmatched_roles` | `bool` | Optional | ignore any unmatched roles provided in assertion. By default, an assertion is treated as invalid for any unmatched role |
| `issuer` | `string` | Optional | if `idp_type`==`saml`. IDP issuer URL |
| `ldap_base_dn` | `string` | Optional | if `idp_type`==`ldap` |
| `ldap_bind_dn` | `string` | Optional | if `idp_type`==`ldap` |
| `ldap_bind_password` | `string` | Optional | if `idp_type`==`ldap` |
| `ldap_certs` | `List of string` | Optional | if `idp_type`==`ldap` |
| `ldap_client_cert` | `string` | Optional | if `idp_type`==`ldap` |
| `ldap_client_key` | `string` | Optional | if `idp_type`==`ldap` |
| `ldap_group_attr` | `string` | Optional | Only if `ldap_type`==`custom` |
| `ldap_group_dn` | `string` | Optional | Only if `ldap_type`==`custom` |
| `ldap_group_filter` | `string` | Optional | Only if `ldap_type`==`custom` |
| `ldap_server_hosts` | `List of string` | Optional | if `idp_type`==`ldap` |
| `ldap_type` | [`LdapTypeEnum`](../../doc/models/ldap-type-enum.md) | Optional | if `idp_type`==`ldap`<br>**Default**: `'azure'` |
| `ldap_user_filter` | `string` | Optional | Only if `ldap_type`==`custom` |
| `modified_time` | `float` | Optional | - |
| `msp_id` | `uuid\|string` | Optional | - |
| `name` | `string` | Required | name |
| `nameid_format` | [`NameidFormatEnum`](../../doc/models/nameid-format-enum.md) | Optional | if `idp_type`==`saml`<br>**Default**: `'email'` |
| `oauth_cc_client_id` | `string` | Optional | if `oauth_type`==`okta`, Client Credentials |
| `oauth_cc_client_secret` | `string` | Optional | if `oauth_type`==`okta`, oauth_cc_client_secret is RSA private key, of the form "-----BEGIN RSA PRIVATE KEY--...." |
| `oauth_discovery_url` | `string` | Optional | if `idp_type`==`oauth` |
| `oauth_ropc_client_id` | `string` | Optional | ropc = Resource Owner Password Credentials |
| `oauth_ropc_secret` | `string` | Optional | oauth_ropc_client_secret can be empty if oauth_type is azure |
| `oauth_tenant_id` | `string` | Optional | if `oauth_type`==`okta`, oauth_tenant_id |
| `oauth_type` | [`OauthTypeEnum`](../../doc/models/oauth-type-enum.md) | Optional | **Default**: `'azure'` |
| `org_id` | `uuid\|string` | Optional | - |
| `role_attr_extraction` | `string` | Optional | optional, custom role attribute parsing scheme<br><br>Supported Role Parsing Schemes<br><br><table><tr><th>Name</th><th>Scheme</th></tr><tr><td>cn</td><td><ul><li>The expected role attribute format in SAML Assertion is “CN=cn,OU=ou1,OU=ou2,…”</li><li>CN (the key) is case insensitive and exactly 1 CN is expected (or the entire entry will be ignored)</li><li>E.g. if role attribute is “CN=cn,OU=ou1,OU=ou2” then parsed role value is “cn”</li></ul></td></tr></table><br> |
| `role_attr_from` | `string` | Optional | name of the attribute in SAML Assertion to extract role from<br>**Default**: `'role'` |
| `site_id` | `uuid\|string` | Optional | - |
| `mtype` | `string` | Optional | - |

## Example (as JSON)

```json
{
  "idp_type": "saml",
  "ldap_type": "azure",
  "name": "name0",
  "nameid_format": "email",
  "oauth_cc_client_id": "e60da615-7def-4c5a-8196-43675f45e174",
  "oauth_cc_client_secret": "akL8Q~5kWFMVFYl4TFZ3fi~7cMdyDONi6cj01cpH",
  "oauth_ropc_client_id": "9ce04c97-b5b1-4ec8-af17-f5ed42d2daf7",
  "oauth_ropc_secret": "blM9R~6kWFMVFYl4TFZ3fi~8cMdyDONi6cj01dqI",
  "oauth_tenant_id": "dev-88336535",
  "oauth_type": "azure",
  "role_attr_from": "role",
  "created_time": 198.3,
  "custom_logout_url": "custom_logout_url6",
  "default_role": "default_role2",
  "domain": "domain6",
  "id": "00001770-0000-0000-0000-000000000000"
}
```

