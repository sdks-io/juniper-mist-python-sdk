
# Stats Org

Org statistics

## Structure

`StatsOrg`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `alarmtemplate_id` | `uuid\|string` | Required | - |
| `allow_mist` | `bool` | Required | - |
| `created_time` | `float` | Required | - |
| `id` | `uuid\|string` | Required | - |
| `modified_time` | `float` | Required | - |
| `msp_id` | `uuid\|string` | Required | - |
| `name` | `string` | Required | - |
| `num_devices` | `int` | Required | - |
| `num_devices_connected` | `int` | Required | - |
| `num_devices_disconnected` | `int` | Required | - |
| `num_inventory` | `int` | Required | - |
| `num_sites` | `int` | Required | - |
| `orggroup_ids` | `List of uuid\|string` | Required | - |
| `session_expiry` | `int` | Required | - |
| `sle` | [`List of Sle1`](../../doc/models/sle-1.md) | Required | **Constraints**: *Minimum Items*: `1`, *Unique Items Required* |

## Example (as JSON)

```json
{
  "alarmtemplate_id": "00001a0e-0000-0000-0000-000000000000",
  "allow_mist": false,
  "created_time": 198.3,
  "id": "00001770-0000-0000-0000-000000000000",
  "modified_time": 136.66,
  "msp_id": "0000156c-0000-0000-0000-000000000000",
  "name": "name0",
  "num_devices": 126,
  "num_devices_connected": 18,
  "num_devices_disconnected": 26,
  "num_inventory": 180,
  "num_sites": 216,
  "orggroup_ids": [
    "0000118a-0000-0000-0000-000000000000",
    "0000118b-0000-0000-0000-000000000000"
  ],
  "session_expiry": 40,
  "sle": [
    {
      "path": "path6",
      "user_minutes": {
        "ok": 178.3,
        "total": 176.84
      }
    }
  ]
}
```

