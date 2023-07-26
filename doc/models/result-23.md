
# Result 23

## Structure

`Result23`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `ap_id` | `uuid\|string` | Required | - |
| `band` | [`Band8Enum`](../../doc/models/band-8-enum.md) | Required | - |
| `bandwidth` | [`Bandwidth5Enum`](../../doc/models/bandwidth-5-enum.md) | Required | channel width for the band |
| `channel` | `int` | Required | channel for the band from rrm |
| `event` | [`Event13Enum`](../../doc/models/event-13-enum.md) | Required | schedule-site-rrm / triggered-site-rrm / interference-ap-co-channel / rrm-radar |
| `power` | `int` | Required | tx power of the radio |
| `pre_bandwidth` | [`PreBandwidthEnum`](../../doc/models/pre-bandwidth-enum.md) | Required | (previously) channel width for the band , 0 means no previously available |
| `pre_channel` | `int` | Required | (previously) channel for the band, 0 means no previously available |
| `pre_power` | `float` | Required | (previously) tx power of the radio, 0 means no previously available |
| `pre_usage` | `string` | Required | - |
| `timestamp` | `float` | Required | timestamp of the event |
| `usage` | `string` | Required | - |

## Example (as JSON)

```json
{
  "ap_id": "000017be-0000-0000-0000-000000000000",
  "band": "6",
  "bandwidth": 20,
  "channel": 120,
  "event": "rrm-radar",
  "power": 60,
  "pre_bandwidth": 40,
  "pre_channel": 74,
  "pre_power": 223.66,
  "pre_usage": "pre_usage2",
  "timestamp": 128.82,
  "usage": "usage8"
}
```

