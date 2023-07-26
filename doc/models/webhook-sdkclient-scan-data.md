
# Webhook Sdkclient Scan Data

## Structure

`WebhookSdkclientScanData`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `events` | [`List of Event11`](../../doc/models/event-11.md) | Required | **Constraints**: *Minimum Items*: `1`, *Unique Items Required* |
| `topic` | `string` | Required, Constant | **Default**: `'sdkclient-scan-data'` |

## Example (as JSON)

```json
{
  "events": [
    {
      "connection_ap": "connection_ap0",
      "connection_band": "connection_band2",
      "connection_bssid": "connection_bssid8",
      "connection_channel": 68,
      "connection_rssi": 3.06,
      "last_seen": 64.2,
      "mac": "mac4",
      "scan_data": [
        {
          "ap": "ap2",
          "band": "2.4",
          "bssid": "bssid4",
          "channel": 26,
          "rssi": 57.04,
          "ssid": "ssid0",
          "timestamp": 69.0
        }
      ],
      "site_id": "site_id6"
    }
  ],
  "topic": "sdkclient-scan-data"
}
```

