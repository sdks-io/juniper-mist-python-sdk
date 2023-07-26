
# Asset

Asset

## Structure

`Asset`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `created_time` | `float` | Optional | - |
| `for_site` | `bool` | Optional | - |
| `id` | `uuid\|string` | Optional | - |
| `mac` | `string` | Required | bluetooth MAC |
| `map_id` | `uuid\|string` | Optional | - |
| `modified_time` | `float` | Optional | - |
| `name` | `string` | Required | name / label of the device |
| `org_id` | `uuid\|string` | Optional | - |
| `site_id` | `uuid\|string` | Optional | - |
| `tag_id` | `uuid\|string` | Optional | - |

## Example (as JSON)

```json
{
  "created_time": 198.3,
  "for_site": false,
  "id": "00001770-0000-0000-0000-000000000000",
  "mac": "mac4",
  "map_id": "000006bc-0000-0000-0000-000000000000",
  "modified_time": 136.66,
  "name": "name0"
}
```

