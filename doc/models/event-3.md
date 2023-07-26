
# Event 3

## Structure

`Event3`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `ap` | `string` | Required | mac address of the AP the client connected to |
| `ap_name` | `string` | Required | user-friendly name of the AP the client connected to. |
| `band` | `string` | Required | 5GHz or 2.4GHz band |
| `bssid` | `string` | Required | - |
| `connect` | `int` | Required | time when the user connects |
| `connect_float` | `float` | Required | floating point connect timestamp with millisecond precision |
| `mac` | `string` | Required | the client’s mac |
| `org_id` | `uuid\|string` | Required | - |
| `rssi` | `float` | Required | RSSI when the client associated |
| `site_id` | `uuid\|string` | Required | - |
| `site_name` | `string` | Required | - |
| `ssid` | `string` | Required | ESSID |
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
  "connect": 108,
  "connect_float": 69.42,
  "mac": "mac4",
  "org_id": "00000ec8-0000-0000-0000-000000000000",
  "rssi": 2.78,
  "site_id": "000007d6-0000-0000-0000-000000000000",
  "site_name": "site_name8",
  "ssid": "ssid2",
  "timestamp": 128.82,
  "version": 45.24,
  "wlan_id": "00002208-0000-0000-0000-000000000000"
}
```

