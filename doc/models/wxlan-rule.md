
# Wxlan Rule

WXlan

## Structure

`WxlanRule`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `action` | [`Action7Enum`](../../doc/models/action-7-enum.md) | Optional | type of action, allow / block |
| `blocked_apps` | `List of string` | Optional | blocked apps (always blocking, ignoring action), the key of Get Application List |
| `created_time` | `float` | Optional | - |
| `dst_allow_wxtags` | `List of string` | Optional | tag list to indicate these tags are allowed access |
| `dst_deny_wxtags` | `List of string` | Optional | tag list to indicate these tags are blocked access |
| `enabled` | `bool` | Optional | **Default**: `True` |
| `for_site` | `bool` | Optional | - |
| `id` | `uuid\|string` | Optional | - |
| `modified_time` | `float` | Optional | - |
| `order` | `float` | Required | the order how rules would be looked up, > 0 and bigger order got matched first, -1 means LAST, uniqueness not checked |
| `org_id` | `uuid\|string` | Optional | - |
| `site_id` | `uuid\|string` | Optional | - |
| `src_wxtags` | `List of string` | Required | tag list to determine if this rule would match |

## Example (as JSON)

```json
{
  "enabled": true,
  "order": 228.16,
  "src_wxtags": [
    "src_wxtags6",
    "src_wxtags7",
    "src_wxtags8"
  ],
  "action": "allow",
  "blocked_apps": [
    "blocked_apps7",
    "blocked_apps8"
  ],
  "created_time": 198.3,
  "dst_allow_wxtags": [
    "dst_allow_wxtags1",
    "dst_allow_wxtags2"
  ],
  "dst_deny_wxtags": [
    "dst_deny_wxtags1",
    "dst_deny_wxtags2"
  ]
}
```

