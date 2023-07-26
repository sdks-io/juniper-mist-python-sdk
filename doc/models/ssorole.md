
# Ssorole

SSO Role response

## Structure

`Ssorole`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `created_time` | `float` | Optional | - |
| `for_site` | `bool` | Optional | - |
| `id` | `uuid\|string` | Optional | - |
| `modified_time` | `float` | Optional | - |
| `msp_id` | `uuid\|string` | Optional | - |
| `name` | `string` | Required | - |
| `org_id` | `uuid\|string` | Optional | - |
| `privileges` | [`List of Privileges`](../../doc/models/privileges.md) | Required | **Constraints**: *Minimum Items*: `1`, *Unique Items Required* |
| `site_id` | `uuid\|string` | Optional | - |

## Example (as JSON)

```json
{
  "name": "name0",
  "privileges": [
    {
      "for_site": false,
      "msp_id": "00002334-0000-0000-0000-000000000000",
      "msp_logo_url": "msp_logo_url6",
      "msp_name": "msp_name2",
      "msp_url": "msp_url8",
      "role": "helpdesk",
      "scope": "msp"
    }
  ],
  "created_time": 198.3,
  "for_site": false,
  "id": "00001770-0000-0000-0000-000000000000",
  "modified_time": 136.66,
  "msp_id": "0000156c-0000-0000-0000-000000000000"
}
```

