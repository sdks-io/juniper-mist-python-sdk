
# Webhook Alarms

**N.B.**: Fields like `aps`, `bssids`, `ssids` are event specific. They are relevant to this event type ( rogue-ap-detected). For a different event type, different fields may be sent. These don’t contain all affected entities and are representative samples of entities (capped at 10). For marvis action related events, we expose `details` to include more event specific details.

Events specific fields for other alarm event type can be found with API https://api.mist.com/api/v1/const/alarm_defs, under “fields” array of /alarm_defs response object.

## Structure

`WebhookAlarms`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `events` | [`List of Event`](../../doc/models/event.md) | Required | list of events<br>**Constraints**: *Minimum Items*: `1`, *Unique Items Required* |
| `topic` | `string` | Required | topic subscribed to<br>**Default**: `'alarms'` |

## Example (as JSON)

```json
{
  "events": [
    {
      "aps": [
        "aps1",
        "aps2"
      ],
      "bssids": [
        "bssids6"
      ],
      "count": 82,
      "event_id": "00001b22-0000-0000-0000-000000000000",
      "for_site": false,
      "id": "0000122a-0000-0000-0000-000000000000",
      "last_seen": 64.2,
      "org_id": "00001302-0000-0000-0000-000000000000",
      "site_id": "00000290-0000-0000-0000-000000000000",
      "timestamp": 152,
      "type": "type0"
    }
  ],
  "topic": "alarms"
}
```

