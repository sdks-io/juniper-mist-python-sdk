
# Event 9

## Structure

`Event9`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `alert_events` | [`List of AlertEvent`](../../doc/models/alert-event.md) | Optional | list of occupancy alerts for non-compliance zones within the site detected around the same time<br>**Constraints**: *Minimum Items*: `1`, *Unique Items Required* |
| `for_site` | `bool` | Optional | - |
| `site_id` | `uuid\|string` | Required | - |
| `site_name` | `string` | Required | - |

## Example (as JSON)

```json
{
  "alert_events": [
    {
      "current_occupancy": 59,
      "map_id": "00001ebf-0000-0000-0000-000000000000",
      "occupancy_limit": 207,
      "org_id": "00000045-0000-0000-0000-000000000000",
      "timestamp": 9.71,
      "type": "COMPLIANCE-OK",
      "zone_id": "000001e9-0000-0000-0000-000000000000",
      "zone_name": "zone_name3"
    },
    {
      "current_occupancy": 58,
      "map_id": "00001ebe-0000-0000-0000-000000000000",
      "occupancy_limit": 206,
      "org_id": "00000046-0000-0000-0000-000000000000",
      "timestamp": 9.72,
      "type": "COMPLIANCE-VIOLATION",
      "zone_id": "000001ea-0000-0000-0000-000000000000",
      "zone_name": "zone_name4"
    }
  ],
  "for_site": false,
  "site_id": "000007d6-0000-0000-0000-000000000000",
  "site_name": "site_name8"
}
```

