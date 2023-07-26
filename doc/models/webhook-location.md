
# Webhook Location

location  webhook

## Structure

`WebhookLocation`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `events` | [`List of Event8`](../../doc/models/event-8.md) | Required | list of events<br>**Constraints**: *Minimum Items*: `1`, *Unique Items Required* |
| `topic` | `string` | Required | topic subscribed to<br>**Default**: `'location'` |

## Example (as JSON)

```json
{
  "events": [
    {
      "battery_voltage": 156,
      "eddystone_uid_instance": "eddystone_uid_instance4",
      "eddystone_uid_namespace": "eddystone_uid_namespace4",
      "eddystone_url_url": "eddystone_url_url4",
      "ibeacon_major": 200,
      "id": "0000122a-0000-0000-0000-000000000000",
      "map_id": "00000c02-0000-0000-0000-000000000000",
      "site_id": "00000290-0000-0000-0000-000000000000",
      "timestamp": 152,
      "type": "type0",
      "x": 36,
      "y": 108
    }
  ],
  "topic": "location"
}
```

