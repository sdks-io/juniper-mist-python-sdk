
# Psk

PSK

## Structure

`Psk`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `admin_sso_id` | `string` | Optional | sso id for psk created from psk portal |
| `created_time` | `float` | Optional | - |
| `email` | `string` | Optional | email to send psk expiring notifications to |
| `expire_time` | `int` | Optional | Expire time for this PSK key (epoch time in seconds). Default `null` (as no expiration) |
| `expiry_notification_time` | `int` | Optional | Number of days before psk is expired. Used as to when to start sending reminder notification when the psk is about to expire |
| `id` | `uuid\|string` | Optional | - |
| `mac` | `string` | Optional | if `usage`==`single`, the mac that this PSK ties to, empty if `auto-binding` |
| `max_usage` | `int` | Optional | For Org PSK Only. Max concurrent users for this PSK key. Default is 0 (unlimited)<br>**Default**: `0` |
| `modified_time` | `float` | Optional | - |
| `name` | `string` | Required | - |
| `note` | `string` | Optional | - |
| `notify_expiry` | `bool` | Optional | If set to true, reminder notification will be sent when psk is about to expire<br>**Default**: `False` |
| `notify_on_create_or_edit` | `bool` | Optional | If set to true, notification will be sent when psk is created or edited |
| `old_passphrase` | `string` | Optional | previous passphrase of the PSK if it has been rotated |
| `org_id` | `uuid\|string` | Optional | - |
| `passphrase` | `string` | Required | passphrase of the PSK (8-63 character or 64 in hex)<br>**Constraints**: *Minimum Length*: `8`, *Maximum Length*: `64` |
| `role` | `string` | Optional | **Constraints**: *Minimum Length*: `0`, *Maximum Length*: `32` |
| `site_id` | `uuid\|string` | Optional | - |
| `ssid` | `string` | Required | SSID this PSK should be applicable to |
| `usage` | [`Usage2Enum`](../../doc/models/usage-2-enum.md) | Optional | **Default**: `'multi'` |
| `vlan_id` | `int` | Optional | VLAN for this PSK key |

## Example (as JSON)

```json
{
  "expire_time": 1614990263,
  "max_usage": 0,
  "name": "name0",
  "notify_expiry": false,
  "passphrase": "passphrase0",
  "ssid": "ssid2",
  "usage": "multi",
  "admin_sso_id": "admin_sso_id4",
  "created_time": 198.3,
  "email": "email6",
  "expiry_notification_time": 20
}
```

