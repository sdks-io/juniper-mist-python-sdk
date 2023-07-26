
# Webhook Device Updowns

device up/down webhook

## Structure

`WebhookDeviceUpdowns`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `events` | [`List of Event6`](../../doc/models/event-6.md) | Required | **Constraints**: *Minimum Items*: `1`, *Unique Items Required* |
| `topic` | `string` | Required | **Default**: `'device-updowns'` |

## Example (as JSON)

```json
{
  "events": [
    {
      "ap": "ap4",
      "ap_name": "ap_name8",
      "for_site": false,
      "org_id": "00001302-0000-0000-0000-000000000000",
      "site_id": "00000290-0000-0000-0000-000000000000",
      "site_name": "site_name8",
      "timestamp": 157.68,
      "type": "type0"
    }
  ],
  "topic": "device-updowns"
}
```

