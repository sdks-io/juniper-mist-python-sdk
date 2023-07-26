
# Result 16

## Structure

`Result16`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `ap_mac` | `string` | Required | - |
| `client_mac` | `string` | Required | - |
| `fromap` | `string` | Required | - |
| `latency` | `float` | Required | - |
| `ssid` | `string` | Required | - |
| `subtype` | `string` | Optional | - |
| `timestamp` | `float` | Required | timestamp of the event in nsec |
| `mtype` | [`Type56Enum`](../../doc/models/type-56-enum.md) | Optional | success / fail / none / poor/ pingpong / slow |

## Example (as JSON)

```json
{
  "ap_mac": "ap_mac2",
  "client_mac": "client_mac8",
  "fromap": "fromap2",
  "latency": 125.6,
  "ssid": "ssid2",
  "subtype": "subtype2",
  "timestamp": 128.82,
  "type": "none"
}
```

