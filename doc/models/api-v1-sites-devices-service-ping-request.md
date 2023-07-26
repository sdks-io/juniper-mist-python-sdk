
# Api V1 Sites Devices Service Ping Request

## Structure

`ApiV1SitesDevicesServicePingRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `count` | `int` | Optional | **Default**: `10` |
| `host` | `string` | Required | - |
| `service` | `string` | Required | ping packet takes the same path as the service |
| `size` | `int` | Optional | **Default**: `56`<br>**Constraints**: `>= 56`, `<= 65535` |
| `tenant` | `string` | Optional | tenant context in which the packet is sent |

## Example (as JSON)

```json
{
  "count": 10,
  "host": "host8",
  "service": "service0",
  "size": 56,
  "tenant": "tenant4"
}
```

