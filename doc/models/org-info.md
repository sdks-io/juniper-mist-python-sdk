
# Org Info

## Structure

`OrgInfo`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `alarmtemplate_id` | `uuid\|string` | Optional | - |
| `allow_mist` | `bool` | Optional | **Default**: `True` |
| `created_time` | `float` | Optional | - |
| `id` | `uuid\|string` | Required | - |
| `modified_time` | `float` | Optional | - |
| `msp_id` | `uuid\|string` | Optional | - |
| `msp_logo_url` | `string` | Optional | logo uploaded by the MSP with advanced tier, only present if provided |
| `msp_name` | `string` | Optional | name of the msp the org belongs to |
| `name` | `string` | Required | - |
| `orggroup_ids` | `List of uuid\|string` | Optional | - |
| `session_expiry` | `float` | Optional | **Default**: `1440` |

## Example (as JSON)

```json
{
  "allow_mist": true,
  "created_time": 1652905706.0,
  "id": "2818e386-8dec-2562-9ede-5b8a0fbbdc71",
  "modified_time": 1652905706.0,
  "msp_id": "b9d42c2e-88ee-41f8-b798-f009ce7fe909",
  "msp_logo_url": "https://.../logo/b9d42c2e-88ee-41f8-b798-f009ce7fe909.jpeg",
  "msp_name": "MSP",
  "name": "Org",
  "session_expiry": 1440,
  "alarmtemplate_id": "00001a0e-0000-0000-0000-000000000000"
}
```

