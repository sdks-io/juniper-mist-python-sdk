
# Webhook Client Join

client join webhook

## Structure

`WebhookClientJoin`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `events` | [`List of Event3`](../../doc/models/event-3.md) | Required | **Constraints**: *Minimum Items*: `1`, *Unique Items Required* |
| `topic` | `string` | Required | **Default**: `'client-join'` |

## Example (as JSON)

```json
{
  "events": [
    {
      "ap": "ap4",
      "ap_name": "ap_name8",
      "band": "band2",
      "bssid": "bssid4",
      "connect": 86,
      "connect_float": 99.92,
      "mac": "mac4",
      "org_id": "00001302-0000-0000-0000-000000000000",
      "rssi": 27.72,
      "site_id": "00000290-0000-0000-0000-000000000000",
      "site_name": "site_name8",
      "ssid": "ssid8",
      "timestamp": 157.68,
      "version": 241.26,
      "wlan_id": "00001cc2-0000-0000-0000-000000000000"
    }
  ],
  "topic": "client-join"
}
```

