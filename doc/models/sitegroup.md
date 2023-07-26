
# Sitegroup

Sites Group

## Structure

`Sitegroup`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `created_time` | `float` | Optional | - |
| `id` | `uuid\|string` | Optional | - |
| `modified_time` | `float` | Optional | - |
| `name` | `string` | Required | - |
| `org_id` | `uuid\|string` | Optional | - |
| `site_ids` | `List of uuid\|string` | Optional | - |

## Example (as JSON)

```json
{
  "created_time": 198.3,
  "id": "00001770-0000-0000-0000-000000000000",
  "modified_time": 136.66,
  "name": "name0",
  "org_id": "00000ec8-0000-0000-0000-000000000000",
  "site_ids": [
    "00001a9a-0000-0000-0000-000000000000",
    "00001a9b-0000-0000-0000-000000000000"
  ]
}
```

