
# Event 11

## Structure

`Event11`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `connection_ap` | `string` | Required | mac address of the AP the client is connected to<br>**Constraints**: *Minimum Length*: `1` |
| `connection_band` | `string` | Required | 5GHz or 2.4GHz band, of the BSSID the client is connected to<br>**Constraints**: *Minimum Length*: `1` |
| `connection_bssid` | `string` | Required | BSSID of the AP the client is connected to<br>**Constraints**: *Minimum Length*: `1` |
| `connection_channel` | `int` | Required | channel of the band the client is connected to |
| `connection_rssi` | `float` | Required | RSSI of the client’s connection to the AP/BSSID |
| `last_seen` | `float` | Required | time client last seen with scan data |
| `mac` | `string` | Required | the client’s mac<br>**Constraints**: *Minimum Length*: `1` |
| `scan_data` | [`List of ScanDatum`](../../doc/models/scan-datum.md) | Optional | **Constraints**: *Minimum Items*: `1`, *Unique Items Required* |
| `site_id` | `string` | Required | Site ID<br>**Constraints**: *Minimum Length*: `1` |

## Example (as JSON)

```json
{
  "connection_ap": "connection_ap0",
  "connection_band": "connection_band2",
  "connection_bssid": "connection_bssid8",
  "connection_channel": 90,
  "connection_rssi": 27.44,
  "last_seen": 33.7,
  "mac": "mac4",
  "scan_data": [
    {
      "ap": "ap0",
      "band": "2.4",
      "bssid": "bssid8",
      "channel": 96,
      "rssi": 112.66,
      "ssid": "ssid8",
      "timestamp": 13.38
    }
  ],
  "site_id": "site_id6"
}
```

