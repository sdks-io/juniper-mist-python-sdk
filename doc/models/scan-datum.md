
# Scan Datum

## Structure

`ScanDatum`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `ap` | `string` | Required | mac address of the AP associated with the BSSID scanned<br>**Constraints**: *Minimum Length*: `1` |
| `band` | [`Band12Enum`](../../doc/models/band-12-enum.md) | Required | 5GHz or 2.4GHz band, associated with the BSSID scanned<br>**Constraints**: *Minimum Length*: `1` |
| `bssid` | `string` | Required | BSSID found during client’s background scan for wifi<br>**Constraints**: *Minimum Length*: `1` |
| `channel` | `int` | Required | channel of the band found in the scan |
| `rssi` | `float` | Required | client’s RSSI relative to the BSSID scanned |
| `ssid` | `string` | Required | ESSID containing the BSSID scanned<br>**Constraints**: *Minimum Length*: `1` |
| `timestamp` | `float` | Required | time the scan of the particular BSSID occurred |

## Example (as JSON)

```json
{
  "ap": "ap4",
  "band": "2.4",
  "bssid": "bssid6",
  "channel": 120,
  "rssi": 2.78,
  "ssid": "ssid2",
  "timestamp": 128.82
}
```

