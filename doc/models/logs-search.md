
# Logs Search

## Structure

`LogsSearch`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `end` | `int` | Required | - |
| `limit` | `int` | Required | - |
| `next` | `string` | Optional | - |
| `results` | [`List of Result3`](../../doc/models/result-3.md) | Required | **Constraints**: *Minimum Items*: `1`, *Unique Items Required* |
| `start` | `int` | Required | - |
| `total` | `int` | Required | - |

## Example (as JSON)

```json
{
  "end": 254,
  "limit": 172,
  "results": [
    {
      "admin_id": "00000d77-0000-0000-0000-000000000000",
      "admin_name": "admin_name9",
      "after": {
        "key1": "val1",
        "key2": "val2"
      },
      "before": {
        "key1": "val1",
        "key2": "val2"
      },
      "for_site": true,
      "id": "00000a0d-0000-0000-0000-000000000000",
      "message": "message7",
      "org_id": "00000ae5-0000-0000-0000-000000000000",
      "site_id": "00002183-0000-0000-0000-000000000000",
      "timestamp": 63.09
    }
  ],
  "start": 212,
  "total": 10,
  "next": "next2"
}
```

