
# Psk Portal

## Structure

`PskPortal`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `auth` | [`Auth1Enum`](../../doc/models/auth-1-enum.md) | Optional | Note: `sponsor` not yet available<br>**Default**: `'sso'` |
| `bg_image_url` | `string` | Optional | - |
| `cleanup_psk` | `bool` | Optional | used to cleanup exited psk when portal delete or ssid changed<br>**Default**: `False` |
| `created_time` | `int` | Optional | - |
| `expire_time` | `int` | Optional | unit min |
| `expiry_notification_time` | `int` | Optional | Number of days before psk is expired. Used as to when to start sending reminder notification when the psk is about to expire |
| `hide_psks_created_by_other_admins` | `bool` | Optional | only if `type`==`admin`<br>**Default**: `False` |
| `id` | `string` | Optional | - |
| `max_usage` | `int` | Optional | `max_usage`==`0` means unlimited<br>**Default**: `0` |
| `modified_time` | `int` | Optional | - |
| `name` | `string` | Required | - |
| `notify_expiry` | `bool` | Optional | If set to true, reminder notification will be sent when psk is about to expire |
| `notify_on_create_or_edit` | `bool` | Optional | **Default**: `False` |
| `org_id` | `string` | Optional | - |
| `passphrase_rules` | [`PassphraseRules`](../../doc/models/passphrase-rules.md) | Optional | - |
| `required_fields` | `List of string` | Optional | what information to ask for (email is required by default) |
| `role` | `string` | Optional | - |
| `ssid` | `string` | Required | intended SSID |
| `sso` | [`Sso2`](../../doc/models/sso-2.md) | Optional | if `auth`==`sso` |
| `template_url` | `string` | Optional | UI customization |
| `thumbnail_url` | `string` | Optional | - |
| `mtype` | [`Type35Enum`](../../doc/models/type-35-enum.md) | Optional | for personal psk portal |
| `vlan_id` | `int` | Optional | - |

## Example (as JSON)

```json
{
  "auth": "sso",
  "cleanup_psk": false,
  "hide_psks_created_by_other_admins": false,
  "max_usage": 0,
  "name": "name0",
  "notify_on_create_or_edit": false,
  "ssid": "ssid2",
  "bg_image_url": "bg_image_url8",
  "created_time": 118,
  "expire_time": 72
}
```

