
# Event 4

## Structure

`Event4`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `ap` | `string` | Required | mac address of the AP the client roamed or disconnected from |
| `ap_name` | `string` | Required | user-friendly name of the AP the client roamed or disconnected from. |
| `band` | `string` | Required | 5GHz or 2.4GHz band |
| `bssid` | `string` | Required | - |
| `client_family` | `string` | Required | device family E.g. “Mac”, “iPhone”, “Apple watch” |
| `client_manufacture` | `string` | Required | device manufacturer E.g. “Apple” |
| `client_model` | `string` | Required | device model E.g. “8+”, “XS” |
| `client_os` | `string` | Required | device operating system E.g. “Mojave”, “Windows 10”, “Linux” |
| `connect` | `int` | Required | time when the user connects |
| `connect_float` | `float` | Required | floating point connect timestamp with millisecond precision |
| `disconnect` | `int` | Required | time when the user disconnects |
| `disconnect_float` | `float` | Required | floating point disconnect timestamp with millisecond precision |
| `duration` | `int` | Required | the duration of the roamed or complete session indicated by termination_reason field. |
| `mac` | `string` | Required | the client’s mac |
| `next_ap` | `string` | Required | the AP the client has roamed to. |
| `org_id` | `uuid\|string` | Required | - |
| `rssi` | `float` | Required | latest average RSSI before the user disconnects |
| `site_id` | `uuid\|string` | Required | - |
| `site_name` | `string` | Required | - |
| `ssid` | `string` | Required | - |
| `termination_reason` | `int` | Required | 1 disassociate - when the client disassociates. 2 inactive - when the client is timeout. 3 roamed - when the client is roamed between APs |
| `timestamp` | `float` | Required | - |
| `version` | `float` | Required | schema version of this message |
| `wlan_id` | `uuid\|string` | Required | - |

## Example (as JSON)

```json
{
  "ap": "ap4",
  "ap_name": "ap_name2",
  "band": "band2",
  "bssid": "bssid6",
  "client_family": "client_family4",
  "client_manufacture": "client_manufacture6",
  "client_model": "client_model4",
  "client_os": "client_os8",
  "connect": 108,
  "connect_float": 69.42,
  "disconnect": 58,
  "disconnect_float": 36.8,
  "duration": 112,
  "mac": "mac4",
  "next_ap": "next_ap2",
  "org_id": "00000ec8-0000-0000-0000-000000000000",
  "rssi": 2.78,
  "site_id": "000007d6-0000-0000-0000-000000000000",
  "site_name": "site_name8",
  "ssid": "ssid2",
  "termination_reason": 14,
  "timestamp": 128.82,
  "version": 45.24,
  "wlan_id": "00002208-0000-0000-0000-000000000000"
}
```

