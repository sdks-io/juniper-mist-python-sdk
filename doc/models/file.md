
# File

## Structure

`File`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `archive` | [`Archive`](../../doc/models/archive.md) | Optional | - |
| `contents` | [`List of Content2`](../../doc/models/content-2.md) | Optional | - |
| `explicit_priority` | `bool` | Optional | - |
| `file` | `string` | Optional | - |
| `match` | `string` | Optional | - |
| `structured_data` | `bool` | Optional | - |

## Example (as JSON)

```json
{
  "file": "file-name",
  "match": "!alarm|ntp|errors.crc_error[chan]",
  "archive": {
    "files": 122,
    "size": "size8"
  },
  "contents": [
    {
      "facility": "authorization",
      "severity": "warning"
    }
  ],
  "explicit_priority": false
}
```

