
# Comment

## Structure

`Comment`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `attachments` | [`List of Attachment`](../../doc/models/attachment.md) | Optional | - |
| `author` | `string` | Required | - |
| `comment` | `string` | Required | - |
| `created_at` | `int` | Required | - |

## Example (as JSON)

```json
{
  "attachments": [
    {
      "content_type": "content_type4",
      "content_url": "content_url4",
      "size": 124
    },
    {
      "content_type": "content_type5",
      "content_url": "content_url5",
      "size": 125
    },
    {
      "content_type": "content_type6",
      "content_url": "content_url6",
      "size": 126
    }
  ],
  "author": "author0",
  "comment": "comment6",
  "created_at": 6
}
```

