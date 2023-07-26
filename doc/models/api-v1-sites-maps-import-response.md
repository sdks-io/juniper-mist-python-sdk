
# Api V1 Sites Maps Import Response

## Structure

`ApiV1SitesMapsImportResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `aps` | [`List of Aps3`](../../doc/models/aps-3.md) | Required | **Constraints**: *Minimum Items*: `1`, *Unique Items Required* |
| `floorplans` | [`List of Floorplan1`](../../doc/models/floorplan-1.md) | Optional | **Constraints**: *Minimum Items*: `1`, *Unique Items Required* |
| `site_id` | `string` | Required | **Constraints**: *Minimum Length*: `1` |
| `summary` | [`Summary1`](../../doc/models/summary-1.md) | Optional | - |

## Example (as JSON)

```json
{
  "aps": [
    {
      "action": "assigned-placed",
      "floorplan_id": "floorplan_id5",
      "height": 42.47,
      "mac": "mac5",
      "map_id": "map_id3",
      "orientation": 140.51
    }
  ],
  "site_id": "site_id6",
  "floorplans": [
    {
      "action": "imported",
      "id": "id4",
      "map_id": "map_id0",
      "name": "name4",
      "reason": "reason0"
    }
  ],
  "summary": {
    "num_ap_assigned": 92.82,
    "num_inv_assigned": 6.86,
    "num_map_assigned": 104.04
  }
}
```

