
# Api V1 Const Alarm Defs Response

## Structure

`ApiV1ConstAlarmDefsResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `display` | `string` | Required | Description of the alarm type |
| `fields` | `List of string` | Required | List of fields available in an alarm details payload (in REST APIs & Webhooks); e.g. `aps`, `switches`, `gateways`, `hostnames`, `ssids`, `bssids` |
| `group` | `string` | Required | Group to which the alarm belongs |
| `key` | `string` | Required | Key name of an alarm type |
| `marvis_suggestion_category` | `string` | Optional | Marvis defined category to which the alarm belongs |
| `severity` | `string` | Required | Severity of the alarm |

## Example (as JSON)

```json
{
  "display": "display8",
  "fields": [
    "fields2",
    "fields3"
  ],
  "group": "group8",
  "key": "key0",
  "marvis_suggestion_category": "marvis_suggestion_category0",
  "severity": "severity0"
}
```

