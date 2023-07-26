
# Applies

where this template should be applied to, can be org_id, site_ids, sitegroup_ids

## Structure

`Applies`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `org_id` | `uuid\|string` | Optional | org id, should be the same as the org, this shadows sitegroup_ids and site_ids |
| `site_ids` | `List of uuid\|string` | Optional | list of site ids |
| `sitegroup_ids` | `List of uuid\|string` | Optional | list of sitegroup ids |

## Example (as JSON)

```json
{
  "org_id": "00000ec8-0000-0000-0000-000000000000",
  "site_ids": [
    "00001a9a-0000-0000-0000-000000000000",
    "00001a9b-0000-0000-0000-000000000000"
  ],
  "sitegroup_ids": [
    "000002a0-0000-0000-0000-000000000000",
    "000002a1-0000-0000-0000-000000000000"
  ]
}
```

