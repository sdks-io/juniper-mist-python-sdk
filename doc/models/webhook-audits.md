
# Webhook Audits

audit webhook

## Structure

`WebhookAudits`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `events` | [`List of Event2`](../../doc/models/event-2.md) | Required | **Constraints**: *Minimum Items*: `1`, *Unique Items Required* |
| `topic` | `string` | Required | **Default**: `'audits'` |

## Example (as JSON)

```json
{
  "events": [
    {
      "admin_name": "admin_name8",
      "device_id": "00000380-0000-0000-0000-000000000000",
      "id": "0000122a-0000-0000-0000-000000000000",
      "message": "message0",
      "org_id": "00001302-0000-0000-0000-000000000000",
      "site_id": "00000290-0000-0000-0000-000000000000",
      "src_ip": "src_ip6",
      "timestamp": 157.68
    }
  ],
  "topic": "audits"
}
```

