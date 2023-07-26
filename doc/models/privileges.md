
# Privileges

Privilieges settings

## Structure

`Privileges`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `for_site` | `bool` | Optional | - |
| `msp_id` | `uuid\|string` | Optional | id of the MSP (if the org belongs to an MSP) |
| `msp_logo_url` | `string` | Optional | logo of the MSP (if the MSP belongs to an Advanced tier) |
| `msp_name` | `string` | Optional | name of the MSP (if the org belongs to an MSP) |
| `msp_url` | `string` | Optional | custom url of the MSP (if the MSP belongs to an Advanced tier) |
| `name` | `string` | Optional | name of the org/site/MSP depending on object scope |
| `org_id` | `uuid\|string` | Optional | id of the org |
| `org_name` | `string` | Optional | name of the org (for a site belonging to org) |
| `orggroup_ids` | `List of uuid\|string` | Optional | list of orggroup ids (if the org belongs to an MSP) |
| `role` | [`RoleEnum`](../../doc/models/role-enum.md) | Required | access permissions |
| `scope` | [`ScopeEnum`](../../doc/models/scope-enum.md) | Required | list of privileges the admin has on the MSP / OrgGroups / Orgs / Sites |
| `site_id` | `uuid\|string` | Optional | id of the site |
| `sitegroup_ids` | `List of uuid\|string` | Optional | list of sitegroup ids |
| `views` | `List of string` | Optional | Custom roles restrict Org users to specific UI views. This is useful for limiting UI access of Org users.<br><br>You can invite a new user or update existing users in your Org to this custom role. For this, specify view along with role when assigning privileges.<br><br>Below are the list of supported UI views. Note that this is UI only feature<br>Custom roles restrict Org users to specific UI views. This is useful for limiting UI access of Org users.<br><br>You can invite a new user or update existing users in your Org to this custom role. For this, specify `view` along with `role` when assigning privileges.<br><br>Below are the list of supported UI views. Note that this is UI only feature<br><br>\| UI View \| Description \|<br>\| --- \| --- \|<br>\| `reporting` \| full access to all analytics tools \|<br>\| `marketing` \| can view analytics and location maps \|<br>\| `location` \| can view and manage location maps \|<br>\| `security` \| can view and manage WLAN, rogues and authentication \|<br>\| `switch_admin` \| can view and manage Switch ports \|<br>\| `mxedge_admin` \| can view and manage Mist edges and Mist tunnels \|<br>\| `lobby_admin` \| full access to Org and Site Pre-shared keys \| |

## Example (as JSON)

```json
{
  "for_site": false,
  "msp_id": "0000156c-0000-0000-0000-000000000000",
  "msp_logo_url": "msp_logo_url8",
  "msp_name": "msp_name4",
  "msp_url": "msp_url0",
  "role": "write",
  "scope": "msp"
}
```

