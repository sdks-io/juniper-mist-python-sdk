
# Wlan Portal

portal wlan settings

## Structure

`WlanPortal`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `allow_wlan_id_roam` | `bool` | Optional | whether to allow guest roam between different wlan_ids (same ssid). requires cross_site enabled<br>**Default**: `False` |
| `amazon_client_id` | `string` | Optional | amazon OAuth2 client id. This is optional. If not provided, it will use a default one. |
| `amazon_client_secret` | `string` | Optional | amazon OAuth2 client secret. If amazon_client_id was provided, provide a correspoinding value. Else leave blank. |
| `amazon_email_domains` | `List of string` | Optional | Matches authenticated user email against provided domains. If null or [], all authenticated emails will be allowed. |
| `amazon_enabled` | `bool` | Optional | whether amazon is enabled as a login method |
| `auth` | [`Auth2Enum`](../../doc/models/auth-2-enum.md) | Optional | authentication scheme<br>**Default**: `'none'` |
| `azure_client_id` | `string` | Optional | azure active directory app client id |
| `azure_client_secret` | `string` | Optional | azure active directory app client secret |
| `azure_enabled` | `bool` | Optional | whether Azure Active Directory is enabled as a login method |
| `azure_tenant_id` | `string` | Optional | azure active directory tenant id. |
| `broadnet_password` | `string` | Optional | when `sms_provider`==`broadnet` |
| `broadnet_sid` | `string` | Optional | when `sms_provider`==`broadnet` |
| `broadnet_user_id` | `string` | Optional | when `sms_provider`==`broadnet` |
| `bypass_when_cloud_down` | `bool` | Optional | whether to bypass the guest portal when cloud not reachable (and apply the default policies)<br>**Default**: `False` |
| `clickatell_api_key` | `string` | Optional | when `sms_provider`==`clickatell` |
| `cross_site` | `bool` | Optional | whether to allow guest to roam between sites of same org without reauthentication<br>**Default**: `False` |
| `email_enabled` | `bool` | Optional | whether email (access code verification) is enabled as a login method |
| `enabled` | `bool` | Optional | whether guest portal is enabled<br>**Default**: `False` |
| `expire` | `float` | Optional | how long to remain authorized, in minutes<br>**Default**: `1440` |
| `external_portal_url` | `string` | Optional | external portal URL (e.g. https://host/url) where we can append our query parameters to |
| `facebook_client_id` | `string` | Optional | facebook OAuth2 app id. This is optional. If not provided, it will use a default one. |
| `facebook_client_secret` | `string` | Optional | facebook OAuth2 app secret. If facebook_client_id was provided, provide a correspoinding value. Else leave blank. |
| `facebook_email_domains` | `List of string` | Optional | Matches authenticated user email against provided domains. If null or [], all authenticated emails will be allowed. |
| `facebook_enabled` | `bool` | Optional | whether facebook is enabled as a login method |
| `forward` | `bool` | Optional | whether to forward the user to another URL after authorized<br>**Default**: `False` |
| `forward_url` | `string` | Optional | the URL to forward the user to |
| `google_client_id` | `string` | Optional | Google OAuth2 app id. This is optional. If not provided, it will use a default one. |
| `google_client_secret` | `string` | Optional | Google OAuth2 app secret. If google_client_id was provided, provide a correspoinding value. Else leave blank. |
| `google_email_domains` | `List of string` | Optional | Matches authenticated user email against provided domains. If null or [], all authenticated emails will be allowed. |
| `google_enabled` | `bool` | Optional | whether google is enabled as login method |
| `gupshup_password` | `string` | Optional | when `sms_provider`==`gupshup` |
| `gupshup_userid` | `string` | Optional | when `sms_provider`==`gupshup` |
| `microsoft_client_id` | `string` | Optional | microsoft 365 OAuth2 client id. This is optional. If not provided, it will use a default one. |
| `microsoft_client_secret` | `string` | Optional | microsoft 365 OAuth2 client secret. If microsoft_client_id was provided, provide a correspoinding value. Else leave blank. |
| `microsoft_email_domains` | `List of string` | Optional | Matches authenticated user email against provided domains. If null or [], all authenticated emails will be allowed. |
| `microsoft_enabled` | `bool` | Optional | whether microsoft 365 is enabled as a login method |
| `passphrase_enabled` | `bool` | Optional | whether password is enabled |
| `password` | `string` | Optional | passphrase |
| `portal_allowed_hostnames` | `string` | Optional | list of hostnames without http(s):// (matched by substring) |
| `portal_allowed_subnets` | `string` | Optional | list of CIDRs |
| `portal_api_secret` | `string` | Optional | api secret (auto-generated) that can be used to sign guest authorization requests |
| `portal_denied_hostnames` | `string` | Optional | list of hostnames without http(s):// (matched by substring), this takes precedence over portal_allowed_hostnames |
| `portal_image` | `string` | Optional | Url of portal background image |
| `portal_sso_url` | `string` | Optional | for SAML, this is used as the ACS URL |
| `predefined_sponsors_enabled` | `bool` | Optional | whether to show list of sponsor emails mentioned in `sponsors` object as a dropdown. If both `sponsor_notify_all` and `predefined_sponsors_enabled` are false, behaviour is acc to `sponsor_email_domains`<br>**Default**: `True` |
| `privacy` | `bool` | Optional | - |
| `puzzel_password` | `string` | Optional | when `sms_provider`==`puzzel` |
| `puzzel_service_id` | `string` | Optional | when `sms_provider`==`puzzel` |
| `puzzel_username` | `string` | Optional | when `sms_provider`==`puzzel` |
| `sms_message_format` | `string` | Optional | - |
| `sms_enabled` | `bool` | Optional | whether sms is enabled as a login method |
| `sms_provider` | [`SmsProviderEnum`](../../doc/models/sms-provider-enum.md) | Optional | **Default**: `'manual'` |
| `sponsor_auto_approve` | `bool` | Optional | whether to automatically approve guest and allow sponsor to revoke guest access, needs predefined_sponsors_enabled enabled and sponsor_notify_all disabled<br>**Default**: `False` |
| `sponsor_email_domains` | `List of string` | Optional | list of domain allowed for sponsor email. Required if `sponsor_enabled` is `true` and `sponsors` is empty. |
| `sponsor_enabled` | `bool` | Optional | whether sponsor is enabled |
| `sponsor_link_validity_duration` | `string` | Optional | how long to remain valid sponsored guest request approve/deny link received in email, in minutes. |
| `sponsor_notify_all` | `bool` | Optional | whether to notify all sponsors that are mentioned in `sponsors` object. Both `sponsor_notify_all` and `predefined_sponsors_enabled` should be true in order to notify sponsors. If true, email sent to 10 sponsors in no particular order.<br>**Default**: `False` |
| `sponsor_status_notify` | `bool` | Optional | if enabled, guest will get email about sponsor's action (approve/deny)<br>**Default**: `False` |
| `sponsors` | `dict` | Optional | object of allowed sponsors email with name. Required if `sponsor_enabled` is `true` and `sponsor_email_domains` is empty. |
| `sso_default_role` | `string` | Optional | default role to assign if there’s no match. By default, an assertion is treated as invalid when there’s no role matched |
| `sso_forced_role` | `string` | Optional | - |
| `sso_idp_cert` | `string` | Optional | IDP Cert (used to verify the signed response) |
| `sso_idp_sign_algo` | `string` | Optional | signing algorithm for SAML Assertion |
| `sso_idp_sso_url` | `string` | Optional | IDP Single-Sign-On URL |
| `sso_issuer` | `string` | Optional | IDP issuer URL |
| `sso_nameid_format` | [`SsoNameidFormatEnum`](../../doc/models/sso-nameid-format-enum.md) | Optional | **Default**: `'email'` |
| `telstra_client_id` | `string` | Optional | when `sms_provider`==`telstra`, Client ID provided by Telstra |
| `telstra_client_secret` | `string` | Optional | when `sms_provider`==`telstra`, Client secret provided by Telstra |
| `thumbnail` | `string` | Optional | Url of portal background image thumbnail |
| `twilio_auth_token` | `string` | Optional | when `sms_provider`==`twilio`, Auth token account with twilio account |
| `twilio_phone_number` | `string` | Optional | when `sms_provider`==`twilio`, Twilio phone number associated with the account. See example for accepted format. |
| `twilio_sid` | `string` | Optional | when `sms_provider`==`twilio`, Account SID provided by Twilio |

## Example (as JSON)

```json
{
  "allow_wlan_id_roam": false,
  "auth": "none",
  "bypass_when_cloud_down": false,
  "cross_site": false,
  "enabled": false,
  "expire": 1440,
  "forward": false,
  "predefined_sponsors_enabled": true,
  "sms_provider": "manual",
  "sponsor_auto_approve": false,
  "sponsor_notify_all": false,
  "sponsor_status_notify": false,
  "sso_nameid_format": "email",
  "amazon_client_id": "amazon_client_id2",
  "amazon_client_secret": "amazon_client_secret8",
  "amazon_email_domains": [
    "amazon_email_domains2",
    "amazon_email_domains3",
    "amazon_email_domains4"
  ],
  "amazon_enabled": false
}
```

