
# Webhook Occupancy Alerts

occupancy alert  webhook

## Structure

`WebhookOccupancyAlerts`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `events` | [`List of Event9`](../../doc/models/event-9.md) | Required | **Constraints**: *Minimum Items*: `1`, *Unique Items Required* |
| `topic` | `string` | Required | **Default**: `'occupancy-alerts'` |

## Example (as JSON)

```json
{
  "events": [
    {
      "alert_events": [
        {
          "current_occupancy": 235,
          "map_id": "0000226f-0000-0000-0000-000000000000",
          "occupancy_limit": 127,
          "org_id": "000023a5-0000-0000-0000-000000000000",
          "timestamp": 0.27,
          "type": "COMPLIANCE-OK",
          "zone_id": "00002549-0000-0000-0000-000000000000",
          "zone_name": "zone_name9"
        },
        {
          "current_occupancy": 236,
          "map_id": "00002270-0000-0000-0000-000000000000",
          "occupancy_limit": 128,
          "org_id": "000023a4-0000-0000-0000-000000000000",
          "timestamp": 0.26,
          "type": "COMPLIANCE-VIOLATION",
          "zone_id": "00002548-0000-0000-0000-000000000000",
          "zone_name": "zone_name8"
        },
        {
          "current_occupancy": 237,
          "map_id": "00002271-0000-0000-0000-000000000000",
          "occupancy_limit": 129,
          "org_id": "000023a3-0000-0000-0000-000000000000",
          "timestamp": 0.25,
          "type": "COMPLIANCE-OK",
          "zone_id": "00002547-0000-0000-0000-000000000000",
          "zone_name": "zone_name7"
        }
      ],
      "for_site": false,
      "site_id": "00000290-0000-0000-0000-000000000000",
      "site_name": "site_name8"
    }
  ],
  "topic": "occupancy-alerts"
}
```

