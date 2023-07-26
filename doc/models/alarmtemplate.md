
# Alarmtemplate

Alarm Template

## Structure

`Alarmtemplate`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `created_time` | `float` | Optional | - |
| `delivery` | [`Delivery`](../../doc/models/delivery.md) | Required | Delivery object to configure the alarm delivery |
| `id` | `uuid\|string` | Optional | - |
| `modified_time` | `float` | Optional | - |
| `name` | `string` | Optional | Some string to name the alarm template |
| `org_id` | `uuid\|string` | Optional | - |
| `rules` | [`dict`](../../doc/models/rules.md) | Required | Alarm Rules object to configure the individual alarm keys/types. Property key is the alarm name. |

## Example (as JSON)

```json
{
  "created_time": 198.3,
  "delivery": {
    "additional_emails": [
      "additional_emails9",
      "additional_emails0",
      "additional_emails1"
    ],
    "enabled": false,
    "to_org_admins": false,
    "to_site_admins": false
  },
  "id": "00001770-0000-0000-0000-000000000000",
  "modified_time": 136.66,
  "name": "name0",
  "org_id": "00000ec8-0000-0000-0000-000000000000",
  "rules": {
    "key0": {
      "delivery": {
        "additional_emails": [
          "additional_emails3",
          "additional_emails4",
          "additional_emails5"
        ],
        "enabled": false,
        "to_org_admins": false,
        "to_site_admins": false
      },
      "enabled": false
    }
  }
}
```

