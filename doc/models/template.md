
# Template

Template

## Structure

`Template`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `applies` | [`Applies`](../../doc/models/applies.md) | Optional | where this template should be applied to, can be org_id, site_ids, sitegroup_ids |
| `created_time` | `float` | Optional | - |
| `deviceprofile_ids` | `List of uuid\|string` | Optional | list of Device Profile ids |
| `exceptions` | [`Exceptions`](../../doc/models/exceptions.md) | Optional | where this template should not be applied to (takes precedence) |
| `filter_by_deviceprofile` | `bool` | Optional | whether to further filter by Device Profile |
| `id` | `uuid\|string` | Optional | - |
| `modified_time` | `float` | Optional | - |
| `name` | `string` | Required | - |
| `org_id` | `uuid\|string` | Optional | - |

## Example (as JSON)

```json
{
  "applies": {
    "org_id": "00001bdc-0000-0000-0000-000000000000",
    "site_ids": [
      "00001706-0000-0000-0000-000000000000",
      "00001707-0000-0000-0000-000000000000",
      "00001708-0000-0000-0000-000000000000"
    ],
    "sitegroup_ids": [
      "00000634-0000-0000-0000-000000000000"
    ]
  },
  "created_time": 198.3,
  "deviceprofile_ids": [
    "00002429-0000-0000-0000-000000000000"
  ],
  "exceptions": {
    "site_ids": [
      "00001604-0000-0000-0000-000000000000",
      "00001603-0000-0000-0000-000000000000",
      "00001602-0000-0000-0000-000000000000"
    ],
    "sitegroup_ids": [
      "00000c2e-0000-0000-0000-000000000000"
    ]
  },
  "filter_by_deviceprofile": false,
  "name": "name0"
}
```

