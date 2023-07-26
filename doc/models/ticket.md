
# Ticket

Support Ticket

## Structure

`Ticket`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `case_number` | `string` | Optional | - |
| `comments` | [`List of Comment`](../../doc/models/comment.md) | Optional | - |
| `created_at` | `int` | Optional | - |
| `id` | `uuid\|string` | Optional | - |
| `requester` | `string` | Optional | - |
| `requester_email` | `string` | Optional | email of the requester |
| `status` | [`Status5Enum`](../../doc/models/status-5-enum.md) | Optional | Status open: ticket is open, Mist is working on it<br><br>* pending: ticket is open and Requester attention is needed (e.g. Mist is asking for some more information)<br>* solved: ticket is marked as solved / considered by Mist (requester can update it, causing it to re-open; or rate it)<br>* closed: ticket is archived and cannot be changed |
| `subject` | `string` | Required | - |
| `mtype` | `string` | Required | question (default) / bug / critical |
| `updated_at` | `int` | Optional | - |

## Example (as JSON)

```json
{
  "case_number": "case_number0",
  "comments": [
    {
      "attachments": [
        {
          "content_type": "content_type3",
          "content_url": "content_url3",
          "size": 215
        },
        {
          "content_type": "content_type4",
          "content_url": "content_url4",
          "size": 216
        }
      ],
      "author": "author1",
      "comment": "comment7",
      "created_at": 171
    },
    {
      "attachments": [
        {
          "content_type": "content_type4",
          "content_url": "content_url4",
          "size": 216
        },
        {
          "content_type": "content_type5",
          "content_url": "content_url5",
          "size": 217
        },
        {
          "content_type": "content_type6",
          "content_url": "content_url6",
          "size": 218
        }
      ],
      "author": "author0",
      "comment": "comment6",
      "created_at": 170
    }
  ],
  "created_at": 6,
  "id": "00001770-0000-0000-0000-000000000000",
  "requester": "requester2",
  "subject": "subject6",
  "type": "type0"
}
```

