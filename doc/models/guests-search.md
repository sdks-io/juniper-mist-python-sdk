
# Guests Search

## Structure

`GuestsSearch`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `end` | `int` | Required | - |
| `limit` | `int` | Required | - |
| `next` | `string` | Required | - |
| `results` | [`List of Result18`](../../doc/models/result-18.md) | Required | **Constraints**: *Minimum Items*: `1`, *Unique Items Required* |
| `start` | `int` | Required | - |
| `total` | `int` | Required | - |

## Example (as JSON)

```json
{
  "end": 254,
  "limit": 172,
  "next": "next2",
  "results": [
    {
      "ap": "ap1",
      "auth_method": "auth_method3",
      "authorized_expiring_time": 158.75,
      "authorized_time": 120.75,
      "company": "company7",
      "email": "email3",
      "name": "name3",
      "ssid": "ssid9",
      "timestamp": 63.09
    }
  ],
  "start": 212,
  "total": 10
}
```

