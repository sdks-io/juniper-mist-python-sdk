
# Api V1 Sites Alarms Unack Request

## Structure

`ApiV1SitesAlarmsUnackRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `alarm_ids` | `List of uuid\|string` | Required | - |
| `note` | `string` | Optional | Some text note describing the intent |

## Example (as JSON)

```json
{
  "alarm_ids": [
    "000019f8-0000-0000-0000-000000000000",
    "000019f9-0000-0000-0000-000000000000"
  ],
  "note": "note4"
}
```

