
# Sle Impacted Users

## Structure

`SleImpactedUsers`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `classifier` | `string` | Required | - |
| `end` | `float` | Required | - |
| `failure` | `string` | Required | - |
| `limit` | `float` | Required | - |
| `metric` | `string` | Required | **Constraints**: *Minimum Length*: `1` |
| `page` | `float` | Required | - |
| `start` | `float` | Required | - |
| `total_count` | `float` | Required | - |
| `users` | [`List of User2`](../../doc/models/user-2.md) | Required | **Constraints**: *Minimum Items*: `1`, *Unique Items Required* |

## Example (as JSON)

```json
{
  "classifier": "classifier4",
  "end": 12.78,
  "failure": "failure6",
  "limit": 237.24,
  "metric": "metric8",
  "page": 110.38,
  "start": 224.84,
  "total_count": 82.96,
  "users": [
    {
      "ap_mac": "ap_mac5",
      "ap_name": "ap_name9",
      "degraded": 246.83,
      "device_os": "device_os3",
      "device_type": "device_type7",
      "duration": 119.89,
      "mac": "mac7",
      "name": "name3",
      "ssid": "ssid9",
      "total": 237.17,
      "wlan_id": "wlan_id5"
    }
  ]
}
```

