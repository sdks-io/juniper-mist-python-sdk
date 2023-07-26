
# Result

## Structure

`Result`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `application_health` | `float` | Optional | - |
| `gateway_health` | `float` | Optional | - |
| `num_clients` | `float` | Optional | - |
| `num_gateways` | `float` | Optional | - |
| `site_id` | `uuid\|string` | Required | - |
| `wan_link_health` | `float` | Optional | - |

## Example (as JSON)

```json
{
  "application-health": 25.62,
  "gateway-health": 117.2,
  "num_clients": 193.5,
  "num_gateways": 82.14,
  "site_id": "000007d6-0000-0000-0000-000000000000",
  "wan-link-health": 3.36
}
```

