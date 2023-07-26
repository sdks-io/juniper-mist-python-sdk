
# Zone

Zone

## Structure

`Zone`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `created_time` | `float` | Optional | - |
| `for_site` | `bool` | Optional | - |
| `id` | `uuid\|string` | Optional | - |
| `map_id` | `uuid\|string` | Required | map where this zone is defined |
| `modified_time` | `float` | Optional | - |
| `name` | `string` | Required | The name of the zone |
| `org_id` | `uuid\|string` | Optional | - |
| `site_id` | `uuid\|string` | Optional | - |
| `vertices` | [`List of Vertex`](../../doc/models/vertex.md) | Required | vertices used to define an area. It’s assumed that the last point connects to the first point and forms an closed area<br>**Constraints**: *Unique Items Required* |

## Example (as JSON)

```json
{
  "map_id": "000006bc-0000-0000-0000-000000000000",
  "name": "name0",
  "vertices": [
    {
      "x": 25.55,
      "y": 156.83
    }
  ],
  "created_time": 198.3,
  "for_site": false,
  "id": "00001770-0000-0000-0000-000000000000",
  "modified_time": 136.66,
  "org_id": "00000ec8-0000-0000-0000-000000000000"
}
```

