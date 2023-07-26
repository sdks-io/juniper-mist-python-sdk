
# Site

Site

## Structure

`Site`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `address` | `string` | Optional | full address of the site |
| `alarmtemplate_id` | `uuid\|string` | Optional | Alarm Template ID, this takes precedence over the Org-level alarmtemplate_id |
| `aptemplate_id` | `string` | Optional | AP Template ID, used by APs |
| `country_code` | `string` | Optional | country code for the site (for AP config generation), in two-character |
| `created_time` | `float` | Optional | - |
| `gatewaytemplate_id` | `uuid\|string` | Optional | Gateway Template ID, used by gateways |
| `id` | `uuid\|string` | Optional | - |
| `latlng` | [`Latlng1`](../../doc/models/latlng-1.md) | Optional | site location |
| `modified_time` | `float` | Optional | - |
| `name` | `string` | Required | - |
| `networktemplate_id` | `uuid\|string` | Optional | Network Template ID, this takes precedence over Site Settings |
| `notes` | `string` | Optional | optional, any notes about the site |
| `org_id` | `uuid\|string` | Optional | - |
| `rftemplate_id` | `uuid\|string` | Optional | RF Template ID, this takes precedence over Site Settings |
| `secpolicy_id` | `uuid\|string` | Optional | SecPolicy ID |
| `sitegroup_ids` | `List of uuid\|string` | Optional | sitegroups this site belongs to |
| `sitetemplate_id` | `uuid\|string` | Optional | Site Template ID |
| `timezone` | `string` | Optional | Timezone the site is at |

## Example (as JSON)

```json
{
  "address": "1601 S. Deanza Blvd., Cupertino, CA, 95014",
  "alarmtemplate_id": "684dfc5c-fe77-2290-eb1d-ef3d677fe168",
  "aptemplate_id": "16bdf952-ade2-4491-80b0-85ce506c760b",
  "country_code": "US",
  "gatewaytemplate_id": "6f9b2e75-9b2f-b5ae-81e3-e14c76f1a90f",
  "name": "Mist Office",
  "networktemplate_id": "12ae9bd2-e0ab-107b-72e8-a7a005565ec2",
  "rftemplate_id": "bb8a9017-1e36-5d6c-6f2b-551abe8a76a2",
  "secpolicy_id": "3bcd0beb-5d0a-4cbd-92c1-14aea91e98ef",
  "timezone": "America/Los_Angeles",
  "created_time": 198.3
}
```

