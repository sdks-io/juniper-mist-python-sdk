
# Orggroup

Organizations Group

## Structure

`Orggroup`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `created_time` | `float` | Optional | - |
| `id` | `uuid\|string` | Optional | - |
| `modified_time` | `float` | Optional | - |
| `msp_id` | `uuid\|string` | Optional | - |
| `name` | `string` | Required | - |
| `org_ids` | `List of uuid\|string` | Optional | - |

## Example (as JSON)

```json
{
  "created_time": 198.3,
  "id": "00001770-0000-0000-0000-000000000000",
  "modified_time": 136.66,
  "msp_id": "0000156c-0000-0000-0000-000000000000",
  "name": "name0",
  "org_ids": [
    "00001198-0000-0000-0000-000000000000"
  ]
}
```

