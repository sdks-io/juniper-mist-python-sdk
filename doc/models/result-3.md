
# Result 3

## Structure

`Result3`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `admin_id` | `uuid\|string` | Required | admin id |
| `admin_name` | `string` | Required | name of the admin that performs the action |
| `after` | `object` | Optional | field values after the change |
| `before` | `object` | Optional | field values prior to the change |
| `for_site` | `bool` | Optional | - |
| `id` | `uuid\|string` | Optional | - |
| `message` | `string` | Required | log message |
| `org_id` | `uuid\|string` | Required | org id |
| `site_id` | `uuid\|string` | Required | site id |
| `timestamp` | `float` | Required | start time, in epoch |

## Example (as JSON)

```json
{
  "admin_id": "00001ada-0000-0000-0000-000000000000",
  "admin_name": "admin_name2",
  "after": {
    "key1": "val1",
    "key2": "val2"
  },
  "before": {
    "key1": "val1",
    "key2": "val2"
  },
  "for_site": false,
  "id": "00001770-0000-0000-0000-000000000000",
  "message": "message0",
  "org_id": "00000ec8-0000-0000-0000-000000000000",
  "site_id": "000007d6-0000-0000-0000-000000000000",
  "timestamp": 128.82
}
```

