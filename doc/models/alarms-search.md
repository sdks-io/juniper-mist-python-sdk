
# Alarms Search

## Structure

`AlarmsSearch`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `end` | `int` | Required | - |
| `limit` | `int` | Required | - |
| `next` | `string` | Optional | - |
| `results` | [`List of Alarm`](../../doc/models/alarm.md) | Required | **Constraints**: *Minimum Items*: `1`, *Unique Items Required* |
| `start` | `int` | Required | - |
| `total` | `int` | Required | - |

## Example (as JSON)

```json
{
  "end": 254,
  "limit": 172,
  "results": [
    {
      "ack_admin_id": "00001e63-0000-0000-0000-000000000000",
      "ack_admin_name": "ack_admin_name1",
      "acked": true,
      "acked_time": 19,
      "aps": [
        "aps4",
        "aps5"
      ],
      "count": 143,
      "group": "group1",
      "id": "00000a0d-0000-0000-0000-000000000000",
      "last_seen": 215,
      "severity": "severity7",
      "timestamp": 165,
      "type": "type7"
    }
  ],
  "start": 212,
  "total": 10,
  "next": "next2"
}
```

