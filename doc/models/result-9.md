
# Result 9

## Structure

`Result9`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `admin_id` | `uuid\|string` | Required | - |
| `admin_name` | `string` | Required | - |
| `after` | [`After`](../../doc/models/after.md) | Optional | field values after the change |
| `before` | [`Before`](../../doc/models/before.md) | Optional | field values prior to the change |
| `for_site` | `bool` | Optional | - |
| `id` | `uuid\|string` | Required | - |
| `message` | `string` | Required | - |
| `org_id` | `uuid\|string` | Required | - |
| `site_id` | `uuid\|string` | Required | - |
| `timestamp` | `float` | Required | - |

## Example (as JSON)

```json
{
  "admin_id": "00001ada-0000-0000-0000-000000000000",
  "admin_name": "admin_name2",
  "after": {
    "auth": {
      "type": "type8"
    }
  },
  "before": {
    "auth": {
      "type": "type6"
    }
  },
  "for_site": false,
  "id": "00001770-0000-0000-0000-000000000000",
  "message": "message0",
  "org_id": "00000ec8-0000-0000-0000-000000000000",
  "site_id": "000007d6-0000-0000-0000-000000000000",
  "timestamp": 128.82
}
```

