
# Curd Ui Settings

CURD UI Settings

## Structure

`CurdUiSettings`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `created_time` | `float` | Required | - |
| `default_scope_id` | `string` | Optional | - |
| `default_scope_type` | `string` | Optional | - |
| `default_time_range` | [`DefaultTimeRange`](../../doc/models/default-time-range.md) | Optional | - |
| `description` | `string` | Required | - |
| `for_site` | `bool` | Required | - |
| `id` | `uuid\|string` | Required | - |
| `is_custom_databoard` | `bool` | Optional | - |
| `is_scope_linked` | `bool` | Optional | - |
| `is_time_range_linked` | `bool` | Optional | - |
| `modified_time` | `float` | Required | - |
| `name` | `string` | Optional | - |
| `org_id` | `uuid\|string` | Required | - |
| `purpose` | `string` | Required | - |
| `site_id` | `uuid\|string` | Required | - |
| `tiles` | [`List of Tile`](../../doc/models/tile.md) | Optional | **Constraints**: *Minimum Items*: `1`, *Unique Items Required* |

## Example (as JSON)

```json
{
  "created_time": 198.3,
  "defaultScopeId": "defaultScopeId2",
  "defaultScopeType": "defaultScopeType0",
  "defaultTimeRange": {
    "end": 224,
    "endDate": "endDate8",
    "interval": "interval4",
    "name": "name6",
    "shortName": "shortName4"
  },
  "description": "description0",
  "for_site": false,
  "id": "00001770-0000-0000-0000-000000000000",
  "isCustomDataboard": false,
  "isScopeLinked": false,
  "modified_time": 136.66,
  "org_id": "00000ec8-0000-0000-0000-000000000000",
  "purpose": "purpose6",
  "site_id": "000007d6-0000-0000-0000-000000000000"
}
```

