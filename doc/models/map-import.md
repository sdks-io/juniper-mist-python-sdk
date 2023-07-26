
# Map Import

## Structure

`MapImport`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `aps` | [`List of Aps2`](../../doc/models/aps-2.md) | Required | **Constraints**: *Minimum Items*: `1`, *Unique Items Required* |
| `floorplans` | [`List of Floorplan`](../../doc/models/floorplan.md) | Required | **Constraints**: *Minimum Items*: `1`, *Unique Items Required* |
| `for_site` | `bool` | Optional | - |
| `site_id` | `uuid\|string` | Required | - |
| `summary` | [`Summary`](../../doc/models/summary.md) | Required | - |

## Example (as JSON)

```json
{
  "aps": [
    {
      "action": "assigned-placed",
      "floorplan_id": "00001153-0000-0000-0000-000000000000",
      "height": 42.47,
      "mac": "mac5",
      "map_id": "00000ebd-0000-0000-0000-000000000000",
      "orientation": 140.51,
      "reason": "reason3"
    }
  ],
  "floorplans": [
    {
      "action": "action2",
      "id": "000026e2-0000-0000-0000-000000000000",
      "map_id": "000008b6-0000-0000-0000-000000000000",
      "name": "name4",
      "reason": "reason0"
    }
  ],
  "site_id": "000007d6-0000-0000-0000-000000000000",
  "summary": {
    "num_ap_assigned": 66,
    "num_inv_assigned": 174,
    "num_map_assigned": 164
  },
  "for_site": false
}
```

