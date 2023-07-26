
# Delivery

Delivery object to configure the alarm delivery

## Structure

`Delivery`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `additional_emails` | `List of string` | Optional | List of additional email string to deliver the alarms via emails |
| `enabled` | `bool` | Required | Whether to enable the alarm delivery via emails or not |
| `to_org_admins` | `bool` | Optional | Whether to deliver the alarms via emails to Org admins or not |
| `to_site_admins` | `bool` | Optional | Whether to deliver the alarms via emails to Site admins or not |

## Example (as JSON)

```json
{
  "additional_emails": [
    "additional_emails7"
  ],
  "enabled": false,
  "to_org_admins": false,
  "to_site_admins": false
}
```

