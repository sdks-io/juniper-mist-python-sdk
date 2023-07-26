
# Events Other Devices Search

## Structure

`EventsOtherDevicesSearch`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `end` | `int` | Optional | - |
| `limit` | `int` | Optional | - |
| `results` | [`EventOtherdevice`](../../doc/models/event-otherdevice.md) | Optional | - |
| `start` | `int` | Optional | - |
| `total` | `int` | Optional | - |

## Example (as JSON)

```json
{
  "end": 254,
  "limit": 172,
  "results": {
    "device_mac": "device_mac0",
    "mac": "mac0",
    "org_id": "org_id2",
    "site_id": "site_id2",
    "text": "text4"
  },
  "start": 212,
  "total": 10
}
```

