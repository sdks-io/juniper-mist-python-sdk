
# Webhook Ping

ping webhook

## Structure

`WebhookPing`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `events` | [`List of Event10`](../../doc/models/event-10.md) | Required | **Constraints**: *Minimum Items*: `1`, *Unique Items Required* |
| `topic` | `string` | Required | **Default**: `'ping'` |

## Example (as JSON)

```json
{
  "events": [
    {
      "id": "0000122a-0000-0000-0000-000000000000",
      "name": "name0",
      "site_id": "00000290-0000-0000-0000-000000000000",
      "timestamp": 157.68
    }
  ],
  "topic": "ping"
}
```

