
# User 1

## Structure

`User1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `contents` | [`List of Content2`](../../doc/models/content-2.md) | Optional | - |
| `match` | `string` | Optional | - |
| `user` | `string` | Optional | - |

## Example (as JSON)

```json
{
  "match": "\"!alarm|ntp|errors.crc_error[chan]\"",
  "user": "*",
  "contents": [
    {
      "facility": "authorization",
      "severity": "warning"
    }
  ]
}
```

