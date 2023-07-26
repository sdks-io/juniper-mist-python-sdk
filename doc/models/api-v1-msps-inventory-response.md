
# Api V1 Msps Inventory Response

## Structure

`ApiV1MspsInventoryResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `for_site` | `bool` | Optional | - |
| `mac` | `string` | Required | - |
| `model` | `string` | Required | - |
| `org_id` | `uuid\|string` | Required | - |
| `serial` | `string` | Required | - |
| `site_id` | `uuid\|string` | Required | - |
| `mtype` | `string` | Required | - |

## Example (as JSON)

```json
{
  "for_site": false,
  "mac": "mac4",
  "model": "model2",
  "org_id": "00000ec8-0000-0000-0000-000000000000",
  "serial": "serial0",
  "site_id": "000007d6-0000-0000-0000-000000000000",
  "type": "type0"
}
```

