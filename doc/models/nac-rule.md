
# Nac Rule

## Structure

`NacRule`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `action` | [`Action5Enum`](../../doc/models/action-5-enum.md) | Required | - |
| `apply_tags` | `List of string` | Optional | all optional, this goes into Access-Accept |
| `created_time` | `int` | Optional | - |
| `enabled` | `bool` | Optional | enabled or not<br>**Default**: `True` |
| `id` | `uuid\|string` | Optional | - |
| `matching` | [`NacRuleMatching`](../../doc/models/nac-rule-matching.md) | Optional | - |
| `modified_time` | `int` | Optional | - |
| `name` | `string` | Required | - |
| `not_matching` | [`NacRuleMatching`](../../doc/models/nac-rule-matching.md) | Optional | - |
| `order` | `float` | Optional | the order of the rule, lower value implies higher priority<br>**Constraints**: `>= 1` |
| `org_id` | `uuid\|string` | Optional | - |

## Example (as JSON)

```json
{
  "action": "allow",
  "apply_tags": [
    "c049dfcd-0c73-5014-1c64-062e9903f1e5\""
  ],
  "enabled": true,
  "name": "name0",
  "order": 1,
  "created_time": 118,
  "id": "00001770-0000-0000-0000-000000000000",
  "matching": {
    "auth_type": "psk",
    "nactags": [
      "nactags6"
    ],
    "port_types": [
      "wireless"
    ],
    "site_ids": [
      "00000738-0000-0000-0000-000000000000"
    ],
    "sitegroup_ids": [
      "00002472-0000-0000-0000-000000000000",
      "00002473-0000-0000-0000-000000000000",
      "00002474-0000-0000-0000-000000000000"
    ]
  }
}
```

