
# Webhook Zone

zone webhook

## Structure

`WebhookZone`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `events` | [`List of Event12`](../../doc/models/event-12.md) | Required | list of events<br>**Constraints**: *Minimum Items*: `1`, *Unique Items Required* |
| `topic` | `string` | Required | topic subscribed to<br>**Default**: `'zone'` |

## Example (as JSON)

```json
{
  "events": [
    {
      "asset_id": "00000374-0000-0000-0000-000000000000",
      "id": "0000122a-0000-0000-0000-000000000000",
      "mac": "mac4",
      "map_id": "00000c02-0000-0000-0000-000000000000",
      "name": "name0",
      "site_id": "00000290-0000-0000-0000-000000000000",
      "timestamp": 152,
      "trigger": "enter",
      "type": "type0",
      "zone_id": "000014a6-0000-0000-0000-000000000000"
    }
  ],
  "topic": "zone"
}
```

