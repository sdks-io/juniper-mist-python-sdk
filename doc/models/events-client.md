
# Events Client

client events

## Structure

`EventsClient`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `ap` | `string` | Optional | - |
| `band` | [`Band7Enum`](../../doc/models/band-7-enum.md) | Required | - |
| `bssid` | `string` | Optional | - |
| `channel` | `int` | Optional | - |
| `proto` | [`ProtoEnum`](../../doc/models/proto-enum.md) | Required | b / g / n / a / ac |
| `ssid` | `string` | Optional | - |
| `text` | `string` | Optional | - |
| `timestamp` | `float` | Required | - |
| `mtype` | `string` | Optional | event type, e.g. MARVIS_EVENT_CLIENT_FBT_FAILURE |
| `type_code` | `int` | Optional | for assoc/disassoc events |
| `wlan_id` | `uuid\|string` | Optional | - |

## Example (as JSON)

```json
{
  "ap": "ap4",
  "band": "24",
  "bssid": "bssid6",
  "channel": 120,
  "proto": "a",
  "ssid": "ssid2",
  "text": "text0",
  "timestamp": 128.82
}
```

