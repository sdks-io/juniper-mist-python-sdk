
# Api V1 Sites Maps Auto Placement Request

## Structure

`ApiV1SitesMapsAutoPlacementRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `device_ids` | `List of string` | Optional | list of device macs |
| `force_collection` | `bool` | Optional | * If `force_collection`==`false`: the API Iattempts to start localization with existing data.<br>* If `force_collection`==`true`: maintenance the API attempts to start orchestration.<br>**Default**: `False` |

## Example (as JSON)

```json
{
  "force_collection": false,
  "device_ids": [
    "device_ids9",
    "device_ids0"
  ]
}
```

