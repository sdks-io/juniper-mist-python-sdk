
# Webhook Device Events

device event  webhook

## Structure

`WebhookDeviceEvents`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `events` | [`List of Event5`](../../doc/models/event-5.md) | Required | list of events<br>**Constraints**: *Minimum Items*: `1`, *Unique Items Required* |
| `topic` | `string` | Required | topic subscribed to<br>**Default**: `'device-events'` |

## Example (as JSON)

```json
{
  "events": [
    {
      "ap": "ap4",
      "ap_name": "ap_name8",
      "audit_id": "00002280-0000-0000-0000-000000000000",
      "device_name": "device_name2",
      "device_type": "switch",
      "ev_type": "notice",
      "mac": "mac4",
      "org_id": "00001302-0000-0000-0000-000000000000",
      "reason": "reason4",
      "site_id": "00000290-0000-0000-0000-000000000000",
      "timestamp": 152,
      "type": "type0"
    }
  ],
  "topic": "device-events"
}
```

