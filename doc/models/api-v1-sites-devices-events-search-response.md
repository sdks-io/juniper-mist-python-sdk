
# Api V1 Sites Devices Events Search Response

## Structure

`ApiV1SitesDevicesEventsSearchResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `end` | `int` | Required | - |
| `limit` | `int` | Required | - |
| `next` | `string` | Required | - |
| `results` | [`List of EventsDeviceAp`](../../doc/models/events-device-ap.md) | Required | **Constraints**: *Minimum Items*: `1`, *Unique Items Required* |
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
      "last_reboot_time": 40.95,
      "text": "text7",
      "timestamp": 63.09,
      "type": "type7",
      "type_code": 95
    }
  ],
  "start": 212,
  "total": 10
}
```

