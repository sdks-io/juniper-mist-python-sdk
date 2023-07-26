
# Api V1 Installer Orgs Sites Response

## Structure

`ApiV1InstallerOrgsSitesResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `address` | `string` | Required | - |
| `country_code` | `string` | Required | - |
| `id` | `uuid\|string` | Required | - |
| `latlng` | [`Latlng2`](../../doc/models/latlng-2.md) | Required | - |
| `name` | `string` | Required | - |
| `timezone` | `string` | Required | - |

## Example (as JSON)

```json
{
  "address": "address6",
  "country_code": "country_code0",
  "id": "00001770-0000-0000-0000-000000000000",
  "latlng": {
    "lat": 144.64,
    "lng": 22.82
  },
  "name": "name0",
  "timezone": "timezone0"
}
```

