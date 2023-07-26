
# Api V1 Sites Devices Show Service Path Request

The exact service name for which to display the service path

## Structure

`ApiV1SitesDevicesShowServicePathRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `node` | [`NodeEnum`](../../doc/models/node-enum.md) | Optional | only for HA |
| `service_name` | `string` | Optional | - |

## Example (as JSON)

```json
{
  "service_name": "any",
  "node": "node0"
}
```

