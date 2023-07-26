
# Event 5

## Structure

`Event5`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `ap` | `string` | Optional | (will be deprecated soon; please use mac instead) ap mac |
| `ap_name` | `string` | Optional | (will be deprecated soon; please use device_name instead) ap name |
| `audit_id` | `uuid\|string` | Optional | (optional) audit id |
| `device_name` | `string` | Required | device name |
| `device_type` | [`DeviceType1Enum`](../../doc/models/device-type-1-enum.md) | Required | device type (ap/switch/gateway) |
| `ev_type` | [`EvTypeEnum`](../../doc/models/ev-type-enum.md) | Required | (optional) event advisory (notice/warn) |
| `mac` | `string` | Required | device mac |
| `org_id` | `uuid\|string` | Required | org id |
| `reason` | `string` | Optional | (optional) event reason |
| `site_id` | `uuid\|string` | Optional | site id |
| `site_name` | `string` | Optional | site name |
| `text` | `string` | Optional | (optional) event description |
| `timestamp` | `int` | Required | time the event occurred e.g. 1565987313 |
| `mtype` | `string` | Required | event type |

## Example (as JSON)

```json
{
  "ap": "ap4",
  "ap_name": "ap_name2",
  "audit_id": "000000b6-0000-0000-0000-000000000000",
  "device_name": "device_name2",
  "device_type": "switch",
  "ev_type": "notice",
  "mac": "mac4",
  "org_id": "00000ec8-0000-0000-0000-000000000000",
  "reason": "reason4",
  "site_id": "000007d6-0000-0000-0000-000000000000",
  "timestamp": 82,
  "type": "type0"
}
```

