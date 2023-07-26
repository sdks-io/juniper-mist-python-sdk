
# Result 19

## Structure

`Result19`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `ap_mac` | `string` | Required | mac of the device that had strongest signal strength for ssid/bssid pair |
| `avg_rssi` | `float` | Required | average signal strength of ap_mac for ssid/bssid pair |
| `bssid` | `string` | Required | bssid of the network detected as threat |
| `channel` | `string` | Required | channel over which ap_mac heard ssid/bssid pair |
| `delta_x` | `float` | Optional | X position relative to the reporting AP (`ap_mac`) |
| `delta_y` | `float` | Optional | Y position relative to the reporting AP (`ap_mac`) |
| `num_aps` | `int` | Required | num of aps that heard the ssid/bssid pair |
| `seen_on_lan` | `bool` | Optional | whether the reporting AP see a wireless client (on LAN) connecting to it |
| `ssid` | `string` | Optional | ssid of the network detected as threat |
| `times_heard` | `int` | Optional | represents number of times the pair was heard in the interval. Each count roughly corresponds to a minute. |

## Example (as JSON)

```json
{
  "ap_mac": "ap_mac2",
  "avg_rssi": 46.3,
  "bssid": "bssid6",
  "channel": "channel4",
  "delta_x": 157.2,
  "delta_y": 177.66,
  "num_aps": 230,
  "seen_on_lan": false,
  "ssid": "ssid2",
  "times_heard": 20
}
```

