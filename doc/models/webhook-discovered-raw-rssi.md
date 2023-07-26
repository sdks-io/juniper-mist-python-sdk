
# Webhook Discovered Raw Rssi

## Structure

`WebhookDiscoveredRawRssi`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `events` | [`List of Event7`](../../doc/models/event-7.md) | Optional | - |
| `topic` | `string` | Required | - |

## Example (as JSON)

```json
{
  "events": [
    {
      "ap_loc": [
        3.52,
        3.53,
        3.54
      ],
      "beam": 146,
      "device_id": "00000380-0000-0000-0000-000000000000",
      "ibeacon_major": 200,
      "ibeacon_minor": 62,
      "ibeacon_uuid": "00000d30-0000-0000-0000-000000000000",
      "is_asset": false,
      "mac": "mac4",
      "map_id": "00000c02-0000-0000-0000-000000000000",
      "org_id": "00001302-0000-0000-0000-000000000000",
      "rssi": 27.72,
      "site_id": "00000290-0000-0000-0000-000000000000"
    }
  ],
  "topic": "topic8"
}
```

