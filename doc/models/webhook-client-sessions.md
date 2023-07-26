
# Webhook Client Sessions

client session webhook

## Structure

`WebhookClientSessions`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `events` | [`List of Event4`](../../doc/models/event-4.md) | Required | **Constraints**: *Minimum Items*: `1`, *Unique Items Required* |
| `topic` | `string` | Required | **Default**: `'client-sessions'` |

## Example (as JSON)

```json
{
  "events": [
    {
      "ap": "ap4",
      "ap_name": "ap_name8",
      "band": "band2",
      "bssid": "bssid4",
      "client_family": "client_family4",
      "client_manufacture": "client_manufacture6",
      "client_model": "client_model4",
      "client_os": "client_os8",
      "connect": 86,
      "connect_float": 99.92,
      "disconnect": 36,
      "disconnect_float": 249.7,
      "duration": 90,
      "mac": "mac4",
      "next_ap": "next_ap8",
      "org_id": "00001302-0000-0000-0000-000000000000",
      "rssi": 27.72,
      "site_id": "00000290-0000-0000-0000-000000000000",
      "site_name": "site_name8",
      "ssid": "ssid8",
      "termination_reason": 220,
      "timestamp": 157.68,
      "version": 241.26,
      "wlan_id": "00001cc2-0000-0000-0000-000000000000"
    }
  ],
  "topic": "client-sessions"
}
```

